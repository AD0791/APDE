# CAHIER D'EXERCICES MASTERY : VOLUME 2 (INTENSIF)

Ce volume se concentre sur l'interaction entre les structures de données, la logique de validation et la modélisation objet avancée.

---

## NIVEAU 5 : MANIPULATION DE COLLECTIONS & LOGIQUE MÉTIER
**Problème :** Créer un système de gestion de notes pour une classe. 
1. Saisir les noms de 5 étudiants et leurs notes respectives dans deux listes (ou un dictionnaire).
2. Calculer la moyenne de la classe.
3. Afficher le nom de l'étudiant ayant la meilleure note (Recherche de Maximum).

### Solution Algorithmie (Pseudo-code)
```
Variable Noms[5] en Chaîne
Variable Notes[5] en Réel
Variable i, index_max en Entier
Variable somme, moyenne, max en Réel
Début
  somme ← 0
  Pour i ← 0 à 4
    Écrire "Nom de l'étudiant ", i + 1
    Lire Noms[i]
    Écrire "Note de l'étudiant ", i + 1
    Lire Notes[i]
    somme ← somme + Notes[i]
  Fin Pour
  
  moyenne ← somme / 5
  max ← Notes[0]
  index_max ← 0
  
  Pour i ← 1 à 4
    Si Notes[i] > max Alors
      max ← Notes[i]
      index_max ← i
    Fin Si
  Fin Pour
  
  Écrire "Moyenne de la classe : ", moyenne
  Écrire "Major de promo : ", Noms[index_max], " avec ", max
Fin
```

### Solution Python
```python
noms = []
notes = []

for i in range(5):
    noms.append(input(f"Nom étudiant {i+1} : "))
    notes.append(float(input(f"Note étudiant {i+1} : ")))

moyenne = sum(notes) / len(notes)
note_max = max(notes)
index_major = notes.index(note_max)

print(f"Moyenne : {moyenne:.2f}")
print(f"Major : {noms[index_major]} ({note_max}/100)")
```

---

## NIVEAU 6 : ALGORITHMES DE RECHERCHE & VALIDATION DE CHAÎNES
**Problème :** Écrire une fonction `valider_email(email)` qui vérifie si une chaîne contient à la fois un `@` et un `.` (point). L'algorithme doit parcourir la chaîne caractère par caractère.

### Solution Algorithmie
```
Fonction valider_email(email en Chaîne) en Booléen
Variable i en Entier
Variable a_arobase, a_point en Booléen
Début
  a_arobase ← Faux
  a_point ← Faux
  Pour i ← 0 à Longueur(email) - 1
    Si email[i] = "@" Alors a_arobase ← Vrai Fin Si
    Si email[i] = "." Alors a_point ← Vrai Fin Si
  Fin Pour
  Retourner (a_arobase ET a_point)
Fin
```

### Solution Python
```python
def valider_email(email):
    a_arobase = False
    a_point = False
    for car in email:
        if car == "@":
            a_arobase = True
        if car == ".":
            a_point = True
    return a_arobase and a_point

# Test
print(valider_email("test@bdeb.qc.ca")) # True
```

---

## NIVEAU 7 : POO - COMPOSITION ET RÉGIME D'AFFAIRES
**Problème :** Modéliser un système de **Paie de Consultant**.
1. Une classe `Consultant` avec `nom` et `taux_horaire`.
2. Une méthode `calculer_salaire(heures)` qui applique une taxe de 20%.
3. Une classe `Projet` qui contient un `Consultant` (Composition) et le nombre d'heures travaillées. Une méthode `facturer()` qui appelle le calcul de paie du consultant.

### Solution Python
```python
class Consultant:
    def __init__(self, nom, taux):
        self.nom = nom
        self.taux = taux

    def calculer_paie(self, heures):
        salaire_brut = self.taux * heures
        return salaire_brut * 0.80 # 20% de retenue

class Projet:
    def __init__(self, nom_projet, consultant, heures_prevues):
        self.nom_projet = nom_projet
        self.consultant = consultant # Composition
        self.heures = heures_prevues

    def facturer(self):
        montant = self.consultant.calculer_paie(self.heures)
        print(f"Facturation Projet {self.nom_projet}")
        print(f"Payable à {self.consultant.nom} : {montant}$")

# Test
expert = Consultant("Disla", 100)
mon_projet = Projet("Migration Cloud", expert, 40)
mon_projet.facturer()
```

---

## NIVEAU 8 : DÉFI "INTELLIGENCE ARTIFICIELLE" (Synthèse)
**Problème :** Créer un algorithme qui simule un filtre de recommandation.
Soit une liste de films avec leurs catégories : `films = [{"titre": "Inception", "genre": "SF"}, {"titre": "Joker", "genre": "Drame"}]`.
Demandez à l'utilisateur son genre préféré et affichez tous les titres correspondants.

### Solution Python
```python
films = [
    {"titre": "Inception", "genre": "SF"},
    {"titre": "Interstellar", "genre": "SF"},
    {"titre": "Joker", "genre": "Drame"},
    {"titre": "Parasite", "genre": "Drame"}
]

pref = input("Quel genre préférez-vous (SF/Drame) ? ")
trouve = False

print(f"--- Recommandations {pref} ---")
for f in films:
    if f["genre"].upper() == pref.upper():
        print(f"- {f['titre']}")
        trouve = True

if not trouve:
    print("Aucun film trouvé pour ce genre.")
```

---
*Ce volume 2 complète votre préparation pour les aspects dynamiques et modulaires du cours.*
