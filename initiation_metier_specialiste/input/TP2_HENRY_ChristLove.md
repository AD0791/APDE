**College Bois de Boulogne**

**Initation au metier de specialiste en intégration de données**

**TP2 : Initiation au metier de specialiste de donnees (C48)**

Professeur : ZID TALEL

Etudiante : Christ-Love Henry

> Date : 3 mai 2026

# Table des matières {#table-des-matières .TOC-Heading}

[**Section1** [3](#section1)](#section1)

[Tâche 1.1 : Prompt minimal
[3](#tâche-1.1-prompt-minimal)](#tâche-1.1-prompt-minimal)

[Tâche 1.2 : Comparaison
[3](#tâche-1.2-comparaison)](#tâche-1.2-comparaison)

[Tâche 1.3 Réflexion [3](#tâche-1.3-réflexion)](#tâche-1.3-réflexion)

[**Section 2** [4](#section-2)](#section-2)

[Tâche 2.1 Prompt enrichi avec contexte
[4](#tâche-2.1-prompt-enrichi-avec-contexte)](#tâche-2.1-prompt-enrichi-avec-contexte)

[Tâche 2.2 Prompt complet avec contraintes
[4](#tâche-2.2-prompt-complet-avec-contraintes)](#tâche-2.2-prompt-complet-avec-contraintes)

[Tâche 2.3 Tableau de Progression
[5](#tâche-2.3-tableau-de-progression)](#tâche-2.3-tableau-de-progression)

[Tâche 2.4 Réflexion [5](#tâche-2.4-réflexion)](#tâche-2.4-réflexion)

[**Section 3** [6](#section-3)](#section-3)

[Tâche 3.1 Prompt avec les 5 composantes
[6](#tâche-3.1-prompt-avec-les-5-composantes)](#tâche-3.1-prompt-avec-les-5-composantes)

[Rapport d'analyse de qualité -- Dataset Clients
[8](#rapport-danalyse-de-qualité-dataset-clients)](#rapport-danalyse-de-qualité-dataset-clients)

[Tâche 3.2 Checklist de Validation
[10](#tâche-3.2-checklist-de-validation)](#tâche-3.2-checklist-de-validation)

[**Section 4** [11](#section-4)](#section-4)

[Tâche 4.1 Prompt Chain-of-Thought complet
[11](#tâche-4.1-prompt-chain-of-thought-complet)](#tâche-4.1-prompt-chain-of-thought-complet)

[Résultat obtenu après exécution du prompt Chain-of-Thought
[14](#résultat-obtenu-après-exécution-du-prompt-chain-of-thought)](#résultat-obtenu-après-exécution-du-prompt-chain-of-thought)

[Tâche 4.2 Justification du Prompt
[17](#tâche-4.2-justification-du-prompt)](#tâche-4.2-justification-du-prompt)

[Tâche 4.3 Comparaison : Prompt Simple vs Chain-of-Thought
[17](#tâche-4.3-comparaison-prompt-simple-vs-chain-of-thought)](#tâche-4.3-comparaison-prompt-simple-vs-chain-of-thought)

[Tâche 4.4 Réflexion finale
[17](#tâche-4.4-réflexion-finale)](#tâche-4.4-réflexion-finale)

# **Section1**

## Tâche 1.1 : Prompt minimal

Tu es un analyste de données spécialisé en qualité des données.

Analyse le fichier clients.csv afin d'identifier les principaux
problèmes de qualité des données, notamment les doublons, les valeurs
manquantes, les formats invalides et les incohérences dans les champs
clients.

## Tâche 1.2 : Comparaison

**Prompt simple :** Analyse ce fichier CSV de clients.

  ---------------------------------------------------------------------------
  **Critère**   **Prompt Simple** **Votre Prompt**
  ------------- ----------------- -------------------------------------------
  **Détecte les Oui, mais de      Oui, avec une attention plus claire sur les
  doublons ?**  manière générale  doublons

  **Identifie   Possiblement,     Oui, car la qualité des champs est
  emails        mais sans         explicitement demandée
  invalides ?** garantie          

  **Quantifie   Pas toujours      Partiellement, selon la réponse générée
  les anomalies                   
  ?**                             

  **Propose des Pas               Plus probable, car le rôle d'analyste de
  solutions ?** nécessairement    données oriente l'analyse
  ---------------------------------------------------------------------------

## Tâche 1.3 Réflexion

Le prompt simple donne une réponse plus générale, car il ne précise ni
le rôle attendu ni le type d'analyse souhaité. En ajoutant un rôle clair
d'analyste de données et une tâche précise, l'IA comprend mieux qu'elle
doit évaluer la qualité du fichier et repérer des anomalies spécifiques.
Le résultat devient donc plus pertinent, même si le prompt peut encore
être amélioré avec du contexte, des contraintes et un format de sortie.

# **Section 2**

## Tâche 2.1 Prompt enrichi avec contexte

Tu es un analyste de données spécialisé en qualité, nettoyage et
préparation de données clients. Analyse le fichier clients.csv afin
d'identifier les principaux problèmes de qualité des données : doublons,
valeurs manquantes, formats invalides, dates problématiques, espaces
parasites et incohérences entre les champs.

**CONTEXTE** :

Le fichier clients.csv contient 200 lignes de données clients. Ces
données pourraient être utilisées par une entreprise pour gérer sa base
clients, communiquer avec les clients et produire des analyses fiables.
La qualité des informations est donc importante, car des emails
invalides, des doublons ou des champs manquants peuvent nuire aux
communications, aux rapports et à la prise de décision.

L'objectif est d'obtenir une analyse claire permettant de comprendre les
problèmes présents dans le fichier et de préparer un plan de nettoyage.

## Tâche 2.2 Prompt complet avec contraintes

Tu es un analyste de données spécialisé en qualité, nettoyage et
préparation de données clients.

Analyse le fichier clients.csv afin d'identifier les principaux
problèmes de qualité des données : doublons, valeurs manquantes, formats
invalides, dates problématiques, espaces parasites et incohérences entre
les champs.

+:----------------------------------------------------------------------+
| **CONTEXTE** :                                                        |
|                                                                       |
| Le fichier clients.csv contient 200 lignes de données clients. Ces    |
| données pourraient être utilisées par une entreprise pour gérer sa    |
| base clients, communiquer avec les clients et produire des analyses   |
| fiables. La qualité des informations est donc importante, car des     |
| emails invalides, des doublons ou des champs manquants peuvent nuire  |
| aux communications, aux rapports et à la prise de décision.           |
|                                                                       |
| **CONTRAINTES** :                                                     |
|                                                                       |
| 1\. Identifier tous les types d'anomalies présents dans le fichier.   |
|                                                                       |
| 2\. Quantifier chaque anomalie en indiquant le nombre de lignes       |
| affectées.                                                            |
|                                                                       |
| 3\. Donner des exemples de lignes ou d'identifiants concernés pour    |
| chaque type de problème.                                              |
|                                                                       |
| 4\. Distinguer les problèmes critiques des problèmes moins urgents.   |
|                                                                       |
| 5\. Proposer des actions concrètes de nettoyage et de prévention pour |
| améliorer la qualité des données.                                     |
+-----------------------------------------------------------------------+

## Tâche 2.3 Tableau de Progression

  -----------------------------------------------------------------------
  **Élément**        **Ex 1 : Rôle + **Ex 2 : Avec Contexte +
                     Tâche**         Contraintes**
  ------------------ --------------- ------------------------------------
  Anomalies          Partiellement   Oui, de façon plus systématique
  quantifiées ?                      

  Stratégies         Peu détaillées  Oui, avec des actions concrètes
  proposées ?                        

  Analyse            Moyennement     Oui, car elle peut guider le
  actionnable ?                      nettoyage des données
  -----------------------------------------------------------------------

## Tâche 2.4 Réflexion

L'ajout du contexte permet à l'IA de mieux comprendre pourquoi l'analyse
est importante et à quoi serviront les données. Les contraintes rendent
la réponse plus précise, car elles obligent l'IA à quantifier les
problèmes, à fournir des exemples et à proposer des solutions. Le
résultat devient plus exploitable pour une équipe de données, car il ne
se limite plus à une observation générale. Il devient un outil d'aide à
la décision pour prioriser les corrections.

# **Section 3**

## Tâche 3.1 Prompt avec les 5 composantes

+:----------------------------------------------------------------------+
| **RÔLE** :                                                            |
|                                                                       |
| Tu es un analyste senior en qualité des données, spécialisé dans le   |
| nettoyage, la validation et la préparation de bases de données        |
| clients.                                                              |
|                                                                       |
| **TÂCHE** :                                                           |
|                                                                       |
| Analyse le fichier clients.csv afin de produire un rapport complet de |
| qualité des données. Tu dois identifier, quantifier et expliquer les  |
| anomalies présentes dans le fichier.                                  |
|                                                                       |
| **CONTEXTE** :                                                        |
|                                                                       |
| Le fichier contient 200 lignes de données clients avec les colonnes   |
| suivantes : id, email, first_name, last_name, phone et                |
| registration_date. Ces données peuvent être utilisées pour la         |
| communication client, les analyses internes et le suivi des           |
| inscriptions. Une mauvaise qualité des données peut entraîner des     |
| doublons dans les rapports, des communications impossibles avec       |
| certains clients et des décisions basées sur des informations         |
| incorrectes.                                                          |
|                                                                       |
| Source de données : Fichier CSV clients.csv                           |
|                                                                       |
| Volumétrie : 200 lignes                                               |
|                                                                       |
| Action : Charger et nettoyer les données clients                      |
|                                                                       |
| **CONTRAINTES** :                                                     |
|                                                                       |
| 1\. Identifier les doublons exacts et partiels, notamment les emails  |
| répétés.                                                              |
|                                                                       |
| 2\. Identifier les emails manquants, invalides ou contenant des       |
| espaces parasites.                                                    |
|                                                                       |
| 3\. Identifier les champs manquants dans first_name, last_name et     |
| phone.                                                                |
|                                                                       |
| 4\. Identifier les dates problématiques, notamment les dates futures  |
| ou invalides.                                                         |
|                                                                       |
| 5\. Quantifier chaque anomalie et donner des exemples de lignes/id    |
| affectés.                                                             |
|                                                                       |
| 6\. Proposer une stratégie de nettoyage réaliste et priorisée.        |
|                                                                       |
| 7\. Mentionner les risques si les anomalies ne sont pas corrigées.    |
|                                                                       |
| **FORMAT DE SORTIE** :                                                |
|                                                                       |
| Présente le résultat sous la structure suivante :                     |
|                                                                       |
| RAPPORT D'ANALYSE DE QUALITÉ -- Dataset Clients                       |
|                                                                       |
| 1\. Résumé                                                            |
|                                                                       |
| Présente en 2 à 3 phrases l'état général de la qualité des données.   |
|                                                                       |
| 2\. Anomalies détectées                                               |
|                                                                       |
| A. Doublons                                                           |
|                                                                       |
| \- Type de doublons :                                                 |
|                                                                       |
| \- Nombre de lignes affectées :                                       |
|                                                                       |
| \- Exemples :                                                         |
|                                                                       |
| \- Niveau de priorité :                                               |
|                                                                       |
| B. Emails manquants ou invalides                                      |
|                                                                       |
| \- Emails manquants :                                                 |
|                                                                       |
| \- Emails invalides :                                                 |
|                                                                       |
| \- Exemples :                                                         |
|                                                                       |
| \- Risque associé :                                                   |
|                                                                       |
| C. Téléphones manquants ou invalides                                  |
|                                                                       |
| \- Téléphones manquants :                                             |
|                                                                       |
| \- Téléphones invalides :                                             |
|                                                                       |
| \- Exemples :                                                         |
|                                                                       |
| \- Risque associé :                                                   |
|                                                                       |
| D. Champs nominatifs manquants                                        |
|                                                                       |
| \- first_name manquants :                                             |
|                                                                       |
| \- last_name manquants :                                              |
|                                                                       |
| \- Exemples :                                                         |
|                                                                       |
| \- Risque associé :                                                   |
|                                                                       |
| E. Dates problématiques                                               |
|                                                                       |
| \- Dates invalides :                                                  |
|                                                                       |
| \- Dates futures :                                                    |
|                                                                       |
| \- Exemples :                                                         |
|                                                                       |
| \- Risque associé :                                                   |
|                                                                       |
| F. Espaces parasites                                                  |
|                                                                       |
| \- Champs affectés :                                                  |
|                                                                       |
| \- Nombre de lignes affectées :                                       |
|                                                                       |
| \- Exemples :                                                         |
|                                                                       |
| 3\. Impact estimé sur l'utilisation des données                       |
|                                                                       |
| Explique les conséquences possibles sur les communications, les       |
| analyses et les rapports.                                             |
|                                                                       |
| 4\. Stratégie de nettoyage recommandée                                |
|                                                                       |
| Présente les étapes de nettoyage par ordre de priorité.               |
|                                                                       |
| 5\. Recommandations de prévention                                     |
|                                                                       |
| Propose des règles de validation pour éviter que les mêmes problèmes  |
| se reproduisent.                                                      |
+-----------------------------------------------------------------------+

### Rapport d'analyse de qualité -- Dataset Clients

+:----------------------------------------------------------------------+
| **1. Résumé**                                                         |
|                                                                       |
| L'analyse du fichier **clients.csv**, composé de 200 lignes, montre   |
| que la base de données est globalement exploitable, mais qu'elle      |
| contient plusieurs anomalies importantes. Les principaux problèmes    |
| concernent les emails en doublon, les emails invalides ou manquants,  |
| les téléphones manquants, certains champs nominatifs incomplets et    |
| quelques dates futures. Ces anomalies doivent être corrigées avant    |
| toute utilisation pour des communications clients ou des analyses     |
| fiables.                                                              |
|                                                                       |
| **2. Anomalies détectées**                                            |
|                                                                       |
| **A. Doublons**                                                       |
|                                                                       |
| -   Type de doublons : doublons basés principalement sur les emails   |
|     répétés.                                                          |
|                                                                       |
| -   Nombre de lignes affectées : 16 lignes.                           |
|                                                                       |
| -   Exemples : id 1, 3, 8, 9, 11, 14, 15, 16, 17, 19, 20, 36, 78,     |
|     108, 111, 125.                                                    |
|                                                                       |
| -   Niveau de priorité : élevé.                                       |
|                                                                       |
| Les doublons peuvent fausser le nombre réel de clients et créer des   |
| communications répétées vers les mêmes personnes.                     |
|                                                                       |
| **B. Emails manquants ou invalides**                                  |
|                                                                       |
| -   Emails manquants : 3 lignes.                                      |
|                                                                       |
| -   Exemples : id 7, 13, 106.                                         |
|                                                                       |
| -   Emails invalides : 3 lignes.                                      |
|                                                                       |
| -   Exemples : id 5, 101, 168.                                        |
|                                                                       |
| -   Risque associé : impossibilité de contacter certains clients      |
|                                                                       |
| **C. Téléphones manquants ou invalides**                              |
|                                                                       |
| -   Téléphones manquants : 15 lignes.                                 |
|                                                                       |
| -   Exemples : id 1, 3, 5, 8, 10, 13, 15, 16, 18, 19, 101, 114, 168,  |
|     177, 196.                                                         |
|                                                                       |
| -   Téléphones invalides : 2 lignes.                                  |
|                                                                       |
| -   Exemples : id 125, 126.                                           |
|                                                                       |
| -   Risque associé : difficulté à joindre les clients par téléphone.  |
|                                                                       |
| **D. Champs nominatifs manquants**                                    |
|                                                                       |
| -   first_name manquants : 3 lignes.                                  |
|                                                                       |
| -   Exemples : id 10, 16, 168.                                        |
|                                                                       |
| -   last_name manquants : 1 ligne.                                    |
|                                                                       |
| -   Exemple : id 16.                                                  |
|                                                                       |
| -   Risque associé : difficulté à personnaliser les communications et |
|     à identifier correctement les clients.                            |
|                                                                       |
| **E. Dates problématiques**                                           |
|                                                                       |
| -   Dates invalides : aucune détectée.                                |
|                                                                       |
| -   Dates futures : 2 lignes.                                         |
|                                                                       |
| -   Exemples : id 178, 198.                                           |
|                                                                       |
| -   Risque associé : erreurs dans les analyses temporelles, par       |
|     exemple le suivi des inscriptions par mois ou par année.          |
|                                                                       |
| **F. Espaces parasites**                                              |
|                                                                       |
| -   Champ affecté : email.                                            |
|                                                                       |
| -   Nombre de lignes affectées : 1 ligne.                             |
|                                                                       |
| -   Exemple : id 111.                                                 |
|                                                                       |
| -   Risque associé : difficulté à détecter correctement les doublons  |
|     ou à valider les emails si les espaces ne sont pas supprimés.     |
|                                                                       |
| **3. Impact estimé sur l'utilisation des données**                    |
|                                                                       |
| Ces anomalies peuvent avoir un impact direct sur la qualité des       |
| analyses et des décisions. Les doublons peuvent surestimer le nombre  |
| de clients, tandis que les emails ou téléphones manquants peuvent     |
| réduire l'efficacité des communications. Les champs nominatifs        |
| incomplets limitent la capacité de personnalisation, et les dates     |
| futures peuvent fausser les rapports d'évolution des inscriptions.    |
|                                                                       |
| **4. Stratégie de nettoyage recommandée**                             |
|                                                                       |
| La première étape consiste à normaliser les données textuelles en     |
| supprimant les espaces parasites et en mettant les emails en          |
| minuscules. Ensuite, il faut traiter les emails invalides et          |
| manquants, car ils représentent un risque important pour les          |
| communications. Les doublons doivent être examinés afin de fusionner  |
| les informations utiles, par exemple conserver la ligne la plus       |
| complète lorsque deux enregistrements partagent le même email. Les    |
| téléphones doivent être validés selon un format standard, et les      |
| dates futures doivent être corrigées ou confirmées avec la source des |
| données.                                                              |
|                                                                       |
| **5. Recommandations de prévention**                                  |
|                                                                       |
| Pour éviter la répétition de ces erreurs, il est recommandé d'imposer |
| des règles de validation au moment de la saisie. Le champ email       |
| devrait être obligatoire et respecter un format valide. Le téléphone  |
| devrait suivre un format standard, par exemple un numéro commençant   |
| par +33. Les champs first_name et last_name devraient être            |
| obligatoires. Enfin, la date d'inscription ne devrait pas pouvoir     |
| être supérieure à la date du jour.                                    |
+-----------------------------------------------------------------------+

## Tâche 3.2 Checklist de Validation

  -------------------------------------------------------------------------------
  **Critère**           **Validation**   **Commentaire**
  --------------------- ---------------- ----------------------------------------
  Toutes les 5 sections Oui              Le rapport contient les 5 sections
  présentes ?                            demandées.

  Résumé exécutif clair Oui              Il présente l'état général des données
  ?                                      en quelques phrases.

  Anomalies quantifiées Oui              Chaque type d'anomalie est accompagné
  ?                                      d'un nombre de lignes.

  Stratégie de          Oui              Les étapes de nettoyage sont priorisées.
  nettoyage proposée ?                   

  Impact estimé calculé Oui              Les impacts sur les communications et
  ?                                      les analyses sont expliqués.

  Risques identifiés ?  Oui              Chaque anomalie est liée à un risque
                                         métier.
  -------------------------------------------------------------------------------

# **Section 4**

## Tâche 4.1 Prompt Chain-of-Thought complet

+:----------------------------------------------------------------------+
| **RÔLE** :                                                            |
|                                                                       |
| Tu es un développeur Python senior spécialisé en analyse de données,  |
| en débogage de scripts pandas avec 10 ans d\'expérience en traitement |
| de fichiers CSV. Tu es un expert de la donnée spécialisé dans         |
| l\'analyse d\'anomalies de données et les stratégies de déduplication |
| multi-sources avec expertise en diagnostique de transformations ETL   |
| complexes.                                                            |
|                                                                       |
| **TÂCHE** :                                                           |
|                                                                       |
| Analyse le log d'erreur ci-dessous afin de diagnostiquer précisément  |
| pourquoi le script Python a planté. Tu dois identifier l'erreur,      |
| expliquer sa cause, mesurer son impact sur le traitement du fichier   |
| clients.csv, proposer une correction du code et recommander des       |
| mesures de prévention.                                                |
|                                                                       |
| **CONTEXTE** :                                                        |
|                                                                       |
| Un script Python d'analyse de qualité des données clients a été       |
| exécuté sur un fichier nommé clients.csv contenant 200 lignes. Le     |
| script devait vérifier et nettoyer les emails des clients. Cependant, |
| il s'est arrêté pendant le traitement, après seulement 6 lignes       |
| analysées. L'erreur se produit à la ligne 7 du fichier de données,    |
| lorsque la valeur du champ email est None.                            |
|                                                                       |
| Source de données : Fichier CSV clients.csv                           |
|                                                                       |
| Volumétrie : 200 lignes                                               |
|                                                                       |
| Action : Charger et nettoyer les données clients                      |
|                                                                       |
| [LOG À ANALYSER :]{.underline}                                        |
|                                                                       |
| === DÉBUT DU LOG ===                                                  |
|                                                                       |
| \[2026-03-06 14:32:15\] INFO - Démarrage du script d\'analyse de      |
| données clients                                                       |
|                                                                       |
| \[2026-03-06 14:32:15\] INFO - Chargement du fichier clients.csv      |
|                                                                       |
| \[2026-03-06 14:32:16\] INFO - 200 lignes chargées avec succès        |
|                                                                       |
| \[2026-03-06 14:32:16\] INFO - Début de l\'analyse de qualité des     |
| données                                                               |
|                                                                       |
| \[2026-03-06 14:32:16\] DEBUG - Vérification des emails en cours\...  |
|                                                                       |
| \[2026-03-06 14:32:16\] DEBUG - Traitement de la ligne 1:             |
| alice@company.com                                                     |
|                                                                       |
| \[2026-03-06 14:32:16\] DEBUG - Traitement de la ligne 2:             |
| bob@company.com                                                       |
|                                                                       |
| \[2026-03-06 14:32:16\] DEBUG - Traitement de la ligne 3:             |
| alice@company.com                                                     |
|                                                                       |
| \[2026-03-06 14:32:16\] DEBUG - Traitement de la ligne 4:             |
| charlie@test.fr                                                       |
|                                                                       |
| \[2026-03-06 14:32:16\] DEBUG - Traitement de la ligne 5:             |
| invalid-email                                                         |
|                                                                       |
| \[2026-03-06 14:32:17\] ERROR - Une erreur est survenue lors du       |
| traitement                                                            |
|                                                                       |
| Traceback (most recent call last):                                    |
|                                                                       |
| File \"analyze_data_quality.py\", line 87, in process_customer_data   |
|                                                                       |
| cleaned_email = email.strip().lower()                                 |
|                                                                       |
| AttributeError: \'NoneType\' object has no attribute \'strip\'        |
|                                                                       |
| \[2026-03-06 14:32:17\] DEBUG - Contexte de l\'erreur:                |
|                                                                       |
| \- Ligne en cours de traitement: 7                                    |
|                                                                       |
| \- Données de la ligne: {\'id\': 7, \'email\': None, \'first_name\':  |
| \'Frank\', \'last_name\': \'Moreau\', \'phone\': \'+33789123456\',    |
| \'registration_date\': \'2024-02-10\'}                                |
|                                                                       |
| \- Fonction appelante: validate_and_clean_emails()                    |
|                                                                       |
| \- État de la variable \'email\': None (type: \<class \'NoneType\'\>) |
|                                                                       |
| \[2026-03-06 14:32:17\] INFO - Le script s\'est arrêté après avoir    |
| traité 6 lignes sur 200                                               |
|                                                                       |
| \[2026-03-06 14:32:17\] ERROR - Script terminé avec erreur - Code 1   |
|                                                                       |
| === FIN DU LOG ===                                                    |
|                                                                       |
| **CONTRAINTES** :                                                     |
|                                                                       |
| 1\. Avant de donner la réponse finale, décris ton raisonnement étape  |
| par étape en suivant obligatoirement cette progression :              |
| Identification → Cause → Impact → Solution → Prévention.              |
|                                                                       |
| 2\. Ne saute pas directement à la correction du code. Explique        |
| d'abord ce que le log montre.                                         |
|                                                                       |
| 3\. Identifie clairement le type d'erreur, la ligne de code           |
| responsable et la variable problématique.                             |
|                                                                       |
| 4\. Explique pourquoi la valeur None provoque une erreur lorsque le   |
| script exécute email.strip().lower().                                 |
|                                                                       |
| 5\. Propose une correction simple du code, compréhensible pour un     |
| étudiant débutant en Python.                                          |
|                                                                       |
| 6\. Propose aussi une correction plus robuste adaptée à un traitement |
| de données avec pandas.                                               |
|                                                                       |
| 7\. Termine avec des recommandations pour éviter que ce type d'erreur |
| bloque à nouveau le traitement complet du fichier.                    |
|                                                                       |
| **FORMAT DE SORTIE** :                                                |
|                                                                       |
| Présente la réponse avec la structure suivante :                      |
|                                                                       |
| \## Diagnostic de l'erreur Python                                     |
|                                                                       |
| \### 1. Identification de l'erreur                                    |
|                                                                       |
| \- Type d'erreur :                                                    |
|                                                                       |
| \- Ligne de code concernée :                                          |
|                                                                       |
| \- Variable problématique :                                           |
|                                                                       |
| \- Ligne du fichier clients.csv concernée :                           |
|                                                                       |
| \### 2. Analyse de la cause racine                                    |
|                                                                       |
| Explique pourquoi l'erreur se produit.                                |
|                                                                       |
| \### 3. Impact sur le traitement des données                          |
|                                                                       |
| Explique les conséquences sur le script et sur l'analyse des 200      |
| lignes.                                                               |
|                                                                       |
| \### 4. Solution proposée                                             |
|                                                                       |
| Présente une correction simple du code, puis une correction plus      |
| robuste avec pandas.                                                  |
|                                                                       |
| \### 5. Mesures de prévention                                         |
|                                                                       |
| Présente au moins trois bonnes pratiques pour éviter ce problème à    |
| l'avenir.                                                             |
|                                                                       |
| \### 6. Conclusion                                                    |
|                                                                       |
| Résume le diagnostic et la solution en quelques phrases.              |
+-----------------------------------------------------------------------+

### Résultat obtenu après exécution du prompt Chain-of-Thought

+:----------------------------------------------------------------------+
| **Diagnostic de l'erreur Python**                                     |
|                                                                       |
| [1. Identification de l'erreur]{.underline}                           |
|                                                                       |
| -   Type d'erreur : AttributeError                                    |
|                                                                       |
| -   Ligne de code concernée : cleaned_email = email.strip().lower()   |
|                                                                       |
| -   Variable problématique : email                                    |
|                                                                       |
| -   Valeur de la variable : None                                      |
|                                                                       |
| -   Ligne du fichier clients.csv concernée : ligne 7                  |
|                                                                       |
| Le log montre que le script a bien commencé son exécution. Il a       |
| chargé le fichier clients.csv, qui contient 200 lignes, puis il a     |
| commencé la vérification des emails. Les premières lignes ont été     |
| traitées, mais le script s'est arrêté au moment où il a rencontré une |
| valeur manquante dans la colonne email.                               |
|                                                                       |
| L'erreur indique que Python essaie d'utiliser la méthode .strip() sur |
| une valeur de type NoneType. Or, .strip() est une méthode qui         |
| s'applique aux chaînes de caractères, par exemple \" texte \", mais   |
| pas aux valeurs nulles comme None.                                    |
|                                                                       |
| [2. Analyse de la cause racine]{.underline}                           |
|                                                                       |
| La cause principale de l'erreur est que le champ email est vide à la  |
| ligne 7 du fichier. Cette valeur vide a été lue comme None par le     |
| script. Ensuite, le programme a tenté d'exécuter cette instruction :  |
|                                                                       |
| cleaned_email = email.strip().lower()                                 |
|                                                                       |
| Cette ligne suppose que la variable email contient toujours du texte. |
| Pourtant, dans le fichier, certains clients peuvent avoir un email    |
| manquant. Lorsque email = None, Python ne peut pas faire              |
| email.strip(), car None n'est pas une chaîne de caractères.           |
|                                                                       |
| Autrement dit, le script n'a pas prévu le cas des valeurs manquantes  |
| avant d'appliquer des méthodes de nettoyage comme .strip() et         |
| .lower().                                                             |
|                                                                       |
| 3\. Impact sur le traitement des données                              |
|                                                                       |
| L'impact est important, car le script s'est arrêté après seulement 6  |
| lignes traitées sur 200. Cela signifie que les 194 lignes restantes   |
| n'ont pas été analysées. Les autres anomalies possibles, comme les    |
| doublons, les emails invalides, les téléphones manquants ou les dates |
| problématiques, n'ont donc pas pu être détectées.                     |
|                                                                       |
| Cette erreur rend le processus d'analyse incomplet. Elle empêche      |
| aussi la production d'un rapport fiable sur la qualité des données.   |
| Dans un contexte professionnel, ce type de problème peut bloquer une  |
| pipeline de données et retarder la prise de décision.                 |
|                                                                       |
| 4\. Solution proposée                                                 |
|                                                                       |
| Une première solution simple consiste à vérifier si l'email est       |
| manquant avant d'utiliser .strip() et .lower().                       |
|                                                                       |
| email = row\[\"email\"\]                                              |
|                                                                       |
| if email is None:                                                     |
|                                                                       |
| cleaned_email = None                                                  |
|                                                                       |
| else:                                                                 |
|                                                                       |
| cleaned_email = email.strip().lower()                                 |
|                                                                       |
| Cette correction évite que le script plante lorsque l'email est vide. |
| Si l'email est None, on garde la valeur None. Sinon, on nettoie       |
| l'email normalement.                                                  |
|                                                                       |
| Une version un peu plus complète serait :                             |
|                                                                       |
| email = row\[\"email\"\]                                              |
|                                                                       |
| if email is None or email == \"\":                                    |
|                                                                       |
| cleaned_email = None                                                  |
|                                                                       |
| else:                                                                 |
|                                                                       |
| cleaned_email = email.strip().lower()                                 |
|                                                                       |
| Cette version gère à la fois les valeurs None et les chaînes vides.   |
|                                                                       |
| Pour un traitement plus robuste avec pandas, on peut utiliser :       |
|                                                                       |
| df\[\"email\"\] =                                                     |
| df\[\"email\"\].fillna(\"\").astype(str).str.strip().str.lower()      |
|                                                                       |
| Cette solution remplace les valeurs manquantes par une chaîne vide,   |
| transforme les valeurs en texte, supprime les espaces au début et à   |
| la fin, puis met les emails en minuscules.                            |
|                                                                       |
| Après cela, on peut identifier les emails vides avec :                |
|                                                                       |
| emails_manquants = df\[df\[\"email\"\] == \"\"\]                      |
|                                                                       |
| Cette approche est plus adaptée à l'analyse d'un fichier complet, car |
| elle permet de continuer le traitement même si certaines valeurs sont |
| manquantes.                                                           |
|                                                                       |
| 5\. Mesures de prévention                                             |
|                                                                       |
| Pour éviter ce type d'erreur à l'avenir, il faut d'abord ajouter une  |
| étape de validation des valeurs manquantes avant le nettoyage des     |
| données. Le script ne doit jamais supposer que tous les champs        |
| contiennent du texte valide.                                          |
|                                                                       |
| Ensuite, il est recommandé de créer une fonction de nettoyage         |
| réutilisable pour les emails. Par exemple :                           |
|                                                                       |
| def nettoyer_email(email):                                            |
|                                                                       |
| if email is None:                                                     |
|                                                                       |
| return None                                                           |
|                                                                       |
| email = str(email).strip().lower()                                    |
|                                                                       |
| if email == \"\" or email == \"null\":                                |
|                                                                       |
| return None                                                           |
|                                                                       |
| return email                                                          |
|                                                                       |
| Cette fonction permet de gérer plusieurs cas problématiques : valeur  |
| None, chaîne vide, valeur \"null\" écrite sous forme de texte,        |
| espaces parasites et différences de majuscules/minuscules.            |
|                                                                       |
| Il faut aussi ajouter des logs pour signaler les anomalies sans       |
| arrêter complètement le script. Par exemple, au lieu de planter, le   |
| programme pourrait enregistrer que la ligne 7 contient un email       |
| manquant et continuer avec les autres lignes.                         |
|                                                                       |
| Enfin, il serait utile d'ajouter des tests sur des cas particuliers   |
| avant d'exécuter le script sur tout le fichier. Ces tests devraient   |
| inclure un email valide, un email vide, une valeur None, un email     |
| avec espaces et un email invalide.                                    |
+-----------------------------------------------------------------------+

## Tâche 4.2 Justification du Prompt

J'ai choisi le rôle de développeur Python senior spécialisé en analyse
de données, parce que l'erreur concerne à la fois le langage Python, le
traitement d'un fichier CSV et la qualité des données. Ce rôle est plus
précis qu'un simple rôle d'informaticien, car il oriente l'IA vers une
réponse adaptée au contexte des données.

Les contraintes ont été structurées pour forcer une analyse étape par
étape. La prompte demande explicitement de suivre la progression
Identification → Cause → Impact → Solution → Prévention. Cette structure
empêche l'IA de donner directement une correction sans expliquer le
diagnostic. Elle oblige aussi l'IA à expliquer la ligne responsable, la
variable problématique et la raison pour laquelle la valeur None
provoque une erreur.

Le format choisi reprend une logique de diagnostic professionnel. Il
permet de séparer clairement l'identification du problème, la cause
racine, l'impact, la solution et la prévention. Cette structure rend la
réponse facile à comprendre et directement utile pour corriger le
script.

## Tâche 4.3 Comparaison : Prompt Simple vs Chain-of-Thought

Prompt simple testé : Analyse cette erreur Python et propose une
solution. \[log\]

  ------------------------------------------------------------------------
  **Critère**           **Prompt Simple**    **Chain-of-Thought**
  --------------------- -------------------- -----------------------------
  Identifie la cause    Oui, mais parfois    Oui, avec une explication
  racine ?              brièvement           détaillée

  Explique le           Partiellement        Oui, étape par étape
  raisonnement ?                             

  Analyse l'impact ?    Pas toujours         Oui, impact sur le traitement
                                             des 200 lignes

  Propose une solution  Oui, mais souvent    Oui, avec code corrigé et des
  détaillée ?           courte               explications

  Suggère des           Rarement             Oui, avec bonnes pratiques
  préventions ?                              
  ------------------------------------------------------------------------

## Tâche 4.4 Réflexion finale

La valeur ajoutée du Chain-of-Thought est qu'il oblige l'IA à produire
une analyse plus structurée et plus fiable. Au lieu de donner
directement une solution, l'IA explique d'abord le problème, sa cause et
ses conséquences. Cela permet de mieux comprendre l'erreur et d'éviter
de la reproduire dans d'autres scripts. Cette approche est
particulièrement utile dans les situations complexes, comme le débogage
de code, l'analyse de logs, la résolution d'erreurs dans une pipeline de
données ou la vérification de la qualité d'une base de données. Elle est
aussi utile en contexte professionnel, car elle transforme une simple
réponse technique exploitable. Grâce à cette méthode, l'utilisateur peut
non seulement corriger l'erreur, mais aussi améliorer la robustesse de
son processus de traitement des données.
