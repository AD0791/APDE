# Manuel de 100 Exercices Corrigés : Spécialiste en Intégration de Données

Ce manuel présente 100 exercices progressifs. Chaque solution contient le pseudocode et le code Python.

---

## Niveau 1 : Bases, Types et Entrées/Sorties (1-25)

### Exercice 1 : Accueil du Système
**Énoncé** : Demander le nom de l'opérateur de données et afficher "Session de nettoyage lancée pour : [nom]".
**Pseudocode** :
```text
Saisir operateur
Afficher "Session de nettoyage lancée pour : " + operateur
```
**Code Python** :
```python
operateur = input("Nom de l'opérateur : ")
print("Session de nettoyage lancée pour : {}".format(operateur))
```

### Exercice 2 : Calcul de Volume de Données
**Énoncé** : Saisir la taille d'un fichier en octets et l'afficher en Ko (1 Ko = 1024 octets).
**Code Python** :
```python
taille_octets = int(input("Taille en octets : "))
taille_ko = taille_octets / 1024
print("Taille : {:.2f} Ko".format(taille_ko))
```

### Exercice 3 : Conversion de Type Forcée
**Énoncé** : Saisir un prix (chaîne) et lui ajouter 15% de taxes. Afficher le résultat formaté.
**Code Python** :
```python
prix_str = input("Prix de base : ")
prix_float = float(prix_str)
total = prix_float * 1.15
print("Total avec taxes : {:.2f}$".format(total))
```

### Exercice 4 : Vérification d'Intégrité Simple
**Énoncé** : Saisir un ID. Afficher `True` si l'ID est de type numérique (entier), sinon `False`.
**Code Python** :
```python
saisie = input("Saisir ID : ")
print("Est numérique : {}".format(saisie.isdigit()))
```

### Exercice 5 : Concaténation de Métadonnées
**Énoncé** : Demander le nom d'un serveur et son port (ex: 8080). Afficher l'URL : "http://[serveur]:[port]".
**Code Python** :
```python
serveur = input("Nom serveur : ")
port = input("Port : ")
print("URL : http://{}:{}".format(serveur, port))
```

### Exercice 6 : Calcul de Ratio de Succès
**Énoncé** : Saisir lignes_total et lignes_reussies. Afficher le % de succès.
**Code Python** :
```python
total = int(input("Total : "))
reussies = int(input("Réussies : "))
ratio = (reussies / total) * 100
print("Taux de succès : {:.1f}%".format(ratio))
```

### Exercice 7 : Division de Données (Lots)
**Énoncé** : Saisir un nombre de lignes. Si on les traite par paquets de 50, combien de lignes reste-t-il dans le dernier lot incomplet ?
**Code Python** :
```python
lignes = int(input("Nombre de lignes : "))
reste = lignes % 50
print("Lignes dans le lot incomplet : {}".format(reste))
```

### Exercice 8 : Temps de Transfert
**Énoncé** : Saisir taille (Mo) et vitesse (Mo/s). Afficher le temps en secondes.
**Code Python** :
```python
taille = float(input("Taille Mo : "))
vitesse = float(input("Vitesse Mo/s : "))
temps = taille / vitesse
print("Temps estimé : {:.2f}s".format(temps))
```

### Exercice 9 : Formatage de Nom de Champ
**Énoncé** : Saisir un nom de colonne. L'afficher tout en majuscules avec des espaces remplacés par des underscores.
**Code Python** :
```python
col = input("Nom colonne : ")
clean_col = col.upper().replace(" ", "_")
print("Format DB : {}".format(clean_col))
```

### Exercice 10 : Incrémentation d'Identifiant
**Énoncé** : Saisir un ID actuel et afficher l'ID suivant (ID + 1).
**Code Python** :
```python
actuel = int(input("ID actuel : "))
print("Prochain ID : {}".format(actuel + 1))
```

### Exercice 11 : Moyenne de Latence
**Énoncé** : Saisir 3 mesures de latence (ms) et afficher la moyenne arrondie à l'entier.
**Code Python** :
```python
l1 = int(input("L1 : "))
l2 = int(input("L2 : "))
l3 = int(input("L3 : "))
moy = round((l1 + l2 + l3) / 3)
print("Latence moyenne : {}ms".format(moy))
```

### Exercice 12 : Inversion de Données (Swap)
**Énoncé** : Saisir A et B, puis les échanger et afficher les nouvelles valeurs.
**Code Python** :
```python
a = input("A : ")
b = input("B : ")
a, b = b, a
print("A est maintenant : {}, B est maintenant : {}".format(a, b))
```

### Exercice 13 : Calcul de Puissance de Calcul
**Énoncé** : Saisir un nombre X. Calculer X au carré et X au cube.
**Code Python** :
```python
x = int(input("X : "))
print("X^2 : {}, X^3 : {}".format(x**2, x**3))
```

### Exercice 14 : Validation de Longueur de Champ
**Énoncé** : Saisir un code postal. Afficher sa longueur.
**Code Python** :
```python
cp = input("Code postal : ")
print("Longueur : {} caractères".format(len(cp)))
```

### Exercice 15 : Calcul de Remise Data
**Énoncé** : Un service coûte 100$. Saisir un % de remise et afficher le prix final.
**Code Python** :
```python
remise = float(input("Remise (%) : "))
final = 100 * (1 - remise/100)
print("Prix final : {}$".format(final))
```

### Exercice 16 : Formatage de Date Simple
**Énoncé** : Saisir jour, mois, annee (entiers). Afficher "Date : JJ/MM/AAAA".
**Code Python** :
```python
j = int(input("Jour : "))
m = int(input("Mois : "))
a = int(input("Année : "))
print("Date : {:02d}/{:02d}/{}".format(j, m, a))
```

### Exercice 17 : Extraction de Premier Caractère
**Énoncé** : Saisir un nom de fichier. Afficher le premier caractère (souvent indicateur du type).
**Code Python** :
```python
f = input("Fichier : ")
print("Premier caractère : {}".format(f[0]))
```

### Exercice 18 : Calcul de Revenu par Ligne
**Énoncé** : Saisir revenu total et nb lignes. Afficher revenu moyen par ligne.
**Code Python** :
```python
rev = float(input("Revenu : "))
nb = int(input("Lignes : "))
print("Moyenne/ligne : {:.4f}".format(rev/nb))
```

### Exercice 19 : Test d'Appartenance Simple
**Énoncé** : Saisir une phrase. Vérifier si le mot "ERREUR" est présent (Affiche True/False).
**Code Python** :
```python
txt = input("Log : ")
print("Erreur détectée : {}".format("ERREUR" in txt.upper()))
```

### Exercice 20 : Division Entière de Ressources
**Énoncé** : Répartir 100 Go sur X serveurs équitablement (en entiers). Combien chaque serveur reçoit-il ?
**Code Python** :
```python
x = int(input("Nb serveurs : "))
print("Part/serveur : {} Go".format(100 // x))
```

### Exercice 21 : Création d'Email Professionnel
**Énoncé** : Saisir prenom et nom. Générer : "prenom.nom@entreprise.ca" en minuscules.
**Code Python** :
```python
p = input("Prénom : ")
n = input("Nom : ")
print("Email : {}.{}@entreprise.ca".format(p.lower(), n.lower()))
```

### Exercice 22 : Calcul de Périmètre de Stockage
**Énoncé** : Saisir la largeur et longueur d'un rack. Afficher le périmètre.
**Code Python** :
```python
l = float(input("Largeur : "))
h = float(input("Longueur : "))
print("Périmètre : {}".format(2*(l+h)))
```

### Exercice 23 : Répétition de Signal
**Énoncé** : Saisir un caractère et un nombre N. Afficher le caractère répété N fois.
**Code Python** :
```python
c = input("Signal : ")
n = int(input("Répétitions : "))
print(c * n)
```

### Exercice 24 : Vérification de Type Booléen
**Énoncé** : Affecter True à une variable `est_valide`. Afficher son type.
**Code Python** :
```python
est_valide = True
print(type(est_valide))
```

### Exercice 25 : Calcul de Différence d'Années
**Énoncé** : Saisir année actuelle et année de naissance. Afficher l'âge.
**Code Python** :
```python
act = 2024
naiss = int(input("Année naissance : "))
print("Âge estimé : {}".format(act - naiss))
```

---

## Niveau 2 : Structures de TEST (26-50)

### Exercice 26 : TEST de Validation d'Âge
**Énoncé** : Saisir un âge. Si l'âge est >= 18, afficher "Accès Data autorisé", sinon "Accès refusé".
**Pseudocode** :
```text
Saisir age
Si age >= 18 Alors
    Afficher "Accès autorisé"
Sinon
    Afficher "Accès refusé"
```
**Code Python** :
```python
age = int(input("Âge : "))
if age >= 18:
    print("Accès Data autorisé")
else:
    print("Accès refusé")
```

### Exercice 27 : TEST de Valeur Nulle (Nettoyage)
**Énoncé** : Saisir une valeur. Si elle est vide (""), afficher "Donnée manquante", sinon afficher la valeur.
**Code Python** :
```python
val = input("Entrer donnée : ")
if val == "":
    print("Donnée manquante")
else:
    print("Valeur : {}".format(val))
```

### Exercice 28 : TEST de Parité d'Index
**Énoncé** : Saisir un index de ligne. Afficher "Ligne Paire" ou "Ligne Impaire".
**Code Python** :
```python
idx = int(input("Index : "))
if idx % 2 == 0:
    print("Ligne Paire")
else:
    print("Ligne Impaire")
```

### Exercice 29 : Comparaison de Deux Serveurs
**Énoncé** : Saisir la charge de deux serveurs. Afficher le nom du serveur le plus chargé.
**Code Python** :
```python
s1 = float(input("Charge S1 (%) : "))
s2 = float(input("Charge S2 (%) : "))
if s1 > s2:
    print("Serveur 1 est plus sollicité")
elif s2 > s1:
    print("Serveur 2 est plus sollicité")
else:
    print("Charges égales")
```

### Exercice 30 : TEST de Seuil d'Alerte
**Énoncé** : Saisir une température. Si > 35, afficher "ALERTE CHALEUR", sinon "Température normale".
**Code Python** :
```python
temp = float(input("Température : "))
if temp > 35:
    print("ALERTE CHALEUR")
else:
    print("Température normale")
```

### Exercice 31 : Validation de Format Email
**Énoncé** : Vérifier si un email contient "@". Afficher "Valide" ou "Invalide".
**Code Python** :
```python
email = input("Email : ")
if "@" in email:
    print("Valide")
else:
    print("Invalide")
```

### Exercice 32 : TEST Multi-voies de Grade
**Énoncé** : Saisir une note. >= 90 (A), >= 80 (B), >= 70 (C), sinon (Echec).
**Code Python** :
```python
note = int(input("Note : "))
if note >= 90:
    print("Grade A")
elif note >= 80:
    print("Grade B")
elif note >= 70:
    print("Grade C")
else:
    print("Echec")
```

### Exercice 33 : Calcul de Frais de Port
**Énoncé** : Saisir montant commande. Si >= 100$, frais = 0$. Sinon, frais = 10$.
**Code Python** :
```python
mt = float(input("Montant : "))
frais = 0 if mt >= 100 else 10
print("Frais : {}$".format(frais))
```

### Exercice 34 : TEST de Positivité
**Énoncé** : Saisir un nombre. Afficher s'il est Positif, Négatif ou Nul.
**Code Python** :
```python
n = float(input("Nombre : "))
if n > 0:
    print("Positif")
elif n < 0:
    print("Négatif")
else:
    print("Nul")
```

### Exercice 35 : Vérification de Mot de Passe
**Énoncé** : Saisir un mot de passe. S'il est égal à "admin123", afficher "Accès accordé".
**Code Python** :
```python
mdp = input("Mot de passe : ")
if mdp == "admin123":
    print("Accès accordé")
else:
    print("Refusé")
```

### Exercice 36 : TEST de Divisibilité par 5 et 3
**Énoncé** : Saisir un nombre. Vérifier s'il est divisible par 15 (3 et 5).
**Code Python** :
```python
n = int(input("N : "))
if n % 3 == 0 and n % 5 == 0:
    print("Divisible par 3 et 5")
else:
    print("Non divisible")
```

### Exercice 37 : Classification de Fichiers
**Énoncé** : Saisir taille Mo. < 10 (Petit), < 100 (Moyen), sinon (Gros).
**Code Python** :
```python
t = float(input("Taille Mo : "))
if t < 10:
    print("Petit")
elif t < 100:
    print("Moyen")
else:
    print("Gros")
```

### Exercice 38 : TEST de Domaine (Data Integration)
**Énoncé** : Saisir une URL. Si elle finit par ".ca", afficher "Domaine Canadien".
**Code Python** :
```python
url = input("URL : ")
if url.endswith(".ca"):
    print("Domaine Canadien")
else:
    print("Autre domaine")
```

### Exercice 39 : Calculateur de Rabais Quantité
**Énoncé** : Saisir quantité. Si > 50, -20%. Si > 20, -10%. Sinon 0%.
**Code Python** :
```python
q = int(input("Quantité : "))
if q > 50:
    rabais = 0.20
elif q > 20:
    rabais = 0.10
else:
    rabais = 0
print("Rabais appliqué : {:.0%}".format(rabais))
```

### Exercice 40 : TEST de Jour Ouvrable
**Énoncé** : Saisir un numéro de jour (1-7). Si 6 ou 7, afficher "Weekend", sinon "Travail".
**Code Python** :
```python
j = int(input("Jour (1-7) : "))
if j == 6 or j == 7:
    print("Weekend")
else:
    print("Travail")
```

### Exercice 41 : TEST de Login Triple
**Énoncé** : Saisir user et mdp. Si user=="admin" et mdp=="123", OK. Sinon Erreur.
**Code Python** :
```python
u = input("User : ")
m = input("Pass : ")
if u == "admin" and m == "123":
    print("OK")
else:
    print("Erreur")
```

### Exercice 42 : Validation de Note de Passage
**Énoncé** : Saisir note. Si >= 60, "Réussite", sinon "Échec". Utiliser opérateur ternaire.
**Code Python** :
```python
n = int(input("Note : "))
res = "Réussite" if n >= 60 else "Échec"
print(res)
```

### Exercice 43 : TEST de Saisie Numérique (Sécurisé)
**Énoncé** : Saisir une valeur. Utiliser  après conversion pour vérifier si c'est un float. (Note: input est str, donc on teste si le float() réussit).
**Code Python** :
```python
s = input("Valeur : ")
try:
    v = float(s)
    print("C'est un nombre valide")
except:
    print("Erreur de type")
```

### Exercice 44 : Comparaison de Longueur de Chaînes
**Énoncé** : Saisir deux noms de colonnes. Afficher la plus longue.
**Code Python** :
```python
c1 = input("Col 1 : ")
c2 = input("Col 2 : ")
if len(c1) > len(c2):
    print(c1)
else:
    print(c2)
```

### Exercice 45 : TEST de Multi-Filtre (AND)
**Énoncé** : Une ligne est valide si  ET .
**Code Python** :
```python
age = int(input("Age : "))
ville = input("Ville : ")
if age > 18 and ville.lower() == "montreal":
    print("Ligne valide")
else:
    print("Ligne rejetée")
```

### Exercice 46 : TEST de Multi-Filtre (OR)
**Énoncé** : Un client a droit à un cadeau si  OU .
**Code Python** :
```python
mt = float(input("Achat : "))
m = input("Membre (O/N) : ")
if mt > 500 or m.upper() == "O":
    print("Cadeau !")
else:
    print("Pas de cadeau")
```

### Exercice 47 : TEST de Négation (NOT)
**Énoncé** : Si le fichier n'est pas vide (taille != 0), procéder au traitement.
**Code Python** :
```python
t = int(input("Taille : "))
if not t == 0:
    print("Traitement...")
else:
    print("Fichier vide")
```

### Exercice 48 : Classification de Température Datacenter
**Énoncé** : < 18 (Trop froid), 18-24 (Idéal), > 24 (Trop chaud).
**Code Python** :
```python
t = float(input("T : "))
if t < 18:
    print("Froid")
elif t <= 24:
    print("Idéal")
else:
    print("Chaud")
```

### Exercice 49 : TEST de Caractère de Contrôle
**Énoncé** : Saisir une ligne. Si elle commence par "#", c'est un commentaire.
**Code Python** :
```python
l = input("Ligne : ")
if l.startswith("#"):
    print("Commentaire")
else:
    print("Donnée")
```

### Exercice 50 : TEST d'Année Bissextile (Logique)
**Énoncé** : Saisir année. Si (divisible par 4 AND non par 100) OR divisible par 400.
**Code Python** :
```python
a = int(input("Année : "))
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print("Bissextile")
else:
    print("Normale")
```

---

## Niveau 2 : Structures de TEST (26-50)

### Exercice 26 : TEST de Validation d'Âge
**Énoncé** : Saisir un âge. Si l'âge est >= 18, afficher "Accès Data autorisé", sinon "Accès refusé".
**Pseudocode** :
```text
Saisir age
Si age >= 18 Alors
    Afficher "Accès autorisé"
Sinon
    Afficher "Accès refusé"
```
**Code Python** :
```python
age = int(input("Âge : "))
if age >= 18:
    print("Accès Data autorisé")
else:
    print("Accès refusé")
```

### Exercice 27 : TEST de Valeur Nulle (Nettoyage)
**Énoncé** : Saisir une valeur. Si elle est vide (""), afficher "Donnée manquante", sinon afficher la valeur.
**Code Python** :
```python
val = input("Entrer donnée : ")
if val == "":
    print("Donnée manquante")
else:
    print("Valeur : {}".format(val))
```

### Exercice 28 : TEST de Parité d'Index
**Énoncé** : Saisir un index de ligne. Afficher "Ligne Paire" ou "Ligne Impaire".
**Code Python** :
```python
idx = int(input("Index : "))
if idx % 2 == 0:
    print("Ligne Paire")
else:
    print("Ligne Impaire")
```

### Exercice 29 : Comparaison de Deux Serveurs
**Énoncé** : Saisir la charge de deux serveurs. Afficher le nom du serveur le plus chargé.
**Code Python** :
```python
s1 = float(input("Charge S1 (%) : "))
s2 = float(input("Charge S2 (%) : "))
if s1 > s2:
    print("Serveur 1 est plus sollicité")
elif s2 > s1:
    print("Serveur 2 est plus sollicité")
else:
    print("Charges égales")
```

### Exercice 30 : TEST de Seuil d'Alerte
**Énoncé** : Saisir une température. Si > 35, afficher "ALERTE CHALEUR", sinon "Température normale".
**Code Python** :
```python
temp = float(input("Température : "))
if temp > 35:
    print("ALERTE CHALEUR")
else:
    print("Température normale")
```

### Exercice 31 : Validation de Format Email
**Énoncé** : Vérifier si un email contient "@". Afficher "Valide" ou "Invalide".
**Code Python** :
```python
email = input("Email : ")
if "@" in email:
    print("Valide")
else:
    print("Invalide")
```

### Exercice 32 : TEST Multi-voies de Grade
**Énoncé** : Saisir une note. >= 90 (A), >= 80 (B), >= 70 (C), sinon (Echec).
**Code Python** :
```python
note = int(input("Note : "))
if note >= 90:
    print("Grade A")
elif note >= 80:
    print("Grade B")
elif note >= 70:
    print("Grade C")
else:
    print("Echec")
```

### Exercice 33 : Calcul de Frais de Port
**Énoncé** : Saisir montant commande. Si >= 100$, frais = 0$. Sinon, frais = 10$.
**Code Python** :
```python
mt = float(input("Montant : "))
frais = 0 if mt >= 100 else 10
print("Frais : {}$".format(frais))
```

### Exercice 34 : TEST de Positivité
**Énoncé** : Saisir un nombre. Afficher s'il est Positif, Négatif ou Nul.
**Code Python** :
```python
n = float(input("Nombre : "))
if n > 0:
    print("Positif")
elif n < 0:
    print("Négatif")
else:
    print("Nul")
```

### Exercice 35 : Vérification de Mot de Passe
**Énoncé** : Saisir un mot de passe. S'il est égal à "admin123", afficher "Accès accordé".
**Code Python** :
```python
mdp = input("Mot de passe : ")
if mdp == "admin123":
    print("Accès accordé")
else:
    print("Refusé")
```

### Exercice 36 : TEST de Divisibilité par 5 et 3
**Énoncé** : Saisir un nombre. Vérifier s'il est divisible par 15 (3 et 5).
**Code Python** :
```python
n = int(input("N : "))
if n % 3 == 0 and n % 5 == 0:
    print("Divisible par 3 et 5")
else:
    print("Non divisible")
```

### Exercice 37 : Classification de Fichiers
**Énoncé** : Saisir taille Mo. < 10 (Petit), < 100 (Moyen), sinon (Gros).
**Code Python** :
```python
t = float(input("Taille Mo : "))
if t < 10:
    print("Petit")
elif t < 100:
    print("Moyen")
else:
    print("Gros")
```

### Exercice 38 : TEST de Domaine (Data Integration)
**Énoncé** : Saisir une URL. Si elle finit par ".ca", afficher "Domaine Canadien".
**Code Python** :
```python
url = input("URL : ")
if url.endswith(".ca"):
    print("Domaine Canadien")
else:
    print("Autre domaine")
```

### Exercice 39 : Calculateur de Rabais Quantité
**Énoncé** : Saisir quantité. Si > 50, -20%. Si > 20, -10%. Sinon 0%.
**Code Python** :
```python
q = int(input("Quantité : "))
if q > 50:
    rabais = 0.20
elif q > 20:
    rabais = 0.10
else:
    rabais = 0
print("Rabais appliqué : {:.0%}".format(rabais))
```

### Exercice 40 : TEST de Jour Ouvrable
**Énoncé** : Saisir un numéro de jour (1-7). Si 6 ou 7, afficher "Weekend", sinon "Travail".
**Code Python** :
```python
j = int(input("Jour (1-7) : "))
if j == 6 or j == 7:
    print("Weekend")
else:
    print("Travail")
```

### Exercice 41 : TEST de Login Triple
**Énoncé** : Saisir user et mdp. Si user=="admin" et mdp=="123", OK. Sinon Erreur.
**Code Python** :
```python
u = input("User : ")
m = input("Pass : ")
if u == "admin" and m == "123":
    print("OK")
else:
    print("Erreur")
```

### Exercice 42 : Validation de Note de Passage
**Énoncé** : Saisir note. Si >= 60, "Réussite", sinon "Échec". Utiliser opérateur ternaire.
**Code Python** :
```python
n = int(input("Note : "))
res = "Réussite" if n >= 60 else "Échec"
print(res)
```

### Exercice 43 : TEST de Saisie Numérique (Sécurisé)
**Énoncé** : Saisir une valeur. Vérifier si c'est un nombre avant de traiter.
**Code Python** :
```python
s = input("Valeur : ")
if s.replace('.','',1).isdigit():
    print("C'est un nombre valide")
else:
    print("Erreur de format")
```

### Exercice 44 : Comparaison de Longueur de Chaînes
**Énoncé** : Saisir deux noms de colonnes. Afficher la plus longue.
**Code Python** :
```python
c1 = input("Col 1 : ")
c2 = input("Col 2 : ")
if len(c1) > len(c2):
    print(c1)
else:
    print(c2)
```

### Exercice 45 : TEST de Multi-Filtre (AND)
**Énoncé** : Une ligne est valide si age > 18 ET ville == "Montreal".
**Code Python** :
```python
age = int(input("Age : "))
ville = input("Ville : ")
if age > 18 and ville.lower() == "montreal":
    print("Ligne valide")
else:
    print("Ligne rejetée")
```

### Exercice 46 : TEST de Multi-Filtre (OR)
**Énoncé** : Un client a droit à un cadeau si achat > 500 OU est_membre == "O".
**Code Python** :
```python
mt = float(input("Achat : "))
m = input("Membre (O/N) : ")
if mt > 500 or m.upper() == "O":
    print("Cadeau !")
else:
    print("Pas de cadeau")
```

### Exercice 47 : TEST de Négation (NOT)
**Énoncé** : Si le fichier n'est pas vide (taille != 0), procéder au traitement.
**Code Python** :
```python
t = int(input("Taille : "))
if not t == 0:
    print("Traitement...")
else:
    print("Fichier vide")
```

### Exercice 48 : Classification de Température Datacenter
**Énoncé** : < 18 (Trop froid), 18-24 (Idéal), > 24 (Trop chaud).
**Code Python** :
```python
t = float(input("T : "))
if t < 18:
    print("Froid")
elif t <= 24:
    print("Idéal")
else:
    print("Chaud")
```

### Exercice 49 : TEST de Caractère de Contrôle
**Énoncé** : Saisir une ligne. Si elle commence par "#", c'est un commentaire.
**Code Python** :
```python
l = input("Ligne : ")
if l.startswith("#"):
    print("Commentaire")
else:
    print("Donnée")
```

### Exercice 50 : TEST d'Année Bissextile (Logique)
**Énoncé** : Saisir année. Si (divisible par 4 AND non par 100) OR divisible par 400.
**Code Python** :
```python
a = int(input("Année : "))
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print("Bissextile")
else:
    print("Normale")
```

---

## Niveau 3 : Structures de BOUCLE (51-75)

### Exercice 51 : Compteur de Lignes Simple
**Énoncé** : Afficher les nombres de 1 à 10 en utilisant une boucle `while`.
**Pseudocode** :
```text
compteur = 1
Tant que compteur <= 10 faire
    Afficher compteur
    compteur = compteur + 1
```
**Code Python** :
```python
i = 1
while i <= 10:
    print(i)
    i += 1
```

### Exercice 52 : Itération sur Plage avec `for`
**Énoncé** : Afficher les nombres de 1 à 10 en utilisant `for` et `range`.
**Code Python** :
```python
for i in range(1, 11):
    print(i)
```

### Exercice 53 : Somme Accumulée de Données
**Énoncé** : Demander 5 nombres à l'utilisateur et afficher la somme totale à la fin.
**Code Python** :
```python
somme = 0
for i in range(5):
    n = float(input("Nombre {} : ".format(i+1)))
    somme += n
print("Total : {}".format(somme))
```

### Exercice 54 : Lecture jusqu'à Sentinelle
**Énoncé** : Saisir des noms de fichiers. Arrêter quand l'utilisateur saisit "FIN".
**Code Python** :
```python
f = ""
while f.upper() != "FIN":
    f = input("Fichier (ou FIN) : ")
    if f.upper() != "FIN":
        print("Fichier {} enregistré".format(f))
```

### Exercice 55 : Table de Multiplication de Transformation
**Énoncé** : Saisir un nombre X et afficher sa table de multiplication de 1 à 10.
**Code Python** :
```python
x = int(input("Table de : "))
for i in range(1, 11):
    print("{} x {} = {}".format(x, i, x*i))
```

### Exercice 56 : Décompte de Sécurité
**Énoncé** : Afficher un compte à rebours de 10 à 0, puis "Lancement !".
**Code Python** :
```python
for i in range(10, -1, -1):
    print(i)
print("Lancement !")
```

### Exercice 57 : Moyenne de Températures (Indéterminée)
**Énoncé** : Saisir des températures. S'arrêter à 999. Afficher la moyenne des valeurs saisies.
**Code Python** :
```python
somme = 0
nb = 0
t = float(input("T (999 pour stop) : "))
while t != 999:
    somme += t
    nb += 1
    t = float(input("T (999 pour stop) : "))
if nb > 0:
    print("Moyenne : {:.2f}".format(somme/nb))
```

### Exercice 58 : Recherche de Valeur avec `break`
**Énoncé** : Parcourir les nombres de 1 à 100. S'arrêter et afficher le premier nombre divisible par 17.
**Code Python** :
```python
for i in range(1, 101):
    if i % 17 == 0:
        print("Trouvé : {}".format(i))
        break
```

### Exercice 59 : Filtrage avec `continue`
**Énoncé** : Afficher les nombres de 1 à 10, sauf le 5.
**Code Python** :
```python
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
```

### Exercice 60 : Multiplication de Puissance de 2
**Énoncé** : Afficher les puissances de 2 (2, 4, 8, 16...) inférieures à 1000.
**Code Python** :
```python
n = 2
while n < 1000:
    print(n)
    n *= 2
```

### Exercice 61 : Parcours de Chaîne de Caractères
**Énoncé** : Saisir une phrase et afficher chaque caractère sur une ligne.
**Code Python** :
```python
txt = input("Phrase : ")
for car in txt:
    print(car)
```

### Exercice 62 : Comptage de Voyelles
**Énoncé** : Saisir un mot et compter combien de voyelles (a, e, i, o, u, y) il contient.
**Code Python** :
```python
mot = input("Mot : ").lower()
v = 0
for c in mot:
    if c in "aeiouy":
        v += 1
print("Voyelles : {}".format(v))
```

### Exercice 63 : Validation de Saisie (Boucle `while`)
**Énoncé** : Demander une note entre 0 et 100. Recommencer tant que la saisie est invalide.
**Code Python** :
```python
note = -1
while note < 0 or note > 100:
    note = int(input("Note (0-100) : "))
    if note < 0 or note > 100:
        print("Erreur !")
print("Note enregistrée : {}".format(note))
```

### Exercice 64 : Génération de Logs Aléatoires
**Énoncé** : Générer 5 nombres aléatoires entre 1 et 100 et les afficher.
**Code Python** :
```python
import random
for i in range(5):
    print(random.randint(1, 100))
```

### Exercice 65 : Somme des N premiers nombres
**Énoncé** : Saisir N et calculer la somme 1 + 2 + 3 + ... + N.
**Code Python** :
```python
n = int(input("N : "))
s = 0
for i in range(1, n + 1):
    s += i
print("Somme : {}".format(s))
```

### Exercice 66 : Factorielle d'un Nombre
**Énoncé** : Saisir N et calculer N! (ex: 5! = 1*2*3*4*5 = 120).
**Code Python** :
```python
n = int(input("N : "))
f = 1
for i in range(1, n + 1):
    f *= i
print("{}! = {}".format(n, f))
```

### Exercice 67 : TEST de Nombre Premier
**Énoncé** : Saisir N et vérifier s'il est premier (divisible uniquement par 1 et lui-même).
**Code Python** :
```python
n = int(input("N : "))
est_premier = True
if n < 2:
    est_premier = False
for i in range(2, n):
    if n % i == 0:
        est_premier = False
        break
print("Premier : {}".format(est_premier))
```

### Exercice 68 : Affichage par Pas (Step)
**Énoncé** : Afficher les nombres pairs entre 2 et 20 inclus avec `range`.
**Code Python** :
```python
for i in range(2, 21, 2):
    print(i)
```

### Exercice 69 : Accumulation avec Seuil
**Énoncé** : Saisir des nombres. S'arrêter dès que la somme dépasse 100.
**Code Python** :
```python
somme = 0
while somme <= 100:
    n = float(input("Nombre : "))
    somme += n
print("Somme finale : {}".format(somme))
```

### Exercice 70 : Répétition de Texte Dynamique
**Énoncé** : Saisir un mot et un nombre N. Afficher le mot N fois.
**Code Python** :
```python
mot = input("Mot : ")
n = int(input("N : "))
for i in range(n):
    print(mot)
```

### Exercice 71 : Inversion de Chaîne (Boucle)
**Énoncé** : Saisir une chaîne et l'afficher à l'envers en utilisant une boucle.
**Code Python** :
```python
txt = input("Texte : ")
inv = ""
for car in txt:
    inv = car + inv
print(inv)
```

### Exercice 72 : Comptage d'Occurrences
**Énoncé** : Saisir une phrase et un caractère. Compter combien de fois le caractère apparaît.
**Code Python** :
```python
p = input("Phrase : ")
c = input("Caractère : ")
nb = 0
for x in p:
    if x == c:
        nb += 1
print("Occurrences : {}".format(nb))
```

### Exercice 73 : Suite de Fibonacci (N premiers termes)
**Énoncé** : Saisir N et afficher les N premiers termes de la suite (0, 1, 1, 2, 3, 5, 8...).
**Code Python** :
```python
n = int(input("N : "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
```

### Exercice 74 : TEST de Palindrome
**Énoncé** : Vérifier si un mot est un palindrome (se lit pareil dans les deux sens).
**Code Python** :
```python
mot = input("Mot : ").lower()
inv = ""
for c in mot:
    inv = c + inv
if mot == inv:
    print("Palindrome")
else:
    print("Non")
```

### Exercice 75 : Recherche de Max dans une série
**Énoncé** : Demander 5 nombres et afficher le plus grand.
**Code Python** :
```python
maxi = float(input("N1 : "))
for i in range(4):
    n = float(input("N{} : ".format(i+2)))
    if n > maxi:
        maxi = n
print("Maximum : {}".format(maxi))
```

---

## Niveau 4 : Logique Avancée et Synthèse (76-100)

### Exercice 76 : Boucles Imbriquées (Grille)
**Énoncé** : Afficher une grille de coordonnées (X, Y) de 1 à 3.
**Pseudocode** :
```text
Pour x de 1 à 3 faire
    Pour y de 1 à 3 faire
        Afficher "(x, y)"
```
**Code Python** :
```python
for x in range(1, 4):
    for y in range(1, 4):
        print("({},{})".format(x, y), end=" ")
    print()
```

### Exercice 77 : Triangle d'Astérisques
**Énoncé** : Demander une hauteur H et afficher un triangle.
**Code Python** :
```python
h = int(input("Hauteur : "))
for i in range(1, h + 1):
    print("*" * i)
```

### Exercice 78 : Rectangle Creux
**Énoncé** : Saisir largeur et hauteur, afficher un rectangle de '#' avec l'intérieur vide.
**Code Python** :
```python
l = int(input("L : "))
h = int(input("H : "))
for i in range(h):
    if i == 0 or i == h - 1:
        print("#" * l)
    else:
        print("#" + " " * (l - 2) + "#")
```

### Exercice 79 : Calculateur de Moyenne par Lot
**Énoncé** : Saisir le nombre de lots. Pour chaque lot, demander 3 valeurs et afficher la moyenne du lot.
**Code Python** :
```python
nb = int(input("Nb lots : "))
for i in range(1, nb + 1):
    print("Lot", i)
    s = 0
    for j in range(3):
        v = float(input("  Valeur {} : ".format(j+1)))
        s += v
    print("  Moyenne : {:.2f}".format(s/3))
```

### Exercice 80 : Menu Persistant
**Énoncé** : Afficher un menu (1. Dire Bonjour, 2. Quitter). Boucler tant que l'utilisateur ne choisit pas 2.
**Code Python** :
```python
choix = 0
while choix != 2:
    print("1. Bonjour\n2. Quitter")
    choix = int(input("Choix : "))
    if choix == 1:
        print("Bonjour !")
print("Au revoir")
```

### Exercice 81 : Deviner le Nombre (Jeu)
**Énoncé** : L'ordinateur choisit un nombre entre 1 et 10. L'utilisateur doit le trouver.
**Code Python** :
```python
import random
secret = random.randint(1, 10)
essai = 0
while essai != secret:
    essai = int(input("Devinez : "))
    if essai < secret:
        print("Plus grand")
    elif essai > secret:
        print("Plus petit")
print("Gagné !")
```

### Exercice 82 : Somme des chiffres d'un nombre
**Énoncé** : Saisir un nombre entier et calculer la somme de ses chiffres (ex: 123 -> 6).
**Code Python** :
```python
n = input("Nombre : ")
s = 0
for c in n:
    s += int(c)
print("Somme : {}".format(s))
```

### Exercice 83 : Filtrage de Données Invalides
**Énoncé** : Saisir 5 nombres. Afficher la somme uniquement des nombres positifs.
**Code Python** :
```python
s = 0
for i in range(5):
    n = float(input("N : "))
    if n < 0:
        continue
    s += n
print("Somme positifs : {}".format(s))
```

### Exercice 84 : Simulation de Pipeline de Nettoyage
**Énoncé** : Saisir une chaîne. Supprimer tous les espaces et mettre en majuscule.
**Code Python** :
```python
txt = input("Data : ")
clean = ""
for car in txt:
    if car != " ":
        clean += car
print(clean.upper())
```

### Exercice 85 : Calcul de Puissance sans opérateur `**`
**Énoncé** : Saisir base et exposant, calculer le résultat avec une boucle `for`.
**Code Python** :
```python
b = int(input("Base : "))
e = int(input("Exp : "))
res = 1
for i in range(e):
    res *= b
print(res)
```

### Exercice 86 : TEST de Validité de Code (Format)
**Énoncé** : Un code doit commencer par 'A' et finir par un chiffre.
**Code Python** :
```python
c = input("Code : ")
if c.startswith("A") and c[-1].isdigit():
    print("Format OK")
else:
    print("Invalide")
```

### Exercice 87 : Extraction de Nombres d'un texte
**Énoncé** : Saisir une chaîne mélangeant lettres et chiffres. Afficher uniquement les chiffres.
**Code Python** :
```python
s = input("Saisie : ")
for car in s:
    if car.isdigit():
        print(car, end="")
print()
```

### Exercice 88 : Statistiques de Logs (Compteur)
**Énoncé** : Saisir 5 types de logs (INFO, WARN, ERROR). Compter le nombre d'ERROR.
**Code Python** :
```python
err = 0
for i in range(5):
    log = input("Type log : ").upper()
    if log == "ERROR":
        err += 1
print("Nombre d'erreurs : {}".format(err))
```

### Exercice 89 : Pyramide de Chiffres
**Énoncé** : Pour H=3, afficher :
1
22
333
**Code Python** :
```python
h = int(input("H : "))
for i in range(1, h + 1):
    print(str(i) * i)
```

### Exercice 90 : Conversion de Liste de Prix
**Énoncé** : Saisir 3 prix en USD. Afficher leur valeur en CAD (taux 1.35) un par un.
**Code Python** :
```python
for i in range(3):
    usd = float(input("Prix USD : "))
    print("CAD : {:.2f}".format(usd * 1.35))
```

### Exercice 91 : Recherche de Doublons Consécutifs
**Énoncé** : Saisir 5 valeurs. Signaler si deux valeurs identiques sont saisies de suite.
**Code Python** :
```python
prec = ""
for i in range(5):
    act = input("Val : ")
    if act == prec:
        print("Doublon détecté !")
    prec = act
```

### Exercice 92 : Calculateur de Facture avec Taxes Variables
**Énoncé** : Saisir prix et province (QC: 15%, ON: 13%). Afficher total.
**Code Python** :
```python
p = float(input("Prix : "))
prov = input("Province : ").upper()
if prov == "QC":
    t = 1.15
elif prov == "ON":
    t = 1.13
else:
    t = 1.05
print("Total : {:.2f}".format(p * t))
```

### Exercice 93 : Simulation de Chargement (Progress Bar)
**Énoncé** : Afficher "[##########]" en ajoutant un '#' par seconde (simulé par boucle).
**Code Python** :
```python
import time
for i in range(1, 11):
    print("\r[" + "#" * i + " " * (10-i) + "]", end="")
    time.sleep(0.1)
print("\nTerminé")
```

### Exercice 94 : Détection de "Null" dans un flux
**Énoncé** : Saisir des données. Si "null" ou "none" (insensible à la casse) apparaît, afficher une alerte.
**Code Python** :
```python
d = input("Data : ").lower()
if d == "null" or d == "none":
    print("ALERTE : Valeur manquante")
```

### Exercice 95 : Multiplication par additions successives
**Énoncé** : Calculer A * B en utilisant uniquement des additions dans une boucle.
**Code Python** :
```python
a = int(input("A : "))
b = int(input("B : "))
res = 0
for i in range(b):
    res += a
print(res)
```

### Exercice 96 : Vérification de Complexité de Mot de Passe
**Énoncé** : Un mot de passe doit avoir >= 8 car ET au moins un chiffre.
**Code Python** :
```python
mdp = input("MDP : ")
a_chiffre = False
for c in mdp:
    if c.isdigit():
        a_chiffre = True
if len(mdp) >= 8 and a_chiffre:
    print("Sécurisé")
else:
    print("Faible")
```

### Exercice 97 : Calcul d'intérêt composé (Data Finance)
**Énoncé** : Saisir capital, taux (%) et années. Afficher le capital final.
**Code Python** :
```python
c = float(input("Capital : "))
t = float(input("Taux % : ")) / 100
a = int(input("Années : "))
for i in range(a):
    c = c * (1 + t)
print("Final : {:.2f}".format(c))
```

### Exercice 98 : Remplacement de Caractères
**Énoncé** : Saisir une chaîne. Remplacer tous les 'e' par '3'.
**Code Python** :
```python
s = input("Texte : ")
res = ""
for c in s:
    if c.lower() == 'e':
        res += '3'
    else:
        res += c
print(res)
```

### Exercice 99 : TEST de Portée de Variables
**Énoncé** : Créer une boucle qui modifie une variable globale et l'afficher après la boucle.
**Code Python** :
```python
total = 0
for i in range(1, 6):
    total += i
print("Somme globale (1-5) : {}".format(total))
```

### Exercice 100 : Synthèse Finale (ETL Simple)
**Énoncé** : Saisir 3 noms de produits et leurs prix. Si prix > 100, appliquer 10% de remise. Afficher un mini-rapport.
**Code Python** :
```python
rapport = ""
for i in range(3):
    nom = input("Produit {} : ".format(i+1))
    prix = float(input("Prix : "))
    if prix > 100:
        prix *= 0.9
    rapport += "{}: {:.2f}$ | ".format(nom, prix)
print("--- RAPPORT ---")
print(rapport)
```
