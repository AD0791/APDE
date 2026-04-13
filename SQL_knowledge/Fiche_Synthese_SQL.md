# FICHE DE SYNTHÈSE — SQL & SGBDR
## A lire 30 minutes avant l'examen !
### Cours de Soraya Ferdenache | SQL Server / SSMS

---

## 1. LES 4 FAMILLES SQL

> **MNÉMO : "Dieu Mange Des Tartes"** (DDL, DML, DCL, TCL)

```
┌──────┬──────────────────────────────────────────────────────┐
│ DDL  │ CREATE  ALTER  DROP  TRUNCATE     → STRUCTURE        │
│ DML  │ SELECT  INSERT  UPDATE  DELETE   → DONNÉES           │
│ DCL  │ GRANT  REVOKE                    → SÉCURITÉ          │
│ TCL  │ COMMIT  ROLLBACK  SAVEPOINT      → TRANSACTIONS      │
└──────┴──────────────────────────────────────────────────────┘
```

**CRUCIAL :** DDL = auto-committée → ROLLBACK sans effet sur CREATE/DROP/TRUNCATE

---

## 2. ORDRE SELECT — Écriture vs Exécution

> **MNÉMO ÉCRITURE : "Sept Filles Web Gèrent Habilement Online"**

```
ÉCRITURE :           EXÉCUTION INTERNE :
──────────           ──────────────────
SELECT     ─────►    5. Projeter les colonnes
FROM       ─────►    1. Charger les tables   ← EN PREMIER
WHERE      ─────►    2. Filtrer les lignes
GROUP BY   ─────►    3. Créer les groupes
HAVING     ─────►    4. Filtrer les groupes
ORDER BY   ─────►    6. Trier               ← EN DERNIER
```

**Conséquences :**
- Alias défini dans SELECT → **INTERDIT** dans WHERE et HAVING (exécutés avant)
- Alias défini dans SELECT → **AUTORISÉ** dans ORDER BY (exécuté après)
- La clause WHERE suit immédiatement FROM (jamais après ORDER BY !)

---

## 3. LES 5 CONTRAINTES D'INTÉGRITÉ

> **MNÉMO : "P.F.U.N.C." — Pour Faire Une Nouvelle Contrainte**

```
P → PRIMARY KEY : NOT NULL + UNIQUE. 1 seule par table. Identifie chaque ligne.
F → FOREIGN KEY : Lien entre tables. Peut être NULL. Intégrité référentielle.
U → UNIQUE      : Valeurs uniques. Autorise NULL. N contraintes par table.
N → NOT NULL    : Champ obligatoire. Toujours inline.
C → CHECK       : Condition métier. Ex: CHECK (formation IN ('DEC','AEC'))
```

**PK vs UNIQUE :**
```
PRIMARY KEY = NOT NULL + UNIQUE     |     UNIQUE = peut contenir NULL
```

**Niveaux de définition :**
```
NOT NULL               → COLONNE uniquement (inline)
PK composée (2+ cols)  → TABLE uniquement (out-of-line)
PK/FK/UNIQUE/CHECK     → COLONNE ou TABLE (si 1 colonne)
```

---

## 4. PROPRIÉTÉS ACID (Transactions)

> **MNÉMO : ACID — "Un acide doit être complet et fort !"**

```
A  Atomicité  : Tout ou Rien. Succès total ou échec total.
C  Cohérence  : BD passe d'un état valide à un autre état valide.
I  Isolation  : Transactions isolées. Enregistrements verrouillés.
D  Durabilité : COMMIT = permanent même après panne.
```

**Cycle transaction :**
```
BEGIN → [instructions DML] → COMMIT  (valider, libérer verrous)
                           → ROLLBACK (annuler, libérer verrous)
```

**Avant COMMIT :** Changements en RAM, enregistrements verrouillés.
**Après COMMIT :** Changements sur disque, verrous libérés.

---

## 5. NORMALISATION (1FN → 2FN → 3FN)

> **MNÉMO : "L'Atome — Toute la clé — Rien que la clé"**

```
┌────────────────────────────────────────────────────────────────────┐
│  1FN : L'Atome    → Chaque cellule = 1 seule valeur (atomique)    │
│                     Pas de listes, pas de répétitions              │
├────────────────────────────────────────────────────────────────────┤
│  2FN : Toute la  → 1FN + attribut non-clé dépend de TOUTE la PK  │
│        clé          (important si PK composée)                     │
├────────────────────────────────────────────────────────────────────┤
│  3FN : Rien que  → 2FN + pas de dépendance TRANSITIVE             │
│        la clé       (A → B → C interdit si B n'est pas une clé)   │
└────────────────────────────────────────────────────────────────────┘
```

**Pourquoi ?** Éliminer redondances, anomalies d'insertion/modification/suppression.

---

## 6. MODÉLISATION (MCD → MLD → MPD)

```
RÉALITÉ → MCD (Entités + Associations) → MLD (Tables + Clés) → MPD (SQL)
           Indépendant du SGBD            Normalisation         CREATE TABLE
```

**Relations :**
```
1:N  → FK dans la table côté "N" (plusieurs)  — LE PLUS COURANT
N:M  → Table de jonction avec PK = FK1 + FK2
1:1  → Rare. Sécurité ou table trop large.
```

**Ordre CREATE/INSERT/DROP :**
```
Créer  : PARENT d'abord → ENFANT ensuite
Insérer: PARENT d'abord → ENFANT ensuite
Supprimer: ENFANT d'abord → PARENT ensuite   ← INVERSE !
```

---

## 7. DDL — SYNTAXES ESSENTIELLES

```sql
-- Créer une table
CREATE TABLE Etudiant (
    idEtudiant INT IDENTITY(1,1) CONSTRAINT etudiant_pk PRIMARY KEY,
    nom        NVARCHAR(50) NOT NULL,
    tel        CHAR(10) NOT NULL,
    courriel   VARCHAR(100),                               -- nullable
    formation  VARCHAR(5) NOT NULL
               CONSTRAINT etudiant_formation_ck CHECK (formation IN ('DEC','AEC'))
);

-- PK composée → TOUJOURS out-of-line
CREATE TABLE Inscriptions (
    idEtudiant INT NOT NULL,  idCours INT NOT NULL,
    CONSTRAINT pk_inscriptions PRIMARY KEY (idEtudiant, idCours),
    CONSTRAINT fk_etud FOREIGN KEY (idEtudiant) REFERENCES Etudiant(idEtudiant),
    CONSTRAINT fk_cours FOREIGN KEY (idCours)   REFERENCES Cours(idCours)
);

-- Modifier
ALTER TABLE Etudiant ADD email VARCHAR(100);          -- Ajouter colonne
ALTER TABLE Etudiant ALTER COLUMN email NVARCHAR(150); -- Modifier colonne
ALTER TABLE Etudiant DROP COLUMN email;               -- Supprimer colonne
ALTER TABLE emp ADD CONSTRAINT fk_dept FOREIGN KEY (deptno) REFERENCES dept(deptno);
ALTER TABLE emp DROP CONSTRAINT fk_dept;              -- Pas d'ALTER CONSTRAINT !

-- Supprimer (vérifier ordre !)
DROP TABLE Inscriptions;  -- ENFANT en premier
DROP TABLE Etudiant;      -- PARENT ensuite
```

---

## 8. DML — SYNTAXES ESSENTIELLES

```sql
-- INSERT
INSERT INTO dept (deptno, dname, loc) VALUES (50, 'RH', 'MTL');

-- UPDATE  ← TOUJOURS mettre WHERE !
UPDATE emp SET deptno = 20 WHERE empno = 7782;
-- DANGER : Sans WHERE → toute la table est modifiée !

-- DELETE  ← TOUJOURS mettre WHERE !
DELETE FROM emp WHERE empno = 4444;
-- DANGER : Sans WHERE → toute la table est supprimée !
```

**TRUNCATE vs DELETE :**
```
TRUNCATE : DDL, ultra-rapide, ROLLBACK impossible, pas de WHERE
DELETE   : DML, ligne par ligne, ROLLBACK possible, peut avoir WHERE
```

---

## 9. SELECT — OPÉRATEURS CLÉS

```sql
-- Filtres
WHERE sal BETWEEN 2000 AND 5000      -- Inclus les bornes
WHERE job IN ('MANAGER', 'ANALYST')  -- Liste de valeurs
WHERE ename LIKE '%R%'               -- Contient R
WHERE ename LIKE 'A%'                -- Commence par A
WHERE ename LIKE '_L%'               -- 2ème lettre est L
WHERE comm IS NULL                   -- Valeur inconnue
WHERE comm IS NOT NULL               -- Valeur connue

-- Jamais : WHERE comm = NULL ← INCORRECT !

-- Logique
WHERE job = 'CLERK' AND sal > 1000   -- LES DEUX conditions vraies
WHERE sal > 1100 OR job = 'CLERK'    -- AU MOINS UNE condition vraie
WHERE job NOT IN ('CLERK','MANAGER') -- Inverse

-- Concaténation SQL Server
SELECT ename + ' est un ' + job AS Emploi FROM emp;

-- Trier
ORDER BY sal ASC    -- Croissant (défaut)
ORDER BY sal DESC   -- Décroissant
```

---

## 10. SÉQUENCE vs IDENTITY

```
SÉQUENCE                        IDENTITY
────────────────────────────    ──────────────────────────────
Objet indépendant               Propriété d'une colonne
Peut être partagée (N tables)   Liée à 1 seule table
NEXT VALUE FOR seq              Valeur auto au INSERT
Valeur récupérable avant INSERT Pas de récupération avant INSERT
Cycle possible                  Pas de cycle automatique
```

```sql
-- Séquence
CREATE SEQUENCE seq_dept INCREMENT BY 10 START WITH 120;
INSERT INTO dept VALUES (NEXT VALUE FOR seq_dept, 'RH');

-- Identity
CREATE TABLE t (id INT IDENTITY(1,1) PRIMARY KEY);
INSERT INTO t (col1) VALUES ('val');  -- id généré auto
```

---

## 11. INDEX

```
INDEX = Accélère les recherches SELECT + WHERE
COÛT  = Ralentit INSERT, UPDATE, DELETE (index à maintenir)

Créé AUTO sur : PRIMARY KEY, UNIQUE
Créé MANUELLEMENT pour : colonnes fréquemment dans WHERE

CREATE INDEX emp_ename_idx ON emp (ename);
DROP INDEX emp_ename_idx;          -- Pas d'ALTER INDEX !
```

---

## 12. QUESTIONS VRAI/FAUX — RÉPONSES RAPIDES

```
SQL est déclaratif (non procédural)                      → VRAI
SQL est un langage procédural                            → FAUX
DDL peut être annulé avec ROLLBACK                       → FAUX (auto-commit)
Alias du SELECT utilisable dans WHERE                    → FAUX (WHERE avant SELECT)
Alias du SELECT utilisable dans ORDER BY                 → VRAI (ORDER BY après SELECT)
WHERE suit ORDER BY                                      → FAUX (WHERE avant ORDER BY)
NULL = 0                                                 → FAUX (NULL = inconnu)
NULL = ''                                                → FAUX
UNIQUE autorise NULL                                     → VRAI
PRIMARY KEY autorise NULL                                → FAUX (NOT NULL obligatoire)
Transaction DML = instructions DML                       → VRAI
Transaction DML = instructions DDL                       → FAUX
TRUNCATE peut être annulé                                → FAUX (DDL, auto-commit)
DELETE peut être annulé                                  → VRAI (DML, ROLLBACK possible)
Une PK peut être définie sur plusieurs colonnes          → VRAI (PK composée)
Il peut y avoir plusieurs PK dans une table              → FAUX (1 seule)
Il peut y avoir plusieurs contraintes UNIQUE             → VRAI
```

---

## 13. PIÈGES SQL SERVER SPÉCIFIQUES

```
Concaténation       : + (SQL Server) vs || (Oracle/PostgreSQL)
Sensibilité casse   : Dépend de la COLLATION (par défaut : non sensible)
Date du jour        : getDate() (SQL Server) vs sysdate (Oracle)
Auto-incrémentation : IDENTITY (SQL Server) vs SEQUENCE ou AUTO_INCREMENT
Vérif. existence    : IF OBJECT_ID('table', 'U') IS NOT NULL
Alias avec espaces  : "Salaire Annuel" ou [Salaire Annuel]
Chaînes de texte    : ' ' (guillemets simples)
Alias               : " " (guillemets doubles) ou [ ]
```

---

## 14. TEMPLATE D'EXAMEN PRATIQUE

```sql
-- ÉTAPE 1 : Script réexécutable (supprimer ordre ENFANT → PARENT)
IF OBJECT_ID('Inscriptions','U') IS NOT NULL DROP TABLE Inscriptions;
IF OBJECT_ID('Cours','U')        IS NOT NULL DROP TABLE Cours;
IF OBJECT_ID('Etudiant','U')     IS NOT NULL DROP TABLE Etudiant;

-- ÉTAPE 2 : Créer les tables (PARENT → ENFANT)
CREATE TABLE Etudiant ( ... );
CREATE TABLE Cours    ( ... );
CREATE TABLE Inscriptions ( ... );

-- ÉTAPE 3 : Insérer (PARENT → ENFANT)
INSERT INTO Etudiant ... ;
INSERT INTO Cours    ... ;
INSERT INTO Inscriptions ... ;

-- ÉTAPE 4 : Mettre à jour
UPDATE nomTable SET col = val WHERE condition;

-- ÉTAPE 5 : Requêtes SELECT
SELECT col1, col2 FROM table WHERE condition ORDER BY col1;
```

---

## 15. CHECKLIST DE DERNIÈRE MINUTE

```
[ ] Je connais les 4 familles (DDL/DML/DCL/TCL) et leurs commandes
[ ] Je connais l'ordre d'exécution SQL (FROM→WHERE→GROUP→HAVING→SELECT→ORDER)
[ ] Je sais pourquoi alias interdit dans WHERE mais autorisé dans ORDER BY
[ ] Je connais les 5 contraintes (P.F.U.N.C.) et leurs différences
[ ] Je sais quand une contrainte va au niveau colonne vs table
[ ] Je connais ACID et ce que fait COMMIT / ROLLBACK
[ ] Je sais que DDL est auto-committée (ROLLBACK sans effet)
[ ] Je connais les 3 formes normales (Atome / Toute la clé / Rien que la clé)
[ ] Je sais l'ordre CREATE/INSERT/DROP (Parent avant Enfant)
[ ] Je sais que UPDATE et DELETE SANS WHERE modifient/suppriment TOUT
[ ] Je sais que NULL ≠ 0 et qu'on utilise IS NULL (jamais = NULL)
[ ] Je connais TRUNCATE vs DELETE (DDL vs DML, vitesse, ROLLBACK)
[ ] Je connais la différence SÉQUENCE vs IDENTITY
[ ] Je sais quand créer un INDEX (et son coût sur INSERT/UPDATE)
[ ] Je sais que LIKE utilise % (0+ caractères) et _ (1 caractère exact)
```

---

*Bonne chance ! Lis bien les énoncés, regarde bien la structure des tables, et reste calme.*