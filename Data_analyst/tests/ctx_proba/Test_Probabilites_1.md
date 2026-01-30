# Test Probabilités - Test 1

**Sujet:** Notions de Probabilité  
**Niveau:** Intermédiaire  
**Nombre de questions:** 25

---

## Questions et Réponses

**Q1.** Définissez les termes: expérience aléatoire, espace échantillonnal, événement.

**R1.**
- **Expérience aléatoire:** Processus dont le résultat n'est pas prévisible avec certitude (ex: lancer un dé)
- **Espace échantillonnal (Ω):** Ensemble de tous les résultats possibles (ex: {1,2,3,4,5,6})
- **Événement:** Sous-ensemble de Ω (ex: "obtenir un nombre pair" = {2,4,6})

---

**Q2.** Quelle est la formule de probabilité classique?

**R2.**
**Probabilité de Laplace (équiprobabilité):**
```
P(A) = Nombre de cas favorables / Nombre de cas possibles
P(A) = |A| / |Ω|
```

**Exemple:** Probabilité d'obtenir un 6 avec un dé équilibré
P(6) = 1/6 ≈ 0.167 ou 16.7%

---

**Q3.** Énoncez les trois axiomes de probabilité (Kolmogorov).

**R3.**
1. **Non-négativité:** P(A) ≥ 0 pour tout événement A
2. **Normalisation:** P(Ω) = 1 (certitude)
3. **Additivité:** Si A ∩ B = ∅, alors P(A ∪ B) = P(A) + P(B)

---

**Q4.** Qu'est-ce que le complément d'un événement?

**R4.**
Le **complément** de A (noté Ā ou A') contient tous les résultats qui ne sont pas dans A.

**Formule:**
```
P(Ā) = 1 - P(A)
```

**Exemple bancaire:** Si P(Défaut) = 5%, alors P(Non-défaut) = 95%

---

**Q5.** Quelle est la formule de l'union de deux événements?

**R5.**
**Formule générale:**
```
P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
```

**Cas particulier (événements mutuellement exclusifs):**
```
Si A ∩ B = ∅, alors P(A ∪ B) = P(A) + P(B)
```

---

**Q6.** Qu'est-ce qu'une probabilité conditionnelle?

**R6.**
La probabilité de A **sachant que** B s'est produit.

**Formule:**
```
P(A|B) = P(A ∩ B) / P(B)
```

**Exemple bancaire:**
P(Défaut | Score < 500) = Probabilité de défaut sachant que le score est bas

---

**Q7.** Qu'est-ce que l'indépendance de deux événements?

**R7.**
A et B sont **indépendants** si l'occurrence de l'un n'affecte pas la probabilité de l'autre.

**Définition:**
```
A et B indépendants ⟺ P(A ∩ B) = P(A) × P(B)
```

**Équivalent:**
```
P(A|B) = P(A)
```

---

**Q8.** Énoncez et expliquez le théorème de Bayes.

**R8.**
**Formule:**
```
P(A|B) = P(B|A) × P(A) / P(B)
```

**Avec formule des probabilités totales:**
```
P(A|B) = P(B|A) × P(A) / [P(B|A)×P(A) + P(B|Ā)×P(Ā)]
```

**Terminologie:**
- P(A): Probabilité a priori
- P(A|B): Probabilité a posteriori
- P(B|A): Vraisemblance

---

**Q9.** Application bancaire: Si 5% des clients font défaut, le test de scoring détecte 90% des défauts (sensibilité) et a 10% de faux positifs. Quelle est P(Défaut | Test Positif)?

**R9.**
**Données:**
- P(D) = 0.05 (taux de défaut)
- P(+|D) = 0.90 (sensibilité)
- P(+|D̄) = 0.10 (faux positif)

**Bayes:**
```
P(D|+) = P(+|D) × P(D) / P(+)

P(+) = P(+|D)×P(D) + P(+|D̄)×P(D̄)
P(+) = 0.90×0.05 + 0.10×0.95 = 0.045 + 0.095 = 0.14

P(D|+) = 0.90 × 0.05 / 0.14 = 0.045 / 0.14 ≈ 0.32 ou 32%
```

**Conclusion:** Même avec un bon test, seulement 32% des positifs sont de vrais défauts.

---

**Q10.** Qu'est-ce qu'une variable aléatoire discrète vs continue?

**R10.**
| Discrète | Continue |
|----------|----------|
| Valeurs dénombrables | Valeurs sur un intervalle |
| Comptage | Mesure |
| PMF (fonction de masse) | PDF (densité) |
| Exemple: Nb de défauts | Exemple: Montant du prêt |

---

**Q11.** Qu'est-ce que l'espérance (moyenne) d'une variable aléatoire?

**R11.**
**Variable discrète:**
```
E[X] = Σ xᵢ × P(X = xᵢ)
```

**Variable continue:**
```
E[X] = ∫ x × f(x) dx
```

**Propriétés:**
- E[aX + b] = a×E[X] + b
- E[X + Y] = E[X] + E[Y]

---

**Q12.** Qu'est-ce que la variance d'une variable aléatoire?

**R12.**
**Définition:**
```
Var(X) = E[(X - μ)²] = E[X²] - (E[X])²
```

**Propriétés:**
- Var(aX + b) = a² × Var(X)
- Si X et Y indépendants: Var(X + Y) = Var(X) + Var(Y)

---

**Q13.** Décrivez la distribution de Bernoulli.

**R13.**
**Variable:** X ∈ {0, 1} (succès/échec)

**Paramètre:** p = probabilité de succès

**PMF:**
```
P(X = 1) = p
P(X = 0) = 1 - p
```

**Moments:**
- E[X] = p
- Var(X) = p(1-p)

**Exemple bancaire:** Défaut (1) ou non-défaut (0)

---

**Q14.** Décrivez la distribution binomiale.

**R14.**
**Variable:** X = nombre de succès sur n essais indépendants

**Paramètres:** n (nombre d'essais), p (probabilité de succès)

**PMF:**
```
P(X = k) = C(n,k) × p^k × (1-p)^(n-k)
```

**Moments:**
- E[X] = n × p
- Var(X) = n × p × (1-p)

**Exemple:** Nombre de défauts sur 100 prêts avec taux de défaut 5%
E[X] = 100 × 0.05 = 5 défauts

---

**Q15.** Décrivez la distribution de Poisson.

**R15.**
**Variable:** X = nombre d'événements dans un intervalle

**Paramètre:** λ = taux moyen d'occurrence

**PMF:**
```
P(X = k) = (λ^k × e^(-λ)) / k!
```

**Moments:**
- E[X] = λ
- Var(X) = λ

**Exemple bancaire:** Nombre de nouveaux clients par jour (λ = 5)

---

**Q16.** Décrivez la distribution normale.

**R16.**
**Variable:** X ∈ ℝ (continue)

**Paramètres:** μ (moyenne), σ (écart-type)

**PDF:**
```
f(x) = (1/σ√2π) × exp(-(x-μ)²/2σ²)
```

**Propriétés:**
- Symétrique autour de μ
- 68-95-99.7 règle
- Z = (X-μ)/σ ~ N(0,1) (standardisation)

---

**Q17.** Comment calculer des probabilités avec la loi normale?

**R17.**
```python
from scipy.stats import norm

# P(X < 100) avec μ=80, σ=15
p = norm.cdf(100, loc=80, scale=15)

# P(X > 100)
p = 1 - norm.cdf(100, loc=80, scale=15)
# ou
p = norm.sf(100, loc=80, scale=15)

# P(70 < X < 90)
p = norm.cdf(90, 80, 15) - norm.cdf(70, 80, 15)

# Quantile (inverse): valeur pour P = 0.95
x = norm.ppf(0.95, loc=80, scale=15)
```

---

**Q18.** Qu'est-ce que la distribution log-normale?

**R18.**
Si X ~ N(μ, σ²), alors Y = e^X suit une **log-normale**.

**Propriétés:**
- Valeurs strictement positives
- Asymétrique à droite
- Souvent utilisée pour les montants financiers

**Moments:**
- E[Y] = exp(μ + σ²/2)
- Var(Y) = [exp(σ²) - 1] × exp(2μ + σ²)

---

**Q19.** Qu'est-ce que la covariance et comment l'interpréter?

**R19.**
**Définition:**
```
Cov(X,Y) = E[(X - μₓ)(Y - μᵧ)] = E[XY] - E[X]E[Y]
```

**Interprétation:**
- Cov > 0: X et Y varient dans le même sens
- Cov < 0: X et Y varient en sens opposé
- Cov = 0: Pas de relation linéaire (mais pas forcément indépendants)

---

**Q20.** Quelle est la différence entre covariance nulle et indépendance?

**R20.**
- **Indépendance → Covariance nulle:** Toujours vrai
- **Covariance nulle → Indépendance:** Pas toujours vrai

**Exemple:** X ~ N(0,1), Y = X²
- Cov(X, Y) = 0 (pas de relation linéaire)
- Mais X et Y sont dépendants (Y déterminé par X)

**Conclusion:** La covariance mesure seulement la relation LINÉAIRE.

---

**Q21.** Qu'est-ce que la loi des grands nombres?

**R21.**
**Énoncé:** Quand n → ∞, la moyenne empirique converge vers l'espérance.

```
x̄ₙ → E[X] quand n → ∞
```

**Implication bancaire:** Le taux de défaut observé sur un grand portefeuille converge vers le vrai taux de défaut.

---

**Q22.** Calculez la probabilité que sur 1000 prêts avec taux de défaut 4%, il y ait plus de 50 défauts.

**R22.**
**Méthode exacte (binomiale):**
```python
from scipy.stats import binom
p = 1 - binom.cdf(50, n=1000, p=0.04)
```

**Approximation normale (n grand):**
```
μ = np = 1000 × 0.04 = 40
σ = √(np(1-p)) = √(1000 × 0.04 × 0.96) ≈ 6.2

Z = (50.5 - 40) / 6.2 ≈ 1.69  (avec correction de continuité)
P(X > 50) = 1 - Φ(1.69) ≈ 0.046 ou 4.6%
```

---

**Q23.** Qu'est-ce que la VaR (Value at Risk) en termes probabilistes?

**R23.**
La **VaR** à α% est le quantile (1-α) des pertes.

**Définition:** P(Perte > VaR_α) = α

**Exemple:** VaR 95% = 1 million HTG signifie:
- Il y a 5% de chances de perdre plus de 1M HTG
- 95% du temps, les pertes seront < 1M HTG

```python
# Si pertes ~ N(μ, σ)
var_95 = norm.ppf(0.95, loc=mu_perte, scale=sigma_perte)
```

---

**Q24.** Comment utiliser la simulation Monte Carlo?

**R24.**
```python
import numpy as np

# Simulation de 10,000 portefeuilles
n_simulations = 10000
n_prets = 100
p_defaut = 0.05
perte_par_defaut = 50000

# Simuler le nombre de défauts
defauts = np.random.binomial(n_prets, p_defaut, n_simulations)

# Calculer les pertes
pertes = defauts * perte_par_defaut

# Statistiques
print(f"Perte moyenne: {pertes.mean():,.0f}")
print(f"Écart-type: {pertes.std():,.0f}")
print(f"VaR 95%: {np.percentile(pertes, 95):,.0f}")
print(f"VaR 99%: {np.percentile(pertes, 99):,.0f}")
```

---

**Q25.** Expliquez le concept de probabilité de défaut (PD) dans le risque de crédit.

**R25.**
**PD (Probability of Default):** Probabilité qu'un emprunteur fasse défaut sur une période donnée (généralement 1 an).

**Estimation:**
1. **Historique:** Taux de défaut observé sur le portefeuille
2. **Modèle:** Régression logistique sur les caractéristiques du client
3. **Rating:** Mapping rating → PD (ex: AAA → 0.01%, B → 5%)

**Utilisation dans Expected Loss:**
```
EL = PD × LGD × EAD
```

**En Python:**
```python
# Estimation PD avec logistique
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

# PD pour chaque client
pd_estimates = model.predict_proba(X_test)[:, 1]
```

---

## Scoring

| Score | Niveau |
|-------|--------|
| 0-10 | À améliorer |
| 11-17 | Intermédiaire |
| 18-22 | Avancé |
| 23-25 | Expert |
