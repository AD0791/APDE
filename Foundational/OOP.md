# OOP (POO) — Guide complet (Java + Python)

**Objectif:** Comprendre les concepts de la POO et savoir les appliquer en Java et Python.  
**Priorité:** 🔴 CRITIQUE — très fréquent en examen bancaire.

---

## 1) Les 4 piliers (comprendre, pas réciter)

### Encapsulation
**Idée:** protéger l'état interne et contrôler son accès.  
**Pourquoi:** éviter des modifications invalides (ex: solde négatif).

**Java**
```java
public class Compte {
    private double solde;
    public void deposer(double montant) {
        if (montant <= 0) throw new IllegalArgumentException();
        solde += montant;
    }
    public double getSolde() { return solde; }
}
```

**Python**
```python
class Compte:
    def __init__(self):
        self._solde = 0.0
    def deposer(self, montant):
        if montant <= 0:
            raise ValueError()
        self._solde += montant
    @property
    def solde(self):
        return self._solde
```

### Abstraction
**Idée:** exposer l'essentiel, cacher les détails.  
**Pourquoi:** simplifier l'usage et réduire le couplage.

**Java**
```java
interface Paiement {
    boolean payer(double montant);
}
```

**Python**
```python
from abc import ABC, abstractmethod

class Paiement(ABC):
    @abstractmethod
    def payer(self, montant):
        pass
```

### Héritage
**Idée:** réutiliser et spécialiser.  
**Pourquoi:** factoriser le code commun.

**Java**
```java
class Compte {
    protected double solde;
    public void deposer(double m) { solde += m; }
}

class CompteEpargne extends Compte {
    private double taux;
}
```

**Python**
```python
class Compte:
    def __init__(self):
        self.solde = 0
    def deposer(self, m):
        self.solde += m

class CompteEpargne(Compte):
    def __init__(self, taux):
        super().__init__()
        self.taux = taux
```

### Polymorphisme
**Idée:** même interface, comportements différents.  
**Pourquoi:** code client simple et extensible.

**Java**
```java
interface Notification { void envoyer(String msg); }
class SMS implements Notification { public void envoyer(String msg) {} }
class Email implements Notification { public void envoyer(String msg) {} }
```

**Python**
```python
class SMS:
    def envoyer(self, msg): pass

class Email:
    def envoyer(self, msg): pass
```

---

## 2) Composition vs Héritage

**Règle:** préférer la **composition** si la relation n'est pas un vrai "est-un".

**Exemple**
```java
class Moteur {}
class Voiture { private Moteur moteur = new Moteur(); }  // composition
```

---

## 3) Classe abstraite vs Interface

| Critère | Classe abstraite | Interface |
|---------|------------------|----------|
| Héritage multiple | Non | Oui (plusieurs interfaces) |
| Attributs | Oui | Constantes |
| Méthodes | Abstraites + concrètes | Abstraites (et défaut en Java) |

**Astuce:** interface = contrat, abstraite = base partagée.

---

## 4) Encapsulation avancée (immutabilité)

**Pourquoi:** éviter les bugs et faciliter le multi-threading.

**Java**
```java
public final class Client {
    private final String nom;
    public Client(String nom) { this.nom = nom; }
    public String getNom() { return nom; }
}
```

**Python**
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Client:
    nom: str
```

---

## 5) Polymorphisme dynamique (overriding)

**Java**
```java
class Compte {
    public boolean retirer(double m) { return false; }
}
class CompteCourant extends Compte {
    @Override public boolean retirer(double m) { return m <= 1000; }
}
```

**Python**
```python
class Compte:
    def retirer(self, m): return False

class CompteCourant(Compte):
    def retirer(self, m): return m <= 1000
```

---

## 6) Exceptions et contrat

**Objectif:** protéger l'intégrité métier.

**Java**
```java
if (montant <= 0) {
    throw new IllegalArgumentException("Montant invalide");
}
```

**Python**
```python
if montant <= 0:
    raise ValueError("Montant invalide")
```

---

## 7) Mini-exercices (avec solutions)

### Exercice A: Classe CompteBancaire
**Énoncé:** solde privé, dépôt/retrait sécurisés.

**Java**
```java
class CompteBancaire {
    private double solde;
    public void deposer(double m) { if (m > 0) solde += m; }
    public boolean retirer(double m) {
        if (m > 0 && solde >= m) { solde -= m; return true; }
        return false;
    }
}
```

**Python**
```python
class CompteBancaire:
    def __init__(self):
        self._solde = 0
    def deposer(self, m):
        if m > 0:
            self._solde += m
    def retirer(self, m):
        if m > 0 and self._solde >= m:
            self._solde -= m
            return True
        return False
```

---

## 8) Pièges fréquents (examens)

- Utiliser `==` pour comparer des `String` en Java → utiliser `.equals()`
- Oublier `@Override`
- Héritage utilisé alors que composition suffit
- Pas de validation métier dans les setters/méthodes

---

## 9) Checklist mémoire

- Encapsulation = **protéger l'état**
- Abstraction = **cacher la complexité**
- Héritage = **réutiliser**
- Polymorphisme = **même interface, comportements différents**

---

**Objectif final:** être capable d'expliquer un concept, puis de le montrer en Java et en Python.

**Prochain document:** `Jour3_POO_SOLID.md` - POO avancée & SOLID
