# Databases (50 Questions + Reponses)

Contexte: entretien pour analyste programmeur - unibankhaiti.

1) Q: Qu'est-ce qu'un SGBD?
   A: Systeme de gestion de base de donnees.
2) Q: Difference entre base relationnelle et NoSQL?
   A: Relationnelle = schema/SQL; NoSQL = schema flexible.
3) Q: Avantage principal d'une base relationnelle?
   A: Integrite des donnees via contraintes.
4) Q: Qu'est-ce que la redondance des donnees?
   A: Donnees dupliquees dans plusieurs endroits.
5) Q: Pourquoi normaliser?
   A: Reduire redondance et anomalies.
6) Q: Qu'est-ce qu'une cle candidate?
   A: Attributs pouvant identifier une ligne.
7) Q: Cle primaire vs cle unique?
   A: Primaire identifie et ne peut etre NULL; unique autorise un NULL.
8) Q: Qu'est-ce qu'une cle surrogate?
   A: Identifiant artificiel (auto-increment).
9) Q: Que signifie "cardinalite"?
   A: Nombre de lignes et relations entre entites.
10) Q: Qu'est-ce qu'un index B-Tree?
    A: Index equilibre pour requetes range/equality.
11) Q: Qu'est-ce qu'un index hash?
    A: Index pour equality, pas pour range.
12) Q: Que signifie OLTP?
    A: Online Transaction Processing, operations rapides.
13) Q: Que signifie OLAP?
    A: Analyse et rapports sur gros volumes.
14) Q: Qu'est-ce qu'un data warehouse?
    A: Base optimisee pour analytique et historique.
15) Q: Et un data mart?
    A: Sous-ensemble du warehouse pour un domaine.
16) Q: Qu'est-ce que la replication?
    A: Copie des donnees vers d'autres noeuds.
17) Q: Replication synchrone vs asynchrone?
    A: Synchrone garantit ecriture; asynchrone peut lagger.
18) Q: Qu'est-ce que le sharding?
    A: Partitionner les donnees par cle.
19) Q: Qu'est-ce que le partitionnement?
    A: Diviser une table en segments logiques.
20) Q: Pourquoi partitionner?
    A: Ameliorer performance et maintenance.
21) Q: Qu'est-ce que le CAP theorem?
    A: Cohérence, Disponibilite, Partition tolerance: choisir 2.
22) Q: Qu'est-ce que BASE?
    A: Basically Available, Soft state, Eventual consistency.
23) Q: ACID vs BASE?
    A: ACID fort coherence; BASE plus disponible/elastic.
24) Q: Qu'est-ce que un "write-ahead log"?
    A: Journal ecrit avant les donnees pour recovery.
25) Q: Qu'est-ce que le checkpoint?
    A: Point de sauvegarde pour limiter replay du log.
26) Q: Qu'est-ce que la sauvegarde full/incremental?
    A: Full = tout; incremental = changements depuis dernier backup.
27) Q: RPO et RTO?
    A: RPO = perte acceptable; RTO = temps de reprise.
28) Q: Qu'est-ce que la contention?
    A: Conflit pour ressources partagées.
29) Q: Qu'est-ce qu'un verrouillage pessimiste?
    A: Bloque acces concurrent pour eviter conflits.
30) Q: Et un verrouillage optimiste?
    A: Valide la version avant commit, pas de lock prolongé.
31) Q: Qu'est-ce que MVCC?
    A: Multi-Version Concurrency Control, plusieurs versions visibles.
32) Q: Qu'est-ce que la fragmentation?
    A: Donnees eparpillees, degrade performance.
33) Q: Qu'est-ce qu'un ORM?
    A: Outil mapping objets vers tables.
34) Q: Risques d'un ORM?
    A: Requetes cachees, N+1, performance.
35) Q: Qu'est-ce que la migration de schema?
    A: Evolution contrôlée du schema via scripts.
36) Q: Pourquoi documenter le schema?
    A: Faciliter maintenance et comprehension.
37) Q: Qu'est-ce que un "slow query log"?
    A: Journal des requetes lentes.
38) Q: Comment choisir une cle de sharding?
    A: Cle stable, bonne distribution, faible hot-spot.
39) Q: Qu'est-ce qu'un "hot spot"?
    A: Cle ou noeud surchargé par trop de traffic.
40) Q: Qu'est-ce que la compression de donnees?
    A: Reduit stockage et parfois I/O.
41) Q: Qu'est-ce que un index couvrant?
    A: Index contient toutes colonnes requises par requete.
42) Q: Qu'est-ce que la haute disponibilite?
    A: Minimiser les interruptions de service.
43) Q: Qu'est-ce que le failover?
    A: Bascule automatique vers un noeud de secours.
44) Q: Qu'est-ce qu'un cluster?
    A: Groupe de serveurs geres ensemble.
45) Q: Pourquoi isoler les environnements?
    A: Eviter impacts prod, securite et tests.
46) Q: Qu'est-ce que un "data dictionary"?
    A: Catalogue des objets DB et metadonnees.
47) Q: Pourquoi auditer les acces?
    A: Traçabilite et conformite.
48) Q: Qu'est-ce que la retention des donnees?
    A: Duree de conservation des infos.
49) Q: Qu'est-ce que un "soft delete"?
    A: Marquer supprime sans effacer physiquement.
50) Q: Pourquoi choisir une base relationnelle en banque?
    A: Integrite, transactions fortes, audit.
