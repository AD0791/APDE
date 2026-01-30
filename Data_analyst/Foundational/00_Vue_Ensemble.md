# Plan de Préparation Data Analyst - Examen UniBank Haiti

## Vue d'ensemble

**Contexte:** Préparation pour un poste de Data Analyst dans une banque commerciale  
**Institution:** UniBank Haiti  
**Format:** Questions d'entretien + Études de cas pratiques  
**Niveau minimum:** Intermédiaire

---

## Structure de la Préparation

| # | Document | Sujet | Priorité |
|---|----------|-------|----------|
| 1 | `01_Data_Visualization.md` | Visualisation de données - Statistiques par graphe | Haute |
| 2 | `02_EDA_Data_Wrangling.md` | Exploration et nettoyage des données | Critique |
| 3 | `03_Indicateurs_Indices.md` | Indicateurs et indices (théorie + pratique) | Haute |
| 4 | `04_Statistiques_Descriptives.md` | Statistiques descriptives | Critique |
| 5 | `05_Statistiques_Inferentielles.md` | Enquêtes et tests d'hypothèses | Haute |
| 6 | `06_Analyse_Univariee_Multivariee.md` | Analyse uni/multivariée | Haute |
| 7 | `07_Probabilites.md` | Concepts clés de probabilité | Moyenne |
| 8 | `08_Business_Intelligence_Banque.md` | BI et métriques bancaires | Critique |
| 9 | `09_PowerBI_Python.md` | DAX, Pandas, Power BI | Critique |
| 10 | `10_SQL_Data_Analyst.md` | SQL avancé pour analysts | Haute |

---

## Dossiers Complémentaires

### `/PowerBI/`
- `DAX_Complete_Manual.md` - Manuel complet du langage DAX
- `PowerBI_Python_Integration.md` - Intégration Python dans Power BI
- `BI_Banque_Commerciale.md` - Business Intelligence bancaire

### `/revisions/`
- `Manuel_Revision_Complet.md` - Révision finale
- `Fiches_Synthese.md` - Mémos ultra-rapides avant examen

### `/tests/`
- `ctx_global/` - 4 tests globaux (30-50 questions)
- `ctx_*/` - Tests individuels par sujet (2 par sujet)

### `/FULL/`
- Études de cas complètes par domaine

---

## Principe Pareto Appliqué (20/80)

### Concepts à priorité absolue pour Data Analyst Bancaire

**Visualisation de données:**
- Histogrammes, Box plots, Scatter plots
- Choix du graphe selon le type de données
- Interprétation statistique

**EDA & Data Wrangling:**
- Détection et traitement des outliers
- Gestion des valeurs manquantes
- Feature engineering basique

**Statistiques Descriptives:**
- Moyenne, médiane, mode
- Variance, écart-type
- Quartiles, percentiles

**Statistiques Inférentielles:**
- Test t, Chi-carré, ANOVA
- p-value et intervalles de confiance
- Corrélation vs causalité

**Business Intelligence Bancaire:**
- KPIs bancaires (NPL, LTV, CAR, ROA, ROE)
- Segmentation clients
- Analyse de risque crédit

**Power BI & DAX:**
- Fonctions CALCULATE, FILTER
- Mesures vs colonnes calculées
- Contexte de filtre et de ligne
- Relations et modélisation

**SQL pour Analysts:**
- Window functions (ROW_NUMBER, RANK, LAG, LEAD)
- CTEs et requêtes complexes
- Optimisation des requêtes
- N+1 query problem

---

## Contexte Bancaire Haïtien - Points d'Attention

### Métriques Clés UniBank
- **Portefeuille de prêts:** NPL ratio, provision coverage
- **Dépôts:** Mix des dépôts, cost of funds
- **Rentabilité:** NIM, cost-to-income ratio
- **Liquidité:** LCR, NSFR
- **Capital:** CAR, Tier 1 ratio

### Réglementation
- BRH (Banque de la République d'Haïti) standards
- Reporting réglementaire
- Anti-money laundering (AML)

### Défis Data Spécifiques
- Qualité des données historiques
- Intégration de sources multiples
- Reporting en temps réel vs batch

---

## Matériel Nécessaire

### Outils Techniques
- Power BI Desktop
- Python (Pandas, NumPy, Matplotlib, Seaborn)
- SQL (PostgreSQL ou SQL Server)
- Excel avancé

### Documentation
- Ce guide de préparation complet
- Fiches de synthèse pour révision rapide
- Tests d'entraînement avec corrections

---

## Stratégie de Préparation Recommandée

### Phase 1: Fondamentaux (Jours 1-3)
1. Statistiques descriptives
2. Probabilités de base
3. SQL fondamental

### Phase 2: Analyse (Jours 4-6)
1. EDA et Data Wrangling
2. Statistiques inférentielles
3. Analyse uni/multivariée

### Phase 3: Outils (Jours 7-9)
1. Power BI et DAX
2. Python pour l'analyse
3. SQL avancé

### Phase 4: Contexte (Jours 10-11)
1. BI bancaire
2. Métriques et KPIs
3. Études de cas

### Phase 5: Révision (Jour 12)
1. Tests pratiques
2. Fiches de synthèse
3. Simulation d'entretien

---

## Conseils pour l'Entretien

### Questions Techniques
- Toujours contextualiser avec des exemples bancaires
- Montrer la compréhension business, pas juste technique
- Expliquer le "pourquoi" derrière chaque choix

### Études de Cas
- Structurer la réponse: Problème → Données → Méthode → Résultat
- Mentionner les limites et hypothèses
- Proposer des next steps

### Communication
- Vulgariser pour un public non-technique
- Utiliser des analogies bancaires
- Être prêt à défendre ses choix méthodologiques

---

**Objectif:** Démontrer une maîtrise technique solide avec une compréhension approfondie du contexte bancaire haïtien.
