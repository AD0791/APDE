---
title: "Manuel de 30 Exercices Corriges - Python Fondamental"
subtitle: "Preparation Examen Pre Data Specialist - C45 Hiver"
author: "APDE - Alexandro Disla"
date: "2026"
lang: fr
documentclass: article
geometry: "margin=2.2cm"
fontsize: 11pt
colorlinks: true
---

# Manuel de 30 Exercices Corriges

> **Portee du cours :** types (`int`, `float`, `str`, `bool`), operateurs arithmetiques/logiques/comparaison,
> `if/elif/else`, `while`, `for`, `break`, `continue`, `random.randint`, `input/print`, `format`,
> methodes de chaine (`.upper .lower .strip .replace .startswith .endswith .isdigit`), operateur `in`.
>
> **Interdit :** listes `[]`, fonctions `def`, `try/except`, `import math`.

---

## GROUPE A - Structures Conditionnelles Avancees (1-10)

---

### Exercice 1 - Classification IMC selon l'OMS avec rapport nutritionnel

**Enonce**

Saisir le poids en kg et la taille en cm. Calculer l'IMC (`poids / taille_m2`). Classer selon les 5
categories OMS et associer un conseil nutritionnel personnalise. Afficher un rapport formate aligne.

**Pseudocode**

```text
Saisir poids_kg (float), taille_cm (float)
taille_m <- taille_cm / 100
imc <- poids_kg / (taille_m ** 2)

Si imc < 18.5       : categorie = "Sous-poids",      conseil = "Augmentez votre apport calorique"
Sinon si imc < 25.0 : categorie = "Normal",           conseil = "Maintenez vos habitudes actuelles"
Sinon si imc < 30.0 : categorie = "Surpoids",         conseil = "Reduisez les glucides raffines"
Sinon si imc < 35.0 : categorie = "Obesite grade I",  conseil = "Consultez un nutritionniste"
Sinon               : categorie = "Obesite II/III",   conseil = "Suivi medical urgent"
Afficher IMC (:.2f), categorie, conseil
```

**Code Python**

```python
poids_kg  = float(input("Poids (kg)  : "))
taille_cm = float(input("Taille (cm) : "))

taille_m = taille_cm / 100
imc      = poids_kg / (taille_m ** 2)

if imc < 18.5:
    categorie = "Sous-poids"
    conseil   = "Augmentez votre apport calorique"
elif imc < 25.0:
    categorie = "Normal"
    conseil   = "Maintenez vos habitudes actuelles"
elif imc < 30.0:
    categorie = "Surpoids"
    conseil   = "Reduisez les glucides raffines"
elif imc < 35.0:
    categorie = "Obesite grade I"
    conseil   = "Consultez un nutritionniste"
else:
    categorie = "Obesite grade II/III"
    conseil   = "Suivi medical urgent recommande"

print("=" * 50)
print("  IMC       : {:.2f} kg/m2".format(imc))
print("  Categorie : {}".format(categorie))
print("  Conseil   : {}".format(conseil))
print("=" * 50)
```

**Pourquoi cette solution ?**

L'IMC exige la taille en metres - la conversion `/100` est obligatoire avant le calcul, pas pendant.
Les `elif` en cascade garantissent l'exclusivite mutuelle : des que la premiere condition vraie est
trouvee, Python sort de la structure entiere. Des `if` separes s'evalueraient tous, produisant
potentiellement plusieurs categories pour une meme valeur.

**A retenir**

- `** 2` est l'exponentiation - ne pas confondre avec `* 2` (multiplication)
- `elif` : une seule branche s'execute parmi N alternatives
- Convertir les unites **avant** le calcul, jamais a l'interieur de la formule
- Les seuils OMS sont des inegalites strictes (`< 18.5`, pas `<= 18.5`)
- Le `else` final capture implicitement `imc >= 35.0`

---

### Exercice 2 - Impot progressif a 4 tranches (calcul tranche par tranche)

**Enonce**

L'impot haitien simplifie : les tranches s'appliquent sur chaque portion de revenu separement
(systeme marginal). Saisir le revenu annuel brut. Afficher la decomposition tranche par tranche,
l'impot total, le taux effectif et le revenu net.

| Tranche | De (HTG)  | A (HTG)   | Taux |
|---------|-----------|-----------|------|
| 1       | 0         | 60 000    | 0 %  |
| 2       | 60 001    | 150 000   | 10 % |
| 3       | 150 001   | 250 000   | 20 % |
| 4       | > 250 000 | ---       | 30 % |

**Pseudocode**

```text
Saisir revenu
impot <- 0
Pour chaque tranche :
    montant_tranche <- max(0, min(revenu, borne_haute) - borne_basse)
    impot += montant_tranche x taux
taux_effectif <- impot / revenu x 100
revenu_net    <- revenu - impot
```

**Code Python**

```python
revenu = float(input("Revenu annuel brut (HTG) : "))
impot  = 0.0

# Tranche 1 : 0-60 000 @ 0%
t1  = min(revenu, 60000)
it1 = t1 * 0.00

# Tranche 2 : 60 001-150 000 @ 10%
t2  = max(0.0, min(revenu, 150000) - 60000)
it2 = t2 * 0.10
impot += it2

# Tranche 3 : 150 001-250 000 @ 20%
t3  = max(0.0, min(revenu, 250000) - 150000)
it3 = t3 * 0.20
impot += it3

# Tranche 4 : > 250 000 @ 30%
t4  = max(0.0, revenu - 250000)
it4 = t4 * 0.30
impot += it4

taux_effectif = (impot / revenu * 100) if revenu > 0 else 0
revenu_net    = revenu - impot

print("=" * 52)
print("  CALCUL D'IMPOT PROGRESSIF")
print("=" * 52)
print("  T1 (0-60K    @ 0%)  : {:.2f} HTG".format(it1))
print("  T2 (60-150K  @ 10%) : {:.2f} HTG".format(it2))
print("  T3 (150-250K @ 20%) : {:.2f} HTG".format(it3))
print("  T4 (>250K    @ 30%) : {:.2f} HTG".format(it4))
print("-" * 52)
print("  Impot total   : {:.2f} HTG".format(impot))
print("  Taux effectif : {:.2f} %".format(taux_effectif))
print("  Revenu net    : {:.2f} HTG".format(revenu_net))
print("=" * 52)
```

**Pourquoi cette solution ?**

L'erreur classique : appliquer le taux marginal a tout le revenu (`revenu x 30%`). La methode correcte
extrait la portion imposable par tranche avec `min(revenu, borne_haute) - borne_basse`. `max(0, ...)`
protege contre un resultat negatif si le revenu n'atteint pas cette tranche. On utilise 4 `if`
independants (non `elif`) car chaque tranche contribue independamment.

**A retenir**

- `min(revenu, borne)` extrait la portion <= borne ; soustraire la borne basse isole la tranche
- `max(0, valeur)` : garde-fou contre les negatifs - pattern universel pour les tranches
- Taux effectif < taux marginal (toujours, en fiscalite progressive)
- 4 `if` independants ici, pas `elif` - chaque tranche contribue meme si les autres aussi
- Verification rapide : revenu 200 000 HTG -> impot = 0 + 9 000 + 10 000 + 0 = 19 000 HTG

---

### Exercice 3 - Validation de date complete avec annees bissextiles

**Enonce**

Saisir jour, mois et annee. Valider que la date est reelle : (1) mois entre 1 et 12, (2) jour selon
les regles de chaque mois (avec gestion de fevrier), (3) annee bissextile si divisible par 4 ET
(non divisible par 100 OU divisible par 400). Afficher "Date valide : JJ/MM/AAAA" ou un message
d'erreur precis.

**Pseudocode**

```text
Saisir jour, mois, annee (int)

Si mois < 1 ou mois > 12 :
    Afficher "ERREUR : Mois invalide"
Sinon :
    Si mois == 2 :
        Si (annee%4==0 et annee%100!=0) ou annee%400==0 : jours_max <- 29
        Sinon : jours_max <- 28
    Sinon si mois == 4 ou mois == 6 ou mois == 9 ou mois == 11 : jours_max <- 30
    Sinon : jours_max <- 31

    Si jour < 1 ou jour > jours_max : Afficher "ERREUR"
    Sinon : Afficher "Date valide"
```

**Code Python**

```python
jour  = int(input("Jour  : "))
mois  = int(input("Mois  : "))
annee = int(input("Annee : "))

if mois < 1 or mois > 12:
    print("ERREUR : Mois {} invalide (attendu 1-12).".format(mois))
else:
    if mois == 2:
        bissextile = (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)
        jours_max  = 29 if bissextile else 28
    elif mois == 4 or mois == 6 or mois == 9 or mois == 11:
        jours_max = 30
    else:
        jours_max = 31

    if jour < 1 or jour > jours_max:
        print("ERREUR : Le {}/{} a {} jours max (recu : {}).".format(
            mois, annee, jours_max, jour))
    else:
        print("Date valide : {:02d}/{:02d}/{:04d}".format(jour, mois, annee))
```

**Pourquoi cette solution ?**

La validation est imbriquee : verifier le mois d'abord, car `jours_max` depend d'un mois valide.
La regle bissextile est une conjonction-disjonction : `(% 4 == 0 AND % 100 != 0) OR % 400 == 0`.
On l'evalue en un booleen `bissextile`, puis l'operateur ternaire selectionne 29 ou 28.

**A retenir**

- Regle bissextile : `(an%4==0 and an%100!=0) or (an%400==0)` - memoriser cette formule
- 2000 est bissextile (divise par 400), 1900 ne l'est pas (divise par 100 mais pas par 400)
- Mois a 30 jours : **4, 6, 9, 11** (avril, juin, septembre, novembre)
- `{:02d}` formate un entier sur 2 chiffres avec zero de remplissage (`01`, `09`)
- Toujours valider les pre-conditions avant les calculs qui en dependent

---

### Exercice 4 - Score de securite d'un mot de passe

**Enonce**

Saisir un mot de passe. Calculer un score de securite sur 5 : +1 si longueur >= 8, +1 si longueur
>= 12, +1 s'il contient au moins un chiffre, +1 s'il contient au moins une majuscule, +1 s'il ne
contient pas d'espace. Parcourir les caracteres avec `for i in range(len(mdp))`. Afficher le score
et le niveau.

**Pseudocode**

```text
Saisir mdp ; score <- 0
Si len >= 8 : score += 1
Si len >= 12 : score += 1

a_chiffre <- Faux ; a_majuscule <- Faux
Pour i de 0 a len(mdp)-1 :
    c <- mdp[i]
    Si c.isdigit()    : a_chiffre   <- Vrai
    Si c != c.lower() : a_majuscule <- Vrai

Si a_chiffre : score += 1
Si a_majuscule : score += 1
Si " " not in mdp : score += 1
```

**Code Python**

```python
mdp   = input("Mot de passe : ")
score = 0

if len(mdp) >= 8:
    score += 1
if len(mdp) >= 12:
    score += 1

a_chiffre   = False
a_majuscule = False

for i in range(len(mdp)):
    c = mdp[i]
    if c.isdigit():
        a_chiffre = True
    if c != c.lower():
        a_majuscule = True

if a_chiffre:
    score += 1
if a_majuscule:
    score += 1
if " " not in mdp:
    score += 1

if score <= 1:
    niveau = "Tres faible  - Changez immediatement !"
elif score == 2:
    niveau = "Faible       - Ameliorez votre mot de passe"
elif score == 3:
    niveau = "Moyen        - Acceptable mais perfectible"
elif score == 4:
    niveau = "Fort         - Bonne protection"
else:
    niveau = "Tres fort    - Excellente securite"

print("Score  : {}/5".format(score))
print("Niveau : {}".format(niveau))
```

**Pourquoi cette solution ?**

Sans `.isupper()` (hors portee du cours), on detecte une majuscule par `c != c.lower()` : une lettre
majuscule est differente de sa version minuscule. Les **drapeaux booleens** s'initialisent a `False`
et passent a `True` des la premiere occurrence - la boucle continue mais la detection est deja faite.

**A retenir**

- **Drapeau booleen** : initialiser a `False` avant la boucle, mettre a `True` a l'interieur
- `c != c.lower()` detecte une majuscule sans `.isupper()` (hors portee du cours)
- `if a_chiffre:` suffit - ne pas ecrire `if a_chiffre == True:`
- `" " not in mdp` : operateur `not in` sur une chaine
- `for i in range(len(s)):` + `c = s[i]` est le seul moyen de parcourir une chaine sans liste

---

### Exercice 5 - Fiche de paie avec 3 paliers d'heures supplementaires

**Enonce**

Calculer le salaire brut d'un employe. Heures au-dela de 40h majorees par palier : 41-48h a x1.5,
49-60h a x2.0, au-dela de 60h a x2.5. Afficher le detail de chaque segment et le total.

**Pseudocode**

```text
Saisir heures, taux
h_normal <- min(heures, 40)
h_sup1   <- max(0, min(heures, 48) - 40)
h_sup2   <- max(0, min(heures, 60) - 48)
h_sup3   <- max(0, heures - 60)
salaire  <- h_normal*taux + h_sup1*taux*1.5 + h_sup2*taux*2.0 + h_sup3*taux*2.5
```

**Code Python**

```python
heures = float(input("Heures travaillees : "))
taux   = float(input("Taux horaire (HTG) : "))

h_normal = min(heures, 40.0)
h_sup1   = max(0.0, min(heures, 48.0) - 40.0)
h_sup2   = max(0.0, min(heures, 60.0) - 48.0)
h_sup3   = max(0.0, heures - 60.0)

s_normal = h_normal * taux
s_sup1   = h_sup1   * taux * 1.5
s_sup2   = h_sup2   * taux * 2.0
s_sup3   = h_sup3   * taux * 2.5
total    = s_normal + s_sup1 + s_sup2 + s_sup3

print("=" * 55)
print("  FICHE DE PAIE")
print("=" * 55)
print("  Normales  {:5.1f}h x {:.2f}        : {:>9.2f}".format(
    h_normal, taux, s_normal))
if h_sup1 > 0:
    print("  HS x1.5  {:5.1f}h x {:.2f} x 1.5 : {:>9.2f}".format(
        h_sup1, taux, s_sup1))
if h_sup2 > 0:
    print("  HS x2.0  {:5.1f}h x {:.2f} x 2.0 : {:>9.2f}".format(
        h_sup2, taux, s_sup2))
if h_sup3 > 0:
    print("  HS x2.5  {:5.1f}h x {:.2f} x 2.5 : {:>9.2f}".format(
        h_sup3, taux, s_sup3))
print("-" * 55)
print("  SALAIRE BRUT TOTAL             : {:>9.2f} HTG".format(total))
print("=" * 55)
```

**Pourquoi cette solution ?**

Le pattern `max(0, min(heures, borne_haute) - borne_basse)` extrait proprement la portion de chaque
palier. C'est le **meme pattern** qu'a l'exercice 2 sur l'impot - reconnaitre ce pattern permet de
resoudre rapidement toute structure a paliers.

**A retenir**

- `min(h, borne_haute) - borne_basse` puis `max(0, ...)` : le tandem pour les intervalles
- Ce pattern est identique a l'impot progressif (exercice 2) - meme structure, probleme different
- `{:>9.2f}` : alignement a droite sur 9 caracteres, 2 decimales
- Les `if h_sup1 > 0:` evitent d'afficher des lignes a 0.00

---

### Exercice 6 - Classification complete d'un triangle

**Enonce**

Saisir trois cotes (a, b, c). Verifier la validite (inegalite triangulaire). Si valide : (1) nature
selon les cotes (equilateral / isocele / scalene) et (2) nature selon les angles en identifiant le
plus grand cote `g` : `g2 == p12+p22` -> rectangle, `g2 <` -> acutangle, `g2 >` -> obtus.

**Code Python**

```python
a = float(input("Cote a : "))
b = float(input("Cote b : "))
c = float(input("Cote c : "))

if a + b <= c or a + c <= b or b + c <= a:
    print("ERREUR : Ces cotes ne forment pas un triangle valide.")
else:
    if a == b and b == c:
        nature_cotes = "Equilateral"
    elif a == b or b == c or a == c:
        nature_cotes = "Isocele"
    else:
        nature_cotes = "Scalene"

    if a >= b and a >= c:
        g, p1, p2 = a, b, c
    elif b >= a and b >= c:
        g, p1, p2 = b, a, c
    else:
        g, p1, p2 = c, a, b

    carre_g = g  ** 2
    somme_p = p1 ** 2 + p2 ** 2

    if carre_g == somme_p:
        nature_angles = "Rectangle (angle droit)"
    elif carre_g < somme_p:
        nature_angles = "Acutangle (tous angles < 90 deg)"
    else:
        nature_angles = "Obtusangle (un angle > 90 deg)"

    print("Triangle {} - {}".format(nature_cotes, nature_angles))
    print("Grand cote : {:.2f}  |  g^2 {} p1^2+p2^2".format(
        g, "==" if carre_g == somme_p else ("<" if carre_g < somme_p else ">")))
```

**Pourquoi cette solution ?**

La loi des cosinus generalisee reduit le classement angulaire a une comparaison de carres. En
comparant `g2` a `p12+p22` (g = plus grand cote), on evite tout calcul trigonometrique. L'ordre
est obligatoire : inegalite triangulaire d'abord, sinon le classement serait applique a des
triangles impossibles.

**A retenir**

- Inegalite triangulaire : les **trois** combinaisons doivent etre verifiees simultanement
- `a == b and b == c` (pas `a == b == c` - eviter l'ambiguite)
- `g2 vs p12+p22` : rectangle si egaux, acutangle si `g2 <`, obtus si `g2 >`
- Comparer des flottants avec `==` est risque - ici on suppose des saisies entieres ou simples

---

### Exercice 7 - Remise commerciale a paliers avec bonus fidelite et plafond

**Enonce**

Remise en deux composantes : (A) remise de base selon montant (< 500->0%, 500-1999->5%,
2000-4999->10%, >= 5000->15%) et (B) bonus fidelite selon type client (Standard->+0%, Premium->+3%,
VIP->+5%). Remise combinee plafonnee a 20%. Afficher montant brut, taux applique, economie, montant net.

**Code Python**

```python
montant     = float(input("Montant HT (HTG) : "))
print("Type client : 1=Standard  2=Premium  3=VIP")
type_client = int(input("Votre choix : "))

if montant < 500:
    remise_base = 0
elif montant < 2000:
    remise_base = 5
elif montant < 5000:
    remise_base = 10
else:
    remise_base = 15

if type_client == 2:
    bonus   = 3
    libelle = "Premium"
elif type_client == 3:
    bonus   = 5
    libelle = "VIP"
else:
    bonus   = 0
    libelle = "Standard"

remise_totale = min(remise_base + bonus, 20)
economie      = montant * remise_totale / 100
montant_net   = montant - economie

print("=" * 44)
print("  Client         : {}".format(libelle))
print("  Montant brut   : {:>10.2f} HTG".format(montant))
print("  Remise base    : {:>10}%".format(remise_base))
print("  Bonus fidelite : {:>10}%".format(bonus))
print("  Remise totale  : {:>10}% (plafond 20%)".format(remise_totale))
print("  Economie       : {:>10.2f} HTG".format(economie))
print("  Montant net    : {:>10.2f} HTG".format(montant_net))
print("=" * 44)
```

**Pourquoi cette solution ?**

Les deux composantes (remise de base, bonus fidelite) sont orthogonales - calculees separement,
puis combinees. `min(remise_base + bonus, 20)` applique le plafond en une seule operation. Appliquer
le plafond avant la combinaison serait incorrect car le bonus s'appliquerait sur une remise deja
tronquee.

**A retenir**

- `min(valeur, plafond)` = pattern standard pour tout plafonnement
- Calculer les deux composantes separement avant de les combiner
- `{:>10.2f}` : `>` = alignement a droite, `10` = largeur totale, `.2f` = 2 decimales
- Toujours afficher le plafond dans le rapport pour que l'utilisateur comprenne la regle

---

### Exercice 8 - Quadrant cartesien, distance euclidienne et zone

**Enonce**

Saisir les coordonnees (x, y). Determiner : Origine, Axe X, Axe Y, ou l'un des 4 quadrants.
Calculer la distance a l'origine (`(x2+y2)**0.5`). Classifier : distance < 2 -> "Proche",
2-10 -> "Intermediaire", > 10 -> "Lointain".

**Code Python**

```python
x = float(input("Coordonnee x : "))
y = float(input("Coordonnee y : "))

if x == 0 and y == 0:
    position = "Origine (0, 0)"
elif x == 0:
    position = "Axe Y (x = 0)"
elif y == 0:
    position = "Axe X (y = 0)"
elif x > 0 and y > 0:
    position = "Quadrant I   (x > 0, y > 0)"
elif x < 0 and y > 0:
    position = "Quadrant II  (x < 0, y > 0)"
elif x < 0 and y < 0:
    position = "Quadrant III (x < 0, y < 0)"
else:
    position = "Quadrant IV  (x > 0, y < 0)"

distance = (x ** 2 + y ** 2) ** 0.5

if distance < 2:
    zone = "Proche de l'origine"
elif distance <= 10:
    zone = "Zone intermediaire"
else:
    zone = "Point lointain"

print("Point    : ({:.3f}, {:.3f})".format(x, y))
print("Position : {}".format(position))
print("Distance : {:.4f} unites".format(distance))
print("Zone     : {}".format(zone))
```

**Pourquoi cette solution ?**

L'ordre des conditions est critique : on verifie l'Origine (cas le plus restrictif) avant les axes,
et les axes avant les quadrants. Un point sur l'axe X satisfait aussi les conditions du quadrant I
ou IV - si on verificait les quadrants en premier, le point serait mal classe.

**A retenir**

- Toujours verifier les cas les plus specifiques (Origine) **avant** les cas generaux (Quadrants)
- Racine carree : `n ** 0.5` (valide en Python, pas besoin de `math.sqrt`)
- Distance euclidienne : `(x**2 + y**2) ** 0.5` - memoriser cette formule
- L'ordre des `elif` definit la priorite de classification

---

### Exercice 9 - Tarification cloud : vCPU, RAM, region, abonnement

**Enonce**

Calculer le cout d'une instance cloud. Parametres : vCPU, RAM en Go, region (1=Amerique, 2=Europe,
3=Asie-Pacifique), abonnement (1=a la demande, 2=reserve 1 an -20%, 3=reserve 3 ans -40%). Tarifs :
vCPU <= 4 -> 0.06$/vCPU, 5-16 -> 0.05$/vCPU, > 16 -> 0.04$/vCPU ; RAM -> 0.012$/Go. Multiplicateurs :
AM x1.0, EU x1.15, AP x0.95.

**Code Python**

```python
vcpu       = int(input("Nombre de vCPU : "))
ram_go     = int(input("RAM en Go      : "))
region     = int(input("Region (1=AM, 2=EU, 3=AP) : "))
abonnement = int(input("Abonnement (1=demande, 2=1an-20%, 3=3ans-40%) : "))

if vcpu <= 4:
    tarif_vcpu = 0.06
elif vcpu <= 16:
    tarif_vcpu = 0.05
else:
    tarif_vcpu = 0.04

if region == 2:
    multi_region = 1.15
    nom_region   = "Europe"
elif region == 3:
    multi_region = 0.95
    nom_region   = "Asie-Pacifique"
else:
    multi_region = 1.0
    nom_region   = "Amerique"

if abonnement == 2:
    remise_abo = 0.20
    nom_abo    = "Reserve 1 an (-20%)"
elif abonnement == 3:
    remise_abo = 0.40
    nom_abo    = "Reserve 3 ans (-40%)"
else:
    remise_abo = 0.0
    nom_abo    = "A la demande"

cout_horaire_base  = (vcpu * tarif_vcpu + ram_go * 0.012) * multi_region
cout_horaire_final = cout_horaire_base * (1 - remise_abo)
cout_mensuel       = cout_horaire_final * 730

print("\n  DEVIS CLOUD - {}".format(nom_region))
print("  Config       : {} vCPU @ {:.3f}$/h, {} Go RAM".format(vcpu, tarif_vcpu, ram_go))
print("  Abonnement   : {}".format(nom_abo))
print("  Cout horaire : {:.4f} USD".format(cout_horaire_final))
print("  Cout mensuel : {:.2f} USD (730h)".format(cout_mensuel))
```

**Pourquoi cette solution ?**

Contrairement a l'impot (progressif par tranche), la tarification vCPU est "tout ou rien" : 8 vCPUs
a 0.05$/vCPU coutent 0.40$/h - le tarif inferieur s'applique a **toutes** les unites, pas seulement
a la portion dans la tranche. Les trois facteurs se combinent en cascade multiplicative.

**A retenir**

- **Palier "tout ou rien"** vs **progressif** : ici le taux change pour toutes les unites
- Difference avec l'impot : pas de calcul de tranche, juste selection du taux selon le palier
- 730h = reference standard pour un mois cloud (365 x 24 / 12)
- `.lower()` sur une saisie texte elimine les erreurs de casse ("O" vs "o")

---

### Exercice 10 - Systeme de notation GPA sur 5 matieres

**Enonce**

Saisir 5 notes sur 100 avec une boucle `for`. Calculer la moyenne. Convertir en lettre et GPA :
>= 90->A/4.0, >= 80->B/3.0, >= 70->C/2.0, >= 60->D/1.0, < 60->F/0.0. Determiner la mention selon
le GPA : 4.0->Summa Cum Laude, >= 3.7->Magna Cum Laude, >= 3.3->Cum Laude, >= 3.0->Mention Bien,
>= 2.0->Passage, < 2.0->Echec. Afficher le bulletin.

**Code Python**

```python
somme = 0.0
for i in range(1, 6):
    note = float(input("Note {}/5 (sur 100) : ".format(i)))
    somme += note
moyenne = somme / 5

if moyenne >= 90:
    lettre = "A"
    gpa    = 4.0
elif moyenne >= 80:
    lettre = "B"
    gpa    = 3.0
elif moyenne >= 70:
    lettre = "C"
    gpa    = 2.0
elif moyenne >= 60:
    lettre = "D"
    gpa    = 1.0
else:
    lettre = "F"
    gpa    = 0.0

if gpa == 4.0:
    mention = "Summa Cum Laude"
elif gpa >= 3.7:
    mention = "Magna Cum Laude"
elif gpa >= 3.3:
    mention = "Cum Laude"
elif gpa >= 3.0:
    mention = "Mention Bien"
elif gpa >= 2.0:
    mention = "Passage"
else:
    mention = "Echec - Rattrapage requis"

print("\n  BULLETIN DE NOTES")
print("  Moyenne  : {:.2f} / 100".format(moyenne))
print("  Lettre   : {}".format(lettre))
print("  GPA      : {:.1f} / 4.0".format(gpa))
print("  Mention  : {}".format(mention))
```

**Pourquoi cette solution ?**

Deux classificateurs en sequence (non imbriques) : note -> lettre/GPA, puis GPA -> mention.
On ne peut pas les fusionner car les seuils de mention ne correspondent pas directement aux tranches
de notes. L'accumulation `somme += note` dans `for i in range(1, 6)` est le pattern fondamental.

**A retenir**

- Accumulateur : `somme = 0` **avant** la boucle ; `moyenne = somme / n` **apres**
- `range(1, 6)` -> [1, 2, 3, 4, 5] - utiliser `i` dans le prompt pour numeroter les saisies
- Deux `if/elif` en sequence = deux logiques independantes
- `gpa == 4.0` est sur car 4.0 est une valeur exacte en IEEE 754

---

## GROUPE B - Algorithmes avec Boucles (11-20)

---

### Exercice 11 - Saisie securisee avec verrouillage (3 tentatives)

**Enonce**

Demander un entier entre 1 et 100. Maximum 3 tentatives. A chaque erreur : afficher le numero de
tentative et les essais restants. Apres 3 echecs : "Compte verrouille". En cas de succes : afficher
le carre, la racine carree et la parite.

**Pseudocode**

```text
MAX <- 3 ; tentative <- 0 ; valide <- Faux

Tant que tentative < MAX et non valide :
    tentative += 1
    Saisir n
    Si 1 <= n <= 100 : valide <- Vrai
    Sinon : Afficher erreur + essais restants

Si valide : Afficher carre, racine, parite
Sinon : "Compte verrouille"
```

**Code Python**

```python
MAX_ESSAIS = 3
tentative  = 0
valide     = False

while tentative < MAX_ESSAIS and not valide:
    tentative += 1
    n = int(input("Tentative {}/{} - Entrez un entier [1-100] : ".format(
        tentative, MAX_ESSAIS)))

    if 1 <= n <= 100:
        valide = True
    else:
        restants = MAX_ESSAIS - tentative
        if restants > 0:
            print("  ERREUR : {} hors plage. {} essai(s) restant(s).".format(n, restants))
        else:
            print("  ERREUR : {} hors plage.".format(n))

if valide:
    print("\n  Valeur        : {}".format(n))
    print("  Carre         : {}".format(n ** 2))
    print("  Racine carree : {:.4f}".format(n ** 0.5))
    print("  Parite        : {}".format("Pair" if n % 2 == 0 else "Impair"))
else:
    print("\nCOMPTE VERROUILLE - Trop de tentatives invalides.")
```

**Pourquoi cette solution ?**

La condition `while tentative < MAX_ESSAIS and not valide` combine deux gardes : la limite d'essais
ET le signal de succes. Sans `not valide`, la boucle continuerait meme apres une saisie correcte.
Le drapeau `valide` permet ensuite de distinguer "succes" de "verrouillage".

**A retenir**

- Pattern "boucle + drapeau" : `while compteur < MAX and not success:` - forme canonique
- `1 <= n <= 100` : chainage d'inegalites Python (equivaut a `n >= 1 and n <= 100`)
- `MAX_ESSAIS = 3` en majuscules : convention Python pour les constantes
- Apres la boucle, `valide` distingue succes vs epuisement des essais

---

### Exercice 12 - Multi-statistiques en une seule passe (formule de Huygens)

**Enonce**

Saisir N valeurs reelles (N >= 2). En **une seule passe** (`while`), calculer : somme, moyenne,
minimum, maximum, variance et ecart-type. Afficher l'etendue et le coefficient de variation.
La variance : `Var = E[X2] - (E[X])2` (formule de Huygens).

**Pseudocode**

```text
somme <- 0 ; somme_carres <- 0 ; minimum <- None ; maximum <- None ; i <- 0

Tant que i < n :
    i += 1 ; Saisir val
    somme += val ; somme_carres += val**2
    Si minimum est None ou val < minimum : minimum <- val
    Si maximum est None ou val > maximum : maximum <- val

variance <- somme_carres/n - (somme/n)**2
```

**Code Python**

```python
n = int(input("Nombre de valeurs (min 2) : "))
if n < 2:
    n = 2

somme        = 0.0
somme_carres = 0.0
minimum      = None
maximum      = None
i            = 0

while i < n:
    i += 1
    val = float(input("Valeur {} : ".format(i)))
    somme        += val
    somme_carres += val ** 2
    if minimum is None or val < minimum:
        minimum = val
    if maximum is None or val > maximum:
        maximum = val

moyenne    = somme / n
variance   = somme_carres / n - moyenne ** 2
ecart_type = variance ** 0.5
etendue    = maximum - minimum
cv         = (ecart_type / moyenne * 100) if moyenne != 0 else 0.0

print("\n  STATISTIQUES DESCRIPTIVES ({} valeurs)".format(n))
print("  Somme            : {:.4f}".format(somme))
print("  Moyenne          : {:.4f}".format(moyenne))
print("  Minimum          : {:.4f}".format(minimum))
print("  Maximum          : {:.4f}".format(maximum))
print("  Etendue          : {:.4f}".format(etendue))
print("  Variance         : {:.4f}".format(variance))
print("  Ecart-type       : {:.4f}".format(ecart_type))
print("  Coeff. variation : {:.2f} %".format(cv))
```

**Pourquoi cette solution ?**

La formule `Var = E[X2] - (E[X])2` (identite de Huygens) permet de calculer la variance **sans
stocker les valeurs** - on accumule `somme` et `somme_carres` simultanement. Sans cette formule,
il faudrait stocker toutes les valeurs pour un second passage, ce qui necessite une liste.

**A retenir**

- **Formule de Huygens** : `Var = (Somme xi2)/n - (Somme xi / n)2` - cle des stats en une passe
- `minimum = None` puis `if minimum is None or val < minimum` : initialisation universelle
- L'ecart-type est toujours la racine de la variance : `variance ** 0.5`
- Proteger la division par zero : `if moyenne != 0 else 0.0`

---

### Exercice 13 - Suite de Fibonacci jusqu'a un seuil

**Enonce**

Saisir un seuil S. Afficher tous les termes de Fibonacci (F0=0, F1=1, Fn=Fn-1+Fn-2) inferieurs ou
egaux a S. Compter les termes. Determiner si S est lui-meme un nombre de Fibonacci. Afficher le ratio
entre termes consecutifs (converge vers phi = 1.618).

**Code Python**

```python
seuil    = int(input("Seuil S : "))
a        = 0
b        = 1
compteur = 0
est_fibo = False
prev     = 0

print("Termes de Fibonacci <= {} :".format(seuil))

while a <= seuil:
    if compteur > 0 and prev > 0:
        ratio = a / prev
        print("  F[{:2d}] = {:>12}   (ratio: {:.6f})".format(compteur, a, ratio))
    else:
        print("  F[{:2d}] = {:>12}".format(compteur, a))

    if a == seuil:
        est_fibo = True

    prev    = a
    suivant = a + b
    a       = b
    b       = suivant
    compteur += 1

print("\nNombre de termes : {}".format(compteur))
print("{} {} un nombre de Fibonacci.".format(
    seuil, "EST" if est_fibo else "N'EST PAS"))
print("Remarque : le ratio converge vers phi = 1.618033...")
```

**Pourquoi cette solution ?**

La difficulte de Fibonacci sans tableau : maintenir deux variables glissantes `a` et `b`. L'ordre
des mises a jour est critique : calculer `suivant = a + b` **avant** de modifier `a`. Si on ecrivait
`a = b; b = a + b`, la deuxieme ligne utiliserait le nouveau `a` - resultat faux.

**A retenir**

- Fibonacci sans liste : variables glissantes `a` (courant), `b` (suivant)
- **Ne jamais oublier** la temporaire : `suivant = a + b`, puis `a = b`, puis `b = suivant`
- Inverser l'ordre (`a = b; b = a + b`) est une erreur classique - le resultat est faux
- Detecter la presence de S : tester `a == seuil` **avant** la mise a jour

---

### Exercice 14 - PGCD par l'algorithme d'Euclide avec trace

**Enonce**

Saisir deux entiers positifs. Calculer leur PGCD par l'algorithme d'Euclide en affichant chaque
etape sous la forme `a = b x q + r`. En deduire le PPCM. Verifier que `PGCD x PPCM = a x b`.
Identifier si les deux nombres sont premiers entre eux (PGCD = 1).

**Code Python**

```python
a = int(input("Premier entier  a : "))
b = int(input("Deuxieme entier b : "))

orig_a = a
orig_b = b

print("\nAlgorithme d'Euclide :")
print("{:<8} {:<8} {:<8} {:<8}".format("a", "b", "q=a//b", "r=a%b"))
print("-" * 36)

while b != 0:
    q = a // b
    r = a  % b
    print("{:<8} {:<8} {:<8} {:<8}  ({} = {}x{} + {})".format(
        a, b, q, r, a, b, q, r))
    a = b
    b = r

pgcd = a
ppcm = orig_a * orig_b // pgcd

print("-" * 36)
print("PGCD({}, {}) = {}".format(orig_a, orig_b, pgcd))
print("PPCM({}, {}) = {}".format(orig_a, orig_b, ppcm))
print("Verif : {} x {} = {} == {} x {} = {}".format(
    pgcd, ppcm, pgcd * ppcm, orig_a, orig_b, orig_a * orig_b))
if pgcd == 1:
    print("{} et {} sont PREMIERS ENTRE EUX.".format(orig_a, orig_b))
```

**Pourquoi cette solution ?**

L'algorithme repose sur `PGCD(a, b) = PGCD(b, a mod b)`. A chaque etape b diminue strictement,
garantissant la terminaison. Quand b = 0, `a` contient le PGCD. La relation `PGCD x PPCM = a x b`
permet de calculer le PPCM sans algorithme separe. Sauvegarder les valeurs originales est obligatoire
car elles sont modifiees en boucle.

**A retenir**

- Euclide : `while b != 0: q=a//b; r=a%b; a=b; b=r` - PGCD = `a` a la fin
- L'ordre `a = b; b = r` est critique - ne pas inverser
- PPCM = `orig_a * orig_b // pgcd` (avec `//` pour garantir un entier)
- Sauvegarder les valeurs initiales **avant** la boucle - elles seront ecrasees

---

### Exercice 15 - Conversion decimal vers binaire par divisions successives

**Enonce**

Saisir un entier positif N. Convertir en binaire par divisions successives par 2 - les restes lus
de bas en haut donnent le binaire. Construire la chaine par concatenation en tete (`str(r) + chaine`).
Verifier en reconvertissant le binaire en decimal. Afficher aussi la representation en octal.

**Code Python**

```python
original = int(input("Entier N (>= 0) : "))

if original == 0:
    binaire = "0"
    octal   = "0"
else:
    binaire = ""
    octal   = ""
    temp    = original

    while temp > 0:
        binaire = str(temp % 2) + binaire
        temp    = temp // 2

    temp = original
    while temp > 0:
        octal = str(temp % 8) + octal
        temp  = temp // 8

verification = 0
puissance    = 0
for i in range(len(binaire) - 1, -1, -1):
    verification += int(binaire[i]) * (2 ** puissance)
    puissance    += 1

print("Decimal : {}".format(original))
print("Binaire : {}  (base 2)".format(binaire))
print("Octal   : {}  (base 8)".format(octal))
print("Verif   : {} -> {} [{}]".format(
    binaire, verification, "OK" if verification == original else "ERREUR"))
```

**Pourquoi cette solution ?**

La division successive par 2 produit les bits de poids faible en premier. En **prefixant** chaque
reste (`str(reste) + chaine`), on inverse automatiquement l'ordre. La reconversion verifie
l'algorithme : `range(len(b)-1, -1, -1)` parcourt de droite a gauche.

**A retenir**

- Conversion base N : `reste = val % N` puis `val = val // N` ; repeter jusqu'a `val == 0`
- Prefixer : `str(r) + chaine` = lecture inverse automatique (restes en ordre inverse)
- Le cas `n == 0` : traiter separement (la boucle ne s'executerait jamais)
- `range(len(s) - 1, -1, -1)` = parcours de chaine de droite a gauche

---

### Exercice 16 - Test de primalite optimise (jusqu'a sqrt(N))

**Enonce**

Saisir un entier N > 1. Tester si N est premier en ne verifiant les diviseurs que jusqu'a sqrt(N)
(optimisation : `d * d <= n` evite `sqrt`). Afficher tous les diviseurs trouves. Comparer le nombre
de tests avec la methode naive (jusqu'a N-1) et calculer le gain de performance.

**Code Python**

```python
n = int(input("Entier N (> 1) : "))

est_premier   = True
diviseurs_str = ""
nb_tests_opti = 0
d             = 2

while d * d <= n:
    nb_tests_opti += 1
    if n % d == 0:
        est_premier    = False
        diviseurs_str += "{}  ".format(d)
        if d != n // d:
            diviseurs_str += "{}  ".format(n // d)
    d += 1

nb_tests_naif = n - 2

print("\n  Analyse de N = {}".format(n))
if est_premier:
    print("  Resultat  : PREMIER")
    print("  Diviseurs : 1 et {} uniquement".format(n))
else:
    print("  Resultat  : COMPOSE")
    print("  Diviseurs : 1  {}{}".format(diviseurs_str, n))

print("  Tests effectues (optimise) : {}".format(nb_tests_opti))
print("  Tests (methode naive)      : {}".format(nb_tests_naif))
if nb_tests_naif > 0:
    gain = (1.0 - nb_tests_opti / nb_tests_naif) * 100
    print("  Gain de performance        : {:.1f}%".format(gain))
```

**Pourquoi cette solution ?**

Si N possede un diviseur d > sqrt(N), alors N/d < sqrt(N) est aussi un diviseur - deja trouve.
`d * d <= n` est equivalent a `d <= sqrt(n)` mais evite de calculer une racine flottante. Pour
chaque diviseur d trouve, son "conjugue" n//d est automatiquement ajoute.

**A retenir**

- `while d * d <= n:` equivaut a `while d <= sqrt(n)` - sans `import math`
- Si `n % d == 0` et `d != n // d` : deux diviseurs trouves d'un seul test
- Gain : sqrt(1 000 000) = 1000 tests vs 999 998 naive -> gain de ~99.9%
- Complexite naive O(N) ; optimisee O(sqrt(N))

---

### Exercice 17 - Suite de Collatz : record sur une plage

**Enonce**

Saisir une limite L. Pour chaque entier de 1 a L, calculer la longueur de sa suite de Collatz
(si pair -> N//2, si impair -> 3N+1, jusqu'a 1). Trouver le nombre de depart produisant la suite
la plus longue. Afficher le record, sa longueur et le debut de la suite.

**Code Python**

```python
L = int(input("Tester les entiers de 1 a L : "))

record_longueur = 0
record_depart   = 1
record_suite    = ""

for depart in range(1, L + 1):
    n        = depart
    longueur = 1
    suite    = str(n)
    nb_affi  = 0

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        longueur += 1
        if nb_affi < 9:
            suite   += " -> " + str(n)
            nb_affi += 1
        elif nb_affi == 9:
            suite   += " -> ..."
            nb_affi += 1

    if longueur > record_longueur:
        record_longueur = longueur
        record_depart   = depart
        record_suite    = suite

print("\n  RECORD DE COLLATZ (1 a {})".format(L))
print("  Nombre de depart  : {}".format(record_depart))
print("  Longueur de suite : {} etapes".format(record_longueur))
print("  Debut de suite    : {}".format(record_suite))
```

**Pourquoi cette solution ?**

Boucle imbriquee : `for` exterieur sur tous les candidats, `while` interieur pour calculer chaque
suite. Les variables de record s'actualisent a chaque fin de suite interieure. La suite de 27
(sur L=30) a 111 etapes - resultat contre-intuitif.

**A retenir**

- **Boucle imbriquee** : `for` exterieur (exploration) + `while` interieur (calcul jusqu'a condition)
- Variables de record : initialiser avant toute boucle, comparer et mettre a jour a l'interieur
- Regles Collatz : `n//2` si pair, `3*n+1` si impair - toujours `//` (division entiere)

---

### Exercice 18 - Approximation de pi par la serie de Leibniz

**Enonce**

La serie de Leibniz : pi/4 = 1 - 1/3 + 1/5 - 1/7 + ... (signes alternes, denominateurs impairs).
Saisir N termes. Calculer l'approximation et l'erreur vs `PI_REEL = 3.14159265358979`. Trouver
ensuite combien de termes sont necessaires pour une erreur inferieure a 0.0001.

**Code Python**

```python
PI_REEL  = 3.14159265358979
n_termes = int(input("Nombre de termes N : "))

somme        = 0.0
signe        = 1
denominateur = 1

for i in range(n_termes):
    somme       += signe / denominateur
    signe        = -signe
    denominateur += 2

pi_approx = 4 * somme
erreur    = abs(pi_approx - PI_REEL)

print("  pi approx ({} termes) : {:.10f}".format(n_termes, pi_approx))
print("  pi reel               : {:.10f}".format(PI_REEL))
print("  Erreur absolue        : {:.10f}".format(erreur))

seuil  = 0.0001
somme2 = 0.0
signe2 = 1
denom2 = 1
k      = 0

while abs(4 * somme2 - PI_REEL) >= seuil or k == 0:
    somme2 += signe2 / denom2
    signe2  = -signe2
    denom2  += 2
    k       += 1

print("\n  Termes pour erreur < 0.0001 : {}".format(k))
print("  pi obtenu                   : {:.6f}".format(4 * somme2))
```

**Pourquoi cette solution ?**

La serie est alternee - le signe change a chaque terme (`signe = -signe`). Le denominateur progresse
par pas de 2 pour rester impair. La deuxieme boucle illustre "boucler jusqu'a satisfaction d'une
precision cible" au lieu de "boucler N fois".

**A retenir**

- Serie alternee : maintenir `signe` (+1 ou -1) et faire `signe = -signe` a chaque iteration
- `abs(valeur)` = valeur absolue (toujours pour mesurer une erreur)
- `for i in range(n)` pour N iterations fixes ; `while precision >= seuil` pour convergence
- Leibniz est lent : 10 000 termes donnent ~4 decimales correctes seulement

---

### Exercice 19 - Analyse linguistique d'une phrase

**Enonce**

Saisir une phrase. Parcourir chaque caractere avec `for i in range(len(phrase))`. Compter : voyelles,
consonnes (lettres a-z non voyelles), chiffres, espaces et autres. Afficher un rapport avec
pourcentages et le ratio voyelles/consonnes.

**Code Python**

```python
phrase   = input("Entrez une phrase : ")
VOYELLES = "aeiouyaaeeeeiiouu"

nb_voyelles  = 0
nb_consonnes = 0
nb_chiffres  = 0
nb_espaces   = 0
nb_autres    = 0

for i in range(len(phrase)):
    c = phrase[i].lower()
    if c.isdigit():
        nb_chiffres += 1
    elif c == " ":
        nb_espaces += 1
    elif c in VOYELLES:
        nb_voyelles += 1
    elif "a" <= c <= "z":
        nb_consonnes += 1
    else:
        nb_autres += 1

total = len(phrase)
p_v   = (nb_voyelles  / total * 100) if total > 0 else 0
p_c   = (nb_consonnes / total * 100) if total > 0 else 0

print('\n  ANALYSE : "{}"'.format(phrase))
print("  Total       : {} caracteres".format(total))
print("  Voyelles    : {:3d}  ({:.1f}%)".format(nb_voyelles,  p_v))
print("  Consonnes   : {:3d}  ({:.1f}%)".format(nb_consonnes, p_c))
print("  Chiffres    : {:3d}".format(nb_chiffres))
print("  Espaces     : {:3d}".format(nb_espaces))
print("  Autres      : {:3d}".format(nb_autres))

if nb_consonnes > 0:
    ratio = nb_voyelles / nb_consonnes
    print("  Ratio V/C   : {:.2f}  ({})".format(
        ratio, "Lisible" if ratio >= 0.7 else "Dense"))
```

**Pourquoi cette solution ?**

L'ordre dans les `elif` est critique : chiffres d'abord, puis espaces, puis voyelles (via `in`),
puis consonnes ASCII (`"a" <= c <= "z"`), puis le reste. Toujours appliquer `.lower()` avant de
comparer - `"A" in "aeiouy"` retourne `False`.

**A retenir**

- `c in "chaine_de_reference"` : operateur `in` pour tester l'appartenance a un ensemble de chars
- `"a" <= c <= "z"` : chainage d'inegalites pour tester si c est une lettre ASCII minuscule
- Toujours appliquer `.lower()` **avant** de comparer
- L'ordre des `elif` definit la priorite de classification - ne pas l'inverser

---

### Exercice 20 - Simulation de 2 des : frequences et histogramme textuel

**Enonce**

Saisir N (nombre de lancers de 2 des). Simuler N lancers avec `random.randint(1, 6)`. Compter la
frequence de chaque somme possible (2 a 12) en utilisant 11 compteurs distincts. Trouver la somme
la plus frequente. Afficher un histogramme textuel avec la probabilite theorique.

**Code Python**

```python
import random

n = int(input("Nombre de lancers : "))

c2=c3=c4=c5=c6=c7=c8=c9=c10=c11=c12 = 0

for i in range(n):
    s = random.randint(1, 6) + random.randint(1, 6)
    if   s == 2:  c2  += 1
    elif s == 3:  c3  += 1
    elif s == 4:  c4  += 1
    elif s == 5:  c5  += 1
    elif s == 6:  c6  += 1
    elif s == 7:  c7  += 1
    elif s == 8:  c8  += 1
    elif s == 9:  c9  += 1
    elif s == 10: c10 += 1
    elif s == 11: c11 += 1
    else:         c12 += 1

max_c = c2
if c3  > max_c: max_c = c3
if c4  > max_c: max_c = c4
if c5  > max_c: max_c = c5
if c6  > max_c: max_c = c6
if c7  > max_c: max_c = c7
if c8  > max_c: max_c = c8
if c9  > max_c: max_c = c9
if c10 > max_c: max_c = c10
if c11 > max_c: max_c = c11
if c12 > max_c: max_c = c12

# Probabilites theoriques (nb combinaisons sur 36)
th = [0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]

print("\n  HISTOGRAMME - {} lancers".format(n))
print("  {:<4} {:<7} {:<7} {}".format("Som.", "Freq.", "Theo.", "Histogramme"))
print("  " + "-" * 48)

for val, cnt in ((2,c2),(3,c3),(4,c4),(5,c5),(6,c6),(7,c7),
                  (8,c8),(9,c9),(10,c10),(11,c11),(12,c12)):
    bar = int(cnt / max_c * 30) if max_c > 0 else 0
    print("  {:<4} {:<7} {:<7} {}".format(
        val, cnt, "{:.1f}%".format(th[val] / 36 * 100), "*" * bar))
```

**Pourquoi cette solution ?**

Sans liste, 11 compteurs distincts remplacent un tableau de frequences. C'est intentionnellement
verbeux pour illustrer **pourquoi les listes existent**. La probabilite maximale theorique est a
la somme 7 (6 combinaisons sur 36 = 16.7%).

**A retenir**

- Sans liste : 11 compteurs separes - faisable, mais revele les limites de l'approche scalaire
- `c2=c3=...=0` : affectation multiple Python en une ligne
- `random.randint(1, 6)` : les **deux bornes sont inclusives** (contrairement a `range(1, 6)`)
- Somme 7 : la plus probable (6 combinaisons/36 = 16.7%)

---

## GROUPE C - Programmes de Synthese (21-30)

---

### Exercice 21 - Simulateur de compte bancaire avec menu

**Enonce**

Creer un simulateur de compte avec solde initial saisi. Menu en boucle `while` :
(1) Depot, (2) Retrait (refuser si insuffisant), (3) Consulter le solde, (4) Resume des operations,
(5) Quitter. Chaque operation affiche une confirmation.

**Code Python**

```python
solde          = float(input("Solde initial (HTG) : "))
nb_depots      = 0
total_depots   = 0.0
nb_retraits    = 0
total_retraits = 0.0
choix          = ""

while choix != "5":
    print("\n  +==============================+")
    print("  |    BANQUE - Compte courant   |")
    print("  +==============================+")
    print("  | 1. Depot                     |")
    print("  | 2. Retrait                   |")
    print("  | 3. Consulter le solde        |")
    print("  | 4. Resume des operations     |")
    print("  | 5. Quitter                   |")
    print("  +==============================+")
    choix = input("  Votre choix : ")

    if choix == "1":
        montant = float(input("  Montant a deposer : "))
        if montant > 0:
            solde        += montant
            nb_depots    += 1
            total_depots += montant
            print("  OK Depot de {:.2f} HTG. Solde : {:.2f} HTG".format(montant, solde))
        else:
            print("  ERREUR : Montant invalide.")

    elif choix == "2":
        montant = float(input("  Montant a retirer : "))
        if montant <= 0:
            print("  ERREUR : Montant invalide.")
        elif montant > solde:
            print("  ERREUR : Solde insuffisant ({:.2f} HTG).".format(solde))
        else:
            solde          -= montant
            nb_retraits    += 1
            total_retraits += montant
            print("  OK Retrait de {:.2f} HTG. Solde : {:.2f} HTG".format(montant, solde))

    elif choix == "3":
        print("  Solde actuel : {:.2f} HTG".format(solde))

    elif choix == "4":
        print("  --- Resume -----------------------------------")
        print("  Depots   : {} op. / {:.2f} HTG".format(nb_depots, total_depots))
        print("  Retraits : {} op. / {:.2f} HTG".format(nb_retraits, total_retraits))
        print("  Solde    : {:.2f} HTG".format(solde))

    elif choix != "5":
        print("  ERREUR : Choix invalide. Entrez 1-5.")

print("\n  Session terminee. Merci.")
```

**Pourquoi cette solution ?**

Le menu en `while choix != "5"` est le pattern fondamental des applications interactives. La
validation du retrait en deux etapes (montant valide, puis solde suffisant) est une validation
en cascade : verifier les conditions simples avant les conditions complexes.

**A retenir**

- Pattern menu : `choix = ""; while choix != "quitter":` - initialiser a valeur differente de la sortie
- Validation en cascade : montant > 0 **puis** montant <= solde (pas l'inverse)
- Les compteurs de resume s'incrementent a chaque operation reussie seulement
- `elif choix != "5":` capture les saisies invalides sans perturber la condition de sortie

---

### Exercice 22 - FizzBuzz triple avec rapport statistique

**Enonce**

Afficher les entiers de 1 a N. Regles cumulables : divisible par 3 -> "Fizz", par 5 -> "Buzz",
par 7 -> "Jazz" (15 -> "FizzBuzz", 21 -> "FizzJazz", 105 -> "FizzBuzzJazz"). Compter et afficher
un rapport final.

**Code Python**

```python
N = int(input("Limite N : "))

nb_fizz         = 0
nb_buzz         = 0
nb_jazz         = 0
nb_combinaisons = 0
nb_purs         = 0

for i in range(1, N + 1):
    sortie = ""
    if i % 3 == 0:
        sortie += "Fizz"
    if i % 5 == 0:
        sortie += "Buzz"
    if i % 7 == 0:
        sortie += "Jazz"

    if sortie == "":
        sortie = str(i)
        nb_purs += 1
    elif sortie == "Fizz":
        nb_fizz += 1
    elif sortie == "Buzz":
        nb_buzz += 1
    elif sortie == "Jazz":
        nb_jazz += 1
    else:
        nb_combinaisons += 1

    print("{:4d} -> {}".format(i, sortie))

print("\n  RAPPORT FizzBuzzJazz (1 a {})".format(N))
print("  Nombres purs      : {}".format(nb_purs))
print("  Fizz uniquement   : {}".format(nb_fizz))
print("  Buzz uniquement   : {}".format(nb_buzz))
print("  Jazz uniquement   : {}".format(nb_jazz))
print("  Combinaisons (2+) : {}".format(nb_combinaisons))
```

**Pourquoi cette solution ?**

Trois `if` independants (non `elif`) permettent de cumuler les regles. Avec `elif`, seule la premiere
regle vraie s'executerait - 15 donnerait "Fizz" au lieu de "FizzBuzz". L'accumulation sur `sortie`
(`sortie += "Fizz"`) est le coeur de l'exercice.

**A retenir**

- FizzBuzz multi-regle : **3 `if` separes** (pas `elif`) pour permettre le cumul
- `sortie += "Fizz"` : concatenation d'affectation
- Tester `if sortie == "":` **apres** les 3 `if` pour detecter "aucune regle appliquee"

---

### Exercice 23 - Tableau d'amortissement de pret a taux fixe

**Enonce**

Saisir le capital emprunte, le taux annuel (%) et la duree en mois. Calculer la mensualite fixe
(`M = P x r x (1+r)^n / ((1+r)^n - 1)` ou r = taux mensuel). Afficher mois par mois le detail
complet. Afficher le total rembourse et le cout total du credit.

**Code Python**

```python
capital     = float(input("Capital emprunte (HTG) : "))
taux_annuel = float(input("Taux annuel (%)        : "))
n_mois      = int(input("Duree (mois)           : "))

taux_mensuel = taux_annuel / 100 / 12
facteur      = (1 + taux_mensuel) ** n_mois

if taux_mensuel == 0:
    mensualite = capital / n_mois
else:
    mensualite = capital * taux_mensuel * facteur / (facteur - 1)

capital_restant = capital
total_rembourse = 0.0
total_interets  = 0.0

print("\n  TABLEAU D'AMORTISSEMENT")
print("  {:<5} {:<13} {:<11} {:<13} {:<12}".format(
    "Mois", "Capital du", "Interets", "Cap. remb.", "Restant"))
print("  " + "-" * 58)

mois = 1
while mois <= n_mois and capital_restant > 0.005:
    capital_debut     = capital_restant
    interets_mois     = capital_restant * taux_mensuel
    capital_rembourse = mensualite - interets_mois

    if capital_rembourse > capital_restant:
        capital_rembourse = capital_restant

    capital_restant -= capital_rembourse
    if capital_restant < 0:
        capital_restant = 0.0

    total_interets  += interets_mois
    total_rembourse += mensualite

    print("  {:<5} {:<13.2f} {:<11.2f} {:<13.2f} {:<12.2f}".format(
        mois, capital_debut, interets_mois, capital_rembourse, capital_restant))
    mois += 1

print("  " + "-" * 58)
print("  Total rembourse : {:.2f} HTG".format(total_rembourse))
print("  Cout du credit  : {:.2f} HTG".format(total_interets))
```

**Pourquoi cette solution ?**

La mensualite fixe garantit que le pret est solde en `n_mois`. Chaque mois, les interets se calculent
sur le **capital restant** (decroissant), donc la part d'interets diminue et la part de capital
augmente - c'est l'amortissement progressif.

**A retenir**

- Formule d'annuite : `M = P x r x (1+r)^n / ((1+r)^n - 1)` - a memoriser
- Interets du mois = capital **restant** x taux mensuel (pas sur le capital initial !)
- Capital restant diminue -> interets diminuent -> capital rembourse augmente
- Taux mensuel = taux annuel / 100 / 12

---

### Exercice 24 - Estimation de pi par la methode Monte-Carlo

**Enonce**

Tirer aleatoirement des points (x, y) dans le carre [-1, 1]^2. Un point est dans le cercle unitaire
si x2 + y2 <= 1. La proportion converge vers pi/4. Simuler avec
`random.randint(-10000, 10000) / 10000`. Afficher l'estimation pour N = 1000, 10000 et 100000.

**Code Python**

```python
import random

PI_REEL = 3.14159265358979

for n in (1000, 10000, 100000):
    dans_cercle = 0
    for i in range(n):
        x = random.randint(-10000, 10000) / 10000.0
        y = random.randint(-10000, 10000) / 10000.0
        if x * x + y * y <= 1.0:
            dans_cercle += 1

    pi_estime = 4 * dans_cercle / n
    erreur    = abs(pi_estime - PI_REEL)

    print("  N = {:>8} | dans_cercle = {:>7} | pi = {:.5f} | erreur = {:.5f}".format(
        n, dans_cercle, pi_estime, erreur))

print("\n  pi reel = {:.6f}".format(PI_REEL))
print("  Note : erreur ~ O(1/sqrt(N)) - 100x plus de points => 10x plus precis")
```

**Pourquoi cette solution ?**

Aire cercle unitaire = pi, aire carre [-1,1]^2 = 4. Proportion dans le cercle = pi/4.
`random.randint(-10000, 10000) / 10000.0` simule un reel uniforme sur [-1, 1]. La precision est
en O(1/sqrt(N)) : pour gagner 1 decimale correcte, il faut 100x plus de tirages.

**A retenir**

- Monte-Carlo : pi = 4 x (points_dans_cercle / total)
- `random.randint(a, b)` : bornes incluses - diviser pour simuler un reel
- Test cercle : `x*x + y*y <= 1.0` (pas de racine carree necessaire)
- Convergence lente : O(1/sqrt(N))

---

### Exercice 25 - Jeu Chifoumi (5 manches) avec score et series

**Enonce**

Pierre-Papier-Ciseaux sur 5 manches. L'ordinateur joue avec `random.randint(1, 3)`. Codes :
1=Pierre, 2=Papier, 3=Ciseaux. Compter victoires, defaites, nuls. Suivre la meilleure serie de
victoires consecutives. Determiner le vainqueur global.

**Code Python**

```python
import random

NOMS  = {1: "Pierre", 2: "Papier", 3: "Ciseaux"}
GAGNE = {1: 3, 2: 1, 3: 2}  # GAGNE[x] = l'objet battu par x

score_j     = 0
score_o     = 0
nb_nuls     = 0
serie_j     = 0
max_serie_j = 0

for manche in range(1, 6):
    print("\n  --- Manche {} ---".format(manche))
    joueur = int(input("  1=Pierre  2=Papier  3=Ciseaux : "))
    ordi   = random.randint(1, 3)
    print("  Vous : {}  |  Ordi : {}".format(NOMS[joueur], NOMS[ordi]))

    if joueur == ordi:
        print("  -> NUL")
        nb_nuls += 1
        serie_j  = 0
    elif GAGNE[joueur] == ordi:
        print("  -> VOUS GAGNEZ !")
        score_j += 1
        serie_j += 1
        if serie_j > max_serie_j:
            max_serie_j = serie_j
    else:
        print("  -> L'ORDINATEUR gagne.")
        score_o += 1
        serie_j  = 0

print("\n  === RESULTAT FINAL ===")
print("  Joueur : {} victoire(s)".format(score_j))
print("  Ordi   : {} victoire(s)".format(score_o))
print("  Nuls   : {}".format(nb_nuls))

if score_j > score_o:
    print("  VAINQUEUR : VOUS !")
elif score_o > score_j:
    print("  VAINQUEUR : L'ORDINATEUR")
else:
    print("  EGALITE !")

if max_serie_j >= 2:
    print("  Meilleure serie : {} manches consecutives".format(max_serie_j))
```

**Pourquoi cette solution ?**

Le dictionnaire `GAGNE = {1: 3, 2: 1, 3: 2}` encode la relation de victoire en une table de
lookup. Sans dictionnaire, il faudrait 9 conditions `if/elif`. Le compteur `serie_j` se remet
a 0 des une perte ou un nul.

**A retenir**

- Dictionnaire comme table de decision : `GAGNE[joueur] == ordi` remplace des `if/elif` multiples
- Variables de serie : compteur actuel + compteur maximum
- Remettre la serie a 0 a chaque perte ou nul
- `NOMS[valeur]` : acces dictionnaire pour la traduction code -> texte lisible

---

### Exercice 26 - Decomposition temporelle complete (secondes -> semaines)

**Enonce**

Saisir une duree totale en secondes (ou minutes). Decomposer en semaines, jours, heures, minutes
et secondes en utilisant uniquement `//` et `%`. Afficher le resultat formate. Verifier en
reconstituant le total.

**Code Python**

```python
print("Unite de saisie : 1=Secondes  2=Minutes")
unite  = int(input("Votre choix : "))
valeur = int(input("Valeur      : "))

total_sec = valeur * 60 if unite == 2 else valeur

semaines, reste   = total_sec // 604800, total_sec % 604800
jours,    reste   = reste     //  86400, reste     %  86400
heures,   reste   = reste     //   3600, reste     %   3600
minutes,  secondes = reste    //     60, reste     %     60

reconstitue = (semaines * 604800 + jours * 86400 +
               heures * 3600 + minutes * 60 + secondes)

print("\n  Duree totale : {} secondes".format(total_sec))
print("  ----------------------------------------")
print("  Semaines : {:>6}  (x 604 800 s)".format(semaines))
print("  Jours    : {:>6}  (x  86 400 s)".format(jours))
print("  Heures   : {:>6}  (x   3 600 s)".format(heures))
print("  Minutes  : {:>6}  (x      60 s)".format(minutes))
print("  Secondes : {:>6}".format(secondes))
print("  ----------------------------------------")
print("  Verif    : {} s [{}]".format(
    reconstitue, "OK" if reconstitue == total_sec else "ERREUR"))
print("\n  -> {} sem. {} j. {}h {:02d}min {:02d}s".format(
    semaines, jours, heures, minutes, secondes))
```

**Pourquoi cette solution ?**

La decomposition temporelle s'effectue par divisions euclidiennes en cascade : `//` extrait le
quotient (unite complete) et `%` extrait le reste transmis a l'etape suivante. L'ordre est critique :
commencer par la plus grande unite (semaine) jusqu'a la plus petite (seconde).

**A retenir**

- Decomposition : `quotient, reste = valeur // diviseur, valeur % diviseur`
- Facteurs cles : 60 s/min, 3 600 s/h, 86 400 s/j, 604 800 s/sem
- `{:02d}` : entier sur 2 chiffres avec zero de remplissage
- Toujours verifier par reconstitution

---

### Exercice 27 - Table de multiplication formatee avec alignement

**Enonce**

Saisir N (lignes) et M (colonnes). Afficher le tableau de multiplication N x M avec alignement
parfait (largeur calculee selon la valeur maximale N x M). Afficher les sommes de chaque ligne
et colonne.

**Code Python**

```python
N = int(input("Nombre de lignes  N : "))
M = int(input("Nombre de colonnes M : "))

lc = len(str(N * M)) + 1  # largeur colonne

entete = "     "
for j in range(1, M + 1):
    entete += "{:>{w}}".format(j, w=lc)
entete += "   | Somme"
print("\n  " + entete)
print("  " + "-" * len(entete))

for i in range(1, N + 1):
    ligne     = "  {:>3} |".format(i)
    somme_lig = 0
    for j in range(1, M + 1):
        prod       = i * j
        somme_lig += prod
        ligne     += "{:>{w}}".format(prod, w=lc)
    ligne += "   | {:>6}".format(somme_lig)
    print(ligne)

print("  " + "-" * len(entete))

ligne_somme = "  Som |"
for j in range(1, M + 1):
    s = 0
    for i in range(1, N + 1):
        s += i * j
    ligne_somme += "{:>{w}}".format(s, w=lc)
print(ligne_somme)
```

**Pourquoi cette solution ?**

L'affichage 2D sans liste necessite deux passes : une pour les lignes (sommes en une passe), une
seconde pour les sommes de colonnes (recalculer i x j pour chaque colonne). `lc = len(str(N*M)) + 1`
calcule dynamiquement la largeur necessaire.

**A retenir**

- `{:>{w}}`.format(valeur, w=largeur) : largeur de champ calculee dynamiquement
- `lc = len(str(N*M)) + 1` accommode la valeur maximale
- Sans liste, les sommes de colonnes necessitent une deuxieme boucle imbriquee
- Boucles imbriquees : `for i ... : for j ...:`

---

### Exercice 28 - Rapport de paie complet avec cotisations et impot

**Enonce**

Saisir nom, heures travaillees (avec 3 paliers HS comme exercice 5), taux horaire, annees
d'anciennete. Calculer : salaire brut (base + HS), prime d'anciennete (2%/an, max 15%), cotisation
ONA (6%), cotisation RARA (3%), impot progressif, salaire net.

**Code Python**

```python
nom        = input("Nom de l'employe    : ")
heures     = float(input("Heures travaillees  : "))
taux       = float(input("Taux horaire (HTG)  : "))
anciennete = int(input("Annees d'anciennete : "))

h_normal = min(heures, 40.0)
h_sup1   = max(0.0, min(heures, 48.0) - 40.0)
h_sup2   = max(0.0, min(heures, 60.0) - 48.0)
h_sup3   = max(0.0, heures - 60.0)
s_base   = (h_normal * taux + h_sup1 * taux * 1.5 +
            h_sup2 * taux * 2.0 + h_sup3 * taux * 2.5)

taux_anc  = min(anciennete * 2, 15) / 100
prime_anc = s_base * taux_anc
s_brut    = s_base + prime_anc

ona         = s_brut * 0.06
rara        = s_brut * 0.03
cotisations = ona + rara
imposable   = s_brut - cotisations

it2   = max(0.0, min(imposable, 150000) - 60000)  * 0.10
it3   = max(0.0, min(imposable, 250000) - 150000) * 0.20
it4   = max(0.0, imposable - 250000)              * 0.30
impot = it2 + it3 + it4

salaire_net = imposable - impot

print("\n  " + "=" * 50)
print("  FICHE DE PAIE - {}".format(nom.upper()))
print("  " + "=" * 50)
print("  Salaire brut de base    : {:>10.2f} HTG".format(s_base))
print("  Prime anciennete ({:2d}%)  : {:>10.2f} HTG".format(
    min(anciennete * 2, 15), prime_anc))
print("  SALAIRE BRUT TOTAL      : {:>10.2f} HTG".format(s_brut))
print("  " + "-" * 50)
print("  ONA (6%)                : {:>10.2f} HTG".format(ona))
print("  RARA (3%)               : {:>10.2f} HTG".format(rara))
print("  Salaire imposable       : {:>10.2f} HTG".format(imposable))
print("  Impot a la source       : {:>10.2f} HTG".format(impot))
print("  " + "=" * 50)
print("  SALAIRE NET             : {:>10.2f} HTG".format(salaire_net))
print("  " + "=" * 50)
```

**Pourquoi cette solution ?**

La fiche de paie illustre une chaine de calculs dependants : brut -> cotisations -> imposable ->
impot -> net. L'ordre est impose par les dependances. La prime d'anciennete utilise
`min(anciennete * 2, 15)` - identique au pattern de remise plafonnee (exercice 7).

**A retenir**

- Chaine de calculs : brut d'abord, net a la fin - l'ordre est impose
- Prime plafonnee : `min(taux_calcule, taux_max)` - meme pattern que remise (exercice 7)
- ONA et RARA s'appliquent sur le **brut total** (base + prime)
- `nom.upper()` : mettre le nom en majuscule pour un rapport professionnel

---

### Exercice 29 - Pipeline de validation de donnees ETL

**Enonce**

Saisir N enregistrements. Chaque enregistrement a : identifiant (str), montant (str), statut (str).
Regles : (1) identifiant commence par "REC" et a exactement 8 chars avec les 5 derniers numeriques ;
(2) montant est numerique entre 1 et 999 999 ; (3) statut est "actif" ou "inactif". Classer et
afficher un rapport de qualite de donnees.

**Code Python**

```python
n = int(input("Nombre d'enregistrements a valider : "))

total        = 0
conformes    = 0
err_id       = 0
err_montant  = 0
err_statut   = 0
err_multiple = 0

for i in range(1, n + 1):
    print("\n  --- Enregistrement {} ---".format(i))
    identifiant = input("  ID      : ")
    montant_str = input("  Montant : ")
    statut      = input("  Statut  : ")
    total      += 1

    id_ok = (identifiant.startswith("REC") and
             len(identifiant) == 8 and
             identifiant[3:].isdigit())

    montant_ok = False
    if montant_str.isdigit():
        m          = int(montant_str)
        montant_ok = (1 <= m <= 999999)

    statut_ok = (statut.lower() == "actif" or statut.lower() == "inactif")

    nb_erreurs = (0 if id_ok else 1) + (0 if montant_ok else 1) + (0 if statut_ok else 1)

    if nb_erreurs == 0:
        conformes += 1
        verdict   = "CONFORME"
    elif nb_erreurs == 1:
        if not id_ok:      err_id      += 1
        if not montant_ok: err_montant += 1
        if not statut_ok:  err_statut  += 1
        verdict = "1 ERREUR"
    else:
        err_multiple += 1
        verdict      = "{} ERREURS".format(nb_erreurs)

    print("  -> {} | ID:{} MNT:{} STAT:{}".format(
        verdict,
        "OK" if id_ok      else "ERR",
        "OK" if montant_ok else "ERR",
        "OK" if statut_ok  else "ERR"))

taux = (conformes / total * 100) if total > 0 else 0

print("\n  " + "=" * 38)
print("  RAPPORT DE QUALITE DONNEES")
print("  " + "=" * 38)
print("  Total             : {}".format(total))
print("  Conformes         : {} ({:.1f}%)".format(conformes, taux))
print("  Erreur ID         : {}".format(err_id))
print("  Erreur montant    : {}".format(err_montant))
print("  Erreur statut     : {}".format(err_statut))
print("  Erreurs multiples : {}".format(err_multiple))
print("  " + "=" * 38)

if taux >= 95:
    print("  Qualite EXCELLENTE - Pipeline pret")
elif taux >= 80:
    print("  Qualite ACCEPTABLE - Nettoyage partiel requis")
else:
    print("  Qualite INSUFFISANTE - Audit de la source requis")
```

**Pourquoi cette solution ?**

La validation multi-criteres separe les trois regles en trois booleens independants. `(0 if ok else 1)`
convertit un booleen en compte d'erreurs. `identifiant[3:]` extrait les 5 derniers caracteres -
l'indexing de tranches de chaine est valide dans la portee du cours.

**A retenir**

- Validation multi-criteres : un booleen par regle, puis les combiner
- `(0 if condition else 1)` : convertir booleen en compte d'erreurs
- `identifiant[3:]` : tranche de chaine du 4eme caractere a la fin
- Taux de conformite = indicateur cle de qualite de donnees en ETL

---

### Exercice 30 - Serie geometrique : convergence et somme

**Enonce**

Saisir le premier terme `a`, la raison `r` et le nombre de termes N. Afficher chaque terme et la
somme cumulative. Calculer la somme par la formule close (`S = a x (1 - r^n) / (1 - r)` si r != 1).
Si `|r| < 1`, afficher la somme infinie theorique `S-inf = a / (1 - r)` et l'erreur de troncature.

**Code Python**

```python
a = float(input("Premier terme a : "))
r = float(input("Raison r        : "))
N = int(input("Nombre de termes N : "))

terme       = a
somme_cumul = 0.0

print("\n  {:<6} {:<22} {:<22}".format("Terme", "Valeur", "Somme cumulee"))
print("  " + "-" * 52)

for i in range(1, N + 1):
    somme_cumul += terme
    print("  {:<6} {:<22.8f} {:<22.8f}".format(i, terme, somme_cumul))
    terme = terme * r

if r == 1:
    somme_formule = a * N
elif r == -1:
    somme_formule = a if N % 2 == 1 else 0
else:
    somme_formule = a * (1 - r ** N) / (1 - r)

print("\n  Somme boucle  (N={}) : {:.8f}".format(N, somme_cumul))
print("  Somme formule (N={}) : {:.8f}".format(N, somme_formule))
print("  Ecart               : {:.2e}".format(abs(somme_cumul - somme_formule)))

r_abs = r if r >= 0 else -r
if r_abs < 1:
    somme_infinie     = a / (1 - r)
    erreur_troncature = abs(somme_infinie - somme_cumul)
    print("\n  |r| = {:.4f} < 1 -> Serie CONVERGENTE".format(r_abs))
    print("  Somme infinie S-inf = a/(1-r) = {:.8f}".format(somme_infinie))
    print("  Erreur de troncature : {:.2e}".format(erreur_troncature))
    print("  Terme dominant restant : {:.2e}".format(abs(terme)))
elif r_abs == 1:
    print("\n  |r| = 1 -> Serie oscillante ou constante")
else:
    print("\n  |r| = {:.4f} > 1 -> Serie DIVERGENTE".format(r_abs))
```

**Pourquoi cette solution ?**

La mise a jour `terme = terme * r` (multiplicative) est plus stable numeriquement que recalculer
`a * r**i` a chaque iteration (accumulation d'erreurs flottantes). La formule close
`S = a(1-r^n)/(1-r)` permet de verifier la boucle. `{:.2e}` affiche en notation scientifique -
adapte pour les tres petites valeurs d'erreur.

**A retenir**

- Serie geometrique : chaque terme = terme precedent x r
- Formule close : `S_N = a x (1 - r^n) / (1 - r)` (valide pour r != 1)
- Convergence : `|r| < 1` -> S-inf = `a / (1 - r)` ; `|r| >= 1` -> divergence
- `{:.2e}` : notation scientifique (ex: `1.23e-07`)
- Erreur de troncature ≈ valeur absolue du prochain terme

---

*Fin du manuel - 30 exercices corriges.*

*Tous les exercices respectent la portee stricte du cours : types de base, operateurs,*
*`if/elif/else`, `while`, `for`, `break/continue`, `random.randint`, methodes de chaine, `format`.*
*Aucune liste, aucune fonction `def`, aucun `try/except`.*
