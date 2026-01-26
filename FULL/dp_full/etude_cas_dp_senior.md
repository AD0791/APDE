# Étude de Cas Design Patterns — Niveau Senior

## Guide de Préparation : Architecture et Patterns Comportementaux Avancés

---

Ce document avancé cible des patterns de structuration d'architecture et de responsabilités.

---

## Problème 1 : Chain of Responsibility (Validation de Transaction)

### Énoncé

Valider une transaction bancaire via une chaîne de règles (solde suffisant, limites, conformité).

### Solution Python

```python
class Handler:
    def __init__(self, nxt=None):
        self.nxt = nxt
    def handle(self, ctx):
        if self.nxt:
            return self.nxt.handle(ctx)
        return True

class SoldeCheck(Handler):
    def handle(self, ctx):
        if ctx["solde"] < ctx["montant"]:
            return False
        return super().handle(ctx)

class LimitCheck(Handler):
    def handle(self, ctx):
        if ctx["montant"] > ctx["limite"]:
            return False
        return super().handle(ctx)
```

### Solution Java

```java
abstract class Handler {
    protected Handler next;
    public Handler linkWith(Handler next) { this.next = next; return next; }
    public boolean handle(Context ctx) {
        return next == null || next.handle(ctx);
    }
}

class SoldeCheck extends Handler {
    public boolean handle(Context ctx) {
        if (ctx.solde < ctx.montant) return false;
        return super.handle(ctx);
    }
}

class LimitCheck extends Handler {
    public boolean handle(Context ctx) {
        if (ctx.montant > ctx.limite) return false;
        return super.handle(ctx);
    }
}
```

---

## Problème 2 : Command (Journaliser des Actions)

### Énoncé

Encapsuler des actions (depot, retrait) pour pouvoir les journaliser et annuler.

### Solution Python

```python
class Command:
    def execute(self):
        raise NotImplementedError
    def undo(self):
        raise NotImplementedError

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
interface Command {
    void execute();
    void undo();
}

class Depot implements Command {
    private final Compte compte;
    private final double montant;
    public Depot(Compte compte, double montant) {
        this.compte = compte;
        this.montant = montant;
    }
    public void execute() { compte.solde += montant; }
    public void undo() { compte.solde -= montant; }
}
```

---

## Problème 3 : Proxy (Accès Contrôlé aux Données)

### Énoncé

Limiter l'accès à des informations sensibles via un proxy.

### Solution Python

```python
class CompteService:
    def get_solde(self, user):
        return 12500

class CompteServiceProxy:
    def __init__(self, service):
        self.service = service
    def get_solde(self, user):
        if user.get("role") != "ADMIN":
            raise PermissionError("Acces refuse")
        return self.service.get_solde(user)
```

### Solution Java

```java
class CompteService {
    public double getSolde(User user) { return 12500; }
}

class CompteServiceProxy {
    private final CompteService service = new CompteService();
    public double getSolde(User user) {
        if (!"ADMIN".equals(user.role)) {
            throw new SecurityException("Acces refuse");
        }
        return service.getSolde(user);
    }
}
```

---

## Problème 4 : State (Cycle de Vie d'un Compte)

### Énoncé

Gérer les états d'un compte (ACTIF, BLOQUE, FERME) et leurs transitions.

### Solution Python

```python
class State:
    def retirer(self, compte, montant):
        raise NotImplementedError

class Actif(State):
    def retirer(self, compte, montant):
        if compte.solde < montant:
            raise ValueError("Solde insuffisant")
        compte.solde -= montant

class Bloque(State):
    def retirer(self, compte, montant):
        raise PermissionError("Compte bloque")
```

### Solution Java

```java
interface State {
    void retirer(Compte compte, double montant);
}

class Actif implements State {
    public void retirer(Compte compte, double montant) {
        if (compte.solde < montant) throw new IllegalArgumentException("Solde insuffisant");
        compte.solde -= montant;
    }
}

class Bloque implements State {
    public void retirer(Compte compte, double montant) {
        throw new SecurityException("Compte bloque");
    }
}
```

---

## Problème 5 : Mediator (Coordination de Services)

### Énoncé

Coordonner KYC, scoring et approbation sans couplage direct.

### Solution Python

```python
class Mediator:
    def __init__(self, kyc, score, approve):
        self.kyc = kyc
        self.score = score
        self.approve = approve
    def process(self, dossier):
        if not self.kyc.check(dossier):
            return False
        if not self.score.run(dossier):
            return False
        return self.approve.ok(dossier)
```

### Solution Java

```java
class Mediator {
    private final KycService kyc;
    private final ScoreService score;
    private final ApproveService approve;
    Mediator(KycService k, ScoreService s, ApproveService a) {
        this.kyc = k; this.score = s; this.approve = a;
    }
    boolean process(String dossier) {
        if (!kyc.check(dossier)) return false;
        if (!score.run(dossier)) return false;
        return approve.ok(dossier);
    }
}
```

---

## Problème 6 : Interpreter (Règles Simples)

### Énoncé

Interpréter une règle simple: "solde > 10000 ET statut = VIP".

### Solution Python

```python
class Rule:
    def eval(self, ctx): raise NotImplementedError

class AndRule(Rule):
    def __init__(self, left, right):
        self.left = left; self.right = right
    def eval(self, ctx):
        return self.left.eval(ctx) and self.right.eval(ctx)

class SoldeRule(Rule):
    def eval(self, ctx): return ctx["solde"] > 10000

class StatutRule(Rule):
    def eval(self, ctx): return ctx["statut"] == "VIP"
```

### Solution Java

```java
interface Rule { boolean eval(Context ctx); }

class AndRule implements Rule {
    private final Rule left, right;
    AndRule(Rule l, Rule r) { left = l; right = r; }
    public boolean eval(Context ctx) { return left.eval(ctx) && right.eval(ctx); }
}

class SoldeRule implements Rule {
    public boolean eval(Context ctx) { return ctx.solde > 10000; }
}

class StatutRule implements Rule {
    public boolean eval(Context ctx) { return "VIP".equals(ctx.statut); }
}
```
