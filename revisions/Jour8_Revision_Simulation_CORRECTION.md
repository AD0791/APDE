# Correction - Simulation d'examen Jour 8

Ce document contient la resolution complete de l'examen ainsi que des
explications additionnelles pour chaque question.

---

## Section 1: Theorie

### Question 1 - ACID (exemples bancaires)
- **Atomicite**: une transaction est tout ou rien.  
  Exemple: un virement debit + credit. Si le credit echoue, on annule le debit.
- **Coherence**: les regles metier restent vraies.  
  Exemple: un compte ne peut pas devenir negatif si la banque l'interdit.
- **Isolation**: les transactions simultanees ne se perturbent pas.  
  Exemple: deux retraits en meme temps ne doivent pas "dupliquer" l'argent.
- **Durabilite**: une transaction validee survit aux pannes.  
  Exemple: apres un crash, un virement valide reste en base.

### Question 2 - Classe abstraite vs interface (Java)
- **Classe abstraite**: peut contenir attributs, methodes concretes et abstraites.
  Heritages simple.
  Exemple d'usage: `CompteBancaire` partage du code commun.
- **Interface**: definit un contrat, implementation multiple possible.
  Exemple d'usage: `Payable`, `Comparable`, `Serializable`.

### Question 3 - SOLID (definition + violation + bonne pratique)
1) **Single Responsibility**  
   - Definition: une classe = une seule raison de changer.  
   - Violation: `UserService` gere logique, email et base.  
   - Bonne pratique: separer `UserService`, `EmailService`, `UserRepository`.
2) **Open/Closed**  
   - Definition: ouvert a l'extension, ferme a la modification.  
   - Violation: `switch` geant sur un type.  
   - Bonne pratique: polymorphisme via classes/fonctions.
3) **Liskov Substitution**  
   - Definition: un enfant remplace le parent sans casser le comportement.  
   - Violation: `Rectangle`/`Square` si setters cassent les invariants.  
   - Bonne pratique: hierarchie coherente ou composition.
4) **Interface Segregation**  
   - Definition: interfaces petites et ciblees.  
   - Violation: interface "tout-en-un" forcee.  
   - Bonne pratique: interfaces par role.
5) **Dependency Inversion**  
   - Definition: dependances sur des abstractions, pas des details.  
   - Violation: `Service` depend de `MySQLConnection`.  
   - Bonne pratique: `Service` depend de l'interface `Database`.

### Question 4 - TCP 3-way handshake
```
Client  -> Serveur : SYN
Serveur -> Client  : SYN-ACK
Client  -> Serveur : ACK
```
Explication: negotiation de la connexion et synchronisation des numeros de
sequence avant l'echange de donnees.

### Question 5 - XSS et CSRF + prevention
- **XSS**: injection de scripts dans une page.  
  Prevention: echappement/encodage HTML, CSP, validation stricte.
- **CSRF**: action forcee par un tiers sur un utilisateur connecte.  
  Prevention: tokens CSRF, cookies SameSite, verification d'origine.

---

## Section 2: UML

### Question 6 - Diagramme de classes (reservation de vols)
Classes:
- `Passager(nom, email, telephone)`
- `Vol(numero, destination, dateDepart, siegesDisponibles)`
- `Reservation(dateReservation, statut, siege)`
- `Paiement(montant, datePaiement, methodePaiement)`

Relations:
- `Passager 1 ---- 0..* Reservation`
- `Reservation 1 ---- 1 Vol`
- `Reservation 1 ---- 1 Paiement`

Methodes principales (exemples):
- `Passager`: `creerReservation()`, `annulerReservation()`
- `Vol`: `verifierDisponibilite()`, `reserverSiege()`
- `Reservation`: `confirmer()`, `annuler()`
- `Paiement`: `effectuer()`, `rembourser()`

### Question 7 - Diagramme de sequence (retrait 500 HTG)
Flux (avec fragment `alt`):
```
Client -> GAB : insererCarte()
GAB -> ServeurBanque : validerCarte()
Client -> GAB : saisirPIN()
Client -> GAB : choisirMontant(500)
GAB -> ServeurBanque : verifierSolde(500)
alt solde suffisant
  ServeurBanque -> Compte : debiter(500)
  ServeurBanque -> GAB : autoriserRetrait()
  GAB -> Client : distribuerCash()
else solde insuffisant
  ServeurBanque -> GAB : refuser()
  GAB -> Client : messageErreur()
end
```

---

## Section 3: SQL

### Question 8 - Clients + nb comptes + solde total > 10000
```sql
SELECT
  c.client_id,
  c.nom,
  c.prenom,
  COUNT(co.compte_id) AS total_comptes,
  SUM(co.solde) AS solde_total
FROM clients c
JOIN comptes co ON co.client_id = c.client_id
GROUP BY c.client_id, c.nom, c.prenom
HAVING SUM(co.solde) > 10000
ORDER BY solde_total DESC;
```
Explication: `HAVING` filtre apres aggregation. `COUNT` et `SUM` se font par
client via `GROUP BY`.

### Question 9 - Transaction virement 1000 HTG (pseudo SQL)
```sql
BEGIN TRANSACTION;

SELECT solde FROM comptes WHERE compte_id = 123 FOR UPDATE;

UPDATE comptes
SET solde = solde - 1000
WHERE compte_id = 123;

UPDATE comptes
SET solde = solde + 1000
WHERE compte_id = 456;

INSERT INTO transactions(compte_source_id, compte_dest_id, type, montant, statut)
VALUES (123, 456, 'virement', 1000, 'complete');

COMMIT;
```
Si solde insuffisant: `ROLLBACK;`.

### Question 10 - Table transactions
```sql
CREATE TABLE transactions (
  transaction_id SERIAL PRIMARY KEY,
  compte_source_id INT NOT NULL,
  compte_dest_id INT NULL,
  type VARCHAR(20) NOT NULL CHECK (type IN ('depot','retrait','virement')),
  montant DECIMAL(12,2) NOT NULL CHECK (montant > 0),
  date_transaction TIMESTAMP NOT NULL DEFAULT NOW(),
  statut VARCHAR(20) NOT NULL CHECK (statut IN ('en_cours','complete','annulee')),
  CONSTRAINT fk_source FOREIGN KEY (compte_source_id) REFERENCES comptes(compte_id),
  CONSTRAINT fk_dest FOREIGN KEY (compte_dest_id) REFERENCES comptes(compte_id)
);

CREATE INDEX idx_transactions_source ON transactions(compte_source_id);
CREATE INDEX idx_transactions_date ON transactions(date_transaction);
```

---

## Section 4: Java/POO

### Question 11 - CompteBancaire + CompteEpargne
```java
public abstract class CompteBancaire {
    private String numeroCompte;
    private double solde;
    private String titulaire;

    public CompteBancaire(String numeroCompte, double solde, String titulaire) {
        this.numeroCompte = numeroCompte;
        this.solde = solde;
        this.titulaire = titulaire;
    }

    public abstract boolean retirer(double montant);

    public void deposer(double montant) {
        if (montant > 0) {
            solde += montant;
        }
    }

    public String getNumeroCompte() { return numeroCompte; }
    public double getSolde() { return solde; }
    public String getTitulaire() { return titulaire; }

    protected void setSolde(double solde) { this.solde = solde; }
}

public class CompteEpargne extends CompteBancaire {
    private double tauxInteret;
    private int retraitsCeMois = 0;

    public CompteEpargne(String numero, double solde, String titulaire, double tauxInteret) {
        super(numero, solde, titulaire);
        this.tauxInteret = tauxInteret;
    }

    @Override
    public boolean retirer(double montant) {
        if (montant <= 0 || retraitsCeMois >= 3) return false;
        if (getSolde() >= montant) {
            setSolde(getSolde() - montant);
            retraitsCeMois++;
            return true;
        }
        return false;
    }

    public double calculerInterets() {
        return getSolde() * tauxInteret;
    }
}
```
Explication: `retirer` est abstraite car depend du type de compte. La limite de
3 retraits est geree par un compteur mensuel.

### Question 12 - Singleton (Bill Pugh, thread-safe)
```java
public class Configuration {
    private Configuration() {}

    private static class Holder {
        private static final Configuration INSTANCE = new Configuration();
    }

    public static Configuration getInstance() {
        return Holder.INSTANCE;
    }
}
```
Explication: initialisation lazy, thread-safe, sans `synchronized`.

---

## Section 5: Algorithmes

### Question 13 - Binary Search
```java
public static int binarySearch(int[] arr, int target) {
    int left = 0, right = arr.length - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) return mid;
        if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
```
Explication: on divise l'espace de recherche par 2 a chaque iteration.

### Question 14 - Trace Quick Sort [5, 2, 8, 1, 9] (pivot = dernier)
1. Pivot = 9: `[5,2,8,1] | 9`
2. Pivot = 1: `[] | 1 | [5,2,8]`
3. Pivot = 8: `[5,2] | 8`
4. Pivot = 2: `[] | 2 | [5]`

Resultat final: **[1,2,5,8,9]**

### Question 15 - BFS (pseudo-code Java)
```java
public static void bfs(Map<Integer, List<Integer>> graph, int start) {
    Queue<Integer> queue = new LinkedList<>();
    Set<Integer> visited = new HashSet<>();

    visited.add(start);
    queue.add(start);

    while (!queue.isEmpty()) {
        int node = queue.poll();
        System.out.println(node);

        for (int neighbor : graph.get(node)) {
            if (!visited.contains(neighbor)) {
                visited.add(neighbor);
                queue.add(neighbor);
            }
        }
    }
}
```
Explication: exploration en largeur, couche par couche, via une file FIFO.

