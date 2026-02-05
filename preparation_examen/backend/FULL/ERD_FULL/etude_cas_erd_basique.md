# Étude de Cas ERD — Niveau Basique

## Guide de Préparation aux Examens : Modélisation de Bases de Données avec ERD

---

Ce document vous prépare à concevoir des diagrammes Entité-Association (ERD - Entity-Relationship Diagram), un format de modélisation visuel utilisé pour représenter la structure des bases de données avant leur implémentation en SQL. C'est l'équivalent d'un blueprint architectural pour vos bases de données.

---

## 📌 Qu'est-ce qu'un ERD ?

Un **ERD (Entity-Relationship Diagram)** ou **Modèle Entité-Association** est un diagramme qui représente :

- **Entités** : Les "tables" ou objets du monde réel (Client, Compte, Transaction)
- **Attributs** : Les propriétés de chaque entité (nom, email, solde)
- **Relations** : Les liens entre les entités (un Client possède plusieurs Comptes)
- **Cardinalités** : Le nombre d'instances impliquées dans une relation (1:1, 1:N, M:N)

**Pourquoi c'est important dans le secteur bancaire ?**
- Communiquer la structure de la BDD avec les équipes non-techniques
- Valider la conception avant l'implémentation SQL
- Identifier les problèmes de normalisation tôt dans le processus

---

## 🎨 Notations ERD (Crow's Foot - La plus utilisée)

### Symboles de base

```
┌─────────────┐
│   ENTITE    │  ← Rectangle = Entité (Table)
├─────────────┤
│ PK id       │  ← PK = Primary Key (Clé primaire)
│    nom      │  ← Attributs normaux
│    email    │
│ FK autre_id │  ← FK = Foreign Key (Clé étrangère)
└─────────────┘
```

### Cardinalités (Notation Crow's Foot)

```
Zéro ou un        ─○|─
Exactement un     ─┤├─
Zéro ou plusieurs ─○<
Un ou plusieurs   ─┤<
```

### Exemples visuels

```
1:1 (Un à Un)
CLIENT ─┤├───────┤├─ PROFIL_CLIENT
Un client a exactement un profil

1:N (Un à Plusieurs)
CLIENT ─┤├───────○<─ COMPTE
Un client peut avoir zéro ou plusieurs comptes

M:N (Plusieurs à Plusieurs)
COMPTE ─○<───────○<─ PRODUIT_FINANCIER
Nécessite une table d'association (jonction)
```

---

## Problème 1 : ERD Simple - Système Bancaire de Base

### Énoncé

Vous devez concevoir un ERD pour un système bancaire simplifié avec :
- **Clients** : Identifiés par un ID, ont un nom, email, téléphone et date d'inscription
- **Comptes** : Appartiennent à UN client, ont un numéro de compte, type (COURANT/EPARGNE), solde, et date d'ouverture
- **Transactions** : Sont liées à UN compte, ont un type (DEPOT/RETRAIT), montant, et date

### Questions
1. Identifiez les entités et leurs attributs
2. Définissez les clés primaires et étrangères
3. Déterminez les relations et cardinalités

### Solution - Diagramme ERD

```
┌──────────────────┐
│     CLIENT       │
├──────────────────┤
│ PK client_id     │─┤├───────○<─┐
│    nom           │            │
│    email (UQ)    │            │
│    telephone     │            │
│    date_inscrip  │            │
└──────────────────┘            │
                                │
                    ┌───────────┴──────────┐
                    │       COMPTE         │
                    ├──────────────────────┤
                    │ PK compte_id         │─┤├───────○<─┐
                    │ FK client_id         │            │
                    │    numero_compte (UQ)│            │
                    │    type_compte       │            │
                    │    solde             │            │
                    │    date_ouverture    │            │
                    └──────────────────────┘            │
                                                        │
                                        ┌───────────────┴────────────┐
                                        │      TRANSACTION           │
                                        ├────────────────────────────┤
                                        │ PK transaction_id          │
                                        │ FK compte_id               │
                                        │    type_transaction        │
                                        │    montant                 │
                                        │    date_transaction        │
                                        │    description             │
                                        └────────────────────────────┘
```

### Relations expliquées

1. **CLIENT ─┤├───────○< COMPTE** (1:N)
   - Un client possède **zéro ou plusieurs** comptes
   - Un compte appartient à **exactement un** client
   - Clé étrangère : `compte.client_id` → `client.client_id`

2. **COMPTE ─┤├───────○< TRANSACTION** (1:N)
   - Un compte contient **zéro ou plusieurs** transactions
   - Une transaction appartient à **exactement un** compte
   - Clé étrangère : `transaction.compte_id` → `compte.compte_id`

### Traduction en SQL

```sql
CREATE TABLE clients (
    client_id      INT PRIMARY KEY,
    nom            VARCHAR(100) NOT NULL,
    email          VARCHAR(120) UNIQUE NOT NULL,
    telephone      VARCHAR(20),
    date_inscrip   DATE NOT NULL
);

CREATE TABLE comptes (
    compte_id      INT PRIMARY KEY,
    client_id      INT NOT NULL,
    numero_compte  VARCHAR(20) UNIQUE NOT NULL,
    type_compte    VARCHAR(10) NOT NULL CHECK (type_compte IN ('COURANT', 'EPARGNE')),
    solde          DECIMAL(12,2) NOT NULL DEFAULT 0,
    date_ouverture DATE NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(client_id)
);

CREATE TABLE transactions (
    transaction_id     INT PRIMARY KEY,
    compte_id          INT NOT NULL,
    type_transaction   VARCHAR(10) NOT NULL CHECK (type_transaction IN ('DEPOT', 'RETRAIT', 'VIREMENT')),
    montant            DECIMAL(12,2) NOT NULL,
    date_transaction   TIMESTAMP NOT NULL,
    description        TEXT,
    FOREIGN KEY (compte_id) REFERENCES comptes(compte_id)
);
```

---

## Problème 2 : Ajouter une Relation 1:1

### Énoncé

Le système doit maintenant gérer des **Cartes Bancaires**. Chaque compte peut avoir **au maximum une** carte active, et chaque carte est liée à **exactement un** compte.

### Solution - ERD mis à jour

```
┌──────────────────────┐
│       COMPTE         │
├──────────────────────┤
│ PK compte_id         │─┤├───────┤├─┐
│ FK client_id         │            │
│    numero_compte     │            │ Relation 1:1
│    solde             │            │
└──────────────────────┘            │
                                    │
                    ┌───────────────┴──────────┐
                    │    CARTE_BANCAIRE        │
                    ├──────────────────────────┤
                    │ PK carte_id              │
                    │ FK compte_id (UQ)        │
                    │    numero_carte          │
                    │    code_cvv              │
                    │    date_expiration       │
                    │    statut                │
                    └──────────────────────────┘
```

### Points clés

- La clé étrangère `carte_bancaire.compte_id` est marquée **UNIQUE** pour garantir la relation 1:1
- Notation : `─┤├───────┤├─` indique "exactement un" des deux côtés

### SQL

```sql
CREATE TABLE cartes_bancaires (
    carte_id        INT PRIMARY KEY,
    compte_id       INT UNIQUE NOT NULL,  -- UNIQUE force le 1:1
    numero_carte    VARCHAR(16) NOT NULL,
    code_cvv        VARCHAR(3) NOT NULL,
    date_expiration DATE NOT NULL,
    statut          VARCHAR(10) DEFAULT 'ACTIVE',
    FOREIGN KEY (compte_id) REFERENCES comptes(compte_id)
);
```

---

## Problème 3 : Identifier les Erreurs dans un ERD

### Énoncé

Voici un ERD avec des erreurs courantes. Identifiez les problèmes :

```
┌──────────────────┐
│     CLIENT       │
├──────────────────┤
│    nom           │  ← Pas de PK !
│    email         │
│    adresse       │  ← Violation 1NF si format "rue, ville, code postal"
└──────────────────┘
         │
         │ (relation non définie)
         ▼
┌──────────────────┐
│     COMPTE       │
├──────────────────┤
│ PK compte_id     │
│    solde         │
│    client_nom    │  ← Redondance ! Nom déjà dans CLIENT
└──────────────────┘
```

### Erreurs identifiées

1. **Entité CLIENT sans clé primaire**
   - Solution : Ajouter `PK client_id`

2. **Attribut "adresse" non atomique** (violation 1NF)
   - Solution : Séparer en `rue`, `ville`, `code_postal`
   - Ou créer une entité ADRESSE séparée

3. **Relation non définie entre CLIENT et COMPTE**
   - Solution : Ajouter `FK client_id` dans COMPTE et représenter la cardinalité

4. **Redondance : `client_nom` dans COMPTE**
   - Solution : Supprimer. Le nom est accessible via la relation (JOIN)

### ERD corrigé

```
┌──────────────────┐
│     CLIENT       │
├──────────────────┤
│ PK client_id     │─┤├───────○<─┐
│    nom           │            │
│    email         │            │
│    rue           │            │
│    ville         │            │
│    code_postal   │            │
└──────────────────┘            │
                    ┌───────────┴──────────┐
                    │       COMPTE         │
                    ├──────────────────────┤
                    │ PK compte_id         │
                    │ FK client_id         │
                    │    solde             │
                    └──────────────────────┘
```

---

## Problème 4 : Relation Réflexive

### Énoncé

Les clients peuvent **parrainer** d'autres clients. Un client peut avoir un parrain (ou aucun), et peut parrainer plusieurs autres clients.

### Solution - ERD avec auto-référence

```
┌──────────────────────┐
│       CLIENT         │
├──────────────────────┤
│ PK client_id         │─┤├───────○<─┐
│ FK parrain_id        │──────────────┘
│    nom               │    (Auto-référence)
│    email             │
└──────────────────────┘
```

### Explications

- La relation est de type **1:N sur elle-même**
- Un client (parrain) peut avoir plusieurs filleuls
- Un client (filleul) a zéro ou un parrain

### SQL

```sql
CREATE TABLE clients (
    client_id   INT PRIMARY KEY,
    parrain_id  INT NULL,  -- NULL = pas de parrain
    nom         VARCHAR(100) NOT NULL,
    email       VARCHAR(120) UNIQUE NOT NULL,
    FOREIGN KEY (parrain_id) REFERENCES clients(client_id)
);

-- Exemple de données
INSERT INTO clients VALUES (1, NULL, 'Alice', 'alice@demo.ht');      -- Pas de parrain
INSERT INTO clients VALUES (2, 1, 'Bob', 'bob@demo.ht');              -- Parrainé par Alice
INSERT INTO clients VALUES (3, 1, 'Charlie', 'charlie@demo.ht');     -- Parrainé par Alice
```

---

## Problème 5 : De l'ERD au SQL (Exercice complet)

### Énoncé

Créez l'ERD puis le code SQL pour un système de **Succursales bancaires** :
- Chaque **succursale** a un nom, adresse, et téléphone
- Chaque **employé** travaille dans UNE succursale et a un nom, poste, et salaire
- Chaque **client** est rattaché à UNE succursale

### Solution - ERD

```
┌──────────────────┐
│   SUCCURSALE     │
├──────────────────┤
│ PK succursale_id │─┤├───────○<─┐
│    nom           │            │
│    adresse       │            │
│    telephone     │            │
└──────────────────┘            │
         │                      │
         │                      │
         │─┤├───────○<─┐        │
                        │        │
          ┌─────────────┴──┐     │
          │    EMPLOYE     │     │
          ├────────────────┤     │
          │ PK employe_id  │     │
          │ FK succursale  │     │
          │    nom         │     │
          │    poste       │     │
          │    salaire     │     │
          └────────────────┘     │
                                 │
                    ┌────────────┴─────┐
                    │     CLIENT       │
                    ├──────────────────┤
                    │ PK client_id     │
                    │ FK succursale_id │
                    │    nom           │
                    │    email         │
                    └──────────────────┘
```

### SQL

```sql
CREATE TABLE succursales (
    succursale_id INT PRIMARY KEY,
    nom           VARCHAR(100) NOT NULL,
    adresse       VARCHAR(200) NOT NULL,
    telephone     VARCHAR(20)
);

CREATE TABLE employes (
    employe_id    INT PRIMARY KEY,
    succursale_id INT NOT NULL,
    nom           VARCHAR(100) NOT NULL,
    poste         VARCHAR(50) NOT NULL,
    salaire       DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (succursale_id) REFERENCES succursales(succursale_id)
);

CREATE TABLE clients (
    client_id     INT PRIMARY KEY,
    succursale_id INT NOT NULL,
    nom           VARCHAR(100) NOT NULL,
    email         VARCHAR(120) UNIQUE,
    FOREIGN KEY (succursale_id) REFERENCES succursales(succursale_id)
);
```

---

## 📝 Checklist ERD - Niveau Basique

Avant de valider votre ERD, vérifiez :

✅ **Entités**
- [ ] Chaque entité a un nom au singulier et en MAJUSCULES
- [ ] Chaque entité a une clé primaire (PK)
- [ ] Les attributs ont des types de données appropriés

✅ **Relations**
- [ ] Toutes les relations ont des cardinalités définies
- [ ] Les clés étrangères (FK) sont clairement identifiées
- [ ] La notation est cohérente (Crow's Foot recommandée)

✅ **Normalisation**
- [ ] Tous les attributs sont atomiques (1NF)
- [ ] Aucune redondance de données
- [ ] Les contraintes UNIQUE sont identifiées

✅ **Conversion SQL**
- [ ] Chaque entité = une table CREATE TABLE
- [ ] Chaque relation 1:N = une clé étrangère
- [ ] Les contraintes CHECK sont définies si nécessaire

---

## 🎓 Conseils pour l'Examen

### Pendant la conception ERD :
1. **Commencez par identifier les entités** (noms au singulier)
2. **Listez les attributs et types** pour chaque entité
3. **Identifiez les clés primaires** (ID auto-incrémenté recommandé)
4. **Dessinez les relations** avec les cardinalités
5. **Validez la normalisation** (1NF minimum)

### Pendant la conversion SQL :
1. **Une entité = une table**
2. **Une relation 1:N = une clé étrangère** dans la table "plusieurs"
3. **Une relation 1:1 = clé étrangère UNIQUE**
4. **Une relation M:N = table d'association** (voir niveau moyen)

### Erreurs fréquentes à éviter :
- ❌ Oublier les clés primaires
- ❌ Inverser les cardinalités (mettre la FK du mauvais côté)
- ❌ Dupliquer des données entre tables
- ❌ Utiliser des attributs multi-valués (violation 1NF)

---

## 📚 Ressources complémentaires

- Notation Crow's Foot : https://vertabelo.com/blog/crow-s-foot-notation/
- Outils en ligne pour dessiner des ERD : draw.io, Lucidchart, dbdiagram.io
- Pratiquer avec des cas réels : Système de bibliothèque, E-commerce, Hôpital

---

**Prochaine étape :** Étude de cas ERD Niveau Moyen (Relations M:N, tables d'association, héritage)
