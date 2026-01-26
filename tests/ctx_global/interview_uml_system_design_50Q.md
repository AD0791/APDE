# UML et System Design (50 Questions + Reponses)

Contexte: entretien pour analyste programmeur - unibankhaiti.

1) Q: A quoi sert UML?
   A: Standard pour modeliser logiciels et processus.
2) Q: Diagramme de cas d'utilisation?
   A: Montre acteurs et interactions avec le systeme.
3) Q: Diagramme de classes?
   A: Montre classes, attributs, methodes, relations.
4) Q: Diagramme de sequence?
   A: Ordre des messages entre objets dans le temps.
5) Q: Diagramme d'activite?
   A: Flux de travail et decisions.
6) Q: Diagramme d'etats?
   A: Etats possibles d'un objet et transitions.
7) Q: Diagramme de composants?
   A: Decomposition en modules et dependances.
8) Q: Diagramme de deploiement?
   A: Infrastructure physique/logique.
9) Q: Association vs aggregation vs composition?
   A: Association lien; aggregation "has-a" faible; composition "has-a" fort (cycle de vie).
10) Q: Cardinalite en UML?
    A: Multiplicite 0..1, 1..*, etc.
11) Q: Generalisation?
    A: Relation heritage.
12) Q: Realisation?
    A: Implementation d'une interface.
13) Q: Qu'est-ce qu'un diagramme de paquetages?
    A: Organisation en packages et dependances.
14) Q: Notation d'un acteur?
    A: Bonhomme ou stereotype <<actor>>.
15) Q: "Include" vs "extend" en use case?
    A: Include = reutilisation obligatoire; extend = optionnel.
16) Q: A quoi sert un modele conceptuel?
    A: Capturer besoins metier sans details techniques.
17) Q: Difference modele logique vs physique?
    A: Logique = structure DB; physique = implementation SGBD.
18) Q: Qu'est-ce qu'une exigence non fonctionnelle?
    A: Performance, securite, scalabilite, etc.
19) Q: Que signifie SLA?
    A: Accord de niveau de service.
20) Q: Quels sont les objectifs du design systeme?
    A: Fiabilite, performance, securite, evolutivite.
21) Q: Qu'est-ce que la scalabilite verticale?
    A: Augmenter ressources d'une machine.
22) Q: Scalabilite horizontale?
    A: Ajouter des machines.
23) Q: Qu'est-ce que la haute disponibilite?
    A: Minimiser le downtime via redondance.
24) Q: Qu'est-ce que la tolerance aux pannes?
    A: Continuer malgre pannes partielles.
25) Q: Single point of failure?
    A: Composant unique dont la panne arrete le systeme.
26) Q: Qu'est-ce que le capacity planning?
    A: Estimer ressources necessaires.
27) Q: Que signifie "stateless service"?
    A: Pas d'etat local; facile a scaler.
28) Q: Pourquoi utiliser un cache?
    A: Reduire latence et charge.
29) Q: Quels risques du cache?
    A: Donnees obsoletes, invalidation.
30) Q: Qu'est-ce que la partition de base de donnees?
    A: Decouper tables pour performance/maintenance.
31) Q: Qu'est-ce que la replication?
    A: Copier donnees pour lecture et resilence.
32) Q: Qu'est-ce que l'observabilite?
    A: Logs, metrics, traces pour comprendre le systeme.
33) Q: Qu'est-ce que le blue/green deployment?
    A: Deux environnements pour deploiement sans downtime.
34) Q: Qu'est-ce que le canary release?
    A: Deploiement progressif sur petit trafic.
35) Q: Qu'est-ce que l'event-driven architecture?
    A: Services reacts aux evenements.
36) Q: Quand utiliser une file de messages?
    A: Decouplage et traitement asynchrone.
37) Q: Qu'est-ce que le "throughput"?
    A: Volume de requetes par unite de temps.
38) Q: Qu'est-ce que la latence?
    A: Temps de reponse.
39) Q: Qu'est-ce qu'un diagramme C4?
    A: Niveaux: contexte, conteneurs, composants, code.
40) Q: A quoi sert un "sequence diagram" en design?
    A: Clarifier interactions entre services.
41) Q: Qu'est-ce que un "domain model"?
    A: Representation des concepts metier.
42) Q: Qu'est-ce que la separation des concerns?
    A: Isoler les responsabilites.
43) Q: Pourquoi utiliser une API contract?
    A: Stabilite et compatibilite entre services.
44) Q: Qu'est-ce qu'un SLO?
    A: Objectif de niveau de service mesurable.
45) Q: Que signifie MTTR?
    A: Mean Time To Repair.
46) Q: Qu'est-ce que le DR (disaster recovery)?
    A: Plan de reprise apres sinistre.
47) Q: RPO vs RTO?
    A: Perte de donnees acceptable vs temps de reprise.
48) Q: Qu'est-ce qu'un diagramme d'activite UML utile en banque?
    A: Modeliser le flux d'un virement/credit.
49) Q: Qu'est-ce que un "bounded context"?
    A: Limite de modele metier coherent (DDD).
50) Q: Pourquoi documenter l'architecture?
    A: Facilite maintenance, audit, onboarding.
