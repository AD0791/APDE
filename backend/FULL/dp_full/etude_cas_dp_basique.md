# Étude de Cas Design Patterns — Niveau Basique

## Guide de Préparation : Patterns Creational et Observer

---

Ce document couvre les patterns essentiels avec des exercices concrets et des solutions en Python et Java.

---

## Problème 1 : Factory Method (Création de Compte)

### Énoncé

Créer des comptes bancaires de différents types sans utiliser de `switch` dans le code client.

### Solution Python

```python
from abc import ABC, abstractmethod

class Compte(ABC):
    def __init__(self, titulaire):
        self.titulaire = titulaire

class CompteCourant(Compte):
    pass

class CompteEpargne(Compte):
    pass

class CompteFactory(ABC):
    @abstractmethod
    def creer(self, titulaire):
        pass

class CompteCourantFactory(CompteFactory):
    def creer(self, titulaire):
        return CompteCourant(titulaire)

class CompteEpargneFactory(CompteFactory):
    def creer(self, titulaire):
        return CompteEpargne(titulaire)
```

### Solution Java

```java
abstract class Compte {
    protected String titulaire;
    public Compte(String titulaire) { this.titulaire = titulaire; }
}

class CompteCourant extends Compte {
    public CompteCourant(String titulaire) { super(titulaire); }
}

class CompteEpargne extends Compte {
    public CompteEpargne(String titulaire) { super(titulaire); }
}

interface CompteFactory {
    Compte creer(String titulaire);
}

class CompteCourantFactory implements CompteFactory {
    public Compte creer(String titulaire) { return new CompteCourant(titulaire); }
}

class CompteEpargneFactory implements CompteFactory {
    public Compte creer(String titulaire) { return new CompteEpargne(titulaire); }
}
```

---

## Problème 2 : Singleton (Configuration Bancaire)

### Énoncé

Assurer qu'une classe de configuration n'a qu'une seule instance.

### Solution Python

```python
class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.env = "prod"
        return cls._instance
```

### Solution Java

```java
public class Config {
    private static final Config INSTANCE = new Config();
    private String env = "prod";
    private Config() {}
    public static Config getInstance() { return INSTANCE; }
}
```

---

## Problème 3 : Observer (Notifications)

### Énoncé

Notifier les clients lorsqu'une transaction est effectuée.

### Solution Python

```python
class Observable:
    def __init__(self):
        self._observers = []
    def subscribe(self, obs):
        self._observers.append(obs)
    def notify(self, data):
        for o in self._observers:
            o.update(data)

class SMSObserver:
    def update(self, data):
        print("SMS:", data)
```

### Solution Java

```java
import java.util.ArrayList;
import java.util.List;

interface Observer {
    void update(String data);
}

class Observable {
    private final List<Observer> observers = new ArrayList<>();
    void subscribe(Observer o) { observers.add(o); }
    void notifyAll(String data) {
        for (Observer o : observers) o.update(data);
    }
}
```

---

## Problème 4 : Builder (Construction d'Objet Complexe)

### Énoncé

Construire un objet `Compte` avec des paramètres optionnels (devise, plafond, services).

### Solution Python

```python
class Compte:
    def __init__(self, titulaire, devise, plafond, services):
        self.titulaire = titulaire
        self.devise = devise
        self.plafond = plafond
        self.services = services

class CompteBuilder:
    def __init__(self, titulaire):
        self.titulaire = titulaire
        self.devise = "HTG"
        self.plafond = 0
        self.services = []
    def with_devise(self, devise):
        self.devise = devise; return self
    def with_plafond(self, plafond):
        self.plafond = plafond; return self
    def add_service(self, service):
        self.services.append(service); return self
    def build(self):
        return Compte(self.titulaire, self.devise, self.plafond, self.services)
```

### Solution Java

```java
class Compte {
    String titulaire;
    String devise;
    double plafond;
    java.util.List<String> services;
    private Compte(Builder b) {
        this.titulaire = b.titulaire;
        this.devise = b.devise;
        this.plafond = b.plafond;
        this.services = b.services;
    }
    static class Builder {
        String titulaire;
        String devise = "HTG";
        double plafond = 0;
        java.util.List<String> services = new java.util.ArrayList<>();
        Builder(String titulaire) { this.titulaire = titulaire; }
        Builder devise(String d) { this.devise = d; return this; }
        Builder plafond(double p) { this.plafond = p; return this; }
        Builder addService(String s) { this.services.add(s); return this; }
        Compte build() { return new Compte(this); }
    }
}
```

---

## Problème 5 : Facade (Simplifier un Sous-système)

### Énoncé

Fournir une interface simple pour ouvrir un compte et créer une carte.

### Solution Python

```python
class KYC:
    def verify(self, client): return True

class CardService:
    def create_card(self, client): return "CARD-001"

class AccountService:
    def open_account(self, client): return "ACC-001"

class BankFacade:
    def __init__(self):
        self.kyc = KYC()
        self.card = CardService()
        self.account = AccountService()
    def onboard(self, client):
        if not self.kyc.verify(client):
            raise ValueError("KYC echoue")
        acc = self.account.open_account(client)
        card = self.card.create_card(client)
        return acc, card
```

### Solution Java

```java
class KYC { boolean verify(String client) { return true; } }
class CardService { String createCard(String client) { return "CARD-001"; } }
class AccountService { String openAccount(String client) { return "ACC-001"; } }

class BankFacade {
    private final KYC kyc = new KYC();
    private final CardService card = new CardService();
    private final AccountService account = new AccountService();
    public String[] onboard(String client) {
        if (!kyc.verify(client)) throw new IllegalArgumentException("KYC echoue");
        String acc = account.openAccount(client);
        String cardId = card.createCard(client);
        return new String[]{acc, cardId};
    }
}
```
