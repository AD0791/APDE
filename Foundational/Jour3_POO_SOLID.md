# Jour 3 (23 janvier): POO avancée & Principes SOLID

**Temps estimé:** 5-6 heures  
**Priorité:** 🔴 CRITIQUE - Questions systématiques en examen

---

## 🎯 Objectif du jour

Maîtriser les **concepts fondamentaux de la POO** et les **5 principes SOLID** qui reviennent dans TOUS les examens de développeur. Ces principes sont essentiels pour démontrer une compréhension mature de la conception logicielle.

---

## 🏛️ Les 4 piliers de la POO

| Pilier | Définition | Mécanisme Java | Exemple |
|--------|------------|----------------|---------|
| **Encapsulation** | Cacher les données, contrôler l'accès | `private` + getters/setters | Solde bancaire privé |
| **Héritage** | Réutiliser le code d'une classe parent | `extends` | CompteEpargne extends Compte |
| **Polymorphisme** | Même interface, comportements différents | Overriding, interfaces | Forme.calculerAire() |
| **Abstraction** | Cacher la complexité, montrer l'essentiel | `abstract`, `interface` | Interface Paiement |

### 1. Encapsulation détaillée

**But:** Protéger les données et contrôler leur modification

```java
public class CompteBancaire {
    // ❌ MAUVAIS: attributs publics
    // public double solde;
    
    // ✅ BON: attributs privés
    private double solde;
    private String numero;
    
    // Contrôle via getters/setters
    public double getSolde() {
        // Peut ajouter de la logique (logs, vérifications)
        return solde;
    }
    
    public void deposer(double montant) {
        // Validation avant modification!
        if (montant > 0) {
            this.solde += montant;
        } else {
            throw new IllegalArgumentException("Montant doit être positif");
        }
    }
    
    public boolean retirer(double montant) {
        // Logique métier protégée
        if (montant > 0 && this.solde >= montant) {
            this.solde -= montant;
            return true;
        }
        return false;
    }
}
```

**Pourquoi c'est important en bancaire:**
- Empêche des modifications directes du solde
- Permet d'ajouter des contrôles (montant positif, solde suffisant)
- Facilite le débogage et la maintenance

### 2. Héritage détaillé

**But:** Factoriser le code commun, créer des hiérarchies

```java
// Classe parent abstraite
public abstract class Compte {
    protected String numero;
    protected double solde;
    protected String titulaire;
    
    public Compte(String numero, String titulaire) {
        this.numero = numero;
        this.titulaire = titulaire;
        this.solde = 0;
    }
    
    // Méthode commune à tous les comptes
    public void deposer(double montant) {
        if (montant > 0) {
            this.solde += montant;
        }
    }
    
    // Méthode abstraite - chaque type définit sa logique
    public abstract boolean retirer(double montant);
    
    public double getSolde() {
        return solde;
    }
}

// Compte épargne - retrait avec pénalité
public class CompteEpargne extends Compte {
    private double tauxInteret;
    private int retraitsRestants;
    
    public CompteEpargne(String numero, String titulaire, double taux) {
        super(numero, titulaire);  // Appel constructeur parent
        this.tauxInteret = taux;
        this.retraitsRestants = 3;  // Max 3 retraits/mois
    }
    
    @Override
    public boolean retirer(double montant) {
        if (retraitsRestants > 0 && montant <= solde) {
            solde -= montant;
            retraitsRestants--;
            return true;
        }
        return false;
    }
    
    public void calculerInterets() {
        solde += solde * tauxInteret;
    }
}

// Compte courant - découvert autorisé
public class CompteCourant extends Compte {
    private double decouvertAutorise;
    
    public CompteCourant(String numero, String titulaire, double decouvert) {
        super(numero, titulaire);
        this.decouvertAutorise = decouvert;
    }
    
    @Override
    public boolean retirer(double montant) {
        if (montant <= (solde + decouvertAutorise)) {
            solde -= montant;
            return true;
        }
        return false;
    }
}
```

### 3. Polymorphisme détaillé

**But:** Utiliser une interface commune pour différents comportements

```java
public class BanqueService {
    // Polymorphisme: accepte n'importe quel type de Compte
    public void traiterRetrait(Compte compte, double montant) {
        if (compte.retirer(montant)) {
            System.out.println("Retrait réussi");
        } else {
            System.out.println("Retrait refusé");
        }
        // La méthode retirer() appelée dépend du type réel
        // CompteEpargne ou CompteCourant
    }
    
    public static void main(String[] args) {
        BanqueService service = new BanqueService();
        
        // Même méthode, comportements différents!
        Compte epargne = new CompteEpargne("E001", "Alice", 0.03);
        Compte courant = new CompteCourant("C001", "Bob", 500);
        
        epargne.deposer(1000);
        courant.deposer(1000);
        
        service.traiterRetrait(epargne, 100);  // Logique CompteEpargne
        service.traiterRetrait(courant, 1400); // Logique CompteCourant
    }
}
```

### 4. Abstraction détaillée

**But:** Définir des contrats sans imposer l'implémentation

```java
// Interface = contrat pur
public interface Paiement {
    boolean effectuerPaiement(double montant);
    String getStatut();
}

// Implémentations diverses
public class PaiementCarte implements Paiement {
    private String numeroCarte;
    
    @Override
    public boolean effectuerPaiement(double montant) {
        // Logique spécifique carte
        System.out.println("Paiement par carte: " + montant);
        return true;
    }
    
    @Override
    public String getStatut() {
        return "Carte validée";
    }
}

public class PaiementPayPal implements Paiement {
    private String email;
    
    @Override
    public boolean effectuerPaiement(double montant) {
        // Logique spécifique PayPal
        System.out.println("Paiement PayPal: " + montant);
        return true;
    }
    
    @Override
    public String getStatut() {
        return "PayPal connecté";
    }
}

// Utilisation polymorphe
public class ProcesseurPaiement {
    public void processer(Paiement paiement, double montant) {
        if (paiement.effectuerPaiement(montant)) {
            System.out.println("Succès: " + paiement.getStatut());
        }
    }
}
```

---

## 🎨 Principes SOLID

### S - Single Responsibility Principle (Responsabilité unique)

**"Une classe ne doit avoir qu'une seule raison de changer"**

```java
// ❌ MAUVAIS: Classe avec multiples responsabilités
public class Employe {
    private String nom;
    private double salaire;
    
    public void calculerSalaire() { 
        // Logique de calcul
    }
    
    public void sauvegarderEnBDD() { 
        // Logique de persistence
    }
    
    public void genererRapportPDF() { 
        // Logique de rapport
    }
    
    public void envoyerEmail() { 
        // Logique de notification
    }
}
// Problème: 4 raisons de changer cette classe!

// ✅ BON: Une responsabilité par classe
public class Employe {
    private String nom;
    private double salaire;
    
    // Getters/setters uniquement
}

public class ServiceCalculPaie {
    public double calculerSalaire(Employe e) {
        // Logique de calcul isolée
        return e.getSalaire() * 1.1;
    }
}

public class EmployeRepository {
    public void sauvegarder(Employe e) {
        // Logique de persistence isolée
    }
}

public class GenerateurRapport {
    public void genererPDF(Employe e) {
        // Logique de rapport isolée
    }
}

public class ServiceNotification {
    public void envoyerEmail(Employe e, String message) {
        // Logique de notification isolée
    }
}
```

**Avantages:**
- Changement dans le calcul n'affecte pas la persistence
- Tests plus faciles (une classe = une préoccupation)
- Réutilisabilité (ServiceCalculPaie peut servir ailleurs)

### O - Open/Closed Principle (Ouvert/Fermé)

**"Ouvert à l'extension, fermé à la modification"**

```java
// ❌ MAUVAIS: Modification de la classe existante à chaque nouvelle forme
public class CalculateurAire {
    public double calculer(Object forme, String type) {
        if (type.equals("RECTANGLE")) {
            Rectangle r = (Rectangle) forme;
            return r.largeur * r.hauteur;
        } else if (type.equals("CERCLE")) {
            Cercle c = (Cercle) forme;
            return Math.PI * c.rayon * c.rayon;
        }
        // Ajouter un triangle nécessite de MODIFIER cette classe!
        return 0;
    }
}

// ✅ BON: Extension par nouvelles classes, pas de modification
public interface Forme {
    double calculerAire();
}

public class Rectangle implements Forme {
    private double largeur, hauteur;
    
    public Rectangle(double l, double h) {
        this.largeur = l;
        this.hauteur = h;
    }
    
    @Override
    public double calculerAire() {
        return largeur * hauteur;
    }
}

public class Cercle implements Forme {
    private double rayon;
    
    public Cercle(double r) {
        this.rayon = r;
    }
    
    @Override
    public double calculerAire() {
        return Math.PI * rayon * rayon;
    }
}

// Ajouter un triangle? Nouvelle classe, AUCUNE modification!
public class Triangle implements Forme {
    private double base, hauteur;
    
    public Triangle(double b, double h) {
        this.base = b;
        this.hauteur = h;
    }
    
    @Override
    public double calculerAire() {
        return (base * hauteur) / 2;
    }
}

// Utilisation
public class CalculateurAire {
    public double calculer(Forme forme) {
        return forme.calculerAire();  // Polymorphisme
    }
}
```

### L - Liskov Substitution Principle (Substitution de Liskov)

**"Les sous-classes doivent être substituables à leurs classes de base"**

```java
// ❌ MAUVAIS: Carré viole le contrat de Rectangle
public class Rectangle {
    protected int largeur;
    protected int hauteur;
    
    public void setLargeur(int l) { largeur = l; }
    public void setHauteur(int h) { hauteur = h; }
    public int getAire() { return largeur * hauteur; }
}

public class Carre extends Rectangle {
    @Override
    public void setLargeur(int l) {
        largeur = l;
        hauteur = l;  // Violation: le carré force hauteur = largeur
    }
    
    @Override
    public void setHauteur(int h) {
        hauteur = h;
        largeur = h;  // Violation
    }
}

// Test qui échoue:
public void test(Rectangle r) {
    r.setLargeur(5);
    r.setHauteur(4);
    assert r.getAire() == 20;  // ✅ OK pour Rectangle
                                // ❌ ÉCHOUE pour Carré (25 au lieu de 20)
}

// ✅ BON: Abstraction correcte
public interface Forme {
    double calculerAire();
}

public class Rectangle implements Forme {
    private double largeur, hauteur;
    
    public Rectangle(double l, double h) {
        this.largeur = l;
        this.hauteur = h;
    }
    
    public void setDimensions(double l, double h) {
        this.largeur = l;
        this.hauteur = h;
    }
    
    @Override
    public double calculerAire() {
        return largeur * hauteur;
    }
}

public class Carre implements Forme {
    private double cote;
    
    public Carre(double c) {
        this.cote = c;
    }
    
    public void setCote(double c) {
        this.cote = c;
    }
    
    @Override
    public double calculerAire() {
        return cote * cote;
    }
}
```

### I - Interface Segregation Principle (Ségrégation d'interface)

**"Ne pas forcer les clients à dépendre de méthodes qu'ils n'utilisent pas"**

```java
// ❌ MAUVAIS: Interface trop large
public interface Travailleur {
    void travailler();
    void manger();
    void dormir();
    void prendreVacances();
}

public class Robot implements Travailleur {
    @Override
    public void travailler() { /* OK */ }
    
    @Override
    public void manger() { 
        // Robot ne mange pas! Implémentation vide forcée
    }
    
    @Override
    public void dormir() { 
        // Robot ne dort pas!
    }
    
    @Override
    public void prendreVacances() { 
        // Robot ne prend pas de vacances!
    }
}

// ✅ BON: Interfaces ségrégées
public interface Travaillable {
    void travailler();
}

public interface Mangeable {
    void manger();
}

public interface Reposable {
    void dormir();
}

public interface AvecConges {
    void prendreVacances();
}

// Robot implémente seulement ce dont il a besoin
public class Robot implements Travaillable {
    @Override
    public void travailler() {
        System.out.println("Robot travaille 24/7");
    }
}

// Humain implémente tout
public class Humain implements Travaillable, Mangeable, Reposable, AvecConges {
    @Override
    public void travailler() { /* ... */ }
    
    @Override
    public void manger() { /* ... */ }
    
    @Override
    public void dormir() { /* ... */ }
    
    @Override
    public void prendreVacances() { /* ... */ }
}
```

### D - Dependency Inversion Principle (Inversion de dépendance)

**"Dépendre d'abstractions, pas de concrétions"**

```java
// ❌ MAUVAIS: Haut niveau dépend de bas niveau
public class ServiceCommande {
    private BaseDonneeMySQL db = new BaseDonneeMySQL();  // Dépendance concrète!
    
    public void sauvegarderCommande(Commande c) {
        db.save(c);  // Couplage fort à MySQL
    }
}
// Problème: Changer de BDD nécessite de modifier ServiceCommande

// ✅ BON: Dépendre de l'abstraction
public interface BaseDonnee {
    void save(Commande c);
    Commande load(int id);
}

// Implémentations concrètes
public class BaseDonneeMySQL implements BaseDonnee {
    @Override
    public void save(Commande c) {
        // Logique MySQL
    }
    
    @Override
    public Commande load(int id) {
        // Logique MySQL
        return null;
    }
}

public class BaseDonneePostgreSQL implements BaseDonnee {
    @Override
    public void save(Commande c) {
        // Logique PostgreSQL
    }
    
    @Override
    public Commande load(int id) {
        // Logique PostgreSQL
        return null;
    }
}

// Service dépend de l'abstraction
public class ServiceCommande {
    private BaseDonnee db;  // Abstraction!
    
    // Injection de dépendance via constructeur
    public ServiceCommande(BaseDonnee db) {
        this.db = db;
    }
    
    public void sauvegarderCommande(Commande c) {
        db.save(c);  // Peut utiliser MySQL, PostgreSQL, etc.
    }
}

// Utilisation
public class Main {
    public static void main(String[] args) {
        // Facile de changer d'implémentation!
        BaseDonnee db = new BaseDonneePostgreSQL();
        ServiceCommande service = new ServiceCommande(db);
        
        Commande c = new Commande();
        service.sauvegarderCommande(c);
    }
}
```

---

## 🎭 Design Patterns essentiels

### 1. Singleton (Instance unique)

```java
// Thread-safe - Méthode Bill Pugh
public class Configuration {
    // Constructeur privé
    private Configuration() { }
    
    // Classe interne statique
    private static class ConfigurationHolder {
        private static final Configuration INSTANCE = new Configuration();
    }
    
    // Méthode publique d'accès
    public static Configuration getInstance() {
        return ConfigurationHolder.INSTANCE;
    }
    
    // Méthodes métier
    public void chargerConfig() {
        System.out.println("Configuration chargée");
    }
}

// Utilisation
Configuration config1 = Configuration.getInstance();
Configuration config2 = Configuration.getInstance();
// config1 == config2 (même instance)
```

### 2. Factory Method (Fabrique)

```java
// Produit abstrait
public interface Paiement {
    void effectuerPaiement(double montant);
}

// Produits concrets
public class PaiementCarte implements Paiement {
    @Override
    public void effectuerPaiement(double montant) {
        System.out.println("Paiement carte: " + montant + " HTG");
    }
}

public class PaiementMobile implements Paiement {
    @Override
    public void effectuerPaiement(double montant) {
        System.out.println("Paiement mobile: " + montant + " HTG");
    }
}

public class PaiementEspeces implements Paiement {
    @Override
    public void effectuerPaiement(double montant) {
        System.out.println("Paiement espèces: " + montant + " HTG");
    }
}

// Fabrique
public class FabriquePaiement {
    public static Paiement creerPaiement(String type) {
        switch (type.toUpperCase()) {
            case "CARTE":
                return new PaiementCarte();
            case "MOBILE":
                return new PaiementMobile();
            case "ESPECES":
                return new PaiementEspeces();
            default:
                throw new IllegalArgumentException("Type inconnu: " + type);
        }
    }
}

// Utilisation
public class Main {
    public static void main(String[] args) {
        Paiement p1 = FabriquePaiement.creerPaiement("CARTE");
        p1.effectuerPaiement(500);
        
        Paiement p2 = FabriquePaiement.creerPaiement("MOBILE");
        p2.effectuerPaiement(300);
    }
}
```

### 3. Strategy (Stratégie)

```java
// Stratégie abstraite
public interface StrategieCalculInteret {
    double calculer(double capital);
}

// Stratégies concrètes
public class InteretSimple implements StrategieCalculInteret {
    private double taux;
    
    public InteretSimple(double taux) {
        this.taux = taux;
    }
    
    @Override
    public double calculer(double capital) {
        return capital * taux;
    }
}

public class InteretCompose implements StrategieCalculInteret {
    private double taux;
    private int periodes;
    
    public InteretCompose(double taux, int periodes) {
        this.taux = taux;
        this.periodes = periodes;
    }
    
    @Override
    public double calculer(double capital) {
        return capital * Math.pow(1 + taux, periodes) - capital;
    }
}

// Contexte
public class CompteEpargne {
    private double solde;
    private StrategieCalculInteret strategie;
    
    public CompteEpargne(double solde) {
        this.solde = solde;
    }
    
    public void setStrategie(StrategieCalculInteret s) {
        this.strategie = s;
    }
    
    public void appliquerInterets() {
        double interets = strategie.calculer(solde);
        solde += interets;
        System.out.println("Intérêts: " + interets + ", Nouveau solde: " + solde);
    }
}

// Utilisation
public class Main {
    public static void main(String[] args) {
        CompteEpargne compte = new CompteEpargne(10000);
        
        // Changer de stratégie dynamiquement
        compte.setStrategie(new InteretSimple(0.03));
        compte.appliquerInterets();
        
        compte.setStrategie(new InteretCompose(0.03, 12));
        compte.appliquerInterets();
    }
}
```

### 4. Observer (Observateur)

```java
// Observateur
public interface ObservateurCompte {
    void notifier(String message);
}

// Sujet observable
public class CompteBancaire {
    private String numero;
    private double solde;
    private List<ObservateurCompte> observateurs = new ArrayList<>();
    
    public void ajouterObservateur(ObservateurCompte obs) {
        observateurs.add(obs);
    }
    
    public void retirerObservateur(ObservateurCompte obs) {
        observateurs.remove(obs);
    }
    
    private void notifierObservateurs(String message) {
        for (ObservateurCompte obs : observateurs) {
            obs.notifier(message);
        }
    }
    
    public void deposer(double montant) {
        solde += montant;
        notifierObservateurs("Dépôt de " + montant + " HTG");
    }
    
    public void retirer(double montant) {
        if (solde >= montant) {
            solde -= montant;
            notifierObservateurs("Retrait de " + montant + " HTG");
        }
    }
}

// Observateurs concrets
public class ServiceEmail implements ObservateurCompte {
    @Override
    public void notifier(String message) {
        System.out.println("📧 Email envoyé: " + message);
    }
}

public class ServiceSMS implements ObservateurCompte {
    @Override
    public void notifier(String message) {
        System.out.println("📱 SMS envoyé: " + message);
    }
}

public class ServiceLog implements ObservateurCompte {
    @Override
    public void notifier(String message) {
        System.out.println("📝 Log: " + message);
    }
}

// Utilisation
public class Main {
    public static void main(String[] args) {
        CompteBancaire compte = new CompteBancaire();
        
        compte.ajouterObservateur(new ServiceEmail());
        compte.ajouterObservateur(new ServiceSMS());
        compte.ajouterObservateur(new ServiceLog());
        
        compte.deposer(1000);  // Tous les observateurs sont notifiés
    }
}
```

### 5. MVC (Model-View-Controller)

```java
// MODEL - Données
public class Etudiant {
    private int id;
    private String nom;
    private double moyenne;
    
    public Etudiant(int id, String nom, double moyenne) {
        this.id = id;
        this.nom = nom;
        this.moyenne = moyenne;
    }
    
    // Getters et setters
    public int getId() { return id; }
    public String getNom() { return nom; }
    public void setNom(String nom) { this.nom = nom; }
    public double getMoyenne() { return moyenne; }
    public void setMoyenne(double moyenne) { this.moyenne = moyenne; }
}

// VIEW - Présentation
public class EtudiantVue {
    public void afficherEtudiant(int id, String nom, double moyenne) {
        System.out.println("=== Détails Étudiant ===");
        System.out.println("ID: " + id);
        System.out.println("Nom: " + nom);
        System.out.println("Moyenne: " + moyenne);
    }
}

// CONTROLLER - Logique
public class EtudiantControleur {
    private Etudiant model;
    private EtudiantVue vue;
    
    public EtudiantControleur(Etudiant model, EtudiantVue vue) {
        this.model = model;
        this.vue = vue;
    }
    
    public void setNom(String nom) {
        model.setNom(nom);
    }
    
    public void setMoyenne(double moyenne) {
        model.setMoyenne(moyenne);
    }
    
    public void mettreAJourVue() {
        vue.afficherEtudiant(
            model.getId(),
            model.getNom(),
            model.getMoyenne()
        );
    }
}

// Utilisation
public class Main {
    public static void main(String[] args) {
        Etudiant model = new Etudiant(1, "Alice", 15.5);
        EtudiantVue vue = new EtudiantVue();
        EtudiantControleur controleur = new EtudiantControleur(model, vue);
        
        controleur.mettreAJourVue();
        
        controleur.setNom("Alice Dupont");
        controleur.setMoyenne(16.2);
        controleur.mettreAJourVue();
    }
}
```

---

## ✅ SOLID — Solutions Java et Python (exemples courts)

### 1) SRP — Une classe = une responsabilité

**Java**
```java
class RapportService { void genererRapport() {} }
class RapportPrinter { void imprimer(String contenu) {} }
```

**Python**
```python
class RapportService:
    def generer_rapport(self): pass

class RapportPrinter:
    def imprimer(self, contenu): pass
```

### 2) OCP — Ouvert à l'extension, fermé à la modification

**Java**
```java
interface FeePolicy { double fee(double amount); }
class StandardFee implements FeePolicy { public double fee(double a){ return a*0.01; } }
```

**Python**
```python
class FeePolicy:
    def fee(self, amount): raise NotImplementedError

class StandardFee(FeePolicy):
    def fee(self, amount): return amount * 0.01
```

### 3) LSP — Sous-types substituables

**Java**
```java
class Compte { boolean retirer(double m){ return m >= 0; } }
class CompteCourant extends Compte { @Override boolean retirer(double m){ return m >= 0; } }
```

**Python**
```python
class Compte:
    def retirer(self, m): return m >= 0

class CompteCourant(Compte):
    def retirer(self, m): return m >= 0
```

### 4) ISP — Interfaces petites et ciblées

**Java**
```java
interface ExportPdf { void exportPdf(); }
interface ExportCsv { void exportCsv(); }
```

**Python**
```python
class ExportPdf:
    def export_pdf(self): pass
class ExportCsv:
    def export_csv(self): pass
```

### 5) DIP — Dépendre d'abstractions

**Java**
```java
interface Repository { void save(String data); }
class Service {
    private final Repository repo;
    Service(Repository repo){ this.repo = repo; }
}
```

**Python**
```python
class Repository:
    def save(self, data): raise NotImplementedError

class Service:
    def __init__(self, repo: Repository):
        self.repo = repo
```

---

## 📝 Exercices pratiques Jour 3

### Exercice 1: SOLID
**Sur papier, expliquer en 2 phrases:**
1. Principe de responsabilité unique
2. Principe ouvert/fermé
3. Principe de substitution de Liskov
4. Principe de ségrégation d'interface
5. Principe d'inversion de dépendance

### Exercice 2: Singleton
**Implémenter de mémoire un Singleton thread-safe (méthode Bill Pugh)**

### Exercice 3: Factory
**Créer une Factory pour différents types de comptes bancaires (Epargne, Courant, Crédit)**

### Exercice 4: Observer
**Dessiner le diagramme de classes du pattern Observer avec CompteBancaire et 3 observateurs**

---

## ✅ Checklist de révision Jour 3

- [ ] Expliquer les 4 piliers de la POO avec exemples
- [ ] Différencier classe abstraite et interface
- [ ] Énoncer les 5 principes SOLID en une phrase chacun
- [ ] Donner un exemple de violation de chaque principe SOLID
- [ ] Implémenter le pattern Singleton
- [ ] Implémenter le pattern Factory
- [ ] Implémenter le pattern Strategy
- [ ] Implémenter le pattern Observer
- [ ] Expliquer le pattern MVC avec un schéma

---

**💡 Conseil:** Les principes SOLID sont souvent demandés en définition courte. Mémorisez une phrase claire pour chacun!

**Prochain document:** `Jour4_UML.md` - Modélisation avec diagrammes
