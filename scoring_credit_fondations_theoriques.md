# Fondations Théoriques du Scoring Crédit

## Cours Magistral — Module 1 : De la Statistique Inférentielle au Scoring Bancaire

**Auteur :** Formation Avancée en Analyse de Risque  
**Destinataire :** Alexandro Disla  
**Contexte :** Préparation au poste d'Analyste-Programmeur / Data Analyst — Secteur Bancaire  
**Prérequis :** Notions de statistiques descriptives, algèbre linéaire de base, familiarité avec les séries temporelles

---

## Introduction Générale

Le scoring crédit constitue l'une des applications les plus anciennes et les plus rigoureuses de la statistique appliquée dans le secteur financier. Bien avant l'émergence du terme « machine learning », les banques développaient des modèles de prédiction du défaut fondés sur la régression logistique — un outil dont la robustesse théorique et l'interprétabilité demeurent inégalées dans le contexte réglementaire actuel.

Ce cours magistral a pour objectif de vous doter des fondations théoriques nécessaires pour concevoir, implémenter et défendre un modèle de scoring devant un comité de risque ou un superviseur possédant une expertise statistique avancée.

Nous procéderons en quatre cycles d'apprentissage, chacun constituant un bloc conceptuel autonome mais interconnecté avec les suivants.

---

## Structure des Cycles d'Apprentissage

| Cycle | Intitulé | Objectif Pédagogique |
|-------|----------|---------------------|
| **Cycle 1** | La Régression Logistique | Maîtriser le modèle fondamental du scoring et l'interprétation de ses paramètres |
| **Cycle 2** | L'Estimation par Maximum de Vraisemblance | Comprendre comment le modèle est estimé et comment évaluer sa qualité d'ajustement |
| **Cycle 3** | Weight of Evidence et Information Value | Acquérir les techniques de transformation des variables spécifiques au scoring bancaire |
| **Cycle 4** | Métriques de Performance | Savoir évaluer et valider un modèle de scoring selon les standards de l'industrie |

---

# Cycle 1 : La Régression Logistique

## 1.1 Positionnement du Problème

Dans le contexte du scoring crédit, nous sommes confrontés à un problème de **classification binaire**. Soit Y une variable aléatoire représentant le statut de défaut d'un emprunteur :

- Y = 1 si le client fait défaut (événement « mauvais »)
- Y = 0 si le client honore ses engagements (événement « bon »)

Notre objectif est de modéliser la probabilité conditionnelle :

$$P(Y = 1 | X_1, X_2, ..., X_k)$$

où les variables $X_1, X_2, ..., X_k$ représentent les caractéristiques observables du client (revenu, ancienneté d'emploi, historique de crédit, etc.).

## 1.2 Insuffisance du Modèle Linéaire Classique

Une première approche naïve consisterait à appliquer un modèle de régression linéaire :

$$P(Y = 1 | X) = \beta_0 + \beta_1 X_1 + ... + \beta_k X_k$$

Cette approche se heurte à une difficulté fondamentale : le membre de droite n'est pas borné, alors que le membre de gauche est une probabilité devant appartenir à l'intervalle [0, 1]. Il est parfaitement possible d'obtenir des prédictions négatives ou supérieures à l'unité, ce qui est dépourvu de sens probabiliste.

## 1.3 La Transformation Logit

Pour résoudre cette difficulté, nous introduisons la **transformation logit**. Plutôt que de modéliser directement la probabilité p, nous modélisons son **logit**, défini comme le logarithme népérien du rapport des chances (odds) :

$$\text{logit}(p) = \ln\left(\frac{p}{1-p}\right)$$

Le rapport $\frac{p}{1-p}$ est appelé **odds** (ou cote en français). Il représente combien de fois l'événement Y = 1 est plus probable que l'événement Y = 0. Par exemple, si p = 0.75, alors odds = 3, signifiant que le défaut est trois fois plus probable que le non-défaut.

Le logit possède une propriété remarquable : il transforme l'intervalle ]0, 1[ en l'ensemble des réels ℝ. Ceci autorise une modélisation linéaire sans contrainte de bornes.

## 1.4 Le Modèle de Régression Logistique

Le modèle de régression logistique s'écrit :

$$\ln\left(\frac{p}{1-p}\right) = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + ... + \beta_k X_k$$

ou, de manière plus compacte :

$$\text{logit}(p) = X\beta$$

où X désigne la matrice des variables explicatives (augmentée d'une colonne de 1 pour la constante) et β le vecteur des coefficients.

## 1.5 La Fonction Sigmoïde : Inversion du Logit

Pour obtenir la probabilité p à partir du prédicteur linéaire z = Xβ, nous inversons la transformation logit :

$$p = \frac{1}{1 + e^{-z}} = \frac{e^z}{1 + e^z}$$

Cette fonction, dénommée **fonction sigmoïde** (ou fonction logistique), possède les propriétés suivantes :

- Elle est strictement croissante sur ℝ
- Elle tend vers 0 lorsque z → -∞
- Elle tend vers 1 lorsque z → +∞
- Elle vaut exactement 0.5 lorsque z = 0
- Sa dérivée est maximale en z = 0 (point d'inflexion)

Ces propriétés garantissent que nos prédictions de probabilité seront toujours comprises dans l'intervalle ]0, 1[.

## 1.6 Interprétation des Coefficients

L'interprétation des coefficients constitue l'un des avantages majeurs de la régression logistique en contexte bancaire, où la transparence et l'explicabilité des décisions sont des exigences réglementaires.

### 1.6.1 Interprétation en Termes de Log-Odds

Le coefficient $\beta_j$ représente la variation du log-odds de défaut lorsque la variable $X_j$ augmente d'une unité, toutes autres variables maintenues constantes.

Formellement :

$$\frac{\partial \text{logit}(p)}{\partial X_j} = \beta_j$$

### 1.6.2 Interprétation en Termes d'Odds Ratio

En exponentialisant le coefficient, nous obtenons l'**odds ratio** (OR) :

$$OR_j = e^{\beta_j}$$

L'odds ratio représente le facteur multiplicatif appliqué aux odds lorsque $X_j$ augmente d'une unité.

**Règles d'interprétation :**

| Valeur de $\beta_j$ | Valeur de $e^{\beta_j}$ | Interprétation |
|---------------------|-------------------------|----------------|
| $\beta_j > 0$ | OR > 1 | L'augmentation de $X_j$ accroît le risque de défaut |
| $\beta_j < 0$ | OR < 1 | L'augmentation de $X_j$ réduit le risque de défaut |
| $\beta_j = 0$ | OR = 1 | La variable $X_j$ n'a pas d'effet sur le risque |

### 1.6.3 Exemple Numérique

Supposons que le coefficient associé à la variable « ancienneté d'emploi (en années) » soit $\beta = -0.18$.

- **Interprétation log-odds** : Chaque année supplémentaire d'ancienneté diminue le log-odds de défaut de 0.18.
- **Interprétation odds ratio** : $e^{-0.18} \approx 0.835$. Chaque année supplémentaire d'ancienneté **multiplie** les odds de défaut par 0.835, soit une **réduction de 16.5%** des odds.

Cette interprétation est directement communicable à un comité de crédit : « Un client avec 5 ans d'ancienneté a, toutes choses égales par ailleurs, des odds de défaut $(0.835)^5 \approx 0.41$ fois ceux d'un client sans ancienneté — soit une réduction de près de 60%. »

## 1.7 Hypothèses du Modèle

La validité des inférences statistiques tirées d'une régression logistique repose sur un ensemble d'hypothèses qu'il convient de vérifier.

### Hypothèse 1 : Linéarité du Logit

La relation entre les variables explicatives et le log-odds doit être linéaire. Cette hypothèse n'implique pas une relation linéaire entre X et p (qui est de fait sigmoïdale), mais entre X et logit(p).

**Méthode de vérification** : Test de Box-Tidwell. On introduit un terme d'interaction $X_j \times \ln(X_j)$ ; si ce terme est significatif, l'hypothèse de linéarité est violée.

### Hypothèse 2 : Indépendance des Observations

Les observations doivent être indépendantes les unes des autres. Cette hypothèse serait violée si, par exemple, plusieurs crédits d'un même client figuraient dans l'échantillon sans prise en compte de cette structure.

**Méthode de vérification** : Analyse du design de l'étude. En cas de données groupées, recourir à des modèles multiniveaux ou à des erreurs standard robustes (clustered).

### Hypothèse 3 : Absence de Multicolinéarité Parfaite

Les variables explicatives ne doivent pas être parfaitement corrélées entre elles. Une multicolinéarité élevée (même imparfaite) gonfle la variance des estimateurs et rend les coefficients instables.

**Méthode de vérification** : Calcul du **Variance Inflation Factor (VIF)** pour chaque variable.

| VIF | Diagnostic |
|-----|------------|
| VIF < 5 | Acceptable |
| 5 ≤ VIF < 10 | Multicolinéarité modérée — à surveiller |
| VIF ≥ 10 | Multicolinéarité sévère — action corrective nécessaire |

**Actions correctives** : Élimination de variables, combinaison de variables corrélées, utilisation de techniques de régularisation (Ridge).

### Hypothèse 4 : Taille d'Échantillon Suffisante

La règle empirique dite des « Events Per Variable » (EPV) stipule qu'il faut disposer d'au moins 10 événements (défauts) par variable explicative dans le modèle.

**Exemple** : Si le taux de défaut est de 5% et que l'on souhaite inclure 15 variables, il faut au minimum $15 \times 10 / 0.05 = 3000$ observations.

### Hypothèse 5 : Absence de Valeurs Extrêmes Influentes

Certaines observations peuvent exercer une influence disproportionnée sur l'estimation des coefficients.

**Méthodes de diagnostic** :
- Résidus de Pearson standardisés (|r| > 3 suspect)
- Distance de Cook (mesure l'influence globale d'une observation)
- DFBETAs (mesure l'influence sur chaque coefficient)

---

# Cycle 2 : L'Estimation par Maximum de Vraisemblance

## 2.1 Pourquoi le Maximum de Vraisemblance ?

Contrairement à la régression linéaire où les coefficients peuvent être obtenus par une formule analytique fermée (équations normales), la régression logistique ne possède pas de solution explicite. L'estimation des paramètres requiert une procédure itérative d'optimisation numérique.

La méthode du **Maximum de Vraisemblance** (Maximum Likelihood Estimation, MLE) est l'approche standard. Elle consiste à trouver les valeurs des paramètres qui **maximisent la probabilité d'observer les données effectivement recueillies**.

## 2.2 Construction de la Fonction de Vraisemblance

### 2.2.1 Vraisemblance d'une Observation

Pour une observation i caractérisée par ses covariables $X_i$ et son statut $y_i \in \{0, 1\}$, la probabilité d'observer ce statut est :

$$P(Y_i = y_i | X_i) = p_i^{y_i} \times (1 - p_i)^{1 - y_i}$$

où $p_i = P(Y_i = 1 | X_i)$ est la probabilité de défaut prédite par le modèle.

Cette expression compacte englobe les deux cas :
- Si $y_i = 1$ : contribution = $p_i$
- Si $y_i = 0$ : contribution = $1 - p_i$

### 2.2.2 Vraisemblance Globale

Sous l'hypothèse d'indépendance des observations, la vraisemblance globale est le produit des vraisemblances individuelles :

$$L(\beta) = \prod_{i=1}^{n} p_i^{y_i} \times (1 - p_i)^{1 - y_i}$$

### 2.2.3 Log-Vraisemblance

Le produit de nombreuses probabilités (valeurs comprises entre 0 et 1) tend rapidement vers des valeurs extrêmement petites, posant des problèmes de précision numérique. On travaille donc avec le **logarithme** de la vraisemblance :

$$\ell(\beta) = \ln L(\beta) = \sum_{i=1}^{n} \left[ y_i \ln(p_i) + (1 - y_i) \ln(1 - p_i) \right]$$

Le logarithme transforme le produit en somme, ce qui est numériquement stable et mathématiquement plus aisé à manipuler.

## 2.3 Optimisation de la Log-Vraisemblance

La recherche du maximum de $\ell(\beta)$ s'effectue par des méthodes itératives, typiquement :

- **Newton-Raphson** : Utilise la dérivée première (gradient) et la dérivée seconde (matrice hessienne)
- **Fisher Scoring** : Variante utilisant l'espérance de la hessienne
- **IRLS** (Iteratively Reweighted Least Squares) : Reformulation comme problème de moindres carrés pondérés

Ces algorithmes convergent généralement en quelques itérations lorsque le modèle est correctement spécifié et les données ne présentent pas de pathologies (séparation parfaite, colinéarité).

## 2.4 Critères de Qualité d'Ajustement

### 2.4.1 La Log-Vraisemblance

La valeur de la log-vraisemblance au maximum, notée $\ell(\hat{\beta})$, constitue une mesure de l'ajustement du modèle aux données. Cependant, cette valeur dépend de la taille de l'échantillon et n'est pas directement interprétable isolément.

On compare généralement :
- $\ell_0$ : log-vraisemblance du modèle nul (constante uniquement)
- $\ell_1$ : log-vraisemblance du modèle complet

### 2.4.2 La Déviance

La **déviance** est définie comme :

$$D = -2 \ell(\hat{\beta})$$

La déviance du modèle nul moins la déviance du modèle complet suit approximativement une loi du chi-deux à k degrés de liberté (k = nombre de variables ajoutées).

### 2.4.3 Critère d'Information d'Akaike (AIC)

L'AIC pénalise la complexité du modèle :

$$AIC = -2 \ell(\hat{\beta}) + 2k$$

où k est le nombre de paramètres (coefficients inclus dans le modèle).

**Règle de décision** : Entre deux modèles, préférer celui avec l'AIC le plus faible.

### 2.4.4 Critère d'Information Bayésien (BIC)

Le BIC pénalise plus fortement la complexité, surtout pour les grands échantillons :

$$BIC = -2 \ell(\hat{\beta}) + k \ln(n)$$

où n est le nombre d'observations.

**Recommandation pratique** : Le BIC est plus conservateur et tend à sélectionner des modèles plus parcimonieux. En contexte bancaire, où l'interprétabilité prime, le BIC est souvent privilégié.

### 2.4.5 Pseudo-R² de McFadden

Par analogie avec le R² de la régression linéaire, on définit :

$$R^2_{McFadden} = 1 - \frac{\ell_1}{\ell_0}$$

**Attention** : Ce pseudo-R² n'a pas la même interprétation que le R² classique. Une valeur de 0.20 à 0.40 est généralement considérée comme satisfaisante en régression logistique.

## 2.5 Tests de Significativité

### 2.5.1 Test de Wald

Le test de Wald évalue l'hypothèse nulle $H_0 : \beta_j = 0$ pour un coefficient individuel.

**Statistique de test** :

$$W = \frac{\hat{\beta}_j}{SE(\hat{\beta}_j)}$$

Sous $H_0$, W suit approximativement une loi normale standard N(0,1). Alternativement, $W^2$ suit une loi du chi-deux à 1 degré de liberté.

**Limites** : Le test de Wald peut être biaisé lorsque les coefficients sont grands en valeur absolue (problème de Hauck-Donner).

### 2.5.2 Test du Rapport de Vraisemblance (Likelihood Ratio Test)

Le LRT compare un modèle restreint (sous $H_0$) à un modèle complet (sous $H_1$) :

$$LRT = -2(\ell_{restreint} - \ell_{complet}) = D_{restreint} - D_{complet}$$

Sous $H_0$, cette statistique suit approximativement une loi du chi-deux à q degrés de liberté, où q est le nombre de contraintes imposées par $H_0$.

**Avantage** : Le LRT est généralement plus fiable que le test de Wald, particulièrement pour les petits échantillons.

### 2.5.3 Test du Score (Test de Rao)

Le test du Score évalue les dérivées de la log-vraisemblance au point contraint (sous $H_0$). Il présente l'avantage de ne nécessiter que l'estimation du modèle restreint.

En pratique, le LRT reste le plus utilisé en raison de sa disponibilité systématique dans les logiciels statistiques.

---

# Cycle 3 : Weight of Evidence et Information Value

## 3.1 Contexte et Motivation

Le scoring crédit se distingue des applications classiques de machine learning par ses exigences spécifiques en matière de :

1. **Interprétabilité** : Chaque variable doit avoir un effet compréhensible et monotone
2. **Transparence** : Le régulateur et l'audit interne doivent pouvoir valider le modèle
3. **Stabilité** : Le modèle doit conserver ses propriétés prédictives dans le temps
4. **Conformité réglementaire** : Les accords de Bâle imposent des standards de documentation

Pour satisfaire ces exigences, les praticiens du scoring n'utilisent généralement pas les variables brutes. Ils procèdent à une transformation systématique des variables en **Weight of Evidence (WoE)**, une technique développée dans les années 1950-1960 et perfectionnée par l'industrie bancaire.

## 3.2 Le Concept de Weight of Evidence

### 3.2.1 Définition Formelle

Soit une variable X discrétisée en J catégories (ou bins). Pour chaque catégorie j, le Weight of Evidence est défini par :

$$WoE_j = \ln\left(\frac{D_j^{(G)}}{D_j^{(B)}}\right)$$

où :
- $D_j^{(G)} = \frac{n_j^{(G)}}{N^{(G)}}$ est la distribution des « Goods » (non-défaillants) dans la catégorie j
- $D_j^{(B)} = \frac{n_j^{(B)}}{N^{(B)}}$ est la distribution des « Bads » (défaillants) dans la catégorie j
- $n_j^{(G)}$ et $n_j^{(B)}$ sont respectivement les effectifs de Goods et Bads dans la catégorie j
- $N^{(G)}$ et $N^{(B)}$ sont les effectifs totaux de Goods et Bads

### 3.2.2 Interprétation Intuitive

Le WoE compare la « concentration » de bons payeurs à celle de mauvais payeurs dans chaque catégorie :

| WoE | Signification |
|-----|---------------|
| WoE > 0 | La catégorie contient proportionnellement plus de Goods que de Bads → **Faible risque** |
| WoE < 0 | La catégorie contient proportionnellement plus de Bads que de Goods → **Risque élevé** |
| WoE ≈ 0 | Distribution similaire → **Catégorie non discriminante** |

### 3.2.3 Relation avec le Log-Odds

Il existe une relation élégante entre le WoE et le log-odds. Si l'on note $\pi_j$ le taux de défaut dans la catégorie j :

$$\text{logit}(\pi_j) = \ln\left(\frac{\pi_j}{1-\pi_j}\right) = \text{logit}(\pi) + WoE_j$$

où $\pi$ est le taux de défaut global de la population.

Cette relation démontre que le WoE capture l'écart de risque entre une catégorie et la population globale, exprimé sur l'échelle du log-odds.

## 3.3 Propriétés de la Transformation WoE

### 3.3.1 Linéarisation de la Relation

Lorsque les variables sont transformées en WoE, la relation avec le log-odds de défaut devient **naturellement linéaire**. L'hypothèse de linéarité du logit (Hypothèse 1 du Cycle 1) est ainsi automatiquement satisfaite.

### 3.3.2 Standardisation de l'Échelle

Toutes les variables transformées en WoE sont exprimées sur la même échelle (le log-odds relatif). Ceci facilite la comparaison de l'importance relative des variables et l'interprétation des coefficients.

### 3.3.3 Traitement Naturel des Variables Catégorielles

Le WoE s'applique indifféremment aux variables catégorielles et aux variables continues (préalablement discrétisées). Il n'est pas nécessaire de créer des variables indicatrices (dummies).

### 3.3.4 Gestion des Modalités Rares

Les catégories à faible effectif peuvent être regroupées pour obtenir des WoE stables et statistiquement fiables.

## 3.4 Information Value (IV)

### 3.4.1 Définition

L'Information Value mesure le **pouvoir prédictif global** d'une variable. Elle agrège les WoE de toutes les catégories :

$$IV = \sum_{j=1}^{J} \left( D_j^{(G)} - D_j^{(B)} \right) \times WoE_j$$

Cette formule peut se réécrire :

$$IV = \sum_{j=1}^{J} \left( D_j^{(G)} - D_j^{(B)} \right) \times \ln\left(\frac{D_j^{(G)}}{D_j^{(B)}}\right)$$

### 3.4.2 Interprétation de l'IV

L'IV est toujours positive ou nulle. Elle quantifie la divergence entre les distributions de Goods et de Bads au sens de la mesure de Kullback-Leibler (information theory).

**Grille d'interprétation standardisée :**

| Information Value | Pouvoir Prédictif | Recommandation |
|-------------------|-------------------|----------------|
| IV < 0.02 | Non significatif | Exclure la variable |
| 0.02 ≤ IV < 0.10 | Faible | À considérer avec prudence |
| 0.10 ≤ IV < 0.30 | Moyen | Variable utile |
| 0.30 ≤ IV < 0.50 | Fort | Variable très prédictive |
| IV ≥ 0.50 | Suspicieusement élevé | Vérifier le data leakage |

### 3.4.3 Alerte sur les IV Très Élevées

Une Information Value supérieure à 0.50 doit éveiller les soupçons du modélisateur. Elle peut indiquer :

- Une **fuite d'information** (data leakage) : la variable contient, directement ou indirectement, l'information sur le défaut futur
- Une variable collectée **après** l'octroi du crédit
- Un artefact de construction de l'échantillon

Ces situations violent le principe de causalité temporelle et rendent le modèle inutilisable en production.

## 3.5 Discrétisation (Binning) des Variables Continues

### 3.5.1 Nécessité du Binning

Pour calculer le WoE d'une variable continue, il faut préalablement la découper en intervalles (bins). Le choix de ces intervalles influence directement la qualité du WoE et, par conséquent, la performance du modèle.

### 3.5.2 Méthodes de Binning

| Méthode | Principe | Avantages | Inconvénients |
|---------|----------|-----------|---------------|
| **Equal Width** | Intervalles de même amplitude | Simple à mettre en œuvre | Peut créer des bins vides ou déséquilibrés |
| **Equal Frequency** | Même effectif par bin | Équilibre statistique | Peut regrouper des valeurs aux risques différents |
| **Optimal Binning** | Maximise l'IV sous contrainte de monotonie | Performance optimale | Plus complexe, risque de surapprentissage |
| **Chi-Square Binning** | Fusionne les bins adjacents non significativement différents | Fondé statistiquement | Peut produire trop de bins |

### 3.5.3 Contrainte de Monotonie

En scoring crédit, on impose généralement que le WoE soit **monotone** (strictement croissant ou décroissant) en fonction des bins ordonnés. Cette contrainte :

- Garantit l'interprétabilité (« plus le revenu est élevé, plus le risque est faible »)
- Facilite la validation par les métiers
- Est souvent exigée par les régulateurs

**Exemple problématique** : Si le WoE est croissant puis décroissant (forme de ∩), cela suggère une relation non monotone difficile à justifier métier et à défendre en comité.

### 3.5.4 Traitement des Valeurs Manquantes

Les valeurs manquantes constituent une catégorie à part entière pour laquelle on calcule un WoE spécifique. Cette approche présente l'avantage de conserver l'information portée par l'absence de donnée (qui peut être informative en soi).

## 3.6 Processus de Transformation WoE : Synthèse

Le processus complet de transformation d'une variable en WoE suit les étapes :

1. **Analyse univariée** : Distribution, taux de défaut par modalité
2. **Binning** (si variable continue) : Choix de la méthode, définition des intervalles
3. **Calcul du WoE** : Pour chaque bin ou modalité
4. **Vérification de la monotonie** : Ajustement des bins si nécessaire
5. **Calcul de l'IV** : Évaluation du pouvoir prédictif
6. **Décision** : Inclusion ou exclusion de la variable

---

# Cycle 4 : Métriques de Performance du Scoring

## 4.1 Cadre Général de l'Évaluation

L'évaluation d'un modèle de scoring s'effectue selon deux perspectives complémentaires :

1. **Discrimination** : Le modèle sépare-t-il bien les bons des mauvais ?
2. **Calibration** : Les probabilités prédites reflètent-elles les fréquences observées ?

En contexte bancaire, la discrimination est généralement privilégiée car l'objectif premier est de **classer** les clients par ordre de risque.

## 4.2 La Courbe ROC et l'AUC

### 4.2.1 Construction de la Courbe ROC

La courbe **ROC** (Receiver Operating Characteristic) représente graphiquement le compromis entre la sensibilité et la spécificité pour tous les seuils de classification possibles.

**Définitions préliminaires** (pour un seuil de classification donné) :

| Métrique | Formule | Interprétation |
|----------|---------|----------------|
| Sensibilité (TPR) | $\frac{VP}{VP + FN}$ | Proportion de Bads correctement identifiés |
| Spécificité (TNR) | $\frac{VN}{VN + FP}$ | Proportion de Goods correctement identifiés |
| Taux de Faux Positifs (FPR) | $1 - \text{Spécificité} = \frac{FP}{FP + VN}$ | Proportion de Goods mal classés |

La courbe ROC trace la **Sensibilité (TPR)** en ordonnée contre le **Taux de Faux Positifs (FPR)** en abscisse, pour des seuils variant de 0 à 1.

### 4.2.2 Interprétation Géométrique

- Un modèle parfait produit une courbe passant par le point (0, 1) : tous les Bads sont détectés avant de mal classer le moindre Good.
- Un modèle aléatoire produit la diagonale reliant (0, 0) à (1, 1).
- Plus la courbe « bombe » vers le coin supérieur gauche, meilleur est le modèle.

### 4.2.3 L'Aire Sous la Courbe (AUC)

L'**AUC** (Area Under the Curve) synthétise la courbe ROC en un scalaire :

$$AUC = \int_0^1 TPR(t) \, d(FPR(t))$$

**Propriétés de l'AUC** :

| AUC | Interprétation |
|-----|----------------|
| 0.50 | Modèle aléatoire — aucun pouvoir discriminant |
| 0.60 - 0.70 | Discrimination faible |
| 0.70 - 0.80 | Discrimination acceptable |
| 0.80 - 0.90 | Bonne discrimination |
| 0.90 - 1.00 | Excellente discrimination (vérifier le data leakage) |

### 4.2.4 Interprétation Probabiliste de l'AUC

L'AUC possède une interprétation probabiliste élégante :

> L'AUC est la probabilité qu'un Bad choisi au hasard ait un score de risque plus élevé qu'un Good choisi au hasard.

Cette interprétation en fait une mesure naturelle de la capacité du modèle à ordonner correctement les individus.

## 4.3 La Statistique de Kolmogorov-Smirnov (KS)

### 4.3.1 Définition

La statistique **KS** mesure la séparation maximale entre les fonctions de répartition cumulative (CDF) des Goods et des Bads :

$$KS = \max_{s} \left| F^{(G)}(s) - F^{(B)}(s) \right|$$

où :
- $F^{(G)}(s)$ est la proportion de Goods ayant un score ≤ s
- $F^{(B)}(s)$ est la proportion de Bads ayant un score ≤ s

### 4.3.2 Interprétation Graphique

On trace les deux courbes cumulatives en fonction du score. Le KS est la distance verticale maximale entre ces deux courbes.

Le point où cette distance est maximale indique le **seuil optimal de séparation** — le score à partir duquel on discrimine le mieux.

### 4.3.3 Grille d'Interprétation

| KS | Évaluation |
|----|------------|
| KS < 0.20 | Modèle insuffisant |
| 0.20 ≤ KS < 0.30 | Acceptable (contexte difficile) |
| 0.30 ≤ KS < 0.40 | Bon modèle |
| 0.40 ≤ KS < 0.50 | Très bon modèle |
| KS ≥ 0.50 | Excellent — vérifier le data leakage |

### 4.3.4 Relation entre AUC et KS

Il n'existe pas de relation analytique exacte entre AUC et KS, mais empiriquement, pour des distributions raisonnablement symétriques :

$$KS \approx AUC - 0.50$$

ou encore :

$$KS \approx \frac{Gini}{2}$$

Ces approximations ne sont qu'indicatives et ne dispensent pas du calcul exact.

## 4.4 Le Coefficient de Gini

### 4.4.1 Définition

Le coefficient de **Gini** (également appelé Accuracy Ratio ou Somers' D) est une transformation linéaire de l'AUC :

$$Gini = 2 \times AUC - 1$$

### 4.4.2 Interprétation

| AUC | Gini | Interprétation |
|-----|------|----------------|
| 0.50 | 0.00 | Aucune discrimination |
| 0.70 | 0.40 | Discrimination acceptable |
| 0.80 | 0.60 | Bonne discrimination |
| 0.90 | 0.80 | Excellente discrimination |

Le Gini ramène l'échelle de l'AUC à un intervalle [0, 1] où 0 correspond au hasard, ce qui peut être plus intuitif pour certaines audiences.

## 4.5 Analyse par Déciles et Courbe de Lift

### 4.5.1 Construction de l'Analyse par Déciles

L'analyse par déciles est un outil de diagnostic essentiel en scoring bancaire :

1. Ordonner la population par score décroissant (du plus risqué au moins risqué)
2. Découper en 10 groupes de même effectif (déciles)
3. Calculer le taux de défaut observé dans chaque décile

### 4.5.2 Tableau d'Analyse par Déciles (Exemple)

| Décile | Score Moyen | Effectif | Nb Bads | Taux Défaut | % Cumulé Bads |
|--------|-------------|----------|---------|-------------|---------------|
| 1 (risqué) | 0.82 | 1000 | 180 | 18.0% | 36.0% |
| 2 | 0.71 | 1000 | 95 | 9.5% | 55.0% |
| 3 | 0.62 | 1000 | 65 | 6.5% | 68.0% |
| ... | ... | ... | ... | ... | ... |
| 10 (sûr) | 0.08 | 1000 | 8 | 0.8% | 100.0% |

### 4.5.3 Critère de Validation : Monotonie

**Règle fondamentale** : Le taux de défaut doit être strictement décroissant du décile 1 au décile 10.

Toute **inversion** (un décile ayant un taux de défaut supérieur au décile précédent) constitue un signal d'alerte grave qui nécessite investigation.

### 4.5.4 Courbe de Lift

La courbe de **Lift** (ou courbe de capture) représente le pourcentage cumulé de Bads capturés en fonction du pourcentage de population ciblée.

**Interprétation** : « En ciblant les 20% de clients les plus risqués (déciles 1-2), on capture X% de l'ensemble des défauts. »

Le **Lift** du premier décile se calcule :

$$Lift_{D1} = \frac{\text{Taux de défaut du décile 1}}{\text{Taux de défaut global}}$$

Un Lift de 3 signifie que le premier décile contient 3 fois plus de Bads que la moyenne de la population.

## 4.6 Métriques de Calibration

### 4.6.1 Test de Hosmer-Lemeshow

Ce test évalue si les probabilités prédites correspondent aux fréquences observées. On groupe les observations par décile de probabilité prédite et on compare les effectifs attendus aux effectifs observés.

**Statistique de test** : Suit approximativement une loi du chi-deux à (g-2) degrés de liberté, où g est le nombre de groupes.

**Interprétation** : Une p-value faible indique un défaut de calibration.

### 4.6.2 Brier Score

Le Brier Score mesure l'erreur quadratique moyenne des probabilités :

$$Brier = \frac{1}{n} \sum_{i=1}^{n} (p_i - y_i)^2$$

Un Brier Score plus faible indique de meilleures prédictions probabilistes.

## 4.7 Population Stability Index (PSI)

### 4.7.1 Contexte

Le **PSI** évalue la stabilité du modèle dans le temps en comparant la distribution des scores entre une période de référence (développement) et une période récente (production).

### 4.7.2 Formule

$$PSI = \sum_{j=1}^{J} \left( A_j - D_j \right) \times \ln\left(\frac{A_j}{D_j}\right)$$

où :
- $D_j$ : proportion d'observations dans le bin j au moment du développement
- $A_j$ : proportion d'observations dans le bin j en production (Actual)

### 4.7.3 Interprétation

| PSI | Interprétation |
|-----|----------------|
| PSI < 0.10 | Stabilité satisfaisante |
| 0.10 ≤ PSI < 0.25 | Changement modéré — à surveiller |
| PSI ≥ 0.25 | Changement significatif — recalibration ou redéveloppement nécessaire |

---

# Synthèse et Questions de Validation

## Questions que Votre Supérieur Pourrait Poser

À l'issue de ces quatre cycles, vous devez être en mesure de répondre avec assurance aux questions suivantes :

### Sur la Régression Logistique (Cycle 1)

1. « Pourquoi utiliser une régression logistique plutôt qu'un arbre de décision pour le scoring ? »
   
2. « Le coefficient du ratio dette/revenu est de 0.45. Que signifie-t-il concrètement ? »

3. « Quelles sont les hypothèses de la régression logistique et comment les vérifiez-vous ? »

### Sur l'Estimation (Cycle 2)

4. « Comment sont estimés les coefficients d'une régression logistique ? »

5. « Quelle différence entre le test de Wald et le test du rapport de vraisemblance ? Lequel préférez-vous ? »

6. « Comment interprétez-vous un AIC de 1250 versus 1280 ? »

### Sur WoE/IV (Cycle 3)

7. « Pourquoi transformer les variables en WoE plutôt que les utiliser brutes ? »

8. « Une variable a un IV de 0.08. La conservez-vous ? Et si elle a un IV de 0.65 ? »

9. « Comment gérez-vous une variable dont le WoE n'est pas monotone ? »

### Sur les Métriques (Cycle 4)

10. « Votre modèle a un AUC de 0.74 et un KS de 0.38. Est-ce satisfaisant ? »

11. « Que vérifiez-vous dans l'analyse par déciles ? »

12. « Le PSI est passé à 0.22. Quelle est votre réaction ? »

---

## Ressources Bibliographiques

### Ouvrages de Référence

- **Hosmer, D.W., Lemeshow, S., & Sturdivant, R.X.** (2013). *Applied Logistic Regression* (3rd ed.). Wiley.

- **Siddiqi, N.** (2017). *Credit Risk Scorecards: Developing and Implementing Intelligent Credit Scoring* (2nd ed.). Wiley.

- **Anderson, R.** (2007). *The Credit Scoring Toolkit: Theory and Practice for Retail Credit Risk Management and Decision Automation*. Oxford University Press.

### Documentation Python

- **statsmodels** : https://www.statsmodels.org/stable/index.html
- **scikit-learn** : https://scikit-learn.org/stable/
- **optbinning** : https://gnpalencia.org/optbinning/

### Documentation R (Équivalents)

- Package **glm** (base R) : Régression logistique
- Package **scorecard** : WoE/IV et développement de scorecards
- Package **pROC** : Courbes ROC et métriques de performance

---

## Prochaine Étape

Ce document constitue le socle théorique du **Cycle 1 de l'Axe 4**. La phase suivante consistera à mettre en application ces concepts via l'accès aux données (ORM SQLAlchemy) et l'analyse exploratoire en Jupyter Notebook.

*Fin du Cours Magistral — Module 1*
