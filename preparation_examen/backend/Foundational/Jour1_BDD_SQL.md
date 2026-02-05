# Jour 1 (21 janvier): Bases de données & SQL

**Temps estimé:** 6-8 heures  
**Priorité:** 🔴 CRITIQUE - Le secteur bancaire repose sur les BDD

---

## 🎯 Pourquoi commencer par les BDD?

Le secteur bancaire vit et respire les **transactions** et l'**intégrité des données**. Les propriétés **ACID** apparaissent dans PRESQUE TOUS les examens bancaires. Votre expérience PostgreSQL/MySQL est un atout, mais l'écriture manuscrite de requêtes SQL sans IDE demande de la pratique.



>**Définition simple**: Une base de données (BDD) est un système organisé pour stocker, gérer et récupérer des données de manière structurée et efficace. C'est comme un classeur numérique ultra-puissant avec des règles strictes d'organisation.


**En résumé**:

Une base de données est un coffre-fort numérique intelligent qui :

- ✅ Stocke les données de façon organisée
- ✅ Empêche les erreurs et corruptions
- ✅ Permet à plusieurs personnes d'y accéder en même temps
- ✅ Garantit que les opérations critiques se déroulent correctement (ACID)

Dans le secteur bancaire, c'est absolument vital car on ne peut pas se permettre de perdre des données de transactions ou d'avoir des soldes incorrects !

---

## 📚 Concepts essentiels (Pareto 20/80)

### 1. Propriétés ACID - À MÉMORISER ABSOLUMENT

| Propriété | Définition | Exemple bancaire concret |
|-----------|------------|--------------------------|
| **Atomicity** (Atomicité) | Tout ou rien - la transaction complète réussit ou échoue entièrement | Virement: le débit ET le crédit doivent réussir ensemble. Si l'un échoue, tout est annulé. |
| **Consistency** (Cohérence) | La BDD passe d'un état valide à un autre état valide | Le solde ne peut jamais devenir négatif si une contrainte CHECK l'interdit |
| **Isolation** | Les transactions concurrentes n'interfèrent pas entre elles | Deux retraits simultanés sur le même compte ne causent pas d'erreur de solde |
| **Durability** (Durabilité) | Les changements committés survivent aux pannes système | Après confirmation d'un virement, les données persistent même en cas de coupure électrique |

#### Commandes de transaction
```sql
BEGIN TRANSACTION;
    UPDATE comptes SET solde = solde - 500 WHERE compte_id = 1;
    UPDATE comptes SET solde = solde + 500 WHERE compte_id = 2;
COMMIT;  -- Ou ROLLBACK en cas d'erreur
```

---

### 2. Les JOINs - Visualiser mentalement les ensembles

```sql
-- INNER JOIN: Clients AVEC comptes uniquement (intersection)
SELECT c.nom, a.numero_compte, a.solde
FROM clients c
INNER JOIN comptes a ON c.client_id = a.client_id;

-- LEFT JOIN: TOUS les clients, même sans compte
SELECT c.nom, a.numero_compte
FROM clients c
LEFT JOIN comptes a ON c.client_id = a.client_id;

-- RIGHT JOIN: TOUS les comptes, même sans client (rare)
SELECT c.nom, a.numero_compte
FROM clients c
RIGHT JOIN comptes a ON c.client_id = a.client_id;

-- Mnémonique: 
-- INNER = intersection (∩)
-- LEFT = tout à gauche + correspondances
-- RIGHT = tout à droite + correspondances
```

**Diagramme mental:**
```
CLIENTS          COMPTES
   A  ────────────  1
   B  ────────────  2
   C               3

INNER JOIN → A-1, B-2 (seulement les correspondances)
LEFT JOIN  → A-1, B-2, C-NULL (tous les clients)
RIGHT JOIN → A-1, B-2, NULL-3 (tous les comptes)
```

---

### 3. Normalisation simplifiée

> **Définition**: La normalisation est le processus d'organisation des données pour éliminer la redondance et garantir l'intégrité des données. C'est comme ranger un placard en désordre pour éviter les doublons et faciliter la recherche. ❌ Sans normalisation : données dupliquées, incohérences, gaspillage d'espace. ✅ Avec normalisation : données propres, pas de répétition, mises à jour faciles.

1. 1NF (Première Forme Normale)

> Règle : Chaque cellule contient UNE SEULE valeur (atomique) + avoir une clé primaire

2. 2NF (Deuxième Forme Normale)

> Règle : 1NF + tous les attributs dépendent de la CLÉ ENTIÈRE (pas juste d'une partie)

3. 3NF (Troisième Forme Normale)

> Règle : 2NF + aucune dépendance transitive (attribut non-clé → attribut non-clé)




| Forme | Règle d'or | Problème résolu | Exemple violation |
|-------|-----------|-----------------|-------------------|
| **1NF** | Valeurs atomiques uniquement + clé primaire | Groupes répétitifs | Colonne "téléphones" = "555-1234, 555-5678" |
| **2NF** | 1NF + pas de dépendances partielles de la clé | Attributs dépendant d'une partie de la clé composée | Table (étudiant_id, cours_id, nom_étudiant) - nom dépend seulement de étudiant_id |
| **3NF** | 2NF + pas de dépendances transitives | Attributs non-clés dépendant d'autres non-clés | Table (client_id, ville, code_postal) - code_postal dépend de ville |

**Exemple pratique de normalisation:**

**Non normalisé:**
```
Commande(commande_id, client_nom, client_adresse, produit1, qte1, produit2, qte2)
```

**3NF:**
```
Client(client_id, nom, adresse)
Commande(commande_id, client_id, date)
LigneCommande(ligne_id, commande_id, produit_id, quantite)
Produit(produit_id, nom, prix)
```

---

### 4. Index et performance

> **Définition**: Un index est une structure de données qui accélère la recherche dans une table, comme l'index d'un livre qui te permet de trouver rapidement un sujet sans lire toutes les pages.

1. B-Tree (Balanced Tree) - INDEX PAR DÉFAUT
Définition : Structure d'arbre équilibré qui maintient les données triées.

2. Hash Index
Définition : Utilise une fonction de hachage pour accès direct ultra-rapide.

3. Unique Index
Définition : Index qui garantit l'unicité des valeurs (pas de doublons).

4. Composite Index (Index Composé)
Définition : Index sur plusieurs colonnes à la fois.

5. Clustered Index (Index Clustérisé)
Définition : Réorganise physiquement les lignes de la table selon l'ordre de l'index.

Caractéristiques :
1 seul par table (car les données ne peuvent être ordonnées que d'une façon)
Automatiquement créé sur la PRIMARY KEY
Très rapide pour lectures séquentielles

7. Full-Text Index
Définition : Index optimisé pour recherche textuelle dans de longs textes.

8. Spatial Index
Définition : Index pour données géographiques (coordonnées GPS, polygones).

9. Covering Index (Index Couvrant)
Définition : Index contenant toutes les colonnes nécessaires à la requête (pas besoin de lire la table).

10. Partial Index (Index Partiel)
Définition : Index sur un sous-ensemble filtré de la table.


| Type d'index | Structure | Meilleur usage | Exemple |
|--------------|-----------|----------------|---------|
| **B-Tree** | Arbre équilibré (défaut) | Plages, égalité, ORDER BY | `CREATE INDEX idx_nom ON clients(nom);` |
| **Hash** | Table de hachage | Égalité exacte uniquement | Rarement supporté en production |
| **Clustered** | Ordonne physiquement les données | Clé primaire (1 seul par table) | Automatique sur PRIMARY KEY |
| **Non-clustered** | Structure séparée pointant vers données | Colonnes recherchées fréquemment | `CREATE INDEX idx_email ON clients(email);` |

```sql
-- Créer un index simple
CREATE INDEX idx_client_email ON clients(email);

-- Créer un index composé
CREATE INDEX idx_transaction_date_montant ON transactions(date_creation, montant);

-- Index UNIQUE
CREATE UNIQUE INDEX idx_numero_compte ON comptes(numero_compte);
```

**Quand utiliser un index?**
- ✅ Colonnes dans WHERE/JOIN fréquents
- ✅ Colonnes dans ORDER BY
- ✅ Clés étrangères
- ❌ Tables très petites (< 100 lignes)
- ❌ Colonnes modifiées très souvent

---

## 💻 10 Requêtes SQL bancaires à MÉMORISER

### 1. Obtenir le solde d'un compte
```sql
SELECT numero_compte, solde, devise, type_compte
FROM comptes 
WHERE compte_id = ?;
```

### 2. Virement entre comptes (transaction ACID complète)
```sql
BEGIN TRANSACTION;

-- Vérifier solde suffisant
DECLARE @solde_actuel DECIMAL(15,2);
SELECT @solde_actuel = solde FROM comptes WHERE compte_id = 1;

IF @solde_actuel >= 500
BEGIN
    -- Débiter compte source
    UPDATE comptes 
    SET solde = solde - 500 
    WHERE compte_id = 1;
    
    -- Créditer compte destination
    UPDATE comptes 
    SET solde = solde + 500 
    WHERE compte_id = 2;
    
    -- Enregistrer transaction
    INSERT INTO transactions (de_compte, vers_compte, montant, type, statut)
    VALUES (1, 2, 500, 'virement', 'complete');
    
    COMMIT;
END
ELSE
BEGIN
    ROLLBACK;
    -- Gérer l'erreur de solde insuffisant
END
```

### 3. Historique des transactions d'un compte
```sql
SELECT 
    t.transaction_id,
    t.montant,
    t.type,
    t.date_creation,
    CASE 
        WHEN t.de_compte = ? THEN 'débit'
        WHEN t.vers_compte = ? THEN 'crédit'
    END AS sens
FROM transactions t
WHERE t.de_compte = ? OR t.vers_compte = ?
ORDER BY t.date_creation DESC
LIMIT 50;
```

### 4. Client avec tous ses comptes (JOIN)
```sql
SELECT 
    c.client_id,
    c.nom,
    c.prenom,
    c.email,
    a.numero_compte,
    a.type_compte,
    a.solde,
    a.devise
FROM clients c
INNER JOIN comptes a ON c.client_id = a.client_id
WHERE c.client_id = ?;
```

### 5. Solde total par client (agrégation)
```sql
SELECT 
    c.client_id,
    c.nom,
    c.prenom,
    COUNT(a.compte_id) AS nombre_comptes,
    SUM(a.solde) AS solde_total
FROM clients c
LEFT JOIN comptes a ON c.client_id = a.client_id
GROUP BY c.client_id, c.nom, c.prenom
HAVING SUM(a.solde) > 10000  -- Clients avec plus de 10000
ORDER BY solde_total DESC;
```

### 6. Top 10 clients par solde
```sql
SELECT 
    c.nom,
    c.prenom,
    SUM(a.solde) AS solde_total
FROM clients c
INNER JOIN comptes a ON c.client_id = a.client_id
GROUP BY c.client_id, c.nom, c.prenom
ORDER BY solde_total DESC
LIMIT 10;
```

### 7. Comptes par type avec statistiques
```sql
SELECT 
    type_compte,
    COUNT(*) AS nombre_comptes,
    AVG(solde) AS solde_moyen,
    MIN(solde) AS solde_min,
    MAX(solde) AS solde_max,
    SUM(solde) AS solde_total
FROM comptes
GROUP BY type_compte;
```

### 8. Clients avec emails dupliqués (problème de qualité)
```sql
SELECT 
    email,
    COUNT(*) AS nombre_occurrences,
    STRING_AGG(nom, ', ') AS clients_concernes
FROM clients
GROUP BY email
HAVING COUNT(*) > 1;
```

### 9. CREATE TABLE avec contraintes (conception)
```sql
CREATE TABLE comptes (
    compte_id INT PRIMARY KEY AUTO_INCREMENT,
    client_id INT NOT NULL,
    numero_compte VARCHAR(20) UNIQUE NOT NULL,
    type_compte VARCHAR(20) CHECK (type_compte IN ('epargne', 'courant', 'credit')),
    solde DECIMAL(15, 2) DEFAULT 0.00 CHECK (solde >= 0),
    devise CHAR(3) DEFAULT 'HTG',
    date_ouverture DATE NOT NULL DEFAULT CURRENT_DATE,
    statut VARCHAR(10) CHECK (statut IN ('actif', 'ferme', 'suspendu')),
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE RESTRICT
);

-- Index pour performance
CREATE INDEX idx_client ON comptes(client_id);
CREATE INDEX idx_numero ON comptes(numero_compte);
```

### 10. Verrouillage pour éviter les race conditions
```sql
BEGIN TRANSACTION;

-- Verrouiller la ligne pour lecture exclusive
SELECT solde 
FROM comptes 
WHERE compte_id = 1 
FOR UPDATE;  -- Ligne verrouillée jusqu'au COMMIT

-- Effectuer le retrait si solde suffisant
UPDATE comptes 
SET solde = solde - 100 
WHERE compte_id = 1 AND solde >= 100;

-- Vérifier si UPDATE a réussi
IF @@ROWCOUNT > 0
    COMMIT;
ELSE
    ROLLBACK;
```

---

## ⚠️ Pièges SQL courants en examen écrit

| Erreur | Conséquence | Correction |
|--------|-------------|------------|
| Oublier le point-virgule `;` | Syntaxe invalide | Terminer CHAQUE requête par `;` |
| `WHERE column = NULL` | Ne retourne rien | Utiliser `WHERE column IS NULL` |
| Confondre WHERE et HAVING | Erreur de logique | WHERE avant GROUP BY, HAVING après |
| Oublier WHERE dans UPDATE/DELETE | Modifie TOUTES les lignes! | Toujours tester avec SELECT d'abord |
| Mauvais type de JOIN | Perte de données | Dessiner un diagramme mental |
| Parenthèses manquantes | Ordre d'opérations incorrect | `WHERE (a AND b) OR c` vs `WHERE a AND (b OR c)` |
| Virgule avant FROM | Syntaxe invalide | `SELECT a, b FROM` (pas de virgule finale) |

---

## 📝 Exercices pratiques Jour 1

### Exercice 1: Requêtes de base
**Sur papier, sans regarder les notes, écrire:**

1. Une requête pour obtenir tous les clients de la ville "Port-au-Prince"
2. Une requête avec INNER JOIN montrant clients et leurs comptes
3. Une requête calculant le nombre total de transactions par type
4. Une requête trouvant les comptes avec solde négatif (découvert)

### Exercice 2: Transaction complète
**Écrire une transaction SQL pour:**
- Retrait de 200 HTG du compte #123
- Vérifier que le solde est suffisant
- Enregistrer l'opération dans une table `operations`
- Utiliser BEGIN, COMMIT, ROLLBACK

### Exercice 3: Conception de table
**Créer une table `transactions` avec:**
- transaction_id (PK)
- compte_id (FK vers comptes)
- type (depot, retrait, virement)
- montant (> 0)
- date_transaction (avec valeur par défaut)
- description (optionnel)

### Exercice 4: ACID
**Expliquer en 2-3 phrases chacune des 4 propriétés ACID avec un exemple bancaire différent de ceux du cours.**

---

## ✅ Checklist de révision Jour 1

Avant de passer au Jour 2, vérifier que vous pouvez:

- [ ] Expliquer les 4 propriétés ACID avec exemples bancaires
- [ ] Dessiner un diagramme Venn des différents JOIN
- [ ] Écrire de mémoire une transaction avec BEGIN/COMMIT
- [ ] Expliquer 1NF, 2NF, 3NF en une phrase chacune
- [ ] Écrire les 5 requêtes SQL bancaires les plus courantes
- [ ] Créer une table avec contraintes CHECK et FK
- [ ] Utiliser GROUP BY avec HAVING
- [ ] Différencier WHERE et HAVING
- [ ] Utiliser FOR UPDATE pour verrouillage
- [ ] Créer un index simple et composé

---

## 🎓 Concepts avancés (bonus si temps disponible)

### Niveaux d'isolation des transactions

| Niveau | Dirty Read | Non-repeatable Read | Phantom Read |
|--------|------------|---------------------|--------------|
| **READ UNCOMMITTED** | ✓ Possible | ✓ Possible | ✓ Possible |
| **READ COMMITTED** | ✗ Impossible | ✓ Possible | ✓ Possible |
| **REPEATABLE READ** | ✗ Impossible | ✗ Impossible | ✓ Possible |
| **SERIALIZABLE** | ✗ Impossible | ✗ Impossible | ✗ Impossible |

```sql
-- Définir le niveau d'isolation
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN TRANSACTION;
-- vos requêtes
COMMIT;
```

### Sous-requêtes

```sql
-- Clients ayant plus d'un compte
SELECT nom, prenom
FROM clients
WHERE client_id IN (
    SELECT client_id 
    FROM comptes 
    GROUP BY client_id 
    HAVING COUNT(*) > 1
);

-- Comptes avec solde supérieur à la moyenne
SELECT numero_compte, solde
FROM comptes
WHERE solde > (SELECT AVG(solde) FROM comptes);
```

---

## 📖 Ressources recommandées

- **SQLBolt** - Tutoriels interactifs SQL (faire les 13 leçons)
- **Mode Analytics SQL Tutorial** - Exercices pratiques
- **W3Schools SQL** - Référence rapide
- **PostgreSQL Documentation** - Pour syntaxe avancée

---

**💡 Conseil:** Pratiquez l'écriture manuscrite! Écrivez au moins 5 requêtes SQL sur papier aujourd'hui et chronométrez-vous. L'examen est MANUSCRIT, pas sur ordinateur.

---

## 🔎 Extension: Compréhension & Rétention (Jour 1)

### 1) Erreurs fréquentes (et comment les éviter)
- Oublier le `WHERE` → impact massif (UPDATE/DELETE)
- Confondre `WHERE` et `HAVING`
- Mauvais `JOIN` (clé incorrecte)
- `COUNT(col)` vs `COUNT(*)` (NULL ignorés)

### 2) Exercices rapides (avec solutions)

**Exercice A:** clients sans compte  
```sql
SELECT c.client_id, c.nom
FROM clients c
LEFT JOIN comptes co ON co.client_id = c.client_id
WHERE co.compte_id IS NULL;
```

**Exercice B:** total des retraits par compte  
```sql
SELECT compte_id, SUM(montant) AS total_retraits
FROM transactions
WHERE type_tx = 'RETRAIT'
GROUP BY compte_id;
```

**Exercice C:** top 3 comptes par solde  
```sql
SELECT compte_id, solde
FROM comptes
ORDER BY solde DESC
LIMIT 3;
```

### 3) Questions type examen
- Définir ACID en 1 phrase chacun
- Différence `INNER JOIN` vs `LEFT JOIN`
- Expliquer pourquoi un index accélère la lecture mais ralentit l'écriture

### 4) Checklist mémoire
- [ ] ACID compris + exemple bancaire
- [ ] JOINs dessinés mentalement
- [ ] GROUP BY + HAVING maîtrisés
- [ ] Index = lecture + / écriture -

---

**Prochain document:** `OOP.md` - Guide complet POO (Java + Python)
