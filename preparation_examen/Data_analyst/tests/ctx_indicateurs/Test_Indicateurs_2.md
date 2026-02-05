# Test Indicateurs et Indices - Test 2

**Sujet:** Indicateurs et Indices - Applications Bancaires  
**Niveau:** Intermédiaire  
**Nombre de questions:** 20

---

## Questions et Réponses

**Q1.** Comment calculer le ratio de productivité par employé?

**R1.**
```
Productivité = Métrique / Nombre d'employés

Exemples:
- PNB / Employé = 10M / 50 = 200K HTG/employé
- Prêts / Employé = 500M / 50 = 10M HTG/employé
- Clients / Employé = 5000 / 50 = 100 clients/employé
```

---

**Q2.** Comment calculer le ratio de liquidité court terme?

**R2.**
```
Quick Ratio = (Caisse + Équivalents + Titres Liquides) / Passifs Court Terme

Exemple:
Caisse: 500M
Titres liquides: 800M
Passifs CT: 1,000M
Quick Ratio = 1,300 / 1,000 = 1.3

Cible: > 1
```

---

**Q3.** Comment interpréter le ratio de transformation?

**R3.**
```
Ratio Transformation = Emplois LT / Ressources LT

< 1: Ressources LT > Emplois LT (bon)
> 1: Gap de transformation (risque de liquidité)

Idéal: Financer les actifs longs avec des ressources longues
```

---

**Q4.** Comment calculer le PNB par ligne de métier?

**R4.**
```sql
SELECT 
    ligne_metier,
    SUM(revenus_interets - charges_interets) as marge_interets,
    SUM(commissions_nettes) as commissions,
    SUM(autres_revenus) as autres,
    SUM(revenus_interets - charges_interets + commissions_nettes + autres_revenus) as pnb_total
FROM transactions
GROUP BY ligne_metier;
```

---

**Q5.** Comment mesurer l'efficience opérationnelle?

**R5.**
```
Coût par Transaction = Charges Opérationnelles / Nombre Transactions

Coût par Client = Charges Opérationnelles / Nombre Clients

Ratio Efficience = Revenus / Charges (> 1 = profitable)
```

---

**Q6.** Comment calculer le rendement ajusté au risque (RAROC)?

**R6.**
```
RAROC = (Revenus - Coûts - Pertes Attendues) / Capital Économique

Composantes:
- Revenus: Intérêts + Commissions
- Coûts: Charges opérationnelles allouées
- Pertes Attendues: EL = PD × LGD × EAD
- Capital Économique: VaR ou Economic Capital
```

---

**Q7.** Comment suivre la concentration sectorielle?

**R7.**
```sql
SELECT 
    secteur,
    SUM(encours) as total_secteur,
    SUM(encours) * 100.0 / SUM(SUM(encours)) OVER () as pct_portefeuille,
    SUM(SUM(encours)) OVER (ORDER BY SUM(encours) DESC) * 100.0 / 
        SUM(SUM(encours)) OVER () as pct_cumule
FROM portefeuille
GROUP BY secteur
ORDER BY total_secteur DESC;
```

**Seuils d'alerte:** Aucun secteur > 25% du portefeuille

---

**Q8.** Comment calculer le taux de recouvrement?

**R8.**
```
Taux Recouvrement = Montants Récupérés / Montants en Défaut × 100

LGD = 1 - Taux Recouvrement

Exemple:
Créances douteuses: 100M HTG
Montants récupérés: 55M HTG
Taux Recouvrement = 55%
LGD = 45%
```

---

**Q9.** Comment mesurer la performance du cross-selling?

**R9.**
```
Ratio Cross-sell = Nombre de Produits / Nombre de Clients

Taux Pénétration Produit = Clients avec Produit X / Total Clients × 100

Évolution:
- Nouveaux clients: 1.2 produits en moyenne
- Clients fidèles (>3 ans): 3.5 produits en moyenne
```

---

**Q10.** Comment calculer le taux d'approbation des crédits?

**R10.**
```
Taux Approbation = Demandes Approuvées / Demandes Totales × 100

Par étape:
- Taux éligibilité = Éligibles / Demandes
- Taux approbation crédit = Approuvés / Éligibles
- Taux décaissement = Décaissés / Approuvés
- Taux conversion global = Décaissés / Demandes
```

---

**Q11.** Comment mesurer la qualité du service client?

**R11.**
```
NPS = % Promoteurs - % Détracteurs

CSAT (Customer Satisfaction) = Clients Satisfaits / Total Réponses × 100

CES (Customer Effort Score) = Score moyen (1-7)

First Contact Resolution = Résolutions 1er Contact / Total Contacts × 100
```

---

**Q12.** Comment calculer le délai moyen de traitement?

**R12.**
```sql
SELECT 
    type_demande,
    AVG(date_traitement - date_reception) as delai_moyen,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY date_traitement - date_reception) as delai_median,
    PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY date_traitement - date_reception) as delai_p90
FROM demandes
WHERE statut = 'Traité'
GROUP BY type_demande;
```

---

**Q13.** Comment mesurer la fidélité client (rétention)?

**R13.**
```
Taux Rétention = Clients Fin - Nouveaux / Clients Début × 100

Taux Attrition = 1 - Taux Rétention

Durée Moyenne Relation = Σ(durée) / Nb clients
                       ≈ 1 / Taux Attrition Mensuel (en mois)
```

---

**Q14.** Comment calculer les indicateurs AML (Anti-Money Laundering)?

**R14.**
```
Taux Alertes = Alertes Générées / Transactions Analysées

Taux Faux Positifs = Alertes Non Confirmées / Alertes Totales

Taux Déclarations = STR Soumises / Alertes Confirmées
(STR = Suspicious Transaction Report)

Délai Traitement Alerte = AVG(Date Clôture - Date Alerte)
```

---

**Q15.** Comment construire un score de santé client?

**R15.**
```python
def score_sante_client(client):
    score = 100
    
    # Négatifs
    if client['jours_retard'] > 30:
        score -= 30
    elif client['jours_retard'] > 0:
        score -= 10
    
    if client['dti'] > 0.5:
        score -= 20
    elif client['dti'] > 0.35:
        score -= 10
    
    # Positifs
    if client['anciennete'] > 5:
        score += 10
    
    if client['nb_produits'] >= 3:
        score += 10
    
    return max(0, min(100, score))
```

---

**Q16.** Comment calculer le ratio de couverture des intérêts?

**R16.**
```
ICR (Interest Coverage Ratio) = EBIT / Charges d'Intérêts

Pour un emprunteur:
ICR = Résultat Opérationnel / Intérêts de la Dette

Interprétation:
- ICR > 3: Confortable
- 1.5 < ICR < 3: Acceptable
- ICR < 1.5: Risqué
- ICR < 1: Ne couvre pas ses intérêts
```

---

**Q17.** Comment mesurer l'utilisation des canaux digitaux?

**R17.**
```
% Transactions Digitales = Tx Digital / Tx Totales × 100

Taux Adoption Mobile = Clients App / Total Clients × 100

Fréquence Connexion = Connexions / Clients Actifs / Mois

Taux Conversion Digital = Actions Complétées Online / Actions Totales × 100
```

---

**Q18.** Comment calculer le coût du risque?

**R18.**
```
Coût du Risque = Dotations aux Provisions / Encours Moyen × 100

Ou en points de base (bp):
Coût du Risque = Provisions / Encours × 10,000

Exemple:
Provisions année: 50M HTG
Encours moyen: 5,000M HTG
Coût du Risque = 50 / 5,000 × 100 = 1% = 100 bp
```

---

**Q19.** Comment présenter l'évolution des KPIs?

**R19.**
```
Format recommandé pour reporting:

| KPI | Actuel | N-1 | Var | Budget | Vs Budget |
|-----|--------|-----|-----|--------|-----------|
| ROE | 15.2%  | 14.1%| +1.1pt | 14.5% | +0.7pt   |
| NPL | 4.2%   | 3.8% | +0.4pt | 4.0%  | +0.2pt   |
| CIR | 52%    | 55%  | -3pt   | 54%   | -2pt     |

pt = points de pourcentage
```

---

**Q20.** Concevez un système d'alertes basé sur les KPIs.

**R20.**
```python
def generate_alerts(kpis):
    alerts = []
    
    # NPL
    if kpis['npl'] > 0.05:
        alerts.append({'level': 'CRITICAL', 'kpi': 'NPL', 'msg': f"NPL à {kpis['npl']:.1%} > 5%"})
    elif kpis['npl'] > 0.04:
        alerts.append({'level': 'WARNING', 'kpi': 'NPL', 'msg': f"NPL à {kpis['npl']:.1%} > 4%"})
    
    # Coverage
    if kpis['coverage'] < 0.80:
        alerts.append({'level': 'CRITICAL', 'kpi': 'Coverage', 'msg': f"Coverage à {kpis['coverage']:.0%} < 80%"})
    
    # CAR
    if kpis['car'] < 0.12:
        alerts.append({'level': 'CRITICAL', 'kpi': 'CAR', 'msg': f"CAR à {kpis['car']:.1%} < 12%"})
    elif kpis['car'] < 0.14:
        alerts.append({'level': 'WARNING', 'kpi': 'CAR', 'msg': f"CAR à {kpis['car']:.1%} < 14%"})
    
    # LDR
    if kpis['ldr'] > 0.95:
        alerts.append({'level': 'WARNING', 'kpi': 'LDR', 'msg': f"LDR à {kpis['ldr']:.0%} > 95%"})
    
    return alerts
```

---

## Scoring

| Score | Niveau |
|-------|--------|
| 0-8 | À améliorer |
| 9-13 | Intermédiaire |
| 14-17 | Avancé |
| 18-20 | Expert |
