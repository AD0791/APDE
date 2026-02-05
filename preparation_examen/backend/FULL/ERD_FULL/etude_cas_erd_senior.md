# Étude de Cas ERD — Niveau Senior

## Guide de Préparation aux Examens : Architectures Complexes et Optimisation Avancée

---

Ce document senior vous prépare à concevoir des ERD pour des systèmes bancaires à grande échelle, avec des millions de transactions, des contraintes de haute disponibilité, et des besoins de performance extrêmes. Vous apprendrez à faire des compromis architecturaux justifiés.

---

## 🎯 Concepts d'architecture couverts

- Dénormalisation stratégique et trade-offs
- Partitionnement horizontal et vertical
- Réplication et stratégies de cohérence
- Event Sourcing et CQRS
- Sharding et distribution géographique
- Audit trail et conformité (SOX, GDPR)
- Temporal tables et time-travel queries

---

## Problème 1 : Dénormalisation Stratégique - Table de Reporting

### Contexte

Vous gérez 10 millions de transactions par jour. Le rapport quotidien suivant prend 45 secondes à générer :

```sql
SELECT 
    c.client_id,
    c.nom,
    COUNT(t.transaction_id) AS nb_transactions,
    SUM(CASE WHEN t.type_tx = 'DEPOT' THEN t.montant ELSE 0 END) AS total_depots,
    SUM(CASE WHEN t.type_tx = 'RETRAIT' THEN t.montant ELSE 0 END) AS total_retraits,
    SUM(co.solde) AS solde_total
FROM clients c
LEFT JOIN comptes co ON co.client_id = c.client_id
LEFT JOIN transactions t ON t.compte_id = co.compte_id
WHERE t.date_tx >= CURRENT_DATE - INTERVAL 30 DAYS
GROUP BY c.client_id, c.nom;
```

### Solution - Table dénormalisée avec mise à jour incrémentale

#### ERD Normalisé vs Dénormalisé

```
=== MODÈLE NORMALISÉ (actuel) ===

CLIENT ─┤├────○< COMPTE ─┤├────○< TRANSACTION
(3 JOINs pour chaque rapport)


=== MODÈLE DÉNORMALISÉ (optimisé) ===

CLIENT ─┤├────○< COMPTE ─┤├────○< TRANSACTION
   │
   │
   └────┤├──── STATS_CLIENT_30J  (table matérialisée, rafraîchie par trigger)
             ├─ client_id (PK, FK)
             ├─ nb_transactions
             ├─ total_depots
             ├─ total_retraits
             ├─ solde_total
             └─ date_maj
```

#### SQL - Table dénormalisée

```sql
CREATE TABLE stats_clients_30j (
    client_id       INT PRIMARY KEY,
    nb_transactions INT DEFAULT 0,
    total_depots    DECIMAL(15,2) DEFAULT 0,
    total_retraits  DECIMAL(15,2) DEFAULT 0,
    solde_total     DECIMAL(15,2) DEFAULT 0,
    date_maj        TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id)
);

-- Index pour requêtes de filtrage
CREATE INDEX idx_stats_depots ON stats_clients_30j(total_depots);
CREATE INDEX idx_stats_solde ON stats_clients_30j(solde_total);

-- Trigger de mise à jour incrémentale
DELIMITER $$
CREATE TRIGGER trg_maj_stats_transaction
AFTER INSERT ON transactions
FOR EACH ROW
BEGIN
    DECLARE v_client_id INT;
    
    -- Récupérer le client_id du compte
    SELECT client_id INTO v_client_id
    FROM comptes
    WHERE compte_id = NEW.compte_id;
    
    -- Mise à jour incrémentale des stats
    INSERT INTO stats_clients_30j (client_id, nb_transactions, total_depots, total_retraits)
    VALUES (
        v_client_id,
        1,
        IF(NEW.type_tx = 'DEPOT', NEW.montant, 0),
        IF(NEW.type_tx = 'RETRAIT', NEW.montant, 0)
    )
    ON DUPLICATE KEY UPDATE
        nb_transactions = nb_transactions + 1,
        total_depots = total_depots + IF(NEW.type_tx = 'DEPOT', NEW.montant, 0),
        total_retraits = total_retraits + IF(NEW.type_tx = 'RETRAIT', NEW.montant, 0);
END$$
DELIMITER ;

-- Job de recalcul quotidien (pour correction de dérives)
-- À exécuter via cron ou scheduler DB
TRUNCATE TABLE stats_clients_30j;
INSERT INTO stats_clients_30j (client_id, nb_transactions, total_depots, total_retraits, solde_total)
SELECT 
    c.client_id,
    COUNT(t.transaction_id),
    SUM(CASE WHEN t.type_tx = 'DEPOT' THEN t.montant ELSE 0 END),
    SUM(CASE WHEN t.type_tx = 'RETRAIT' THEN t.montant ELSE 0 END),
    SUM(co.solde)
FROM clients c
LEFT JOIN comptes co ON co.client_id = c.client_id
LEFT JOIN transactions t ON t.compte_id = co.compte_id AND t.date_tx >= CURRENT_DATE - INTERVAL 30 DAYS
GROUP BY c.client_id;
```

#### Trade-offs

| Aspect | Avant (3NF pur) | Après (Dénormalisé) |
|--------|-----------------|---------------------|
| **Performance lecture** | 45s (JOINs lourds) | < 100ms (lecture directe) |
| **Performance écriture** | Rapide (INSERT simple) | Légèrement plus lent (trigger) |
| **Stockage** | Optimal | +2-5% (table stats) |
| **Risque d'incohérence** | Zéro | Faible (job de correction) |
| **Complexité** | Simple | Moyenne (triggers, jobs) |

**Règle d'or** : Dénormaliser uniquement si le ratio lecture/écriture > 100:1 et la performance est critique.

---

## Problème 2 : Partitionnement Horizontal - Transactions par Date

### Contexte

La table `transactions` contient 500 millions de lignes. Les requêtes récentes sont rapides, mais les recherches historiques sont lentes. 90% des requêtes concernent les 3 derniers mois.

### Solution - Partitionnement par RANGE sur date_transaction

```
┌─────────────────────────────────────────────────┐
│             TRANSACTION (logique)               │
├─────────────────────────────────────────────────┤
│ PK transaction_id                               │
│ FK compte_id                                    │
│    date_transaction [PARTITION KEY]             │
│    montant                                      │
└─────────────────────────────────────────────────┘
         │
         │ (Partitionnement physique)
         │
    ┌────┴──────────┬──────────────┬──────────────┐
    │               │              │              │
┌───▼────────┐ ┌───▼────────┐ ┌──▼─────────┐ ┌──▼────────────┐
│ tx_2024_01 │ │ tx_2024_02 │ │ tx_2024_03 │ │ tx_2024_04... │
└────────────┘ └────────────┘ └────────────┘ └───────────────┘
(Janvier)      (Février)      (Mars)         (Archives)
```

### SQL - Partitionnement MySQL

```sql
CREATE TABLE transactions (
    transaction_id      BIGINT AUTO_INCREMENT,
    compte_id           INT NOT NULL,
    type_tx             VARCHAR(10) NOT NULL,
    montant             DECIMAL(12,2) NOT NULL,
    date_transaction    DATE NOT NULL,
    description         TEXT,
    INDEX idx_compte (compte_id),
    INDEX idx_date (date_transaction),
    PRIMARY KEY (transaction_id, date_transaction)
)
PARTITION BY RANGE (YEAR(date_transaction) * 100 + MONTH(date_transaction)) (
    PARTITION p_2024_01 VALUES LESS THAN (202402),
    PARTITION p_2024_02 VALUES LESS THAN (202403),
    PARTITION p_2024_03 VALUES LESS THAN (202404),
    PARTITION p_2024_04 VALUES LESS THAN (202405),
    PARTITION p_2024_05 VALUES LESS THAN (202406),
    PARTITION p_2024_06 VALUES LESS THAN (202407),
    PARTITION p_2024_07 VALUES LESS THAN (202408),
    PARTITION p_2024_08 VALUES LESS THAN (202409),
    PARTITION p_2024_09 VALUES LESS THAN (202410),
    PARTITION p_2024_10 VALUES LESS THAN (202411),
    PARTITION p_2024_11 VALUES LESS THAN (202412),
    PARTITION p_2024_12 VALUES LESS THAN (202501),
    PARTITION p_future VALUES LESS THAN MAXVALUE
);

-- Ajouter une partition pour le mois prochain (à automatiser)
ALTER TABLE transactions REORGANIZE PARTITION p_future INTO (
    PARTITION p_2025_01 VALUES LESS THAN (202502),
    PARTITION p_future VALUES LESS THAN MAXVALUE
);

-- Archiver et supprimer les anciennes partitions
ALTER TABLE transactions DROP PARTITION p_2024_01;
```

### Avantages du partitionnement

✅ **Performance** : Requêtes sur 3 derniers mois = scan de 3 partitions seulement  
✅ **Maintenance** : Archivage/suppression rapide (DROP PARTITION au lieu de DELETE)  
✅ **Scalabilité** : Partitions peuvent être sur des disques physiques différents  

### Requête optimisée automatiquement

```sql
-- Cette requête scanne UNIQUEMENT la partition p_2024_03
SELECT * FROM transactions
WHERE date_transaction BETWEEN '2024-03-01' AND '2024-03-31'
AND compte_id = 1234;

EXPLAIN PARTITIONS SELECT ...;
-- Résultat : partitions: p_2024_03 (1 seule partition scannée)
```

---

## Problème 3 : Event Sourcing - Audit Trail Immuable

### Contexte

Dans le secteur bancaire, vous DEVEZ conserver un **audit trail immuable** de toutes les opérations pour conformité réglementaire (SOX, PCI-DSS). Le problème : les UPDATE/DELETE effacent l'historique.

### Solution - Event Sourcing Pattern

```
=== MODÈLE TRADITIONNEL (ÉTAT ACTUEL) ===

COMPTE (état mutable)
├─ compte_id
├─ solde (modifié par UPDATE)
└─ statut (modifié par UPDATE)


=== MODÈLE EVENT SOURCING (ÉVÉNEMENTS IMMUABLES) ===

COMPTE_EVENTS (append-only, jamais de UPDATE/DELETE)
├─ event_id (PK, auto-increment)
├─ compte_id
├─ event_type (COMPTE_CREE, DEPOT, RETRAIT, BLOQUE, FERME)
├─ montant
├─ solde_apres_event
├─ metadata (JSON)
├─ timestamp
└─ user_id

COMPTE_SNAPSHOTS (état reconstitué périodiquement)
├─ compte_id (PK)
├─ solde_actuel
├─ statut
├─ version (numéro du dernier event appliqué)
└─ date_maj
```

### ERD Event Sourcing

```
┌────────────────────────┐
│   COMPTE_SNAPSHOTS     │ ← État actuel (lecture rapide)
├────────────────────────┤
│ PK compte_id           │─┤├────○<─┐
│    solde_actuel        │         │
│    statut              │         │
│    version             │         │
│    date_maj            │         │
└────────────────────────┘         │
                                   │
                       ┌───────────┴────────────────────┐
                       │   COMPTE_EVENTS (append-only)  │
                       ├────────────────────────────────┤
                       │ PK event_id                    │
                       │ FK compte_id                   │
                       │    event_type                  │
                       │    montant                     │
                       │    solde_apres                 │
                       │    metadata (JSON)             │
                       │    timestamp                   │
                       │    user_id                     │
                       └────────────────────────────────┘
                       PARTITION BY RANGE(timestamp)
```

### SQL

```sql
-- Table des événements (immuable)
CREATE TABLE compte_events (
    event_id        BIGINT PRIMARY KEY AUTO_INCREMENT,
    compte_id       INT NOT NULL,
    event_type      VARCHAR(30) NOT NULL,
    montant         DECIMAL(12,2),
    solde_apres     DECIMAL(12,2) NOT NULL,
    metadata        JSON,
    timestamp       TIMESTAMP(6) DEFAULT CURRENT_TIMESTAMP(6),
    user_id         INT NOT NULL,
    INDEX idx_compte_ts (compte_id, timestamp),
    INDEX idx_timestamp (timestamp)
) PARTITION BY RANGE (UNIX_TIMESTAMP(timestamp)) (
    -- Partitionnement par mois comme précédemment
);

-- Table snapshot (état actuel)
CREATE TABLE compte_snapshots (
    compte_id       INT PRIMARY KEY,
    solde_actuel    DECIMAL(12,2) NOT NULL,
    statut          VARCHAR(20) NOT NULL,
    version         BIGINT NOT NULL,  -- Dernier event_id appliqué
    date_maj        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (compte_id) REFERENCES comptes(compte_id)
);

-- Procédure pour créer un événement
DELIMITER $$
CREATE PROCEDURE enregistrer_depot(
    IN p_compte_id INT,
    IN p_montant DECIMAL(12,2),
    IN p_user_id INT
)
BEGIN
    DECLARE v_solde_actuel DECIMAL(12,2);
    DECLARE v_nouveau_solde DECIMAL(12,2);
    DECLARE v_event_id BIGINT;
    
    START TRANSACTION;
    
    -- Récupérer solde actuel avec verrou
    SELECT solde_actuel INTO v_solde_actuel
    FROM compte_snapshots
    WHERE compte_id = p_compte_id
    FOR UPDATE;
    
    SET v_nouveau_solde = v_solde_actuel + p_montant;
    
    -- Créer l'événement (JAMAIS de UPDATE sur cette table)
    INSERT INTO compte_events (compte_id, event_type, montant, solde_apres, user_id)
    VALUES (p_compte_id, 'DEPOT', p_montant, v_nouveau_solde, p_user_id);
    
    SET v_event_id = LAST_INSERT_ID();
    
    -- Mettre à jour le snapshot
    UPDATE compte_snapshots
    SET solde_actuel = v_nouveau_solde,
        version = v_event_id,
        date_maj = CURRENT_TIMESTAMP
    WHERE compte_id = p_compte_id;
    
    COMMIT;
END$$
DELIMITER ;
```

### Requêtes avancées

```sql
-- 1. État actuel (lecture du snapshot)
SELECT compte_id, solde_actuel, statut
FROM compte_snapshots
WHERE compte_id = 1234;

-- 2. Historique complet d'un compte
SELECT event_id, event_type, montant, solde_apres, timestamp
FROM compte_events
WHERE compte_id = 1234
ORDER BY event_id;

-- 3. Time-travel query : Quel était le solde le 15 mars 2024 à 14:30 ?
SELECT solde_apres
FROM compte_events
WHERE compte_id = 1234
  AND timestamp <= '2024-03-15 14:30:00'
ORDER BY timestamp DESC
LIMIT 1;

-- 4. Audit : Qui a modifié ce compte dans les 7 derniers jours ?
SELECT e.event_type, e.montant, e.timestamp, u.nom AS utilisateur
FROM compte_events e
JOIN users u ON u.user_id = e.user_id
WHERE e.compte_id = 1234
  AND e.timestamp >= CURRENT_TIMESTAMP - INTERVAL 7 DAY
ORDER BY e.timestamp DESC;
```

### Avantages Event Sourcing

✅ **Audit trail parfait** : Tout est tracé, rien n'est perdu  
✅ **Time-travel** : Reconstruire l'état à n'importe quel moment  
✅ **Debugging** : Rejouer les événements pour reproduire bugs  
✅ **Conformité** : SOX, GDPR, PCI-DSS automatiquement satisfaits  
✅ **Analytics** : Analyser les patterns comportementaux  

❌ **Complexité** : Courbe d'apprentissage élevée  
❌ **Stockage** : Croissance continue (nécessite archivage)  

---

## Problème 4 : CQRS - Séparation Lecture/Écriture

### Contexte

Votre système bancaire a :
- **Transactions** : 50 000/sec en écriture (haute cohérence requise)
- **Consultations** : 500 000/sec en lecture (tolérance à 1-2 sec de latence)

Le modèle unique ne peut pas scaler.

### Solution - CQRS (Command Query Responsibility Segregation)

```
=== ARCHITECTURE TRADITIONNELLE ===

         ┌──────────────────┐
         │   APPLICATION    │
         └────────┬─────────┘
                  │
         ┌────────▼─────────┐
         │   BASE UNIQUE    │ ← Goulot d'étranglement
         │   (Lecture +     │
         │    Écriture)     │
         └──────────────────┘


=== ARCHITECTURE CQRS ===

         ┌──────────────────┐
         │   APPLICATION    │
         └───┬─────────┬────┘
             │         │
    Commands │         │ Queries
    (Write)  │         │ (Read)
             │         │
    ┌────────▼─┐     ┌─▼─────────────┐
    │ WRITE DB │────>│  READ DB      │ ← Réplication async
    │ (Master) │     │  (Replicas)   │    (1-2 sec lag)
    │          │     │  - Replica 1  │
    │ Normalisé│     │  - Replica 2  │
    │ ACID     │     │  - Replica 3  │
    │          │     │  Dénormalisé  │
    └──────────┘     └───────────────┘
```

### ERD - Modèles Séparés

#### Write Model (Base maître - Normalisée)

```
CLIENT ─┤├───○< COMPTE ─┤├───○< TRANSACTION
(3NF strict, contraintes ACID, triggers)
```

#### Read Model (Replicas - Dénormalisé)

```
┌──────────────────────────────────────┐
│   VUE_COMPTE_ENRICHI (matérialisée)  │
├──────────────────────────────────────┤
│ compte_id                            │
│ client_nom                           │ ← Dénormalisé
│ client_email                         │ ← Dénormalisé
│ solde_actuel                         │
│ nb_transactions_30j                  │ ← Précalculé
│ derniere_transaction_date            │ ← Précalculé
│ statut_compte                        │
└──────────────────────────────────────┘

Index sur TOUT (read-optimized)
```

### SQL - Configuration CQRS

```sql
-- ===== BASE WRITE (MASTER) =====
CREATE TABLE transactions (
    transaction_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    compte_id INT NOT NULL,
    type_tx VARCHAR(10) NOT NULL,
    montant DECIMAL(12,2) NOT NULL,
    date_tx TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (compte_id) REFERENCES comptes(compte_id)
) ENGINE=InnoDB;  -- ACID strict

-- ===== BASE READ (REPLICA) =====
-- Configurée avec réplication MySQL maître-esclave

-- Vue matérialisée pour lectures (refresh toutes les 2 secondes)
CREATE TABLE vue_comptes_enrichis (
    compte_id INT PRIMARY KEY,
    client_nom VARCHAR(100),
    client_email VARCHAR(120),
    solde_actuel DECIMAL(12,2),
    nb_transactions_30j INT,
    derniere_transaction_date TIMESTAMP,
    statut VARCHAR(20),
    date_maj TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_client_nom (client_nom),
    INDEX idx_email (client_email),
    INDEX idx_solde (solde_actuel),
    INDEX idx_statut (statut)
) ENGINE=InnoDB;

-- Job de refresh (toutes les 2 secondes via cron ou scheduler)
TRUNCATE TABLE vue_comptes_enrichis;
INSERT INTO vue_comptes_enrichis
SELECT 
    co.compte_id,
    cl.nom,
    cl.email,
    co.solde,
    (SELECT COUNT(*) FROM transactions t 
     WHERE t.compte_id = co.compte_id 
     AND t.date_tx >= CURRENT_TIMESTAMP - INTERVAL 30 DAY) AS nb_tx_30j,
    (SELECT MAX(date_tx) FROM transactions t WHERE t.compte_id = co.compte_id) AS derniere_tx,
    co.statut
FROM comptes co
JOIN clients cl ON cl.client_id = co.client_id;
```

### Code Application - Séparation des responsabilités

```python
# ===== COMMANDES (ÉCRITURE) =====
class DepotCommand:
    def execute(self, compte_id, montant):
        with write_db.transaction():  # Connexion MASTER
            compte = write_db.query("SELECT * FROM comptes WHERE compte_id = %s FOR UPDATE", compte_id)
            if not compte:
                raise ComptInexistant()
            
            write_db.execute("""
                INSERT INTO transactions (compte_id, type_tx, montant)
                VALUES (%s, 'DEPOT', %s)
            """, compte_id, montant)
            
            write_db.execute("""
                UPDATE comptes SET solde = solde + %s WHERE compte_id = %s
            """, montant, compte_id)
        # Pas de retour de données (Command pattern)

# ===== REQUÊTES (LECTURE) =====
class CompteQueryService:
    def get_compte_details(self, compte_id):
        # Connexion REPLICA (lecture seule)
        return read_db.query_one("""
            SELECT * FROM vue_comptes_enrichis
            WHERE compte_id = %s
        """, compte_id)
    
    def search_comptes_by_client(self, nom_partiel):
        # Index optimisé sur read replica
        return read_db.query("""
            SELECT * FROM vue_comptes_enrichis
            WHERE client_nom LIKE %s
            ORDER BY solde_actuel DESC
            LIMIT 100
        """, f"%{nom_partiel}%")
```

### Trade-offs CQRS

| Aspect | Avantage | Inconvénient |
|--------|----------|--------------|
| **Performance** | Lectures 10-100x plus rapides | Cohérence éventuelle (lag 1-2s) |
| **Scalabilité** | Replicas indépendants | Complexité opérationnelle |
| **Coût** | Efficace (scaling horizontal) | Plus de serveurs |
| **Maintenance** | Optimisations indépendantes | Double modèle à maintenir |

---

## Problème 5 : Sharding Géographique - Banque Multi-Pays

### Contexte

Votre banque opère dans 5 pays. Les clients français ne consultent jamais les comptes haïtiens, et vice-versa. La latence réseau cross-continent tue les performances.

### Solution - Sharding par pays (geo-sharding)

```
=== ARCHITECTURE SHARDÉE ===

┌─────────────────────────────────────────────────────┐
│            GLOBAL ROUTING LAYER                     │
│  (Détermine le shard basé sur client_id)           │
└──────┬──────────┬──────────┬──────────┬────────────┘
       │          │          │          │
   ┌───▼───┐  ┌──▼────┐  ┌──▼────┐  ┌──▼──────┐
   │SHARD  │  │SHARD  │  │SHARD  │  │ SHARD   │
   │FRANCE │  │HAITI  │  │CANADA │  │ USA     │
   │(Paris)│  │(P-a-P)│  │(MTL)  │  │(NYC)    │
   └───────┘  └───────┘  └───────┘  └─────────┘
   
   Chaque shard contient TOUTES les tables pour un sous-ensemble de clients
```

### ERD avec Shard Key

```
┌────────────────────────────────┐
│          CLIENT                │
├────────────────────────────────┤
│ PK client_id [SHARD KEY]       │ ← Détermine le shard
│    pays_code (FR/HT/CA/US)     │ ← Dénormalisé pour routing
│    nom                         │
│    email                       │
└────────────────────────────────┘

Règle de sharding : 
- client_id % 4 = 0 → SHARD_FRANCE
- client_id % 4 = 1 → SHARD_HAITI
- client_id % 4 = 2 → SHARD_CANADA
- client_id % 4 = 3 → SHARD_USA

(En production : sharding par pays_code plus logique)
```

### SQL - Configuration avec Vitess (ou similaire)

```sql
-- ===== SHARD FRANCE (DB shard_fr) =====
CREATE TABLE clients (
    client_id INT PRIMARY KEY,
    pays_code VARCHAR(2) NOT NULL DEFAULT 'FR',
    nom VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE,
    CHECK (pays_code = 'FR')  -- Contrainte shard
);

CREATE TABLE comptes (
    compte_id INT PRIMARY KEY,
    client_id INT NOT NULL,
    solde DECIMAL(12,2),
    FOREIGN KEY (client_id) REFERENCES clients(client_id)
);

-- ===== SHARD HAITI (DB shard_ht) =====
CREATE TABLE clients (
    client_id INT PRIMARY KEY,
    pays_code VARCHAR(2) NOT NULL DEFAULT 'HT',
    nom VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE,
    CHECK (pays_code = 'HT')  -- Contrainte shard
);

CREATE TABLE comptes (
    compte_id INT PRIMARY KEY,
    client_id INT NOT NULL,
    solde DECIMAL(12,2),
    FOREIGN KEY (client_id) REFERENCES clients(client_id)
);

-- ... même structure pour CA et US
```

### Routing Logic (Application Layer)

```python
class ShardRouter:
    SHARDS = {
        'FR': 'mysql://shard-fr.bank.com:3306/bank_fr',
        'HT': 'mysql://shard-ht.bank.com:3306/bank_ht',
        'CA': 'mysql://shard-ca.bank.com:3306/bank_ca',
        'US': 'mysql://shard-us.bank.com:3306/bank_us',
    }
    
    def get_connection(self, client_id):
        """Détermine le shard à partir du client_id"""
        # Option 1 : Query de metadata (centralisée)
        pays = metadata_db.query_one("SELECT pays_code FROM client_routing WHERE client_id = %s", client_id)
        
        # Option 2 : Hash consistant
        # shard_index = hash(client_id) % 4
        
        return self.SHARDS[pays]
    
    def execute_query(self, client_id, query, params):
        conn = self.get_connection(client_id)
        return conn.execute(query, params)

# Usage
router = ShardRouter()
compte = router.execute_query(
    client_id=12345,
    query="SELECT * FROM comptes WHERE client_id = %s",
    params=[12345]
)
```

### Défis du Sharding

❌ **Cross-shard queries** : Impossible de faire un JOIN entre shards  
❌ **Transactions distribuées** : 2PC (Two-Phase Commit) lent et complexe  
❌ **Rebalancing** : Difficile de migrer des données entre shards  
❌ **Global uniqueness** : ID globaux nécessitent coordination (Snowflake ID)  

✅ **Performance** : Latence réduite (données proches géographiquement)  
✅ **Scalabilité** : Croissance linéaire  
✅ **Isolation** : Pannes isolées par pays  
✅ **Conformité** : GDPR (données UE restent en UE)  

---

## 📝 Checklist ERD - Niveau Senior

✅ **Dénormalisation**
- [ ] Trade-offs documentés (lecture vs écriture vs cohérence)
- [ ] Stratégie de synchronisation définie (triggers, jobs, messaging)
- [ ] Métriques de performance justifiant la dénormalisation

✅ **Partitionnement**
- [ ] Clé de partition choisie (date, ID, geo)
- [ ] Stratégie d'archivage des anciennes partitions
- [ ] Gestion automatisée des nouvelles partitions

✅ **Event Sourcing**
- [ ] Tous les événements métier identifiés
- [ ] Stratégie de snapshot définie (fréquence, retention)
- [ ] Requêtes time-travel documentées

✅ **CQRS**
- [ ] Séparation write/read justifiée (ratio lecture/écriture)
- [ ] Lag de réplication acceptable défini
- [ ] Vues matérialisées optimisées pour les queries fréquentes

✅ **Sharding**
- [ ] Shard key choisie (éviter les hot spots)
- [ ] Stratégie cross-shard documentée
- [ ] Plan de rebalancing défini

---

## 🎓 Conseils pour l'Examen - Niveau Senior

### Questions typiques d'architecture

**Q : "La table X contient 1 milliard de lignes et les requêtes sont lentes. Que faire ?"**

Réponse structurée :
1. **Diagnostiquer** : EXPLAIN, index manquants, requêtes inefficaces
2. **Optimiser** : Index, réécriture queries, vues matérialisées
3. **Partitionner** : Si données temporelles ou géographiques
4. **Sharding** : Si partitionnement insuffisant
5. **Dénormaliser** : Si ratio lecture/écriture très élevé

**Q : "Comment garantir l'audit trail complet dans un système bancaire ?"**

Réponse :
1. **Event Sourcing** : Pas de UPDATE/DELETE, uniquement INSERT
2. **Partition par date** : Immutabilité physique (partitions read-only)
3. **Triggers d'audit** : Table `audit_log` pour tout changement
4. **Replication** : Backup continu sur site distant

### Erreurs à éviter

- ❌ Dénormaliser sans justification chiffrée
- ❌ Sharding prématuré (complexité > bénéfice)
- ❌ Oublier les index sur les foreign keys dans tables dénormalisées
- ❌ Ne pas documenter les trade-offs

### Phrases clés pour impressionner

- "Dans ce contexte de **haute vélocité transactionnelle**, je propose un **CQRS pattern** avec réplication asynchrone."
- "Pour garantir l'**auditabilité réglementaire**, j'implémente un **event sourcing** avec snapshots quotidiens."
- "La **dénormalisation stratégique** de cette métrique justifie le trade-off cohérence éventuelle, vu le ratio 1000:1 lecture/écriture."
- "Le **sharding géographique** réduit la latence de 300ms à 20ms pour 95% des requêtes."

---

## 📚 Ressources Avancées

- **Books** : 
  - "Designing Data-Intensive Applications" (Martin Kleppmann)
  - "Database Internals" (Alex Petrov)
- **Patterns** : 
  - Event Sourcing (Greg Young)
  - CQRS (Martin Fowler)
- **Tools** :
  - Vitess (sharding MySQL)
  - Debezium (CDC - Change Data Capture)
  - TimescaleDB (time-series sur PostgreSQL)

---

**Félicitations !** Vous maîtrisez maintenant la modélisation ERD du niveau basique au senior. Pratiquez sur des cas réels et justifiez toujours vos choix architecturaux.
