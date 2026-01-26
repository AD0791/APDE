# Étude de Cas ERD — Niveau Moyen

## Guide de Préparation aux Examens : Modélisation Avancée et Optimisation

---

Ce document intermédiaire vous entraîne à concevoir des ERD complexes avec des relations plusieurs-à-plusieurs (M:N), des tables d'association, de l'héritage, et des stratégies d'optimisation. Vous apprendrez également à modéliser des contraintes métier avancées.

---

## 🎯 Concepts avancés couverts

- Relations M:N et tables de jonction
- Héritage (Généralisation/Spécialisation)
- Attributs dérivés et calculés
- Historisation temporelle
- Contraintes métier complexes
- Indexation stratégique

---

## Problème 1 : Relation M:N - Produits Financiers

### Énoncé

Une banque propose plusieurs **produits financiers** (prêt immobilier, prêt auto, carte de crédit premium, etc.). Un client peut souscrire à plusieurs produits, et un produit peut être souscrit par plusieurs clients.

**Entités :**
- **CLIENT** : client_id, nom, email, date_inscription
- **PRODUIT_FINANCIER** : produit_id, nom_produit, taux_interet, frais_mensuel
- Relation : Un client peut avoir 0 à N produits, un produit peut appartenir à 0 à N clients

### Solution - ERD avec table d'association

```
┌──────────────────┐                    ┌─────────────────────────┐
│     CLIENT       │                    │   PRODUIT_FINANCIER     │
├──────────────────┤                    ├─────────────────────────┤
│ PK client_id     │─○<────┐      ┌────○<─│ PK produit_id           │
│    nom           │       │      │    │    nom_produit          │
│    email         │       │      │    │    taux_interet         │
│    date_inscrip  │       │      │    │    frais_mensuel        │
└──────────────────┘       │      │    └─────────────────────────┘
                           │      │
                   ┌───────┴──────┴─────────┐
                   │   SOUSCRIPTION         │ ← Table d'association (jonction)
                   ├────────────────────────┤
                   │ PK,FK client_id        │
                   │ PK,FK produit_id       │
                   │       date_souscription│
                   │       statut           │
                   │       montant_accorde  │
                   └────────────────────────┘
                   Clé primaire composée (client_id, produit_id)
```

### Points clés

1. **Table d'association obligatoire** pour résoudre M:N
2. **Clé primaire composée** : (client_id, produit_id)
3. **Attributs de la relation** : date_souscription, statut, montant_accorde appartiennent à la SOUSCRIPTION, pas au CLIENT ni au PRODUIT

### SQL

```sql
CREATE TABLE clients (
    client_id       INT PRIMARY KEY,
    nom             VARCHAR(100) NOT NULL,
    email           VARCHAR(120) UNIQUE NOT NULL,
    date_inscription DATE NOT NULL
);

CREATE TABLE produits_financiers (
    produit_id      INT PRIMARY KEY,
    nom_produit     VARCHAR(100) NOT NULL,
    taux_interet    DECIMAL(5,2),  -- Ex: 3.50 pour 3.5%
    frais_mensuel   DECIMAL(8,2)
);

CREATE TABLE souscriptions (
    client_id           INT NOT NULL,
    produit_id          INT NOT NULL,
    date_souscription   DATE NOT NULL,
    statut              VARCHAR(20) DEFAULT 'ACTIF',
    montant_accorde     DECIMAL(12,2),
    PRIMARY KEY (client_id, produit_id),
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (produit_id) REFERENCES produits_financiers(produit_id)
);
```

### Requête exemple

```sql
-- Tous les produits d'un client
SELECT c.nom, p.nom_produit, s.date_souscription, s.statut
FROM clients c
JOIN souscriptions s ON s.client_id = c.client_id
JOIN produits_financiers p ON p.produit_id = s.produit_id
WHERE c.client_id = 1;
```

---

## Problème 2 : Héritage - Comptes Spécialisés

### Énoncé

Une banque gère différents types de comptes avec des attributs spécifiques :
- **Compte Courant** : découvert_autorise, frais_gestion
- **Compte Épargne** : taux_interet, plafond_depot
- **Compte Joint** : co_titulaire_id, type_gestion

Tous les comptes partagent : compte_id, numero_compte, solde, date_ouverture

### Stratégies de modélisation

#### Stratégie 1 : Table Unique (Single Table Inheritance)

```
┌────────────────────────────────────────┐
│            COMPTE                      │
├────────────────────────────────────────┤
│ PK compte_id                           │
│    numero_compte                       │
│    solde                               │
│    date_ouverture                      │
│    type_compte (DISCRIMINANT)          │ ← 'COURANT', 'EPARGNE', 'JOINT'
│    --- Attributs spécifiques ---       │
│    decouvert_autorise (nullable)       │ ← Seulement pour COURANT
│    frais_gestion (nullable)            │ ← Seulement pour COURANT
│    taux_interet (nullable)             │ ← Seulement pour EPARGNE
│    plafond_depot (nullable)            │ ← Seulement pour EPARGNE
│    co_titulaire_id (nullable)          │ ← Seulement pour JOINT
│    type_gestion (nullable)             │ ← Seulement pour JOINT
└────────────────────────────────────────┘

✅ Avantages : Simple, requêtes rapides, pas de JOIN
❌ Inconvénients : Beaucoup de colonnes NULL, moins normalisé
```

#### Stratégie 2 : Tables Séparées (Class Table Inheritance)

```
┌──────────────────────┐
│    COMPTE (parent)   │
├──────────────────────┤
│ PK compte_id         │
│    numero_compte     │
│    solde             │
│    date_ouverture    │
│    type_compte       │
└──────────────────────┘
         △
         │ (Héritage)
         ├───────────────┬───────────────┬──────────────┐
         │               │               │              │
┌────────┴─────────┐ ┌──┴────────────┐ ┌┴─────────────┐
│ COMPTE_COURANT   │ │ COMPTE_EPARGNE│ │ COMPTE_JOINT │
├──────────────────┤ ├───────────────┤ ├──────────────┤
│ PK,FK compte_id  │ │ PK,FK compte  │ │ PK,FK compte │
│ decouvert_auto   │ │ taux_interet  │ │ co_titulaire │
│ frais_gestion    │ │ plafond_depot │ │ type_gestion │
└──────────────────┘ └───────────────┘ └──────────────┘

✅ Avantages : Bien normalisé, pas de NULL, extensible
❌ Inconvénients : Requêtes avec JOIN, plus complexe
```

### SQL - Stratégie 2 (Recommandée)

```sql
-- Table parente
CREATE TABLE comptes (
    compte_id       INT PRIMARY KEY,
    numero_compte   VARCHAR(20) UNIQUE NOT NULL,
    solde           DECIMAL(12,2) NOT NULL,
    date_ouverture  DATE NOT NULL,
    type_compte     VARCHAR(10) NOT NULL CHECK (type_compte IN ('COURANT', 'EPARGNE', 'JOINT'))
);

-- Tables enfants
CREATE TABLE comptes_courants (
    compte_id           INT PRIMARY KEY,
    decouvert_autorise  DECIMAL(10,2) DEFAULT 0,
    frais_gestion       DECIMAL(6,2) DEFAULT 5.00,
    FOREIGN KEY (compte_id) REFERENCES comptes(compte_id) ON DELETE CASCADE
);

CREATE TABLE comptes_epargnes (
    compte_id       INT PRIMARY KEY,
    taux_interet    DECIMAL(5,2) NOT NULL,
    plafond_depot   DECIMAL(10,2),
    FOREIGN KEY (compte_id) REFERENCES comptes(compte_id) ON DELETE CASCADE
);

CREATE TABLE comptes_joints (
    compte_id       INT PRIMARY KEY,
    co_titulaire_id INT NOT NULL,
    type_gestion    VARCHAR(20) DEFAULT 'SOLIDAIRE',  -- SOLIDAIRE ou DISJOINT
    FOREIGN KEY (compte_id) REFERENCES comptes(compte_id) ON DELETE CASCADE
);
```

### Requête pour récupérer tous les comptes avec détails

```sql
-- Vue unifiée
CREATE VIEW v_tous_comptes AS
SELECT 
    c.compte_id,
    c.numero_compte,
    c.solde,
    c.type_compte,
    cc.decouvert_autorise,
    cc.frais_gestion,
    ce.taux_interet,
    ce.plafond_depot,
    cj.co_titulaire_id,
    cj.type_gestion
FROM comptes c
LEFT JOIN comptes_courants cc ON cc.compte_id = c.compte_id
LEFT JOIN comptes_epargnes ce ON ce.compte_id = c.compte_id
LEFT JOIN comptes_joints cj ON cj.compte_id = c.compte_id;
```

---

## Problème 3 : Historisation Temporelle

### Énoncé

La banque doit conserver l'**historique des soldes** pour audit et reporting. Chaque modification de solde doit être tracée.

### Solution - Table d'historique

```
┌──────────────────────┐
│       COMPTE         │
├──────────────────────┤
│ PK compte_id         │─┤├───────○<─┐
│    numero_compte     │            │
│    solde_actuel      │            │ (1:N)
│    date_maj          │            │
└──────────────────────┘            │
                        ┌───────────┴──────────────────┐
                        │   HISTORIQUE_SOLDE           │
                        ├──────────────────────────────┤
                        │ PK hist_id                   │
                        │ FK compte_id                 │
                        │    solde_avant               │
                        │    solde_apres               │
                        │    difference                │
                        │    date_modification         │
                        │    type_operation            │
                        │    utilisateur               │
                        └──────────────────────────────┘
```

### SQL avec Trigger automatique

```sql
CREATE TABLE comptes (
    compte_id       INT PRIMARY KEY,
    numero_compte   VARCHAR(20) UNIQUE NOT NULL,
    solde_actuel    DECIMAL(12,2) NOT NULL,
    date_maj        TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE historique_soldes (
    hist_id             INT PRIMARY KEY AUTO_INCREMENT,
    compte_id           INT NOT NULL,
    solde_avant         DECIMAL(12,2) NOT NULL,
    solde_apres         DECIMAL(12,2) NOT NULL,
    difference          DECIMAL(12,2) NOT NULL,
    date_modification   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    type_operation      VARCHAR(20),
    utilisateur         VARCHAR(50),
    FOREIGN KEY (compte_id) REFERENCES comptes(compte_id)
);

-- Trigger automatique
CREATE TRIGGER trg_historiser_solde
AFTER UPDATE ON comptes
FOR EACH ROW
BEGIN
    IF OLD.solde_actuel <> NEW.solde_actuel THEN
        INSERT INTO historique_soldes 
        (compte_id, solde_avant, solde_apres, difference, type_operation)
        VALUES 
        (NEW.compte_id, OLD.solde_actuel, NEW.solde_actuel, 
         NEW.solde_actuel - OLD.solde_actuel, 'MODIFICATION');
    END IF;
END;
```

---

## Problème 4 : Attributs Dérivés et Calculés

### Énoncé

Certains attributs peuvent être **calculés** à partir d'autres données :
- `age_compte` = différence entre aujourd'hui et `date_ouverture`
- `solde_total_client` = somme des soldes de tous ses comptes
- `nombre_transactions` = count des transactions

**Question** : Faut-il les stocker dans l'ERD ?

### Règle de conception

```
┌──────────────────────┐
│       COMPTE         │
├──────────────────────┤
│ PK compte_id         │
│    solde             │
│    date_ouverture    │
│ /  age_compte /      │ ← Notation ERD : "/" = attribut dérivé (ne PAS stocker)
└──────────────────────┘
```

### Décision : Stocker ou Calculer ?

| Critère | Stocker | Calculer à la volée |
|---------|---------|---------------------|
| **Fréquence de lecture** | Très élevée | Occasionnelle |
| **Coût de calcul** | Élevé (agrégations, JOIN complexes) | Faible (DATE, arithmétique simple) |
| **Risque d'incohérence** | Oui (dénormalisation) | Non |
| **Exemple** | `solde_total_client` | `age_compte` |

### SQL - Vue pour attributs calculés

```sql
-- Vue avec attributs dérivés
CREATE VIEW v_comptes_enrichis AS
SELECT 
    c.compte_id,
    c.numero_compte,
    c.solde,
    c.date_ouverture,
    TIMESTAMPDIFF(YEAR, c.date_ouverture, CURDATE()) AS age_compte_annees,
    (SELECT COUNT(*) FROM transactions t WHERE t.compte_id = c.compte_id) AS nombre_transactions,
    (SELECT SUM(montant) FROM transactions t WHERE t.compte_id = c.compte_id AND type_tx = 'DEPOT') AS total_depots
FROM comptes c;
```

---

## Problème 5 : Contraintes Métier Complexes

### Énoncé

Modéliser les règles suivantes dans l'ERD et le SQL :

1. **Un client mineur** (< 18 ans) ne peut avoir qu'un compte épargne
2. **Le solde d'un compte courant** ne peut descendre sous -decouvert_autorise
3. **Les virements** entre comptes doivent être atomiques (débit = crédit)

### Solution

#### Règle 1 : Contrainte CHECK avec sous-requête

```sql
-- Ajouter date_naissance aux clients
ALTER TABLE clients 
ADD COLUMN date_naissance DATE NOT NULL;

-- Contrainte sur les comptes
ALTER TABLE comptes
ADD CONSTRAINT chk_mineur_epargne_only
CHECK (
    type_compte = 'EPARGNE' 
    OR client_id NOT IN (
        SELECT client_id FROM clients 
        WHERE TIMESTAMPDIFF(YEAR, date_naissance, CURDATE()) < 18
    )
);
```

#### Règle 2 : Contrainte avec jointure (nécessite trigger)

```sql
-- Trigger avant mise à jour
CREATE TRIGGER trg_verifier_decouvert
BEFORE UPDATE ON comptes
FOR EACH ROW
BEGIN
    DECLARE limite DECIMAL(12,2);
    
    -- Récupérer le découvert autorisé si compte courant
    IF NEW.type_compte = 'COURANT' THEN
        SELECT COALESCE(-decouvert_autorise, 0) INTO limite
        FROM comptes_courants
        WHERE compte_id = NEW.compte_id;
        
        IF NEW.solde < limite THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Découvert dépassé';
        END IF;
    END IF;
END;
```

#### Règle 3 : Transaction ACID pour virements

```sql
-- Table pour les virements
CREATE TABLE virements (
    virement_id         INT PRIMARY KEY AUTO_INCREMENT,
    compte_source_id    INT NOT NULL,
    compte_dest_id      INT NOT NULL,
    montant             DECIMAL(12,2) NOT NULL,
    date_virement       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    statut              VARCHAR(20) DEFAULT 'EN_COURS',
    FOREIGN KEY (compte_source_id) REFERENCES comptes(compte_id),
    FOREIGN KEY (compte_dest_id) REFERENCES comptes(compte_id),
    CHECK (montant > 0),
    CHECK (compte_source_id <> compte_dest_id)
);

-- Procédure stockée atomique
DELIMITER $$
CREATE PROCEDURE effectuer_virement(
    IN p_source INT,
    IN p_dest INT,
    IN p_montant DECIMAL(12,2)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Virement échoué';
    END;
    
    START TRANSACTION;
    
    -- Débiter le compte source
    UPDATE comptes SET solde = solde - p_montant WHERE compte_id = p_source;
    
    -- Créditer le compte destination
    UPDATE comptes SET solde = solde + p_montant WHERE compte_id = p_dest;
    
    -- Enregistrer le virement
    INSERT INTO virements (compte_source_id, compte_dest_id, montant, statut)
    VALUES (p_source, p_dest, p_montant, 'COMPLETE');
    
    COMMIT;
END$$
DELIMITER ;
```

---

## Problème 6 : Indexation Stratégique dans l'ERD

### Énoncé

Identifier les colonnes à indexer pour ces requêtes fréquentes :

1. Rechercher un client par email
2. Lister les transactions d'un compte par date décroissante
3. Trouver tous les comptes d'une succursale avec solde > X

### Solution - Annotations dans l'ERD

```
┌──────────────────────┐
│       CLIENT         │
├──────────────────────┤
│ PK client_id         │ ← Index automatique (PRIMARY KEY)
│    nom               │
│    email (UQ) [IDX]  │ ← Index UNIQUE automatique
│    date_inscrip      │
└──────────────────────┘

┌──────────────────────────┐
│      TRANSACTION         │
├──────────────────────────┤
│ PK transaction_id        │ ← Index automatique
│ FK compte_id [IDX]       │ ← Index composite recommandé
│    date_transaction [IDX]│ ← (compte_id, date_transaction)
│    montant               │
└──────────────────────────┘

┌──────────────────────┐
│       COMPTE         │
├──────────────────────┤
│ PK compte_id         │
│ FK succursale_id [IDX]│ ← Index composite
│    solde [IDX]       │ ← (succursale_id, solde)
└──────────────────────┘
```

### SQL

```sql
-- Index pour recherche par email (déjà créé par UNIQUE)
-- CREATE INDEX idx_client_email ON clients(email);

-- Index composite pour transactions par compte et date
CREATE INDEX idx_transaction_compte_date 
ON transactions(compte_id, date_transaction DESC);

-- Index composite pour comptes par succursale et solde
CREATE INDEX idx_compte_succursale_solde 
ON comptes(succursale_id, solde);

-- Requêtes optimisées
SELECT * FROM clients WHERE email = 'test@demo.ht';  -- Utilise idx_client_email
SELECT * FROM transactions WHERE compte_id = 100 ORDER BY date_transaction DESC;  -- Utilise idx_transaction_compte_date
SELECT * FROM comptes WHERE succursale_id = 5 AND solde > 10000;  -- Utilise idx_compte_succursale_solde
```

---

## 📝 Checklist ERD - Niveau Moyen

✅ **Relations avancées**
- [ ] Les relations M:N utilisent des tables d'association
- [ ] Les clés primaires composées sont bien identifiées
- [ ] Les attributs de relation sont dans la bonne table

✅ **Héritage**
- [ ] La stratégie d'héritage est justifiée (table unique vs tables séparées)
- [ ] Les attributs communs sont bien dans la table parente
- [ ] Les contraintes CASCADE sont définies si nécessaire

✅ **Performance**
- [ ] Les attributs dérivés sont identifiés (notation "/")
- [ ] Les index sont annotés dans l'ERD
- [ ] Les requêtes fréquentes sont anticipées

✅ **Contraintes métier**
- [ ] Les règles complexes sont documentées
- [ ] Les triggers nécessaires sont identifiés
- [ ] Les transactions ACID sont planifiées

---

## 🎓 Conseils pour l'Examen

### Quand utiliser une table d'association ?
- Dès que vous voyez une relation M:N
- Si la relation a des attributs propres (date, statut, etc.)

### Héritage : quelle stratégie ?
- **Table unique** : Si peu d'attributs spécifiques, requêtes simples
- **Tables séparées** : Si beaucoup d'attributs spécifiques, logique métier complexe

### Erreurs fréquentes :
- ❌ Oublier la table d'association pour M:N
- ❌ Mettre des attributs de relation dans les entités principales
- ❌ Sur-indexer (index = coût en écriture)
- ❌ Stocker des attributs dérivés sans justification

---

**Prochaine étape :** Étude de cas ERD Niveau Senior (Optimisation, dénormalisation, partitionnement, cas d'usage distribués)
