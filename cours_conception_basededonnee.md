# Analyse et conception d’une solution de données — Cours regroupés

**Code du cours : 420-C47-BB**  
**Enseignant : Nadir Bouakel**

> Fichier Markdown généré à partir des PDF fournis. La conversion est textuelle : les schémas, logos et captures d’écran peuvent être décrits seulement par le texte extrait automatiquement.

## Table des matières

- [Cours 1](#cours-1)
- [Cours 5](#cours-5)
- [Cours 7](#cours-7)
- [Cours 8](#cours-8)
- [Cours 9](#cours-9)
- [Cours 10](#cours-10)
- [Cours 11](#cours-11)

---

# Cours 1

_Source : C47-cours1(2).pdf — 52 diapositives/pages_

## Cours 1 — Diapositive 1 : Analyse et conception

Analyse et conception
d’une solution de données

Code du Cours : 420-C47-BB

Cours 1

Enseignant : Nadir, BOUAKEL
nadir.bouakel@bdeb.qc.ca

---

## Cours 1 — Diapositive 2 : Plan de la séance

Plan de la séance

- Qui suis-je ?
- Qui êtes-vous ?
- Objectifs du cours
- Règles et attentes
- Stratégie pédagogique
- Évaluation
- Cours 1 :

- Introduction
- Cycle de vie de développement logiciel
- Différents modèles du cycle de vie

2

---

## Cours 1 — Diapositive 3 : Qui suis-je?

Qui suis-je?

3

---

## Cours 1 — Diapositive 4 : Expérience

Expérience

Cursus

Objectifs

Loisirs

Motivation

Qui êtes-vous?

Nom

Formation

Intérêts

Profession

4

---

## Cours 1 — Diapositive 5 : Objectifs du cours

Objectifs du cours

5

---

## Cours 1 — Diapositive 6 : Règles et attentes

Règles et attentes

- Présence et participation!
- 5% de la note pour la qualité du français pour chaque examen ou TP
- Toute absence doit être justifiée sinon la note zéro s’applique.
- Respect des échéances, en cas de retard : -5 % par jour ouvrable 3

jours de retard = note zéro
- Plagiat et tricherie (AUCUNE TOLÉRENCE !)

6

---

## Cours 1 — Diapositive 7 : Sans titre

7

---

## Cours 1 — Diapositive 8 : Évaluation

Évaluation

9

---

## Cours 1 — Diapositive 9 : Question ?

Question ?

10

---

## Cours 1 — Diapositive 10 : Les concepts

Les concepts
fondamentaux du génie

logiciel

11

---

## Cours 1 — Diapositive 11 : Qu’est-ce que le génie logiciel?

Qu’est-ce que le génie logiciel?

Le génie logiciel est la discipline qui applique des méthodes d’ingénierie
rigoureuses à la conception, au développement, à la validation et à la
maintenance de logiciels complexes.

- Son objectif est de produire des logiciels fiables, maintenables et adaptés

aux besoins réels, dans des contraintes de coût, de délai et de qualité
clairement définies.

12

---

## Cours 1 — Diapositive 12 : Un produit logiciel est un programme informatique

Un produit logiciel est un programme informatique
conçu pour répondre à un besoin précis. C’est un
logiciel qui est fabriqué, vendu ou distribué pour
être utilisé par des personnes.

Qu’est-ce
- u’un
produit
logiciel ?

Caractéristiques clés :

- Fonctionnalité : ce que le logiciel fait

- Fiabilité : comportement correct et stable

- Maintenabilité : facilité de modification et

d’évolution

- Portabilité : capacité à fonctionner dans

différents environnements

13

---

## Cours 1 — Diapositive 13 : Exemples de logiciels :

Exemples de logiciels :

- Navigateurs web : Google Chrome, Mozilla Firefox, Safari

- Jeux vidéo : Minecraft, FIFA, Uncharted

- Applications mobiles : WhatsApp, Instagram, Messenger

- Logiciels de bureautique : Microsoft Word, Excel, LibreOffice

14

---

## Cours 1 — Diapositive 14 : Livrable

Livrable

Les livrables sont les documents ou artefacts produits au cours du projet
logiciel, servant à valider, communiquer ou documenter le travail.

Exemples :

- Cahier des charges / spécifications fonctionnelles

- Modèles de données et schémas architecturaux

- Prototypes ou maquettes

- Documentation technique et utilisateur

Ils permettent d’assurer la traçabilité et de réduire les ambiguïtés dans le
projet.
15

---

## Cours 1 — Diapositive 15 : Taches et Activités

Taches et Activités

Une tâche est une unité de travail assignable, qui contribue à la réalisation
d’un livrable ou d’une étape du projet. Les tâches sont souvent regroupées
en activités plus larges : conception, développement, tests, documentation.

- Objectif clair et mesurable

- Durée et ressources estimées

- Dépendances avec d’autres tâches

La gestion efficace des tâches permet de suivre l’avancement du projet et
d’identifier rapidement les problèmes.

16

---

## Cours 1 — Diapositive 16 : Modularité

Modularité

La modularité signifie qu’un logiciel est divisé en petites parties
indépendantes appelées modules. Chaque module fait une tâche précise, et on peut
les modifier ou les remplacer sans toucher à tout le logiciel.

- Facilite la compréhension, le test et la maintenance

- Réduit les risques d’erreurs

17

---

## Cours 1 — Diapositive 17 : Réutilisabilité

Réutilisabilité

La réutilisabilité signifie qu’un composant ou un module peut être utilisé dans
plusieurs projets différents, sans le réécrire.

- Permet de gagner du temps et réduire les coûts

- Favorise la cohérence entre différents projets

18

---

## Cours 1 — Diapositive 18 : Documentation

Documentation

La documentation est un élément clé du génie logiciel, elle accompagne le
développement et assure la compréhension du logiciel par tous.

- Technique : pour les développeurs et mainteneurs
- Utilisateur : guide et manuel pour l’exploitation

- Projet : rapports, plan de tests, décisions de conception

19

---

## Cours 1 — Diapositive 19 : Atelier – Décomposer

Atelier – Décomposer

20

---

## Cours 1 — Diapositive 20 : Décrire le

Décrire le
produit logiciel

---

## Cours 1 — Diapositive 21 : Décrire le produit logiciel

Décrire le produit logiciel

- Permettre aux utilisateurs de chercher un produit, le

sélectionner, le payer, et suivre la livraison.
- Permettre au système de gérer le stock, mettre à jour les

commandes, et envoyer des notifications.

22

---

## Cours 1 — Diapositive 22 : Identifier les

Identifier les

livrables

---

## Cours 1 — Diapositive 23 : Identifier les livrables

Identifier les livrables

Cahier des charges :
spécifications fonctionnelles et
techniques.

24

---

## Cours 1 — Diapositive 24 : Identifier les

Identifier les
livrables

Maquettes et interfaces
utilisateur : écrans de recherche,
panier, paiement.

25

---

## Cours 1 — Diapositive 25 : Identifier les livrables

Identifier les livrables

Base de données : schéma pour
produits, utilisateurs, commandes.

26

---

## Cours 1 — Diapositive 26 : Identifier les livrables

Identifier les livrables

Code : backend, frontend,
intégration paiement.

27

---

## Cours 1 — Diapositive 27 : Identifier les livrables

Identifier les livrables

Tests : unitaires, intégration,
fonctionnels.

28

---

## Cours 1 — Diapositive 28 : Identifier les livrables

Identifier les livrables

Documentation technique : pour
développeurs et administrateurs.

29

---

## Cours 1 — Diapositive 29 : Identifier les livrables

Identifier les livrables

Documentation utilisateur :
guides ou tutoriels pour les
clients.

30

---

## Cours 1 — Diapositive 30 : Identifier les tâches

Identifier les tâches

Pour chacun de ces livrables, quelles sont les tâches nécessaires ?

Livrable

Cahier de charges

Maquettes/interfaces

Base de données

Code

Tests

31

---

## Cours 1 — Diapositive 31 : Identifier les tâches

Identifier les tâches

Livrable
Tâches possible

Cahier de charges
Recueillir besoins, rédiger spécifications, valider avec les parties
prenantes
Maquettes/interfaces
Créer wireframes, designer les écrans, valider avec l’utilisateur

Base de données
Concevoir le schéma, créer tables et relations, tester intégrité

Code
Développer fonctionnalités recherche, panier, paiement ; intégrer
API de paiement ; coder notifications
Tests
Écrire tests unitaires, réaliser tests fonctionnels, tester
performance

32

---

## Cours 1 — Diapositive 32 : Discussion

Discussion

33

---

## Cours 1 — Diapositive 33 : Cycle de vie du développement logiciel

Cycle de vie du développement logiciel

34

---

## Cours 1 — Diapositive 34 : Qu’est-ce qu’un cycle de vie logiciel?

Qu’est-ce qu’un cycle de vie logiciel?

Le cycle de vie d’un logiciel est l’ensemble des étapes organisées par
lesquelles passe un logiciel, de sa conception initiale jusqu’à sa mise hors
service.

Pourquoi ?

- Structurer le travail
- Faciliter la collaboration
- Réduire les erreurs

35

---

## Cours 1 — Diapositive 35 : Pourquoi s’intéresser au cycle de vie ?

Pourquoi s’intéresser au cycle de vie ?

Un logiciel n’est pas produit au hasard. Il suit un processus structuré

Bien suivre ce processus permet de :

v Gagner du temps
v Réduire les coûts
v Assurer une meilleure qualité
v Mieux répartir les responsabilités

36

---

## Cours 1 — Diapositive 36 : Les phases du cycle

Les phases du cycle
de vie logiciel

37

---

## Cours 1 — Diapositive 37 : Phase 1 – Analyse des besoins

Phase 1 – Analyse des besoins

Identifier et rassembler les attentes des utilisateurs et les exigences du
projet. Cette phase permet de bien comprendre le problème à résoudre.

Exemple : discuter avec les utilisateurs pour savoir ce qu’ils veulent dans le
logiciel.

38

---

## Cours 1 — Diapositive 38 : Phase 1 – Sous-processus

Phase 1 – Sous-processus

- Collecte des exigences (entretiens, sondages, observation)

- Analyse de faisabilité fonctionnelle

- Rédaction du cahier des charges (spécifications fonctionnelles)
- Validation des besoins avec les parties prenantes

39

---

## Cours 1 — Diapositive 39 : Phase 2 – Planification

Phase 2 – Planification

Évaluer la faisabilité du projet, déterminer les ressources (temps, budget,
équipe) et anticiper les risques.

Exemple : estimer que le projet prendra 2 mois avec 3 développeurs.

40

---

## Cours 1 — Diapositive 40 : Phase 2 – Sous-processus

Phase 2 – Sous-processus

- Estimation des coûts et du temps

- Allocation des ressources humaines et matérielles

- Analyse des risques et élaboration de plans de mitigation
- Définition du calendrier de projet

- Création du plan de projet (planning, jalons, livrables)

41

---

## Cours 1 — Diapositive 41 : Phase 3 – Conception de logiciels

Phase 3 – Conception de logiciels

On transforme les besoins en une solution technique structurée :
architecture, maquettes, choix des outils.

Exemple : décider que l’application aura deux interfaces (admin et
utilisateur).

42

---

## Cours 1 — Diapositive 42 : Phase 3 – Sous-processus

Phase 3 – Sous-processus

- Conception de l’architecture logicielle

- Modélisation (UML, ERD, etc.)

- Conception de l’interface utilisateur (UI/UX)
- Choix des technologies et outils

- Rédaction des spécifications techniques

43

---

## Cours 1 — Diapositive 43 : Phase 4 – Développement

Phase 4 – Développement

Les programmeurs écrivent le code en suivant les décisions prises lors de la
conception.

Exemple : créer les pages de l’application et programmer les
fonctionnalités.

44

---

## Cours 1 — Diapositive 44 : Phase 4 – Sous-processus

Phase 4 – Sous-processus

- Programmation des fonctionnalités (back-end / front-end)

- Intégration des modules

- Suivi du code source (Git, gestion de version)
- Réunions techniques et résolution de blocages

- Revue de code (code review)

45

---

## Cours 1 — Diapositive 45 : Phase 5 – Test

Phase 5 – Test

Le logiciel est vérifié pour détecter et corriger les erreurs. On s’assure qu’il
fonctionne comme prévu.

Exemple : tester si les données sont bien enregistrées et si les erreurs sont
gérées.

46

---

## Cours 1 — Diapositive 46 : Phase 5 – Sous-processus

Phase 5 – Sous-processus

- Élaboration des plans de test

- Tests unitaires (chaque module séparément)

- Tests d’intégration (modules ensemble)
- Tests fonctionnels et de performance

- Rapport de bugs et validation des corrections

47

---

## Cours 1 — Diapositive 47 : Phase 6 – Déploiement

Phase 6 – Déploiement

Le logiciel est installé dans l’environnement réel pour être utilisé par les
utilisateurs.

Exemple : mettre l’application en ligne pour que l’école commence à
l’utiliser.

48

---

## Cours 1 — Diapositive 48 : Phase 6 – Sous-processus

Phase 6 – Sous-processus

- Préparation de l’environnement de production

- Livraison continue (CI/CD) ou installation manuelle

- Configuration des serveurs ou des plateformes
- Formation des utilisateurs finaux (si nécessaire)

- Mise en ligne ou distribution

49

---

## Cours 1 — Diapositive 49 : Phase 7 – Maintenance

Phase 7 – Maintenance

On corrige les problèmes découverts après la mise en service, on améliore
le logiciel et on ajoute de nouvelles fonctionnalités si nécessaire.

Exemple : ajouter une nouvelle option ou corriger un bug signalé par un
utilisateur.

50

---

## Cours 1 — Diapositive 50 : Phase 7 – Sous-processus

Phase 7 – Sous-processus

- Surveillance des performances et des erreurs

- Correction de bugs signalés

- Mises à jour de sécurité et techniques
- Améliorations fonctionnelles (nouveaux besoins)

- Support utilisateur (hotline, tickets)

51

---

## Cours 1 — Diapositive 51 : Phase

Phase
Description
Intervenants

- Analyste métier
- Client / Utilisateur final
- Chef de projet

1. Analyse des besoins
Identifier les besoins, attentes et contraintes du client

- Chef de projet
- Analyste fonctionnel
- Responsable qualité

2. Planification
Évaluer les ressources, délais, coûts et risques

- Architecte logiciel
- Développeur senior
- UX/UI designer

3. Conception
Concevoir l’architecture et les composants du logiciel

- Développeurs
- Intégrateurs
- Chef technique (Tech Lead)

4. Développement
Programmer et construire les modules fonctionnels

- Testeurs QA (Assurance qualité)
- Développeurs
- Analystes de test

5. Test
Vérifier la qualité, la stabilité et la conformité du code

- Ingénieur DevOps
- Administrateur système
- Chef de projet

6. Déploiement
Mettre le logiciel en production

- Équipe de support technique
- Développeurs
- Responsable produit

7. Maintenance
Corriger les bugs, améliorer ou mettre à jour le logiciel

52

---

## Cours 1 — Diapositive 52 : Question ?

Question ?

53

---

# Cours 5

_Source : C47_cours5.pdf — 75 diapositives/pages_

## Cours 5 — Diapositive 1 : Analyse et conception

Analyse et conception
d’une solution de données

Code du Cours : 420-C47-BB

Cours 5

Enseignant : Nadir, BOUAKEL
nadir.bouakel@bdeb.qc.ca

---

## Cours 5 — Diapositive 2 : Introduction à la donnée

Introduction à la donnée

Enjeux clés

Plan de la

Valorisation de la donnée

séance

Protection des données

Qualité des données

Formats de données

---

## Cours 5 — Diapositive 3 : Qu'est-ce que la donnée ?

Qu'est-ce que la donnée ?

La donnée est un ensemble d'informations collectées,
organisées et stockées, qui peut être utilisée pour générer
des connaissances, des décisions ou des actions.

- Elle peut être sous différentes formes : chiffres, textes,

images, vidéos, etc.
3

---

## Cours 5 — Diapositive 4 : Le rôle de la donnée dans

Le rôle de la donnée dans
l'entreprise

Pourquoi la donnée est-elle importante ?

- Décisions basées sur les faits : Aide à prendre des

décisions plus éclairées

- Optimisation des processus : Permet d'améliorer

l'efficacité

produits innovants
4

- Création de valeur : Peut être transformée en services ou

---

## Cours 5 — Diapositive 5 : Enjeux autour de la donnée

Enjeux autour de la donnée

Les enjeux autour de la donnée sont des défis et des
responsabilités liés à la manière dont elle est collectée,
utilisée, protégée et valorisée dans une organisation. Ces
enjeux incluent la protection des données, la gestion de leur
- ualité, et leur gouvernance.

5

---

## Cours 5 — Diapositive 6 : Enjeux clés autour de la

Enjeux clés autour de la
donnée

- Valorisation des données : Exploiter les données pour

créer de la valeur (ex. modèles prédictifs, rapports
dynamiques, tableaux de bord)

- Protection des données : Garantir la sécurité et la

confidentialité des données sensibles.

complètes, exactes, actuelles et fiables.
6

- Qualité des données : Assurer que les données sont

---

## Cours 5 — Diapositive 7 : Valorisation de

Valorisation de

la donnée

7

---

## Cours 5 — Diapositive 8 : Valorisation de la donnée

Valorisation de la donnée

La valorisation de la donnée consiste à transformer des données brutes en
informations utiles pour créer de la valeur. Cette valeur peut être
économique, stratégique ou opérationnelle.

8

---

## Cours 5 — Diapositive 9 : Donnée brute vs Information

Donnée brute vs Information

Donnée brute : chiffre ou texte sans contexte (ex : 125)

Information : donnée interprétée (ex : 125 ventes aujourd’hui)

La valorisation commence par donner du sens aux données

9

---

## Cours 5 — Diapositive 10 : De la donnée à la décision

De la donnée à la décision

Processus simplifié :

Collecte → Stockage → Analyse → Visualisation → Décision

La valorisation se situe principalement dans l’analyse et la restitution.

10

---

## Cours 5 — Diapositive 11 : Business Intelligence (BI)

Business Intelligence (BI)

La Business Intelligence regroupe les outils et méthodes permettant
d’analyser les données pour aider à la décision.
Exemples d’outils : Power BI, Tableau, Looker.

11

---

## Cours 5 — Diapositive 12 : Sans titre

12

---

## Cours 5 — Diapositive 13 : Tableaux de bord (Dashboard)

Tableaux de bord (Dashboard)

Un tableau de bord est une interface visuelle qui présente les indicateurs
clés d’une activité en temps réel ou périodiquement.

13

---

## Cours 5 — Diapositive 14 : Tableaux de bord (Dashboard)

Tableaux de bord (Dashboard)

14

---

## Cours 5 — Diapositive 15 : Objectif d’un tableau de bord

Objectif d’un tableau de bord

- Suivre la performance

- Détecter des anomalies

- Comparer des périodes
- Faciliter la prise de décision rapide

- Centraliser l’information importante

15

---

## Cours 5 — Diapositive 16 : Indicateurs clés (KPI)

Indicateurs clés (KPI)

Un KPI (Key Performance Indicator) est un indicateur mesurable
permettant d’évaluer une performance.
Exemples :

- Chiffre d’affaires

- Taux de conversion

- Temps moyen de traitement

16

---

## Cours 5 — Diapositive 17 : Visualisation de données

Visualisation de données

La visualisation consiste à représenter les données sous forme graphique.

- Graphiques en barres

- Courbes
- Diagrammes circulaires

- Cartes interactives

17

---

## Cours 5 — Diapositive 18 : Sans titre

18

---

## Cours 5 — Diapositive 19 : Analyse descriptive

Analyse descriptive

Elle résume les
données historiques

Répond à la question :

(rapports,
statistiques).

Que s’est-il passé ?

19

---

## Cours 5 — Diapositive 20 : Analyse diagnostique

Analyse diagnostique

Répond à la

Elle cherche les

- uestion :
Pourquoi cela s’est-

causes d’un
événement à partir

il produit ?

des données.

20

---

## Cours 5 — Diapositive 21 : Analyse prédictive

Analyse prédictive

Répond à la question :

Elle utilise des
modèles statistiques

Que va-t-il
probablement se

ou du machine

passer ?

learning.

21

---

## Cours 5 — Diapositive 22 : Modèle prédictif

Modèle prédictif

Un modèle prédictif est un algorithme qui utilise des données passées pour
anticiper des résultats futurs.

22

---

## Cours 5 — Diapositive 23 : Exemple de modèles prédictifs

Exemple de modèles prédictifs

vPrévision des ventes

vDétection de fraude

vRecommandation de produits
vPrévision de panne

23

---

## Cours 5 — Diapositive 24 : Machine Learning

Machine Learning

Le Machine Learning est une branche de l’intelligence artificielle permettant
aux systèmes d’apprendre à partir des données sans être explicitement
programmés pour chaque règle.

24

---

## Cours 5 — Diapositive 25 : Valorisaiton des donées en temps réel

Valorisaiton des donées en temps réel

Certaines données sont exploitées immédiatement après leur collecte.

- Recommandations instantanées

- Publicité ciblée

- Détection de transactions frauduleuses

25

---

## Cours 5 — Diapositive 26 : Monétisation des données

Monétisation des données

La monétisation consiste à générer un revenu direct à partir des données.

- Vente de données anonymisées

- API payantes

- Services basés sur l’analyse de données

26

---

## Cours 5 — Diapositive 27 : Personnalisation grâce aux données

Personnalisation grâce aux données

Les données permettent d’adapter un service à un utilisateur.

- Recommandations Netflix

- Suggestions Amazon

- Publicités ciblées

27

---

## Cours 5 — Diapositive 28 : Conditions pour bien valoriser la donnée

Conditions pour bien valoriser la donnée

üDonnées de qualité

üDonnées accessibles

üOutils adaptés
üCompétences en analyse

üRespect des règles de protection

28

---

## Cours 5 — Diapositive 29 : Protection des données

Protection des données

29

---

## Cours 5 — Diapositive 30 : Protection des données

Protection des données

La protection des données regroupe l’ensemble des mesures techniques et
organisationnelles mises en place pour sécuriser les données contre les
risques.

30

---

## Cours 5 — Diapositive 31 : Pourquoi protéger les données ?

Pourquoi protéger les données ?

- Éviter les fuites d’informations
- Protéger la vie privée des utilisateurs
- Éviter les sanctions légales
- Maintenir la confiance des clients
- Assurer la continuité des services

31

---

## Cours 5 — Diapositive 32 : Les risques liés aux données

Les risques liés aux données

vPiratage informatique

vErreur humaine

vPerte ou vol de matériel
vVirus / ransomware

vMauvaise configuration système

32

---

## Cours 5 — Diapositive 33 : La triade CIA

La triade CIA

La sécurité des données repose sur trois
piliers :
- Confidentialité

- Intégrité

- Disponibilité

33

---

## Cours 5 — Diapositive 34 : Confidentialité

Confidentialité

La confidentialité signifie que seules les personnes autorisées peuvent
accéder aux données.

34

---

## Cours 5 — Diapositive 35 : Moyens d’assurer la confidentialité

Moyens d’assurer la confidentialité

Authentification (mot de passe, MFA)

Gestion des droits d’accès
Chiffrement des données

Réseaux sécurisés (VPN)

Sensibilisation des utilisateurs

35

---

## Cours 5 — Diapositive 36 : Intégrité

Intégrité

L’intégrité garantit que les données ne sont pas modifiées ou altérées de
manière non autorisée.

36

---

## Cours 5 — Diapositive 37 : Mécanismes assurant l’intégrité

Mécanismes assurant l’intégrité

- Hash (empreinte numérique)

- Signature numérique
- Journalisation des actions (logs)

- Contrôles de validation

- Sauvegardes régulières

37

---

## Cours 5 — Diapositive 38 : Disponibilité

Disponibilité

La disponibilité garantit que les données sont accessibles quand on en a
besoin.

38

---

## Cours 5 — Diapositive 39 : Assurer la disponibilité

Assurer la disponibilité

- Sauvegardes automatiques

- Systèmes redondants
- Plan de reprise d’activité (PRA)

- Surveillance des serveurs

- Protection contre les attaques DDoS

39

---

## Cours 5 — Diapositive 40 : Données personnelles

Données personnelles

Une donnée personnelle est toute information permettant d’identifier une personne
directement ou indirectement.

Exemples : nom, email, numéro de téléphone, adresse IP.

40

---

## Cours 5 — Diapositive 41 : Anonymisation

Anonymisation

L’anonymisation consiste à transformer des données pour qu’il soit impossible
d’identifier une personne.

41

---

## Cours 5 — Diapositive 42 : Chiffrement

Chiffrement

Le chiffrement transforme une donnée lisible en donnée illisible sans clé de
déchiffrement.

42

---

## Cours 5 — Diapositive 43 : Gestion des accès (IAM)

Gestion des accès (IAM)

IAM = Identity and Access Management

Permet de gérer :

- Les utilisateurs

- Les rôles
- Les permissions

- Les authentifications

43

---

## Cours 5 — Diapositive 44 : Principe du moindre privilège

Principe du moindre privilège

Un utilisateur ne doit avoir accès qu’aux données strictement nécessaires à sa
mission.

44

---

## Cours 5 — Diapositive 45 : Qualité des données

Qualité des données

45

---

## Cours 5 — Diapositive 46 : Qualité des données

Qualité des données

La qualité des données mesure à quel point les données sont fiables, correctes et
utilisables pour un objectif donné.

46

---

## Cours 5 — Diapositive 47 : Pourquoi la qualité est importante ?

Pourquoi la qualité est importante ?

Éviter les erreurs de décision

Améliorer la performance des analyses
Réduire les coûts liés aux corrections

Renforcer la confiance dans les systèmes
Assurer la conformité réglementaire

47

---

## Cours 5 — Diapositive 48 : Mauvaise qualité – Exemples

Mauvaise qualité – Exemples

- Champs vides

- Fautes de frappe

- Données dupliquées
- Dates incorrectes

- Formats incohérents

48

---

## Cours 5 — Diapositive 49 : Complétude

Complétude

La complétude mesure si toutes les données nécessaires sont présentes.

- Exemple : un client sans adresse email = donnée incomplète.

49

---

## Cours 5 — Diapositive 50 : Exactitude

Exactitude

L’exactitude indique si la donnée est correcte par rapport à la réalité.

- Exemple : âge = 250 ans → donnée inexacte.

50

---

## Cours 5 — Diapositive 51 : Cohérence

Cohérence

La cohérence signifie que les données ne se contredisent pas entre différents
systèmes.

- Exemple : deux bases affichent des montants différents pour le même client.

51

---

## Cours 5 — Diapositive 52 : Règles de validation

Règles de validation

Les règles de validation permettent de contrôler automatiquement la qualité.

Exemples :

- Champ obligatoire

- Format spécifique

- Valeur minimale / maximale

52

---

## Cours 5 — Diapositive 53 : Audit de qualité des données

Audit de qualité des données

Un audit consiste à analyser un ensemble de données pour mesurer leur niveau de
- ualité.

53

---

## Cours 5 — Diapositive 54 : Indicateurs de qualité

Indicateurs de qualité

Exemples d’indicateurs mesurables :

- % de champs complétés

- % d’erreurs détectées

- Nombre de doublons
- Taux de conformité aux règles

54

---

## Cours 5 — Diapositive 55 : Impact d’une mauvaise qualité

Impact d’une mauvaise qualité

- Analyses faussées

- Modèles prédictifs inefficaces

- Perte de temps

- Mauvaise expérience utilisateur
- Décisions stratégiques erronées

55

---

## Cours 5 — Diapositive 56 : Amélioration continue

Amélioration continue

- La qualité des données est

un processus continu :

56

---

## Cours 5 — Diapositive 57 : Formats de

Formats de
données

57

---

## Cours 5 — Diapositive 58 : Données structurées

Données structurées

Les données structurées sont organisées dans des formats bien définis,
généralement sous forme de tableaux ou de bases de données. Elles
suivent un modèle précis, ce qui les rend faciles à traiter et à analyser.

58

---

## Cours 5 — Diapositive 59 : JSON (JavaScript

JSON (JavaScript

JSON est un format léger et lisible
pour les humains, souvent utilisé
pour échanger des données entre
serveurs et applications web.

Object Notation)

59

---

## Cours 5 — Diapositive 60 : JSON (JavaScript

JSON (JavaScript

Object Notation)

60

---

## Cours 5 — Diapositive 61 : XML est un format textuel

XML est un format textuel
extensible qui définit des règles
pour l’encodage des documents. Il
est plus verbeux que JSON mais
très utilisé dans des systèmes plus
anciens ou dans les échanges B2B.

XML (Extensible
Markup Language)

61

---

## Cours 5 — Diapositive 62 : XML (Extensible

XML (Extensible
Markup Language)

62

---

## Cours 5 — Diapositive 63 : YAML est un format lisible par

YAML est un format lisible par
l’homme, souvent utilisé pour la
configuration d’applications ou la
gestion de données dans des
scripts. Il est plus simple que JSON
et XML, mais moins universel.

YAML (YAML Ain’t
Markup Language)

63

---

## Cours 5 — Diapositive 64 : Fichiers logs

Fichiers logs

64

---

## Cours 5 — Diapositive 65 : Les fichiers de configuration contiennent des

Les fichiers de configuration contiennent des
paramètres définissant le comportement d’un
logiciel ou d’un système. Ils peuvent être en
XML, JSON, ou dans des formats spécifiques
comme YAML.

Fichiers de
configuration

65

---

## Cours 5 — Diapositive 66 : Fichiers de configuration (YAML)

Fichiers de configuration (YAML)

66

---

## Cours 5 — Diapositive 67 : Données non structurées

Données non structurées

Les données non structurées ne suivent aucun format pré-défini et
peuvent être sous forme de texte libre, d'images, de vidéos, etc.
Elles sont beaucoup plus difficiles à analyser, mais représentent
une grande partie des données générées aujourd'hui.

67

---

## Cours 5 — Diapositive 68 : Texte libre (Emails, documents,…)

Texte libre (Emails, documents,…)

68
Les emails et les documents (Word, PDF) sont des exemples de données
non structurées. Bien qu'ils contiennent des informations précieuses, leur
analyse nécessite souvent des outils de traitement du langage naturel.

---

## Cours 5 — Diapositive 69 : Images

Images

69
Les images sont également des données non structurées. Elles
nécessitent des algorithmes d’analyse d’image pour extraire des
informations (reconnaissance d'objets, analyse de contenu).

---

## Cours 5 — Diapositive 70 : Vidéos et enregistrements audio

Vidéos et enregistrements audio

70
Les vidéos et audios sont des flux continus de données multimédia. Leur
traitement inclut des techniques comme l’analyse de contenu vidéo et
audio (ex : détection d’objets, reconnaissance vocale).

---

## Cours 5 — Diapositive 71 : Données brutes

Données brutes

Les données brutes proviennent directement de capteurs, de systèmes
transactionnels ou d’API externes. Elles sont généralement collectées en
temps réel et doivent être transformées avant analyse.

71

---

## Cours 5 — Diapositive 72 : Capteurs IoT (Internet of Things)

Capteurs IoT (Internet of Things)

72
Les capteurs IoT génèrent des données en temps réel, souvent sous forme
de nombres ou de séries temporelles, qui peuvent être analysées pour
suivre des paramètres comme la température, l'humidité, ou le
mouvement.

---

## Cours 5 — Diapositive 73 : Systèmes transactionnels

Systèmes transactionnels

73
Les systèmes transactionnels (ex : banques, plateformes e-commerce)
génèrent des données brutes concernant les transactions, les paiements,
les achats, etc.

---

## Cours 5 — Diapositive 74 : Données binaires

Données binaires

74
Les données binaires sont des fichiers contenant des informations
codées en binaire (0 et 1). Elles sont utilisées pour des images, des
vidéos, des fichiers compressés ou des exécutables.

---

## Cours 5 — Diapositive 75 : Examen INTRA

Examen INTRA

75

---

# Cours 7

_Source : C47_cours7.pdf — 47 diapositives/pages_

## Cours 7 — Diapositive 1 : Analyse et conception

Analyse et conception
d’une solution de données

Code du Cours : 420-C47-BB

Cours 7

Enseignant : Nadir, BOUAKEL
nadir.bouakel@bdeb.qc.ca

---

## Cours 7 — Diapositive 2 : - Cycle de vie de la donnée

- Cycle de vie de la donnée
- Processus de collecte des besoins
- Méthodes et techniques de collecte
- Outils de documentation des

exigences
- Outils de documentation

Plan de la séance

collaboratifs
- Principes de qualité dans la collecte
- Structuration de l'information

collectée

2

---

## Cours 7 — Diapositive 3 : Cycle de vie de

Cycle de vie de

la donnée

3

---

## Cours 7 — Diapositive 4 : Cycle de vie de la donnée

Cycle de vie de la donnée

4

---

## Cours 7 — Diapositive 5 : Cycle de vie de la donnée

Cycle de vie de la donnée

Le cycle de vie de la donnée désigne l'ensemble des étapes par lesquelles
passe une donnée, depuis sa création jusqu'à sa suppression ou son
archivage. Chaque étape implique des responsabilités spécifiques en
matière de gestion, de qualité et de sécurité.

5

---

## Cours 7 — Diapositive 6 : Création et acquisition

Création et acquisition

- Création : la donnée est générée pour la première fois (saisie manuelle,

capteur, transaction, formulaire).
- Acquisition : la donnée est obtenue depuis une source externe (API,

partenaire, achat de données, import de fichier).

C'est à cette étape que la qualité et la provenance doivent être définies et
documentées.

6

---

## Cours 7 — Diapositive 7 : Nettoyage et transformation

Nettoyage et transformation

- Nettoyage : correction des erreurs, suppression des doublons,

traitement des valeurs manquantes.
- Transformation : conversion dans un format utilisable, agrégation,

normalisation, enrichissement.

Cette étape est essentielle avant toute analyse ou exploitation des
données.

7

---

## Cours 7 — Diapositive 8 : Stockage

Stockage

- Les données sont conservées dans des systèmes adaptés

- Le stockage doit garantir la sécurité, la durabilité et l'accessibilité des

données.

- La structure de stockage dépend du volume, de la fréquence d'accès et

des besoins d'analyse.

8

---

## Cours 7 — Diapositive 9 : Stockage – Base de données

Stockage – Base de données

9

---

## Cours 7 — Diapositive 10 : Stockage - Entreposage de données

Stockage - Entreposage de données

10

---

## Cours 7 — Diapositive 11 : Stockage – Lac de données

Stockage – Lac de données

11

---

## Cours 7 — Diapositive 12 : Exploitation et valorisation

Exploitation et valorisation

- Les données sont analysées, visualisées et utilisées pour prendre des

décisions.
- Exemples : tableaux de bord, rapports, modèles prédictifs,

recommandations.

- La valorisation maximise la valeur économique, stratégique ou

opérationnelle des données.

12

---

## Cours 7 — Diapositive 13 : Exploitation et valorisation

Exploitation et valorisation

13

---

## Cours 7 — Diapositive 14 : Archivage ou suppression

Archivage ou suppression

- Archivage : les données moins utilisées sont déplacées vers un stockage

à faible coût, mais restent accessibles si nécessaire.
- Suppression : les données inutiles ou périmées sont effacées de

manière sécurisée.

Le respect des délais légaux de conservation est obligatoire (ex. : RGPD,
Loi 25).

14

---

## Cours 7 — Diapositive 15 : Surveillance et auditabilité

Surveillance et auditabilité

- Surveillance : suivi continu de l'utilisation, de la qualité et de la sécurité

des données tout au long de leur cycle de vie.
- Auditabilité : capacité à retracer les actions effectuées sur les données

(qui a accédé, quand, pourquoi).

Les journaux d'audit (logs) sont essentiels pour la conformité
réglementaire et la détection d'anomalies.

15

---

## Cours 7 — Diapositive 16 : Processus de collecte

Processus de collecte

des besoins

16

---

## Cours 7 — Diapositive 17 : Processus de collecte des

Processus de collecte des
besoins

La collecte des besoins est une étape fondamentale dans la conception d'une
solution de données. Elle consiste à comprendre les objectifs d'affaires, les
processus existants et les attentes des parties prenantes afin de définir précisément
ce que la solution doit accomplir.

17

---

## Cours 7 — Diapositive 18 : Identifier un processus de

Identifier un processus de
collecte approprié

- Analyser le contexte organisationnel : taille de l'équipe, complexité du projet,

contraintes de temps.

- Choisir une approche itérative ou séquentielle selon la nature du projet.

- Impliquer les bons interlocuteurs dès le départ : analystes, gestionnaires,

utilisateurs finaux.

- Définir la portée de la collecte : quels processus couvrir, quelles données sont

concernées.

18

---

## Cours 7 — Diapositive 19 : Comprendre les processus

Comprendre les processus

- Observer et documenter les processus métiers actuels (flux d'information, étapes,

acteurs).

- Identifier les sources de données existantes et les systèmes en place.

- Repérer les points de friction, les lacunes et les opportunités d'amélioration.
- Cartographier les flux d'information entre les systèmes et les équipes.

19

---

## Cours 7 — Diapositive 20 : Identifier ce que la solution doit

Identifier ce que la solution doit
accomplir

- Définir les objectifs d'affaires : que veut atteindre l'organisation avec cette solution ?

- Identifier les indicateurs de succès : comment saura-t-on que la solution fonctionne

?

- Distinguer les besoins prioritaires des besoins secondaires.
- Aligner les attentes de toutes les parties prenantes autour d'une vision commune.

20

---

## Cours 7 — Diapositive 21 : Méthodes et

Méthodes et
techniques de collecte

21

---

## Cours 7 — Diapositive 22 : Méthodes de collecte des

Méthodes de collecte des
besoins

- Les méthodes de collecte permettent d'obtenir une compréhension

approfondie et structurée des besoins.
- Il est recommandé d'utiliser plusieurs méthodes complémentaires pour

valider les informations recueillies.

- Le choix des méthodes dépend du contexte, du nombre de parties prenantes

et du temps disponible.

22

---

## Cours 7 — Diapositive 23 : Entrevues individuelles

Entrevues individuelles

- Rencontre en tête-à-tête avec un interlocuteur clé (gestionnaire, utilisateur, expert).

- Permet d'obtenir des informations détaillées et d'approfondir des points

spécifiques.

- Favorise la confiance et l'expression libre des besoins réels.
- Nécessite une préparation rigoureuse : liste de questions, objectifs clairs, prise de

notes structurée.

23

---

## Cours 7 — Diapositive 24 : Focus groups

Focus groups

- Réunion de groupe avec plusieurs parties prenantes ayant des perspectives

différentes.

- Favorise les échanges, le débat et la convergence vers des besoins communs.

- Utile pour valider des hypothèses ou explorer des solutions en groupe.

Risque : les participants les plus influents peuvent dominer les discussions.

24

---

## Cours 7 — Diapositive 25 : Réunions de discussion

Réunions de discussion

- Séances structurées avec l'équipe projet et les représentants du client.

- Permettent de partager l'avancement, de valider des livrables et de prendre des

décisions.

- Doivent être planifiées avec un ordre du jour clair et un compte rendu formalisé.
- Fréquentes dans les projets agiles (sprint planning, revues de sprint).

25

---

## Cours 7 — Diapositive 26 : Analyse de l'existant

Analyse de l'existant

- Étude des systèmes, outils, bases de données et processus déjà en place.

- Permet d'identifier les forces et faiblesses de la situation actuelle.
- Évite de recréer l'existant et d'identifier les intégrations nécessaires.

- Inclut l'analyse des données actuelles : structure, qualité, volumétrie.

26

---

## Cours 7 — Diapositive 27 : Questionnaires/sondages

Questionnaires/sondages

- Outil idéal pour collecter des informations auprès d'un grand nombre de personnes.

- Permet de quantifier les besoins et de prioriser les fonctionnalités.
- Doit être court, clair et ciblé pour obtenir des réponses exploitables.

- Exemples d'outils : Google Forms, Microsoft Forms, SurveyMonkey.

27

---

## Cours 7 — Diapositive 28 : Analyse documentaire

Analyse documentaire

- Étude des documents existants : rapports, procédures, cahiers des charges,

manuels.

- Permet de comprendre le contexte sans solliciter directement les parties prenantes.

- Complète les informations obtenues lors des entrevues et réunions.
- Sources typiques : rapports annuels, schémas de bases de données, diagrammes

de processus.

28

---

## Cours 7 — Diapositive 29 : Structuration de

Structuration de
l'information collectée

29

---

## Cours 7 — Diapositive 30 : Structuration de l'information

Structuration de l'information
collectée

Une fois les besoins collectés, il est essentiel de les organiser et de les classifier pour
- ue l'équipe technique puisse concevoir et développer la solution de données de
manière efficace.

30

---

## Cours 7 — Diapositive 31 : Contraintes techniques

Contraintes techniques

- Technologies existantes : la solution doit s'intégrer aux systèmes déjà en place.

- Formats de données : compatibilité avec les formats utilisés (CSV, JSON, SQL, etc.).
- Compatibilité : respect des normes et protocoles en vigueur dans l'organisation.

- Performance : temps de réponse, volume de données à traiter, disponibilité requise.

31

---

## Cours 7 — Diapositive 32 : Contraintes organisationnelles

Contraintes organisationnelles

- Budget : ressources financières disponibles pour la réalisation du projet.

- Ressources humaines : disponibilité et compétences des équipes impliquées.
- Calendrier : délais imposés, jalons et dates de livraison.

- Culture d'entreprise : adoption des outils, résistance au changement, habitudes de

travail.

32

---

## Cours 7 — Diapositive 33 : Contraintes juridiques et

Contraintes juridiques et
réglementaires

- Protection des données personnelles : respect du RGPD (Europe) ou de la Loi 25

(Québec).

- Localisation des données : certaines données ne peuvent pas être hébergées hors

du territoire.

- Conservation des données : délais légaux de conservation selon le secteur

d'activité.

- Accès et audit : obligation de pouvoir retracer l'utilisation des données sensibles.

33

---

## Cours 7 — Diapositive 34 : Outils de

Outils de
documentation des

exigences

34

---

## Cours 7 — Diapositive 35 : Outils de documentation des

Outils de documentation des
exigences

- Documenter les besoins de manière structurée est essentiel pour

assurer la traçabilité et la communication.
- Plusieurs outils et gabarits permettent de formaliser les exigences de

façon claire et exploitable.

- Un bon document d'exigences facilite la validation avec le client et le

travail de l'équipe technique.

35

---

## Cours 7 — Diapositive 36 : Fiches de besoins

Fiches de besoins

- Document structuré décrivant un besoin précis identifié lors de la

collecte.
- Contient généralement : le titre, la description, la priorité, le responsable

et le statut.

- Permet de suivre l'évolution de chaque besoin tout au long du projet.

- Facilite la communication entre les analystes, les développeurs et les

clients.

36

---

## Cours 7 — Diapositive 37 : Canevas de questions

Canevas de questions

- Gabarit préparé à l'avance pour guider les entrevues ou les ateliers de

collecte.
- Assure que tous les thèmes importants sont abordés avec chaque

interlocuteur.

- Permet de comparer facilement les réponses de différents participants.

- Exemples de thèmes : processus actuels, problèmes rencontrés,

attentes, contraintes.

37

---

## Cours 7 — Diapositive 38 : Gabarits de prise de notes

Gabarits de prise de notes

- Structure prédéfinie pour consigner les informations collectées lors des

réunions.
- Inclut : date, participants, décisions prises, actions à réaliser, points

ouverts.

- Facilite la rédaction de comptes rendus et la transmission de

l'information.

- Assure la cohérence dans la documentation tout au long du projet.

38

---

## Cours 7 — Diapositive 39 : Outils de

Outils de
documentation

collaboratifs

39

---

## Cours 7 — Diapositive 40 : Outils de documentation

Outils de documentation
collaboratifs

- Les outils collaboratifs permettent aux équipes de documenter, partager

et mettre à jour les exigences en temps réel. Ils centralisent l'information
et facilitent la communication entre toutes les parties prenantes du
projet.

40

---

## Cours 7 — Diapositive 41 : JIRA et confluence

JIRA et confluence

41

---

## Cours 7 — Diapositive 42 : Microsoft OneNote

Microsoft OneNote

42

---

## Cours 7 — Diapositive 43 : Principes de

Principes de
- ualité dans la

collecte

43

---

## Cours 7 — Diapositive 44 : Principes de qualité dans la collecte

Principes de qualité dans la collecte

La qualité du processus de collecte détermine directement la qualité de la
solution de données qui sera développée. Des besoins mal collectés ou
mal documentés entraînent des erreurs coûteuses en phase de
réalisation.

44

---

## Cours 7 — Diapositive 45 : Validation continue auprès du client

Validation continue auprès du client

- Soumettre régulièrement les résultats

de la collecte aux parties prenantes
pour validation.

- Corriger rapidement les

incompréhensions ou les oublis avant
- u'ils ne deviennent des problèmes.

45

---

## Cours 7 — Diapositive 46 : Synthèse claire et structurée des

Synthèse claire et structurée des
besoins

Organiser les besoins de façon logique, utiliser un vocabulaire commun,
prioriser selon l’impact sur les objectifs, et présenter la synthèse
visuellement avec tableaux,

46

---

## Cours 7 — Diapositive 47 : Autres principes de qualité

Autres principes de qualité

- Exhaustivité : s'assurer que tous les besoins ont été identifiés et

documentés.
- Traçabilité : lier chaque exigence à un besoin d'affaires ou à une

contrainte identifiée.

- Non-ambiguïté : formuler les besoins de façon précise, sans

interprétation possible.

- Cohérence : vérifier que les besoins ne se contredisent pas entre eux.

47

---

# Cours 8

_Source : C47_cours8.pdf — 90 diapositives/pages_

## Cours 8 — Diapositive 1 : Analyse et conception

Analyse et conception
d’une solution de données

Code du Cours : 420-C47-BB

Cours 8

Enseignant : Nadir, BOUAKEL
nadir.bouakel@bdeb.qc.ca

---

## Cours 8 — Diapositive 2 : Architectures

Architectures

---

## Cours 8 — Diapositive 3 : Concepts fondamentaux

Concepts fondamentaux
d'architecture

Une architecture de données est un plan structuré qui définit comment
les données sont collectées, stockées, transformées et distribuées au
sein d'une organisation. Elle établit les règles, les standards et les
composants nécessaires pour gérer e>icacement l'information.

---

## Cours 8 — Diapositive 4 : Les composantes d'une architecture

Les composantes d'une architecture

- Les sources de données (bases de données, API, fichiers)

- les mécanismes de traitement et transformation, les systèmes de

stockage, et les interfaces d'accès.

---

## Cours 8 — Diapositive 5 : Pourquoi les architectures sont

Pourquoi les architectures sont
importantes

- Assurer la cohérence des données

- Optimiser les performances, de garantir la sécurité et la conformité
- Elles facilitent également l'évolution des systèmes

- Réduisent les coûts de maintenance en évitant la duplication et la

redondance.

---

## Cours 8 — Diapositive 6 : Architecture client-serveur

Architecture client-serveur

L'architecture client-serveur est un modèle où les tâches sont réparties
entre deux types d'entités :

- le client qui demande des services

- le serveur qui fournit ces services.

Cette séparation permet de centraliser les ressources et de faciliter leur
partage entre plusieurs utilisateurs.

---

## Cours 8 — Diapositive 7 : Rôles du client et du serveur

Rôles du client et du serveur

---

## Cours 8 — Diapositive 8 : Avantages et inconvénients

Avantages et inconvénients

Avantages : centralisation des données, maintenance simplifiée, sécurité
renforcée, partage de ressources.

Inconvénients : point de défaillance unique si le serveur tombe,
dépendance au réseau, scalabilité limitée si le serveur est surchargé.

---

## Cours 8 — Diapositive 9 : Exemple d'architecture client-

Exemple d'architecture client-
serveur

---

## Cours 8 — Diapositive 10 : Architecture 3 tiers - Définition

Architecture 3 tiers - Définition

L'architecture 3 tiers (three-tier) est une évolution de l'architecture client-
serveur qui sépare l'application en trois couches distinctes : présentation,
logique métier, et données.

Cette séparation améliore la modularité, la maintenabilité et permet de faire
évoluer chaque couche indépendamment.

---

## Cours 8 — Diapositive 11 : Couche présentation

Couche présentation

- Est l'interface avec laquelle

l'utilisateur interagit directement.

---

## Cours 8 — Diapositive 12 : Couche logique/applicative

Couche logique/applicative

- Contient toute la logique de

traitement de l'application

---

## Cours 8 — Diapositive 13 : Couche données

Couche données

La couche données gère le stockage, la
récupération et la persistance des
informations. Elle comprend les systèmes
de gestion de bases de données (SGBD) et
les mécanismes d'accès aux données

---

## Cours 8 — Diapositive 14 : Exemple d'architecture 3 tiers

Exemple d'architecture 3 tiers

---

## Cours 8 — Diapositive 15 : HTTP

HTTP

- HTTP est le protocole de communication qui

permet à votre navigateur web de demander
et de recevoir des pages internet depuis un
serveur.

- Il fonctionne sur un cycle simple de requête

---

## Cours 8 — Diapositive 16 : HTTP

HTTP

---

## Cours 8 — Diapositive 17 : Architecture REST

Architecture REST

- REST (Representational State Transfer) est un style d'architecture pour

les systèmes distribués basé sur le protocole HTTP.

- Elle définit un ensemble de contraintes pour créer des services web

- ui soient simples, scalables et interopérables.

- REST privilégie l'utilisation des méthodes HTTP standard.

---

## Cours 8 — Diapositive 18 : Principes de base de REST

Principes de base de REST

Les principes REST incluent : l'interface uniforme (utilisation standard de
HTTP), la séparation client-serveur, l'absence d'état (stateless - chaque
requête contient toute l'information nécessaire), la possibilité de mise en
cache, et l'architecture en couches. Ces principes garantissent la
simplicité et la performance.

---

## Cours 8 — Diapositive 19 : Concept de ressources

Concept de ressources

Dans REST, tout est une ressource identifiée par une URL unique (URI).

On utilise les verbes HTTP pour manipuler ces ressources :

- GET (lire)

- POST (créer)

- PUT (modifier)

- DELETE (supprimer).

---

## Cours 8 — Diapositive 20 : Exemple

Exemple
d'API
REST

---

## Cours 8 — Diapositive 21 : Architecture WebSockets

Architecture WebSockets

---

## Cours 8 — Diapositive 22 : Architectures

Architectures
classiques de
solutions de données

---

## Cours 8 — Diapositive 23 : Architectures centralisées

Architectures centralisées

- Point unique : Données et traitements regroupés sur un seul serveur.

- Accès commun : Tous les utilisateurs et applications passent par ce

centre.

- Avantages : Cohérence maximale et contrôle simplifié des

ressources.

---

## Cours 8 — Diapositive 24 : Caractéristiques et cas d'usage

Caractéristiques et cas d'usage

Caractéristiques : contrôle total des données, sécurité simplifiée,
cohérence garantie, administration centralisée. Cas d'usage typiques :
systèmes bancaires, ERP d'entreprise, applications nécessitant une forte
cohérence transactionnelle, environnements hautement réglementés.

---

## Cours 8 — Diapositive 25 : Exemple

Exemple
d'architecture
centralisée

---

## Cours 8 — Diapositive 26 : Architectures fédérées

Architectures fédérées

Une architecture fédérée distribue les données et les traitements sur
plusieurs systèmes autonomes qui collaborent tout en maintenant leur
indépendance.

---

## Cours 8 — Diapositive 27 : Avantages et défis

Avantages et défis

Avantages : autonomie des départements, pas de point unique de
défaillance, meilleure scalabilité.

Défis : complexité accrue de gestion, synchronisation des données
di>icile, cohérence éventuelle plutôt qu'immédiate, gouvernance
distribuée plus complexe.

---

## Cours 8 — Diapositive 28 : Exemple

Exemple
d'architecture

fédérée

---

## Cours 8 — Diapositive 29 : Architectures microservices

Architectures microservices

L'architecture microservices décompose une application en petits
services indépendants, chacun responsable d'une fonction métier
spécifique. Chaque microservice possède sa propre base de données,
peut être développé et déployé indépendamment, et communique avec
les autres via des API bien définies.

---

## Cours 8 — Diapositive 30 : Caractéristiques des microservices

Caractéristiques des microservices

v Indépendance de déploiement

v Base de données par service

v Communication via API (REST, messages)
v Technologies hétérogènes possibles,

v Équipes autonomes par service

---

## Cours 8 — Diapositive 31 : Avantages et défis

Avantages et défis

Avantages : agilité de développement, scalabilité fine, résilience accrue,
adoption de nouvelles technologies facilitée.

Défis : complexité opérationnelle, gestion distribuée, transactions
distribuées difficiles, monitoring complexe, latence réseau.

---

## Cours 8 — Diapositive 32 : Exemple

Exemple
d'architecture
microservices

---

## Cours 8 — Diapositive 33 : Architectures

Architectures
adaptées aux besoins

analytiques

---

## Cours 8 — Diapositive 34 : Entrepôt de données (Data

Entrepôt de données (Data
Warehouse)

Centralisation : Regroupe les données venant de plusieurs sources
différentes en un seul lieu.
Qualité : Les données sont nettoyées, structurées et organisées avant
d'être stockées.

Analyse : Optimisé spécifiquement pour les rapports et les requêtes
complexes, contrairement aux bases de données classiques.

Aide à la décision : Sert d'outil principal aux dirigeants pour définir des
stratégies basées sur des faits historiques.

---

## Cours 8 — Diapositive 35 : Architecture et composantes

Architecture et composantes

Composantes principales :
- sources de données (systèmes transactionnels),
- ETL (Extract-Transform-Load) pour l'intégration,
- Stockage central,
- Serveurs de requêtes, outils de BI et visualisation.

Les données sont généralement historisées et agrégées.

---

## Cours 8 — Diapositive 36 : L'ETL (Extract, Transform, Load)

L'ETL (Extract, Transform, Load)

L'ETL est un processus qui permet d'extraire des données de diverses
sources, de les nettoyer et de les convertir dans un format standardisé. Une
fois transformées, ces données sont chargées dans un système central
comme un Data Warehouse pour être analysées et exploitées.

---

## Cours 8 — Diapositive 37 : L'ETL (Extract, Transform, Load)

L'ETL (Extract, Transform, Load)

---

## Cours 8 — Diapositive 38 : Exemple - Data Warehouse

Exemple - Data Warehouse

---

## Cours 8 — Diapositive 39 : Lac de données (Data Lake)

Lac de données (Data Lake)

- Un Data Lake est un référentiel centralisé qui stocke des données

brutes dans leur format natif (structurées, semi-structurées, non
structurées).

- Contrairement au Data Warehouse, les données ne sont pas

transformées à l'entrée mais au moment de leur utilisation (schema-
on-read).

---

## Cours 8 — Diapositive 40 : Exemple d'architecture Data Lake

Exemple d'architecture Data Lake

---

## Cours 8 — Diapositive 41 : Data Hub

Data Hub

- Un Data Hub est une architecture centralisée qui sert de point

d'échange et de distribution de données entre di>érents systèmes.

- Il agit comme un intermédiaire qui collecte, intègre et redistribue les

données sans nécessairement les stocker de façon permanente.

---

## Cours 8 — Diapositive 42 : Exemple

Exemple
d'architecture
Data Hub

---

## Cours 8 — Diapositive 43 : Architectures

Architectures
Cloud et Hybride

---

## Cours 8 — Diapositive 44 : Infrastructures locales (On-premise)

Infrastructures locales (On-premise)

Une infrastructure on-premise
signifie que l'organisation possède,
héberge et maintient ses propres
serveurs et équipements dans ses
locaux.

---

## Cours 8 — Diapositive 45 : Avantages et inconvénients

Avantages et inconvénients

Avantages : contrôle total, personnalisation maximale, conformité
facilitée pour données sensibles, pas de dépendance Internet.

Inconvénients : coûts d'investissement élevés, maintenance complexe,
scalabilité limitée, nécessite expertise interne, obsolescence matérielle.

---

## Cours 8 — Diapositive 46 : Infrastructures externes (Off-

Infrastructures externes (Off-
premise)

- Externalisation : Les serveurs sont hébergés hors de l'entreprise

(Cloud ou centres de données tiers).
- Location de matériel : L'organisation ne possède pas les machines

physiques, elle loue un service.

- Dépendance : La maintenance et le fonctionnement reposent

entièrement sur un fournisseur externe.

---

## Cours 8 — Diapositive 47 : Différences avec on-premise

Différences avec on-premise

Contrairement à l'on-premise, l'o>-premise
réduit les investissements initiaux, transfère la
maintenance au fournisseur, o>re une meilleure
scalabilité et permet un accès de partout.

---

## Cours 8 — Diapositive 48 : Solutions Cloud

Solutions Cloud

C'est de l'off-premise avec une couche
d'intelligence en plus. Dans le Cloud, on utilise
la virtualisation. Tu ne loues pas forcément une
machine physique précise, mais des ressources
(CPU, RAM) que tu peux augmenter ou réduire en un
clic. C'est flexible, automatisé et tu ne payes que ce
- ue tu consommes.

---

## Cours 8 — Diapositive 49 : Solutions Cloud

Solutions Cloud

Les trois principaux fournisseurs (AWS, Azure, GCP) o>rent des centaines de
services permettant de construire des architectures complètes.

---

## Cours 8 — Diapositive 50 : Amazon Web Services

Amazon Web Services

AWS est le leader du marché cloud depuis 2006.
- Services clés : EC2 (compute), S3 (stockage objet), RDS (bases de

données relationnelles), Lambda (serverless), Redshift (Data
Warehouse), EMR (big data).
- Force : maturité, écosystème vaste, disponibilité mondiale.

---

## Cours 8 — Diapositive 51 : Microsoft Azure

Microsoft Azure

- Services clés : Virtual Machines, Blob Storage, SQL Database, Azure

Functions, Synapse Analytics, Azure ML.
- Force : intégration Windows/O>ice, solutions hybrides, services

entreprise.

---

## Cours 8 — Diapositive 52 : Google Cloud Platform (GCP)

Google Cloud Platform (GCP)

GCP excelle en analytique et intelligence artificielle.

- Services clés : Compute Engine, Cloud Storage, Cloud SQL, BigQuery

(Data Warehouse), Dataflow, AI Platform.

- Force : analytique avancée, ML/AI, performance réseau Google,

innovation technologique.

---

## Cours 8 — Diapositive 53 : Comparaison des plateformes

Comparaison des plateformes
cloud

v AWS : leader marché, plus vaste catalogue, écosystème mature.

v Azure : meilleur pour entreprises Microsoft, excellent hybride.
v GCP : supérieur en données/IA, prix compétitifs.

Tous o>rent : haute disponibilité, scalabilité élastique, sécurité
enterprise-grade, modèle pay-as-you-go.

---

## Cours 8 — Diapositive 54 : Différent modèle

Différent modèle

de données

---

## Cours 8 — Diapositive 55 : Qu'est-ce qu'un modèle de données

Qu'est-ce qu'un modèle de données
?

Un modèle de données est une représentation visuelle et structurée de
l'information dans un système. C'est comme un plan qui montre
comment organiser et relier les données. Il aide à comprendre et
communiquer la structure des informations avant de créer une base de
données.

---

## Cours 8 — Diapositive 56 : Pourquoi modéliser ?

Pourquoi modéliser ?

La modélisation aide à mieux comprendre les besoins, facilite la
communication avec les utilisateurs, évite les erreurs de conception, et
sert de documentation. Un bon modèle permet de construire un système
de données efficace et cohérent.

---

## Cours 8 — Diapositive 57 : Les trois modèles principaux

Les trois modèles principaux

- Diagramme de Classes UML pour la conception orientée objet.

- Modèle Entité-Association (EA) pour structurer les données
- Diagramme de Flux de Données (DFD) pour comprendre les

processus

---

## Cours 8 — Diapositive 58 : Diagramme de

Diagramme de

classe

---

## Cours 8 — Diapositive 59 : Une classe est un modèle abstrait qui décrit un type d’objet du système.

Une classe est un modèle abstrait qui décrit un type d’objet du système.

Elle définit :

- ce que les objets sont (leurs données)

- ce qu’ils peuvent faire (leurs comportements)

Une classe n’est pas un objet réel, mais un plan pour créer des objets.

---

## Cours 8 — Diapositive 60 : Classe

Classe

§ Modèle

§ Description générale

§ N’existe pas concrètement

Objet

§ Instance de la classe

§ Élément concret du système

§ Existe réellement en mémoire

---

## Cours 8 — Diapositive 61 : Exemple simple : Classe vs Objet

Exemple simple : Classe vs Objet

Classe : Client
Objets :
- Client #1 : Alice Dupont
- Client #2 : Karim Benali
- Client #3 : Sophie Martin

---

## Cours 8 — Diapositive 62 : Classe = plan d’une maison

Classe = plan d’une maison
Objet = maison construite

ANALOGIE
DU MONDE

On peut construire plusieurs
maisons à partir du même plan

RÉEL

Modifier une maison ≠ modifier le
plan

---

## Cours 8 — Diapositive 63 : Une classe représente :

Une classe représente :

vun concept métier

vune entité du monde réel

vquelque chose que le système doit connaître et mémoriser

Exemples : Client, Commande, Produit, Facture

---

## Cours 8 — Diapositive 64 : Une classe a une responsabilité claire.

Une classe a une responsabilité claire.

- Elle représente une chose précise

- Elle ne fait pas tout

“De quoi cette classe est-elle responsable ?”

---

## Cours 8 — Diapositive 65 : Responsabilité d’une classe commande :

Responsabilité d’une classe commande :

- représenter une commande passée par un client

- contenir les informations liées à cette commande

❌ Ce n’est PAS sa responsabilité :

oafficher une page web

oenvoyer des emails

ogérer la base de données

---

## Cours 8 — Diapositive 66 : Les classes ne sortent pas de

Les classes ne sortent pas de
l’imagination du développeur.

D’OÙ
VIENNENT LES

- Elles viennent du besoin métier

CLASSES ?

- Elles viennent du problème à résoudre

---

## Cours 8 — Diapositive 67 : On commence toujours par comprendre :

On commence toujours par comprendre :

§ le domaine (commerce, hôpital, école, banque…)

§ ce que fait l’organisation

§ ce que le système doit gérer

Le vocabulaire métier est une mine d’or pour trouver les classes.

---

## Cours 8 — Diapositive 68 : « Un client peut passer une ou plusieurs commandes sur un site. Chaque commande est

« Un client peut passer une ou plusieurs commandes sur un site. Chaque commande est
associée à un seul client et contient plusieurs produits. Un produit possède un nom et un
prix. Le montant total d’une commande correspond à la somme des prix de tous les
produits qu’elle contient. »

Ce texte décrit un besoin métier et fait naturellement apparaître des classes potentielles.

---

## Cours 8 — Diapositive 69 : ANALYSE DU TEXTE

ANALYSE DU TEXTE

- On repère les noms (substantifs).

DES EXIGENCES

- Chaque nom est une classe

(MÉTHODE DES

potentielle.

NOM)

---

## Cours 8 — Diapositive 70 : Très souvent, une classe correspond à :

Très souvent, une classe correspond à :

vune personne (Client, Employé)

vun objet (Produit, Véhicule)

vun document (Facture, Contrat)

Si ça existe dans la réalité, c’est souvent une classe.

---

## Cours 8 — Diapositive 71 : Ce qui est stocké devient presque toujours une classe :

Ce qui est stocké devient presque toujours une classe :

§ Client

§ Commande

§ Paiement

§ Utilisateur

“Qu’est-ce qui doit être stocké et retrouvé plus tard ?”

---

## Cours 8 — Diapositive 72 : Certains rôles peuvent devenir des classes :

Certains rôles peuvent devenir des classes :

§ Client

§ Administrateur

§ Enseignant

§ Étudiant

⚠ Attention, un rôle ≠ toujours une classe

---

## Cours 8 — Diapositive 73 : Modélisation des classes logicielles

Modélisation des classes logicielles

du raisonnement à la structure UML!

---

## Cours 8 — Diapositive 74 : Après avoir identifié les classes, il faut maintenant :

Après avoir identifié les classes, il faut maintenant :

§ les structurer correctement

§ préciser leurs données

§ définir leurs relations

---

## Cours 8 — Diapositive 75 : En UML, une classe est représentée par un rectangle divisé en trois

En UML, une classe est représentée par un rectangle divisé en trois
parties :

1.Nom de la classe

2.Attributs

3.Méthodes

---

## Cours 8 — Diapositive 76 : § Placé en haut

§ Placé en haut

§ Commence par une majuscule

§ Au singulier

§ Nom clair et métier

---

## Cours 8 — Diapositive 77 : Les attributs décrivent :

Les attributs décrivent :

§ les données contenues dans la classe

§ l’état d’un objet

Un attribut = une information que l’objet mémorise

---

## Cours 8 — Diapositive 78 : Les méthodes décrivent :

Les méthodes décrivent :

§ ce que l’objet peut faire

§ les actions liées à la classe

Une méthode appartient toujours à une classe

---

## Cours 8 — Diapositive 79 : Exemple d’une classe UML

Exemple d’une classe UML

---

## Cours 8 — Diapositive 80 : Chaque attribut a un type :

Chaque attribut a un type :

§ string (texte)

§ int (entier)

§ float / double (nombre)

§ date

§ boolean

---

## Cours 8 — Diapositive 81 : UML utilise des symboles :

UML utilise des symboles :

§ + public

§ - privé

§ # protégé

En conception orientée objet, les attributs sont presque toujours privés.

---

## Cours 8 — Diapositive 82 : Une méthode représente une action liée à la classe. Elle décrit un

Une méthode représente une action liée à la classe. Elle décrit un
comportement cohérent avec la responsabilité de la classe

§ Méthodes métier

§ Méthodes technique

---

## Cours 8 — Diapositive 83 : Méthodes liées au domaine métier.

Méthodes liées au domaine métier.

Exemples :

§calculerTotal()

§ajouterProduit()

§validerCommande()

Elles font du sens pour un non-développeur

---

## Cours 8 — Diapositive 84 : Une méthode technique est une méthode liée à l’implémentation, souvent

Une méthode technique est une méthode liée à l’implémentation, souvent
générée automatiquement et qui ne représente pas une action métier.

§ getNom()

§ setPrix()

§ toString()

Elle sert au fonctionnement du code, pas à décrire le métier.

---

## Cours 8 — Diapositive 85 : - Les classes ne vivent jamais seules.

- Les classes ne vivent jamais seules.

Elles sont liées entre elles. Ces liens
sont appelés des relations.

---

## Cours 8 — Diapositive 86 : Association (relation de base)

Association (relation de base)

Une association indique qu’une classe connaît, utilise ou est liée à
une autre. Elle peut également avoir un nom de rôle.

Exemple :
- Client — Commande
- Client — passe — Commande (Améliore la lisibilité)

Une association peut être bidirectionnelle et unidirectionnelle. Il

faut privilégié la simplicité. On évite la sur-spécification

---

## Cours 8 — Diapositive 87 : § 1 : exactement un

§ 1 : exactement un

§ 0..1 : optionnel

§ * ou 0..* : plusieurs

§ 1..* : au moins un

§ 2..5 : intervalle précis

---

## Cours 8 — Diapositive 88 : Relation entre classes - Agrégation

Relation entre classes - Agrégation

---

## Cours 8 — Diapositive 89 : Relation entre classes - Composition

Relation entre classes - Composition

---

## Cours 8 — Diapositive 90 : § Dépendance forte : l’objet “composé” n’a pas de sens sans son

§ Dépendance forte : l’objet “composé” n’a pas de sens sans son

propriétaire

§ Cycle de vie lié : la durée de vie de l’objet dépend complètement de

celle du conteneur

§ Propriété exclusive : l’objet appartient à un seul propriétaire à la fois

---

# Cours 9

_Source : C47_cours9.pdf — 53 diapositives/pages_

## Cours 9 — Diapositive 1 : Analyse et conception

Analyse et conception
d’une solution de données

Code du Cours : 420-C47-BB

Cours 9

Enseignant : Nadir, BOUAKEL
nadir.bouakel@bdeb.qc.ca

---

## Cours 9 — Diapositive 2 : Différent modèle

Différent modèle

de données

---

## Cours 9 — Diapositive 3 : Modèle

Modèle
Conceptuel de
données (MCD)

---

## Cours 9 — Diapositive 4 : Modèle Entité-Associaiton (EA)

Modèle Entité-Associaiton (EA)

Le modèle EA (Entité-Association) est une méthode de modélisation qui

permet de représenter les données d’un système.

Il se compose de :

- Entités (ex : Client, Produit)

- Attributs (ex : nom, prix)

- Associations (relations entre entités)

---

## Cours 9 — Diapositive 5 : Modèle Entité-Associaiton (EA)

Modèle Entité-Associaiton (EA)

---

## Cours 9 — Diapositive 6 : Définition du MCD

Définition du MCD

Le Modèle Conceptuel de Données (MCD) représente les données d'un

système sous forme d'entités et de relations EA.

Il est indépendant de tout système de gestion de base de données et sert

d'étape intermédiaire entre l'analyse et la conception physique. Il sert
d’étape entre l’analyse des besoins et la conception de la base de
données.

- Son objectif est de répondre à la question : quelles données doivent être

stockées et comment sont-elles reliées entre elles?

---

## Cours 9 — Diapositive 7 : Pourquoi transformer le modèle

Pourquoi transformer le modèle
statique?

- Les classes UML ne correspondent pas directement à des tables de base de

données

- Certaines classes n'ont pas besoin d'être persistées (ex. : calcul temporaire)

- Les relations UML se traduisent différemment selon leur cardinalité
- Un MCD valide garantit la cohérence et l'intégrité des données stockées

---

## Cours 9 — Diapositive 8 : Dequoi est composé un MCD?

Dequoi est composé un MCD?

- Entités : Ce sont les objets ou concepts du monde réel dont on veut

conserver les données de façon durable (ex. : LIVRE, MEMBRE).

- Attributs (ou Colonnes) : Ce sont les propriétés qui décrivent une entité. Par

exemple, l'entité LIVRE possède les attributs "titre" et "auteur". Ils deviennent
les colonnes des tables.

- Identifiants (ou Clés primaires) : Chaque entité possède un identifiant unique

- ui permet de distinguer chaque enregistrement sans erreur. On l'appelle
la clé primaire (PK)

- Relations (ou Associations) : Elles représentent les liens logiques entre les

entités. (Clés étrangère, Tables de jontion)

---

## Cours 9 — Diapositive 9 : Vue d'ensemble des règles de

Vue d'ensemble des règles de
passage

Quatre règles systématiques guident la transformation du modèle statique vers

le MCD :

1. Chaque classe persistante → une entité (table)
2. Chaque attribut de classe → une colonne de la table

3. L'identifiant de la classe → la clé primaire (PK)

4. Chaque association → une relation entre tables (FK ou table de jonction)

---

## Cours 9 — Diapositive 10 : Règle 1 : Classe → Entité

Règle 1 : Classe → Entité

Chaque classe persistante du modèle

statique devient une entité dans le MCD,
puis une table dans la base de données.

Exemples de transformation :

Le nom de la classe est conservé comme

Classe Livre → Table LIVRE

nom de la table. Cette règle s'applique
uniquement aux classes persistantes.

Classe Membre → Table MEMBRE

Classe Emprunt → Table EMPRUNT

---

## Cours 9 — Diapositive 11 : Règle 2 : Attribut → Colonne

Règle 2 : Attribut → Colonne

Chaque attribut d'une classe persistante

devient une colonne de la table
correspondante.

Types courants :

String / Text → VARCHAR, TEXT

Le type de l'attribut détermine le type de

Integer → INT, BIGINT

la colonne. Chaque ligne de la table
représente une instance de la classe.

Date / DateTime → DATE, DATETIME

Float / Decimal → DECIMAL(p,s)

---

## Cours 9 — Diapositive 12 : Règle 3 : Identifiant → Clé primaire

Règle 3 : Identifiant → Clé primaire

L'identifiant unique d'une classe devient la clé primaire (PK) de la table. Elle

identifie chaque enregistrement de façon unique.

- La PK doit être unique dans toute la table
- Elle ne peut jamais être nulle (NOT NULL)

- Si aucun attribut naturel n'existe, on crée un identifiant artificiel

- Exemples : idClient, idProduit, idCommande

---

## Cours 9 — Diapositive 13 : Règle 4 : Association → Relation

Règle 4 : Association → Relation

La stratégie dépend entièrement de la cardinalité de l'association :

o 1..1 ajouter la PK d'une table comme FK dans l'autre
o 1..N ajouter la PK du côté 1 comme FK dans la table côté N

o N..M créer une table de jonction contenant les deux FK

---

## Cours 9 — Diapositive 14 : Exemple1

Exemple1

---

## Cours 9 — Diapositive 15 : Exemple 2

Exemple 2

MCD - Méthode MERISE

---

## Cours 9 — Diapositive 16 : Modèles de flux de

Modèles de flux de

données (DFD)

---

## Cours 9 — Diapositive 17 : Introduction au DFD

Introduction au DFD

- Le DFD représente la circulation des données dans un système

- Il montre comment l’information entre, est traitée et sort

- Il ne décrit pas la structure des données (contrairement au MCD)

Objectif : comprendre le fonctionnement global du système

---

## Cours 9 — Diapositive 18 : Les éléments du DFD

Les éléments du DFD

Un DFD est composé de 4 éléments :

- Processus → transforme les données

- Flux de données → circulation de l’information
- Stockage de données → base de données, fichiers

- Entités externes → acteurs (client, système externe)

---

## Cours 9 — Diapositive 19 : Pourquoi utiliser DFD

Pourquoi utiliser DFD

v Comprendre le fonctionnement d’un système

v Identifier les entrées et sorties

v Visualiser les traitements
v Aider à l’analyse des besoins

---

## Cours 9 — Diapositive 20 : Différence avec MCD

Différence avec MCD

Les deux sont complémentaires :

v MCD → structure des données (quoi stocker)
v DFD → flux des données (comment ça circule)

---

## Cours 9 — Diapositive 21 : DFD - Exemple

DFD - Exemple

---

## Cours 9 — Diapositive 22 : Types de Stockage

Types de Stockage

---

## Cours 9 — Diapositive 23 : Le Stockage de Données

Le Stockage de Données

Lorsqu’une application enregistre des informations (comptes d’utilisateurs,
commandes, messages...), ces données doivent être conservées durablement.
C’est le rôle d’un système de stockage de données.

Définition :
Un système de stockage de données est un logiciel qui permet d’organiser,
d’enregistrer et de récupérer des informations de façon structurée et fiable. On
l’appelle aussi base de données ou SGBD (Système de Gestion de Base de
Données).

---

## Cours 9 — Diapositive 24 : Le Stockage de Données

Le Stockage de Données

Les deux grandes approches :

Stockage relationnel (SQL) : basé sur des tables avec un schéma fixe.
Stockage non relationnel (NoSQL) : basé sur des structures flexibles, adaptées à
des données variées.

Le choix du bon système de stockage est l’une des premières décisions dans la
conception d’une architecture de solution.

---

## Cours 9 — Diapositive 25 : Le Stockage Relationnel (SQL)

Le Stockage Relationnel (SQL)

Le stockage relationnel (SQL) organise les données sous forme de tables,
comme des feuilles de calcul. Chaque table représente un type d’objet (Clients,
Commandes, Produits...). Chaque ligne est un enregistrement et chaque colonne
est une propriété.

Avant d’ajouter des données, on doit définir exactement quels champs existent
et quel type de données chacun contient (texte, nombre, date...). Cette structure
ne change pas facilement.

---

## Cours 9 — Diapositive 26 : Le Stockage Relationnel (SQL)

Le Stockage Relationnel (SQL)

Relations entre tables :
Les tables sont reliées entre elles via des clés (identifiants uniques), ce qui
permet de combiner des données de plusieurs tables dans une même requête.

Exemples de bases SQL populaires : MySQL, PostgreSQL, Microsoft SQL Server,
Oracle.

---

## Cours 9 — Diapositive 27 : Le Stockage Relationnel (SQL) —

Le Stockage Relationnel (SQL) —
Avantages

- Intégrité des données

- Transactions fiables (propriétés ACID)

- Requêtes puissantes

- Cas d’usage recommandés

---

## Cours 9 — Diapositive 28 : ACID

ACID

---

## Cours 9 — Diapositive 29 : Le Stockage Non Relationnel (NoSQL)

Le Stockage Non Relationnel (NoSQL)

- Le stockage NoSQL (Not Only SQL) ne repose pas sur des tables avec

un schéma fixe. Il est conçu pour gérer des données variées,
volumineuses ou dont la structure change fréquemment.

- On peut ajouter de nouveaux champs à un enregistrement sans

modifier toute la base. Chaque document ou enregistrement peut avoir
une structure différente des autres.

---

## Cours 9 — Diapositive 30 : Le Stockage Non Relationnel (NoSQL)

Le Stockage Non Relationnel (NoSQL)

Une famille, pas un seul système :

NoSQL regroupe plusieurs types de bases de données très différents les
uns des autres, chacun optimisé pour un modèle de données ou un cas
d’usage particulier.

Les 4 grandes familles NoSQL sont : documentaire, clé-valeur, colonnes et
graphes. Chacune répond à des besoins différents.

---

## Cours 9 — Diapositive 31 : Le Stockage Non Relationnel (NoSQL) —

Le Stockage Non Relationnel (NoSQL) —
Avantages

- Scalabilité horizontale

- Flexibilité du schéma

- Performances optimisées

- Cas d’usage recommandés

---

## Cours 9 — Diapositive 32 : SQL vs NoSQL — Critères de Choix

SQL vs NoSQL — Critères de Choix

Structure des données :

Données bien définies et stables → SQL. Structure variable ou
fréquemment modifiée → NoSQL.

Volume et vitesse :

Millions d’écritures rapides sur des données distribuées → NoSQL.
Requêtes analytiques complexes et fiables → SQL.

---

## Cours 9 — Diapositive 33 : SQL vs NoSQL — Critères de Choix

SQL vs NoSQL — Critères de Choix

Relations entre données :

Beaucoup de relations entre entités → SQL. Enregistrements relativement
indépendants → NoSQL.

Consistance :

Cohérence stricte indispensable (ex. : transactions financières) → SQL.
Cohérence éventuelle acceptable → NoSQL.

Dans de nombreuses architectures modernes, SQL et NoSQL coexistent : on
utilise le bon outil pour chaque partie du système.

---

## Cours 9 — Diapositive 34 : Les Grandes

Les Grandes
Familles NoSQL

---

## Cours 9 — Diapositive 35 : Les Grandes Familles NoSQL

Les Grandes Familles NoSQL

1. Documentaire :

Stocke les données sous forme de documents JSON. Exemples : MongoDB,
CouchDB.
2. Clé-Valeur :

Associe une clé unique à une valeur. Très rapide. Exemples : Redis, DynamoDB.

3. Colonnes :
Organise les données par colonnes. Optimisé pour les grands volumes.
Exemples : Cassandra, HBase.
4. Graphes :

Modélise des nœuds et des relations. Idéal pour les réseaux complexes.
Exemples : Neo4j, ArangoDB.

---

## Cours 9 — Diapositive 36 : NoSQL Documentaire — MongoDB,

NoSQL Documentaire — MongoDB,
CouchDB

Les bases documentaires stockent chaque enregistrement sous forme de
document structuré, généralement au format JSON. Un document regroupe des
champs et leurs valeurs, comme un objet dans un langage de programmation.

Flexibilité totale :
Deux documents dans la même collection n’ont pas besoin des mêmes champs.
Un produit “chaussure” peut avoir un champ “pointure” absent du produit “t-
shirt”.

---

## Cours 9 — Diapositive 37 : NoSQL Documentaire — MongoDB,

NoSQL Documentaire — MongoDB,
CouchDB

MongoDB est le leader de cette catégorie, très populaire pour les applications
web modernes.

CouchDB est apprécié pour sa synchronisation facile entre appareils
(applications mobiles hors ligne).

Cas d’usage typiques :

Catalogues de produits, profils utilisateurs, gestion de contenu, applications de
blogging.

---

## Cours 9 — Diapositive 38 : NoSQL Clé-Valeur — Redis, DynamoDB

NoSQL Clé-Valeur — Redis, DynamoDB

Les bases clé-valeur sont les plus simples : on associe une clé unique à une
valeur. La valeur peut être n’importe quoi (texte, nombre, liste, objet...). C’est le
modèle le plus rapide de toutes les bases NoSQL.

Redis :

Fonctionne principalement en mémoire vive (RAM), ce qui le rend extrêmement
rapide. Il est souvent utilisé comme cache pour accélérer les autres bases de
données ou comme système de file d’attente.

---

## Cours 9 — Diapositive 39 : NoSQL Clé-Valeur — Redis, DynamoDB

NoSQL Clé-Valeur — Redis, DynamoDB

DynamoDB :

Service géré d’Amazon Web Services. Offre une
scalabilité quasi illimitée. Très utilisé dans les grandes
applications cloud.

Cas d’usage typiques :

Sessions utilisateurs, mise en cache de résultats, files
d’attente, tableaux de classement en temps réel.

---

## Cours 9 — Diapositive 40 : NoSQL Colonnes — Cassandra, HBase

NoSQL Colonnes — Cassandra, HBase

Les bases orientées colonnes stockent les données en regroupant les valeurs par
colonne plutôt que par ligne. Dans une base SQL, on lit une ligne complète
même si on n’a besoin que d’une colonne. Ici, on ne lit que les colonnes
nécessaires — beaucoup plus efficace sur de très grandes tables.

Apache Cassandra :

Conçue pour ne jamais tomber en panne (haute disponibilité). Utilisée par
Netflix, Instagram et Twitter. Supporte des millions d’écritures par seconde.

---

## Cours 9 — Diapositive 41 : NoSQL Colonnes — Cassandra, HBase

NoSQL Colonnes — Cassandra, HBase

HBase :
Intégrée à l’écosystème Hadoop. Utilisée pour
le traitement de très grandes quantités de
données (Big Data).

Cas d’usage typiques :

Journaux d’événements (logs), données IoT,
historique de transactions.

---

## Cours 9 — Diapositive 42 : NoSQL Graphes — Neo4j, ArangoDB

NoSQL Graphes — Neo4j, ArangoDB

Les bases de graphes modélisent les données comme un réseau de nœuds
(entités) reliés par des arêtes (relations). Cette approche est naturelle pour
représenter des connexions entre objets.

Pourquoi les graphes? :
En SQL, traverser des relations complexes (ex. : “les amis de mes amis qui
écoutent la même musique”) nécessite plusieurs jointures coûteuses. Dans un
graphe, cette traversée est native et très rapide.

---

## Cours 9 — Diapositive 43 : NoSQL Graphes — Neo4j, ArangoDB

NoSQL Graphes — Neo4j, ArangoDB

Neo4j :

Base de graphes la plus utilisée au monde. Utilise le
langage de requête Cypher, lisible et intuitif.

ArangoDB :
Base multi-modèle supportant graphes, documents
et clé-valeur dans un seul système.
Cas d’usage typiques :

Réseaux sociaux, moteurs de recommandation,
détection de fraude, gestion de réseaux (télécoms,
logistique).

---

## Cours 9 — Diapositive 44 : Exemple — Choisir la Bonne Famille

Exemple — Choisir la Bonne Famille
NoSQL

---

## Cours 9 — Diapositive 45 : Les 3 Composantes d’une Architecture

Les 3 Composantes d’une Architecture
de Données

Une architecture de solution de données est l’ensemble des composants
techniques permettant de collecter, traiter et distribuer des données. Elle repose
sur 3 grandes composantes : Stockage, Traitement, Diffusion

---

## Cours 9 — Diapositive 46 : Les 3 Composantes d’une Architecture

Les 3 Composantes d’une Architecture
de Données

1. Stockage :

Où et comment les données sont conservées durablement. C’est ici
- u’interviennent les bases SQL et NoSQL. Le choix dépend du volume, de la
structure et de la fréquence d’accès.

---

## Cours 9 — Diapositive 47 : Les 3 Composantes d’une Architecture

Les 3 Composantes d’une Architecture
de Données

2. Traitement :

Comment les données sont transformées, analysées ou enrichies. Le traitement
peut être en temps réel (streaming) ou en différé (batch).

---

## Cours 9 — Diapositive 48 : Les 3 Composantes d’une Architecture

Les 3 Composantes d’une Architecture
de Données

3. Diffusion :
Comment les données sont transmises aux utilisateurs ou aux autres systèmes.
Cela inclut les API, les systèmes de messagerie (ex. : Kafka) et les interfaces
d’accès.

---

## Cours 9 — Diapositive 49 : Critère 1 — Performance et Scalabilité

Critère #1 — Performance et Scalabilité

- Performance : capacité d’un système à répondre rapidement aux requêtes.

- Scalabilité : capacité à maintenir cette performance même quand le volume

ou le nombre d’utilisateurs augmente.

---

## Cours 9 — Diapositive 50 : Critère 1 — Performance et Scalabilité

Critère #1 — Performance et Scalabilité

Scalabilité verticale :

On rend le serveur plus puissant (plus de RAM, processeur plus rapide). Simple
mais limité et coûteux.

Scalabilité horizontale :

On ajoute plusieurs serveurs qui partagent la charge. Quasi illimité. Les bases
NoSQL y sont naturellement adaptées.

---

## Cours 9 — Diapositive 51 : Critère 2 — Sécurité des Données

Critère #2 — Sécurité des Données

La sécurité des données est une exigence non négociable dans toute
architecture de solution. Elle vise à protéger les données contre les accès non
autorisés, la corruption ou la perte.

Authentification et contrôle d’accès :

Seules les personnes ou systèmes autorisés peuvent lire ou modifier les
données, grâce à des comptes, des rôles et des permissions.

Chiffrement :

Les données sont chiffrées en transit (sur le réseau) et au repos (sur le disque).
Cela empêche leur lecture en cas d’interception.

---

## Cours 9 — Diapositive 52 : Critère 2 — Sécurité des Données

Critère #2 — Sécurité des Données

Audit et journalisation :

Toute opération sur les données est enregistrée (qui a accédé à quoi, quand)
pour détecter les anomalies.

Sauvegarde et récupération :

Des sauvegardes régulières permettent de restaurer les données en cas de
panne ou d’attaque. Le RGPD impose des obligations précises sur la protection
des données personnelles.

---

## Cours 9 — Diapositive 53 : Exemple — Architecture de Solution

Exemple — Architecture de Solution
Complète

---

# Cours 10

_Source : cours10.pdf — 37 diapositives/pages_

## Cours 10 — Diapositive 1 : Analyse et conception

Analyse et conception
d’une solution de données

Code du Cours : 420-C47-BB

Cours 10

Enseignant : Nadir, BOUAKEL
nadir.bouakel@bdeb.qc.ca

---

## Cours 10 — Diapositive 2 : Diagrammes

Diagrammes
Architecturaux

UML

---

## Cours 10 — Diapositive 3 : Diagramme Architectural UML

Diagramme Architectural UML

Qu'est-ce qu'un diagramme architectural UML ?

Un diagramme architectural UML est une représentation visuelle
normalisée qui décrit la structure, les composants et les interactions d'un
système informatique.

---

## Cours 10 — Diapositive 4 : Diagramme Architectural UML

Diagramme Architectural UML

Pourquoi l'utiliser ?

Il permet à tous les membres d'une équipe (développeurs, architectes,
gestionnaires) de comprendre et de communiquer de façon claire et
standard la conception d'une solution.

UML signifie : Unified Modeling Language (Langage de Modélisation Unifié)

---

## Cours 10 — Diapositive 5 : Les Principaux Diagrammes UML pour

Les Principaux Diagrammes UML pour
l'Architecture

Diagramme de Classes : représente les entités et leurs relations

Diagramme de Composants : montre les modules logiciels et leurs
dépendances

Diagramme de Déploiement : illustre comment le système est installé sur
l'infrastructure physique

Diagramme de Séquence : montre les échanges de messages entre
composants dans le temps

Diagramme de Flux de Données (DFD) : représente la circulation des
données

---

## Cours 10 — Diapositive 6 : Diagramme de Composants

Diagramme de Composants

Définition :

Un diagramme de composants montre les différents modules logiciels
(composants) d'un système ainsi que les interfaces et les dépendances
- ui les relient.

À quoi ça sert ?

Il permet de visualiser comment les différentes parties du logiciel sont
organisées et comment elles communiquent entre elles.

---

## Cours 10 — Diapositive 7 : Diagramme de Composants

Diagramme de Composants

Éléments clés :

- Composant : un module ou un service indépendant (ex. : API, base de
données, interface utilisateur)

- Interface : le point de connexion entre deux composants

- Dépendance : indique qu'un composant a besoin d'un autre pour
fonctionner

---

## Cours 10 — Diapositive 8 : Diagramme de Composants — Exemple

Diagramme de Composants — Exemple

---

## Cours 10 — Diapositive 9 : Qualité d’une

Qualité d’une

Solution de

Données

---

## Cours 10 — Diapositive 10 : Définition — La Qualité des Données

Définition — La Qualité des Données

Qu'est-ce que la qualité des données ?

La qualité des données désigne le degré auquel les données sont
appropriées pour l'utilisation prévue. Des données de qualité sont fiables,
exactes, complètes et disponibles au bon moment.

---

## Cours 10 — Diapositive 11 : Définition — La Qualité des Données

Définition — La Qualité des Données

Pourquoi c'est important ?

De mauvaises données mènent à de mauvaises décisions. Par exemple, si
les données de stock d'un entrepôt sont incorrectes, on peut commander
trop ou trop peu de marchandises.

Assurer la qualité des données est une responsabilité partagée entre les
équipes techniques et les équipes métiers.

---

## Cours 10 — Diapositive 12 : Les Dimensions de la Qualité des

Les Dimensions de la Qualité des
Données

Exactitude : les données reflètent-elles la réalité ? (ex. : le prix d'un produit est-il correct ?)
Complétude : est-ce que toutes les données requises sont présentes ? (ex. : tous les
clients ont-ils une adresse courriel ?)
Cohérence : les données sont-elles identiques d'un système à l'autre ? (ex. : même format
de date partout)
Fraîcheur (Timeliness) : les données sont-elles à jour ? (ex. : les prix mis à jour chaque jour)
Unicité : existe-t-il des doublons ? (ex. : un même client enregistré deux fois)
Validité : les données respectent-elles les formats attendus ? (ex. : un code postal à 6
caractères)

---

## Cours 10 — Diapositive 13 : Mesures de Performance de la Solution

Mesures de Performance de la Solution

Définition :

Les mesures de performance évaluent la capacité du système à répondre
rapidement et à supporter une charge élevée d'utilisateurs ou de
transactions.

---

## Cours 10 — Diapositive 14 : Mesures de Performance de la Solution

Mesures de Performance de la Solution

Indicateurs clés de performance (KPI) :

v Temps de réponse : délai entre une requête et la réponse du système

(objectif : moins de 2 secondes pour une requête simple)

v Débit (Throughput) : nombre de transactions traitées par seconde ou

par minute

v Disponibilité (Uptime) : pourcentage de temps où le système est

opérationnel (ex. : 99,9 %)

v Latence : délai de transmission des données dans le réseau

---

## Cours 10 — Diapositive 15 : Mesures de Sécurité de la Solution

Mesures de Sécurité de la Solution

Définition :

Les mesures de sécurité protègent les données contre les accès non
autorisés, les pertes et les altérations.

---

## Cours 10 — Diapositive 16 : Mesures de Sécurité de la Solution

Mesures de Sécurité de la Solution

Principaux indicateurs de sécurité :
v Authentification : vérification de l'identité des utilisateurs (ex. : mot de passe,

authentification à deux facteurs)
v Autorisation : contrôle de ce que chaque utilisateur peut voir ou faire (ex. :

rôles et permissions)
v Chiffrement : protection des données en transit (HTTPS/TLS) et au repos (AES-

256)
v Audit et journalisation : enregistrement de toutes les actions pour retracer les

incidents
v Sauvegarde et récupération : fréquence des sauvegardes et délai de

récupération (RTO/RPO)

---

## Cours 10 — Diapositive 17 : Assurer la Qualité de la Solution

Assurer la Qualité de la Solution

Pourquoi investir dans la qualité et la sécurité des données ?

- Meilleures décisions d'affaires
- Réduction des coûts

- Conformité légale

- Confiance des utilisateurs

- Continuité des opérations

---

## Cours 10 — Diapositive 18 : Validation de la

Validation de la

Conformité

---

## Cours 10 — Diapositive 19 : La Gouvernance des Données

La Gouvernance des Données

La gouvernance des données est l'ensemble des règles, processus et
responsabilités qui définissent comment les données sont gérées,
utilisées et protégées au sein d'une organisation.

---

## Cours 10 — Diapositive 20 : La Gouvernance des Données

La Gouvernance des Données

Pourquoi valider la conformité ?

Avant de déployer une solution de données, il faut s'assurer qu'elle
respecte les règles établies par l'organisation. Cette validation se fait
auprès de trois instances principales :

1. L'instance de gouvernance des données

2. Le comité d'architecture (conformité technologique)

3. Les responsables métiers (couverture fonctionnelle)

---

## Cours 10 — Diapositive 21 : Instance de Gouvernance des Données

Instance de Gouvernance des Données

Définition :

L'instance de gouvernance des données est un comité ou une équipe
chargée de définir et de faire respecter les règles de gestion des données
dans l'organisation.

Son rôle dans la validation :

Elle vérifie que la solution respecte les politiques de données de
l'organisation.

---

## Cours 10 — Diapositive 22 : Instance de Gouvernance des Données

Instance de Gouvernance des Données

Exemples de questions posées lors de la validation :

- Les données personnelles sont-elles protégées selon les règles de

confidentialité ?

- La classification des données (publiques, confidentielles, secrètes) est-

elle respectée ?

- Les données sont-elles stockées selon les règles de rétention définies ?

- Y a-t-il un propriétaire de données clairement identifié pour chaque

donnée critique ?

---

## Cours 10 — Diapositive 23 : Comité d'Architecture — Conformité

Comité d'Architecture — Conformité
Technologique

Définition :

Le comité d'architecture est un groupe d'experts techniques qui s'assure
- ue les nouvelles solutions respectent les standards technologiques
choisis par l'organisation.

Son rôle :

Il évalue si la solution proposée est compatible avec les technologies, les
outils et les patterns architecturaux déjà en place.

---

## Cours 10 — Diapositive 24 : Comité d'Architecture — Conformité

Comité d'Architecture — Conformité
Technologique

Exemples de critères vérifiés :

- La solution utilise-t-elle les technologies approuvées ? (ex. : PostgreSQL

plutôt qu'une base de données non standard)

- L'architecture respecte-t-elle les patterns définis ? (ex. : microservices,

3-tiers)

- Les performances et la scalabilité répondent-elles aux exigences

établies ?

- La solution s'intègre-t-elle bien avec les systèmes existants ?

---

## Cours 10 — Diapositive 25 : Responsables Métiers — Couverture

Responsables Métiers — Couverture
Fonctionnelle

Définition :

Les responsables métiers sont les personnes qui utilisent ou
commandent la solution. Ils valident que la solution répond aux besoins
réels de l'organisation.

Leur rôle :

Ils vérifient que toutes les fonctionnalités requises sont bien présentes et
- ue les données disponibles permettent de réaliser les activités métiers
prévues.

---

## Cours 10 — Diapositive 26 : Responsables Métiers — Couverture

Responsables Métiers — Couverture
Fonctionnelle

Exemples de questions posées :

- Est-ce que tous les rapports dont nous avons besoin peuvent être
produits ?

- Les données sont-elles disponibles au bon niveau de détail ?

- Les flux de données correspondent-ils aux processus d'affaires réels ?

- Les délais de disponibilité des données correspondent-ils aux besoins
opérationnels ?

---

## Cours 10 — Diapositive 27 : Processus de Validation — Comment ça

Processus de Validation — Comment ça
se passe ?

Le processus de validation suit généralement les étapes suivantes :

1. Préparation du dossier d'architecture : documentation de la solution (diagrammes,
descriptions, justifications)

2. Présentation à l'instance de gouvernance : vérification des règles de données
3. Présentation au comité d'architecture : vérification de la conformité technologique

4. Présentation aux responsables métiers : vérification de la couverture fonctionnelle
5. Traitement des écarts : si des problèmes sont détectés, on corrige la solution avant
de continuer

6. Approbation et déploiement : une fois toutes les instances satisfaites, la solution
est approuvée pour déploiement

---

## Cours 10 — Diapositive 28 : Représentation

Représentation
d’une architecture

de données

---

## Cours 10 — Diapositive 29 : Modèle Entité-Association (EA) — Le

Modèle Entité-Association (EA) — Le
classique

Inventé dans les années 1970, encore enseigné aujourd'hui.

Les formes utilisées :
- 
→ Rectangle : représente une Entité (= une classe)
- 
→ Ovale / Ellipse : représente un Attribut
- 
→ Losange : représente une Association (= une relation)

Avantages :
- 
→ Très visuel, facile à comprendre pour les non-techniciens.

Limites :
- 
→ Devient illisible quand le schéma est grand.

---

## Cours 10 — Diapositive 30 : [Aucun texte extractible automatiquement sur cette diapositive.]

[Aucun texte extractible automatiquement sur cette diapositive.]

---

## Cours 10 — Diapositive 31 : Exercice 1 - MCD

Exercice 1 - MCD

Notre bibliothèque souhaite gérer ses emprunts. Un Membre (identifié par
un id_membre, un nom et un email) possède une et une seule Carte
d'Abonnement (numero_carte, date_emission). Évidemment, une carte
appartient à un seul membre. Un membre peut emprunter plusieurs Livres
(isbn, titre, annee), ou n'en emprunter aucun s'il vient juste de s'inscrire.
Un livre physique précis est emprunté par au maximum un membre à la
fois (ou zéro s'il est en rayon). Enfin, un livre est écrit par au moins un
Auteur (id_auteur, nom, nationalite), et un auteur a pu écrire plusieurs
livres.

---

## Cours 10 — Diapositive 32 : Exercice 1 -

Exercice 1 -

SOL

Solution format modèle EA : lien

---

## Cours 10 — Diapositive 33 : Exercice 2 - MCD

Exercice 2 - MCD

La clinique souhaite informatiser le suivi de ses Patients. Pour chaque personne soignée, on doit
impérativement enregistrer son numéro d'assurance sociale, son nom complet ainsi que sa date
de naissance pour le suivi des rappels. À chaque patient est rattaché un unique Dossier
Médical. Ce dossier permet de connaître rapidement le groupe sanguin du patient et de lister
ses allergies connues. Un dossier ne peut appartenir qu'à un seul patient et chaque patient
possède obligatoirement le sien. Les patients peuvent planifier plusieurs Rendez-vous au sein
de l'établissement. Pour une consultation donnée, on note la date et l'heure précise du passage
ainsi que le motif de la visite (ex: contrôle, urgence). Un rendez-vous ne concerne toujours qu'un
seul patient à la fois. Chaque consultation est placée sous la responsabilité d'un seul Médecin.
On identifie ces derniers par leur numéro de licence professionnelle. Il est aussi important de
savoir comment ils s'appellent et quelle est leur spécialité (ex: Cardiologue, Généraliste). Un
médecin assure, au fil du temps, de nombreux rendez-vous. Enfin, le système doit permettre de
désigner un médecin comme "référent" pour un patient. Un patient peut n'avoir aucun médecin
référent ou en choisir un seul. De son côté, un médecin peut être le référent de plusieurs
patients différents.

---

## Cours 10 — Diapositive 34 : Exercice 2 - SOL

Exercice 2 - SOL

---

## Cours 10 — Diapositive 35 : Exercice 3 - Architecture

Exercice 3 - Architecture

Le magasin SportDirect possède une base de données pour ses ventes. Le
directeur souhaite maintenant deux évolutions :

1.
Il veut un outil pour analyser les tendances de l'année et générer des rapports
(Dashboard). Pour cela, les données de la base doivent être nettoyées et
organisées dans un nouveau système spécialisé pour l'aide à la décision. On
ne peut pas envoyer les données telles quelles, il faut un mécanisme pour
les extraire et les convertir au bon format chaque soir.
2.
Il veut une application mobile pour les clients. Pour des raisons de sécurité,
l'application ne doit jamais toucher à la base de données. Elle doit passer par
un intermédiaire qui contient la logique de calcul et qui communique via
des standards du web (HTTP).

---

## Cours 10 — Diapositive 36 : Exercice 3 - SOL

Exercice 3 - SOL

---

## Cours 10 — Diapositive 37 : TP2

TP2

---

# Cours 11

_Source : cours11.pdf — 38 diapositives/pages_

## Cours 11 — Diapositive 1 : Analyse et conception

Analyse et conception
d’une solution de données

Code du Cours : 420-C47-BB

Cours 11

Enseignant : Nadir, BOUAKEL
nadir.bouakel@bdeb.qc.ca

---

## Cours 11 — Diapositive 2 : L’écosystème des

L’écosystème des
sources de données

---

## Cours 11 — Diapositive 3 : Les grandes familles de sources

Les grandes familles de sources

- Bases de données (Relationnelles & NoSQL)

- Stockage massif (Entrepôts & Lacs de données)
- Échanges et fichiers (APIs & Fichiers plats)

- Données en mouvement (Flux de données)

---

## Cours 11 — Diapositive 4 : Bases relationnelles : Définition

Bases relationnelles : Définition

Une base relationnelle organise les données sous forme de tableaux rigides
composés de lignes et de colonnes. Ces tableaux sont liés entre eux par des
relations logiques strictes.

On utilise le langage standard SQL pour interroger, insérer ou modifier ces
informations. Ce modèle impose une structure précise avant même d’insérer la
moindre donnée.

---

## Cours 11 — Diapositive 5 : Bases relationnelles

Bases relationnelles

---

## Cours 11 — Diapositive 6 : Bases relationnelles : Avantages

Bases relationnelles : Avantages

- Très grande fiabilité des données.

- Garantit qu’aucune information n’est orpheline (intégrité référentielle).
- Idéal pour les transactions complexes.

---

## Cours 11 — Diapositive 7 : Bases NoSQL : Définition

Bases NoSQL : Définition

Le NoSQL est une approche de stockage qui s’affranchit des tableaux stricts
traditionnels pour offrir plus de flexibilité. Les données peuvent y être stockées
sous forme de documents (comme des objets JSON), de graphes ou de paires
clé-valeur.
Cette méthode permet de sauvegarder des informations sans avoir besoin de
définir un schéma parfait à l’avance. Elle a été conçue pour répondre aux
immenses volumes de données du web moderne.

---

## Cours 11 — Diapositive 8 : Bases NoSQL : Avantages

Bases NoSQL : Avantages

- Extrêmement flexible face aux changements.

- Excellente capacité à gérer d’immenses volumes (scalabilité).
- Performances très rapides pour les lectures simples.

---

## Cours 11 — Diapositive 9 : Bases NoSQL

Bases NoSQL

---

## Cours 11 — Diapositive 10 : Entrepôts de données

Entrepôts de données

Un entrepôt de données est un système centralisé qui consolide des
informations provenant de multiples sources différentes au sein d’une
entreprise. Ces données sont nettoyées, formatées et structurées
spécifiquement pour faciliter l’analyse historique.

---

## Cours 11 — Diapositive 11 : Lacs de données

Lacs de données

Un lac de données est un vaste espace de stockage qui conserve une quantité
massive de données dans leur format brut et original. Contrairement à l’entrepôt,
on y déverse les données (textes, images, logs) sans les structurer ni les nettoyer
au préalable.

---

## Cours 11 — Diapositive 12 : APIs (Interfaces de programmation)

APIs (Interfaces de programmation)

v Une API agit comme un pont de communication sécurisé permettant à deux

logiciels différents de se parler et de s’échanger des informations. Elle définit
un ensemble de règles claires sur la manière dont on peut demander de la
donnée à un système distant.

v Au lieu de se connecter directement à la base de données de quelqu’un

d’autre, on lui pose une question via l’API. C’est comme le serveur dans un
restaurant qui prend votre commande et vous rapporte le plat.

---

## Cours 11 — Diapositive 13 : APIs : Avantages

APIs : Avantages

- Protège la base de données source (accès contrôlé).

- Facilite l’intégration de services externes.
- Format de réponse standardisé (souvent en JSON).

---

## Cours 11 — Diapositive 14 : EXAMPLE

EXAMPLE

---

## Cours 11 — Diapositive 15 : Fichiers plats (CSV, JSON)

Fichiers plats (CSV, JSON)

v Les fichiers plats sont des documents textes simples qui stockent des

données sans aucune logique complexe ni relations internes. Les
informations y sont généralement séparées par un caractère spécifique,
comme une virgule dans un fichier CSV.
v Ils ne nécessitent aucun logiciel spécialisé pour être lus ou modifiés, un

simple bloc-notes suffit. C’est le format d’échange le plus basique et universel
en informatique.

---

## Cours 11 — Diapositive 16 : CSV

CSV

---

## Cours 11 — Diapositive 17 : JSON

JSON

---

## Cours 11 — Diapositive 18 : Flux de données

Flux de données
(Data Streams)

Un flux de données est une
séquence d’informations générée
de manière continue et
ininterrompue par une ou plusieurs
sources. Au lieu d’attendre d’avoir
un gros bloc de données pour le
traiter, le système analyse ces
informations au fil de l’eau, dès
leur arrivée.

---

## Cours 11 — Diapositive 19 : Les défis de la

Les défis de la
consommation de

données

---

## Cours 11 — Diapositive 20 : Défis de consommation : 6 piliers de contraintes

Défis de consommation : 6 piliers de contraintes

v Authentification

v Chiffrement

v Latence
v Intégrité

v Traçabilité

v Résilience aux pannes

---

## Cours 11 — Diapositive 21 : Authentification

Authentification

L’authentification est le
processus informatique
permettant de vérifier de façon
certaine l’identité d’un
utilisateur, d’un système ou
d’une application.

---

## Cours 11 — Diapositive 22 : Authentification : L’enjeu

Authentification : L’enjeu

- Bloquer les accès illégitimes.

- Protéger les données sensibles.
- Associer les actions à un utilisateur précis.

---

## Cours 11 — Diapositive 23 : Authentification :

Authentification :
Exemple

---

## Cours 11 — Diapositive 24 : Chiffrement :

Chiffrement :
Définition

Le chiffrement est une
technique mathématique qui
transforme une donnée lisible
en un format brouillé et
incompréhensible.

---

## Cours 11 — Diapositive 25 : Chiffrement : L’enjeu

Chiffrement : L’enjeu

- Garantir la confidentialité absolue.

- Rendre la donnée inutile même en cas de piratage.
- Respecter les lois sur la vie privée.

---

## Cours 11 — Diapositive 26 : Chiffrement :

Chiffrement :
Exemple

---

## Cours 11 — Diapositive 27 : Latence :

Latence :
Définition

La latence représente le délai
temporel qui s’écoule entre le
moment où une application
demande une donnée et le
moment où elle la reçoit
effectivement.

---

## Cours 11 — Diapositive 28 : Latence : L’enjeu

Latence : L’enjeu

- Garantir une expérience utilisateur réactive.

- Assurer le bon fonctionnement des systèmes en temps réel.
- Optimiser le placement géographique des serveurs.

---

## Cours 11 — Diapositive 29 : Latence : Exemple

Latence : Exemple

---

## Cours 11 — Diapositive 30 : Intégrité :

Intégrité :
Définition

L’intégrité est la garantie
formelle qu’une donnée n’a
subi aucune modification,
altération ou destruction
accidentelle au cours de son
cycle de vie.

---

## Cours 11 — Diapositive 31 : Intégrité : L’enjeu

Intégrité : L’enjeu

- Éviter la corruption des fichiers.

- Maintenir la cohérence logique du système.
- Se protéger contre les manipulations malveillantes.

---

## Cours 11 — Diapositive 32 : Intégrité - Exemple

Intégrité - Exemple

---

## Cours 11 — Diapositive 33 : Traçabilité

Traçabilité
des échanges

La traçabilité est la capacité
d’un système à enregistrer
méticuleusement l’historique
complet de toutes les actions
effectuées sur les données.

---

## Cours 11 — Diapositive 34 : Traçabilité : L’enjeu

Traçabilité : L’enjeu

- Permettre des enquêtes en cas d’incident (audit).

- Faciliter le diagnostic des erreurs (débogage).
- Répondre aux obligations légales et juridiques.

---

## Cours 11 — Diapositive 35 : Traçabilité - Exemple

Traçabilité - Exemple

---

## Cours 11 — Diapositive 36 : Résilience aux

Résilience aux
pannes : Définition

La résilience est la capacité
d’une architecture informatique
à absorber un choc ou une
panne matérielle tout en
continuant à fournir son
service.

---

## Cours 11 — Diapositive 37 : Résilience : L’enjeu

Résilience : L’enjeu

- Éviter les interruptions de service coûteuses.

- Protéger contre la perte définitive de données.
- Assurer un fonctionnement 24h/24 et 7j/7.

---

## Cours 11 — Diapositive 38 : Exemple

Exemple

---

