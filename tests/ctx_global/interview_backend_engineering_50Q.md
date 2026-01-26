# Backend Engineering (50 Questions + Reponses)

Contexte: entretien pour analyste programmeur - unibankhaiti.

1) Q: Qu'est-ce qu'un API gateway?
   A: Point d'entree unique qui route, securise et agrège les services.
2) Q: Difference entre REST et RPC?
   A: REST est ressource/HTTP; RPC est action/operation.
3) Q: Qu'est-ce que l'idempotence?
   A: Meme requete repetee donne le meme resultat (ex: GET, PUT).
4) Q: Pourquoi utiliser la pagination?
   A: Eviter gros transferts et ameliorer performance.
5) Q: Difference entre offset et cursor pagination?
   A: Offset simple mais lent; cursor stable et performant sur gros volumes.
6) Q: Qu'est-ce qu'un reverse proxy?
   A: Serveur qui transfere requetes vers backend, cache, TLS.
7) Q: Qu'est-ce qu'un load balancer?
   A: Repartit le trafic entre serveurs pour disponibilite.
8) Q: Qu'est-ce que le connection pooling?
   A: Reutiliser connexions DB pour reduire cout de creation.
9) Q: Qu'est-ce qu'un cache applicatif?
   A: Stocker donnees frequentes en memoire (Redis) pour reduire latence.
10) Q: Strategie de cache aside?
    A: App lit cache, si miss lit DB puis remplit cache.
11) Q: Cache write-through vs write-back?
    A: Write-through ecrit cache+DB; write-back ecrit cache puis DB plus tard.
12) Q: Invalidation du cache?
    A: Supprimer/expirer les cles apres modification des donnees.
13) Q: Qu'est-ce qu'un circuit breaker?
    A: Coupe appels a un service instable pour eviter panne en cascade.
14) Q: Que signifie "backpressure"?
    A: Controle du flux pour eviter surcharge en streaming.
15) Q: Qu'est-ce que JWT?
    A: Jeton signe contenant des claims; stateless auth.
16) Q: Difference entre authentication et authorization?
    A: Authentifier identite vs autoriser actions.
17) Q: Qu'est-ce que OAuth2?
    A: Protocole d'autorisation pour acces delegue.
18) Q: Qu'est-ce que un refresh token?
    A: Jeton long pour renouveler un access token.
19) Q: Pourquoi chiffrer au repos?
    A: Protege donnees si stockage compromet.
20) Q: TLS termine ou?
    A: Soit au LB, reverse proxy, ou service; choix impacte securite.
21) Q: Difference entre message queue et pub/sub?
    A: Queue consomme une fois; pub/sub diffuse a plusieurs.
22) Q: Qu'est-ce que un "dead letter queue"?
    A: File pour messages echoues pour analyse/retraitement.
23) Q: Que signifie "at-least-once"?
    A: Message peut etre livre plusieurs fois; besoin idempotence.
24) Q: Comment gerer transactions distribuées?
    A: Saga pattern ou 2PC selon besoins.
25) Q: Qu'est-ce que un index DB et pourquoi?
    A: Structure pour accelerer les requetes; cout en ecriture.
26) Q: Difference entre SQL et NoSQL?
    A: SQL schema fixe/relations; NoSQL schema flexible, scaling.
27) Q: Qu'est-ce que un "read replica"?
    A: Replique pour lectures; soulage le primary.
28) Q: Qu'est-ce que la replication asynchrone?
    A: Ecriture non bloquante; risque de lag.
29) Q: Qu'est-ce que le sharding?
    A: Partitionner donnees entre plusieurs noeuds.
30) Q: Qu'est-ce que le "N+1 query problem"?
    A: Requetes multiples pour relations; resoudre par join/batch.
31) Q: Qu'est-ce que la validation cote serveur?
    A: Verifier toutes donnees recues avant traitement.
32) Q: Pourquoi limiter le taux (rate limiting)?
    A: Proteger services contre abus et DDoS.
33) Q: Qu'est-ce que le "retry with jitter"?
    A: Reessais avec delai aleatoire pour eviter pics.
34) Q: Qu'est-ce que la journalisation (logging) structuree?
    A: Logs en JSON avec champs pour recherche/alerting.
35) Q: Qu'est-ce que la correlation d'ID?
    A: Identifier un flux de requetes entre services.
36) Q: Difference entre monolithe et microservices?
    A: Monolithe centralise; microservices decouples.
37) Q: Quand choisir un monolithe?
    A: Petite equipe, complexite reduite, time-to-market.
38) Q: Qu'est-ce que l'event sourcing?
    A: Stocker l'historique des evenements pour reconstruire l'etat.
39) Q: Qu'est-ce que CQRS?
    A: Separer commandes (write) et requetes (read).
40) Q: Qu'est-ce que la "eventual consistency"?
    A: Donnees convergent avec le temps, pas immediat.
41) Q: A quoi sert un schema de versioning API?
    A: Permet evolutions sans casser clients.
42) Q: Qu'est-ce que un webhook?
    A: Callback HTTP appele lors d'un evenement.
43) Q: Qu'est-ce que la compression HTTP?
    A: gzip/brotli reduisent taille des reponses.
44) Q: Que sont les codes 4xx/5xx?
    A: 4xx erreur client, 5xx erreur serveur.
45) Q: Qu'est-ce que la latence p95?
    A: 95% des requetes sont plus rapides que cette valeur.
46) Q: Pourquoi ajouter des timeouts?
    A: Eviter blocages et ressources monopolisees.
47) Q: Qu'est-ce que l'observabilite?
    A: Logs, metrics, traces pour comprendre le systeme.
48) Q: Difference entre stateless et stateful?
    A: Stateless ne garde pas etat local; facile a scaler.
49) Q: Que signifie "graceful shutdown"?
    A: Arret en finissant les requetes en cours.
50) Q: Comment proteger une API bancaire?
    A: TLS, auth forte, RBAC, audit logs, rate limiting.
