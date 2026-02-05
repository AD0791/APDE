# Jour 8 (28 janvier): Révision intensive & Simulation d'examen

**Temps estimé:** 6-8 heures  
**Priorité:** 🔴 CRITIQUE - Jour de consolidation

---

## 🎯 Objectif du jour

**Consolider toutes les connaissances** et se **préparer mentalement** pour l'examen du 29 janvier. Ce jour combine révision ciblée, simulation d'examen, et optimisation de la performance en conditions réelles.

---

## 📅 Planning détaillé du Jour 8

| Heure | Activité | Durée |
|-------|----------|-------|
| **08h00-10h00** | **SIMULATION D'EXAMEN COMPLÈTE** | 2h |
| **10h00-11h00** | Correction et analyse des erreurs | 1h |
| **11h00-13h00** | Révision ciblée des points faibles | 2h |
| **14h00-16h00** | Réécriture des codes essentiels sur papier | 2h |
| **16h00-17h00** | Relecture des fiches de synthèse | 1h |
| **17h00-18h00** | Repos, préparation mentale, confiance | 1h |

---

## 📝 SIMULATION D'EXAMEN (2 heures)

### Consignes

- ⏱️ Chronométrer exactement 2 heures
- 📝 Écrire sur papier UNIQUEMENT
- 🚫 Aucune consultation (notes, internet, livres)
- ✅ Conditions réelles d'examen

### Section 1: Théorie (30 minutes)

**Question 1 (5 points):** Expliquez les 4 propriétés ACID avec un exemple bancaire pour chacune.

**Question 2 (5 points):** Différenciez classe abstraite et interface en Java. Donnez un exemple d'usage pour chacune.

**Question 3 (10 points):** Expliquez les 5 principes SOLID. Pour chaque principe:
- Définition en une phrase
- Exemple de violation
- Exemple de bonne application

**Question 4 (5 points):** Expliquez le TCP 3-way handshake avec un schéma.

**Question 5 (5 points):** Qu'est-ce que XSS et CSRF? Comment les prévenir? (2-3 phrases chacun)

---

### Section 2: UML (30 minutes)

**Question 6 (15 points):** Dessinez un diagramme de classes UML pour un système de réservation de vols avec:
- Classe Passager (nom, email, téléphone)
- Classe Vol (numéro, destination, dateDepart, siègesDisponibles)
- Classe Réservation (dateReservation, statut, siège)
- Classe Paiement (montant, datePaiement, methodePaiement)

**Relations:**
- Un passager peut avoir plusieurs réservations
- Une réservation concerne un seul vol
- Une réservation a un seul paiement
- Inclure multiplicités et méthodes principales

**Question 7 (10 points):** Dessinez un diagramme de séquence pour:
**Scénario:** Un client retire 500 HTG à un guichet automatique.
**Acteurs/Objets:** Client, GAB, ServeurBanque, Compte
**Flux:** Insertion carte → Validation → Saisie PIN → Choix montant → Vérification solde → Retrait
**Inclure:** Fragment `alt` pour solde suffisant/insuffisant

---

### Section 3: SQL (30 minutes)

**Question 8 (10 points):** Écrivez une requête SQL pour:
- Afficher tous les clients avec le nombre total de leurs comptes
- Afficher le solde total par client
- Trier par solde total décroissant
- Afficher seulement les clients avec solde > 10000 HTG

**Tables:**
```sql
clients(client_id, nom, prenom, email)
comptes(compte_id, client_id, numero_compte, solde, type_compte)
```

**Question 9 (10 points):** Écrivez une transaction SQL complète pour effectuer un virement de 1000 HTG du compte #123 vers le compte #456. Inclure:
- Vérification du solde suffisant
- BEGIN TRANSACTION
- Débit du compte source
- Crédit du compte destination
- Enregistrement dans une table transactions
- COMMIT ou ROLLBACK selon le cas

**Question 10 (10 points):** Créez une table `transactions` avec:
- transaction_id (PK, auto-increment)
- compte_source_id (FK vers comptes)
- compte_dest_id (FK vers comptes, nullable)
- type (depot, retrait, virement) - contrainte CHECK
- montant (décimal, > 0) - contrainte CHECK
- date_transaction (timestamp, valeur par défaut NOW)
- statut (en_cours, complete, annulee)
- Index sur compte_source_id et date_transaction

---

### Section 4: Java/POO (30 minutes)

**Question 11 (15 points):** Implémentez en Java:
- Classe abstraite `CompteBancaire` avec:
  - Attributs: numeroCompte, solde, titulaire (tous privés)
  - Constructeur
  - Méthode abstraite: `retirer(double montant): boolean`
  - Méthode concrète: `deposer(double montant): void`
  - Getters pour tous les attributs

- Classe `CompteEpargne` qui hérite de `CompteBancaire` avec:
  - Attribut: tauxInteret
  - Constructeur appelant super()
  - Implémentation de `retirer()` (max 3 retraits/mois)
  - Méthode `calculerInterets(): double`

**Question 12 (10 points):** Implémentez le pattern Singleton (thread-safe) pour une classe `Configuration`. Incluez:
- Constructeur privé
- Méthode statique `getInstance()`
- Classe interne statique (méthode Bill Pugh)

---

### Section 5: Algorithmes (30 minutes)

**Question 13 (10 points):** Implémentez l'algorithme Binary Search. Incluez:
- Paramètres: array trié, target
- Retour: index si trouvé, -1 sinon
- Commentaires expliquant la logique

**Question 14 (10 points):** Tracez l'exécution de Quick Sort pour le tableau [5, 2, 8, 1, 9]:
- Montrer chaque étape de partition
- Indiquer le pivot choisi
- Montrer les appels récursifs
- Array final trié

**Question 15 (10 points):** Implémentez BFS (Breadth-First Search) en pseudo-code ou Java. Inclure:
- Paramètres: graphe (liste d'adjacence), sommet de départ
- Utilisation d'une Queue
- Marquage des nœuds visités

---

## 🔍 Correction et Analyse (1 heure)

### Grille de correction

| Section | Points max | Mes points | % |
|---------|------------|------------|---|
| Théorie | 30 | | |
| UML | 25 | | |
| SQL | 30 | | |
| Java/POO | 25 | | |
| Algorithmes | 30 | | |
| **TOTAL** | **140** | | |

### Analyse des erreurs

Pour chaque erreur, noter:
1. **Type d'erreur:** Concept mal compris / Oubli / Erreur de syntaxe / Manque de temps
2. **Sujet:** SQL, Java, UML, etc.
3. **Action corrective:** Relire section X, refaire exercice Y, mémoriser Z

---

## 📚 Révision ciblée des points faibles (2 heures)

Selon les résultats de la simulation, **réviser prioritairement** les sujets où vous avez perdu le plus de points.

### Matrice de révision

| Score section | Action | Temps alloué |
|---------------|--------|--------------|
| **< 50%** | Révision INTENSIVE | 45 min |
| **50-70%** | Révision CIBLÉE | 30 min |
| **> 70%** | Survol rapide | 15 min |

### Plan de révision type

**Si faible en SQL:**
1. Relire `Jour1_BDD_SQL.md` (sections ACID, JOINs, Transactions)
2. Réécrire 5 requêtes sur papier
3. Tracer une transaction complète
4. Vérifier la syntaxe des contraintes

**Si faible en UML:**
1. Relire `Jour4_UML.md` (notation, relations, multiplicités)
2. Redessiner 2 diagrammes de classes
3. Refaire un diagramme de séquence
4. Mémoriser: agrégation (◇) vs composition (◆)

**Si faible en Java:**
1. Relire `OOP.md` et `Jour3_POO_SOLID.md`
2. Réécrire une classe complète avec héritage
3. Implémenter un pattern (Singleton, Factory)
4. Réviser overloading vs overriding

**Si faible en Algorithmes:**
1. Relire `Jour6_DSA_Algorithmes.md`
2. Tracer Binary Search étape par étape
3. Implémenter Quick Sort sur papier
4. Réviser BFS vs DFS

---

## ✍️ Réécriture des codes essentiels (2 heures)

### Liste des codes à réécrire PARFAITEMENT sur papier

#### SQL (30 min)
1. Transaction de virement avec BEGIN/COMMIT
2. Requête avec INNER JOIN (clients + comptes)
3. Agrégation avec GROUP BY et HAVING
4. CREATE TABLE avec contraintes

#### Java (45 min)
1. Classe avec encapsulation (constructeur, getters, setters)
2. Héritage avec extends et super()
3. Interface et implémentation
4. Singleton (méthode Bill Pugh)
5. ArrayList: add, get, remove, parcourir

#### Algorithmes (45 min)
1. Binary Search
2. Bubble Sort OU Quick Sort (partition)
3. BFS avec Queue
4. Stack (push, pop, peek)

### Méthode de réécriture

1. **Écrire de mémoire** (sans notes)
2. **Vérifier** avec le document source
3. **Corriger les erreurs** en rouge
4. **Réécrire proprement** la version corrigée
5. **Répéter** jusqu'à zéro erreur

---

## 📖 Relecture des fiches de synthèse (1 heure)

Relire lentement et attentivement `Fiches_Synthese.md`:

- ✅ ACID (4 propriétés)
- ✅ SOLID (5 principes)
- ✅ Big O courants
- ✅ HTTP codes (2xx, 4xx, 5xx)
- ✅ TCP vs UDP
- ✅ OSI 7 couches
- ✅ Box Model CSS
- ✅ XSS vs CSRF

**Techniques de mémorisation:**
- Répéter à voix haute
- Écrire les acronymes
- Créer des associations mentales
- Dessiner des schémas simplifiés

---

## 🧘 Repos et préparation mentale (1 heure)

### Checklist pré-examen

#### Matériel
- [ ] 3 stylos bleus/noirs (testés)
- [ ] Effaceur/correcteur blanc
- [ ] Règle pour UML
- [ ] Montre pour gérer le temps
- [ ] Bouteille d'eau
- [ ] Convocation (si nécessaire)

#### Mental
- [ ] Respiration profonde (5 min)
- [ ] Visualisation positive (se voir réussir)
- [ ] Confiance en la préparation
- [ ] Sommeil suffisant (8h)

#### Révision finale
- [ ] Relire fiches de synthèse (15 min max)
- [ ] Ne PAS apprendre de nouveau contenu
- [ ] Se détendre, ne pas stresser

---

## 💡 Stratégies pour le jour de l'examen

### Gestion du temps (examen 2-3h)

| Minutes | Activité |
|---------|----------|
| **0-5** | Lire TOUTES les questions, identifier les faciles |
| **5-10** | Planifier l'ordre de réponse |
| **10-90** | Répondre aux questions (commencer par les faciles) |
| **90-105** | Vérifier les réponses |
| **105-120** | Relecture finale, corrections |

### Priorités de réponse

1. **Questions que vous maîtrisez** (confiance élevée)
2. **Questions à points élevés** (bon ROI)
3. **Questions moyennes** (effort raisonnable)
4. **Questions difficiles** (si temps restant)

### Techniques d'écriture

**Pour le code:**
```java
// 1. Indentation claire
public class Compte {
    private double solde;  // 2. Commentaires si utiles
    
    public Compte(double solde) {
        this.solde = solde;  // 3. Syntaxe précise
    }
}
```

**Pour les diagrammes:**
- Utiliser une règle
- Étiqueter clairement
- Vérifier les multiplicités
- Triangle d'héritage vers le parent

**Pour les requêtes SQL:**
- Indentation des clauses
- Vérifier les parenthèses
- Tester mentalement le résultat
- Inclure les points-virgules

### En cas de blocage

1. **Passer à la question suivante** (ne pas perdre de temps)
2. **Revenir plus tard** avec un esprit frais
3. **Écrire ce que vous savez** (points partiels possibles)
4. **Montrer votre raisonnement** (commentaires, schémas)

### Gestion du stress

- Respirer profondément (4-7-8: inspirer 4s, retenir 7s, expirer 8s)
- Boire de l'eau
- Étirer les mains/poignets
- Se rappeler: "Je me suis bien préparé"

---

## 🔎 Extension: Rétention & Auto-évaluation

### 1) Barème personnel (auto-note /20)
- SQL (5) : requêtes correctes + syntaxe propre
- POO/SOLID (5) : définitions + exemple
- UML (4) : diagrammes lisibles + multiplicités
- Réseaux/Web (3) : OSI + HTTP + sécurité
- DSA (3) : structure + complexité

### 2) Révision express 30 minutes
- 10 min: Fiches de synthèse (ACID, SOLID, OSI)
- 10 min: 3 requêtes SQL manuscrites
- 10 min: 1 diagramme UML + 1 classe Java

### 3) Questions flash (réponse en 1 phrase)
- Différence classe abstraite vs interface
- Pourquoi `LEFT JOIN` et pas `INNER JOIN`
- Que signifie O(n log n)
- CORS: pourquoi et comment l'autoriser
- CSRF: prévention principale

---

## ✅ Checklist finale Jour 8

### Avant de dormir (28 janvier)

- [ ] Simulation d'examen complétée
- [ ] Points faibles identifiés et révisés
- [ ] Codes essentiels réécrits sans erreur
- [ ] Fiches de synthèse relues
- [ ] Matériel préparé
- [ ] Sommeil prévu (coucher avant 22h)

### Matin de l'examen (29 janvier)

- [ ] Réveil 2h avant l'examen
- [ ] Petit-déjeuner léger
- [ ] Relecture rapide des fiches (15 min max)
- [ ] Arrivée 15 min en avance
- [ ] Confiance et calme

---

## 🎓 Message final

Vous avez travaillé dur pendant 8 jours. Vous avez:
- ✅ Maîtrisé les bases de données et SQL
- ✅ Appris Java et la POO
- ✅ Compris les principes SOLID
- ✅ Pratiqué UML
- ✅ Étudié les structures de données et algorithmes
- ✅ Couvert le backend, networking et frontend

**Vous êtes prêt(e)!** 

Faites confiance à votre préparation. Respirez. Restez calme. Donnez le meilleur de vous-même.

**Bonne chance pour votre examen du 29 janvier! 🎯🚀**

---

**Prochain fichier:** `Fiches_Synthese.md` - Mémos ultra-rapides pour révision finale
