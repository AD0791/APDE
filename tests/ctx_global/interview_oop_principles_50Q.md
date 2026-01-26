# OOP et principes de conception (50 Questions + Reponses)

Contexte: entretien pour analyste programmeur - unibankhaiti.

1) Q: Qu'est-ce que l'OOP?
   A: Paradigme base sur objets et encapsulation.
2) Q: Qu'est-ce qu'une classe?
   A: Modele pour creer des objets.
3) Q: Qu'est-ce qu'un objet?
   A: Instance d'une classe avec etat/comportement.
4) Q: Encapsulation?
   A: Cacher l'etat interne via interface publique.
5) Q: Abstraction?
   A: Exposer l'essentiel, masquer les details.
6) Q: Heritage?
   A: Reutiliser et specialiser via classes derivees.
7) Q: Polymorphisme?
   A: Meme interface, comportements differents.
8) Q: Difference entre interface et classe abstraite?
   A: Interface definit contrat; classe abstraite peut avoir implementation.
9) Q: Composition vs heritage?
   A: Composition preferer pour flexibilité; heritage pour is-a.
10) Q: Qu'est-ce que SOLID?
    A: 5 principes pour design maintenable.
11) Q: S (Single Responsibility)?
    A: Une classe = une raison de changer.
12) Q: O (Open/Closed)?
    A: Ouvert a extension, ferme a modification.
13) Q: L (Liskov Substitution)?
    A: Sous-type substituable au type de base.
14) Q: I (Interface Segregation)?
    A: Petites interfaces specialisees.
15) Q: D (Dependency Inversion)?
    A: Dependre d'abstractions, pas de concretions.
16) Q: Qu'est-ce que DRY?
    A: Don't Repeat Yourself.
17) Q: Qu'est-ce que KISS?
    A: Keep It Simple, Stupid.
18) Q: YAGNI?
    A: You Aren't Gonna Need It.
19) Q: Qu'est-ce que le principe de Demeter?
    A: Parler seulement aux voisins proches.
20) Q: Couplage vs cohesion?
    A: Couplage faible, cohesion forte ideal.
21) Q: Qu'est-ce que l'injection de dependances?
    A: Fournir dependances de l'exterieur.
22) Q: Pourquoi utiliser des interfaces?
    A: Decoupler et faciliter tests.
23) Q: Qu'est-ce que une classe immuable?
    A: Etat non modifiable apres creation.
24) Q: Avantages de l'immutabilite?
    A: Thread-safe, predictible.
25) Q: Qu'est-ce que un constructeur?
    A: Methode speciale d'initialisation.
26) Q: Overloading vs overriding?
    A: Overloading = meme nom, params differents; overriding = redefinir.
27) Q: Qu'est-ce qu'une methode statique?
    A: Appartient a la classe, pas a l'objet.
28) Q: Qu'est-ce que un getter/setter?
    A: Acces controle aux attributs.
29) Q: Qu'est-ce que la visibilite (public/private/protected)?
    A: Controle d'acces aux membres.
30) Q: Qu'est-ce qu'un objet value?
    A: Identifie par ses valeurs, pas par une identite.
31) Q: Qu'est-ce que un objet entity?
    A: Possede une identite unique.
32) Q: Qu'est-ce que un agregat (DDD)?
    A: Groupe d'entites avec invariants.
33) Q: Qu'est-ce qu'un repository?
    A: Abstraction d'acces aux donnees.
34) Q: Qu'est-ce que un service de domaine?
    A: Logique metier qui ne appartient pas a une entite.
35) Q: Qu'est-ce que la cohesion fonctionnelle?
    A: Elements d'une classe servent un seul but.
36) Q: Quand utiliser le pattern Factory?
    A: Creer objets sans exposer la logique de creation.
37) Q: Qu'est-ce que le pattern Strategy?
    A: Encapsuler des algorithmes interchangeables.
38) Q: Qu'est-ce que le pattern Observer?
    A: Notifier dependants lors d'un changement.
39) Q: Qu'est-ce que le pattern Adapter?
    A: Adapter une interface existante.
40) Q: Qu'est-ce que le pattern Singleton?
    A: Une seule instance globale (a utiliser avec prudence).
41) Q: Pourquoi eviter les Singletons?
    A: Couplage global, tests difficiles.
42) Q: Qu'est-ce que le refactoring?
    A: Ameliorer code sans changer comportement.
43) Q: Qu'est-ce que la dette technique?
    A: Cout futur causé par solutions rapides.
44) Q: Qu'est-ce que le TDD?
    A: Test-Driven Development, tests avant code.
45) Q: Difference entre test unitaire et integration?
    A: Unitaire isole; integration verifie interactions.
46) Q: Qu'est-ce que le "code smell"?
    A: Indice d'un probleme de design.
47) Q: Pourquoi documenter une API?
    A: Facilite usage et maintenance.
48) Q: Qu'est-ce que l'interface segregation en pratique?
    A: Eviter interfaces trop larges; separer par besoins.
49) Q: Qu'est-ce que un objet DTO?
    A: Objet de transfert de donnees sans logique.
50) Q: Comment appliquer OOP en contexte bancaire?
    A: Modeliser comptes, transactions, clients, regles.
