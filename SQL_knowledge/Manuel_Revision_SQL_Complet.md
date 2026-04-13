# Manuel de Révision SQL et SGBDR — Méthode Pareto 80/20
### Cours : SQL & Systèmes de Gestion de Bases de Données Relationnelles
### Professeure : Soraya Ferdenache | SSMS (SQL Server Management Studio)

> **Philosophie Pareto :** Les sections PARTIE 1 couvrent ~80 % des points d'examen.
> Maîtrise-les parfaitement avant de passer à la PARTIE 2.

---

## TABLE DES MATIÈRES

**PARTIE 1 — L'ESSENTIEL ABSOLU (80 % des points)**
1. [SQL : Définition et Nature](#1-sql--définition-et-nature)
2. [Les 4 Familles de Commandes SQL](#2-les-4-familles-de-commandes-sql)
3. [Modélisation : MCD → MLD → MPD](#3-modélisation--mcd--mld--mpd)
4. [Normalisation : 1FN, 2FN, 3FN](#4-normalisation--1fn-2fn-3fn)
5. [DDL — Créer des Tables avec Contraintes](#5-ddl--créer-des-tables-avec-contraintes)
6. [DML — Manipuler les Données (INSERT, UPDATE, DELETE)](#6-dml--manipuler-les-données)
7. [SELECT — Interroger la Base de Données](#7-select--interroger-la-base-de-données)
8. [Les Transactions et ACID](#8-les-transactions-et-acid)

**PARTIE 2 — CONCEPTS SECONDAIRES (Pour le 100 %)**
9. [ALTER TABLE — Modifier la Structure](#9-alter-table--modifier-la-structure)
10. [Les Objets SQL : Séquences, Identity, Index](#10-les-objets-sql--séquences-identity-index)
11. [Ordre des Opérations en SGBD](#11-ordre-des-opérations-en-sgbd)
12. [Relations entre Tables (Cardinalités)](#12-relations-entre-tables-cardinalités)
13. [Algèbre Relationnelle](#13-algèbre-relationnelle)
14. [Pièges d'Examen et Questions VRAI/FAUX](#14-pièges-dexamen-et-questions-vraifaux)
15. [Exercices Pratiques Complets](#15-exercices-pratiques-complets)

---

# PARTIE 1 — L'ESSENTIEL ABSOLU

---

## 1. SQL : Définition et Nature

### Qu'est-ce que SQL ?

**SQL** = Structured Query Language (Langage de Requête Structuré)

```
┌─────────────────────────────────────────────────────────────────┐
│  SQL est un langage DÉCLARATIF (L4G — 4ème génération)          │
│                                                                  │
│  On dit CE QUE l'on veut  ─►  Le SGBD décide COMMENT le faire  │
│                                                                  │
│  CONTRAIRE de C, Java (impératif) : on dit étape par étape.     │
└─────────────────────────────────────────────────────────────────┘
```

> **MNÉMONIQUE — SQL vs Procédural :**
> SQL = **"Chef de restaurant"** : Tu commandes un steak, le chef décide de la cuisson.
> Java = **"Cuisiner soi-même"** : Tu fais chaque étape toi-même.

### Points clés sur SQL

| Propriété | Valeur | Explication |
|---|---|---|
| **Type de langage** | Déclaratif (NON procédural) | On dit quoi, pas comment |
| **Sensibilité à la casse** | Dépend de la **collation** | Par défaut SQL Server : NON sensible |
| **Norme** | ISO/ANSI SQL | Mais chaque SGBD a son dialecte |
| **Inventeur** | E.F. Codd (1970) | Basé sur la théorie des ensembles |
| **SGBD courants** | SQL Server, Oracle, MySQL, PostgreSQL | Tous utilisent SQL |

> **PIÈGE D'EXAMEN :**
> - "SQL est un langage procédural" → **FAUX** (déclaratif)
> - "Les noms d'objets ne sont jamais sensibles à la casse" → **Dépend de la collation** (par défaut FAUX)
> - "Les commandes SSMS (comme USE) sont exécutées au niveau du SGBD" → **VRAI**

---

## 2. Les 4 Familles de Commandes SQL

> **MNÉMONIQUE : "DMDT" = Dieu Mange Des Tartes**

```
╔══════════════════════════════════════════════════════════════════╗
║  D  DDL  Data Definition Language   → Définir la STRUCTURE      ║
║  M  DML  Data Manipulation Language → Manipuler les DONNÉES     ║
║  D  DCL  Data Control Language      → Contrôler la SÉCURITÉ     ║
║  T  TCL  Transaction Control Lang.  → Gérer les TRANSACTIONS    ║
╚══════════════════════════════════════════════════════════════════╝
```

### DDL — Data Definition Language (Structure)

```sql
CREATE    -- Créer un objet (table, index, vue, séquence)
ALTER     -- Modifier la structure d'un objet existant
DROP      -- Supprimer un objet définitivement
TRUNCATE  -- Vider une table (plus rapide que DELETE)
RENAME    -- Renommer un objet
```

> **Comportement ACID du DDL :** En SQL Server, les instructions DDL sont **auto-committées**.
> Un `ROLLBACK` n'a **AUCUN EFFET** sur un `CREATE TABLE`, `DROP TABLE`, `TRUNCATE`.

### DML — Data Manipulation Language (Données)

```sql
SELECT    -- Lire / Interroger des données
INSERT    -- Ajouter de nouveaux enregistrements
UPDATE    -- Modifier des enregistrements existants
DELETE    -- Supprimer des enregistrements (ligne par ligne)
```

> **Transactions et DML :** Les instructions DML sont regroupées en transactions.
> Un `ROLLBACK` **ANNULE** les opérations `INSERT`, `UPDATE`, `DELETE` non commitées.

### DCL — Data Control Language (Sécurité)

```sql
GRANT     -- Accorder des permissions à un utilisateur
REVOKE    -- Retirer des permissions à un utilisateur
```

### TCL — Transaction Control Language (Transactions)

```sql
BEGIN / BEGIN TRANSACTION  -- Démarrer une transaction
COMMIT                     -- Valider définitivement les changements
ROLLBACK                   -- Annuler tous les changements
SAVE TRAN nomPoint         -- Créer un point de sauvegarde partiel
```

### Résumé visuel des familles

```
┌─────────────────────────────────────────────────────────────────┐
│                     FAMILLES SQL                                 │
│                                                                  │
│  DDL ──► CREATE | ALTER | DROP | TRUNCATE                        │
│           └─► Modifie la STRUCTURE (schéma de la BD)            │
│                                                                  │
│  DML ──► SELECT | INSERT | UPDATE | DELETE                       │
│           └─► Modifie les DONNÉES (contenu des tables)          │
│                                                                  │
│  DCL ──► GRANT | REVOKE                                          │
│           └─► Gère les DROITS et PERMISSIONS                    │
│                                                                  │
│  TCL ──► COMMIT | ROLLBACK | SAVEPOINT                           │
│           └─► Gère la VALIDATION des transactions DML           │
└─────────────────────────────────────────────────────────────────┘
```

> **PIÈGE D'EXAMEN :**
> "Une transaction est composée d'une ou plusieurs instructions DDL" → **FAUX**
> Une transaction DML est composée d'instructions **DML**. Une instruction DDL constitue à elle seule une transaction (auto-commit).

---

## 3. Modélisation : MCD → MLD → MPD

### Vue d'ensemble du processus

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│    RÉALITÉ   │    │     MCD      │    │     MLD      │    │     MPD      │
│  du monde    │───►│  Conceptuel  │───►│   Logique    │───►│  Physique    │
│              │    │              │    │              │    │              │
│ Besoins      │    │ Entités +    │    │ Tables +     │    │ SQL CODE     │
│ utilisateur  │    │ Associations │    │ Clés         │    │ CREATE TABLE │
│              │    │ (MERISE/UML) │    │ Normalisation│    │              │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
                    Indépendant          Modèle              Dépendant
                    de tout SGBD         relationnel         du SGBD
```

### Étape 1 : Analyse des besoins
Comprendre et délimiter les besoins du client (questions, observations, documents).

### Étape 2 : MCD — Modèle Conceptuel de Données

```
MCD = Entités + Associations + Cardinalités

┌────────────────┐  1,N   ┌────────────────┐  N,M  ┌────────────────┐
│    ÉTUDIANT    │───────►│  INSCRIPTION   │◄──────│     COURS      │
│────────────────│        │────────────────│       │────────────────│
│ #idEtudiant   │        │ dateCours      │       │ #idCours       │
│  nom          │        │ numLocal       │       │  titre         │
│  adresse      │        └────────────────┘       │  duree         │
│  tel          │                                  │  categorie     │
└────────────────┘                                 └────────────────┘
```

**Vocabulaire MCD :**
- **Entité** : Une chose concrète ou abstraite (Etudiant, Cours, Produit...)
- **Association** : Lien sémantique entre entités (s'inscrit, commande, emploie...)
- **Cardinalité** : Nombre min et max de participations (0,1 / 1,1 / 0,N / 1,N)

### Étape 3 : MLD — Modèle Logique de Données

Le MLD transforme le MCD en tables avec clés. Notation textuelle :

```
Étudiants(#idEtudiant, nom, adresse, tel, courriel, formation)
Cours(#idCours, titre, duree, categorie)
Inscriptions(#idEtudiant, #idCours, dateCours, numlocal)
              └─FK───────┘  └─FK────┘
              └────── PK composée ───┘
```

> **Règle de transformation N:M :**
> Une relation N:M génère **toujours** une 3ème table (table de jonction)
> dont la PK est composée des FK des deux tables liées.

### Étape 4 : MPD — Modèle Physique de Données

Implémentation SQL concrète dans le SGBD choisi (SQL Server, Oracle...) :

```sql
CREATE TABLE Etudiant (
    idEtudiant INT IDENTITY(1,1) PRIMARY KEY,
    nom        NVARCHAR(50) NOT NULL,
    ...
);
```

---

## 4. Normalisation : 1FN, 2FN, 3FN

### Pourquoi normaliser ?

```
Sans normalisation                 Avec normalisation (3FN)
──────────────────                 ─────────────────────────
Redondances de données         →   Chaque info stockée 1 seule fois
Anomalies d'insertion          →   Aucune donnée "perdue" à l'insertion
Anomalies de modification      →   Modifier à un seul endroit
Anomalies de suppression       →   Supprimer sans perdre d'autres infos
```

> **MNÉMONIQUE des 3 FN : "L'Atome — Toute la clé — Rien que la clé"**

```
┌────────────────────────────────────────────────────────────────────┐
│   1FN : "L'Atome"                                                  │
│   ────────────────────────────────────────────────────────────     │
│   Règle : Chaque cellule contient UNE SEULE valeur (atomique).    │
│   Pas de listes, pas de groupes répétitifs.                        │
│                                                                    │
│   AVANT 1FN :                  APRÈS 1FN :                         │
│   ┌──────────┬─────────────┐   ┌──────────┬───────────┐           │
│   │ Produit  │ Fournisseurs│   │ Produit  │ Fournisseur│           │
│   ├──────────┼─────────────┤   ├──────────┼───────────┤           │
│   │ Télé     │ VIDÉO, HITEK│   │ Télé     │ VIDÉO SA  │           │
│   └──────────┴─────────────┘   ├──────────┼───────────┤           │
│   ← NON ATOMIQUE !              │ Télé     │ HITEK LTD │           │
│                                 └──────────┴───────────┘           │
└────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────┐
│   2FN : "Toute la clé"                                             │
│   ────────────────────────────────────────────────────────────     │
│   Règle : 1FN + Chaque attribut non-clé dépend de la TOTALITÉ    │
│           de la clé primaire (s'applique aux PK composées).        │
│                                                                    │
│   Avant 2FN (PK = idEtudiant + idCours) :                         │
│   ┌───────────┬─────────┬──────────────┬──────────────────┐       │
│   │idEtudiant │ idCours │ nomConseiller│ dateInscription  │       │
│   └───────────┴─────────┴──────────────┴──────────────────┘       │
│   nomConseiller dépend de idEtudiant SEULEMENT → problème !       │
│                                                                    │
│   Après 2FN : Séparer en 2 tables                                 │
│   Etudiant(idEtudiant, nom, idConseiller)                          │
│   Inscription(idEtudiant, idCours, dateInscription)                │
└────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────┐
│   3FN : "Rien que la clé"                                          │
│   ────────────────────────────────────────────────────────────     │
│   Règle : 2FN + Pas de dépendance TRANSITIVE.                     │
│           (A → B → C : si B n'est pas une clé, problème !)        │
│                                                                    │
│   Avant 3FN :                                                      │
│   Employé(idEmp, nom, idDept, nomDept)                             │
│   idEmp → idDept → nomDept  (dépendance transitive !)             │
│                                                                    │
│   Après 3FN :                                                      │
│   Employé(idEmp, nom, idDept)                                      │
│   Département(idDept, nomDept)                                     │
└────────────────────────────────────────────────────────────────────┘
```

### Résumé en une phrase

| Forme Normale | Condition |
|---|---|
| **1FN** | Valeurs atomiques (pas de listes, pas de répétitions) |
| **2FN** | 1FN + Dépend de TOUTE la clé primaire |
| **3FN** | 2FN + Dépend UNIQUEMENT de la clé (pas de dépendance transitive) |

---

## 5. DDL — Créer des Tables avec Contraintes

### 5.1 Règles de nommage des identifiants

```
┌──────────────────────────────────────────────────────────────────┐
│  Règles pour nommer tables, colonnes, contraintes...             │
│                                                                  │
│  ✓ Commence par une lettre ou _                                  │
│  ✓ Longueur max : 128 caractères                                 │
│  ✓ Caractères valides : A-Z, a-z, 0-9, _, @, #                  │
│  ✗ Ne doit PAS être un mot-clé SQL                              │
│  ✗ Deux objets ne peuvent pas avoir le même nom dans une BD     │
│                                                                  │
│  Identificateurs irréguliers (espaces, accents) :               │
│  → Doivent être entre [ ] ou " "   Ex: [mon tableau]            │
│  → Pratique NON recommandée                                     │
└──────────────────────────────────────────────────────────────────┘
```

### 5.2 Les Types de Données SQL Server

```
┌─────────────────────────────────────────────────────────────────┐
│  TYPES PRINCIPAUX SQL SERVER                                    │
│                                                                 │
│  Entiers    : INT, BIGINT, SMALLINT, TINYINT                    │
│  Décimaux   : DECIMAL(p,s), NUMERIC(p,s), FLOAT                │
│  Texte      : VARCHAR(n)    — chaîne variable ASCII             │
│               NVARCHAR(n)   — chaîne variable Unicode (accents)│
│               CHAR(n)       — chaîne fixe                       │
│  Date/Heure : DATE, DATETIME, DATETIME2                         │
│  Booléen    : BIT (0 ou 1)                                      │
│  Monétaire  : MONEY, SMALLMONEY                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 5.3 Les 5 Contraintes d'Intégrité

> **MNÉMONIQUE : P.F.U.N.C. = "Pour Faire Une Nouvelle Contrainte"**

```
╔═══════════════════════════════════════════════════════════════════╗
║  P  PRIMARY KEY  : Identifie chaque ligne de manière unique.    ║
║                    = NOT NULL + UNIQUE combinés.                ║
║                    Une seule PK par table (simple ou composée). ║
╠═══════════════════════════════════════════════════════════════════╣
║  F  FOREIGN KEY  : Lie deux tables (intégrité référentielle).   ║
║                    La valeur DOIT exister dans la table parent. ║
║                    Peut être NULL (optionnel par défaut).       ║
╠═══════════════════════════════════════════════════════════════════╣
║  U  UNIQUE       : Valeurs toutes différentes dans la colonne.  ║
║                    DIFFÉRENCE de PK : autorise les NULL.        ║
╠═══════════════════════════════════════════════════════════════════╣
║  N  NOT NULL     : La colonne NE PEUT PAS être vide.            ║
║                    Toujours définie au niveau COLONNE.          ║
╠═══════════════════════════════════════════════════════════════════╣
║  C  CHECK        : Valide une condition métier.                 ║
║                    Ex: CHECK (salaire > 0)                      ║
║                    Ex: CHECK (formation IN ('DEC','AEC'))       ║
╚═══════════════════════════════════════════════════════════════════╝
```

### 5.4 Syntaxe CREATE TABLE

**Exemple complet avec toutes les contraintes :**

```sql
-- Syntaxe générale
CREATE TABLE nomTable (
    colonne1  type  [DEFAULT valeur]  [contrainte_inline],
    colonne2  type  [DEFAULT valeur]  [contrainte_inline],
    ...
    [CONSTRAINT nomContrainte type_contrainte (colonnes)]
);

-- Exemple : Table Coureur
CREATE TABLE Coureur (
    -- PK simple — contrainte inline (au niveau colonne)
    idCoureur    INT
        CONSTRAINT coureur_idcoureur_pk PRIMARY KEY,

    -- NOT NULL — TOUJOURS inline
    nomCoureur   NVARCHAR(25)  NOT NULL,
    prenomCoureur NVARCHAR(25) NOT NULL,

    -- UNIQUE inline
    dossard      VARCHAR(10)
        CONSTRAINT coureur_dossard_u UNIQUE,

    -- DEFAULT
    sexeCoureur  CHAR(1)       DEFAULT 'M',

    -- CHECK inline
    ageCoureur   INT
        CONSTRAINT coureur_age_ck CHECK (ageCoureur >= 0 AND ageCoureur <= 120),

    -- FK inline
    idClub       INT
        CONSTRAINT fk_coureur_club REFERENCES Club(idClub)
);

-- Exemple : Table Resultat — PK composée (OBLIGATOIREMENT out-of-line)
CREATE TABLE Resultat (
    idCoureur   INT    NOT NULL,
    idCourse    INT    NOT NULL,
    dossard     VARCHAR(20),
    position    INT,

    -- PK composée : DOIT être au niveau TABLE
    CONSTRAINT pk_resultat
        PRIMARY KEY (idCoureur, idCourse),

    -- FK out-of-line
    CONSTRAINT fk_coureur_resultat
        FOREIGN KEY (idCoureur) REFERENCES Coureur(idCoureur),

    CONSTRAINT fk_course_resultat
        FOREIGN KEY (idCourse) REFERENCES Course(idCourse)
);
```

### 5.5 Aide-mémoire des niveaux de contrainte

```
┌─────────────────────────────────────────────────────────────────┐
│  NIVEAUX DE DÉFINITION DES CONTRAINTES                          │
│                                                                 │
│  COLONNE SEULEMENT (inline) :                                   │
│    → NOT NULL  (toujours inline)                               │
│                                                                 │
│  TABLE SEULEMENT (out-of-line) :                                │
│    → Toute contrainte impliquant 2+ colonnes de la même table  │
│    → PK composée, FK composée, CHECK multi-colonnes            │
│                                                                 │
│  COLONNE OU TABLE (selon le nombre de colonnes) :              │
│    → PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK                   │
│      (si 1 colonne : inline ou out-of-line)                    │
│      (si 2+ colonnes : out-of-line obligatoire)                │
└─────────────────────────────────────────────────────────────────┘
```

### 5.6 Nommage recommandé des contraintes

```
Convention : nomTable_nomColonne_typeContrainte

pk  → clé primaire        Ex: coureur_idcoureur_pk
fk  → clé étrangère       Ex: fk_coureur_club
u   → unique              Ex: coureur_dossard_u
ck  → check               Ex: coureur_age_ck
nn  → not null            (souvent pas nommée)
```

### 5.7 Clé Primaire vs Clé Unique

```
┌─────────────────────┬────────────────────────────────────────────┐
│      PRIMARY KEY    │               UNIQUE                        │
├─────────────────────┼────────────────────────────────────────────┤
│ NOT NULL garanti    │ NULL autorisé                              │
│ 1 seule par table   │ Plusieurs contraintes UNIQUE possibles     │
│ Identifie chaque    │ Garantit l'unicité d'une colonne non-clé  │
│ ligne               │ (ex: email, num sécu sociale...)           │
└─────────────────────┴────────────────────────────────────────────┘
```

### 5.8 Créer une table avec SELECT INTO (Copie)

```sql
-- Crée une nouvelle table à partir d'une requête SELECT
SELECT col1, col2, col3
INTO [NouvelleTable]
FROM [TableSource]
WHERE condition;
```

---

## 6. DML — Manipuler les Données

### 6.1 INSERT — Ajouter des données

```sql
-- Syntaxe 1 : Spécifier TOUTES les colonnes (dans l'ordre de la table)
INSERT INTO nomTable
VALUES (val1, val2, val3, ...);

-- Syntaxe 2 : Spécifier les colonnes souhaitées (RECOMMANDÉE)
INSERT INTO nomTable (col1, col2, col3)
VALUES (val1, val2, val3);

-- Bonne pratique : Toujours spécifier les colonnes !
```

**Exemples concrets :**

```sql
-- Insérer un département
INSERT INTO dept (deptno, dname, loc)
VALUES (50, 'FINANCE', 'MONTREAL');

-- Insérer avec valeur par défaut (omettre la colonne optionnelle)
INSERT INTO Etudiant (nom, adresse, tel, formation)
VALUES ('Tremblay', '123 Rue Main', '5141234567', 'DEC');
-- courriel est NULL car non spécifié et colonne nullable

-- Insérer avec une date spécifique
INSERT INTO emp (empno, ename, hiredate)
VALUES (9999, 'MARTIN', '2024-01-15');

-- Insérer avec la date du jour
INSERT INTO emp (empno, ename, hiredate)
VALUES (9999, 'MARTIN', getDate());
```

> **BONNE PRATIQUE :** Toujours utiliser la syntaxe avec liste de colonnes.
> Cela rend le code lisible et résistant aux modifications de la structure de la table.

### 6.2 UPDATE — Modifier des données

```sql
UPDATE nomTable
SET  colonne1 = valeur1,
     colonne2 = valeur2,
     ...
WHERE condition;
```

```sql
-- Transférer l'employé 7782 au département 20
UPDATE emp
SET    deptno = 20
WHERE  empno = 7782;

-- Augmenter le salaire de 10% pour les commis
UPDATE emp
SET    sal = sal * 1.10
WHERE  job = 'CLERK';

-- Modifier plusieurs colonnes à la fois
UPDATE emp
SET    sal  = 5000,
       job  = 'MANAGER',
       deptno = 10
WHERE  empno = 7839;
```

> **DANGER ABSOLU :**
> ```sql
> UPDATE emp SET sal = 0;   -- MODIFIE TOUTE LA TABLE !
> ```
> **Sans WHERE → Tous les enregistrements sont modifiés !**
> Toujours vérifier la clause WHERE avant d'exécuter un UPDATE.

### 6.3 DELETE — Supprimer des données

```sql
DELETE FROM nomTable
WHERE condition;
```

```sql
-- Supprimer l'employé 4444
DELETE FROM emp
WHERE empno = 4444;

-- Supprimer tous les cours qui ne se donnent plus
DELETE FROM Cours
WHERE statut = 'INACTIF';
```

> **DANGER ABSOLU :**
> ```sql
> DELETE FROM emp;   -- SUPPRIME TOUTE LA TABLE !
> ```
> **Sans WHERE → Tous les enregistrements sont supprimés !**

### 6.4 DELETE vs TRUNCATE

```
┌───────────────────────┬────────────────────────────────────────────┐
│       DELETE          │              TRUNCATE                       │
├───────────────────────┼────────────────────────────────────────────┤
│ Famille : DML         │ Famille : DDL                               │
│ Ligne par ligne       │ Tout d'un coup (beaucoup plus rapide)       │
│ Peut avoir WHERE      │ Pas de WHERE possible                       │
│ ROLLBACK possible     │ NON annulable (auto-commit en SQL Server)   │
│ Déclenche triggers    │ Ne déclenche pas les triggers (selon SGBD) │
│ Lent sur grandes      │ Ultra-rapide sur grandes tables             │
│ tables                │                                             │
└───────────────────────┴────────────────────────────────────────────┘
```

> **MNÉMONIQUE :** DELETE = Déménagement (on sort chaque meuble) | TRUNCATE = Bulldozer (tout d'un coup)

### 6.5 Violations de Contraintes d'Intégrité

```
┌─────────────────────────────────────────────────────────────────────┐
│  CAS 1 : Insérer une PK en double                                   │
│  INSERT INTO dept VALUES (10, 'TEST', 'MTL');  ← deptno=10 existe  │
│  → ERREUR : Violation de PRIMARY KEY                                │
│                                                                     │
│  CAS 2 : Insérer avec FK inexistante                                │
│  INSERT INTO emp (empno, deptno) VALUES (999, 99); ← dept 99=??    │
│  → ERREUR : Violation de FOREIGN KEY (dept 99 n'existe pas)         │
│                                                                     │
│  CAS 3 : Supprimer un parent ayant des enfants                      │
│  DELETE FROM dept WHERE deptno = 10;  ← emp a deptno=10            │
│  → ERREUR : Violation de FOREIGN KEY (employés référencent dept 10) │
│                                                                     │
│  CAS 4 : Modifier une PK référencée                                 │
│  UPDATE dept SET deptno = 33 WHERE deptno = 20; ← emp ref. dept 20 │
│  → ERREUR : Violation de FOREIGN KEY                                │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 7. SELECT — Interroger la Base de Données

### 7.1 Structure complète d'un SELECT

> **MNÉMONIQUE (Ordre d'ÉCRITURE) : "Sept Filles Web Gèrent Habilement Online"**

```
S - SELECT    → Colonnes à afficher
F - FROM      → Table(s) source
W - WHERE     → Filtrer les lignes
G - GROUP BY  → Regrouper
H - HAVING    → Filtrer les groupes
O - ORDER BY  → Trier
```

> **MNÉMONIQUE (Ordre d'EXÉCUTION interne par le SGBD) : "Fwd Who Gets Served Orders"**

```
┌─────────────────────────────────────────────────────────────────┐
│  ORDRE D'EXÉCUTION INTERNE DU SGBD (≠ Ordre d'écriture !)      │
│                                                                 │
│  1. FROM      → Charger les tables (et jointures)              │
│  2. WHERE     → Filtrer les lignes                             │
│  3. GROUP BY  → Créer les groupes                              │
│  4. HAVING    → Filtrer les groupes                            │
│  5. SELECT    → Projeter les colonnes                          │
│  6. ORDER BY  → Trier le résultat final                        │
└─────────────────────────────────────────────────────────────────┘
```

> **CONSÉQUENCE IMPORTANTE :**
> Le `WHERE` est exécuté **AVANT** le `SELECT`.
> Donc un alias défini dans SELECT **NE PEUT PAS** être utilisé dans WHERE !
> ```sql
> SELECT sal * 12 AS salAnnuel FROM emp WHERE salAnnuel > 30000;  -- ERREUR !
> SELECT sal * 12 AS salAnnuel FROM emp WHERE sal * 12 > 30000;   -- CORRECT
> ```
> Par contre, `ORDER BY` est exécuté **APRÈS** `SELECT` → alias autorisé dans ORDER BY.

### 7.2 SELECT de base

```sql
-- Tout afficher (déconseillé en production)
SELECT *
FROM emp;

-- Projection (choisir les colonnes)
SELECT dname, loc
FROM dept;

-- Expressions calculées (champs calculés)
SELECT ename, sal, sal * 12 AS "Salaire Annuel"
FROM emp;

-- DISTINCT — Éliminer les doublons
SELECT DISTINCT job
FROM emp;
```

### 7.3 Alias

```sql
-- Méthode 1 : avec AS
SELECT sal * 12 AS salAnnuel
FROM emp;

-- Méthode 2 : sans AS (espace suffit)
SELECT sal * 12 salAnnuel
FROM emp;

-- Méthode 3 : SQL Server spécifique
SELECT salAnnuel = sal * 12
FROM emp;

-- Alias avec espaces ou caractères spéciaux → guillemets doubles " " ou [ ]
SELECT sal * 12 AS "Salaire Annuel"
FROM emp;
```

**Règles sur les alias :**
```
Alias autorisés dans : ORDER BY  ✓
Alias autorisés dans : WHERE     ✗  (WHERE exécuté avant SELECT)
Alias autorisés dans : HAVING    ✗  (HAVING avant SELECT aussi)
```

### 7.4 Opérateur de Concaténation

```sql
-- SQL Server : concaténation avec +
SELECT ename + ' est un ' + job AS Emploi
FROM emp;
-- Résultat : "KING est un PRESIDENT"

-- NOTE : ' ' (guillemets simples) pour les chaînes de caractères
--        " " (guillemets doubles) pour les alias
```

### 7.5 Clause WHERE — Filtrer les lignes

```sql
-- Structure
SELECT colonnes
FROM table
WHERE condition;

-- La clause WHERE SUIT IMMÉDIATEMENT la clause FROM (avant GROUP BY, ORDER BY)
```

**Opérateurs de comparaison :**

```
┌──────────────┬───────────────────────────────────────────────────┐
│  Opérateur   │  Signification                                     │
├──────────────┼───────────────────────────────────────────────────┤
│  =           │  Égal à                                           │
│  <>  ou !=  │  Différent de                                      │
│  >           │  Plus grand que                                    │
│  <           │  Plus petit que                                    │
│  >=          │  Plus grand ou égal à                             │
│  <=          │  Plus petit ou égal à                             │
├──────────────┼───────────────────────────────────────────────────┤
│  BETWEEN...AND│ Entre deux valeurs INCLUSIVEMENT                  │
│  IN(...)     │  Égal à l'une des valeurs d'une liste             │
│  LIKE '...'  │  Correspond à un modèle (% et _)                  │
│  IS NULL     │  La valeur est inconnue/vide                       │
│  IS NOT NULL │  La valeur est connue/non vide                     │
└──────────────┴───────────────────────────────────────────────────┘
```

**Exemples d'opérateurs :**

```sql
-- BETWEEN (inclus les bornes)
SELECT ename, sal FROM emp
WHERE sal BETWEEN 2000 AND 5000;

-- IN (liste de valeurs)
SELECT ename, job FROM emp
WHERE job IN ('MANAGER', 'ANALYST');

-- LIKE (modèles de chaînes)
-- % : 0 ou plusieurs caractères quelconques
-- _ : exactement 1 caractère quelconque
SELECT ename FROM emp WHERE ename LIKE 'A%';    -- Commence par A
SELECT ename FROM emp WHERE ename LIKE '%R%';   -- Contient la lettre R
SELECT ename FROM emp WHERE ename LIKE '_L%';   -- 2ème lettre est L
SELECT titre FROM Cours WHERE titre LIKE '%Initiation%'; -- Contient "Initiation"

-- IS NULL / IS NOT NULL
SELECT ename, mgr FROM emp WHERE mgr IS NULL;       -- Pas de manager
SELECT ename, comm FROM emp WHERE comm IS NOT NULL; -- A une commission
```

> **PIÈGE NULL :**
> ```sql
> WHERE comm = NULL   ← INCORRECT (ne retourne rien !)
> WHERE comm IS NULL  ← CORRECT
> ```
> `NULL` n'est pas une valeur. On ne peut pas le comparer avec `=`.

### 7.6 Opérateurs Logiques

```sql
-- AND : Les DEUX conditions doivent être vraies
SELECT ename, sal FROM emp
WHERE job = 'CLERK' AND sal > 1000;

-- OR : AU MOINS UNE condition doit être vraie
SELECT ename, sal FROM emp
WHERE sal > 1100 OR job = 'CLERK';

-- NOT : Inverse la condition
SELECT ename, job FROM emp
WHERE job NOT IN ('CLERK', 'MANAGER');
-- Équivalent à : WHERE job <> 'CLERK' AND job <> 'MANAGER'
```

**Priorité des opérateurs (ordre décroissant) :**

```
1. Opérateurs arithmétiques     (+, -, *, /)
2. Concaténation                (+)
3. Comparaisons                 (=, <>, >, <, >=, <=)
4. IS NULL, LIKE, IN
5. BETWEEN
6. Not equal to
7. NOT
8. AND
9. OR
```

> Utiliser des parenthèses `( )` pour contrôler l'ordre d'évaluation et améliorer la lisibilité.

### 7.7 Clause ORDER BY — Trier

```sql
SELECT ename, sal FROM emp
ORDER BY sal ASC;    -- Croissant (par défaut)

SELECT ename, sal FROM emp
ORDER BY sal DESC;   -- Décroissant

-- Trier par plusieurs colonnes
SELECT ename, job, sal FROM emp
ORDER BY job ASC, sal DESC;

-- Alias AUTORISÉ dans ORDER BY
SELECT sal * 12 AS salAnnuel FROM emp
ORDER BY salAnnuel DESC;  -- OK ! ORDER BY est exécuté après SELECT
```

> **PIÈGE :** La clause WHERE vient **AVANT** ORDER BY dans l'ordre d'écriture.
> `WHERE ... suit immédiatement FROM. ORDER BY est TOUJOURS EN DERNIER.`

### 7.8 Valeurs NULL — Traitement

```
┌─────────────────────────────────────────────────────────────────┐
│  NULL = valeur INCONNUE, NON APPLICABLE, NON DISPONIBLE         │
│                                                                 │
│  NULL ≠ 0  (zéro est une valeur connue)                        │
│  NULL ≠ '' (chaîne vide est une valeur connue)                 │
│                                                                 │
│  Toute opération arithmétique avec NULL → résultat NULL         │
│  Ex : sal + comm → NULL si comm est NULL                        │
│                                                                 │
│  Pour tester NULL :                                             │
│    IS NULL     → "la valeur est inconnue"                       │
│    IS NOT NULL → "la valeur est connue"                         │
│                                                                 │
│  Ne JAMAIS utiliser : = NULL  ou  <> NULL                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## 8. Les Transactions et ACID

### 8.1 Qu'est-ce qu'une transaction ?

```
┌─────────────────────────────────────────────────────────────────────┐
│  Une TRANSACTION est un ensemble d'instructions SQL qui font        │
│  passer la base de données d'un état COHÉRENT à un autre état       │
│  COHÉRENT.                                                          │
│                                                                     │
│  Exemple : Transfert bancaire                                       │
│  ┌──────────────────────────────────────────────────────────┐      │
│  │  BEGIN TRANSACTION                                        │      │
│  │      UPDATE comptes SET solde = solde - 500               │      │
│  │          WHERE id_compte = 'A';  -- Débiter A            │      │
│  │      UPDATE comptes SET solde = solde + 500               │      │
│  │          WHERE id_compte = 'B';  -- Créditer B           │      │
│  │  COMMIT;  -- Valider les deux ou aucun !                  │      │
│  └──────────────────────────────────────────────────────────┘      │
│                                                                     │
│  Si étape 1 réussit mais étape 2 échoue → ROLLBACK automatique !   │
└─────────────────────────────────────────────────────────────────────┘
```

### 8.2 Propriétés ACID

> **MNÉMONIQUE : ACID (comme un acide, ça doit être complet et fort !)**

```
╔═══════════════════════════════════════════════════════════════════════╗
║  A  ATOMICITÉ    : Tout ou Rien.                                    ║
║                   Toutes les opérations réussissent ensemble,       ║
║                   ou toutes sont annulées ensemble.                 ║
║                   "Le transfert bancaire passe en entier ou pas."  ║
╠═══════════════════════════════════════════════════════════════════════╣
║  C  COHÉRENCE    : État valide vers état valide.                    ║
║                   Les contraintes d'intégrité sont respectées       ║
║                   avant ET après la transaction.                    ║
╠═══════════════════════════════════════════════════════════════════════╣
║  I  ISOLATION    : Transactions invisibles entre elles.             ║
║                   Une transaction en cours n'est pas vue            ║
║                   par les autres tant qu'elle n'est pas committée.  ║
║                   → Les enregistrements modifiés sont VERROUILLÉS. ║
╠═══════════════════════════════════════════════════════════════════════╣
║  D  DURABILITÉ   : Permanence après COMMIT.                         ║
║                   Une fois validées, les données survivent          ║
║                   aux pannes système.                               ╚═══════════════════════════════════════════════════════════════════════╝
```

### 8.3 Instructions TCL

```sql
-- Démarrer une transaction
BEGIN TRANSACTION;  -- ou simplement BEGIN en Oracle

-- Valider définitivement
COMMIT;
-- Effets COMMIT :
-- → Les changements passent de la RAM au disque (BDD)
-- → Les VERROUS sont libérés
-- → La transaction est marquée comme terminée

-- Annuler complètement
ROLLBACK;
-- Effets ROLLBACK :
-- → Les données reviennent à l'état d'avant la transaction
-- → Les VERROUS sont libérés

-- Point de sauvegarde (annulation partielle)
SAVE TRAN nomPoint;
-- ou
SAVEPOINT nomPoint;  -- Oracle

-- Annuler jusqu'au savepoint
ROLLBACK TRAN nomPoint;
```

### 8.4 Cycle de vie d'une transaction

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CYCLE DE VIE D'UNE TRANSACTION                   │
│                                                                     │
│   [DÉBUT]                                                           │
│      │                                                              │
│      ▼                                                              │
│   Première instruction SQL exécutable                               │
│      │                                                              │
│      ▼                                                              │
│   Exécution des instructions DML                                    │
│   (Données modifiées en RAM, verrous posés)                         │
│      │                                                              │
│      ├──── COMMIT ────────► Changements permanents sur disque       │
│      │                      Verrous libérés. Transaction terminée.  │
│      │                                                              │
│      └──── ROLLBACK ───────► Retour à l'état initial               │
│                              Verrous libérés. Transaction annulée.  │
└─────────────────────────────────────────────────────────────────────┘
```

### 8.5 Isolation et Verrous

```
┌─────────────────────────────────────────────────────────────────────┐
│  SCÉNARIO : Utilisateur A et B modifient la même ligne              │
│                                                                     │
│  Utilisateur A :                                                    │
│    UPDATE merit_badge SET id = 200 WHERE id = 1;                    │
│    (Transaction A en cours → VERROU posé sur la ligne id=1)        │
│                                                                     │
│  Utilisateur B :                                                    │
│    UPDATE merit_badge SET id = 300 WHERE id = 1;                    │
│    → B est BLOQUÉ ! La ligne est verrouillée par A.                │
│                                                                     │
│  Solution : Demander à A de faire COMMIT (ou ROLLBACK)              │
│             → Verrou libéré → B peut continuer                      │
└─────────────────────────────────────────────────────────────────────┘
```

> **BONNE PRATIQUE :** Ne jamais laisser une transaction ouverte trop longtemps.
> Les verrous bloquent les autres utilisateurs.

### 8.6 Types de transactions par famille SQL

```
┌─────────────────────────────────────────────────────────────────┐
│  Type          │ Description                                    │
│────────────────┼────────────────────────────────────────────────│
│ DML            │ N'importe quel nombre d'instructions DML       │
│                │ → COMMIT ou ROLLBACK explicite nécessaire      │
│────────────────┼────────────────────────────────────────────────│
│ DDL (CREATE,   │ CHAQUE instruction DDL = UNE transaction       │
│ DROP, ALTER,   │ → Auto-committée immédiatement                 │
│ TRUNCATE)      │ → ROLLBACK sans effet                         │
│────────────────┼────────────────────────────────────────────────│
│ DCL (GRANT,    │ CHAQUE instruction DCL = UNE transaction       │
│ REVOKE)        │ → Auto-committée immédiatement                 │
└─────────────────────────────────────────────────────────────────┘
```

---

# PARTIE 2 — CONCEPTS SECONDAIRES

---

## 9. ALTER TABLE — Modifier la Structure

### Règle : On ne peut pas modifier une contrainte directement
```
Il n'y a pas d'instruction ALTER CONSTRAINT.
Pour modifier une contrainte : SUPPRIMER puis RECRÉER.
```

### Ajouter une colonne

```sql
ALTER TABLE nomTable
ADD nomColonne type [DEFAULT valeur];

-- Exemple : Ajouter une colonne email
ALTER TABLE Etudiant
ADD courriel VARCHAR(100);
```

### Modifier une colonne

```sql
ALTER TABLE nomTable
ALTER COLUMN nomColonne nouveauType [DEFAULT valeur];

-- Exemple : Augmenter la taille de email
ALTER TABLE Etudiant
ALTER COLUMN courriel NVARCHAR(150);
```

> **Directives de modification :**
> - On peut augmenter la taille d'une colonne VARCHAR
> - On peut augmenter la taille/précision d'une colonne numérique
> - On ne peut changer le type que si la colonne ne contient que des NULLs
> - On ne peut réduire la taille que si la table est vide

### Supprimer une colonne

```sql
ALTER TABLE nomTable
DROP COLUMN nomColonne;

-- Exemple
ALTER TABLE Etudiant
DROP COLUMN courriel;
```

### Ajouter une contrainte

```sql
ALTER TABLE nomTable
ADD CONSTRAINT nomContrainte type_contrainte (colonne);

-- Exemple : Ajouter une FK
ALTER TABLE emp
ADD CONSTRAINT fk_emp_dept
    FOREIGN KEY (deptno) REFERENCES dept(deptno);

-- Exemple : Ajouter un CHECK
ALTER TABLE Cours
ADD CONSTRAINT cours_duree_ck
    CHECK (duree BETWEEN 45 AND 90);
```

### Supprimer une contrainte

```sql
ALTER TABLE nomTable
DROP CONSTRAINT nomContrainte;

-- Exemple
ALTER TABLE emp
DROP CONSTRAINT fk_emp_dept;
```

---

## 10. Les Objets SQL : Séquences, Identity, Index

### 10.1 Séquences

```
┌─────────────────────────────────────────────────────────────────┐
│  SÉQUENCE : Objet indépendant qui génère des nombres uniques     │
│                                                                 │
│  Caractéristiques :                                             │
│  → Objet partagé (peut être utilisé par plusieurs tables)       │
│  → Génère des valeurs AVANT l'insertion (sans INSERT)           │
│  → Peut avoir des cycles                                        │
│  → INCONVÉNIENT : Peut créer des "trous" si partagée           │
└─────────────────────────────────────────────────────────────────┘
```

```sql
-- Créer une séquence
CREATE SEQUENCE dept_deptid_seq
    INCREMENT BY 10      -- Pas de 10
    START WITH 120       -- Commence à 120
    MAXVALUE 9999        -- Max
    NOCACHE;             -- Pas de mise en cache

-- Utiliser une séquence
INSERT INTO dept (deptno, dname)
VALUES (NEXT VALUE FOR dept_deptid_seq, 'RH');

-- Modifier une séquence
ALTER SEQUENCE dept_deptid_seq
    RESTART WITH 1
    INCREMENT BY 5;

-- Supprimer une séquence
DROP SEQUENCE dept_deptid_seq;
```

### 10.2 Colonne de type IDENTITY (SQL Server spécifique)

```
┌─────────────────────────────────────────────────────────────────┐
│  IDENTITY : Propriété d'une colonne (liée à LA table)           │
│                                                                 │
│  Caractéristiques :                                             │
│  → UNE SEULE colonne IDENTITY par table                         │
│  → Valeur générée SEULEMENT lors d'un INSERT                    │
│  → Pas de récupération à l'avance                               │
│  → Pas de cycle (contrairement à SEQUENCE)                      │
│  → Types valides : INT, BIGINT, SMALLINT, TINYINT               │
└─────────────────────────────────────────────────────────────────┘
```

```sql
-- Syntaxe : IDENTITY(valeurDépart, pas)
CREATE TABLE Etudiant (
    idEtudiant INT IDENTITY(1, 1) PRIMARY KEY,  -- Commence à 1, +1 à chaque INSERT
    nom        NVARCHAR(50) NOT NULL
);

-- SQL Server génère automatiquement : 1, 2, 3, 4...
-- On n'insère PAS la colonne IDENTITY dans INSERT
INSERT INTO Etudiant (nom) VALUES ('Tremblay');
INSERT INTO Etudiant (nom) VALUES ('Bouchard');
-- → idEtudiant sera 1 puis 2 automatiquement
```

### Séquence vs Identity — Comparatif

```
┌──────────────────────────┬────────────────────────────────────────┐
│      SÉQUENCE            │            IDENTITY                     │
├──────────────────────────┼────────────────────────────────────────┤
│ Objet indépendant        │ Propriété d'une colonne                 │
│ Utilisable par N tables  │ Liée à 1 seule table                    │
│ Valeur avant INSERT      │ Valeur générée lors du INSERT           │
│ CYCLE possible           │ Pas de CYCLE (redémarre pas auto.)      │
│ Peut créer des "trous"   │ Peut créer des "trous" aussi            │
│ Oracle et SQL Server     │ SQL Server (AUTO_INCREMENT en MySQL)     │
└──────────────────────────┴────────────────────────────────────────┘
```

### 10.3 Index

```
┌─────────────────────────────────────────────────────────────────┐
│  INDEX : Objet qui accélère les recherches dans une table        │
│                                                                 │
│  Analogie : Index à la fin d'un livre                           │
│  Sans index : lire tout le livre pour trouver un mot            │
│  Avec index : aller directement à la page                       │
│                                                                 │
│  AVANTAGE : Accélère les SELECT avec WHERE                      │
│  INCONVÉNIENT : Ralentit INSERT, UPDATE, DELETE                 │
│                 (l'index doit être mis à jour à chaque modif)   │
└─────────────────────────────────────────────────────────────────┘
```

**Création automatique :**
```
→ Sur les colonnes PRIMARY KEY  (automatique)
→ Sur les colonnes UNIQUE       (automatique)
```

**Création manuelle :**
```sql
-- Créer un index sur la colonne ename pour accélérer les recherches
CREATE INDEX emp_ename_idx
ON emp (ename);

-- Supprimer un index (pas d'ALTER INDEX)
DROP INDEX emp_ename_idx;
```

**Quand créer un index ?**
```
CRÉER si :
  ✓ Grande table avec peu de résultats retournés (< 2-4% des lignes)
  ✓ Colonne avec large éventail de valeurs distinctes
  ✓ Colonne fréquemment utilisée dans WHERE, JOIN
  ✓ Colonne avec beaucoup de NULLs (paradoxalement utile)

NE PAS CRÉER si :
  ✗ Table petite
  ✗ Colonne rarement utilisée dans WHERE
  ✗ Table mise à jour très fréquemment
  ✗ Requêtes retournent > 2-4% des lignes
```

---

## 11. Ordre des Opérations en SGBD

> **RÈGLE D'OR pour créer/insérer/supprimer avec des FK**

```
┌─────────────────────────────────────────────────────────────────────┐
│  MNÉMONIQUE : "Parent avant Enfant"                                 │
│                                                                     │
│  CRÉATION (CREATE TABLE) :                                          │
│  1. Créer les tables PARENT (sans FK)                               │
│  2. Créer les tables ENFANT (avec FK vers les parents)              │
│                                                                     │
│  INSERTION (INSERT INTO) :                                          │
│  1. Insérer dans les tables PARENT                                  │
│  2. Insérer dans les tables ENFANT                                  │
│                                                                     │
│  SUPPRESSION (DROP TABLE / DELETE) :                                │
│  1. Supprimer/Vider les tables ENFANT                               │
│  2. Supprimer/Vider les tables PARENT                               │
└─────────────────────────────────────────────────────────────────────┘

Exemple :
  dept (idDept) ◄──── emp (idDept FK)
  PARENT              ENFANT

  Ordre création : dept → emp
  Ordre insertion : dept → emp
  Ordre suppression : emp → dept
```

### Script réexécutable (bonne pratique)

```sql
-- Permettre d'exécuter le script plusieurs fois sans erreur
-- Supprimer si existe déjà (table enfant en premier !)
IF OBJECT_ID('emp', 'U') IS NOT NULL DROP TABLE emp;
IF OBJECT_ID('dept', 'U') IS NOT NULL DROP TABLE dept;

-- Créer (table parent en premier)
CREATE TABLE dept (...);
CREATE TABLE emp (...);
```

---

## 12. Relations entre Tables (Cardinalités)

### Les 3 types de relations

```
┌─────────────────────────────────────────────────────────────────────┐
│  RELATION 1:N (Un à Plusieurs) — LE PLUS COURANT                   │
│                                                                     │
│  Un département emploie plusieurs employés.                         │
│  Un employé travaille dans UN seul département.                     │
│                                                                     │
│  ┌──────────┐  1     N  ┌──────────┐                               │
│  │  DEPT    │──────────►│   EMP    │                               │
│  │──────────│           │──────────│                               │
│  │ #idDept  │           │ #idEmp   │                               │
│  │ nomDept  │           │ nomEmp   │                               │
│  └──────────┘           │ idDept(FK)│                              │
│                         └──────────┘                               │
│  Règle : La FK va dans la table côté "N" (plusieurs)               │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│  RELATION N:M (Plusieurs à Plusieurs) — TABLE DE JONCTION          │
│                                                                     │
│  Un étudiant suit plusieurs cours.                                  │
│  Un cours est suivi par plusieurs étudiants.                        │
│                                                                     │
│  ┌──────────┐  N    N  ┌──────────┐                                │
│  │ ETUDIANT │──────────│  COURS   │                                │
│  └──────────┘          └──────────┘                                │
│         │                    │                                      │
│         ▼                    ▼                                      │
│  ┌──────────────────────────────────────────────┐                  │
│  │              INSCRIPTION (table de jonction) │                  │
│  │──────────────────────────────────────────────│                  │
│  │ idEtudiant (FK + PK composée)                │                  │
│  │ idCours    (FK + PK composée)                │                  │
│  │ dateCours                                    │                  │
│  │ numLocal                                     │                  │
│  └──────────────────────────────────────────────┘                  │
│  Règle : PK de la table de jonction = FK1 + FK2                    │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│  RELATION 1:1 (Un à Un) — RARE                                      │
│                                                                     │
│  Chaque employé a exactement un dossier médical.                    │
│  Chaque dossier médical appartient à exactement un employé.         │
│                                                                     │
│  Usage : Séparer les données sensibles ou trop nombreuses.          │
│  Exemple : Table Patients → Table DossierMédical (sécurité)         │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 13. Algèbre Relationnelle

L'algèbre relationnelle est la théorie mathématique derrière SQL (E.F. Codd, 1970).

```
┌──────────────────────────────────────────────────────────────────┐
│  Opération SQL      │  Opération relationnelle                    │
│─────────────────────┼────────────────────────────────────────────│
│  WHERE              │  SÉLECTION (filter les lignes)              │
│  SELECT col1, col2  │  PROJECTION (choisir les colonnes)          │
│  JOIN               │  JOINTURE (combiner deux tables)            │
│  UNION              │  UNION (combiner deux requêtes)             │
│  INTERSECT          │  INTERSECTION                               │
│  EXCEPT             │  DIFFÉRENCE                                 │
│  Produit cartésien  │  PRODUIT CARTÉSIEN (toutes les combins.)    │
└──────────────────────────────────────────────────────────────────┘
```

---

## 14. Pièges d'Examen et Questions VRAI/FAUX

### Questions VRAI/FAUX classiques avec corrections

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Affirmation                               │ Réponse │ Explication       │
│────────────────────────────────────────────┼─────────┼───────────────────│
│ SQL est un langage procédural              │  FAUX   │ Déclaratif (L4G)  │
│────────────────────────────────────────────┼─────────┼───────────────────│
│ Les noms d'objets ne sont jamais sensibles │         │ Dépend de la      │
│ à la casse                                 │  FAUX   │ collation du SGBD │
│────────────────────────────────────────────┼─────────┼───────────────────│
│ INSERT…VALUES peut insérer plusieurs       │  VRAI   │ INSERT INTO t     │
│ enregistrements à la fois                  │         │ VALUES(1),(2),(3) │
│────────────────────────────────────────────┼─────────┼───────────────────│
│ Une instruction DDL peut être annulée      │  FAUX   │ DDL = auto-commit │
│────────────────────────────────────────────┼─────────┼───────────────────│
│ La clause WHERE suit toujours la clause    │  FAUX   │ WHERE avant ORDER │
│ ORDER BY                                   │         │ BY (jamais après) │
│────────────────────────────────────────────┼─────────┼───────────────────│
│ Une contrainte PK doit être définie sur    │  VRAI   │ Bonne pratique,   │
│ toutes les tables                          │         │ recommandé        │
│────────────────────────────────────────────┼─────────┼───────────────────│
│ Les commandes SSMS (USE) sont exécutées    │  VRAI   │ USE = instruction │
│ au niveau du SGBD                          │         │ du moteur SQL Srv │
│────────────────────────────────────────────┼─────────┼───────────────────│
│ Un alias d'un champ calculé peut être      │  FAUX   │ WHERE est exécuté │
│ utilisé dans la clause WHERE               │         │ AVANT SELECT      │
│────────────────────────────────────────────┼─────────┼───────────────────│
│ Une transaction est composée d'une ou      │  FAUX   │ Transaction = DML │
│ plusieurs instructions DDL                 │         │ pas DDL           │
│────────────────────────────────────────────┼─────────┼───────────────────│
│ Il est possible de spécifier UNIQUE sur    │  VRAI   │ UNIQUE ≠ PK,      │
│ une colonne non-clé primaire               │         │ autorise NULLs    │
└─────────────────────────────────────────────────────────────────────────┘
```

### Questions à choix multiples typiques

**Q: Comment supprimer tout le contenu de la table SalesData ?**
```
A: DELETE * FROM SalesData         → INCORRECT (DELETE n'utilise pas *)
B: DELETE FROM SalesData           → CORRECT ✓
C: DELETE SalesData                → INCORRECT (syntaxe invalide)
D: DELETE ALL SalesData            → INCORRECT (inexistant)
```

**Q: Sélectionner tous les enregistrements triés par ProductID ?**
```
A: SELECT * FROM Products WHERE ProductID > 200    → FILTRE (ne sélectionne pas tout)
B: SELECT ProductID FROM Products                  → Une seule colonne, pas triée
C: SELECT * FROM Products ORDERED BY ProductID     → ORDERED BY : INCORRECTE orthographe
D: SELECT * FROM Products ORDER BY ProductID       → CORRECT ✓
```

**Q: Sur lesquelles ROLLBACK n'a AUCUN EFFET ?**
```
INSERT          → DML → ROLLBACK possible
CREATE TABLE    → DDL → ROLLBACK sans effet ✓
DELETE TABLE    → DDL (DROP?) → ROLLBACK sans effet ✓
UPDATE          → DML → ROLLBACK possible
TRUNCATE        → DDL → ROLLBACK sans effet ✓
```

**Q: Commandes pour contrôler les opérations DML ou le comportement transactionnel ?**
```
COMMIT            ✓ (TCL)
UPDATE            ✗ (DML, pas de contrôle transactionnel)
TRUNCATE          ✗ (DDL)
INSERT            ✗ (DML)
DELETE            ✗ (DML)
SET TRANSACTION   ✓ (TCL)
ROLLBACK          ✓ (TCL)
```

---

## 15. Exercices Pratiques Complets

### Exercice 1 — Création de Tables (Examen Intra)

**Contexte :** Créer les tables pour un système de gestion de cours.

```sql
-- Script réexécutable : supprimer dans l'ordre ENFANT → PARENT
IF OBJECT_ID('Inscriptions', 'U') IS NOT NULL DROP TABLE Inscriptions;
IF OBJECT_ID('Cours',         'U') IS NOT NULL DROP TABLE Cours;
IF OBJECT_ID('Etudiant',      'U') IS NOT NULL DROP TABLE Etudiant;

-- Table PARENT : Etudiant
CREATE TABLE Etudiant (
    idEtudiant  INT           IDENTITY(1,1)   -- Auto-incrémentation
                              CONSTRAINT etudiant_idetudiant_pk PRIMARY KEY,

    nom         NVARCHAR(50)  NOT NULL,
    adresse     NVARCHAR(100) NOT NULL,

    tel         CHAR(10)      NOT NULL,         -- Taille fixe de 10
                              -- Pas de contrainte de format ici mais CHECK possible

    courriel    VARCHAR(100),                   -- NULLABLE (information non obligatoire)

    formation   VARCHAR(5)    NOT NULL
                              CONSTRAINT etudiant_formation_ck
                              CHECK (formation IN ('DEC', 'AEC'))
);

-- Table PARENT : Cours
CREATE TABLE Cours (
    idCours     INT           IDENTITY(1,1)
                              CONSTRAINT cours_idcours_pk PRIMARY KEY,

    titre       NVARCHAR(100) NOT NULL,

    duree       INT           NOT NULL
                              DEFAULT 75        -- Valeur par défaut : 75h
                              CONSTRAINT cours_duree_ck
                              CHECK (duree BETWEEN 45 AND 90),

    categorie   VARCHAR(15)   NOT NULL
                              CONSTRAINT cours_categorie_ck
                              CHECK (categorie IN ('Général', 'complémentaire', 'spécifique'))
);

-- Table ENFANT : Inscriptions (relation N:M entre Etudiant et Cours)
CREATE TABLE Inscriptions (
    idEtudiant  INT           NOT NULL,
    idCours     INT           NOT NULL,
    dateCours   DATE          NOT NULL,
    numlocal    VARCHAR(10)   NOT NULL,

    -- Clé primaire composée (DOIT être out-of-line)
    CONSTRAINT pk_inscriptions
        PRIMARY KEY (idEtudiant, idCours),

    -- Clés étrangères
    CONSTRAINT fk_inscriptions_etudiant
        FOREIGN KEY (idEtudiant) REFERENCES Etudiant(idEtudiant),

    CONSTRAINT fk_inscriptions_cours
        FOREIGN KEY (idCours) REFERENCES Cours(idCours)
);
```

### Exercice 2 — Insertions

```sql
-- Insérer dans PARENT (Etudiant) en premier
INSERT INTO Etudiant (nom, adresse, tel, courriel, formation)
VALUES ('Tremblay', '123 Rue Principale, Montreal', '5141234567',
        'jean@email.com', 'DEC');

INSERT INTO Etudiant (nom, adresse, tel, formation)  -- courriel omis (nullable)
VALUES ('Bouchard', '456 Ave du Parc, Laval', '4501234567', 'AEC');

INSERT INTO Etudiant (nom, adresse, tel, formation)
VALUES ('Gagnon', '789 Boul Decarie, Montreal', '5141111111', 'DEC');

-- Insérer dans PARENT (Cours) ensuite
INSERT INTO Cours (titre, duree, categorie)
VALUES ('Initiation à SQL', 60, 'spécifique');

INSERT INTO Cours (titre, duree, categorie)
VALUES ('Programmation Web', 75, 'Général');  -- duree = valeur par défaut

INSERT INTO Cours (titre, categorie)  -- duree prend la valeur DEFAULT (75)
VALUES ('Initiation à Python', 'complémentaire');

-- Insérer dans ENFANT (Inscriptions) en dernier
INSERT INTO Inscriptions (idEtudiant, idCours, dateCours, numlocal)
VALUES (1, 1, '2024-01-15', 'A-101');

INSERT INTO Inscriptions (idEtudiant, idCours, dateCours, numlocal)
VALUES (1, 2, '2024-01-16', 'B-201');

INSERT INTO Inscriptions (idEtudiant, idCours, dateCours, numlocal)
VALUES (2, 1, '2024-01-15', 'A-101');
```

### Exercice 3 — Mises à Jour

```sql
-- Un cours qui ne se donne plus → le supprimer (ou le marquer inactif)
-- Si on a une colonne statut :
-- UPDATE Cours SET statut = 'INACTIF' WHERE titre = 'Programmation Web';

-- Si on doit supprimer (d'abord supprimer les inscriptions liées !)
DELETE FROM Inscriptions WHERE idCours = 2;  -- ENFANT en premier
DELETE FROM Cours WHERE idCours = 2;         -- PARENT ensuite

-- Changer le local d'une inscription
UPDATE Inscriptions
SET    numlocal = 'C-301'
WHERE  idEtudiant = 1 AND idCours = 1;
```

### Exercice 4 — Requêtes SELECT

```sql
-- 1. La liste des cours ayant une durée supérieure à 60 heures
SELECT idCours, titre, duree
FROM   Cours
WHERE  duree > 60;

-- 2. Les étudiants en formation AEC qui ne sont PAS dans la zone 514
SELECT idEtudiant, nom, tel, formation
FROM   Etudiant
WHERE  formation = 'AEC'
AND    tel NOT LIKE '514%';

-- 3. Les cours dont le titre contient le mot "Initiation"
SELECT idCours, titre
FROM   Cours
WHERE  titre LIKE '%Initiation%';

-- 4. Les étudiants en formation DEC
SELECT idEtudiant, nom, formation
FROM   Etudiant
WHERE  formation = 'DEC';

-- 5. Les étudiants dont le téléphone est dans la zone 514
SELECT idEtudiant, nom, tel
FROM   Etudiant
WHERE  tel LIKE '514%';

-- 6. Liste d'inscriptions pour une date donnée
--    La date doit être affichée dans le format "lundi, 15 janvier 2012"
SELECT
    i.idCours,
    FORMAT(i.dateCours, 'dddd, dd MMMM yyyy', 'fr-FR') AS [Date du cours]
FROM   Inscriptions i
WHERE  i.dateCours = '2024-01-15';
-- Note : FORMAT() est une fonction SQL Server pour le formatage de dates
```

---

# ANNEXES

## Annexe A — Comparatif TRUNCATE vs DELETE vs DROP

```
┌──────────────┬─────────────────┬──────────────────┬──────────────────────┐
│              │    TRUNCATE      │     DELETE        │       DROP           │
├──────────────┼─────────────────┼──────────────────┼──────────────────────┤
│ Famille      │ DDL             │ DML              │ DDL                  │
│ Action       │ Vide la table   │ Supprime lignes  │ Supprime la table    │
│ WHERE        │ Non             │ Oui              │ N/A                  │
│ ROLLBACK     │ Non (auto-commit)│ Oui              │ Non (auto-commit)    │
│ Structure    │ Conservée       │ Conservée        │ Détruite             │
│ Vitesse      │ Très rapide     │ Lente (1 par 1)  │ Rapide               │
│ Triggers     │ Non déclenché   │ Déclenché        │ N/A                  │
└──────────────┴─────────────────┴──────────────────┴──────────────────────┘
```

## Annexe B — Résumé des Fonctions SQL Server Utiles

```sql
-- Date du jour
getDate()          -- Ex: INSERT INTO t VALUES (getDate())

-- Formatage de date
FORMAT(date, 'dd/MM/yyyy')              -- 15/01/2024
FORMAT(date, 'dddd, dd MMMM yyyy', 'fr-FR')  -- lundi, 15 janvier 2024

-- Conversion
CONVERT(VARCHAR, getDate(), 103)        -- 15/01/2024 (format français)

-- Longueur d'une chaîne
LEN('bonjour')     -- 7

-- Majuscules / Minuscules
UPPER('hello')     -- HELLO
LOWER('HELLO')     -- hello

-- Vérifier l'existence d'un objet
IF OBJECT_ID('nomTable', 'U') IS NOT NULL
    DROP TABLE nomTable;
```

## Annexe C — Schéma de la BD d'exemple (EMP/DEPT)

```
Table DEPT :
┌─────────┬────────────┬────────────┐
│ DEPTNO  │   DNAME    │    LOC     │
├─────────┼────────────┼────────────┤
│   10    │ ACCOUNTING │  NEW YORK  │
│   20    │ RESEARCH   │  DALLAS    │
│   30    │ SALES      │  CHICAGO   │
│   40    │ OPERATIONS │  BOSTON    │
└─────────┴────────────┴────────────┘

Table EMP (colonnes principales) :
┌──────┬─────────┬───────────┬──────┬─────────┬──────┬────────┬──────────┐
│EMPNO │  ENAME  │    JOB    │ MGR  │HIREDATE │ SAL  │  COMM  │ DEPTNO   │
├──────┼─────────┼───────────┼──────┼─────────┼──────┼────────┼──────────┤
│ 7839 │ KING    │ PRESIDENT │ NULL │17-NOV-81│ 5000 │  NULL  │   10     │
│ 7698 │ BLAKE   │ MANAGER   │ 7839 │01-MAY-81│ 2850 │  NULL  │   30     │
│ 7782 │ CLARK   │ MANAGER   │ 7839 │09-JUN-81│ 2450 │  NULL  │   10     │
│ 7566 │ JONES   │ MANAGER   │ 7839 │02-APR-81│ 2975 │  NULL  │   20     │
│ 7654 │ MARTIN  │ SALESMAN  │ 7698 │28-SEP-81│ 1250 │  1400  │   30     │
│ 7499 │ ALLEN   │ SALESMAN  │ 7698 │20-FEB-81│ 1600 │   300  │   30     │
│ 7844 │ TURNER  │ SALESMAN  │ 7698 │08-SEP-81│ 1500 │     0  │   30     │
│ 7900 │ JAMES   │ CLERK     │ 7698 │03-DEC-81│  950 │  NULL  │   30     │
│ 7902 │ FORD    │ ANALYST   │ 7566 │03-DEC-81│ 3000 │  NULL  │   20     │
│ 7369 │ SMITH   │ CLERK     │ 7902 │17-DEC-80│  800 │  NULL  │   20     │
└──────┴─────────┴───────────┴──────┴─────────┴──────┴────────┴──────────┘

Relation : EMP.DEPTNO (FK) → DEPT.DEPTNO (PK)
           EMP.MGR    (FK auto-référentielle) → EMP.EMPNO (PK)
```

---

*Manuel créé selon la méthode Pareto 80/20 — Basé sur les cours de la Professeure Soraya Ferdenache*
*Contexte : SQL Server / SSMS*