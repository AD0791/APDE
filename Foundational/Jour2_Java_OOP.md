# Jour 2 (22 janvier): Java OOP - Transition depuis Python

**Temps estimé:** 6-8 heures  
**Priorité:** 🔴 CRITIQUE - Java est souvent testé en bancaire

---

## 🎯 Pourquoi Java est critique pour cet examen

Bien que vous maîtrisiez Python, les examens bancaires haïtiens favorisent souvent Java pour:
- **Typage statique**: Moins d'erreurs à l'exécution
- **Robustesse**: Gestion explicite des exceptions
- **Performance**: Compilé vs interprété
- **Écosystème bancaire**: Spring, Hibernate très utilisés

Ce jour se concentre sur la **syntaxe Java** et les **différences clés avec Python**.

---

## 📊 Tableau de conversion Python → Java

| Concept | Python | Java |
|---------|--------|------|
| **Déclaration variable** | `name = "John"` | `String name = "John";` |
| **Constante** | `NAME = "John"` | `final String NAME = "John";` |
| **Print** | `print("Hello")` | `System.out.println("Hello");` |
| **Terminateur** | Aucun (retour ligne) | **Point-virgule `;`** obligatoire |
| **Blocs de code** | Indentation | **Accolades `{ }`** |
| **Commentaires** | `# commentaire` | `// ligne` ou `/* bloc */` |
| **Null** | `None` | `null` |
| **Boolean** | `True/False` | `true/false` (minuscules!) |
| **Type dynamique** | `x = 5` puis `x = "hello"` | Impossible - type fixe |
| **Héritage multiple** | `class C(A, B)` | Impossible - utiliser interfaces |

---

## 🔐 Modificateurs d'accès (n'existent PAS en Python)

| Modificateur | Même classe | Même package | Sous-classe | Partout |
|--------------|-------------|--------------|-------------|---------|
| `public` | ✓ | ✓ | ✓ | ✓ |
| `protected` | ✓ | ✓ | ✓ | ✗ |
| `default` (rien) | ✓ | ✓ | ✗ | ✗ |
| `private` | ✓ | ✗ | ✗ | ✗ |

**Mnémonique:**
- **`public`** = **P**artout
- **`protected`** = **P**arent et enfants
- **`default`** = **D**ans le package
- **`private`** = **P**ersonnellement seulement

---

## 🎲 Types de données primitifs vs Objets

### Types primitifs (8)
```java
// Entiers
byte age = 25;        // -128 à 127
short annee = 2026;   // -32,768 à 32,767
int population = 11000000;
long distance = 9876543210L;  // Suffixe L obligatoire

// Décimaux
float prix = 99.99f;  // Suffixe f obligatoire
double solde = 50000.50;

// Autres
boolean actif = true;
char grade = 'A';     // Simple quote pour char
```

### Wrappers (pour collections)
```java
Integer age = 25;     // Auto-boxing: int → Integer
Double solde = 50000.50;
String nom = "Jean";  // String est TOUJOURS un objet

// Pourquoi utiliser wrappers?
ArrayList<Integer> ages = new ArrayList<>();  // Generics exigent des objets
// ArrayList<int> ages = new ArrayList<>();   // ❌ ERREUR!
```

### Conversion string ↔ primitif
```java
// String → primitif
int age = Integer.parseInt("25");
double prix = Double.parseDouble("99.99");
boolean actif = Boolean.parseBoolean("true");

// Primitif → String
String ageStr = String.valueOf(25);
String prixStr = String.valueOf(99.99);
```

---

## 📦 Templates Java à MÉMORISER

### Template 1: Classe de base avec encapsulation

```java
public class Employe {
    // Champs privés (encapsulation)
    private String nom;
    private int age;
    private double salaire;
    
    // Constructeur
    public Employe(String nom, int age, double salaire) {
        this.nom = nom;
        this.age = age;
        this.salaire = salaire;
    }
    
    // Constructeur par défaut
    public Employe() {
        this.nom = "Inconnu";
        this.age = 0;
        this.salaire = 0.0;
    }
    
    // Getters
    public String getNom() {
        return nom;
    }
    
    public int getAge() {
        return age;
    }
    
    public double getSalaire() {
        return salaire;
    }
    
    // Setters avec validation
    public void setNom(String nom) {
        if (nom != null && !nom.isEmpty()) {
            this.nom = nom;
        }
    }
    
    public void setAge(int age) {
        if (age >= 18 && age <= 70) {
            this.age = age;
        }
    }
    
    public void setSalaire(double salaire) {
        if (salaire >= 0) {
            this.salaire = salaire;
        }
    }
    
    // Méthode métier
    public double calculerSalaireAnnuel() {
        return salaire * 12;
    }
    
    // toString() pour affichage
    @Override
    public String toString() {
        return "Employe{" +
               "nom='" + nom + '\'' +
               ", age=" + age +
               ", salaire=" + salaire +
               '}';
    }
}
```

### Template 2: Méthode main (point d'entrée)

```java
public class Main {
    public static void main(String[] args) {
        // Créer un objet
        Employe emp = new Employe("Jean", 30, 5000.0);
        
        // Utiliser getters
        System.out.println("Nom: " + emp.getNom());
        System.out.println("Salaire annuel: " + emp.calculerSalaireAnnuel());
        
        // Utiliser setters
        emp.setSalaire(5500.0);
        
        // Afficher avec toString()
        System.out.println(emp);
    }
}
```

### Template 3: Interface et implémentation

```java
// Interface (contrat)
public interface Imprimable {
    void imprimer();  // Méthode abstraite (pas de corps)
    void exporterPDF();
    
    // Java 8+: méthode par défaut
    default void afficherInfo() {
        System.out.println("Document imprimable");
    }
}

// Implémentation
public class Document implements Imprimable {
    private String contenu;
    
    public Document(String contenu) {
        this.contenu = contenu;
    }
    
    @Override  // Annotation obligatoire
    public void imprimer() {
        System.out.println("Impression: " + contenu);
    }
    
    @Override
    public void exporterPDF() {
        System.out.println("Export PDF: " + contenu);
    }
    
    // afficherInfo() héritée de l'interface (optionnel de redéfinir)
}

// Utilisation
public class Test {
    public static void main(String[] args) {
        Imprimable doc = new Document("Rapport Q4");
        doc.imprimer();
        doc.afficherInfo();
    }
}
```

### Template 4: Héritage avec extends

```java
// Classe parent (superclasse)
public class Animal {
    protected String nom;  // protected = accessible aux enfants
    private int age;
    
    public Animal(String nom, int age) {
        this.nom = nom;
        this.age = age;
    }
    
    public void faireSon() {
        System.out.println("Un son...");
    }
    
    public void dormir() {
        System.out.println(nom + " dort.");
    }
    
    public int getAge() {
        return age;
    }
}

// Classe enfant (sous-classe)
public class Chien extends Animal {
    private String race;
    
    // Constructeur enfant
    public Chien(String nom, int age, String race) {
        super(nom, age);  // Appelle constructeur parent EN PREMIER
        this.race = race;
    }
    
    // Redéfinition (Override)
    @Override
    public void faireSon() {
        System.out.println(nom + " aboie: Woof!");
    }
    
    // Méthode spécifique au chien
    public void remuerQueue() {
        System.out.println(nom + " remue la queue.");
    }
    
    // dormir() héritée sans modification
}

// Utilisation
public class Test {
    public static void main(String[] args) {
        Chien rex = new Chien("Rex", 3, "Berger Allemand");
        rex.faireSon();       // Version redéfinie
        rex.dormir();         // Version héritée
        rex.remuerQueue();    // Méthode spécifique
        System.out.println(rex.getAge());  // Getter hérité
    }
}
```

### Template 5: Classe abstraite

```java
// Classe abstraite (ne peut pas être instanciée)
public abstract class Forme {
    protected String couleur;
    
    public Forme(String couleur) {
        this.couleur = couleur;
    }
    
    // Méthode abstraite (pas d'implémentation)
    public abstract double calculerAire();
    public abstract double calculerPerimetre();
    
    // Méthode concrète (avec implémentation)
    public void afficherCouleur() {
        System.out.println("Couleur: " + couleur);
    }
}

// Sous-classe concrète
public class Rectangle extends Forme {
    private double largeur;
    private double hauteur;
    
    public Rectangle(String couleur, double largeur, double hauteur) {
        super(couleur);
        this.largeur = largeur;
        this.hauteur = hauteur;
    }
    
    @Override
    public double calculerAire() {
        return largeur * hauteur;
    }
    
    @Override
    public double calculerPerimetre() {
        return 2 * (largeur + hauteur);
    }
}

// Utilisation
public class Test {
    public static void main(String[] args) {
        // Forme f = new Forme("rouge");  // ❌ ERREUR: classe abstraite
        Forme rect = new Rectangle("bleu", 5, 3);  // ✅ OK
        System.out.println("Aire: " + rect.calculerAire());
        rect.afficherCouleur();
    }
}
```

---

## 📚 Collections Java essentielles

### ArrayList - Liste dynamique

```java
import java.util.ArrayList;

public class ExempleArrayList {
    public static void main(String[] args) {
        // Créer une ArrayList
        ArrayList<String> fruits = new ArrayList<>();
        
        // Ajouter des éléments
        fruits.add("Pomme");        // Index 0
        fruits.add("Banane");       // Index 1
        fruits.add("Orange");       // Index 2
        
        // Accéder à un élément
        String premier = fruits.get(0);  // "Pomme"
        
        // Modifier un élément
        fruits.set(1, "Mangue");  // Remplace "Banane" par "Mangue"
        
        // Supprimer
        fruits.remove("Orange");       // Suppression par valeur
        fruits.remove(0);              // Suppression par index
        
        // Taille
        int taille = fruits.size();
        
        // Vérifier existence
        boolean exists = fruits.contains("Pomme");
        
        // Parcourir - Méthode 1: for classique
        for (int i = 0; i < fruits.size(); i++) {
            System.out.println(fruits.get(i));
        }
        
        // Parcourir - Méthode 2: for-each (préféré)
        for (String fruit : fruits) {
            System.out.println(fruit);
        }
        
        // Vider la liste
        fruits.clear();
        
        // Vérifier si vide
        boolean estVide = fruits.isEmpty();
    }
}
```

### HashMap - Dictionnaire clé-valeur

```java
import java.util.HashMap;
import java.util.Map;

public class ExempleHashMap {
    public static void main(String[] args) {
        // Créer un HashMap
        HashMap<String, Integer> scores = new HashMap<>();
        
        // Ajouter des paires clé-valeur
        scores.put("Alice", 95);
        scores.put("Bob", 87);
        scores.put("Charlie", 92);
        
        // Accéder à une valeur
        int scoreAlice = scores.get("Alice");  // 95
        
        // Vérifier l'existence d'une clé
        boolean exists = scores.containsKey("Alice");
        
        // Vérifier l'existence d'une valeur
        boolean hasScore95 = scores.containsValue(95);
        
        // Modifier une valeur
        scores.put("Alice", 98);  // Écrase l'ancienne valeur
        
        // Supprimer
        scores.remove("Bob");
        
        // Taille
        int nombre = scores.size();
        
        // Parcourir - Méthode 1: keySet()
        for (String nom : scores.keySet()) {
            System.out.println(nom + ": " + scores.get(nom));
        }
        
        // Parcourir - Méthode 2: entrySet() (préféré)
        for (Map.Entry<String, Integer> entry : scores.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
        
        // Obtenir valeur avec défaut
        int scoreDavid = scores.getOrDefault("David", 0);  // 0 si absent
    }
}
```

---

## ⚔️ Overloading vs Overriding

| | Overloading (Surcharge) | Overriding (Redéfinition) |
|-|-------------------------|---------------------------|
| **Quand** | Compilation (static) | Exécution (dynamic) |
| **Où** | Même classe | Classe parent-enfant |
| **Signature** | Paramètres DIFFÉRENTS | Signature IDENTIQUE |
| **Nom** | Même nom | Même nom |
| **Annotation** | Aucune | `@Override` (recommandé) |
| **But** | Fournir plusieurs versions | Modifier comportement parent |

### Overloading (Surcharge)
```java
public class Calculatrice {
    // Même nom, paramètres différents
    public int additionner(int a, int b) {
        return a + b;
    }
    
    public double additionner(double a, double b) {
        return a + b;
    }
    
    public int additionner(int a, int b, int c) {
        return a + b + c;
    }
    
    // Le compilateur choisit la bonne version selon les arguments
}

public class Test {
    public static void main(String[] args) {
        Calculatrice calc = new Calculatrice();
        System.out.println(calc.additionner(5, 3));        // Appelle version 1
        System.out.println(calc.additionner(5.5, 3.2));    // Appelle version 2
        System.out.println(calc.additionner(1, 2, 3));     // Appelle version 3
    }
}
```

### Overriding (Redéfinition)
```java
class Animal {
    public void parler() {
        System.out.println("Un son animal...");
    }
    
    public void manger() {
        System.out.println("L'animal mange.");
    }
}

class Chien extends Animal {
    // Redéfinition - même signature exacte
    @Override
    public void parler() {
        System.out.println("Woof! Woof!");
    }
    
    // manger() héritée sans modification
}

public class Test {
    public static void main(String[] args) {
        Animal a = new Chien();  // Polymorphisme!
        a.parler();  // Affiche "Woof! Woof!" (version du Chien)
        a.manger();  // Affiche "L'animal mange." (version d'Animal)
    }
}
```

---

## 🔀 Comparaison Python vs Java - Exemple complet

### Python
```python
class Compte:
    def __init__(self, numero, solde):
        self._numero = numero
        self._solde = solde
    
    def deposer(self, montant):
        if montant > 0:
            self._solde += montant
            return True
        return False
    
    def retirer(self, montant):
        if montant > 0 and self._solde >= montant:
            self._solde -= montant
            return True
        return False
    
    def get_solde(self):
        return self._solde

# Utilisation
compte = Compte("123", 1000)
compte.deposer(500)
print(compte.get_solde())
```

### Java équivalent
```java
public class Compte {
    private String numero;
    private double solde;
    
    public Compte(String numero, double solde) {
        this.numero = numero;
        this.solde = solde;
    }
    
    public boolean deposer(double montant) {
        if (montant > 0) {
            this.solde += montant;
            return true;
        }
        return false;
    }
    
    public boolean retirer(double montant) {
        if (montant > 0 && this.solde >= montant) {
            this.solde -= montant;
            return true;
        }
        return false;
    }
    
    public double getSolde() {
        return this.solde;
    }
    
    public String getNumero() {
        return this.numero;
    }
}

// Utilisation
public class Test {
    public static void main(String[] args) {
        Compte compte = new Compte("123", 1000);
        compte.deposer(500);
        System.out.println(compte.getSolde());
    }
}
```

---

## ⚠️ Pièges Java courants en examen écrit

| Piège | Pourquoi c'est faux | Correction |
|-------|---------------------|------------|
| `True/False` | Python, pas Java | `true/false` (minuscules) |
| `Oublier ;` | Syntaxe invalide | Terminer CHAQUE instruction |
| `==` pour strings | Compare références, pas contenu | Utiliser `.equals()` |
| `ArrayList<int>` | Generics exigent des objets | `ArrayList<Integer>` |
| Oublier `@Override` | Pas obligatoire mais recommandé | Toujours mettre pour clarté |
| `super()` après du code | Doit être la 1ère ligne du constructeur | Mettre en premier |
| Oublier `import` | Classes pas trouvées | `import java.util.ArrayList;` |
| `this` vs `super` | Confusion | `this` = classe actuelle, `super` = parent |

---

## 📝 Exercices pratiques Jour 2

### Exercice 1: Classe simple
**Sur papier, écrire:**
Une classe `CompteBancaire` avec:
- Attributs privés: `numeroCompte` (String), `solde` (double), `titulaire` (String)
- Constructeur avec les 3 paramètres
- Getters pour tous les attributs
- Setter pour `titulaire` uniquement
- Méthode `deposer(double montant)` qui retourne boolean
- Méthode `retirer(double montant)` qui vérifie le solde

### Exercice 2: Héritage
**Sur papier, écrire:**
- Classe `CompteEpargne` qui hérite de `CompteBancaire`
- Ajouter attribut `tauxInteret` (double)
- Constructeur appelant `super()`
- Méthode `calculerInterets()` retournant double

### Exercice 3: Interface
**Sur papier, écrire:**
- Interface `Transactionable` avec méthodes `effectuerTransaction(double)` et `annulerTransaction()`
- Faire implémenter cette interface par `CompteBancaire`

### Exercice 4: Collections
**Sur papier, écrire le code pour:**
1. Créer une ArrayList de comptes bancaires
2. Ajouter 3 comptes
3. Parcourir la liste et afficher les numéros de compte
4. Créer un HashMap<String, Compte> avec numéro comme clé

---

## ✅ Checklist de révision Jour 2

Avant de passer au Jour 3, vérifier que vous pouvez:

- [ ] Écrire une classe Java complète avec constructeur, getters, setters
- [ ] Différencier types primitifs et wrappers
- [ ] Utiliser les 4 modificateurs d'accès (public, private, protected, default)
- [ ] Implémenter une interface avec `implements`
- [ ] Créer un héritage avec `extends` et utiliser `super()`
- [ ] Redéfinir une méthode avec `@Override`
- [ ] Différencier overloading et overriding
- [ ] Utiliser ArrayList (add, get, remove, size)
- [ ] Utiliser HashMap (put, get, containsKey)
- [ ] Comparer strings avec `.equals()`, pas `==`

---

## 🎓 Erreurs de débutant à éviter

```java
// ❌ MAUVAIS
String nom1 = "Alice";
String nom2 = "Alice";
if (nom1 == nom2) { }  // Compare les références!

// ✅ BON
if (nom1.equals(nom2)) { }  // Compare le contenu


// ❌ MAUVAIS
ArrayList<int> nombres = new ArrayList<>();

// ✅ BON
ArrayList<Integer> nombres = new ArrayList<>();


// ❌ MAUVAIS
public Chien(String nom) {
    this.race = "Berger";
    super(nom);  // ERREUR: super() doit être en premier!
}

// ✅ BON
public Chien(String nom) {
    super(nom);
    this.race = "Berger";
}
```

---

**💡 Conseil:** Écrivez AU MOINS 3 classes Java complètes sur papier aujourd'hui. La pratique manuscrite est cruciale pour l'examen!

**Prochain document:** `Jour3_POO_SOLID.md` - Principes avancés de conception
