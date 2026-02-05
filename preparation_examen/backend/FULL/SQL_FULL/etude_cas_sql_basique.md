# Étude de Cas SQL — Niveau Basique

## Guide de Préparation aux Examens : Fondamentaux SQL

---

Ce document vous prépare aux exercices SQL de base souvent posés dans les entretiens techniques. Vous allez manipuler un petit modèle bancaire simplifié et apprendre à écrire des requêtes correctes, lisibles et sûres. L'objectif est d'être capable de créer un schéma relationnel simple, d'insérer des données, puis d'extraire des informations via des requêtes SELECT avec filtres, tris et jointures.

---

## Modèle de Données (Contexte Bancaire Simplifié)

### Schéma (DDL)

```sql
CREATE TABLE clients (
    client_id      INT PRIMARY KEY,
    nom            VARCHAR(100) NOT NULL,
    email          VARCHAR(120) UNIQUE,
    date_inscription DATE NOT NULL
);

CREATE TABLE comptes (
    compte_id      INT PRIMARY KEY,
    client_id      INT NOT NULL,
    type_compte    VARCHAR(20) NOT NULL, -- COURANT, EPARGNE
    solde          DECIMAL(12,2) NOT NULL,
    date_ouverture DATE NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(client_id)
);

CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    compte_id      INT NOT NULL,
    type_tx        VARCHAR(10) NOT NULL, -- DEPOT, RETRAIT, VIREMENT
    montant        DECIMAL(12,2) NOT NULL,
    date_tx        DATE NOT NULL,
    FOREIGN KEY (compte_id) REFERENCES comptes(compte_id)
);
```

### Données de Test (INSERT)

```sql
INSERT INTO clients VALUES
(1, 'Jean Pierre', 'jean.pierre@demo.ht', '2024-01-12'),
(2, 'Marie Noel',   'marie.noel@demo.ht',  '2024-02-03'),
(3, 'Paul Charles', 'paul.charles@demo.ht','2024-03-15');

INSERT INTO comptes VALUES
(100, 1, 'COURANT',  2500.00, '2024-01-15'),
(101, 1, 'EPARGNE',  8000.00, '2024-01-20'),
(200, 2, 'COURANT',  1200.00, '2024-02-10'),
(300, 3, 'COURANT',   500.00, '2024-03-20');

INSERT INTO transactions VALUES
(1, 100, 'DEPOT',    1000.00, '2024-02-01'),
(2, 100, 'RETRAIT',   200.00, '2024-02-05'),
(3, 101, 'DEPOT',    3000.00, '2024-02-07'),
(4, 200, 'RETRAIT',   100.00, '2024-02-12'),
(5, 300, 'DEPOT',     600.00, '2024-03-25');
```

---

## Problème 1 : Requêtes de Base (SELECT, WHERE, ORDER BY)

### Énoncé

1. Lister tous les clients (nom, email), triés par nom.
2. Afficher les comptes avec un solde supérieur à 2000.
3. Afficher toutes les transactions de type DEPOT.

### Solution

```sql
-- 1
SELECT nom, email
FROM clients
ORDER BY nom ASC;

-- 2
SELECT compte_id, client_id, solde
FROM comptes
WHERE solde > 2000
ORDER BY solde DESC;

-- 3
SELECT transaction_id, compte_id, montant, date_tx
FROM transactions
WHERE type_tx = 'DEPOT'
ORDER BY date_tx;
```

---

## Problème 2 : Jointures Simples (JOIN)

### Énoncé

1. Afficher pour chaque compte le nom du client, le type de compte et le solde.
2. Afficher toutes les transactions avec le nom du client concerné.

### Solution

```sql
-- 1
SELECT c.nom, co.type_compte, co.solde
FROM comptes co
JOIN clients c ON c.client_id = co.client_id
ORDER BY c.nom;

-- 2
SELECT c.nom, t.transaction_id, t.type_tx, t.montant, t.date_tx
FROM transactions t
JOIN comptes co ON co.compte_id = t.compte_id
JOIN clients c ON c.client_id = co.client_id
ORDER BY t.date_tx;
```

---

## Problème 3 : Agrégations (COUNT, SUM, GROUP BY)

### Énoncé

1. Compter le nombre de comptes par client.
2. Totaliser le montant des dépôts par compte.

### Solution

```sql
-- 1
SELECT c.client_id, c.nom, COUNT(co.compte_id) AS nb_comptes
FROM clients c
LEFT JOIN comptes co ON co.client_id = c.client_id
GROUP BY c.client_id, c.nom
ORDER BY nb_comptes DESC;

-- 2
SELECT t.compte_id, SUM(t.montant) AS total_depots
FROM transactions t
WHERE t.type_tx = 'DEPOT'
GROUP BY t.compte_id
ORDER BY total_depots DESC;
```

---

## Problème 4 : Insertion de Données

### Énoncé

1. Ajouter un nouveau client.
2. Ouvrir un compte courant pour ce client.

### Solution

```sql
-- 1
INSERT INTO clients (client_id, nom, email, date_inscription)
VALUES (4, 'Luc Etienne', 'luc.etienne@demo.ht', '2024-04-02');

-- 2
INSERT INTO comptes (compte_id, client_id, type_compte, solde, date_ouverture)
VALUES (400, 4, 'COURANT', 0.00, '2024-04-02');
```

---

## Problème 5 : Mise à Jour (UPDATE)

### Énoncé

1. Créditer 250.00 au compte 300.
2. Marquer l'email d'un client comme vide si l'email est NULL.

### Solution

```sql
-- 1
UPDATE comptes
SET solde = solde + 250.00
WHERE compte_id = 300;

-- 2
UPDATE clients
SET email = 'inconnu@demo.ht'
WHERE email IS NULL;
```

---

## Problème 6 : Sous-Requête Simple

### Énoncé

Afficher les clients qui possèdent au moins un compte avec un solde > 5000.

### Solution

```sql
SELECT nom, email
FROM clients
WHERE client_id IN (
    SELECT client_id
    FROM comptes
    WHERE solde > 5000
);
```

---

## Conseils d'Entretien

- Gardez les requêtes simples et lisibles.
- Vérifiez toujours les jointures (clé primaire / clé étrangère).
- Utilisez des alias courts (c, co, t) pour la clarté.
