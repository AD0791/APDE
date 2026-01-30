# Étude de Cas SQL — Niveau Senior

## Guide de Préparation aux Examens : Optimisation, Transactions et Scalabilité

---

Ce document avancé se concentre sur les problématiques réelles en banque : performance, isolation des transactions, cohérence des données et gestion des volumes. Les exercices demandent des solutions robustes et justifiées.

---

## Contexte Métier

Une banque traite des millions de transactions quotidiennes. Les comptes doivent rester cohérents, les accès doivent être rapides, et les rapports doivent être fiables même sous forte charge.

---

## Problème 1 : Transfert Atomique et Isolation

### Énoncé

Écrire une transaction SQL qui transfère 500.00 d'un compte A vers un compte B en garantissant :
1) le solde du compte A ne devient jamais négatif,
2) l'opération est atomique,
3) la concurrence est gérée correctement.

### Solution

```sql
BEGIN;

SELECT solde
FROM comptes
WHERE compte_id = 100
FOR UPDATE;

UPDATE comptes
SET solde = solde - 500.00
WHERE compte_id = 100 AND solde >= 500.00;

UPDATE comptes
SET solde = solde + 500.00
WHERE compte_id = 200;

COMMIT;
```

Notes:
- `FOR UPDATE` verrouille la ligne pour éviter les retraits concurrents.
- Un `ROLLBACK` doit être effectué côté application si l'update ne modifie aucune ligne.

---

## Problème 2 : Rapport Mensuel (Window + Partition)

### Énoncé

Générer un rapport mensuel des 12 derniers mois avec :
- total des transactions par mois,
- variation en pourcentage par rapport au mois précédent.

### Solution

```sql
WITH tx_mensuelles AS (
    SELECT DATE_TRUNC('month', date_tx) AS mois,
           SUM(montant) AS total_mensuel
    FROM transactions
    WHERE date_tx >= CURRENT_DATE - INTERVAL '12 months'
    GROUP BY DATE_TRUNC('month', date_tx)
)
SELECT mois,
       total_mensuel,
       LAG(total_mensuel) OVER (ORDER BY mois) AS total_prec,
       CASE
           WHEN LAG(total_mensuel) OVER (ORDER BY mois) IS NULL THEN NULL
           ELSE ROUND(
               (total_mensuel - LAG(total_mensuel) OVER (ORDER BY mois))
               / LAG(total_mensuel) OVER (ORDER BY mois) * 100, 2
           )
       END AS variation_pct
FROM tx_mensuelles
ORDER BY mois;
```

---

## Problème 3 : Partitionnement des Transactions

### Énoncé

La table `transactions` devient trop volumineuse. Proposer un partitionnement par mois.

### Solution (PostgreSQL)

```sql
CREATE TABLE transactions (
    transaction_id BIGINT NOT NULL,
    compte_id      INT NOT NULL,
    type_tx        VARCHAR(10) NOT NULL,
    montant        DECIMAL(12,2) NOT NULL,
    date_tx        DATE NOT NULL
) PARTITION BY RANGE (date_tx);

CREATE TABLE transactions_2025_01 PARTITION OF transactions
FOR VALUES FROM ('2025-01-01') TO ('2025-02-01');

CREATE TABLE transactions_2025_02 PARTITION OF transactions
FOR VALUES FROM ('2025-02-01') TO ('2025-03-01');
```

---

## Problème 4 : Analyse de Performance (EXPLAIN)

### Énoncé

Une requête lente filtre les transactions par compte et par date. Montrer comment diagnostiquer la requête et proposer une solution.

### Solution

```sql
EXPLAIN ANALYZE
SELECT *
FROM transactions
WHERE compte_id = 100
  AND date_tx >= '2025-01-01'
  AND date_tx <  '2025-02-01';
```

Amélioration recommandée:

```sql
CREATE INDEX idx_tx_compte_date
ON transactions (compte_id, date_tx);
```

---

## Problème 5 : Conflits de Concurrence (Deadlock)

### Énoncé

Deux transactions transfèrent des fonds entre comptes A et B.
Proposer une règle simple pour éviter les deadlocks.

### Solution

Règle: toujours verrouiller les comptes dans le même ordre (par ID).

```sql
BEGIN;

-- verrouillage ordonné
SELECT solde FROM comptes WHERE compte_id = 100 FOR UPDATE;
SELECT solde FROM comptes WHERE compte_id = 200 FOR UPDATE;

-- transfert
UPDATE comptes SET solde = solde - 500.00 WHERE compte_id = 100;
UPDATE comptes SET solde = solde + 500.00 WHERE compte_id = 200;

COMMIT;
```

---

## Problème 6 : Vue Matérialisée pour Reporting

### Énoncé

Créer une vue matérialisée du total mensuel des transactions pour accélérer les rapports.

### Solution

```sql
CREATE MATERIALIZED VIEW mv_tx_mensuelles AS
SELECT DATE_TRUNC('month', date_tx) AS mois,
       SUM(montant) AS total_mensuel
FROM transactions
GROUP BY DATE_TRUNC('month', date_tx);

-- Rafraîchissement planifié
REFRESH MATERIALIZED VIEW mv_tx_mensuelles;
```

---

## Problème 7 : Audit via Trigger

### Énoncé

Tracer chaque retrait dans une table d'audit.

### Solution (PostgreSQL)

```sql
CREATE TABLE audit_retraits (
    audit_id       BIGSERIAL PRIMARY KEY,
    transaction_id INT NOT NULL,
    compte_id      INT NOT NULL,
    montant        DECIMAL(12,2) NOT NULL,
    date_audit     TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE OR REPLACE FUNCTION log_retrait()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.type_tx = 'RETRAIT' THEN
        INSERT INTO audit_retraits (transaction_id, compte_id, montant)
        VALUES (NEW.transaction_id, NEW.compte_id, NEW.montant);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_log_retrait
AFTER INSERT ON transactions
FOR EACH ROW
EXECUTE FUNCTION log_retrait();
```

---

## Conseils d'Entretien

- Expliquez vos choix d'isolation et de verrouillage.
- Pensez aux impacts sur la concurrence.
- Montrez que vous comprenez le coût des requêtes.
