# Cahier d'Exercices Magistral avec Corrigés Détaillés
## Initiation au Métier de Spécialiste (SSD)

### PARTIE 1 : Études de Cas - Rôles et Méthodologies

#### Exercice 1 : Le Dilemme du Projet de Migration
**Énoncé** : La banque "Alpha" veut migrer toutes ses données clients d'un vieux serveur local vers Azure Cloud. Le budget est de 500k$, et le délai est de 6 mois. Les règles de calcul des intérêts sont très strictes et régies par la loi.
1.  Quelle méthodologie choisiriez-vous (Cascade ou Agile) ? Justifiez avec deux arguments.
2.  L'équipe rencontre un problème : les données du vieux serveur sont corrompues. Qui, entre l'Architecte, le QA et le Développeur, doit prendre le leadership pour concevoir la nouvelle structure de stockage sécurisée ?
3.  Le client se plaint de ne rien voir après 3 mois de travail. Quel phénomène méthodologique Marc, le chef de projet, n'a-t-il pas su éviter ?

**CORRIGÉ DÉTAILLÉ** :
1.  **Choix : Cascade (Waterfall)**. 
    *   *Argument 1* : Les exigences sont strictes et réglementaires (loi), donc peu susceptibles de changer.
    *   *Argument 2* : Le budget et le délai sont fixes, ce qui correspond à la prédictibilité de la Cascade.
    *   *Alternative acceptable* : Un "Agile hybride" pour rassurer le client, mais la Cascade est la réponse classique ici.
2.  **L'Architecte**. C'est sa responsabilité de dessiner les plans de structure, de choisir les technologies (Azure) et de garantir la sécurité globale.
3.  **L'Effet Tunnel**. C'est le risque majeur de la Cascade où le client est déconnecté de la réalisation jusqu'à la livraison finale.

---

### PARTIE 2 : Exercices Techniques - IA et Qualité

#### Exercice 2 : Ingénierie de Prompt (Le Spécialiste Augmenté)
**Énoncé** : Vous avez un dataset de 10 000 transactions. Vous suspectez des doublons "flous" (ex: "Alex Disla" et "Alexandro Disla" à la même adresse).
*   Rédigez un prompt "Senior" pour demander à une IA de vous proposer une stratégie de nettoyage en Python. Le prompt doit respecter les 5 composantes (Rôle, Contexte, Tâche, Contraintes, Format).

**CORRIGÉ DÉTAILLÉ** :
*   **Rôle** : Tu es un Expert Data Scientist spécialisé en déduplication (Fuzzy Matching).
*   **Contexte** : Nous nettoyons un fichier de 10 000 transactions bancaires pour un audit de conformité.
*   **Tâche** : Propose un script Python utilisant la bibliothèque `fuzzywuzzy` ou `recordlinkage` pour identifier les doublons potentiels sur les noms et adresses.
*   **Contraintes** : Le script doit être optimisé pour ne pas comparer chaque ligne avec toutes les autres (utiliser le bloquage/indexing). Seuil de similarité à 85%.
*   **Format** : Code Python commenté avec une explication brève de la logique de "Score de distance de Levenshtein".

---

### PARTIE 3 : Productivité et Psychologie du Travail

#### Exercice 3 : Application des Lois du Temps
**Énoncé** : Julie est une SSD talentueuse. Voici sa journée :
*   9h00 : Début du code SQL.
*   9h15 : Notification Teams (Question sur un vieux ticket). Elle répond pendant 10 min.
*   9h25 : Retour au SQL (met 15 min à retrouver sa logique).
*   10h00 : Réunion de 2h pour une tâche qui aurait pu être réglée en 20 min par email.
1.  Quelle loi explique pourquoi Julie a mis 15 min à reprendre son travail à 9h25 ?
2.  Quelle loi explique pourquoi la réunion de 10h00 a duré 2 heures ?
3.  Si Julie doit nettoyer 100 tables, mais que 20 d'entre elles contiennent 80% des données vitales de la banque, quel principe doit-elle appliquer pour son planning ?

**CORRIGÉ DÉTAILLÉ** :
1.  **Loi de Carlson**. Elle stipule qu'un travail interrompu est beaucoup moins efficace. Le "coût cognitif de remise en train" est ici de 15 minutes pour seulement 10 minutes d'interruption.
2.  **Loi de Parkinson**. Le travail (la réunion) s'est étalé pour occuper tout le temps qui lui avait été alloué dans l'agenda (2h), même si le sujet était simple.
3.  **Principe de Pareto (80/20)**. Elle doit prioriser les 20 tables critiques pour maximiser la valeur produite en un minimum de temps.

#### Exercice 4 : Analyse du Stress
**Énoncé** : Après 3 semaines de "Phase de Résistance" sur un projet en retard, Thomas commence à avoir des maux de dos chroniques et oublie des réunions importantes.
1.  Identifiez un symptôme physique et un symptôme cognitif chez Thomas.
2.  Thomas est-il toujours en phase de performance ou risque-t-il la rupture ? Nommez la phase suivante selon Hans Selye.
3.  Proposez une solution basée sur l'Agilité pour réduire son stress.

**CORRIGÉ DÉTAILLÉ** :
1.  **Symptôme physique** : Maux de dos chroniques. **Symptôme cognitif** : Oublis de réunions (troubles de la mémoire immédiate).
2.  Il risque la rupture. La phase suivante est la **Phase d'Épuisement** (Burnout), où l'organisme ne peut plus compenser la dépense énergétique.
3.  **La Priorisation du Backlog**. En collaboration avec le Product Owner, Thomas doit réduire le périmètre du Sprint actuel pour ne garder que les tâches vitales, allégeant ainsi sa charge de travail immédiate.
