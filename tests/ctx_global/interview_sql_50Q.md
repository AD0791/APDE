# SQL (50 Questions + Reponses)

Contexte: entretien pour analyste programmeur - unibankhaiti.

1) Q: Qu'est-ce que SQL?
   A: Langage de requetes pour manipuler des bases relationnelles.
2) Q: Difference entre DDL et DML?
   A: DDL definie schema; DML manipule les donnees.
3) Q: A quoi sert SELECT?
   A: Lire des donnees.
4) Q: Que fait WHERE?
   A: Filtre les lignes.
5) Q: Difference entre INNER JOIN et LEFT JOIN?
   A: INNER garde correspondances; LEFT garde tout a gauche.
6) Q: Qu'est-ce qu'un CROSS JOIN?
   A: Produit cartesien entre tables.
7) Q: Que fait GROUP BY?
   A: Regroupe lignes pour agregats.
8) Q: A quoi sert HAVING?
   A: Filtrer apres aggregation.
9) Q: Difference entre COUNT(*) et COUNT(col)?
   A: COUNT(*) compte toutes lignes; COUNT(col) ignore NULL.
10) Q: Qu'est-ce que NULL?
    A: Valeur inconnue/absente, pas egal a 0 ou ''.
11) Q: Comment tester NULL?
    A: Utiliser IS NULL / IS NOT NULL.
12) Q: Qu'est-ce que l'ordre d'execution logique?
    A: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY.
13) Q: Difference entre UNION et UNION ALL?
    A: UNION elimine doublons; UNION ALL conserve.
14) Q: A quoi sert ORDER BY?
    A: Trier les resultats.
15) Q: Comment limiter le resultat?
    A: LIMIT/OFFSET ou FETCH FIRST selon SGBD.
16) Q: Qu'est-ce qu'un index?
    A: Structure pour accelerer les recherches.
17) Q: Pourquoi un index peut ralentir?
    A: Cout en ecriture et stockage.
18) Q: Qu'est-ce qu'une vue?
    A: Requete sauvegardee presentee comme table.
19) Q: Vue materalisee?
    A: Vue stockee physiquement, necessite refresh.
20) Q: Qu'est-ce qu'une cle primaire?
    A: Identifiant unique non NULL pour une table.
21) Q: Cle etrangere?
    A: Reference a cle primaire d'une autre table.
22) Q: Contraintes courantes?
    A: NOT NULL, UNIQUE, CHECK, FOREIGN KEY.
23) Q: Qu'est-ce qu'une transaction?
    A: Unite atomique de travail (ACID).
24) Q: Propriete ACID?
    A: Atomicite, Coherence, Isolation, Durabilite.
25) Q: Niveaux d'isolation?
    A: Read Uncommitted, Read Committed, Repeatable Read, Serializable.
26) Q: Qu'est-ce que le phantom read?
    A: Nouvelles lignes apparaissent dans une transaction.
27) Q: Qu'est-ce que le dirty read?
    A: Lire des donnees non commitees.
28) Q: Qu'est-ce que le non-repeatable read?
    A: Meme ligne lue differente dans la meme transaction.
29) Q: A quoi sert EXPLAIN?
    A: Voir le plan d'execution pour optimiser.
30) Q: Quand utiliser DISTINCT?
    A: Pour eliminer les doublons.
31) Q: Que fait COALESCE?
    A: Retourne la premiere valeur non NULL.
32) Q: Qu'est-ce que CASE?
    A: Expression conditionnelle.
33) Q: Difference entre DELETE et TRUNCATE?
    A: DELETE supprime ligne par ligne; TRUNCATE vide table rapidement.
34) Q: Difference entre CHAR et VARCHAR?
    A: CHAR fixe; VARCHAR variable.
35) Q: Qu'est-ce que une sous-requete?
    A: Requete imbriquee dans une autre.
36) Q: CTE?
    A: Common Table Expression, avec WITH.
37) Q: Qu'est-ce que window functions?
    A: Fonctions analytiques sur fenetre (OVER).
38) Q: Exemple de window function?
    A: ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...).
39) Q: Qu'est-ce que un index composite?
    A: Index sur plusieurs colonnes.
40) Q: Ordre des colonnes dans un index?
    A: L'ordre doit correspondre aux filtres principaux.
41) Q: Qu'est-ce que la normalisation?
    A: Reduction redondance par formes normales.
42) Q: 1NF?
    A: Valeurs atomiques, pas de groupes repetes.
43) Q: 2NF?
    A: Pas de dependance partielle sur cle.
44) Q: 3NF?
    A: Pas de dependance transitive.
45) Q: Quand denormaliser?
    A: Pour performance lecture en acceptant redondance.
46) Q: Qu'est-ce que un index unique?
    A: Enforce unicite des valeurs.
47) Q: Qu'est-ce que un trigger?
    A: Code execute automatiquement sur insert/update/delete.
48) Q: Qu'est-ce que une sequence?
    A: Generateur de nombres uniques.
49) Q: Comment se proteger contre SQL injection?
    A: Requetes preparees, validation, moindres privileges.
50) Q: Pourquoi utiliser des transactions en banque?
    A: Garantir coherence et fiabilite des operations.
