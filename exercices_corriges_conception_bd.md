# Exercices corrigés — Préparation examen final
## Cours 420-C47-BB : Analyse et conception d'une solution de données

> 15 exercices structurés par bloc thématique, dans l'ordre croissant de difficulté.
> Chaque exercice : **Énoncé** → **Démarche** → **Solution complète** → **Astuce / Piège**.
>
> Recommandation : faites chaque exercice **d'abord seul** (cachez la solution avec une feuille), puis comparez. Objectif : 30 à 40 min par exercice MCD, 15 à 25 min par exercice théorique.

---

## Sommaire

**Bloc A — MCD & cardinalités**
1. [Bibliothèque (emprunts de livres)](#exercice-1--bibliothèque-emprunts-de-livres)
2. [Clinique (dossiers médicaux)](#exercice-2--clinique-dossiers-médicaux)
3. [École (étudiants, cours, enseignants)](#exercice-3--école-étudiants-cours-enseignants)
4. [E-commerce (commandes & produits)](#exercice-4--e-commerce-commandes--produits)
5. [Identifier les cardinalités à partir d'un texte](#exercice-5--identifier-les-cardinalités-à-partir-dun-texte)

**Bloc B — Du MCD au SQL**
6. [Transformation MCD → schéma relationnel + DDL SQL](#exercice-6--transformation-mcd--schéma-relationnel--ddl-sql)

**Bloc C — Architecture & stockage**
7. [SportDirect : architecture analytique + mobile](#exercice-7--sportdirect-architecture-analytique--mobile)
8. [SQL vs NoSQL — 3 mini-cas](#exercice-8--sql-vs-nosql--3-mini-cas)
9. [Choisir la bonne famille NoSQL](#exercice-9--choisir-la-bonne-famille-nosql)
10. [Architecture analytique : DW vs DL vs Hub](#exercice-10--architecture-analytique--dw-vs-dl-vs-hub)

**Bloc D — ACID, REST, UML**
11. [ACID : analyser des scénarios](#exercice-11--acid--analyser-des-scénarios)
12. [Concevoir une API REST pour un blog](#exercice-12--concevoir-une-api-rest-pour-un-blog)
13. [Choisir le bon diagramme UML](#exercice-13--choisir-le-bon-diagramme-uml)

**Bloc E — Qualité, sécurité, gouvernance**
14. [Audit qualité de données — les 6 dimensions](#exercice-14--audit-qualité-de-données--les-6-dimensions)
15. [CIA + 6 piliers : étude de cas API publique](#exercice-15--cia--6-piliers--étude-de-cas-api-publique)

---

# Bloc A — MCD & cardinalités

## Exercice 1 — Bibliothèque (emprunts de livres)

### Énoncé
> Une bibliothèque souhaite gérer ses emprunts. Un **Membre** (identifié par un `id_membre`, un `nom` et un `email`) possède une et une seule **Carte d'Abonnement** (`numero_carte`, `date_emission`). Une carte appartient à un seul membre. Un membre peut emprunter plusieurs **Livres** (`isbn`, `titre`, `annee`), ou n'en emprunter aucun s'il vient juste de s'inscrire. Un livre physique précis est emprunté par au maximum un membre à la fois (ou zéro s'il est en rayon). Enfin, un livre est écrit par au moins un **Auteur** (`id_auteur`, `nom`, `nationalite`), et un auteur a pu écrire plusieurs livres.

### Démarche
1. **Repérer les noms communs persistants** : Membre, Carte, Livre, Auteur → 4 entités.
2. **Identifier les attributs et l'identifiant** de chacune.
3. **Pour chaque verbe d'action ou relation**, formuler la cardinalité dans les deux sens.
4. **Vérifier l'obligation** ("au moins", "doit", "obligatoirement") vs **optionnalité** ("peut", "ou aucun").

### Solution

#### Entités et attributs
| Entité | Identifiant (PK) | Attributs |
|--------|------------------|-----------|
| `MEMBRE` | `id_membre` | `nom`, `email` |
| `CARTE` | `numero_carte` | `date_emission` |
| `LIVRE` | `isbn` | `titre`, `annee` |
| `AUTEUR` | `id_auteur` | `nom`, `nationalite` |

#### Associations et cardinalités
| Association | Sens 1 (UML) | Sens 2 (UML) | Type de relation |
|-------------|--------------|--------------|------------------|
| `MEMBRE — possède — CARTE` | Membre `1..1` Carte | Carte `1..1` Membre | **1..1** ↔ **1..1** (bijection) |
| `MEMBRE — emprunte — LIVRE` | Membre `0..*` Livre | Livre `0..1` Membre | **1..N** (côté Membre) |
| `LIVRE — écrit par — AUTEUR` | Livre `1..*` Auteur | Auteur `0..*` Livre | **N..M** |

#### Schéma relationnel (application des règles)
```text
MEMBRE   (id_membre PK, nom, email)
CARTE    (numero_carte PK, date_emission, id_membre FK UNIQUE NOT NULL → MEMBRE)
LIVRE    (isbn PK, titre, annee, id_membre FK NULL → MEMBRE)   -- NULL si livre en rayon
AUTEUR   (id_auteur PK, nom, nationalite)
ECRIRE   (isbn FK → LIVRE, id_auteur FK → AUTEUR, PK(isbn, id_auteur))
```

#### Justifications
- **MEMBRE / CARTE (1..1 ↔ 1..1)** : on aurait pu **fusionner**, mais on les sépare pour garder une sémantique claire (l'abonnement a son propre cycle de vie : émission, renouvellement). On choisit de mettre la FK dans `CARTE` (avec `UNIQUE`) car la carte « dépend » plus du membre que l'inverse.
- **MEMBRE / LIVRE (1..N)** : un membre emprunte plusieurs livres, mais un livre n'est emprunté que par **au plus un** membre à la fois → la FK `id_membre` va dans `LIVRE`, et est `NULL` quand le livre est disponible.
- **LIVRE / AUTEUR (N..M)** : un livre a plusieurs auteurs, un auteur écrit plusieurs livres → **table de jonction** `ECRIRE` avec PK composite.

### Astuce / Piège
> ⚠️ La phrase « **au moins un** auteur » impose la cardinalité minimale `1` côté Auteur. Si l'énoncé disait « peut être anonyme », ce serait `0..*`. Lire chaque mot.

---

## Exercice 2 — Clinique (dossiers médicaux)

### Énoncé
> La clinique souhaite informatiser le suivi de ses **Patients**. Pour chaque personne soignée, on doit impérativement enregistrer son numéro d'assurance sociale, son nom complet ainsi que sa date de naissance. À chaque patient est rattaché un unique **Dossier Médical** (`groupe_sanguin`, liste des `allergies`). Un dossier ne peut appartenir qu'à un seul patient et chaque patient possède obligatoirement le sien. Les patients peuvent planifier plusieurs **Rendez-vous**. Pour une consultation donnée, on note la date et l'heure ainsi que le motif. Un rendez-vous ne concerne qu'un seul patient. Chaque consultation est placée sous la responsabilité d'un seul **Médecin** (`numero_licence`, `nom`, `specialite`). Un médecin assure de nombreux rendez-vous. Enfin, on doit pouvoir désigner un médecin **référent** pour un patient : un patient peut n'avoir aucun médecin référent ou en choisir un seul ; un médecin peut être référent de plusieurs patients.

### Solution

#### Entités
| Entité | PK | Attributs |
|--------|----|-----------|
| `PATIENT` | `nas` (numéro d'assurance sociale) | `nom_complet`, `date_naissance` |
| `DOSSIER` | `id_dossier` | `groupe_sanguin`, `allergies` |
| `RENDEZ_VOUS` | `id_rdv` | `date_heure`, `motif` |
| `MEDECIN` | `numero_licence` | `nom`, `specialite` |

#### Associations
| Relation | Cardinalités | Stratégie |
|----------|--------------|-----------|
| `PATIENT — possède — DOSSIER` | `1..1 ↔ 1..1` (obligatoire des 2 côtés) | FK + UNIQUE dans `DOSSIER` (ou fusion possible) |
| `PATIENT — planifie — RENDEZ_VOUS` | `1..1 ↔ 0..*` | FK `nas` dans `RENDEZ_VOUS` |
| `MEDECIN — assure — RENDEZ_VOUS` | `1..1 ↔ 0..*` | FK `numero_licence` dans `RENDEZ_VOUS` |
| `MEDECIN — est référent — PATIENT` | `0..* ↔ 0..1` | FK `numero_licence_referent` (nullable) dans `PATIENT` |

#### Schéma relationnel
```text
PATIENT      (nas PK, nom_complet, date_naissance,
              numero_licence_referent FK NULL → MEDECIN)
DOSSIER      (id_dossier PK, groupe_sanguin, allergies,
              nas FK UNIQUE NOT NULL → PATIENT)
MEDECIN      (numero_licence PK, nom, specialite)
RENDEZ_VOUS  (id_rdv PK, date_heure, motif,
              nas FK NOT NULL → PATIENT,
              numero_licence FK NOT NULL → MEDECIN)
```

### Astuce / Piège
> ⚠️ Deux relations différentes entre `MEDECIN` et `PATIENT` :
> 1. via `RENDEZ_VOUS` (relation triangulaire — un médecin **assure** un RDV qui concerne un patient).
> 2. **directe** (un médecin **référent**).
>
> Ne pas les confondre : ce sont **deux liens sémantiques distincts**. La relation « référent » est directe et nullable.

---

## Exercice 3 — École (étudiants, cours, enseignants)

### Énoncé
> Une école veut gérer ses cours. Un **Étudiant** (`matricule`, `nom`, `programme`) s'inscrit à plusieurs **Cours** (`code_cours`, `intitulé`, `crédits`), et un cours accueille plusieurs étudiants — au minimum 5 pour être ouvert, au maximum 35. À chaque inscription, on doit conserver la **note finale** (entre 0 et 100, peut être null avant l'évaluation). Chaque cours est donné par exactement un **Enseignant** (`id_enseignant`, `nom`, `département`), mais un enseignant peut donner plusieurs cours (ou aucun, s'il est en sabbatique).

### Solution

#### Entités & associations
| Entité | PK | Attributs |
|--------|----|-----------|
| `ETUDIANT` | `matricule` | `nom`, `programme` |
| `COURS` | `code_cours` | `intitule`, `credits` |
| `ENSEIGNANT` | `id_enseignant` | `nom`, `departement` |

| Relation | Cardinalités | Stratégie |
|----------|--------------|-----------|
| `ETUDIANT — inscrit_à — COURS` | `0..* ↔ 5..35` | **Table de jonction** `INSCRIPTION` (relation N..M **avec attribut propre** : la note) |
| `ENSEIGNANT — donne — COURS` | `0..* ↔ 1..1` | FK `id_enseignant` dans `COURS` |

#### Schéma relationnel
```text
ETUDIANT     (matricule PK, nom, programme)
ENSEIGNANT   (id_enseignant PK, nom, departement)
COURS        (code_cours PK, intitule, credits,
              id_enseignant FK NOT NULL → ENSEIGNANT)
INSCRIPTION  (matricule FK → ETUDIANT,
              code_cours FK → COURS,
              note_finale DECIMAL(5,2) NULL CHECK (note_finale BETWEEN 0 AND 100),
              PK(matricule, code_cours))
```

### Astuce / Piège
> ⚠️ Quand une relation N..M porte une **information propre** (ici la `note_finale`), elle **doit** devenir une table à part entière. Sinon, on perdrait l'attribut.
>
> ⚠️ Les bornes `5..35` côté Cours ne se traduisent pas en SQL standard (pas de cardinalité min directe). On les implémente côté **application** ou via un **trigger** / **contrainte CHECK** sur une vue agrégée.

---

## Exercice 4 — E-commerce (commandes & produits)

### Énoncé
> Un site marchand gère ses ventes. Un **Client** (`id_client`, `email`, `nom`, `adresse`) peut passer plusieurs **Commandes** (`num_commande`, `date_commande`, `statut`). Chaque commande appartient à un seul client. Une commande contient au moins un **Produit** (`sku`, `libelle`, `prix_unitaire`, `stock`), et chaque produit peut figurer dans plusieurs commandes. Pour chaque produit dans une commande, on doit connaître la **quantité commandée** et le **prix unitaire au moment de la commande** (qui peut différer du prix actuel). Une commande génère exactement une **Facture** (`num_facture`, `montant_total`, `date_emission`) ; une facture correspond à une seule commande.

### Solution

#### Schéma relationnel
```text
CLIENT       (id_client PK, email UNIQUE, nom, adresse)
COMMANDE     (num_commande PK, date_commande, statut,
              id_client FK NOT NULL → CLIENT)
PRODUIT      (sku PK, libelle, prix_unitaire, stock)
LIGNE_CMD    (num_commande FK → COMMANDE,
              sku FK → PRODUIT,
              quantite INT NOT NULL,
              prix_au_moment DECIMAL(10,2) NOT NULL,
              PK(num_commande, sku))
FACTURE      (num_facture PK, montant_total, date_emission,
              num_commande FK UNIQUE NOT NULL → COMMANDE)
```

#### Justifications
- **CLIENT 1..N COMMANDE** : FK simple côté Commande.
- **COMMANDE N..M PRODUIT avec attributs** : table `LIGNE_CMD` avec PK composite + `quantite` + `prix_au_moment` (snapshot pour éviter qu'un changement de tarif réécrive l'historique).
- **COMMANDE 1..1 FACTURE** : FK `num_commande` dans `FACTURE` avec `UNIQUE`.

### Astuce / Piège
> ⚠️ Le **prix au moment** est un grand classique. Si l'on stockait seulement la quantité et qu'on multipliait par `PRODUIT.prix_unitaire`, le total des anciennes factures changerait à chaque mise à jour de prix. **Solution** : figer le prix dans la ligne de commande.

---

## Exercice 5 — Identifier les cardinalités à partir d'un texte

### Énoncé
Pour chaque phrase, donner la cardinalité **complète** (`min..max` des deux côtés) :

1. *« Un employé est rattaché à exactement un département. Un département compte au moins 3 employés. »*
2. *« Un projet peut impliquer plusieurs employés. Un employé peut travailler sur plusieurs projets, ou être en pause. »*
3. *« Un véhicule appartient à un propriétaire ou à un concessionnaire (jamais aux deux). »* — comment modéliser ?
4. *« Une commande peut être livrée en plusieurs colis, mais chaque colis correspond à une seule commande. »*
5. *« Un utilisateur peut suivre d'autres utilisateurs (sans limite), et être suivi par d'autres. »*

### Solution

| # | Cardinalité | Justification |
|---|-------------|---------------|
| 1 | `EMPLOYE 1..1 ↔ 3..* DEPARTEMENT` | « exactement un » côté Employé ; « au moins 3 » côté Département |
| 2 | `PROJET 0..* ↔ 0..* EMPLOYE` | N..M optionnelle des deux côtés → table de jonction |
| 3 | **Héritage/spécialisation** ou attribut typé : créer `VEHICULE` avec FK optionnelle `id_proprio` OU `id_concessionnaire`, avec contrainte `CHECK` que **exactement une** des deux est non-NULL (relation exclusive XOR) |
| 4 | `COMMANDE 1..1 ↔ 1..* COLIS` | « plusieurs colis » ≥ 1 ; « une seule commande » côté Colis |
| 5 | **Auto-association N..M** : `UTILISATEUR ↔ UTILISATEUR` → table `SUIVI(suiveur_id FK, suivi_id FK, PK composite)` |

### Astuce / Piège
> ⚠️ Une **auto-association** (#5) est très fréquente (réseaux sociaux, hiérarchie d'employés). Le piège : oublier que la table de jonction référence **deux fois** la même table avec des rôles différents (`suiveur` / `suivi`).
>
> ⚠️ Une **relation exclusive** (#3) ne s'exprime pas naturellement en relationnel : on combine FK nullable + `CHECK` métier.

---

# Bloc B — Du MCD au SQL

## Exercice 6 — Transformation MCD → schéma relationnel + DDL SQL

### Énoncé
Reprendre le MCD de la **bibliothèque** (exercice 1) et :
1. Donner le schéma relationnel complet.
2. Rédiger le **DDL SQL standard (PostgreSQL)** : `CREATE TABLE` avec PK, FK, contraintes `NOT NULL` et `UNIQUE`.
3. Ajouter 3 contraintes métier supplémentaires : `email` au format valide, `annee` ≤ année courante, et `date_emission` ≤ aujourd'hui.

### Solution

```sql
-- 1. Table MEMBRE
CREATE TABLE membre (
    id_membre   SERIAL PRIMARY KEY,
    nom         VARCHAR(100) NOT NULL,
    email       VARCHAR(255) NOT NULL UNIQUE
                CHECK (email ~* '^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$')
);

-- 2. Table AUTEUR
CREATE TABLE auteur (
    id_auteur    SERIAL PRIMARY KEY,
    nom          VARCHAR(100) NOT NULL,
    nationalite  VARCHAR(60)
);

-- 3. Table LIVRE (FK optionnelle vers Membre = emprunteur courant)
CREATE TABLE livre (
    isbn        VARCHAR(17) PRIMARY KEY,
    titre       VARCHAR(255) NOT NULL,
    annee       SMALLINT NOT NULL CHECK (annee <= EXTRACT(YEAR FROM CURRENT_DATE)),
    id_membre   INTEGER NULL
                REFERENCES membre(id_membre) ON DELETE SET NULL
);

-- 4. Table CARTE (1..1 strict avec Membre)
CREATE TABLE carte (
    numero_carte   VARCHAR(20) PRIMARY KEY,
    date_emission  DATE NOT NULL CHECK (date_emission <= CURRENT_DATE),
    id_membre      INTEGER NOT NULL UNIQUE
                   REFERENCES membre(id_membre) ON DELETE CASCADE
);

-- 5. Table de jonction ECRIRE (N..M Livre/Auteur)
CREATE TABLE ecrire (
    isbn        VARCHAR(17) NOT NULL
                REFERENCES livre(isbn) ON DELETE CASCADE,
    id_auteur   INTEGER NOT NULL
                REFERENCES auteur(id_auteur) ON DELETE RESTRICT,
    PRIMARY KEY (isbn, id_auteur)
);

-- Index utiles
CREATE INDEX idx_livre_membre ON livre(id_membre);
CREATE INDEX idx_ecrire_auteur ON ecrire(id_auteur);
```

#### Notes pédagogiques
- **`ON DELETE CASCADE`** sur `carte.id_membre` : si le membre disparaît, sa carte aussi (logique 1..1).
- **`ON DELETE SET NULL`** sur `livre.id_membre` : le livre survit à la suppression d'un membre.
- **`ON DELETE RESTRICT`** sur `ecrire.id_auteur` : on empêche la suppression d'un auteur tant qu'il a des livres.
- Le `CHECK` regex pour l'email valide est PostgreSQL-spécifique (`~*` = match insensible à la casse).

### Astuce / Piège
> ⚠️ Le choix des **actions ON DELETE / ON UPDATE** fait partie du barème. Il faut justifier chaque choix par la sémantique métier, pas mettre `CASCADE` partout par défaut.

---

# Bloc C — Architecture & stockage

## Exercice 7 — SportDirect : architecture analytique + mobile

### Énoncé (extrait Cours 10)
> Le magasin SportDirect possède une base de données pour ses ventes. Le directeur souhaite :
> 1. Un outil pour analyser les tendances de l'année et générer des rapports (**Dashboard**). Les données de la base doivent être nettoyées et organisées dans un nouveau système spécialisé pour l'aide à la décision. Il faut un mécanisme pour les extraire et les convertir au bon format chaque soir.
> 2. Une **application mobile** pour les clients. Pour des raisons de sécurité, l'application ne doit **jamais** toucher à la base de données. Elle doit passer par un intermédiaire qui contient la logique de calcul et communique via les standards du web (HTTP).

### Solution — Schéma textuel
```text
┌────────────┐
│ App mobile │ ── HTTPS ──► ┌─────────────┐         ┌──────────────┐
│ (clients)  │              │  API REST   │ ──SQL──►│ BD ventes    │
└────────────┘              │ (3-tiers,   │         │ (OLTP, ex.   │
                            │  logique    │         │  PostgreSQL) │
                            │  métier)    │         └──────┬───────┘
                            └─────────────┘                │
                                                           │ ETL nocturne
                                                           ▼
                            ┌──────────────┐     ┌──────────────────┐
                            │ Dashboard BI │◄────│ Data Warehouse   │
                            │ (Power BI,   │ SQL │ (OLAP, ex. Redshift,│
                            │  Tableau)    │     │  BigQuery,       │
                            └──────────────┘     │  Snowflake)      │
                                                 └──────────────────┘
```

#### Justification des choix
| Besoin | Solution | Pourquoi ? |
|--------|----------|------------|
| 1. Analyse de tendances + rapports | **Data Warehouse** alimenté par un **ETL nocturne** | OLTP = transactions rapides ; OLAP = requêtes analytiques. On sépare pour ne pas pénaliser la BD opérationnelle. |
| 2. App mobile sans accès direct à la BD | **API REST** (3-tiers) entre l'app et la BD | Sécurité (BD non exposée), logique métier centralisée, format standard JSON, contrôle d'accès (auth JWT/OAuth2). |

#### Composants à mentionner
- **ETL** (Extract-Transform-Load) : outils tels que Talend, Airbyte, Apache NiFi, AWS Glue, dbt.
- **API** : framework FastAPI / Express / Spring Boot.
- **Sécurité** : HTTPS, OAuth2, rate-limiting, validation d'entrée.
- **Monitoring** : logs d'API, alertes sur erreurs HTTP 5xx.

### Astuce / Piège
> ⚠️ Le mot-clé « **chaque soir** » impose un traitement **batch** (ETL programmé). Si l'énoncé avait dit « en temps réel », on parlerait de **CDC** (Change Data Capture) ou de **streaming** (Kafka, Debezium).
>
> ⚠️ « **L'app ne doit jamais toucher à la BD** » → c'est exactement la justification du pattern **3-tiers** et de l'**API**.

---

## Exercice 8 — SQL vs NoSQL — 3 mini-cas

### Énoncé
Pour chaque situation, indiquer **SQL ou NoSQL** et **justifier** en 2-3 lignes :

**Cas A** — Un système bancaire qui gère des virements entre comptes, avec obligation de conformité réglementaire et reporting financier mensuel.

**Cas B** — Une plateforme IoT collectant 50 000 mesures de température par seconde provenant de capteurs distribués.

**Cas C** — Un site de gestion de contenu (CMS) où chaque article peut avoir un nombre arbitraire de champs (tags, images, vidéos, polls intégrés…) et où le schéma évolue à chaque sprint.

### Solution

| Cas | Choix | Justification |
|-----|-------|---------------|
| **A — Banque** | **SQL** (PostgreSQL, Oracle, SQL Server) | Transactions **ACID** indispensables (atomicité du virement), cohérence stricte, contraintes d'intégrité, reporting via SQL puissant, conformité auditée (logs, schéma figé). |
| **B — IoT** | **NoSQL Colonnes** (Cassandra) ou **série temporelle** (InfluxDB, TimescaleDB) | Volume d'écritures massif et distribué, scalabilité horizontale native, schéma simple répété, on lit souvent par plage temporelle ou par capteur. Cassandra est conçu pour ne **jamais tomber** (Netflix, Twitter). |
| **C — CMS** | **NoSQL Documentaire** (MongoDB) | Schéma flexible (chaque article = document JSON différent), évolution rapide sans migration, modèle proche du code applicatif, lectures rapides. |

### Astuce / Piège
> ⚠️ Ne jamais répondre « SQL parce que c'est sûr » ou « NoSQL parce que c'est moderne ». **Toujours s'appuyer sur les critères du cours** : structure, volume, relations, cohérence requise.
>
> ⚠️ Pour la banque, ne pas céder à la tentation « blockchain ». Le sujet demande une base, pas une révolution.

---

## Exercice 9 — Choisir la bonne famille NoSQL

### Énoncé
Associer chaque besoin à la **famille NoSQL** la plus appropriée et nommer un **produit représentatif** :

1. Cache de sessions utilisateurs ultra-rapide pour un site à fort trafic.
2. Moteur de recommandation Netflix (« les utilisateurs qui ont aimé X ont aussi aimé Y »).
3. Catalogue produits avec attributs très variables (mode, électronique, alimentaire dans une même base).
4. Détection de fraude bancaire en temps réel basée sur le réseau de relations entre comptes.
5. Stockage de logs applicatifs distribués (10 To/jour).
6. Tableau de classement (leaderboard) d'un jeu mobile mis à jour 100 000 fois par seconde.

### Solution

| # | Besoin | Famille | Produit | Pourquoi |
|---|--------|---------|---------|----------|
| 1 | Cache sessions | **Clé-Valeur** | **Redis** | Ultra-rapide (RAM), accès O(1) par clé de session |
| 2 | Recommandation Netflix | **Graphes** | **Neo4j** | Relations « utilisateur → film → utilisateur » natives, traversées multi-niveaux |
| 3 | Catalogue produits variables | **Documentaire** | **MongoDB** | Schéma flexible, chaque produit = document JSON avec ses propres attributs |
| 4 | Fraude bancaire temps réel | **Graphes** | **Neo4j** | Détection de motifs (cycles, hubs anormaux) dans un réseau de comptes |
| 5 | Logs distribués 10 To/jour | **Colonnes** | **Cassandra** ou **HBase** | Écritures massives, scalabilité horizontale, lecture sélective par colonne |
| 6 | Leaderboard temps réel | **Clé-Valeur** | **Redis** (sorted sets) | Structure native `ZSET` ultra-performante pour les classements |

### Astuce / Piège
> ⚠️ Pour les **recommandations**, on hésite souvent entre Documentaire et Graphes. Règle : dès qu'on parle de **« amis d'amis »**, **« chemin entre… »**, **« réseau »**, c'est **Graphes**.
>
> ⚠️ Redis n'est pas qu'un cache : ses structures spécialisées (`ZSET`, `LIST`, `HASH`, `STREAM`) en font un couteau-suisse pour de nombreux cas temps réel.

---

## Exercice 10 — Architecture analytique : DW vs DL vs Hub

### Énoncé
Une grande chaîne de supermarchés veut moderniser son architecture data. Elle a :
- 200 caisses (transactions ventes structurées).
- Un programme de fidélité (profils clients).
- Des caméras en magasin (vidéo brute pour analyse de flux clients).
- Des capteurs température dans les rayons frais (séries temporelles).
- Des avis clients laissés en texte libre (commentaires, photos).

Elle veut faire du **reporting financier mensuel** ET de la **data science** (détection de comportements clients, vision par ordinateur).

**Question** : proposer une architecture data complète. Pour chaque source, indiquer dans **quel système** elle atterrit (Data Warehouse, Data Lake, Data Hub) et **pourquoi**.

### Solution

#### Architecture proposée
```text
                     ┌──────────────────────────────┐
                     │      DATA HUB / INTÉGRATION  │
                     │  (Kafka / Confluent / NiFi)  │
                     └──────────────┬───────────────┘
                                    │
       ┌────────────────────────────┼────────────────────────────┐
       │                            │                            │
       ▼                            ▼                            ▼
┌──────────────┐           ┌──────────────────┐         ┌─────────────────┐
│ DATA WAREHOUSE│           │   DATA LAKE      │         │ BD OPÉRATIONNELLES│
│ (Snowflake,   │           │  (S3, ADLS,      │         │ (PostgreSQL caisses,│
│  Redshift,    │           │  GCS)            │         │  Cosmos DB fidélité)│
│  BigQuery)    │           │                  │         └─────────────────┘
└──────┬───────┘           └──────┬───────────┘
       │                          │
       ▼                          ▼
   Power BI                ML / Computer Vision
   (reporting              (Databricks, Vertex AI)
    financier)
```

#### Allocation par source
| Source | Système cible | Justification |
|--------|---------------|---------------|
| Transactions caisses | **Data Warehouse** (ETL nocturne) | Structurées, schéma stable, reporting financier nécessite OLAP optimisé |
| Profils fidélité | **Data Warehouse** + référentiel maître (MDM) | Données structurées, intégrées aux ventes pour analyses 360° |
| Vidéo brute caméras | **Data Lake** (objet) | Volume massif, non structuré, schema-on-read, traitement ML ultérieur |
| Capteurs température (séries temporelles) | **Data Lake** ou **BD séries temporelles** (TimescaleDB) | Volume continu, accès par plage temporelle, peu de jointures |
| Avis clients (texte + photos) | **Data Lake** | Semi/non structuré, NLP et vision appliqués à la demande |

#### Rôle du Data Hub
Le **hub** (Kafka, NiFi) joue le rôle de **point d'échange central** : il route les flux vers DW (après transformation) ou DL (en brut), sans stocker durablement.

#### Notes
- Architecture moderne : **Lakehouse** (Delta Lake / Iceberg) qui combine flexibilité du DL et performance du DW.
- Gouvernance : catalogue (DataHub OSS, Unity Catalog, Glue Data Catalog) pour documenter toutes les sources.

### Astuce / Piège
> ⚠️ **Vidéo et photos n'ont rien à faire dans un Data Warehouse**. Le DW est conçu pour des colonnes typées, pas pour stocker des fichiers volumineux. Toujours envoyer les non-structurées dans le Data Lake.

---

# Bloc D — ACID, REST, UML

## Exercice 11 — ACID : analyser des scénarios

### Énoncé
Pour chaque scénario, identifier **quelle(s) propriété(s) ACID** est/sont en jeu et expliquer ce qui se passerait sans cette garantie.

**Scénario 1** — Lors d'une réservation d'avion à deux passagers, le système enregistre le passager 1 puis crashe avant d'enregistrer le passager 2.

**Scénario 2** — Deux caissiers vendent simultanément le dernier exemplaire d'un produit en stock 1.

**Scénario 3** — Un transfert bancaire validé est confirmé au client. Le serveur tombe juste après. Au redémarrage, le transfert a-t-il bien eu lieu ?

**Scénario 4** — Un script tente d'insérer une commande avec un `id_client` qui n'existe pas dans la table `CLIENT`.

### Solution

| # | Propriété en jeu | Sans cette garantie |
|---|------------------|---------------------|
| 1 | **Atomicité** | Le passager 1 serait enregistré seul. La réservation serait partielle, incohérente. Avec atomicité, le `ROLLBACK` annule l'enregistrement du passager 1 au crash. |
| 2 | **Isolation** | Les deux caissiers liraient « stock = 1 » et vendraient chacun le produit → **survente** (stock = -1). Avec isolation (verrou ou MVCC), un seul réussit, l'autre reçoit un échec ou attend. |
| 3 | **Durabilité** | Si la transaction est confirmée (commit) avant le crash, elle **survit** au crash. Au redémarrage, elle est restaurée depuis le journal de transactions (WAL). Sans durabilité, on aurait débité le compte du client sans crédit côté destinataire. |
| 4 | **Cohérence** | La contrainte de clé étrangère bloque l'insertion → la base reste dans un état cohérent (pas de commande orpheline). |

### Astuce / Piège
> ⚠️ Beaucoup d'étudiants confondent **isolation** et **atomicité**. Mémo :
> - **Atomicité** : protège *une seule* transaction contre les erreurs internes (tout ou rien).
> - **Isolation** : protège *plusieurs* transactions concurrentes contre les interférences mutuelles.

---

## Exercice 12 — Concevoir une API REST pour un blog

### Énoncé
Vous devez concevoir une **API REST** pour gérer un blog. Les ressources : `Articles`, `Commentaires` (chaque commentaire est attaché à un article), `Auteurs`.

Pour chacune des opérations suivantes, donnez :
1. La **méthode HTTP**.
2. L'**URI** suivant les bonnes pratiques REST.
3. Le **code HTTP de succès** attendu.
4. Le **payload** (si applicable).

Opérations :
- (a) Lister tous les articles.
- (b) Récupérer l'article #42.
- (c) Créer un nouvel article.
- (d) Modifier complètement l'article #42.
- (e) Modifier uniquement le titre de l'article #42.
- (f) Supprimer l'article #42.
- (g) Lister les commentaires de l'article #42.
- (h) Ajouter un commentaire à l'article #42.

### Solution

| # | Méthode | URI | Succès | Payload |
|---|---------|-----|--------|---------|
| a | `GET` | `/articles` | `200 OK` | — (peut accepter `?page=2&limit=20&author=…`) |
| b | `GET` | `/articles/42` | `200 OK` | — |
| c | `POST` | `/articles` | `201 Created` + `Location: /articles/123` | `{ "titre": "…", "contenu": "…", "id_auteur": 7 }` |
| d | `PUT` | `/articles/42` | `200 OK` (ou `204 No Content`) | `{ "titre": "…", "contenu": "…", "id_auteur": 7 }` (objet complet) |
| e | `PATCH` | `/articles/42` | `200 OK` | `{ "titre": "Nouveau titre" }` (champs modifiés uniquement) |
| f | `DELETE` | `/articles/42` | `204 No Content` | — |
| g | `GET` | `/articles/42/commentaires` | `200 OK` | — |
| h | `POST` | `/articles/42/commentaires` | `201 Created` | `{ "auteur": "Alice", "texte": "…" }` |

### Erreurs courantes à éviter (les **anti-patterns** REST)
| ❌ Mauvais | ✅ Bon | Pourquoi |
|-----------|-------|----------|
| `POST /createArticle` | `POST /articles` | Pas de verbe dans l'URI |
| `GET /article/42` | `GET /articles/42` | Pluriel pour les collections |
| `POST /articles/42/delete` | `DELETE /articles/42` | Utiliser le verbe HTTP approprié |
| `GET /getArticleById?id=42` | `GET /articles/42` | URI hiérarchique, pas de query string pour un id |
| `200 OK` après suppression sans corps | `204 No Content` | Code plus précis |

### Astuce / Piège
> ⚠️ **PUT vs PATCH** :
> - `PUT` = **remplacement complet** de la ressource (idempotent).
> - `PATCH` = **mise à jour partielle**.
>
> ⚠️ **Stateless** : ne jamais stocker la session sur le serveur. Toujours envoyer un **token** (JWT, Bearer) dans l'en-tête `Authorization`.

---

## Exercice 13 — Choisir le bon diagramme UML

### Énoncé
Pour chaque besoin de modélisation, indiquer **quel diagramme UML** convient le mieux :

1. Décrire le **scénario** d'un retrait au distributeur (de l'insertion de la carte à la remise des billets), avec les échanges entre l'utilisateur, le distributeur et le serveur bancaire.
2. Représenter les **modules logiciels** d'une application web (frontend React, API Node.js, base PostgreSQL, cache Redis) et leurs dépendances.
3. Documenter la **structure** d'un domaine métier (Client, Commande, Produit, Facture) et les **multiplicités** entre eux.
4. Montrer comment l'application est **installée** sur l'infrastructure (serveur web sur EC2, base sur RDS, fichiers sur S3, accessibles via un Load Balancer).
5. Représenter la **circulation des données** dans un système de paye : depuis le pointage des heures jusqu'à l'émission du bulletin.

### Solution

| # | Diagramme | Justification |
|---|-----------|---------------|
| 1 | **Diagramme de séquence** | Vue dynamique des échanges de **messages** entre acteurs dans le **temps** |
| 2 | **Diagramme de composants** | Modules logiciels et leurs dépendances (interfaces, services) |
| 3 | **Diagramme de classes** | Structure statique : entités, attributs, méthodes, **multiplicités** |
| 4 | **Diagramme de déploiement** | Topologie physique : nœuds (serveurs) et artefacts (binaires, fichiers) |
| 5 | **Diagramme de flux de données (DFD)** | Circulation et transformations de la donnée à travers les processus |

### Astuce / Piège
> ⚠️ **DFD n'est pas UML strict**, mais il fait partie des modèles enseignés dans le cours. Il est complémentaire au diagramme de classes (structure des données) et au diagramme de séquence (dynamique métier).

---

# Bloc E — Qualité, sécurité, gouvernance

## Exercice 14 — Audit qualité de données — les 6 dimensions

### Énoncé
Vous auditez la table `CLIENT` d'une entreprise. Voici un échantillon :

| id_client | nom            | email                  | telephone        | code_postal | date_inscription |
|-----------|----------------|------------------------|------------------|-------------|------------------|
| 1         | Alice Martin   | alice@mail.com         | 514-555-0101     | H2X 1Y4     | 2023-03-15       |
| 2         | Bob Dupont     | bob@mail               | 5145550202       | H3Z9        | 2024-13-45       |
| 3         | Alice Martin   | alice@mail.com         | 514-555-0101     | H2X 1Y4     | 2023-03-15       |
| 4         | Carole Tremblay| (vide)                 | 514-555-0303     | H4A 2B5     | 2025-07-22       |
| 5         | DUPONT, Bob    | bob.dupont@mail.com    | +1-514-555-0202  | h3z 1k1     | 2024-08-10       |
| 6         | Dali Salvador  | dali@mail.com          | (vide)           | (vide)      | 2099-01-01       |

**Question** : pour chaque **dimension de qualité** (parmi les 6), identifier au moins un problème dans cet échantillon, le ligne(s) concernée(s), et proposer une règle de validation.

### Solution

| Dimension | Problème détecté | Ligne(s) | Règle de validation |
|-----------|------------------|----------|---------------------|
| **Exactitude** | Date d'inscription `2099-01-01` (futur) | 6 | `CHECK (date_inscription <= CURRENT_DATE)` |
| **Complétude** | Email vide pour Carole ; téléphone et code postal vides pour Dali | 4, 6 | `NOT NULL` sur colonnes obligatoires (email, téléphone) |
| **Cohérence** | Bob existe deux fois (lignes 2 et 5) sous deux formats : `bob@mail` / `bob.dupont@mail.com`, casse différente, code postal `H3Z9` vs `h3z 1k1` | 2, 5 | Normalisation au moment de l'écriture : majuscules, format unifié |
| **Fraîcheur (Timeliness)** | Pas directement visible ici, mais l'absence de date de dernière mise à jour rend impossible le suivi. | — | Ajouter `date_modification` avec déclencheur |
| **Unicité** | Alice Martin (lignes 1 et 3) — **doublon parfait** | 1, 3 | `UNIQUE (email)` ou détection probabiliste (fuzzy matching) sur nom + email |
| **Validité** | `bob@mail` (pas de TLD) ; `H3Z9` (code postal canadien invalide : 6 caractères format ANA NAN) ; `2024-13-45` (date impossible) ; `5145550202` vs `514-555-0202` vs `+1-514-555-0202` (formats incohérents) | 2, 2, 2, 2/5 | Regex sur email, code postal, téléphone ; type `DATE` natif rejette `2024-13-45` |

### Plan d'action proposé
1. **Court terme** : déduplication (lignes 1/3 et 2/5) avec règles de fusion (garder l'email le plus complet, le téléphone le plus normalisé).
2. **Moyen terme** : ajout de contraintes `CHECK`, `NOT NULL`, `UNIQUE` et regex à la BD.
3. **Long terme** : pipeline d'**ingestion validé** côté application (normalisation systématique : casse, format de téléphone international E.164, code postal sans espace, etc.).
4. **Indicateurs** : suivre `% de champs complétés`, `nombre de doublons détectés`, `taux de conformité` mensuellement.

### Astuce / Piège
> ⚠️ La règle « **un email vide = donnée incomplète** » est aussi un échec **validité** si le champ est censé être un email. Les dimensions se **chevauchent** souvent.
>
> ⚠️ La **déduplication** ne se fait pas qu'à coup de `DISTINCT` : il faut souvent des règles **floues** (fuzzy matching : Levenshtein, Soundex) pour repérer « Bob Dupont » vs « DUPONT, Bob ».

---

## Exercice 15 — CIA + 6 piliers : étude de cas API publique

### Énoncé
Vous concevez une **API REST publique** exposant les données de santé anonymisées d'un hôpital (statistiques, séries temporelles d'occupation des lits) à des chercheurs et journalistes.

**Question** : pour chaque **pilier de la triade CIA** et chaque **pilier des 6 défis de consommation**, citez au moins une mesure technique concrète à mettre en place.

### Solution

#### Triade CIA
| Pilier | Mesure |
|--------|--------|
| **Confidentialité** | **Anonymisation préalable** des données (k-anonymity, suppression d'identifiants directs et quasi-identifiants), accès aux endpoints sensibles uniquement avec clé API (rate-limited), chiffrement TLS 1.3 obligatoire (`HSTS`) |
| **Intégrité** | Signature HMAC des réponses, hash SHA-256 publié pour chaque dataset téléchargeable, journalisation immuable des modifications côté source |
| **Disponibilité** | Hébergement multi-zone (AWS multi-AZ), CDN (CloudFront) pour distribution mondiale, monitoring (Prometheus + Grafana), PRA testé trimestriellement, protection DDoS (AWS Shield, Cloudflare) |

#### Les 6 piliers de la consommation (ACLITR)
| Pilier | Mesure |
|--------|--------|
| **Authentification** | Clé API par chercheur (générée via portail), MFA pour les utilisateurs administrateurs, OAuth2 pour les apps tierces |
| **Chiffrement** | TLS 1.3 en transit ; AES-256 au repos sur la base et le stockage objet ; rotation des clés via AWS KMS |
| **Latence** | CDN, cache HTTP (`Cache-Control`, `ETag`), pagination obligatoire (`?page=&limit=`), endpoints `/v1/aggregates` pré-calculés |
| **Intégrité** | Hash publié par dataset, signature des réponses, validation côté client recommandée |
| **Traçabilité** | Logs centralisés (ELK ou CloudWatch), conservation 1 an, audit trail par clé API (qui a appelé quoi, quand) |
| **Résilience** | Multi-AZ, *circuit breakers*, backups automatisés (RPO 1h, RTO 4h), file d'attente d'écriture (Kafka) pour absorber les pics |

#### Aspects gouvernance à mentionner
- **Validation par les 3 instances** : gouvernance des données (anonymisation conforme RGPD/Loi 25), comité d'architecture (techno standard validée), responsables métiers (besoins chercheurs).
- **Classification des données** : statistiques agrégées = publiques ; séries individuelles = confidentielles → endpoints séparés et droits différenciés.
- **Principe du moindre privilège** : un journaliste reçoit uniquement les endpoints agrégés, pas les détails patient.

### Astuce / Piège
> ⚠️ Une donnée « anonymisée » peut redevenir **ré-identifiable** par croisement (k-anonymity insuffisant + données externes). Toujours évaluer le **risque de ré-identification** avant publication.
>
> ⚠️ **Ne pas confondre anonymisation (irréversible) et pseudonymisation (réversible avec clé)**. Le RGPD distingue les deux.

---

# Conseils stratégiques pour l'examen

### Avant l'examen
- Faire les **15 exercices à blanc** en chronométré (~7-8h total).
- Revoir l'**anti-sèche express** du guide (`guide_examen_conception_bd.md`).
- Refaire de mémoire les 4 règles de passage et les 6 dimensions de qualité.

### Pendant l'examen
- **Lire l'énoncé en entier** avant d'écrire (5 min de lecture vaut 30 min de réécriture).
- Pour un MCD : **toujours commencer par lister les entités**, puis les associations, puis cardinalités, puis traduction relationnelle.
- **Justifier chaque cardinalité** par une phrase de l'énoncé citée entre guillemets.
- Sur un choix technologique (SQL vs NoSQL, REST vs WebSocket, DW vs DL) : structurer en **critères → choix → justification**.
- Garder **5 minutes finales** pour relire le français (5 % du barème).

### Après l'examen
- Mettre à jour ce fichier avec les questions tombées (vraie ou fausse pareto rétroactive).
- Identifier les points où vous avez perdu : c'est votre prochain itéré à étudier.

Bonne préparation !
