# UML FULL — Guide Complet de Modélisation UML et POO

## 📋 Vue d'Ensemble

Ce dossier contient des études de cas complètes sur la modélisation UML (Unified Modeling Language) et la programmation orientée objet (POO), organisées par niveau de complexité. Chaque étude présente des diagrammes UML détaillés avec implémentations en Python et Java dans un contexte bancaire.

---

## 🎯 Structure des Études de Cas

### **Niveau Basique** (`etude_cas_banque_basique.md`)
**Durée estimée :** 4-5 heures  
**Prérequis :** Bases de programmation

**Concepts couverts :**
- **Encapsulation**
  - Attributs privés
  - Getters et setters
  - Contrôle d'accès
  - Validation des données

- **Héritage**
  - Classes parentes et enfants
  - Redéfinition de méthodes (override)
  - Polymorphisme de base
  - Classes abstraites

- **Associations**
  - Relations entre classes
  - Cardinalités (1:1, 1:N, M:N)
  - Navigation entre objets
  - Agrégation vs Composition

- **Diagrammes UML**
  - Diagramme de classes
  - Diagramme de séquence simple
  - Notation de base

**Projets pratiques :**
1. Classe Compte avec encapsulation complète
2. Hiérarchie CompteCourant/CompteEpargne
3. Virement entre comptes (associations)
4. Diagrammes de classes et séquence

**Compétences acquises :**
- ✅ Encapsuler correctement les données
- ✅ Créer des hiérarchies avec héritage
- ✅ Modéliser des associations
- ✅ Dessiner des diagrammes UML de base
- ✅ Implémenter des classes en Python/Java

---

### **Niveau Moyen** (`etude_cas_banque_moyen.md`)
**Durée estimée :** 5-6 heures  
**Prérequis :** Niveau basique + POO intermédiaire

**Concepts couverts :**
- **Principes SOLID**
  - Single Responsibility Principle
  - Open/Closed Principle
  - Liskov Substitution Principle
  - Interface Segregation Principle
  - Dependency Inversion Principle

- **Interfaces et contrats**
  - Définition d'interfaces
  - Implémentation multiple
  - Polymorphisme avancé
  - Injection de dépendances

- **Composition vs Héritage**
  - Quand utiliser chacun
  - Délégation
  - Stratégies de conception

- **Diagrammes avancés**
  - Diagramme d'états-transitions
  - Diagramme d'activités
  - Diagramme de cas d'utilisation

**Projets pratiques :**
1. Système de notifications (Observer pattern)
2. Calcul de frais avec stratégies
3. Gestion d'états de compte
4. Architecture multi-couches

**Compétences acquises :**
- ✅ Appliquer les principes SOLID
- ✅ Concevoir avec des interfaces
- ✅ Choisir entre composition et héritage
- ✅ Créer des diagrammes dynamiques
- ✅ Architecturer des systèmes modulaires

---

### **Niveau Senior** (`etude_cas_banque_senior.md`)
**Durée estimée :** 6-8 heures  
**Prérequis :** Niveau moyen + expérience architecture

**Concepts couverts :**
- **Architecture en couches**
  - Présentation / Application / Domaine / Infrastructure
  - Séparation des préoccupations
  - Dependency Inversion

- **Domain-Driven Design (DDD)**
  - Entités vs Value Objects
  - Agrégats et Aggregate Roots
  - Repositories
  - Domain Services
  - Domain Events

- **Design Patterns architecturaux**
  - MVC / MVP / MVVM
  - Repository Pattern
  - Unit of Work
  - CQRS (Command Query Responsibility Segregation)

- **Diagrammes d'architecture**
  - Diagramme de composants
  - Diagramme de déploiement
  - Diagramme de packages

**Projets pratiques :**
1. Architecture hexagonale complète
2. Domain model avec DDD
3. System design pour application bancaire
4. Documentation architecture complète

**Compétences acquises :**
- ✅ Architecturer des applications enterprise
- ✅ Appliquer Domain-Driven Design
- ✅ Concevoir des systèmes scalables
- ✅ Documenter l'architecture
- ✅ Prendre des décisions architecturales

---

## 📚 Les 4 Piliers de la POO

### 1. Encapsulation
**Définition :** Regrouper données et méthodes, cacher les détails internes

```python
class Compte:
    def __init__(self, numero, titulaire):
        self._numero = numero  # Privé
        self._solde = 0.0      # Privé
        self._titulaire = titulaire
    
    @property
    def solde(self):
        return self._solde
    
    def deposer(self, montant):
        if montant > 0:
            self._solde += montant
```

**Avantages :**
- ✅ Contrôle d'accès aux données
- ✅ Validation centralisée
- ✅ Flexibilité d'implémentation
- ✅ Maintenance facilitée

---

### 2. Héritage
**Définition :** Créer de nouvelles classes à partir de classes existantes

```python
class Compte:
    def __init__(self, numero):
        self.numero = numero
        self.solde = 0
    
    def deposer(self, montant):
        self.solde += montant

class CompteCourant(Compte):  # Hérite de Compte
    def __init__(self, numero, decouvert):
        super().__init__(numero)
        self.decouvert_autorise = decouvert
    
    def retirer(self, montant):
        if self.solde + self.decouvert_autorise >= montant:
            self.solde -= montant
            return True
        return False
```

**Avantages :**
- ✅ Réutilisation du code
- ✅ Extension facile
- ✅ Hiérarchies naturelles
- ✅ Polymorphisme

---

### 3. Polymorphisme
**Définition :** Même interface, comportements différents

```python
def traiter_compte(compte: Compte):
    # Fonctionne avec CompteCourant ET CompteEpargne
    print(f"Solde: {compte.solde}")
    compte.deposer(100)

# Polymorphisme en action
comptes = [
    CompteCourant("CC001", 500),
    CompteEpargne("CE001", 0.03)
]

for compte in comptes:
    traiter_compte(compte)  # Même code, comportements différents
```

**Avantages :**
- ✅ Code générique et flexible
- ✅ Extensibilité sans modification
- ✅ Simplicité d'utilisation

---

### 4. Abstraction
**Définition :** Cacher la complexité, exposer l'essentiel

```python
from abc import ABC, abstractmethod

class Compte(ABC):
    @abstractmethod
    def calculer_frais(self):
        pass  # Force les sous-classes à implémenter

class CompteCourant(Compte):
    def calculer_frais(self):
        return 10.0  # Implémentation concrète

class CompteEpargne(Compte):
    def calculer_frais(self):
        return 0.0
```

**Avantages :**
- ✅ Interface claire
- ✅ Détails cachés
- ✅ Contrat explicite
- ✅ Évolutivité

---

## 🎓 Principes SOLID Expliqués

### S — Single Responsibility Principle
**Règle :** Une classe = une seule responsabilité

❌ **Mauvais :**
```python
class Compte:
    def deposer(self, montant): pass
    def retirer(self, montant): pass
    def send_email(self): pass  # Responsabilité en trop!
    def generer_pdf(self): pass  # Responsabilité en trop!
```

✅ **Bon :**
```python
class Compte:
    def deposer(self, montant): pass
    def retirer(self, montant): pass

class EmailService:
    def send_email(self, destinataire, message): pass

class PDFGenerator:
    def generer_releve(self, compte): pass
```

---

### O — Open/Closed Principle
**Règle :** Ouvert à l'extension, fermé à la modification

❌ **Mauvais :**
```python
class CalculateurFrais:
    def calculer(self, type_compte, montant):
        if type_compte == "COURANT":
            return montant * 0.01
        elif type_compte == "EPARGNE":
            return 0
        # Ajouter un type nécessite de modifier cette méthode
```

✅ **Bon :**
```python
class CalculateurFrais(ABC):
    @abstractmethod
    def calculer(self, montant): pass

class FraisCourant(CalculateurFrais):
    def calculer(self, montant):
        return montant * 0.01

class FraisEpargne(CalculateurFrais):
    def calculer(self, montant):
        return 0

# Ajouter un nouveau type ne modifie pas le code existant
```

---

### L — Liskov Substitution Principle
**Règle :** Les sous-classes doivent être substituables

❌ **Mauvais :**
```python
class Rectangle:
    def set_width(self, w): self.width = w
    def set_height(self, h): self.height = h

class Carre(Rectangle):
    def set_width(self, w):
        self.width = self.height = w  # Change le comportement!
```

✅ **Bon :**
```python
class Forme(ABC):
    @abstractmethod
    def calculer_aire(self): pass

class Rectangle(Forme):
    def __init__(self, w, h):
        self.width = w
        self.height = h
    def calculer_aire(self):
        return self.width * self.height

class Carre(Forme):
    def __init__(self, cote):
        self.cote = cote
    def calculer_aire(self):
        return self.cote ** 2
```

---

### I — Interface Segregation Principle
**Règle :** Interfaces spécifiques plutôt qu'une interface générale

❌ **Mauvais :**
```python
class Compte(ABC):
    @abstractmethod
    def deposer(self): pass
    @abstractmethod
    def retirer(self): pass
    @abstractmethod
    def calculer_interets(self): pass  # Pas pour tous!
```

✅ **Bon :**
```python
class CompteBase(ABC):
    @abstractmethod
    def deposer(self): pass
    @abstractmethod
    def retirer(self): pass

class CompteAvecInterets(CompteBase):
    @abstractmethod
    def calculer_interets(self): pass
```

---

### D — Dependency Inversion Principle
**Règle :** Dépendre d'abstractions, pas de classes concrètes

❌ **Mauvais :**
```python
class Service:
    def __init__(self):
        self.db = MySQLDatabase()  # Dépendance concrète
```

✅ **Bon :**
```python
class Service:
    def __init__(self, db: DatabaseInterface):
        self.db = db  # Dépendance abstraite

# Peut utiliser MySQL, PostgreSQL, MongoDB...
service = Service(MySQLDatabase())
service = Service(PostgreSQLDatabase())
```

---

## 📐 Diagrammes UML Essentiels

### Diagramme de Classes

**Notation de base :**
```
┌─────────────────┐
│   NomClasse     │
├─────────────────┤
│ - attribut1     │  ← Privé (-)
│ + attribut2     │  ← Public (+)
│ # attribut3     │  ← Protégé (#)
├─────────────────┤
│ + methode1()    │
│ - methode2()    │
└─────────────────┘
```

**Relations :**
```
Association       ────────►
Composition       ◆────────
Agrégation        ◇────────
Héritage          ────────▷
Réalisation       ┄┄┄┄┄┄┄▷
Dépendance        ┄┄┄┄┄┄┄►
```

**Cardinalités :**
```
1        Exactement un
0..1     Zéro ou un
*        Zéro ou plusieurs
1..*     Un ou plusieurs
2..5     De 2 à 5
```

---

### Diagramme de Séquence

```
Client          Banque          CompteA         CompteB
  │               │               │               │
  │──virement()──>│               │               │
  │               │──getSolde()──>│               │
  │               │<──solde───────│               │
  │               │               │               │
  │               │──retirer()───>│               │
  │               │<──OK──────────│               │
  │               │               │               │
  │               │──deposer()────────────────────>│
  │               │<──OK──────────────────────────│
  │<───OK─────────│               │               │
```

**Éléments :**
- Acteurs (rectangles en haut)
- Ligne de vie (ligne verticale pointillée)
- Messages (flèches horizontales)
- Activation (rectangles sur ligne de vie)

---

### Diagramme d'États

```
        [création]
            │
            ▼
      ┌─────────┐
      │  ACTIF  │◄──────┐
      └─────────┘       │
         │    ▲         │
depôt/   │    │         │ réactiver
retrait  │    │         │
         │    │         │
         ▼    │         │
      ┌─────────┐       │
      │SUSPENDU │───────┘
      └─────────┘
            │
            │ [fermeture]
            ▼
      ┌─────────┐
      │  FERMÉ  │
      └─────────┘
```

---

### Diagramme de Cas d'Utilisation

```
┌────────────────────────────────────┐
│     Système Bancaire               │
│                                    │
│   ┌────────────────────┐           │
│   │ Consulter Solde    │           │
│   └────────────────────┘           │
│            ▲                       │
│            │                       │
│   ┌────────────────────┐           │
│   │ Effectuer Virement │           │
│   └────────────────────┘           │
│            ▲                       │
│            │                       │
└────────────┼───────────────────────┘
             │
        ┌────┴────┐
        │ Client  │  (Acteur)
        └─────────┘
```

---

## 🛠️ Outils de Modélisation UML

### Outils en ligne
- **PlantUML** — Diagrammes en code
- **draw.io** — Éditeur gratuit en ligne
- **Lucidchart** — Collaboration en équipe
- **Mermaid** — Intégration Markdown

### Logiciels
- **Visual Paradigm** — Suite complète UML
- **StarUML** — Outil open source
- **Enterprise Architect** — Professionnel
- **ArgoUML** — Simple et gratuit

### Plugins IDE
- **PlantUML integration** — VSCode, IntelliJ
- **Mermaid Preview** — VSCode
- **UML Class Diagram** — VSCode

---

## 💡 Patterns de Conception et UML

### Factory Method
```
┌───────────────┐
│CompteFactory  │
│<<interface>>  │
├───────────────┤
│+creer():Compte│
└───────────────┘
        △
        │
   ┌────┴────┐
   │         │
┌──┴──┐   ┌──┴──┐
│CCFac│   │CEFac│
└─────┘   └─────┘
```

### Strategy
```
┌─────────────┐     ┌──────────────┐
│Transaction  │────>│FeeStrategy   │
│             │     │<<interface>> │
│+total()     │     │+calculate()  │
└─────────────┘     └──────────────┘
                           △
                      ┌────┴────┐
                      │         │
                ┌─────┴──┐  ┌───┴───┐
                │Standard│  │Premium│
                └────────┘  └───────┘
```

### Observer
```
┌─────────────┐     ┌──────────────┐
│Observable   │────>│Observer      │
│             │     │<<interface>> │
│+subscribe() │     │+update()     │
│+notify()    │     └──────────────┘
└─────────────┘            △
                      ┌────┴────┐
                      │         │
                ┌─────┴──┐  ┌───┴───┐
                │EmailObs│  │SMSObs │
                └────────┘  └───────┘
```

---

## 🎯 Objectifs d'Apprentissage

### Niveau Basique ✅
Après ce niveau, vous devriez pouvoir :
- [ ] Encapsuler correctement des données
- [ ] Créer des hiérarchies avec héritage
- [ ] Modéliser des associations entre classes
- [ ] Dessiner des diagrammes de classes simples
- [ ] Implémenter des designs POO en Python/Java

### Niveau Moyen ✅
Après ce niveau, vous devriez pouvoir :
- [ ] Appliquer tous les principes SOLID
- [ ] Concevoir avec des interfaces
- [ ] Choisir composition vs héritage
- [ ] Créer des diagrammes d'états et d'activités
- [ ] Architecturer des systèmes modulaires

### Niveau Senior ✅
Après ce niveau, vous devriez pouvoir :
- [ ] Architecturer des applications en couches
- [ ] Appliquer Domain-Driven Design
- [ ] Documenter l'architecture complète
- [ ] Prendre des décisions architecturales
- [ ] Concevoir des systèmes scalables

---

## 📚 Ressources Complémentaires

### Livres Essentiels
- **"UML Distilled"** — Martin Fowler
  - *Introduction concise à UML*
- **"Clean Architecture"** — Robert C. Martin
  - *Principes d'architecture logicielle*
- **"Domain-Driven Design"** — Eric Evans
  - *Le livre de référence sur DDD*
- **"Design Patterns"** — Gang of Four
  - *Patterns de conception classiques*

### Sites Web
- [UML Diagrams](https://www.uml-diagrams.org/) — Référence complète
- [PlantUML](https://plantuml.com/) — Documentation et exemples
- [Martin Fowler](https://martinfowler.com/) — Articles sur l'architecture

### Vidéos
- **Derek Banas** — UML en 30 minutes
- **Code Aesthetic** — Principes de design
- **ArjanCodes** — SOLID principles

---

## 💼 Application en Contexte Bancaire

### Modèle de Domaine Bancaire

```
┌─────────────┐     ┌──────────────┐
│   Client    │────>│   Compte     │
├─────────────┤     │<<abstract>>  │
│+nom         │1   *├──────────────┤
│+email       │     │+numero       │
│+telephone   │     │+solde        │
└─────────────┘     │+deposer()    │
                    │+retirer()    │
                    └──────────────┘
                            △
                       ┌────┴────┐
                       │         │
              ┌────────┴──┐  ┌───┴────────┐
              │Courant    │  │Epargne     │
              ├───────────┤  ├────────────┤
              │-decouvert │  │-tauxInteret│
              │+retirer() │  │+calculer() │
              └───────────┘  └────────────┘
                    │
                    │1
                    │
                   *│
            ┌───────┴────────┐
            │  Transaction   │
            ├────────────────┤
            │+type           │
            │+montant        │
            │+date           │
            └────────────────┘
```

---

## 🚀 Prochaines Étapes

Après avoir maîtrisé UML et POO :

1. **Pratiquez le design** — Modelez vos projets avant de coder
2. **Étudiez les patterns** — Approfondissez les Design Patterns
3. **Apprenez l'architecture** — Clean Architecture, Hexagonal
4. **Explorez le DDD** — Domain-Driven Design
5. **Documentez** — Utilisez UML pour documenter vos systèmes

---

**Dernière mise à jour :** Janvier 2026

**Bonne modélisation UML et conception orientée objet !** 📐
