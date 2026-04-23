# CAHIER D'EXERCICES MASTERY : MAÎTRISE TOTALE (C45)

Ce cahier teste votre capacité à transformer un problème complexe en une solution élégante. Chaque exercice inclut la solution en Algorithmie (Pseudo-code) ET en Python.

---

## NIVEAU 1 : LOGIQUE DE BASE & VALIDATION
**Problème :** Demander un nombre d'étudiants (positif). Pour chaque étudiant, demander sa note. Si la note est invalide (pas entre 0 et 100), redemander jusqu'à ce qu'elle soit correcte.

### Solution Algorithmie
```
Variable nb_etud, i en Entier
Variable note en Réel
Début
  Répéter
    Écrire "Nombre d'étudiants ?"
    Lire nb_etud
  Jusqu'à nb_etud > 0
  
  Pour i ← 0 à nb_etud - 1
    Répéter
      Écrire "Note de l'étudiant ", i + 1
      Lire note
    Jusqu'à note >= 0 ET note <= 100
  Fin Pour
Fin
```

### Solution Python
```python
nb_etud = 0
while nb_etud <= 0:
    nb_etud = int(input("Nombre d'étudiants ? "))

for i in range(nb_etud):
    note = -1
    while not (0 <= note <= 100):
        note = float(input(f"Note étudiant {i+1} : "))
```

---

## NIVEAU 2 : TABLEAUX ET TRAITEMENT STATISTIQUE
**Problème :** À partir d'un tableau de 10 températures, calculer la moyenne, trouver la température maximale et compter combien sont sous le point de congélation (0°C).

### Solution Algorithmie (Extraction)
```
Variable Tab[10] en Réel
Variable moyenne, max, somme en Réel
Variable i, nb_gel en Entier
Début
  somme ← 0
  nb_gel ← 0
  max ← Tab[0]
  Pour i ← 0 à 9
    somme ← somme + Tab[i]
    Si Tab[i] > max Alors
      max ← Tab[i]
    Fin Si
    Si Tab[i] < 0 Alors
      nb_gel ← nb_gel + 1
    Fin Si
  Fin Pour
  moyenne ← somme / 10
  Écrire "Moyenne:", moyenne, " Max:", max, " Gel:", nb_gel
Fin
```

---

## NIVEAU 3 : MODULARITÉ & FONCTIONS (Le Défi de l'Impôt)
**Problème :** Créer une fonction `calculer_impot(salaire)` qui retourne 15% si < 30k, 25% sinon. Créer une procédure `afficher_releve(nom, impot)` qui affiche le nom et le montant.

### Solution Python
```python
def calculer_impot(salaire):
    if salaire < 30000:
        return salaire * 0.15
    return salaire * 0.25

def afficher_releve(nom, impot):
    print(f"--- RELEVÉ POUR {nom.upper()} ---")
    print(f"Impôt à payer : {impot}$")

# Appel
nom_client = input("Nom : ")
sal = float(input("Salaire : "))
montant = calculer_impot(sal)
afficher_releve(nom_client, montant)
```

---

## NIVEAU 4 : POO AVANCÉE (Synthèse Académique)
**Problème :** Créer une classe `Vehicule` (marque, prix). Créer une classe `Auto` (hérite de Vehicule) avec un attribut `nb_portes`. Créer une classe `Moto` (hérite de Vehicule) avec un attribut `cylindree`. Ajouter une méthode `afficher()` qui utilise le polymorphisme.

### Solution Python Master
```python
class Vehicule:
    def __init__(self, marque, prix):
        self.marque = marque
        self.prix = prix
    
    def afficher(self):
        print(f"Marque: {self.marque}, Prix: {self.prix}$")

class Auto(Vehicule):
    def __init__(self, marque, prix, nb_portes):
        super().__init__(marque, prix)
        self.nb_portes = nb_portes
    
    def afficher(self):
        super().afficher()
        print(f"Type: Auto, Portes: {self.nb_portes}")

class Moto(Vehicule):
    def __init__(self, marque, prix, cylindree):
        super().__init__(marque, prix)
        self.cylindree = cylindree
    
    def afficher(self):
        super().afficher()
        print(f"Type: Moto, Cylindrée: {self.cylindree}cc")

# Simulation
flotte = [Auto("Toyota", 25000, 4), Moto("Honda", 12000, 600)]
for v in flotte:
    v.afficher()
    print("-" * 20)
```

---
*Fin du cahier Mastery. Si vous résolvez ces exercices sans aide, vous visez le 100%.*
