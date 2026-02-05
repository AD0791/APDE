# Test Probabilités - Test 2

**Sujet:** Notions de Probabilité  
**Niveau:** Intermédiaire  
**Nombre de questions:** 20

---

## Questions et Réponses

**Q1.** Calculez P(A ∪ B) si P(A) = 0.3, P(B) = 0.4, P(A ∩ B) = 0.15

**R1.**
```
P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
P(A ∪ B) = 0.3 + 0.4 - 0.15 = 0.55
```

---

**Q2.** Si P(A|B) = 0.6, P(B) = 0.3, calculez P(A ∩ B).

**R2.**
```
P(A|B) = P(A ∩ B) / P(B)
P(A ∩ B) = P(A|B) × P(B)
P(A ∩ B) = 0.6 × 0.3 = 0.18
```

---

**Q3.** Deux événements A et B sont-ils indépendants si P(A) = 0.4, P(B) = 0.5, P(A ∩ B) = 0.2?

**R3.**
**Test d'indépendance:** A et B indépendants si P(A ∩ B) = P(A) × P(B)

```
P(A) × P(B) = 0.4 × 0.5 = 0.20
P(A ∩ B) = 0.20
```

**Conclusion:** Oui, A et B sont indépendants (0.20 = 0.20).

---

**Q4.** Quelle est la probabilité d'obtenir au moins un défaut sur 5 prêts indépendants si chaque prêt a 10% de probabilité de défaut?

**R4.**
```
P(au moins 1) = 1 - P(aucun)
P(aucun) = (1 - 0.10)^5 = 0.90^5 = 0.59049
P(au moins 1) = 1 - 0.59049 = 0.40951 ≈ 41%
```

---

**Q5.** Calculez l'espérance et la variance d'une variable Binomiale B(20, 0.05).

**R5.**
```
E[X] = n × p = 20 × 0.05 = 1
Var(X) = n × p × (1-p) = 20 × 0.05 × 0.95 = 0.95
σ = √0.95 ≈ 0.97
```

**Interprétation:** En moyenne, 1 défaut attendu sur 20 prêts, avec écart-type ≈ 1.

---

**Q6.** Une agence reçoit en moyenne 3 nouvelles demandes de prêt par heure. Quelle est la probabilité de recevoir exactement 5 demandes en une heure?

**R6.**
**Distribution de Poisson avec λ = 3:**
```
P(X = 5) = (λ^k × e^(-λ)) / k!
P(X = 5) = (3^5 × e^(-3)) / 5!
P(X = 5) = (243 × 0.0498) / 120
P(X = 5) = 12.1 / 120 ≈ 0.101 ou 10.1%
```

---

**Q7.** Si X ~ N(100, 15²), calculez P(X > 120).

**R7.**
```
Z = (X - μ) / σ = (120 - 100) / 15 = 1.33

P(X > 120) = P(Z > 1.33) = 1 - Φ(1.33)
           = 1 - 0.9082 = 0.0918 ≈ 9.2%
```

```python
from scipy.stats import norm
p = 1 - norm.cdf(120, loc=100, scale=15)  # 0.0912
```

---

**Q8.** Quelle valeur x vérifie P(X < x) = 0.95 si X ~ N(50, 10²)?

**R8.**
```
Z₀.₉₅ = 1.645 (quantile 95%)
x = μ + Z × σ = 50 + 1.645 × 10 = 66.45
```

```python
from scipy.stats import norm
x = norm.ppf(0.95, loc=50, scale=10)  # 66.45
```

---

**Q9.** Expliquez pourquoi P(|Z| > 2) ≈ 5% pour Z ~ N(0,1).

**R9.**
```
P(|Z| > 2) = P(Z < -2) + P(Z > 2)
           = 2 × P(Z > 2)
           = 2 × (1 - 0.9772)
           = 2 × 0.0228
           = 0.0456 ≈ 4.6%
```

C'est la base de la règle des 2σ (environ 95% dans μ ± 2σ).

---

**Q10.** Quelle est la distribution de la somme de n variables de Bernoulli indépendantes?

**R10.**
La somme de n variables de Bernoulli(p) indépendantes suit une **distribution Binomiale(n, p)**.

```
Si X₁, X₂, ..., Xₙ ~ Bernoulli(p) indépendantes
Alors S = X₁ + X₂ + ... + Xₙ ~ Binomiale(n, p)
```

---

**Q11.** Qu'est-ce que la distribution exponentielle et quand l'utiliser?

**R11.**
**Distribution exponentielle:** Modélise le temps entre événements d'un processus de Poisson.

**PDF:** f(x) = λe^(-λx) pour x ≥ 0

**Propriétés:**
- E[X] = 1/λ
- Var(X) = 1/λ²
- Sans mémoire: P(X > s+t | X > s) = P(X > t)

**Usage bancaire:** Temps entre défauts, temps entre transactions.

---

**Q12.** Calculez l'espérance de la perte totale si EL = PD × LGD × EAD avec PD ~ Bernoulli(0.05), LGD = 0.45, EAD = 1,000,000.

**R12.**
```
E[Perte] = E[PD] × LGD × EAD
E[Perte] = 0.05 × 0.45 × 1,000,000
E[Perte] = 22,500 HTG
```

---

**Q13.** Qu'est-ce que l'inégalité de Chebyshev?

**R13.**
**Énoncé:** Pour toute variable aléatoire X avec moyenne μ et variance σ²:
```
P(|X - μ| ≥ kσ) ≤ 1/k²
```

**Exemple:** k = 2 → P(|X - μ| ≥ 2σ) ≤ 25%

**Utilité:** Borne valable pour TOUTE distribution (pas seulement normale).

---

**Q14.** Comment calculer la corrélation entre deux variables aléatoires?

**R14.**
```
ρ(X,Y) = Cov(X,Y) / (σₓ × σᵧ)
       = E[(X-μₓ)(Y-μᵧ)] / (σₓ × σᵧ)
       = [E(XY) - E(X)E(Y)] / (σₓ × σᵧ)
```

**Propriétés:**
- -1 ≤ ρ ≤ 1
- ρ = 0 → pas de relation linéaire
- X, Y indépendants → ρ = 0 (mais pas l'inverse)

---

**Q15.** Si X et Y sont indépendants, quelle est la variance de X + Y?

**R15.**
```
Var(X + Y) = Var(X) + Var(Y) + 2×Cov(X,Y)
```

Si X et Y **indépendants**, Cov(X,Y) = 0, donc:
```
Var(X + Y) = Var(X) + Var(Y)
```

---

**Q16-20.** [Questions additionnelles sur la simulation Monte Carlo, distributions composées, et applications au risque bancaire...]

---

## Scoring

| Score | Niveau |
|-------|--------|
| 0-8 | À améliorer |
| 9-13 | Intermédiaire |
| 14-17 | Avancé |
| 18-20 | Expert |
