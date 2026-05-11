# Manuel de Révision Approfondi : Phase Finale (SSD)
## Module 5 : Planification Tactique et Agilité

### 5.1 Pourquoi Planifier en Data ?
La donnée est une matière instable. Planifier permet de :
*   **Gérer l'Incertitude** : On ne connaît la qualité de la donnée qu'en l'ouvrant.
*   **Gérer les Dépendances** : Accès serveurs, droits de sécurité (IAM), disponibilité du BA.
*   **Éviter le Gaspillage** : Ne pas coder une solution complexe pour une donnée inexistante.

### 5.2 L'Impact de la Taille des Lots
*   **Gros Lots (Cascade)** : Livraison massive à la fin. Risque de rejet total par le client.
*   **Petits Lots (Agile)** : Livraison de petits incréments fonctionnels. Permet de corriger le tir immédiatement.
*   **Exercice de pensée** : Imaginez livrer un rapport de 100 pages vs 10 pages chaque semaine. Lequel permet d'ajuster le contenu selon les besoins réels ?

---

## Module 6 : Gestion du Temps et Productivité

### 6.1 Les Lois Fondamentales du Temps
1.  **Loi de Carlson (Séquence continue)** : Le temps perdu à se "remettre en train" après une interruption est supérieur au temps de l'interruption elle-même. *Conseil SSD : Bloquez des plages de 2h de code sans notifications.*
2.  **Loi de Parkinson (Dilatation)** : Le travail s'étale de manière à occuper tout le temps disponible. *Conseil SSD : Donnez-vous des échéances courtes et strictes (Timeboxing).*
3.  **Loi de Murphy (L'imprévu)** : Tout ce qui peut mal tourner tournera mal. *Conseil SSD : Prévoyez une marge de 20% dans vos estimations pour les problèmes de data quality.*
4.  **Principe de Pareto (80/20)** : 80% de la valeur provient de 20% du travail. *Conseil SSD : Identifiez les 2 tables SQL cruciales avant de nettoyer les 50 autres secondaires.*

### 6.2 Outils de Pilotage
*   **Matrice d'Eisenhower** : Prioriser selon l'Urgence et l'Importance.
*   **Estimation Agile** : Utiliser des points de complexité (Story Points) plutôt que des heures, car l'heure est subjective, la complexité est relative.

---

## Module 7 : Gestion du Stress (Approche Biologique et Proactive)

### 7.1 Le Syndrome Général d'Adaptation (Hans Selye)
Le stress est une réaction biologique en trois phases :
1.  **Phase d'Alarme** : Choc initial, libération d'**Adrénaline**. Coeur bat vite, vigilance accrue. C'est le signal d'action.
2.  **Phase de Résistance** : Le corps s'adapte pour durer. Libération de **Cortisol**. On puise dans les réserves énergétiques. C'est la phase de performance, mais elle est coûteuse.
3.  **Phase d'Épuisement** : Les réserves sont vides. Le stress devient toxique. Risque de maladies (hypertension, ulcères) et de **Burnout**.

### 7.2 Identifier les Agents Stressants (Stresseurs)
*   **Charge de travail excessive** : Trop de tâches pour le temps disponible (conflit avec Pareto).
*   **Manque de contrôle** : Dépendance envers des tiers qui ne livrent pas.
*   **Imprécision du rôle** : Ne pas savoir si on doit être dev, testeur ou analyste ce matin.

### 7.3 Stratégies de Réponse
*   **Physique** : Pauses régulières, ergonomie du poste.
*   **Organisationnelle** : Utiliser l'agilité pour dire "non" ou "plus tard" (Backlog priorisé).
*   **Cognitive** : Découper les gros problèmes stressants en petites tâches gérables.
