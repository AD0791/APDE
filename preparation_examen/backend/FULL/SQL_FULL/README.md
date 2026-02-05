# SQL FULL — Guide Complet de SQL et Bases de Données

## 📋 Vue d'Ensemble

Ce dossier contient des études de cas complètes sur SQL et la gestion de bases de données relationnelles, organisées par niveau de complexité. Chaque étude présente des requêtes SQL pratiques avec des explications détaillées dans un contexte bancaire réel.

---

## 🎯 Structure des Études de Cas

### **Niveau Basique** (`etude_cas_sql_basique.md`)
**Durée estimée :** 2-3 heures  
**Prérequis :** Aucun (introduction complète)

**Concepts couverts :**
- **DDL (Data Definition Language)**
  - CREATE TABLE
  - ALTER TABLE
  - DROP TABLE
  - Contraintes (PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, CHECK)

- **DML (Data Manipulation Language)**
  - SELECT (projection, filtrage)
  - INSERT (simple et multiple)
  - UPDATE (avec WHERE)
  - DELETE (avec précautions)

- **Requêtes de base**
  - WHERE (filtres)
  - ORDER BY (tri)
  - LIMIT (pagination)
  - DISTINCT (valeurs uniques)

- **Jointures simples**
  - INNER JOIN
  - LEFT JOIN
  - Jointures multiples

- **Agrégations**
  - COUNT, SUM, AVG, MIN, MAX
  - GROUP BY
  - HAVING

**Projets pratiques :**
1. Création de schéma bancaire (clients, comptes, transactions)
2. Requêtes de lecture et filtrage
3. Jointures pour rapports combinés
4. Agrégations pour statistiques

**Compétences acquises :**
- ✅ Créer et modifier des tables
- ✅ Insérer et manipuler des données
- ✅ Écrire des requêtes SELECT complexes
- ✅ Effectuer des jointures
- ✅ Calculer des agrégations

---

### **Niveau Moyen** (`etude_cas_sql_moyen.md`)
**Durée estimée :** 3-4 heures  
**Prérequis :** Niveau basique + compréhension des jointures

**Concepts couverts :**
- **Sous-requêtes**
  - Sous-requêtes scalaires
  - Sous-requêtes corrélées
  - EXISTS / NOT EXISTS
  - IN / NOT IN

- **Fonctions SQL**
  - Fonctions de chaînes (CONCAT, SUBSTRING, UPPER, LOWER)
  - Fonctions de dates (DATE_ADD, DATEDIFF, EXTRACT)
  - Fonctions conditionnelles (CASE, COALESCE, NULLIF)

- **Window Functions**
  - ROW_NUMBER()
  - RANK() / DENSE_RANK()
  - PARTITION BY
  - Running totals avec SUM() OVER()

- **CTE (Common Table Expressions)**
  - WITH clause
  - Recursive CTEs

- **Optimisation**
  - Index (CREATE INDEX)
  - EXPLAIN / EXPLAIN ANALYZE
  - Query planning

**Projets pratiques :**
1. Rapports avec window functions
2. Analyses temporelles avec fonctions de dates
3. Requêtes récursives pour hiérarchies
4. Optimisation de requêtes lentes

**Compétences acquises :**
- ✅ Utiliser des sous-requêtes efficacement
- ✅ Maîtriser les window functions
- ✅ Créer des CTEs pour clarté
- ✅ Optimiser les performances
- ✅ Analyser les plans d'exécution

---

### **Niveau Senior** (`etude_cas_sql_senior.md`)
**Durée estimée :** 4-6 heures  
**Prérequis :** Niveau moyen + expérience en production

**Concepts couverts :**
- **Transactions ACID**
  - BEGIN / COMMIT / ROLLBACK
  - Niveaux d'isolation (READ COMMITTED, REPEATABLE READ, SERIALIZABLE)
  - Deadlocks et résolution

- **Procédures stockées et fonctions**
  - CREATE PROCEDURE
  - CREATE FUNCTION
  - Variables et contrôle de flux
  - Gestion d'erreurs (TRY/CATCH)

- **Triggers**
  - BEFORE / AFTER INSERT/UPDATE/DELETE
  - Audit automatique
  - Validation de données

- **Vues et vues matérialisées**
  - CREATE VIEW
  - CREATE MATERIALIZED VIEW
  - Refresh strategies

- **Sécurité et permissions**
  - GRANT / REVOKE
  - Roles et privilèges
  - Row-level security

- **Performance avancée**
  - Partitioning
  - Sharding
  - Replication
  - Query caching

**Projets pratiques :**
1. Système de transactions bancaires atomiques
2. Procédures pour calculs complexes
3. Triggers d'audit complet
4. Stratégie de partitioning pour scaling

**Compétences acquises :**
- ✅ Gérer des transactions complexes
- ✅ Créer des procédures stockées
- ✅ Implémenter l'audit automatique
- ✅ Sécuriser les bases de données
- ✅ Optimiser pour la production

---

## 📚 Hiérarchie des Commandes SQL

### DDL (Data Definition Language)
```sql
CREATE    → Créer des objets (tables, index, vues)
ALTER     → Modifier la structure
DROP      → Supprimer des objets
TRUNCATE  → Vider une table (plus rapide que DELETE)
```

### DML (Data Manipulation Language)
```sql
SELECT    → Lire des données
INSERT    → Ajouter des données
UPDATE    → Modifier des données
DELETE    → Supprimer des données
```

### DCL (Data Control Language)
```sql
GRANT     → Donner des permissions
REVOKE    → Retirer des permissions
```

### TCL (Transaction Control Language)
```sql
BEGIN     → Démarrer une transaction
COMMIT    → Valider une transaction
ROLLBACK  → Annuler une transaction
SAVEPOINT → Point de sauvegarde
```

---

## 🎓 Types de Jointures Expliqués

### INNER JOIN
**Usage :** Retourne uniquement les correspondances

```sql
SELECT c.nom, co.solde
FROM clients c
INNER JOIN comptes co ON c.client_id = co.client_id;
```

**Résultat :** Seulement les clients qui ont des comptes

---

### LEFT JOIN (LEFT OUTER JOIN)
**Usage :** Tous les enregistrements de gauche + correspondances de droite

```sql
SELECT c.nom, co.solde
FROM clients c
LEFT JOIN comptes co ON c.client_id = co.client_id;
```

**Résultat :** Tous les clients, NULL si pas de compte

---

### RIGHT JOIN (RIGHT OUTER JOIN)
**Usage :** Tous les enregistrements de droite + correspondances de gauche

```sql
SELECT c.nom, co.solde
FROM clients c
RIGHT JOIN comptes co ON c.client_id = co.client_id;
```

**Résultat :** Tous les comptes, NULL si client supprimé

---

### FULL OUTER JOIN
**Usage :** Tous les enregistrements des deux côtés

```sql
SELECT c.nom, co.solde
FROM clients c
FULL OUTER JOIN comptes co ON c.client_id = co.client_id;
```

**Résultat :** Tous les clients ET tous les comptes

---

### CROSS JOIN
**Usage :** Produit cartésien (toutes les combinaisons)

```sql
SELECT p.nom, s.ville
FROM produits p
CROSS JOIN succursales s;
```

**Attention :** Peut générer énormément de lignes!

---

## 💡 Patterns SQL Essentiels

### 1. Pagination

```sql
-- PostgreSQL / MySQL
SELECT * FROM transactions
ORDER BY date_tx DESC
LIMIT 20 OFFSET 40;  -- Page 3 (20 par page)

-- SQL Server
SELECT * FROM transactions
ORDER BY date_tx DESC
OFFSET 40 ROWS
FETCH NEXT 20 ROWS ONLY;
```

---

### 2. Top N par Groupe

```sql
-- Avec Window Function
WITH RankedTransactions AS (
    SELECT 
        compte_id,
        montant,
        date_tx,
        ROW_NUMBER() OVER (
            PARTITION BY compte_id 
            ORDER BY montant DESC
        ) as rn
    FROM transactions
)
SELECT compte_id, montant, date_tx
FROM RankedTransactions
WHERE rn <= 5;  -- Top 5 par compte
```

---

### 3. Running Total (Somme Cumulative)

```sql
SELECT 
    date_tx,
    montant,
    SUM(montant) OVER (
        ORDER BY date_tx
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) as solde_cumule
FROM transactions
WHERE compte_id = 123
ORDER BY date_tx;
```

---

### 4. Détection de Doublons

```sql
-- Trouver les doublons
SELECT email, COUNT(*) as count
FROM clients
GROUP BY email
HAVING COUNT(*) > 1;

-- Supprimer les doublons (garder le plus ancien)
DELETE FROM clients
WHERE client_id NOT IN (
    SELECT MIN(client_id)
    FROM clients
    GROUP BY email
);
```

---

### 5. Upsert (Insert ou Update)

```sql
-- PostgreSQL
INSERT INTO comptes (compte_id, solde)
VALUES (123, 5000)
ON CONFLICT (compte_id)
DO UPDATE SET solde = EXCLUDED.solde;

-- MySQL
INSERT INTO comptes (compte_id, solde)
VALUES (123, 5000)
ON DUPLICATE KEY UPDATE solde = VALUES(solde);
```

---

## 🔍 Optimisation des Performances

### Index — Quand et Comment

**Créer des index pour :**
- ✅ Colonnes utilisées dans WHERE
- ✅ Colonnes de jointure (FK)
- ✅ Colonnes dans ORDER BY
- ✅ Colonnes dans GROUP BY

```sql
-- Index simple
CREATE INDEX idx_client_email ON clients(email);

-- Index composite
CREATE INDEX idx_compte_type_solde ON comptes(type_compte, solde);

-- Index unique
CREATE UNIQUE INDEX idx_compte_numero ON comptes(numero_compte);

-- Index partiel
CREATE INDEX idx_comptes_actifs ON comptes(client_id)
WHERE statut = 'ACTIF';
```

**⚠️ Attention :**
- Trop d'index ralentissent INSERT/UPDATE/DELETE
- Index consomment de l'espace disque
- Maintenez les index (REINDEX, ANALYZE)

---

### EXPLAIN — Analyser les Requêtes

```sql
EXPLAIN ANALYZE
SELECT c.nom, SUM(t.montant) as total
FROM clients c
JOIN comptes co ON c.client_id = co.client_id
JOIN transactions t ON t.compte_id = co.compte_id
WHERE t.date_tx >= '2024-01-01'
GROUP BY c.client_id, c.nom;
```

**Indicateurs importants :**
- `Seq Scan` → Scan complet (mauvais pour grandes tables)
- `Index Scan` → Utilise un index (bon)
- `Nested Loop` → Boucles imbriquées (peut être lent)
- `Hash Join` → Jointure par hash (efficace)
- `cost` → Estimation du coût

---

### Optimisations Courantes

```sql
-- ❌ Éviter SELECT *
SELECT * FROM transactions;  -- Mauvais

-- ✅ Sélectionner uniquement les colonnes nécessaires
SELECT transaction_id, montant, date_tx FROM transactions;  -- Bon

-- ❌ Éviter les fonctions dans WHERE
SELECT * FROM clients WHERE YEAR(date_inscription) = 2024;  -- Mauvais

-- ✅ Réécrire pour utiliser l'index
SELECT * FROM clients 
WHERE date_inscription >= '2024-01-01' 
AND date_inscription < '2025-01-01';  -- Bon

-- ❌ Éviter NOT IN avec NULL
SELECT * FROM clients WHERE client_id NOT IN (SELECT client_id FROM blacklist);

-- ✅ Utiliser NOT EXISTS
SELECT * FROM clients c
WHERE NOT EXISTS (SELECT 1 FROM blacklist b WHERE b.client_id = c.client_id);
```

---

## 📖 Transactions ACID

### Propriétés ACID

**Atomicity (Atomicité)**
- Transaction complète ou annulée
- Pas d'état intermédiaire

**Consistency (Cohérence)**
- Respecte toutes les contraintes
- État valide avant et après

**Isolation**
- Transactions concurrentes isolées
- Pas d'interférence

**Durability (Durabilité)**
- Modifications persistantes
- Résiste aux pannes

---

### Exemple de Transaction Bancaire

```sql
BEGIN TRANSACTION;

-- Vérifier le solde
SELECT solde INTO @solde_source
FROM comptes
WHERE compte_id = 100
FOR UPDATE;  -- Verrouillage

-- Validation
IF @solde_source < 500 THEN
    ROLLBACK;
    SELECT 'Solde insuffisant' as message;
ELSE
    -- Débit
    UPDATE comptes
    SET solde = solde - 500
    WHERE compte_id = 100;
    
    -- Crédit
    UPDATE comptes
    SET solde = solde + 500
    WHERE compte_id = 200;
    
    -- Enregistrer la transaction
    INSERT INTO transactions (compte_id, type_tx, montant, date_tx)
    VALUES 
        (100, 'DEBIT', 500, NOW()),
        (200, 'CREDIT', 500, NOW());
    
    COMMIT;
    SELECT 'Virement réussi' as message;
END IF;
```

---

### Niveaux d'Isolation

```sql
-- READ UNCOMMITTED (le plus permissif)
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
-- Peut lire des données non commitées (dirty reads)

-- READ COMMITTED (par défaut dans PostgreSQL)
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
-- Lit uniquement les données commitées

-- REPEATABLE READ (par défaut dans MySQL)
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
-- Mêmes données relues donnent même résultat

-- SERIALIZABLE (le plus strict)
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
-- Transactions s'exécutent comme si séquentielles
```

---

## 🛠️ Configuration et Outils

### Installer PostgreSQL

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install postgresql postgresql-contrib

# Démarrer le service
sudo systemctl start postgresql

# Se connecter
sudo -u postgres psql

# Créer une base de données
CREATE DATABASE banque;
```

---

### Installer MySQL

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install mysql-server

# Sécuriser l'installation
sudo mysql_secure_installation

# Se connecter
sudo mysql -u root -p

# Créer une base de données
CREATE DATABASE banque CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

---

### Outils GUI

**pgAdmin** (PostgreSQL)
```bash
sudo apt install pgadmin4
```

**MySQL Workbench** (MySQL)
```bash
sudo apt install mysql-workbench
```

**DBeaver** (Multi-DB)
- Télécharger depuis https://dbeaver.io/

---

## 🎯 Objectifs d'Apprentissage

### Niveau Basique ✅
Après ce niveau, vous devriez pouvoir :
- [ ] Créer un schéma de base de données complet
- [ ] Écrire des requêtes SELECT avec filtres et tri
- [ ] Effectuer des jointures INNER et LEFT
- [ ] Calculer des agrégations avec GROUP BY
- [ ] Comprendre les contraintes d'intégrité

### Niveau Moyen ✅
Après ce niveau, vous devriez pouvoir :
- [ ] Utiliser des sous-requêtes efficacement
- [ ] Maîtriser les window functions
- [ ] Créer des CTEs pour requêtes complexes
- [ ] Optimiser avec des index
- [ ] Analyser les plans d'exécution

### Niveau Senior ✅
Après ce niveau, vous devriez pouvoir :
- [ ] Gérer des transactions ACID
- [ ] Créer des procédures stockées
- [ ] Implémenter des triggers d'audit
- [ ] Sécuriser avec GRANT/REVOKE
- [ ] Optimiser pour la production (partitioning, replication)

---

## 📚 Ressources Complémentaires

### Livres
- **"SQL Performance Explained"** — Markus Winand
- **"SQL Antipatterns"** — Bill Karwin
- **"High Performance MySQL"** — Baron Schwartz

### Sites Web
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [MySQL Reference Manual](https://dev.mysql.com/doc/)
- [SQL Tutorial - W3Schools](https://www.w3schools.com/sql/)
- [Use The Index, Luke!](https://use-the-index-luke.com/)

### Pratique
- [SQLZoo](https://sqlzoo.net/) — Tutoriels interactifs
- [LeetCode Database](https://leetcode.com/problemset/database/) — Problèmes SQL
- [HackerRank SQL](https://www.hackerrank.com/domains/sql)

---

## 💼 Applications en Contexte Bancaire

### Gestion de Comptes
```sql
-- Solde total par client
SELECT c.nom, SUM(co.solde) as total
FROM clients c
JOIN comptes co ON c.client_id = co.client_id
GROUP BY c.client_id, c.nom;

-- Comptes inactifs (pas de transaction depuis 6 mois)
SELECT co.compte_id, co.numero_compte
FROM comptes co
WHERE NOT EXISTS (
    SELECT 1 FROM transactions t
    WHERE t.compte_id = co.compte_id
    AND t.date_tx > NOW() - INTERVAL '6 months'
);
```

### Analyse de Transactions
```sql
-- Transactions suspectes (montant > 10000)
SELECT 
    t.transaction_id,
    c.nom,
    t.montant,
    t.date_tx
FROM transactions t
JOIN comptes co ON t.compte_id = co.compte_id
JOIN clients c ON co.client_id = c.client_id
WHERE t.montant > 10000
ORDER BY t.date_tx DESC;

-- Moyenne mobile sur 7 jours
SELECT 
    date_tx,
    montant,
    AVG(montant) OVER (
        ORDER BY date_tx
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) as avg_7j
FROM transactions;
```

### Reporting
```sql
-- Rapport mensuel par type de compte
SELECT 
    DATE_TRUNC('month', t.date_tx) as mois,
    co.type_compte,
    COUNT(*) as nb_transactions,
    SUM(t.montant) as total
FROM transactions t
JOIN comptes co ON t.compte_id = co.compte_id
GROUP BY DATE_TRUNC('month', t.date_tx), co.type_compte
ORDER BY mois DESC, type_compte;
```

---

## 🚀 Prochaines Étapes

Après avoir maîtrisé SQL :

1. **Pratiquez quotidiennement** — Résolvez des problèmes sur LeetCode/HackerRank
2. **Étudiez les NoSQL** — MongoDB, Redis pour comparaison
3. **Apprenez l'administration** — Backup, restore, monitoring
4. **Explorez le Big Data** — Spark SQL, Hive
5. **Maîtrisez les ORMs** — SQLAlchemy (Python), Hibernate (Java)

---

**Dernière mise à jour :** Janvier 2026

**Bon apprentissage de SQL !** 🗄️
