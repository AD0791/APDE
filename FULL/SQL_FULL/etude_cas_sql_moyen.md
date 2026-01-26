# Étude de Cas SQL — Niveau Moyen

## Guide de Préparation aux Examens : Requêtes Avancées et Modélisation

---

Ce document intermédiaire vous entraîne à écrire des requêtes plus complexes et à raisonner sur la performance. Vous allez manipuler un schéma bancaire réaliste, utiliser des CTE, des fonctions de fenêtre, des vues, et définir des contraintes d'intégrité.

---

## Schéma Étendu (Banque)

```sql
CREATE TABLE agences (
    agence_id   INT PRIMARY KEY,
    nom         VARCHAR(100) NOT NULL,
    ville       VARCHAR(80) NOT NULL
);

CREATE TABLE clients (
    client_id   INT PRIMARY KEY,
    nom         VARCHAR(100) NOT NULL,
    agence_id   INT NOT NULL,
    date_inscription DATE NOT NULL,
    FOREIGN KEY (agence_id) REFERENCES agences(agence_id)
);

CREATE TABLE comptes (
    compte_id   INT PRIMARY KEY,
    client_id   INT NOT NULL,
    solde       DECIMAL(12,2) NOT NULL,
    statut      VARCHAR(20) NOT NULL, -- ACTIF, BLOQUE
    date_ouverture DATE NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(client_id)
);

CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    compte_id      INT NOT NULL,
    type_tx        VARCHAR(10) NOT NULL, -- DEPOT, RETRAIT, VIREMENT
    montant        DECIMAL(12,2) NOT NULL,
    date_tx        TIMESTAMP NOT NULL,
    FOREIGN KEY (compte_id) REFERENCES comptes(compte_id)
);
```

---

## Problème 1 : Classement des Comptes (Window Functions)

### Énoncé

Pour chaque agence, classer les comptes du plus riche au moins riche et afficher le rang.

### Solution

```sql
SELECT a.nom AS agence,
       c.compte_id,
       c.solde,
       RANK() OVER (PARTITION BY a.agence_id ORDER BY c.solde DESC) AS rang
FROM comptes c
JOIN clients cl ON cl.client_id = c.client_id
JOIN agences a ON a.agence_id = cl.agence_id
ORDER BY a.nom, rang;
```

---

## Problème 2 : CTE et Analyse d'Activité

### Énoncé

Calculer le total des transactions par client sur les 30 derniers jours.

### Solution

```sql
WITH tx_recentes AS (
    SELECT co.client_id, t.montant
    FROM transactions t
    JOIN comptes co ON co.compte_id = t.compte_id
    WHERE t.date_tx >= CURRENT_DATE - INTERVAL '30 days'
)
SELECT client_id, SUM(montant) AS total_30j
FROM tx_recentes
GROUP BY client_id
ORDER BY total_30j DESC;
```

---

## Problème 3 : Vue et Contrôles d'Intégrité

### Énoncé

1. Créer une vue qui expose les comptes actifs uniquement.
2. Ajouter une contrainte pour empêcher un solde négatif.

### Solution

```sql
-- 1
CREATE VIEW comptes_actifs AS
SELECT compte_id, client_id, solde, date_ouverture
FROM comptes
WHERE statut = 'ACTIF';

-- 2
ALTER TABLE comptes
ADD CONSTRAINT chk_solde_positif CHECK (solde >= 0);
```

---

## Problème 4 : Indexation et Performance

### Énoncé

On observe des requêtes lentes sur les transactions filtrées par date et compte. Proposer un index approprié.

### Solution

```sql
CREATE INDEX idx_transactions_compte_date
ON transactions (compte_id, date_tx);
```

---

## Problème 5 : Synthèse par Agence (GROUP BY + HAVING)

### Énoncé

Afficher le total des soldes par agence et garder uniquement les agences dont
le total dépasse 10 000.

### Solution

```sql
SELECT a.nom AS agence,
       SUM(c.solde) AS total_solde
FROM comptes c
JOIN clients cl ON cl.client_id = c.client_id
JOIN agences a ON a.agence_id = cl.agence_id
GROUP BY a.nom
HAVING SUM(c.solde) > 10000
ORDER BY total_solde DESC;
```

---

## Problème 6 : Clients Inactifs

### Énoncé

Trouver les clients sans transactions sur les 60 derniers jours.

### Solution

```sql
SELECT cl.client_id, cl.nom
FROM clients cl
LEFT JOIN comptes co ON co.client_id = cl.client_id
LEFT JOIN transactions t ON t.compte_id = co.compte_id
    AND t.date_tx >= CURRENT_DATE - INTERVAL '60 days'
GROUP BY cl.client_id, cl.nom
HAVING COUNT(t.transaction_id) = 0;
```

---

## Problème 7 : Vue de Reporting

### Énoncé

Créer une vue qui expose pour chaque client son nombre de comptes et son solde total.

### Solution

```sql
CREATE VIEW v_resume_clients AS
SELECT cl.client_id,
       cl.nom,
       COUNT(co.compte_id) AS nb_comptes,
       SUM(co.solde) AS solde_total
FROM clients cl
LEFT JOIN comptes co ON co.client_id = cl.client_id
GROUP BY cl.client_id, cl.nom;
```

---

## Conseils d'Entretien

- Justifiez l'usage d'index par les requêtes cibles.
- Préférez des CTE pour clarifier les étapes logiques.
- Utilisez des contraintes pour sécuriser les règles métier.
