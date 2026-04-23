# Cahier d'Exercices de Révision ULTIME : Programmation Python (C45)

Ce document contient des exercices allant des bases jusqu'aux concepts avancés de la POO et de l'algorithmique.

---

## Niveau 1 : Fondations (Saisie & Arithmétique)

### Exercice 1.1 : Calculateur de IMC
Demandez le poids (kg) et la taille (m) de l'utilisateur. Calculez l'Indice de Masse Corporelle (IMC = poids / taille²). Affichez le résultat avec deux décimales.

**Corrigé :**
```python
poids = float(input("Poids (kg) : "))
taille = float(input("Taille (m) : "))
imc = poids / (taille ** 2)
print(f"Votre IMC est de {imc:.2f}")
```

---

## Niveau 2 : Logique & Séquences (Strings & Listes)

### Exercice 2.1 : Manipulateur de texte
Demandez une phrase à l'utilisateur.
1. Affichez la phrase tout en majuscules.
2. Comptez le nombre de fois que la lettre "e" apparaît.
3. Affichez la phrase à l'envers.

**Corrigé :**
```python
phrase = input("Entrez une phrase : ")
print(f"Majuscules : {phrase.upper()}")
print(f"Nombre de 'e' : {phrase.lower().count('e')}")
print(f"Inverse : {phrase[::-1]}")
```

### Exercice 2.2 : Le Juste Prix (Boucle While)
Générez un nombre secret (disons 42). Demandez à l'utilisateur de deviner. Tant qu'il n'a pas trouvé, dites "Plus haut" ou "Plus bas". Affichez le nombre d'essais à la fin.

**Corrigé :**
```python
secret = 42
tentative = -1
essais = 0

while tentative != secret:
    tentative = int(input("Devinez le nombre : "))
    essais += 1
    if tentative < secret:
        print("Plus haut !")
    elif tentative > secret:
        print("Plus bas !")

print(f"Bravo ! Trouvé en {essais} essais.")
```

---

## Niveau 3 : Algorithmes Imbriqués

### Exercice 3.1 : La Table de Multiplication
Demandez un nombre `N`. Affichez la table de multiplication de 1 à 10 pour ce nombre, mais **uniquement pour les résultats pairs**.

**Corrigé :**
```python
n = int(input("Table de : "))
for i in range(1, 11):
    resultat = n * i
    if resultat % 2 == 0:
        print(f"{n} x {i} = {resultat}")
```

### Exercice 3.2 : Dessiner un Triangle
Demandez un nombre de lignes `L`. Affichez un triangle d'étoiles.
Exemple pour L=3 :
`*`
`**`
`***`

**Corrigé :**
```python
lignes = int(input("Nombre de lignes : "))
for i in range(1, lignes + 1):
    print("*" * i)
```

---

## Niveau 4 : Fonctions & Dictionnaires

### Exercice 4.1 : Gestionnaire d'inventaire
Créez une fonction `ajouter_produit(inventaire, nom, quantite)`. L'inventaire est un dictionnaire. Si le produit existe, augmentez la quantité, sinon ajoutez-le.

**Corrigé :**
```python
def ajouter_produit(inventaire, nom, quantite):
    if nom in inventaire:
        inventaire[nom] += quantite
    else:
        inventaire[nom] = quantite

# Test
mon_stock = {"Pommes": 10}
ajouter_produit(mon_stock, "Pommes", 5)
ajouter_produit(mon_stock, "Bananes", 20)
print(mon_stock) # {'Pommes': 15, 'Bananes': 20}
```

---

## Niveau 5 : POO Avancée (Héritage & Polymorphisme)

### Exercice 5.1 : Système d'Employés
1. Créez une classe `Employe` avec un nom et un salaire de base. Ajoutez une méthode `calculer_paie()` qui retourne le salaire.
2. Créez une classe `Developpeur` qui hérite d'Employe. Ajoutez un bonus fixe de 500$. Redéfinissez `calculer_paie()`.
3. Créez une classe `Vendeur` qui hérite d'Employe. Ajoutez une commission. Redéfinissez `calculer_paie()`.

**Corrigé :**
```python
class Employe:
    def __init__(self, nom, salaire):
        self.nom = nom
        self.salaire = salaire
    
    def calculer_paie(self):
        return self.salaire

class Developpeur(Employe):
    def calculer_paie(self):
        return self.salaire + 500

class Vendeur(Employe):
    def __init__(self, nom, salaire, commission):
        super().__init__(nom, salaire)
        self.commission = commission
    
    def calculer_paie(self):
        return self.salaire + self.commission

# Test du Polymorphisme
equipe = [Developpeur("Alice", 3000), Vendeur("Bob", 2000, 800)]
for emp in equipe:
    print(f"{emp.nom} recevra : {emp.calculer_paie()}$")
```

---

## Niveau 6 : Le Défi du "Boss" (Synthèse Totale)

### Exercice : Système de Bibliothèque
Créez un programme qui gère des `Livres`.
- Chaque `Livre` a un titre, un auteur et un statut (disponible ou emprunté).
- Créez une classe `Bibliotheque` qui contient une liste de livres.
- Ajoutez des méthodes pour :
    1. Ajouter un livre.
    2. Emprunter un livre (change le statut).
    3. Afficher uniquement les livres disponibles.

**Corrigé :**
```python
class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.disponible = True

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter(self, livre):
        self.livres.append(livre)

    def emprunter(self, titre):
        for livre in self.livres:
            if livre.titre == titre and livre.disponible:
                livre.disponible = False
                print(f"Vous avez emprunté : {titre}")
                return
        print("Livre non disponible.")

    def afficher_disponibles(self):
        print("--- Livres disponibles ---")
        for livre in self.livres:
            if livre.disponible:
                print(f"{livre.titre} par {livre.auteur}")

# Simulation
biblio = Bibliotheque()
biblio.ajouter(Livre("1984", "George Orwell"))
biblio.ajouter(Livre("Le Petit Prince", "St-Exupéry"))

biblio.afficher_disponibles()
biblio.emprunter("1984")
biblio.afficher_disponibles()
```

---
*Fin du cahier d'exercices. Si vous maîtrisez tout cela, vous êtes prêt pour l'examen !*
