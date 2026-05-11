# Manuel de Révision Approfondi : Initiation au Métier de Spécialiste (SSD)
## Module 1 : Contexte Organizationnel et Fondations

### 1.1 L'Organisation comme Système
Une organisation n'est pas une entité statique, mais un système dynamique visant à transformer des **données brutes** (matière première) en **décisions stratégiques** (produit fini).
*   **Les Composantes (Le triangle de la valeur)** :
    *   **Humaines** : Experts (Spécialistes SSD), Décideurs (Managers), Utilisateurs finaux.
    *   **Matérielles** : Data Centers, Serveurs Cloud (Azure/AWS), terminaux, réseaux.
    *   **Financières/Immatérielles** : Budget projet, propriété intellectuelle, réputation.
*   **Types de Structures et Enjeux Data** :
    *   **Grandes Entreprises** : Silos de données complexes, enjeux de gouvernance et de sécurité massifs.
    *   **Startups (Scale-ups)** : Architectures agiles, besoin de vélocité, "Data-Centric" par défaut.
    *   **Secteur Public** : Transparence (Open Data), interopérabilité entre ministères, éthique citoyenne.

### 1.2 Le Spécialiste comme "Traducteur"
Le métier de SSD n'est pas purement technique. Il se situe à l'intersection de deux mondes :
*   **Monde Métier (Business)** : Comprendre les KPIs (Indicateurs de performance), les processus de vente, la logistique.
*   **Monde Technique (IT)** : Maîtriser le SQL, le Python, les architectures Cloud et les pipelines ETL.
*   **Le Défi** : Traduire un besoin flou ("Je veux vendre plus") en une solution technique précise ("Pipeline de recommandation basé sur l'historique d'achat").

---

## Module 2 : Méthodologies de Projet (Le Grand Duel)

### 2.1 Le Modèle en Cascade (Waterfall)
*   **Principe** : Linéaire et séquentiel. Chaque phase (Analyse -> Conception -> Dev -> Test -> Déploiement) doit être validée par une "porte de sortie" documentaire avant la suite.
*   **Avantages** : Prédictibilité budgétaire, documentation parfaite, idéal pour les projets à exigences fixes (réglementaire).
*   **Risque majeur : L'Effet Tunnel** : Absence de visibilité pour le client durant des mois, menant souvent à un produit obsolète ou inadéquat à la livraison.

### 2.2 Le Modèle en V
*   **Innovation** : Introduit une symétrie. Pour chaque niveau de conception (haut niveau, détaillé), il existe un niveau de test correspondant (Recette, Intégration, Unitaire).
*   **Bilan** : Plus robuste que la cascade, mais reste rigide face au changement.

### 2.3 L'Approche Agile (Scrum/Kanban)
*   **Philosophie** : Itérative et incrémentale. Le projet avance par cycles courts (Sprints de 2-4 semaines).
*   **Le Manifeste Agile** : Priorité aux individus et interactions, au logiciel opérationnel, à la collaboration client et à l'adaptation au changement.
*   **Points Forts** : Feedback rapide, réduction drastique de l'effet tunnel, flexibilité totale.

---

## Module 3 : Rôles et Responsabilités (Scrum & Data)

### 3.1 Les "Responsabilités" Scrum (Accountabilities)
*   **Product Owner (PO)** : Maximise la **VALEUR**. Propriétaire du Backlog, il définit le "Quoi".
*   **Scrum Master (SM)** : Maximise l'**EFFICACITÉ**. Coach de l'équipe, il élimine les obstacles et protège le focus.
*   **Les Développeurs** : Créent l'**INCRÉMENT**. Inclut les codeurs, mais aussi les testeurs et les analystes.

### 3.2 Profils Spécifiques dans un Projet Data
*   **L'Architecte** : Garant de la **PÉRENNITÉ**. Il dessine les plans (Cloud vs Local, sécurité, scalabilité).
*   **L'Analyste d'Affaires (BA)** : Garant de la **COHÉRENCE**. Il rédige les spécifications fonctionnelles.
*   **Le Testeur (QA)** : Garant de la **CONFORMITÉ**. Il définit la "Definition of Done" et cherche les failles.

---

## Module 4 : IA et Spécialiste "Augmenté"

### 4.1 L'IA comme Pilier du Workflow
L'IA n'est pas un gadget, c'est un multiplicateur de force :
*   **Nettoyage** : Identification automatique d'anomalies complexes.
*   **Code** : Génération de templates SQL/Python pour accélérer le développement.
*   **Documentation** : Traduction technique pour les non-initiés.

### 4.2 L'Art du Prompt Engineering
Un bon prompt pour un SSD doit contenir :
1.  **Rôle** (ex: "Tu es un architecte Azure Senior")
2.  **Contexte** (ex: "Nous migrons une base SQL de 10To")
3.  **Tâche** (ex: "Compare deux stratégies de partitionnement")
4.  **Contraintes** (ex: "Temps d'arrêt < 2h, coût minimal")
5.  **Format** (ex: "Tableau comparatif avec recommandation finale")
