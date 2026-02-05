# Guide Complet Java pour Développeurs Python
## Préparation Examen OOP & DSA - Unibank Haiti

**Pour:** Alexandro Disla | **Java 21** | **Janvier 2026**

---

# TABLE DES MATIÈRES

1. [Java vs Python - Différences Fondamentales](#1-java-vs-python)
2. [Types et Variables](#2-types-et-variables)
3. [POO - Classes et Objets](#3-poo-classes-et-objets)
4. [Héritage et Polymorphisme](#4-héritage-et-polymorphisme)
5. [Interfaces et Classes Abstraites](#5-interfaces-et-classes-abstraites)
6. [Collections](#6-collections)
7. [Exceptions](#7-exceptions)
8. [Generics](#8-generics)
9. [Streams et Lambdas](#9-streams-et-lambdas)
10. [UML - Relations Expliquées](#10-uml-relations)
11. [DSA - Structures de Données](#11-dsa-structures)
12. [DSA - Algorithmes](#12-dsa-algorithmes)
13. [Design Patterns](#13-design-patterns)
14. [SOLID](#14-solid)
15. [Exercices et Aide-Mémoire](#15-exercices)

---

# 1. JAVA VS PYTHON - DIFFÉRENCES FONDAMENTALES

## 1.1 Comparaison Syntaxique

| Aspect | Python | Java |
|--------|--------|------|
| **Variable** | `x = 5` | `int x = 5;` |
| **Constante** | `X = 5` (convention) | `final int X = 5;` |
| **Print** | `print("Hello")` | `System.out.println("Hello");` |
| **Null** | `None` | `null` |
| **Boolean** | `True`, `False` | `true`, `false` ⚠️ |
| **Blocs** | Indentation | Accolades `{ }` |
| **Fin instruction** | Retour ligne | Point-virgule `;` |
| **Comparer strings** | `==` | `.equals()` ⚠️ |

## 1.2 Structure d'un Programme Java

```java
// Fichier: CompteBancaire.java
// Le nom du fichier DOIT correspondre au nom de la classe publique

package com.unibank.comptes;  // Package (optionnel mais recommandé)

import java.util.ArrayList;    // Imports nécessaires
import java.util.List;

public class CompteBancaire {  // Classe publique
    
    // Attributs (variables d'instance)
    private String numero;
    private double solde;
    
    // Constructeur
    public CompteBancaire(String numero, double soldeInitial) {
        this.numero = numero;
        this.solde = soldeInitial;
    }
    
    // Méthodes
    public void deposer(double montant) {
        if (montant > 0) {
            this.solde += montant;
        }
    }
    
    public double getSolde() {
        return this.solde;
    }
    
    // Point d'entrée du programme
    public static void main(String[] args) {
        CompteBancaire compte = new CompteBancaire("001", 1000);
        compte.deposer(500);
        System.out.println("Solde: " + compte.getSolde());  // 1500.0
    }
}
```

## 1.3 Compilation et Exécution

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Code Source   │     │    Bytecode     │     │    Exécution    │
│  (.java)        │────▶│   (.class)      │────▶│     (JVM)       │
│                 │     │                 │     │                 │
│ javac App.java  │     │   App.class     │     │  java App       │
└─────────────────┘     └─────────────────┘     └─────────────────┘
      Compilation             Portable           Machine Virtuelle
```

---

# 2. TYPES ET VARIABLES

## 2.1 Types Primitifs (8 types)

```java
// Entiers
byte age = 25;           // 8 bits:  -128 à 127
short annee = 2026;      // 16 bits: -32,768 à 32,767
int population = 11000000; // 32 bits: ±2.1 milliards
long distance = 9876543210L; // 64 bits - SUFFIXE L OBLIGATOIRE!

// Décimaux
float prix = 99.99f;     // 32 bits - SUFFIXE f OBLIGATOIRE!
double solde = 50000.50; // 64 bits (par défaut pour décimaux)

// Autres
boolean actif = true;    // true ou false (MINUSCULES!)
char grade = 'A';        // UN caractère entre guillemets simples
```

## 2.2 Types Objets (Wrappers)

```java
// Primitifs → Objets (nécessaire pour les Collections)
Integer ageObj = 25;           // int → Integer
Double soldeObj = 1000.0;      // double → Double
Boolean actifObj = true;       // boolean → Boolean
String nom = "Alexandro";      // String est TOUJOURS un objet

// ⚠️ PIÈGE COLLECTIONS:
ArrayList<int> nombres;        // ❌ ERREUR!
ArrayList<Integer> nombres;    // ✅ Correct!
```

## 2.3 Conversions

```java
// String → Primitif
int age = Integer.parseInt("25");
double prix = Double.parseDouble("99.99");

// Primitif → String
String ageStr = String.valueOf(25);
String ageStr2 = Integer.toString(25);
String ageStr3 = "" + 25;  // Concaténation

// Casting entre primitifs
int x = 10;
double y = x;      // Implicite (int → double) OK
int z = (int) 3.7; // Explicite (double → int) = 3 (troncature!)
```

## 2.4 Comparaison de Strings ⚠️ CRITIQUE

```java
String s1 = "Hello";
String s2 = "Hello";
String s3 = new String("Hello");

// == compare les RÉFÉRENCES (adresses mémoire)
System.out.println(s1 == s2);  // true (même objet en pool)
System.out.println(s1 == s3);  // false (objets différents!)

// .equals() compare le CONTENU
System.out.println(s1.equals(s2));  // true
System.out.println(s1.equals(s3));  // true ✅ TOUJOURS UTILISER

// Null-safe
System.out.println("Hello".equals(s1));  // Évite NullPointerException
```

---

# 3. POO - CLASSES ET OBJETS

## 3.1 Anatomie d'une Classe

```java
public class CompteBancaire {
    
    // ════════════════════════════════════════════════════════════
    // ATTRIBUTS (état de l'objet)
    // ════════════════════════════════════════════════════════════
    
    private String numero;        // Encapsulé (privé)
    private double solde;
    private String titulaire;
    private static int compteur = 0;  // Partagé entre toutes les instances
    
    // ════════════════════════════════════════════════════════════
    // CONSTRUCTEURS
    // ════════════════════════════════════════════════════════════
    
    // Constructeur principal
    public CompteBancaire(String numero, String titulaire, double soldeInitial) {
        this.numero = numero;          // this = instance courante
        this.titulaire = titulaire;
        this.solde = soldeInitial;
        compteur++;                    // Incrémenter le compteur statique
    }
    
    // Constructeur par défaut (surcharge)
    public CompteBancaire(String numero, String titulaire) {
        this(numero, titulaire, 0);    // Appel au constructeur principal
    }
    
    // ════════════════════════════════════════════════════════════
    // GETTERS (accès en lecture)
    // ════════════════════════════════════════════════════════════
    
    public String getNumero() {
        return numero;
    }
    
    public double getSolde() {
        return solde;
    }
    
    public String getTitulaire() {
        return titulaire;
    }
    
    public static int getCompteur() {  // Méthode statique pour attribut statique
        return compteur;
    }
    
    // ════════════════════════════════════════════════════════════
    // SETTERS (accès en écriture avec validation)
    // ════════════════════════════════════════════════════════════
    
    public void setTitulaire(String titulaire) {
        if (titulaire != null && !titulaire.isEmpty()) {
            this.titulaire = titulaire;
        }
    }
    
    // Pas de setSolde() - modification via deposer/retirer seulement!
    
    // ════════════════════════════════════════════════════════════
    // MÉTHODES MÉTIER
    // ════════════════════════════════════════════════════════════
    
    public void deposer(double montant) {
        if (montant > 0) {
            this.solde += montant;
        }
    }
    
    public boolean retirer(double montant) {
        if (montant > 0 && montant <= this.solde) {
            this.solde -= montant;
            return true;
        }
        return false;
    }
    
    // ════════════════════════════════════════════════════════════
    // toString() - Représentation textuelle
    // ════════════════════════════════════════════════════════════
    
    @Override
    public String toString() {
        return String.format("Compte[%s, %s, %.2f HTG]", 
                            numero, titulaire, solde);
    }
}
```

## 3.2 Modificateurs d'Accès

```
┌────────────────┬────────────┬────────────┬────────────┬────────────┐
│  Modificateur  │ Même classe│ Même package│ Sous-classe│  Partout   │
├────────────────┼────────────┼────────────┼────────────┼────────────┤
│    public      │     ✓      │     ✓      │     ✓      │     ✓      │
│   protected    │     ✓      │     ✓      │     ✓      │     ✗      │
│    (default)   │     ✓      │     ✓      │     ✗      │     ✗      │
│    private     │     ✓      │     ✗      │     ✗      │     ✗      │
└────────────────┴────────────┴────────────┴────────────┴────────────┘

Mnémonique:
- public   = Partout
- protected = Package + Progéniture (enfants)
- default  = Dans le package
- private  = Personnellement seulement
```

## 3.3 Static vs Instance

```java
public class Banque {
    
    // STATIC = appartient à la CLASSE (partagé)
    private static String nomBanque = "Unibank";
    private static int nombreComptes = 0;
    
    // INSTANCE = appartient à l'OBJET (unique par instance)
    private String codeAgence;
    private String adresse;
    
    public Banque(String codeAgence) {
        this.codeAgence = codeAgence;
        nombreComptes++;  // Modification de l'attribut statique
    }
    
    // Méthode STATIQUE - pas besoin d'instance
    public static int getNombreComptes() {
        return nombreComptes;
        // return codeAgence;  // ❌ ERREUR! Pas d'accès aux attributs d'instance
    }
    
    // Méthode d'INSTANCE - besoin d'un objet
    public String getInfo() {
        return nomBanque + " - " + codeAgence;  // Peut accéder aux deux
    }
}

// Utilisation
System.out.println(Banque.getNombreComptes());  // Appel statique (pas d'objet)

Banque agence1 = new Banque("PAP01");
System.out.println(agence1.getInfo());          // Appel d'instance (avec objet)
```

---

# 4. HÉRITAGE ET POLYMORPHISME

## 4.1 Héritage avec extends

```java
// ════════════════════════════════════════════════════════════════
// CLASSE PARENT (Superclasse)
// ════════════════════════════════════════════════════════════════

public class Compte {
    protected String numero;      // protected = accessible aux enfants
    protected double solde;
    protected String titulaire;
    
    public Compte(String numero, String titulaire, double solde) {
        this.numero = numero;
        this.titulaire = titulaire;
        this.solde = solde;
    }
    
    public void deposer(double montant) {
        if (montant > 0) {
            this.solde += montant;
        }
    }
    
    public boolean retirer(double montant) {
        if (montant > 0 && montant <= solde) {
            this.solde -= montant;
            return true;
        }
        return false;
    }
    
    public double getSolde() {
        return solde;
    }
}

// ════════════════════════════════════════════════════════════════
// CLASSE ENFANT (Sous-classe)
// ════════════════════════════════════════════════════════════════

public class CompteEpargne extends Compte {
    
    private double tauxInteret;
    private int retraitsRestants;
    
    public CompteEpargne(String numero, String titulaire, double solde, double taux) {
        super(numero, titulaire, solde);  // ⚠️ DOIT être la 1ère ligne!
        this.tauxInteret = taux;
        this.retraitsRestants = 3;
    }
    
    // Méthode REDÉFINIE (Override)
    @Override  // ⚠️ Annotation recommandée!
    public boolean retirer(double montant) {
        if (retraitsRestants <= 0) {
            return false;  // Plus de retraits autorisés
        }
        boolean success = super.retirer(montant);  // Appel à la méthode parent
        if (success) {
            retraitsRestants--;
        }
        return success;
    }
    
    // Méthode SPÉCIFIQUE à CompteEpargne
    public void appliquerInterets() {
        double interets = solde * tauxInteret;
        solde += interets;
    }
}

public class CompteCourant extends Compte {
    
    private double decouvertAutorise;
    
    public CompteCourant(String numero, String titulaire, double solde, double decouvert) {
        super(numero, titulaire, solde);
        this.decouvertAutorise = decouvert;
    }
    
    @Override
    public boolean retirer(double montant) {
        // Peut retirer jusqu'au découvert
        if (montant > 0 && montant <= (solde + decouvertAutorise)) {
            solde -= montant;
            return true;
        }
        return false;
    }
}
```

## 4.2 Polymorphisme

```java
public class BanqueService {
    
    // POLYMORPHISME: Accepte n'importe quel type de Compte
    public void effectuerRetrait(Compte compte, double montant) {
        if (compte.retirer(montant)) {
            System.out.println("Retrait réussi!");
        } else {
            System.out.println("Retrait refusé!");
        }
        // La méthode retirer() appelée dépend du TYPE RÉEL de l'objet
    }
    
    public static void main(String[] args) {
        BanqueService service = new BanqueService();
        
        // Même variable de type Compte, objets différents
        Compte compte1 = new CompteEpargne("E001", "Alice", 1000, 0.03);
        Compte compte2 = new CompteCourant("C001", "Bob", 500, 1000);
        
        // Même méthode, comportements différents!
        service.effectuerRetrait(compte1, 100);  // Logique CompteEpargne
        service.effectuerRetrait(compte2, 1400); // Logique CompteCourant (avec découvert)
        
        // Vérification de type
        if (compte1 instanceof CompteEpargne epargne) {  // Java 16+ pattern matching
            epargne.appliquerInterets();  // Méthode spécifique
        }
    }
}
```

---

# 5. INTERFACES ET CLASSES ABSTRAITES

## 5.1 Interface (Contrat Pur)

```java
// ════════════════════════════════════════════════════════════════
// INTERFACE = CONTRAT (que fait l'objet)
// ════════════════════════════════════════════════════════════════

public interface Transactionnable {
    
    // Méthodes abstraites (implicitement public abstract)
    boolean effectuerTransaction(double montant);
    void annulerTransaction(int transactionId);
    
    // Méthode par défaut (Java 8+)
    default void afficherHistorique() {
        System.out.println("Historique non disponible");
    }
    
    // Méthode statique
    static boolean estMontantValide(double montant) {
        return montant > 0 && montant < 1_000_000;
    }
}

public interface Auditable {
    void enregistrerAudit(String action);
}

// Une classe peut implémenter PLUSIEURS interfaces
public class CompteAudite extends Compte implements Transactionnable, Auditable {
    
    public CompteAudite(String numero, String titulaire, double solde) {
        super(numero, titulaire, solde);
    }
    
    @Override
    public boolean effectuerTransaction(double montant) {
        enregistrerAudit("Transaction: " + montant);
        return deposer(montant) || retirer(montant);
    }
    
    @Override
    public void annulerTransaction(int transactionId) {
        enregistrerAudit("Annulation: " + transactionId);
    }
    
    @Override
    public void enregistrerAudit(String action) {
        System.out.println("[AUDIT] " + action);
    }
}
```

## 5.2 Classe Abstraite (Implémentation Partielle)

```java
// ════════════════════════════════════════════════════════════════
// CLASSE ABSTRAITE = MODÈLE (comment l'objet fonctionne)
// ════════════════════════════════════════════════════════════════

public abstract class CompteAbstrait {
    
    protected String numero;
    protected double solde;
    
    // Constructeur (appelé par les sous-classes)
    public CompteAbstrait(String numero, double solde) {
        this.numero = numero;
        this.solde = solde;
    }
    
    // Méthode CONCRÈTE (implémentation fournie)
    public void deposer(double montant) {
        if (montant > 0) {
            solde += montant;
        }
    }
    
    // Méthode ABSTRAITE (pas d'implémentation - les sous-classes DOIVENT l'implémenter)
    public abstract boolean retirer(double montant);
    
    // Méthode ABSTRAITE
    public abstract double calculerFrais();
    
    // Méthode concrète utilisant méthode abstraite
    public void appliquerFraisMensuels() {
        double frais = calculerFrais();  // Appelle l'implémentation de la sous-classe
        solde -= frais;
    }
}

public class CompteEpargneImpl extends CompteAbstrait {
    
    public CompteEpargneImpl(String numero, double solde) {
        super(numero, solde);
    }
    
    @Override
    public boolean retirer(double montant) {
        if (montant <= solde) {
            solde -= montant;
            return true;
        }
        return false;
    }
    
    @Override
    public double calculerFrais() {
        return 0;  // Pas de frais pour épargne
    }
}
```

## 5.3 Interface vs Classe Abstraite

```
┌─────────────────────┬────────────────────────┬────────────────────────┐
│      Critère        │      INTERFACE         │   CLASSE ABSTRAITE     │
├─────────────────────┼────────────────────────┼────────────────────────┤
│ Mot-clé             │ interface              │ abstract class         │
│ Héritage            │ implements (multiple)  │ extends (simple)       │
│ Attributs           │ static final seulement │ Tous types             │
│ Constructeur        │ Non                    │ Oui                    │
│ Méthodes            │ Abstraites + default   │ Abstraites + concrètes │
│ Usage               │ CONTRAT (que faire)    │ MODÈLE (comment faire) │
├─────────────────────┼────────────────────────┼────────────────────────┤
│ QUAND UTILISER ?    │ Comportements partagés │ Code commun à partager │
│                     │ entre classes non      │ entre classes de même  │
│                     │ liées                  │ famille                │
└─────────────────────┴────────────────────────┴────────────────────────┘
```

---

# 6. COLLECTIONS

## 6.1 Hiérarchie des Collections

```
                    Iterable<E>
                        │
                   Collection<E>
                        │
        ┌───────────────┼───────────────┐
        │               │               │
     List<E>         Set<E>         Queue<E>
        │               │               │
   ┌────┴────┐     ┌────┴────┐     ┌────┴────┐
ArrayList  LinkedList  HashSet  TreeSet  LinkedList  ArrayDeque
                                              │
                                           Deque<E>
                                              │
                                          Stack<E>

               Map<K,V> (séparé)
                    │
        ┌───────────┴───────────┐
     HashMap               TreeMap
```

## 6.2 ArrayList (Liste Dynamique)

```java
import java.util.ArrayList;
import java.util.List;

public class ArrayListDemo {
    public static void main(String[] args) {
        
        // Création
        List<String> clients = new ArrayList<>();  // Interface comme type
        
        // Ajout - O(1) amorti
        clients.add("Alice");      // Index 0
        clients.add("Bob");        // Index 1
        clients.add("Charlie");    // Index 2
        clients.add(1, "David");   // Insert à l'index 1, décale les autres
        // [Alice, David, Bob, Charlie]
        
        // Accès - O(1)
        String premier = clients.get(0);     // "Alice"
        String dernier = clients.get(clients.size() - 1);  // "Charlie"
        
        // Modification - O(1)
        clients.set(0, "Alicia");  // Remplace "Alice" par "Alicia"
        
        // Recherche - O(n)
        boolean existe = clients.contains("Bob");  // true
        int index = clients.indexOf("Bob");        // 2
        
        // Suppression - O(n)
        clients.remove("David");       // Supprime par valeur
        clients.remove(0);             // Supprime par index
        
        // Taille
        int taille = clients.size();
        boolean vide = clients.isEmpty();
        
        // Parcours - for classique
        for (int i = 0; i < clients.size(); i++) {
            System.out.println(i + ": " + clients.get(i));
        }
        
        // Parcours - for-each (PRÉFÉRÉ)
        for (String client : clients) {
            System.out.println(client);
        }
        
        // Vider
        clients.clear();
    }
}
```

## 6.3 HashMap (Dictionnaire)

```java
import java.util.HashMap;
import java.util.Map;

public class HashMapDemo {
    public static void main(String[] args) {
        
        // Création
        Map<String, Double> soldes = new HashMap<>();
        
        // Ajout - O(1) moyen
        soldes.put("C001", 1000.0);
        soldes.put("C002", 2500.0);
        soldes.put("C003", 750.0);
        
        // Accès - O(1) moyen
        Double solde = soldes.get("C001");           // 1000.0
        Double solde2 = soldes.getOrDefault("C999", 0.0);  // 0.0 si absent
        
        // Vérification
        boolean existe = soldes.containsKey("C001");    // true
        boolean aValeur = soldes.containsValue(1000.0); // true
        
        // Modification
        soldes.put("C001", 1500.0);  // Remplace la valeur
        
        // Suppression
        soldes.remove("C003");
        
        // Taille
        int nombre = soldes.size();
        
        // Parcours - clés
        for (String numero : soldes.keySet()) {
            System.out.println(numero);
        }
        
        // Parcours - valeurs
        for (Double s : soldes.values()) {
            System.out.println(s);
        }
        
        // Parcours - entrées (RECOMMANDÉ)
        for (Map.Entry<String, Double> entry : soldes.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}
```

## 6.4 Comparaison des Collections

```
┌─────────────────┬──────────┬───────────┬───────────┬───────────┐
│    Structure    │  Accès   │ Recherche │ Insertion │Suppression│
├─────────────────┼──────────┼───────────┼───────────┼───────────┤
│   ArrayList     │   O(1)   │   O(n)    │ O(1)/O(n) │   O(n)    │
│   LinkedList    │   O(n)   │   O(n)    │   O(1)*   │   O(1)*   │
│   HashMap       │   N/A    │   O(1)    │   O(1)    │   O(1)    │
│   HashSet       │   N/A    │   O(1)    │   O(1)    │   O(1)    │
│   TreeMap       │   N/A    │ O(log n)  │ O(log n)  │ O(log n)  │
│   TreeSet       │   N/A    │ O(log n)  │ O(log n)  │ O(log n)  │
└─────────────────┴──────────┴───────────┴───────────┴───────────┘
* Si position connue
```

---

# 7. EXCEPTIONS

## 7.1 Hiérarchie des Exceptions

```
                    Throwable
                        │
            ┌───────────┴───────────┐
         Error                 Exception
     (ne pas attraper)              │
            │               ┌───────┴───────┐
      OutOfMemoryError  RuntimeException   IOException
      StackOverflowError     │             FileNotFoundException
                             │
                    ┌────────┼────────┐
              NullPointer  ArrayIndex  IllegalArgument
              Exception    OutOfBounds  Exception
                          Exception

CHECKED (vérifiées)    = Exception et sous-classes (sauf RuntimeException)
                         → DOIT être déclarée ou attrapée

UNCHECKED (non-vérifiées) = RuntimeException et sous-classes
                            → Pas obligatoire de déclarer/attraper
```

## 7.2 Try-Catch-Finally

```java
public class ExceptionDemo {
    
    public static double diviser(double a, double b) {
        if (b == 0) {
            throw new IllegalArgumentException("Division par zéro!");
        }
        return a / b;
    }
    
    public static void main(String[] args) {
        
        // Try-catch basique
        try {
            double resultat = diviser(10, 0);
            System.out.println(resultat);
        } catch (IllegalArgumentException e) {
            System.out.println("Erreur: " + e.getMessage());
        }
        
        // Multi-catch
        try {
            String str = null;
            str.length();  // NullPointerException
        } catch (NullPointerException | IllegalArgumentException e) {
            System.out.println("Erreur: " + e.getMessage());
        }
        
        // Try-catch-finally
        try {
            // Code risqué
        } catch (Exception e) {
            // Gestion de l'erreur
        } finally {
            // TOUJOURS exécuté (nettoyage)
            System.out.println("Nettoyage...");
        }
    }
}
```

## 7.3 Exception Personnalisée

```java
public class SoldeInsuffisantException extends Exception {
    
    private double soldeDemande;
    private double soldeDisponible;
    
    public SoldeInsuffisantException(String message, double demande, double disponible) {
        super(message);
        this.soldeDemande = demande;
        this.soldeDisponible = disponible;
    }
    
    public double getSoldeDemande() { return soldeDemande; }
    public double getSoldeDisponible() { return soldeDisponible; }
}

// Utilisation
public class CompteBancaire {
    private double solde;
    
    public void retirer(double montant) throws SoldeInsuffisantException {
        if (montant > solde) {
            throw new SoldeInsuffisantException(
                "Solde insuffisant!", montant, solde);
        }
        solde -= montant;
    }
}
```

---

# 8. GENERICS

## 8.1 Classe Générique

```java
// Classe générique - T est un "type parameter"
public class Boite<T> {
    private T contenu;
    
    public Boite(T contenu) {
        this.contenu = contenu;
    }
    
    public T getContenu() {
        return contenu;
    }
    
    public void setContenu(T contenu) {
        this.contenu = contenu;
    }
}

// Utilisation
Boite<String> boiteString = new Boite<>("Hello");
String s = boiteString.getContenu();  // Pas de cast nécessaire

Boite<Integer> boiteInt = new Boite<>(42);
Integer i = boiteInt.getContenu();

Boite<CompteBancaire> boiteCompte = new Boite<>(new CompteBancaire("001", "Alice", 1000));
```

## 8.2 Méthode Générique

```java
public class Utils {
    
    // Méthode générique
    public static <T> void afficher(T[] tableau) {
        for (T element : tableau) {
            System.out.println(element);
        }
    }
    
    // Méthode générique avec contrainte (bounded type)
    public static <T extends Number> double somme(List<T> nombres) {
        double total = 0;
        for (T nombre : nombres) {
            total += nombre.doubleValue();
        }
        return total;
    }
}
```

## 8.3 Wildcards

```java
// ? = type inconnu
public void afficherListe(List<?> liste) {
    for (Object o : liste) {
        System.out.println(o);
    }
}

// ? extends X = X ou sous-classe de X (lecture seule)
public double calculerTotal(List<? extends Number> nombres) {
    double total = 0;
    for (Number n : nombres) {
        total += n.doubleValue();
    }
    return total;
}

// ? super X = X ou super-classe de X (écriture possible)
public void ajouterNombres(List<? super Integer> liste) {
    liste.add(1);
    liste.add(2);
}
```

---

# 9. STREAMS ET LAMBDAS

## 9.1 Expressions Lambda

```java
// Lambda = fonction anonyme
// Syntaxe: (paramètres) -> expression ou { bloc }

// Interface fonctionnelle = 1 seule méthode abstraite
@FunctionalInterface
interface Calculateur {
    double calculer(double a, double b);
}

public class LambdaDemo {
    public static void main(String[] args) {
        
        // Avant Java 8 (classe anonyme)
        Calculateur addition1 = new Calculateur() {
            @Override
            public double calculer(double a, double b) {
                return a + b;
            }
        };
        
        // Avec Lambda
        Calculateur addition = (a, b) -> a + b;
        Calculateur multiplication = (a, b) -> a * b;
        
        System.out.println(addition.calculer(5, 3));        // 8.0
        System.out.println(multiplication.calculer(5, 3));  // 15.0
        
        // Lambda avec bloc
        Calculateur division = (a, b) -> {
            if (b == 0) {
                throw new IllegalArgumentException("Division par zéro!");
            }
            return a / b;
        };
    }
}
```

## 9.2 API Stream

```java
import java.util.*;
import java.util.stream.*;

public class StreamDemo {
    public static void main(String[] args) {
        
        List<Compte> comptes = List.of(
            new Compte("C001", "Alice", 5000),
            new Compte("C002", "Bob", 3000),
            new Compte("C003", "Charlie", 8000),
            new Compte("C004", "Alice", 2000),
            new Compte("C005", "Diana", 1500)
        );
        
        // ════════════════════════════════════════════════════════════
        // FILTER - Filtrer les éléments
        // ════════════════════════════════════════════════════════════
        List<Compte> grosComptes = comptes.stream()
            .filter(c -> c.getSolde() > 3000)
            .collect(Collectors.toList());
        
        // ════════════════════════════════════════════════════════════
        // MAP - Transformer les éléments
        // ════════════════════════════════════════════════════════════
        List<String> numeros = comptes.stream()
            .map(Compte::getNumero)  // Référence de méthode
            .collect(Collectors.toList());
        
        // ════════════════════════════════════════════════════════════
        // SORTED - Trier
        // ════════════════════════════════════════════════════════════
        List<Compte> tries = comptes.stream()
            .sorted(Comparator.comparingDouble(Compte::getSolde).reversed())
            .collect(Collectors.toList());
        
        // ════════════════════════════════════════════════════════════
        // REDUCE - Réduire à une valeur
        // ════════════════════════════════════════════════════════════
        double totalSoldes = comptes.stream()
            .mapToDouble(Compte::getSolde)
            .sum();
        
        // ════════════════════════════════════════════════════════════
        // GROUPING BY - Grouper
        // ════════════════════════════════════════════════════════════
        Map<String, List<Compte>> parTitulaire = comptes.stream()
            .collect(Collectors.groupingBy(Compte::getTitulaire));
        
        // ════════════════════════════════════════════════════════════
        // CHAÎNAGE - Combiner plusieurs opérations
        // ════════════════════════════════════════════════════════════
        String rapport = comptes.stream()
            .filter(c -> c.getSolde() > 2000)
            .sorted(Comparator.comparingDouble(Compte::getSolde).reversed())
            .map(c -> c.getNumero() + ": " + c.getSolde())
            .collect(Collectors.joining("\n"));
        
        System.out.println(rapport);
    }
}
```

---

# 10. UML - RELATIONS EXPLIQUÉES

## 10.1 Les 6 Types de Relations

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        RELATIONS UML                                     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. ASSOCIATION  ──────────────  "utilise" ou "connaît"                 │
│                                                                          │
│  2. AGRÉGATION   ◇─────────────  "a-un" (parties INDÉPENDANTES)         │
│                  losange VIDE                                            │
│                                                                          │
│  3. COMPOSITION  ◆─────────────  "possède" (parties DÉPENDANTES)        │
│                  losange PLEIN                                           │
│                                                                          │
│  4. HÉRITAGE     ─────────────▷  "est-un" (extends)                     │
│                  triangle VIDE pointe vers PARENT                        │
│                                                                          │
│  5. RÉALISATION  ─ ─ ─ ─ ─ ─ ▷  "implémente" (implements)               │
│                  pointillé + triangle                                    │
│                                                                          │
│  6. DÉPENDANCE   - - - - - - ->  "utilise temporairement"               │
│                  pointillé + flèche simple                               │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 10.2 Agrégation vs Composition

```
════════════════════════════════════════════════════════════════════════════
AGRÉGATION (◇) - "Losange VIDE = partie peut PARTIR"
════════════════════════════════════════════════════════════════════════════

Université ◇────────── Professeur
    │                      │
    │                      └─ Le professeur PEUT exister sans l'université
    └─ Si l'université ferme, les professeurs existent encore

Java:
class Universite {
    private List<Professeur> professeurs;
    
    public void ajouterProfesseur(Professeur p) {
        professeurs.add(p);  // Reçoit une référence externe
    }
}

════════════════════════════════════════════════════════════════════════════
COMPOSITION (◆) - "Losange PLEIN = partie PRISONNIÈRE"
════════════════════════════════════════════════════════════════════════════

Maison ◆────────── Chambre
   │                  │
   │                  └─ La chambre NE PEUT PAS exister sans la maison
   └─ Si la maison est détruite, les chambres le sont aussi

Java:
class Maison {
    private List<Chambre> chambres;
    
    public Maison(int nombreChambres) {
        chambres = new ArrayList<>();
        for (int i = 0; i < nombreChambres; i++) {
            chambres.add(new Chambre());  // Crée les chambres
        }
    }
}
```

## 10.3 Mnémonique pour Retenir

```
┌───────────────────────────────────────────────────────────────────┐
│                    MNÉMONIQUES UML                                 │
├───────────────────────────────────────────────────────────────────┤
│                                                                    │
│  ◇ AGRÉGATION   = Losange VIDE = partie peut VIVRE seule          │
│                   "Le professeur peut quitter l'université"        │
│                                                                    │
│  ◆ COMPOSITION  = Losange PLEIN = partie est LIÉE au tout         │
│                   "La chambre meurt avec la maison"                │
│                                                                    │
│  △ HÉRITAGE     = Triangle pointe vers le PARENT (le plus général)│
│                   "L'enfant montre son père"                       │
│                                                                    │
│  ▷ RÉALISATION  = Pointillé = connexion ABSTRAITE (interface)     │
│                   "Ligne en pointillé = promesse non concrète"     │
│                                                                    │
└───────────────────────────────────────────────────────────────────┘
```

## 10.4 Exemple Complet: Système Bancaire

```
┌─────────────────────┐
│    «interface»      │
│   Transactionnable  │
├─────────────────────┤
│ + effectuer(): bool │
│ + annuler(): void   │
└─────────┬───────────┘
          │
          │ implémente (réalisation)
          ▽ (pointillé)
┌─────────────────────┐         ┌─────────────────────┐
│       Banque        │◇────────│       Client        │
├─────────────────────┤   gère  ├─────────────────────┤
│ - nom: String       │   1..*  │ - nom: String       │
│ - code: String      │         │ - email: String     │
├─────────────────────┤         ├─────────────────────┤
│ + ajouterClient()   │         │ + getComptes()      │
└─────────────────────┘         └──────────┬──────────┘
                                           │
                                           │ possède
                                           │ 1..*
                                           ▼
                                ┌─────────────────────┐
                                │  «abstract»         │
                                │     Compte          │
                                ├─────────────────────┤
                                │ # numero: String    │
                                │ # solde: double     │
                                ├─────────────────────┤
                                │ + deposer()         │
                                │ + retirer(): bool   │
                                └──────────┬──────────┘
                                           △
                        ┌──────────────────┼──────────────────┐
                        │                  │                  │
              ┌─────────┴─────────┐ ┌──────┴──────┐ ┌────────┴────────┐
              │  CompteEpargne    │ │CompteCourant│ │  CompteCredit   │
              ├───────────────────┤ ├─────────────┤ ├─────────────────┤
              │ - tauxInteret     │ │ - decouvert │ │ - limiteCredit  │
              ├───────────────────┤ ├─────────────┤ ├─────────────────┤
              │ + appliquerInteret│ │             │ │ + calculerMin() │
              └───────────────────┘ └──────┬──────┘ └─────────────────┘
                                           │
                                           ◆ contient
                                           │ 0..*
                                           ▼
                                ┌─────────────────────┐
                                │    Transaction      │
                                ├─────────────────────┤
                                │ - id: int           │
                                │ - montant: double   │
                                │ - date: LocalDate   │
                                ├─────────────────────┤
                                │ + valider(): bool   │
                                └─────────────────────┘
```

---

# 11. DSA - STRUCTURES DE DONNÉES

## 11.1 Stack (Pile) - LIFO

```java
import java.util.ArrayDeque;
import java.util.Deque;

// Stack = Last In, First Out
// Comme une pile d'assiettes

Deque<Integer> stack = new ArrayDeque<>();

stack.push(10);   // [10]
stack.push(20);   // [20, 10]
stack.push(30);   // [30, 20, 10] ← 30 au sommet

int top = stack.peek();  // 30 (voir sans retirer)
int out = stack.pop();   // 30 (retirer) → stack = [20, 10]

// Complexités: push O(1), pop O(1), peek O(1)
```

## 11.2 Queue (File) - FIFO

```java
import java.util.LinkedList;
import java.util.Queue;

// Queue = First In, First Out
// Comme une file d'attente

Queue<String> queue = new LinkedList<>();

queue.offer("Client1");  // [Client1]
queue.offer("Client2");  // [Client1, Client2]
queue.offer("Client3");  // [Client1, Client2, Client3]

String first = queue.peek();   // "Client1" (voir sans retirer)
String out = queue.poll();     // "Client1" (retirer) → [Client2, Client3]

// Complexités: offer O(1), poll O(1), peek O(1)
```

## 11.3 Complexités Big O

```
┌────────────┬─────────────────────────────────────┬───────────────────┐
│ Complexité │           Visualisation             │     Exemple       │
├────────────┼─────────────────────────────────────┼───────────────────┤
│   O(1)     │ █                                   │ Accès tableau[i]  │
│   O(log n) │ ██                                  │ Binary Search     │
│   O(n)     │ ██████████                          │ Parcours liste    │
│ O(n log n) │ ██████████████████                  │ Merge Sort        │
│   O(n²)    │ ████████████████████████████████████│ Bubble Sort       │
└────────────┴─────────────────────────────────────┴───────────────────┘

ORDRE: O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2^n)
```

---

# 12. DSA - ALGORITHMES

## 12.1 Binary Search - O(log n)

```java
// PRÉREQUIS: Tableau TRIÉ!
public static int binarySearch(int[] arr, int target) {
    int left = 0;
    int right = arr.length - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;  // Évite overflow
        
        if (arr[mid] == target) {
            return mid;  // Trouvé!
        }
        if (arr[mid] < target) {
            left = mid + 1;  // Chercher à droite
        } else {
            right = mid - 1; // Chercher à gauche
        }
    }
    return -1;  // Non trouvé
}
```

## 12.2 Bubble Sort - O(n²)

```java
public static void bubbleSort(int[] arr) {
    int n = arr.length;
    for (int i = 0; i < n - 1; i++) {
        boolean swapped = false;
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = true;
            }
        }
        if (!swapped) break;  // Déjà trié
    }
}
```

## 12.3 Quick Sort - O(n log n)

```java
public static void quickSort(int[] arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

private static int partition(int[] arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;
    return i + 1;
}
```

## 12.4 BFS et DFS

```java
// BFS = Breadth-First Search = QUEUE = Parcours en LARGEUR
public void bfs(int start) {
    Set<Integer> visited = new HashSet<>();
    Queue<Integer> queue = new LinkedList<>();
    
    visited.add(start);
    queue.offer(start);
    
    while (!queue.isEmpty()) {
        int node = queue.poll();
        System.out.print(node + " ");
        
        for (int neighbor : graph.get(node)) {
            if (!visited.contains(neighbor)) {
                visited.add(neighbor);
                queue.offer(neighbor);
            }
        }
    }
}

// DFS = Depth-First Search = STACK/Récursion = Parcours en PROFONDEUR
public void dfs(int node, Set<Integer> visited) {
    visited.add(node);
    System.out.print(node + " ");
    
    for (int neighbor : graph.get(node)) {
        if (!visited.contains(neighbor)) {
            dfs(neighbor, visited);
        }
    }
}
```

---

# 13. DESIGN PATTERNS

## 13.1 Singleton

```java
public class Configuration {
    
    private Configuration() { }  // Constructeur privé
    
    private static class Holder {
        private static final Configuration INSTANCE = new Configuration();
    }
    
    public static Configuration getInstance() {
        return Holder.INSTANCE;
    }
}
```

## 13.2 Factory

```java
public interface Compte { }
public class CompteEpargne implements Compte { }
public class CompteCourant implements Compte { }

public class CompteFactory {
    public static Compte creer(String type) {
        return switch (type) {
            case "EPARGNE" -> new CompteEpargne();
            case "COURANT" -> new CompteCourant();
            default -> throw new IllegalArgumentException();
        };
    }
}
```

## 13.3 Observer

```java
interface Observer { void update(String message); }

class Subject {
    private List<Observer> observers = new ArrayList<>();
    
    public void addObserver(Observer o) { observers.add(o); }
    
    public void notifyAll(String msg) {
        for (Observer o : observers) o.update(msg);
    }
}
```

---

# 14. SOLID

```
┌─────────────────────────────────────────────────────────────────────────┐
│ S - Single Responsibility: Une classe = une responsabilité              │
│     ❌ Classe fait tout: calcul, sauvegarde, affichage                  │
│     ✅ Classes séparées: Calculateur, Repository, Vue                   │
├─────────────────────────────────────────────────────────────────────────┤
│ O - Open/Closed: Ouvert à l'extension, fermé à la modification          │
│     ❌ Modifier la classe existante pour ajouter une fonctionnalité     │
│     ✅ Créer une nouvelle sous-classe ou implémenter une interface      │
├─────────────────────────────────────────────────────────────────────────┤
│ L - Liskov Substitution: Les sous-classes substituables aux parents     │
│     ❌ Carré extends Rectangle (viole les invariants)                   │
│     ✅ Carré et Rectangle implémentent Forme                            │
├─────────────────────────────────────────────────────────────────────────┤
│ I - Interface Segregation: Pas de méthodes inutiles dans les interfaces │
│     ❌ Interface énorme avec méthodes non utilisées                     │
│     ✅ Petites interfaces spécifiques                                   │
├─────────────────────────────────────────────────────────────────────────┤
│ D - Dependency Inversion: Dépendre des abstractions, pas des concrétions│
│     ❌ class Service { private MySQLDb db = new MySQLDb(); }            │
│     ✅ class Service { private Database db; /* injection */ }           │
└─────────────────────────────────────────────────────────────────────────┘
```

---

# 15. AIDE-MÉMOIRE FINAL

## Pièges Java Courants

| Piège | Erreur | Correction |
|-------|--------|------------|
| Comparer Strings | `s1 == s2` | `s1.equals(s2)` ✅ |
| Boolean | `True/False` | `true/false` ✅ |
| Oublier `;` | Erreur compilation | Toujours terminer `;` |
| Collections | `ArrayList<int>` | `ArrayList<Integer>` ✅ |
| super() | Après du code | En 1ère ligne du constructeur ✅ |
| Override | Oublier annotation | Toujours `@Override` ✅ |

## Checklist Examen

- [ ] `true/false` (minuscules)
- [ ] `.equals()` pour Strings
- [ ] Point-virgule `;`
- [ ] `super()` en première ligne
- [ ] `@Override` pour redéfinition
- [ ] Triangle héritage → PARENT
- [ ] Losange vide ◇ = agrégation
- [ ] Losange plein ◆ = composition
- [ ] BFS = Queue, DFS = Stack
- [ ] O(1) < O(log n) < O(n) < O(n²)

---

**🎯 BONNE CHANCE POUR TON EXAMEN!**
