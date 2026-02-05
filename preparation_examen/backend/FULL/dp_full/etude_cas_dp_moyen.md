# Étude de Cas Design Patterns — Niveau Moyen

## Guide de Préparation : Strategy, Adapter, Decorator

---

Ce document intermédiaire met l'accent sur la flexibilité et l'extension de comportements sans modifier le code existant.

---

## Problème 1 : Strategy (Calcul de Frais)

### Énoncé

Appliquer des stratégies de frais différentes selon le type de transaction.

### Solution Python

```python
class FeeStrategy:
    def fee(self, amount):
        raise NotImplementedError

class StandardFee(FeeStrategy):
    def fee(self, amount):
        return amount * 0.01

class PremiumFee(FeeStrategy):
    def fee(self, amount):
        return amount * 0.005

class Transaction:
    def __init__(self, amount, strategy):
        self.amount = amount
        self.strategy = strategy
    def total(self):
        return self.amount + self.strategy.fee(self.amount)
```

### Solution Java

```java
interface FeeStrategy {
    double fee(double amount);
}

class StandardFee implements FeeStrategy {
    public double fee(double amount) { return amount * 0.01; }
}

class PremiumFee implements FeeStrategy {
    public double fee(double amount) { return amount * 0.005; }
}

class Transaction {
    private final double amount;
    private final FeeStrategy strategy;
    public Transaction(double amount, FeeStrategy strategy) {
        this.amount = amount;
        this.strategy = strategy;
    }
    public double total() { return amount + strategy.fee(amount); }
}
```

---

## Problème 2 : Adapter (Intégration d'un Service Externe)

### Énoncé

Adapter une API externe de change pour l'utiliser dans votre système bancaire.

### Solution Python

```python
class ExterneFX:
    def get_rate_usd_to_htg(self):
        return 132.5

class FXAdapter:
    def __init__(self, fx):
        self.fx = fx
    def rate(self, src, dst):
        if src == "USD" and dst == "HTG":
            return self.fx.get_rate_usd_to_htg()
        raise ValueError("Pair non supporte")
```

### Solution Java

```java
class ExterneFX {
    public double getRateUsdToHtg() { return 132.5; }
}

class FXAdapter {
    private final ExterneFX fx;
    public FXAdapter(ExterneFX fx) { this.fx = fx; }
    public double rate(String src, String dst) {
        if ("USD".equals(src) && "HTG".equals(dst)) {
            return fx.getRateUsdToHtg();
        }
        throw new IllegalArgumentException("Pair non supporte");
    }
}
```

---

## Problème 3 : Decorator (Audit des Opérations)

### Énoncé

Ajouter la journalisation d'une opération sans modifier la classe de base.

### Solution Python

```python
class Operation:
    def execute(self, amount):
        return amount

class AuditDecorator(Operation):
    def __init__(self, op):
        self.op = op
    def execute(self, amount):
        result = self.op.execute(amount)
        print("AUDIT:", amount, "->", result)
        return result
```

### Solution Java

```java
interface Operation {
    double execute(double amount);
}

class SimpleOperation implements Operation {
    public double execute(double amount) { return amount; }
}

class AuditDecorator implements Operation {
    private final Operation op;
    public AuditDecorator(Operation op) { this.op = op; }
    public double execute(double amount) {
        double result = op.execute(amount);
        System.out.println("AUDIT: " + amount + " -> " + result);
        return result;
    }
}
```

---

## Problème 4 : Template Method (Workflow Standard)

### Énoncé

Définir un processus standard de traitement de prêt, avec étapes personnalisables.

### Solution Python

```python
class LoanProcess:
    def run(self, dossier):
        self.check_kyc(dossier)
        self.score(dossier)
        self.approve(dossier)
    def check_kyc(self, dossier):
        raise NotImplementedError
    def score(self, dossier):
        raise NotImplementedError
    def approve(self, dossier):
        raise NotImplementedError

class RetailLoanProcess(LoanProcess):
    def check_kyc(self, dossier): pass
    def score(self, dossier): pass
    def approve(self, dossier): pass
```

### Solution Java

```java
abstract class LoanProcess {
    public final void run(String dossier) {
        checkKyc(dossier);
        score(dossier);
        approve(dossier);
    }
    protected abstract void checkKyc(String dossier);
    protected abstract void score(String dossier);
    protected abstract void approve(String dossier);
}
```

---

## Problème 5 : Command (Historique d'Actions)

### Énoncé

Exécuter des opérations (depot, retrait) avec historique et undo.

### Solution Python

```python
class Command:
    def execute(self): pass
    def undo(self): pass

class Depot(Command):
    def __init__(self, compte, montant):
        self.compte = compte
        self.montant = montant
    def execute(self):
        self.compte.solde += self.montant
    def undo(self):
        self.compte.solde -= self.montant
```

### Solution Java

```java
interface Command { void execute(); void undo(); }

class Depot implements Command {
    private final Compte compte;
    private final double montant;
    public Depot(Compte compte, double montant) {
        this.compte = compte; this.montant = montant;
    }
    public void execute() { compte.solde += montant; }
    public void undo() { compte.solde -= montant; }
}
```
