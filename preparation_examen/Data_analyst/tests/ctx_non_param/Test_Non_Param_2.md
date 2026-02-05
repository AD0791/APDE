# Test Tests Non-Paramétriques - Niveau 2 (Avancé)
## UniBank Haiti - Data Analyst

**Durée:** 45 minutes  
**Questions:** 25  
**Niveau:** Avancé  
**Sujets:** Cas complexes, interprétation avancée, choix de test, puissance, effets  

---

### Q1. Vous comparez les temps de traitement de demandes de crédit entre 5 agences (n=20 par agence, distributions très asymétriques). Kruskal-Wallis donne p=0.001. Combien de comparaisons post-hoc devrez-vous effectuer avec Dunn?

A) 5  
B) 10 (C(5,2) = 5×4/2)  
C) 25  
D) 4  

**Réponse:** B) 10 (C(5,2) = 5×4/2)

*Le nombre de comparaisons par paires pour k groupes est k(k-1)/2 = 5×4/2 = 10. Chaque paire d'agences doit être comparée.*

---

### Q2. Après le test de Dunn sur les 5 agences avec correction de Holm, seules les comparaisons A-B (p_adj=0.003) et A-E (p_adj=0.01) sont significatives. Que conclure?

A) Toutes les agences sont différentes  
B) L'agence A diffère significativement de B et E, mais B-E et les autres paires ne diffèrent pas  
C) Aucune différence  
D) Le test Kruskal-Wallis était faux  

**Réponse:** B) L'agence A diffère significativement de B et E, mais B-E et les autres paires ne diffèrent pas

*Le post-hoc identifie précisément quelles paires diffèrent. Ici, A est différente de B et E. Les autres paires (incluant B-E) ne montrent pas de différence significative.*

---

### Q3. La correction de Holm est préférée à Bonferroni car:

A) Elle est plus restrictive  
B) Elle est moins conservative tout en contrôlant le taux d'erreur familywise  
C) Elle ne corrige pas du tout  
D) Elle fonctionne uniquement pour 2 comparaisons  

**Réponse:** B) Elle est moins conservative tout en contrôlant le taux d'erreur familywise

*Holm (step-down) est une procédure séquentielle moins conservative que Bonferroni. Elle offre plus de puissance tout en maintenant le contrôle de l'erreur Type I globale.*

---

### Q4. Vous calculez le r de rang (effect size) pour Mann-Whitney: r = Z/√n = 2.8/√100 = 0.28. Comment interpréter?

A) Effet négligeable  
B) Effet petit à moyen  
C) Effet très grand  
D) r ne s'interprète pas  

**Réponse:** B) Effet petit à moyen

*L'effect size r pour Mann-Whitney: 0.1 = petit, 0.3 = moyen, 0.5 = grand. Donc r = 0.28 est un effet petit à moyen.*

---

### Q5. Le test de tendance de Jonckheere-Terpstra est préféré à Kruskal-Wallis quand:

A) Les groupes sont appariés  
B) Il y a un ordre naturel attendu entre les groupes (tendance)  
C) Les données sont normales  
D) Il y a seulement 2 groupes  

**Réponse:** B) Il y a un ordre naturel attendu entre les groupes (tendance)

*Jonckheere-Terpstra teste si les médianes suivent un ordre spécifique (ex: groupes d'âge). Il est plus puissant que Kruskal-Wallis quand une tendance monotone est attendue.*

---

### Q6. Vous analysez si le score de satisfaction (1-10) augmente avec le niveau d'éducation (Primaire < Secondaire < Universitaire). Quel test privilégier?

A) Kruskal-Wallis  
B) Jonckheere-Terpstra pour tendance ordonnée  
C) Mann-Whitney  
D) Chi-carré  

**Réponse:** B) Jonckheere-Terpstra pour tendance ordonnée

*L'éducation a un ordre naturel et on s'attend à une tendance monotone. Jonckheere-Terpstra teste spécifiquement cette hypothèse de tendance.*

---

### Q7. Pour un Chi-carré 4×3, les degrés de liberté sont:

A) 12  
B) 6 ((4-1)×(3-1))  
C) 7  
D) 11  

**Réponse:** B) 6 ((4-1)×(3-1))

*Pour un tableau r×c, df = (r-1)(c-1) = (4-1)(3-1) = 3×2 = 6.*

---

### Q8. Le Chi-carré d'ajustement (goodness-of-fit) diffère du Chi-carré d'indépendance par:

A) Aucune différence  
B) L'ajustement compare une distribution observée à une distribution théorique, l'indépendance compare deux variables  
C) L'ajustement nécessite deux variables  
D) L'indépendance est pour une seule variable  

**Réponse:** B) L'ajustement compare une distribution observée à une distribution théorique, l'indépendance compare deux variables

*Goodness-of-fit: une variable, compare à une distribution attendue (ex: uniforme). Indépendance: deux variables, teste si elles sont liées.*

---

### Q9. Vous testez si la répartition des types de comptes suit une distribution uniforme (25% chacun pour 4 types). Observés: [150, 120, 100, 130]. Quel type de Chi-carré?

A) Chi-carré d'indépendance  
B) Chi-carré d'ajustement (goodness-of-fit)  
C) Test exact de Fisher  
D) Mann-Whitney  

**Réponse:** B) Chi-carré d'ajustement (goodness-of-fit)

*On compare une distribution observée à une distribution théorique (25% chacun = 125 attendus par type). C'est un test d'ajustement.*

---

### Q10. Kendall's tau-b diffère de tau-a par:

A) tau-b gère les ex-aequo (ties), tau-a non  
B) Aucune différence  
C) tau-a est toujours plus grand  
D) tau-b fonctionne uniquement pour tableaux carrés  

**Réponse:** A) tau-b gère les ex-aequo (ties), tau-a non

*tau-b ajuste pour les ex-aequo dans les deux variables, le rendant plus approprié quand il y a beaucoup de valeurs identiques (fréquent pour données ordinales).*

---

### Q11. Spearman ρ = 0.65 et Pearson r = 0.45 pour les mêmes données. Que suggère cette différence?

A) Erreur de calcul  
B) La relation est monotone mais non-linéaire (Spearman capte plus)  
C) Les deux sont incorrects  
D) Les données sont normales  

**Réponse:** B) La relation est monotone mais non-linéaire (Spearman capte plus)

*Spearman > Pearson suggère une relation monotone forte qui n'est pas parfaitement linéaire. Spearman détecte les relations curvilinéaires monotones.*

---

### Q12. Le coefficient W de Kendall dans le test de Friedman mesure:

A) La corrélation entre deux variables  
B) Le degré de concordance entre plusieurs évaluateurs/conditions  
C) La variance expliquée  
D) Le nombre de groupes  

**Réponse:** B) Le degré de concordance entre plusieurs évaluateurs/conditions

*W de Kendall (coefficient de concordance) mesure l'accord global entre les rangs attribués par différents évaluateurs ou à différentes conditions. W=1 = accord parfait.*

---

### Q13. Vous avez un tableau 2×2 avec cellules [8, 2; 1, 9]. Une cellule a fréquence attendue de 3.5. Quel test privilégier?

A) Chi-carré de Pearson  
B) Chi-carré avec correction de Yates  
C) Test exact de Fisher  
D) t-test  

**Réponse:** C) Test exact de Fisher

*Avec une fréquence attendue < 5 et un tableau 2×2, Fisher exact est préférable. Il calcule la probabilité exacte sans approximation chi-carré.*

---

### Q14. La correction de continuité de Yates pour le Chi-carré 2×2:

A) Augmente toujours la statistique Chi-carré  
B) Réduit la statistique Chi-carré, rendant le test plus conservateur  
C) N'a aucun effet  
D) Est obligatoire pour tous les Chi-carré  

**Réponse:** B) Réduit la statistique Chi-carré, rendant le test plus conservateur

*Yates soustrait 0.5 des écarts |O-E| avant de carrer. Cela réduit χ² et augmente p, rendant le test plus conservateur (moins de faux positifs).*

---

### Q15. Le test des signes diffère du test de Wilcoxon Signed-Rank par:

A) Signes utilise uniquement la direction des différences, Wilcoxon utilise aussi les magnitudes  
B) Aucune différence  
C) Wilcoxon est moins puissant  
D) Signes ne fonctionne pas pour données appariées  

**Réponse:** A) Signes utilise uniquement la direction des différences, Wilcoxon utilise aussi les magnitudes

*Le test des signes compte simplement les + et -. Wilcoxon utilise aussi la taille des différences (rangs), le rendant généralement plus puissant.*

---

### Q16. Quand utiliser le test des signes plutôt que Wilcoxon Signed-Rank?

A) Toujours  
B) Quand seul le sens du changement importe (pas la magnitude) ou pour données très ordinales  
C) Pour les grands échantillons  
D) Jamais  

**Réponse:** B) Quand seul le sens du changement importe (pas la magnitude) ou pour données très ordinales

*Le test des signes est approprié quand les différences ne peuvent pas être classées de façon fiable (très ordinal) ou quand seule la direction compte.*

---

### Q17. Vous effectuez un test Kruskal-Wallis H = 15.2 avec k=4 groupes. La valeur critique χ²(df=3, α=0.05) = 7.81. Quelle conclusion?

A) Pas de différence significative  
B) Différence significative (H > χ² critique)  
C) Besoin de plus d'information  
D) Le test est invalide  

**Réponse:** B) Différence significative (H > χ² critique)

*H = 15.2 > 7.81, donc on rejette H₀. Sous H₀, H suit approximativement χ² avec df = k-1 = 3.*

---

### Q18. Le test de permutation (permutation test) diffère des tests non-paramétriques classiques par:

A) Il est paramétrique  
B) Il calcule la distribution exacte sous H₀ par rééchantillonnage  
C) Il ne fonctionne pas pour les petits échantillons  
D) Il nécessite la normalité  

**Réponse:** B) Il calcule la distribution exacte sous H₀ par rééchantillonnage

*Les tests de permutation simulent la distribution nulle en permutant les données. Ils sont exacts et ne nécessitent aucune hypothèse distributionnelle.*

---

### Q19. Pour un Mann-Whitney avec n1=n2=50, la statistique U peut être approximée par:

A) La distribution t  
B) La distribution normale (Z)  
C) La distribution Chi-carré  
D) Aucune approximation possible  

**Réponse:** B) La distribution normale (Z)

*Pour n1, n2 > 20, U suit approximativement une loi normale avec moyenne = n1×n2/2 et variance connue. C'est cette approximation Z que scipy utilise.*

---

### Q20. Le r de Rosenthal pour l'effect size d'un test de Wilcoxon avec Z=3.5 et N=80 paires est:

A) r = 3.5/80 = 0.044  
B) r = 3.5/√80 ≈ 0.39  
C) r = 80/3.5 ≈ 22.9  
D) Impossible à calculer  

**Réponse:** B) r = 3.5/√80 ≈ 0.39

*r = Z/√N = 3.5/√80 = 3.5/8.94 ≈ 0.39, indiquant un effet moyen à grand.*

---

### Q21. Vous analysez un tableau 5×3 avec Chi-carré. Quelles sont les hypothèses à vérifier?

A) Normalité des cellules  
B) Fréquences attendues ≥ 5 dans 80% des cellules, aucune < 1  
C) Variances égales  
D) Linéarité  

**Réponse:** B) Fréquences attendues ≥ 5 dans 80% des cellules, aucune < 1

*Pour les grands tableaux, la règle est assouplie: ≥ 80% des cellules avec fréquence attendue ≥ 5 et aucune cellule < 1.*

---

### Q22. Le rapport de vraisemblance (G²) est une alternative au Chi-carré de Pearson. Quand est-il préférable?

A) Pour les petits échantillons  
B) Pour les grands tableaux clairsemés ou les modèles log-linéaires  
C) Jamais  
D) Pour les données continues  

**Réponse:** B) Pour les grands tableaux clairsemés ou les modèles log-linéaires

*G² (likelihood ratio chi-square) est préféré pour les analyses log-linéaires et peut être meilleur pour les tableaux avec beaucoup de cellules.*

---

### Q23. Vous voulez comparer les distributions complètes (pas seulement les médianes) de deux groupes. Quel test?

A) Mann-Whitney  
B) Kolmogorov-Smirnov à deux échantillons  
C) t-test  
D) Chi-carré  

**Réponse:** B) Kolmogorov-Smirnov à deux échantillons

*K-S compare les fonctions de distribution cumulatives complètes. Il détecte toute différence de distribution (position, dispersion, forme), pas seulement la tendance centrale.*

---

### Q24. Le test de Cochran's Q est utilisé pour:

A) Comparer 3+ proportions sur groupes indépendants  
B) Comparer 3+ proportions sur mesures appariées (même sujets)  
C) Tester la normalité  
D) Corrélations multiples  

**Réponse:** B) Comparer 3+ proportions sur mesures appariées (même sujets)

*Cochran's Q est l'extension de McNemar pour 3+ conditions appariées avec réponse binaire. Exemple: même clients testés sur 3 produits (achète oui/non).*

---

### Q25. Dans le contexte bancaire, vous analysez si le taux de défaut diffère selon le rating (AAA, AA, A, BBB, BB). Les données sont des proportions par cohorte. Quel test?

A) ANOVA  
B) Chi-carré de tendance (Cochran-Armitage) car les ratings sont ordonnés  
C) t-test  
D) Mann-Whitney  

**Réponse:** B) Chi-carré de tendance (Cochran-Armitage) car les ratings sont ordonnés

*Cochran-Armitage teste si la proportion varie de façon monotone avec un facteur ordonné. Parfait pour voir si le taux de défaut augmente avec la dégradation du rating.*

---

## Résumé des Concepts Avancés

### Effect Sizes
| Test | Effect Size | Formule | Interprétation |
|------|-------------|---------|----------------|
| Mann-Whitney | r | Z/√N | 0.1 petit, 0.3 moyen, 0.5 grand |
| Chi-carré | V de Cramér | √(χ²/N×min(r-1,c-1)) | 0.1 petit, 0.3 moyen, 0.5 grand |
| Friedman | W de Kendall | - | 0-1, concordance |

### Corrections pour Comparaisons Multiples
| Méthode | Type | Conservation |
|---------|------|--------------|
| Bonferroni | α/k | Très conservative |
| Holm | Step-down | Moins conservative |
| Benjamini-Hochberg | FDR | Encore moins conservative |

### Tests Spécialisés
| Situation | Test |
|-----------|------|
| Tendance ordonnée | Jonckheere-Terpstra |
| Proportions appariées binaires | McNemar (2), Cochran Q (3+) |
| Tendance proportions | Cochran-Armitage |
| Distribution complète | Kolmogorov-Smirnov |

---

**Score:** ___/25
