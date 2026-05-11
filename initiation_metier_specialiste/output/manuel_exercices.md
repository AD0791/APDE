# Manuel d'Exercices : Initiation au Métier de Spécialiste (SSD)

## Groupe A : Contexte et Rôles (Niveau Basique)
1.  **Scénario** : Une entreprise de vente en ligne remarque que ses rapports de vente mensuels ne correspondent pas aux stocks physiques.
    *   **Question** : Quel rôle (BA, Architecte, Spécialiste de données) devrait intervenir pour auditer la règle de calcul du profit ? Justifiez.
    *   **Question** : Identifiez 2 ressources matérielles et 1 ressource humaine nécessaires à ce projet.

2.  **Vrai ou Faux** :
    *   Le modèle en Cascade permet de changer les besoins du client à n'importe quel moment sans surcoût. (___)
    *   La loi de Carlson suggère de regrouper les tâches similaires pour éviter les interruptions. (___)

## Groupe B : Technique et IA (Niveau Intermédiaire - Inspiré du TP2)
3.  **Prompt Engineering** :
    *   Vous recevez un fichier `ventes.csv` avec des dates au format "JJ-MM-AAAA" et "MM/JJ/AA". Rédigez un prompt structuré (Rôle, Tâche, Contraintes) pour demander à une IA de standardiser ces dates au format ISO (AAAA-MM-JJ).

4.  **Qualité des Données** :
    *   Listez 4 anomalies typiques que l'on peut trouver dans un dataset client et proposez une action de nettoyage pour chacune.

## Groupe C : Planification et Stress (Niveau Avancé)
5.  **Gestion du Temps** :
    *   Un projet estimé à 10 jours prend finalement 15 jours car chaque petite tâche a pris plus de temps que prévu. Quelle loi de la gestion du temps explique ce phénomène ?
    *   Appliquez la matrice d'Eisenhower : Classer (Urgent/Important) : 
        *   A) Correction d'un bug bloquant en production.
        *   B) Lecture d'articles de veille technologique.
        *   C) Réunion hebdomadaire sans ordre du jour.
        *   D) Planification du prochain sprint.

6.  **Étude de Cas (Stress)** :
    *   Marc est dépassé par les délais serrés de son projet ETL. Il commence à faire des erreurs de syntaxe simples en SQL qu'il ne faisait pas avant.
    *   **Question** : De quel type de symptôme de stress s'agit-il (Physique, Émotionnel, Cognitif ou Comportemental) ?
    *   **Question** : Proposez une solution organisationnelle pour Marc.

---
## Solutions Suggérées (À consulter après l'effort !)
1. **Rôles** : L'Analyste d'Affaires (BA) pour la règle de calcul. Ressources : Serveurs, BD (Matérielles), BA/Spécialiste (Humaines).
2. **V/F** : Faux (Cascade est rigide), Vrai.
3. **Prompt** : "Tu es un expert Python. Tâche : Crée un script pour convertir les dates du fichier ventes.csv... Contrainte : Utilise Pandas, format cible AAAA-MM-JJ."
5. **Lois** : Loi de Parkinson ou Loi de Murphy. Matrice : A(U/I), B(Non U/I), C(U/Non I), D(Non U/I).
6. **Stress** : Symptôme Cognitif. Solution : Priorisation Pareto ou découpage Agile.
