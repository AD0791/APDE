# Guide de préparation — Examen final
## Cours 420-C47-BB : Analyse et conception d'une solution de données

> **Méthode Pareto 20/80** — Partie I : les 20 % de matière qui rapportent ~80 % des points.
> Partie II : compléments à ne pas négliger pour viser l'excellence (le « delta » final).
>
> Document construit à partir de `cours_conception_basededonnee.md` (Cours 1, 5, 7, 8, 9, 10, 11) et enrichi par recherche web ciblée (MERISE, ACID, NoSQL, REST, UML, Data Warehouse/Lake).

---

## Sommaire

- [PARTIE I — Le noyau 20/80 (à maîtriser absolument)](#partie-i--le-noyau-2080-à-maîtriser-absolument)
  - [1. MCD : du diagramme de classes aux tables](#1-mcd--du-diagramme-de-classes-aux-tables)
  - [2. Cardinalités UML & MERISE](#2-cardinalités-uml--merise)
  - [3. Diagramme de classes UML (relations)](#3-diagramme-de-classes-uml-relations)
  - [4. SQL vs NoSQL & les 4 familles NoSQL](#4-sql-vs-nosql--les-4-familles-nosql)
  - [5. Propriétés ACID](#5-propriétés-acid)
  - [6. Architectures classiques (3-tiers, microservices, REST)](#6-architectures-classiques-3-tiers-microservices-rest)
  - [7. Architectures analytiques : Data Warehouse, Data Lake, ETL](#7-architectures-analytiques--data-warehouse-data-lake-etl)
  - [8. Triade CIA + 6 piliers de la consommation de données](#8-triade-cia--6-piliers-de-la-consommation-de-données)
  - [9. Les 6 dimensions de la qualité des données](#9-les-6-dimensions-de-la-qualité-des-données)
  - [10. Cycle de vie du logiciel & cycle de vie de la donnée](#10-cycle-de-vie-du-logiciel--cycle-de-vie-de-la-donnée)
- [PARTIE II — Compléments (le delta vers l'excellence)](#partie-ii--compléments-le-delta-vers-lexcellence)
- [Annexe — Anti-sèche express (à relire la veille)](#annexe--anti-sèche-express-à-relire-la-veille)
- [Sources](#sources)

---

# PARTIE I — Le noyau 20/80 (à maîtriser absolument)

> Ces 10 blocs représentent l'essentiel du barème d'un examen final type. Chaque section suit la même trame : **Définition → Mémo visuel → Pièges classiques → Modèle de question**.

---

## 1. MCD : du diagramme de classes aux tables

### Définition
Le **MCD** (Modèle Conceptuel de Données) — méthode **MERISE** ou notation **Entité-Association** — décrit *quoi* stocker et *comment* c'est relié, indépendamment du SGBD. C'est le pont entre l'analyse (UML) et la base physique (SQL).

> Réponse à la question : **« quelles données stocker et comment sont-elles reliées ? »**

### Les 4 règles de passage Classe → MCD → Table
| # | Règle | Traduction technique |
|---|-------|----------------------|
| 1 | Classe persistante → **Entité** | Devient une **table** |
| 2 | Attribut → **Colonne** | Le type guide le `VARCHAR`, `INT`, `DATE`, `DECIMAL(p,s)`… |
| 3 | Identifiant → **Clé primaire (PK)** | `NOT NULL`, unique. Sinon, créer un id artificiel (`idClient`) |
| 4 | Association → **FK** ou **table de jonction** | Dépend de la cardinalité (voir §2) |

### Stratégie de traduction selon la cardinalité
| Cardinalité | Stratégie de passage | Exemple |
|-------------|----------------------|---------|
| **1..1** | Ajouter la PK d'une table comme **FK** dans l'autre (souvent avec `UNIQUE`) | `Membre 1..1 Carte` → `CARTE(num_carte PK, id_membre FK UNIQUE)` |
| **1..N** | Mettre la PK du côté « 1 » comme **FK** dans la table du côté « N » | `Client 1..N Commande` → `COMMANDE(idCmd PK, idClient FK)` |
| **N..M** | Créer une **table de jonction** contenant les deux FK (PK composite) | `Livre N..M Auteur` → `ECRIRE(isbn FK, idAuteur FK, PK(isbn, idAuteur))` |

### Pièges classiques
- ❌ Oublier qu'une cardinalité **1..1 obligatoire** des deux côtés peut justifier de **fusionner les tables**.
- ❌ Mettre une FK du « mauvais » côté en 1..N (toujours côté N).
- ❌ Sur une N..M, oublier la **PK composite** de la table de jonction.
- ❌ Confondre **MCD** (structure) et **DFD** (flux).

### Modèle de question
> *« Voici un énoncé… Donnez le MCD puis le schéma relationnel correspondant. »*
> → Identifier les entités (noms communs persistants), les attributs, les identifiants, puis les associations avec cardinalités, puis appliquer les 4 règles.

---

## 2. Cardinalités UML & MERISE

### Notation
- **UML** : on note `min..max` du côté de la classe **cible** (ex : `1..*`, `0..1`).
- **MERISE** : on note `min,max` du côté de l'entité **de départ** de la relation (sens opposé à UML).

### Les valeurs canoniques
| Notation | Signification |
|----------|---------------|
| `0..1` / `0,1` | **Optionnel**, au plus un |
| `1..1` / `1,1` | **Exactement un** (obligatoire) |
| `0..*` / `0,n` | Zéro ou plusieurs |
| `1..*` / `1,n` | Au moins un (obligatoire, plusieurs possibles) |
| `2..5` / `2,5` | Plage explicite |

### Lecture systématique
> **« Un X est associé à combien de Y, au minimum et au maximum ? »** — répétez la question dans les deux sens. Toute association a **deux cardinalités** (une par côté).

### Conversion en règle de passage (rappel synthèse)
- `1..1 ↔ 0..1/1..1` → fusion possible ou FK avec contrainte `UNIQUE`.
- `0..1/1..1 ↔ 0..*/1..*` → FK du côté multiple, pointant vers le côté unique.
- `0..*/1..* ↔ 0..*/1..*` → **table associative** (jonction).

### Piège classique
> Un énoncé qui dit *« un livre est écrit par **au moins** un auteur »* impose la cardinalité minimale `1`, pas `0`. À ne jamais oublier dans la phase d'analyse de texte.

---

## 3. Diagramme de classes UML (relations)

### Trois types de relations à reconnaître
| Relation | Symbole | Sémantique | Exemple |
|----------|---------|------------|---------|
| **Association** | Trait simple `—` | Lien structurel entre pairs | `Client — Commande` |
| **Agrégation** | Losange **vide** `◇` | « A possède B », vie indépendante | `Playlist ◇— Morceau` (un morceau survit à la playlist) |
| **Composition** | Losange **plein** `◆` | « A *contient* B », vie liée | `Facture ◆— Ligne` (les lignes meurent avec la facture) |

> **Mnémo** : « **vide = libre**, **plein = lié à la vie ou à la mort** ».

### Anatomie d'une classe UML
Rectangle divisé en **3 compartiments** :
1. **Nom** (en haut, centré, capitales).
2. **Attributs** : `visibilité nom : Type [= valeur]` (ex : `- prix : Decimal`).
3. **Méthodes** : `visibilité nom(paramètres) : TypeRetour`.

Visibilités : `+` public, `-` privé, `#` protégé, `~` package.

### Origine des classes (méthode des noms)
> Dans le texte des exigences, **chaque nom commun désigne une classe candidate**.
> Filtres :
> - Est-ce que ça **se stocke** ? Probablement une classe.
> - Est-ce une **personne, un objet, un document** ? Souvent oui.
> - Est-ce un **simple rôle ou attribut** ? Pas forcément (ex : « rouge » n'est pas une classe).

### Piège classique
- Modéliser en composition ce qui devrait être agrégation (et inversement). Test : *« si je détruis le tout, est-ce que la partie disparaît aussi ? »* — Oui → composition.

---

## 4. SQL vs NoSQL & les 4 familles NoSQL

### Décision binaire SQL vs NoSQL
| Critère | SQL (relationnel) | NoSQL |
|---------|-------------------|-------|
| **Structure** | Bien définie, stable | Variable, évolutive |
| **Volume** | Requêtes analytiques complexes | Millions d'écritures distribuées |
| **Relations** | Nombreuses (jointures) | Données indépendantes |
| **Cohérence** | Stricte (banque, ERP) | Éventuelle acceptable |
| **Schéma** | Fixe (à définir avant) | Flexible (schema-on-read) |
| **Scalabilité** | Verticale | Horizontale (native) |
| **Exemples** | PostgreSQL, MySQL, Oracle, SQL Server | MongoDB, Redis, Cassandra, Neo4j |

> Dans la pratique : **coexistence**. On utilise le bon outil pour chaque partie du système.

### Les 4 familles NoSQL
| Famille | Modèle | Forces | Cas d'usage typiques | Acteurs |
|---------|--------|--------|----------------------|---------|
| **Documentaire** | JSON par document, schéma flexible | Modèle proche du code applicatif | Catalogues produits, profils utilisateurs, CMS, blogging | **MongoDB**, CouchDB |
| **Clé-Valeur** | `clé → valeur`, parfois en RAM | Le plus rapide, ultra-simple | Cache, sessions, files d'attente, classements temps réel | **Redis**, DynamoDB |
| **Colonnes** | Stockage par colonne, pas par ligne | Lecture massive sélective, écritures massives | Logs, IoT, historique de transactions, Big Data | **Cassandra** (haute dispo : Netflix, Instagram), HBase (Hadoop) |
| **Graphes** | Nœuds + arêtes natifs | Traversées relationnelles natives, sans jointure | Réseaux sociaux, recommandations, fraude, télécoms | **Neo4j** (langage Cypher), ArangoDB |

### Mnémo pour choisir
> *« Mes données ressemblent à : un **dossier** (Documentaire), une **étiquette sur un casier** (Clé-Valeur), une **immense feuille Excel** (Colonnes), ou une **toile d'araignée** (Graphes) ? »*

### Piège classique
> Croire que NoSQL = « sans schéma ». Faux : le schéma existe, il est juste **géré côté application** (schema-on-read). Cela transfère la responsabilité mais ne l'élimine pas.

---

## 5. Propriétés ACID

> **Garanties d'une transaction fiable en SGBD relationnel.**

| Lettre | Propriété | Définition opérationnelle |
|--------|-----------|---------------------------|
| **A** | **Atomicité** | « Tout ou rien ». Si une étape échoue, **toute la transaction est annulée** (rollback). |
| **C** | **Cohérence** | La transaction **respecte les contraintes d'intégrité** (PK, FK, CHECK, NOT NULL). L'état avant et après est valide. |
| **I** | **Isolation** | Les transactions concurrentes ne se voient pas pendant leur exécution ; le résultat doit être équivalent à un ordre séquentiel. |
| **D** | **Durabilité** | Une fois `COMMIT`, les données **survivent** à toute panne (crash, coupure, etc.) — généralement via journal/WAL. |

### Exemple canonique : virement bancaire
```
BEGIN TRANSACTION;
  UPDATE Compte SET solde = solde - 100 WHERE id = 'A';  -- Débit
  UPDATE Compte SET solde = solde + 100 WHERE id = 'B';  -- Crédit
COMMIT;
```
- **A** : si le crédit échoue, le débit est annulé.
- **C** : la somme totale des soldes reste constante.
- **I** : un autre virement parallèle ne lit pas un état intermédiaire.
- **D** : après `COMMIT`, le virement survit à un crash serveur.

### Opposition ACID vs BASE (NoSQL)
- **BASE** = **B**asically **A**vailable, **S**oft state, **E**ventually consistent. Sacrifie la cohérence stricte pour la scalabilité et la disponibilité (théorème **CAP**).

### Pièges classiques
- ❌ Confondre **Cohérence ACID** (contraintes respectées) avec la **cohérence CAP** (vue identique sur tous les nœuds).
- ❌ Penser que **isolation** = « privée ». Non : c'est l'**absence d'interférence visible** entre transactions.

---

## 6. Architectures classiques (3-tiers, microservices, REST)

### Architecture client-serveur
- **Client** : demande des services (interface, UI).
- **Serveur** : fournit les ressources, centralise.
- ➕ Centralisation, sécurité, partage. ➖ Point de défaillance unique (SPOF), dépendance réseau.

### Architecture 3-tiers (évolution naturelle)
| Couche | Rôle |
|--------|------|
| **Présentation** | Interface utilisateur (web, mobile, desktop) |
| **Logique / applicative (métier)** | Traitements, règles, validations |
| **Données** | SGBD, persistance |

➕ Modularité, chaque couche évolue indépendamment, maintenance simplifiée.
➖ Plus lourd que monolithique pour les très petites apps.

### Architecture microservices
> Décomposition en **petits services indépendants**, chacun avec **sa propre base** et son cycle de vie. Communication via API (REST, messages).

| ➕ Avantages | ➖ Défis |
|-------------|---------|
| Indépendance de déploiement | Complexité opérationnelle |
| Scalabilité fine (service par service) | Transactions distribuées difficiles |
| Résilience accrue | Latence réseau |
| Polyglottisme technologique | Monitoring distribué |
| Équipes autonomes | Gouvernance des contrats d'API |

### REST en 6 contraintes (à mémoriser)
1. **Interface uniforme** : verbes HTTP standard.
2. **Client-serveur** : séparation des préoccupations.
3. **Stateless** : chaque requête est autonome (auth, contexte).
4. **Cacheable** : réponses marquables comme cachables.
5. **Système en couches** : intermédiaires (proxy, gateway) invisibles.
6. **Code à la demande** (optionnel) : envoi de scripts exécutables.

### Verbes HTTP & ressources
| Verbe | Action | Idempotent ? |
|-------|--------|--------------|
| `GET` | Lire | ✅ |
| `POST` | Créer | ❌ |
| `PUT` | Modifier (remplacer) | ✅ |
| `PATCH` | Modifier partiellement | ❌ (selon impl.) |
| `DELETE` | Supprimer | ✅ |

> Une **ressource** est identifiée par une **URI unique** (ex : `/customers/42/orders/7`). On utilise des **noms au pluriel**, jamais de verbes (`/getUser` est anti-pattern).

### Mnémo synthèse architectures
| Style | Quand l'utiliser |
|-------|------------------|
| **Monolithe** | Petite équipe, MVP, simplicité |
| **3-tiers** | Standard d'entreprise, équilibre flexibilité/simplicité |
| **Microservices** | Équipes nombreuses, scalabilité fine, agilité, polyglottisme |
| **Centralisée** | Cohérence stricte (banques, ERP) |
| **Fédérée** | Autonomie des départements, pas de SPOF |

---

## 7. Architectures analytiques : Data Warehouse, Data Lake, ETL

### Data Warehouse (entrepôt)
- **Schéma fixe**, données **nettoyées, transformées, historisées, agrégées**.
- Optimisé pour **requêtes analytiques** complexes (BI, reporting).
- Modèle **schema-on-write** (structure définie avant ingestion).
- Exemples : Amazon Redshift, BigQuery, Snowflake, Azure Synapse.

### Data Lake (lac)
- Stocke des données **brutes** dans leur format natif (structurées, semi-structurées, **non structurées**).
- **Schema-on-read** : la structure est appliquée au moment de l'analyse.
- Stockage objet à bas coût (S3, Azure Blob, GCS).
- Idéal pour Big Data, Data Science, ML.

### Data Hub
- Point central **d'échange et distribution** entre systèmes. Ne stocke pas forcément.

### Tableau comparatif
| Critère | Data Warehouse | Data Lake |
|---------|----------------|-----------|
| Type de données | Structurées | Toutes (struct, semi, non struct) |
| Schéma | Imposé à l'écriture | Appliqué à la lecture |
| Utilisateurs cibles | Analystes BI, dirigeants | Data scientists, ingénieurs |
| Performance des requêtes | Très haute (optimisé) | Variable (dépend du moteur) |
| Coût stockage | Élevé (structuré) | Bas (objet) |
| Cas d'usage | Reporting historique, KPIs | ML, exploration, archivage massif |

> **Lakehouse** (Databricks, Delta Lake) : tendance hybride qui combine la flexibilité du lac et la gouvernance du warehouse.

### ETL (Extract — Transform — Load)
1. **Extract** : extraction depuis sources hétérogènes (SGBD, API, fichiers).
2. **Transform** : nettoyage, conversion, agrégation, enrichissement, déduplication.
3. **Load** : chargement dans la cible (DW, DL).

> Variante moderne **ELT** : on charge d'abord brut (dans le DW/DL puissant) puis on transforme avec le moteur cible. Adapté au cloud (Snowflake, BigQuery).

---

## 8. Triade CIA + 6 piliers de la consommation de données

### La triade CIA (sécurité)
| Pilier | Définition | Moyens |
|--------|------------|--------|
| **Confidentialité** | Seuls les autorisés accèdent | Authentification (mot de passe, **MFA**), gestion d'accès (**IAM**), chiffrement, VPN, sensibilisation |
| **Intégrité** | Données non altérées sans autorisation | Hash, signatures numériques, journalisation (logs), contrôles de validation, sauvegardes |
| **Disponibilité** | Accessibles quand on en a besoin | Sauvegardes auto, redondance, **PRA** (plan de reprise), monitoring, protection DDoS |

### Notions associées
- **Données personnelles** : toute info identifiant directement ou indirectement (nom, email, IP, etc.). Soumises à **RGPD/Loi 25 (Québec)**.
- **Anonymisation** : transformation rendant l'identification impossible (irréversible).
- **Pseudonymisation** : remplacement par un identifiant (réversible avec clé).
- **Chiffrement** : transit (HTTPS/TLS) + repos (AES-256).
- **IAM** : utilisateurs, rôles, permissions, authentifications.
- **Moindre privilège** : un utilisateur n'a que les droits **strictement nécessaires** à sa mission.

### Les 6 piliers de la consommation de données (Cours 11)
| Pilier | Enjeu central | Exemple concret |
|--------|---------------|-----------------|
| **Authentification** | Bloquer les accès illégitimes, tracer | OAuth2, JWT, MFA |
| **Chiffrement** | Confidentialité absolue, conformité légale | TLS en transit, AES-256 au repos |
| **Latence** | Expérience utilisateur, temps réel | CDN, edge computing, géolocalisation des serveurs |
| **Intégrité** | Pas de corruption ni manipulation | Hash SHA-256, signatures, checksums |
| **Traçabilité** | Audits, débogage, obligations légales | Logs centralisés, journal d'événements |
| **Résilience** | Continuité de service 24/7 | Multi-zone, multi-region, basculement automatique |

> **Mnémo (ACLITR)** : **A**uthentification — **C**hiffrement — **L**atence — **I**ntégrité — **T**raçabilité — **R**ésilience.

---

## 9. Les 6 dimensions de la qualité des données

| Dimension | Question à se poser | Contre-exemple |
|-----------|---------------------|----------------|
| **Exactitude** | Reflète-t-elle la réalité ? | Prix d'un produit erroné |
| **Complétude** | Tous les champs requis sont-ils remplis ? | Client sans email |
| **Cohérence** | Identique d'un système à l'autre ? | Deux bases avec des soldes différents |
| **Fraîcheur (Timeliness)** | À jour ? | Prix non rafraîchis depuis une semaine |
| **Unicité** | Pas de doublons ? | Même client enregistré 2 fois |
| **Validité** | Respecte le format attendu ? | Code postal à 4 chiffres au lieu de 6 caractères |

### Indicateurs mesurables
- % de champs complétés, % d'erreurs détectées, nombre de doublons, taux de conformité aux règles.

### Pourquoi la qualité ?
> **Garbage In, Garbage Out**. Des données médiocres → décisions erronées, modèles ML inefficaces, perte de confiance, non-conformité légale.

> La qualité est une **responsabilité partagée** entre équipes techniques et équipes métiers.

---

## 10. Cycle de vie du logiciel & cycle de vie de la donnée

### Les 7 phases du cycle de vie logiciel
1. **Analyse des besoins** — comprendre le problème, recueillir les exigences.
2. **Planification** — estimer effort, ressources, risques, jalons.
3. **Conception** — architecture, modèles (UML, MCD).
4. **Développement** — codage.
5. **Test** — unitaires, intégration, recette.
6. **Déploiement** — mise en production.
7. **Maintenance** — corrective, évolutive, adaptative, préventive.

> **Pourquoi un cycle ?** Cadre rigoureux → réduit risques, contrôle coûts/délais, garantit qualité, facilite communication équipe.

### Cycle de vie de la donnée (Cours 7)
1. **Création / Acquisition** (capteurs, formulaires, transactions).
2. **Nettoyage / Transformation** (ETL, normalisation).
3. **Stockage** (BD, entrepôt, lac).
4. **Exploitation / Valorisation** (BI, analytics, ML).
5. **Archivage ou suppression** (rétention légale, RGPD : droit à l'oubli).
6. **Surveillance / Auditabilité** (logs transverses tout au long).

### Concepts transverses à citer dans une dissertation
- **Modularité** : découper en modules indépendants → maintenance facile, réutilisation.
- **Réutilisabilité** : briques pensées pour resservir.
- **Documentation** : essentielle pour pérennité et transmission.

---

# PARTIE II — Compléments (le delta vers l'excellence)

> Ces sections rapportent **les 20 % de points restants** mais peuvent faire la différence entre 80 % et 95 %. À survoler après avoir maîtrisé la Partie I.

---

## 11. Modèles de cycle de vie (au-delà du V)
- **Cascade** : phases séquentielles, peu flexible. Adapté aux projets très cadrés.
- **Modèle en V** : tests prévus dès la conception.
- **Itératif/incrémental** : livraisons partielles.
- **Agile (Scrum, Kanban)** : sprints courts, valeur continue.
- **DevOps / CI-CD** : intégration continue, déploiement automatisé.

---

## 12. Collecte des besoins — méthodes (Cours 7)
| Méthode | Force | Faiblesse |
|---------|-------|-----------|
| **Entrevues individuelles** | Profondeur, contexte | Coûteux en temps |
| **Focus groups** | Confrontation d'idées | Risque d'effet de groupe |
| **Réunions de discussion** | Alignement collectif | Pas toujours documenté |
| **Analyse de l'existant** | Factuel, basé sur réel | Risque de biais de continuité |
| **Questionnaires / sondages** | Grand échantillon | Surface uniquement |
| **Analyse documentaire** | Compréhension du métier | Documents souvent obsolètes |

### Contraintes à considérer
- **Techniques** : technologies imposées, intégrations existantes.
- **Organisationnelles** : politique RH, gouvernance, processus métiers.
- **Juridiques / réglementaires** : RGPD, Loi 25 (Qc), HIPAA, PCI-DSS.

### Outils
- **JIRA + Confluence** : tickets + documentation collaborative.
- **Microsoft OneNote** : notes structurées, partage rapide.
- **Fiches de besoins, canevas de questions, gabarits de prise de notes**.

---

## 13. BI, KPI et types d'analyses (Cours 5)
- **BI (Business Intelligence)** : transformer la donnée en décision.
- **Tableau de bord (Dashboard)** : visualisation centralisée des KPI.
- **KPI (Key Performance Indicator)** : indicateur **mesurable, aligné sur un objectif** (SMART).
- **Visualisation** : choisir le bon graphique selon le message (barres, lignes, secteurs, treemap…).

### Les 4 niveaux d'analyse
| Type | Question | Outil |
|------|----------|-------|
| **Descriptive** | Que s'est-il passé ? | Reporting, dashboards |
| **Diagnostique** | Pourquoi cela s'est-il passé ? | Drill-down, corrélations |
| **Prédictive** | Que va-t-il se passer ? | Modèles ML (régression, classification) |
| **Prescriptive** | Que faut-il faire ? | Optimisation, simulation |

### Machine Learning (rappel)
- **Supervisé** : étiquettes connues (classification, régression).
- **Non-supervisé** : pas d'étiquette (clustering, réduction de dim.).
- **Renforcement** : agent qui apprend par essai-erreur.

---

## 14. Formats de données et stockage (Cours 5, 11)
| Format | Type | Usage |
|--------|------|-------|
| **CSV** | Structuré, tabulaire | Échanges simples, import/export |
| **JSON** | Semi-structuré | API REST, NoSQL documentaire, config |
| **XML** | Semi-structuré, verbeux | Systèmes legacy, B2B (SOAP) |
| **YAML** | Semi-structuré, lisible | Configuration (Kubernetes, Ansible) |
| **Parquet** | Colonnaire binaire | Big Data analytics |
| **Logs** | Texte, séquentiel | Surveillance, audit |
| **Binaire** | Brut | Images, vidéos, exécutables |

### Catégories
- **Structurées** : tables (SQL).
- **Semi-structurées** : JSON, XML (NoSQL documentaire).
- **Non structurées** : texte libre, images, vidéos, audio (Data Lake).

---

## 15. Cloud — IaaS / PaaS / SaaS et les 3 hyperscalers
| Modèle | Définition | Exemple |
|--------|-----------|---------|
| **IaaS** | Infrastructure à la demande | AWS EC2, Azure VM, GCE |
| **PaaS** | Plateforme prête (DB, runtime) | AWS RDS, Azure App Service, Cloud Run |
| **SaaS** | Application clé en main | Microsoft 365, Salesforce, Gmail |

### Forces des 3 hyperscalers
| Acteur | Force |
|--------|-------|
| **AWS** | Leader du marché, catalogue le plus vaste, écosystème mature |
| **Azure** | Intégration Windows/Office, hybride/on-prem |
| **GCP** | Analytique avancée (BigQuery), IA/ML, prix compétitifs, réseau Google |

### Services data à connaître par cœur
- **AWS** : S3 (objet), RDS (relationnel), DynamoDB (NoSQL), Redshift (DW), EMR, Lambda.
- **Azure** : Blob Storage, SQL Database, Cosmos DB, Synapse Analytics, Functions.
- **GCP** : Cloud Storage, Cloud SQL, BigQuery (DW), Dataflow, Vertex AI.

### On-premise vs Off-premise vs Cloud
| Critère | On-prem | Off-prem | Cloud |
|---------|---------|----------|-------|
| Contrôle | Total | Partiel | Limité |
| Coût initial (CAPEX) | Très élevé | Moyen | Très bas |
| Coût opérationnel (OPEX) | Faible mais maintenance | Moyen | Pay-as-you-go |
| Scalabilité | Limitée | Moyenne | Élastique |
| Conformité sensible | Plus simple | Variable | Selon fournisseur/région |

---

## 16. DFD (Data Flow Diagram) en détail
> **DFD ≠ MCD.** MCD = structure des données. DFD = circulation des données.

### Les 4 éléments d'un DFD
1. **Processus** : transforme les données (cercle/rectangle arrondi).
2. **Flux de données** : circulation (flèche).
3. **Stockage de données** : BD/fichier (deux lignes parallèles ouvertes).
4. **Entité externe** : acteur hors système (rectangle).

### Niveaux d'un DFD
- **Niveau 0 (contexte)** : système comme une seule boîte noire avec ses acteurs.
- **Niveau 1, 2, …** : décomposition progressive des processus.

---

## 17. Diagrammes UML d'architecture (Cours 10)
| Diagramme | Rôle |
|-----------|------|
| **Classes** | Entités et leurs relations (statique) |
| **Composants** | Modules logiciels et dépendances |
| **Déploiement** | Installation sur l'infrastructure physique |
| **Séquence** | Échanges de messages dans le temps (dynamique) |
| **DFD** | Circulation des données |

### Diagramme de composants — éléments clés
- **Composant** : module/service indépendant (API, BD, UI).
- **Interface** : point de connexion (lollipop ⊙).
- **Dépendance** : flèche pointillée `<<use>>`.

---

## 18. Mesures de performance & sécurité (Cours 10)
### KPIs de performance
- **Temps de réponse** : < 2 s pour une requête simple (cible courante).
- **Débit (throughput)** : transactions/seconde.
- **Disponibilité (uptime)** : 99,9 % = ~8h45 d'indisponibilité/an ; 99,99 % = ~52 min/an.
- **Latence réseau** : délai aller-retour (ms).

### KPIs de sécurité
- **Authentification** : MFA, SSO, OAuth2.
- **Autorisation** : RBAC (par rôle), ABAC (par attribut).
- **Chiffrement** : HTTPS/TLS (transit), AES-256 (repos).
- **Audit / Logs** : centralisation (ELK, Splunk).
- **RTO** (Recovery Time Objective) : délai max d'indisponibilité acceptable.
- **RPO** (Recovery Point Objective) : perte de données max acceptable (en temps).

---

## 19. Gouvernance des données (Cours 10)
> Ensemble des **règles, processus et responsabilités** pour gérer, utiliser et protéger les données.

### Les 3 instances de validation
| Instance | Rôle | Question type |
|----------|------|---------------|
| **Gouvernance des données** | Règles de gestion (classification, rétention, propriété) | « Les données personnelles sont-elles protégées ? Qui en est propriétaire ? » |
| **Comité d'architecture** | Conformité technologique aux standards de l'organisation | « La solution utilise-t-elle les technos approuvées (PostgreSQL vs autre) ? » |
| **Responsables métiers** | Couverture fonctionnelle, adéquation au besoin | « Les rapports requis peuvent-ils être produits ? » |

### Processus en 6 étapes
1. Préparation du dossier d'architecture (diagrammes, justifications).
2. Présentation à la gouvernance.
3. Présentation au comité d'architecture.
4. Présentation aux responsables métiers.
5. Traitement des écarts.
6. Approbation et déploiement.

---

## 20. Autres styles d'architecture
- **WebSockets** : connexion full-duplex persistante (chat, trading, jeux).
- **GraphQL** : requêtes flexibles côté client, un seul endpoint.
- **gRPC** : RPC binaire performant (microservices internes).
- **Event-driven (Kafka, RabbitMQ)** : découplage asynchrone, streaming.
- **Serverless** : fonctions à la demande (AWS Lambda, Azure Functions).

---

## 21. Sources de données — au-delà des classiques (Cours 11)
- **Bases relationnelles** : intégrité référentielle, transactions ACID.
- **Bases NoSQL** : flexibilité, scalabilité, lectures rapides.
- **Entrepôts / Lacs** : voir §7.
- **APIs** : pont sécurisé entre logiciels (souvent REST/JSON). **Protège la source**, format standardisé.
- **Fichiers plats (CSV, JSON)** : universel, basique, sans schéma fort.
- **Flux (data streams)** : données continues, traitement temps réel (Kafka, Flink, Kinesis).

---

# Annexe — Anti-sèche express (à relire la veille)

### Top 15 réflexes
1. **MCD règles** : 1 Classe→Entité, 2 Attr→Col, 3 Id→PK, 4 Asso→FK ou jonction.
2. **Cardinalités** : 1..1 → FK avec UNIQUE ; 1..N → FK côté N ; N..M → table jonction PK composite.
3. **Composition vs Agrégation** : losange **plein** = vie liée ; losange **vide** = libre.
4. **ACID** : Atomicité / Cohérence / Isolation / Durabilité.
5. **4 familles NoSQL** : Documentaire (MongoDB), Clé-Valeur (Redis), Colonnes (Cassandra), Graphes (Neo4j).
6. **REST** : verbes GET/POST/PUT/DELETE, ressources via URI, **stateless**.
7. **3-tiers** : Présentation / Logique / Données.
8. **DW vs DL** : DW = schéma fixe, structuré, BI ; DL = brut, schema-on-read, ML.
9. **CIA** : Confidentialité (chiffrement, IAM) / Intégrité (hash, logs) / Disponibilité (redondance, PRA).
10. **6 piliers data consumption** : Auth, Chiffrement, Latence, Intégrité, Traçabilité, Résilience.
11. **6 dimensions qualité** : Exactitude, Complétude, Cohérence, Fraîcheur, Unicité, Validité.
12. **7 phases cycle de vie** : Analyse, Planif, Conception, Dév, Test, Déploiement, Maintenance.
13. **ETL** : Extract → Transform → Load (vs ELT cloud-native).
14. **3 instances de gouvernance** : Gouvernance données / Comité d'archi / Responsables métiers.
15. **Moindre privilège** : un user n'a que les droits strictement nécessaires.

### Erreurs à éviter le jour J
- Lire le **sujet en entier** avant d'écrire — repérer les questions à fort barème.
- **Justifier chaque cardinalité** par une phrase de l'énoncé.
- Ne pas confondre **MCD / MLD / MPD** : conceptuel / logique (relationnel) / physique (SGBD).
- Pour SQL vs NoSQL : **toujours conclure par un choix justifié**, jamais « ça dépend ».
- Soigner le **français** (5 % du barème) : ponctuation, accords, vocabulaire technique exact.

---

# Sources

Documents internes :
- `cours_conception_basededonnee.md` — Compilation des 7 cours du cursus 420-C47-BB (Nadir Bouakel, Collège de Bois-de-Boulogne).

Sources web externes (vérifiées en mai 2026) :
- [Modèle Conceptuel de Données (MCD) Merise — Memento-dev](https://memento-dev.fr/docs/merise/mcd)
- [Règles de passage du MCD au MLD — Univ. Constantine](https://www.univ-constantine2.dz/CoursOnLine/Benelhadj-Mohamed/co/grain7_2.html)
- [SQLPro — Cours MERISE complet](https://sqlpro.developpez.com/cours/modelisation/merise/?page=passage)
- [Propriétés ACID — Wikipédia](https://fr.wikipedia.org/wiki/Propri%C3%A9t%C3%A9s_ACID)
- [Explication des propriétés ACID — MongoDB](https://www.mongodb.com/fr-fr/resources/basics/databases/acid-transactions)
- [SQL vs NoSQL — Data-Bird](https://www.data-bird.co/blog/sql-vs-nosql)
- [Bases NoSQL : familles — MongoDB](https://www.mongodb.com/fr-fr/resources/basics/databases/nosql-explained/nosql-vs-sql)
- [UML — Diagramme de classes — Developpez.com (L. Audibert)](https://laurent-audibert.developpez.com/Cours-UML/?page=diagramme-classes)
- [Association vs Agrégation vs Composition — EdrawMax](https://www.edrawsoft.com/fr/article/uml-aggregation-vs-composition.html)
- [Microservices vs 3-Tier vs Monolithic — Medium](https://saedhasan.medium.com/microservices-vs-3-tier-vs-monolithic-9073c80df468)
- [Monolithic vs Microservices — AWS](https://aws.amazon.com/compare/the-difference-between-monolithic-and-microservices-architecture/)
- [Data Lake vs Data Warehouse — Qlik](https://www.qlik.com/us/data-lake/data-lake-vs-data-warehouse)
- [Data Warehouse vs Data Lake vs Lakehouse — IBM](https://www.ibm.com/think/topics/data-warehouse-vs-data-lake-vs-data-lakehouse)
- [REST API Design Guide — Strapi](https://strapi.io/blog/restful-api-design-guide-principles-best-practices)
- [Web API Design Best Practices — Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design)
- [REST — Wikipedia](https://en.wikipedia.org/wiki/REST)
