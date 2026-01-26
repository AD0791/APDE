# DSA et Design Patterns (50 Questions + Reponses)

Contexte: entretien pour analyste programmeur - unibankhaiti.

1) Q: Qu'est-ce qu'un tableau (array)?
   A: Structure contigue avec acces O(1) par index.
2) Q: Avantage d'une liste chainee?
   A: Insertion/suppression O(1) si position connue.
3) Q: Inconvenient d'une liste chainee?
   A: Acces par index O(n).
4) Q: Qu'est-ce qu'une pile (stack)?
   A: LIFO, operations push/pop.
5) Q: Qu'est-ce qu'une file (queue)?
   A: FIFO, operations enqueue/dequeue.
6) Q: Difference entre queue et deque?
   A: Deque permet ajout/suppression des deux cotes.
7) Q: Qu'est-ce qu'un arbre binaire?
   A: Structure avec max 2 enfants par noeud.
8) Q: Qu'est-ce qu'un BST?
   A: Arbre binaire de recherche: gauche < noeud < droite.
9) Q: Complexite recherche BST equilibré?
   A: O(log n).
10) Q: Qu'est-ce qu'un heap?
    A: Arbre partiellement ordonne (min-heap/max-heap).
11) Q: A quoi sert un heap?
    A: Priorite et tri (heap sort).
12) Q: Qu'est-ce qu'un graphe?
    A: Sommets et aretes (oriente/non oriente).
13) Q: BFS vs DFS?
    A: BFS explore par niveau; DFS en profondeur.
14) Q: Complexite BFS/DFS?
    A: O(V+E).
15) Q: Qu'est-ce qu'un cycle dans un graphe?
    A: Chemin qui revient au sommet de depart.
16) Q: Qu'est-ce que Dijkstra?
    A: Algo plus court chemin poids positifs.
17) Q: Qu'est-ce que Bellman-Ford?
    A: Plus court chemin avec poids negatifs.
18) Q: Qu'est-ce que un tri stable?
    A: Conserve ordre des elements egaux.
19) Q: Complexite du tri rapide (quick sort)?
    A: O(n log n) moyenne, O(n^2) pire.
20) Q: Quand utiliser merge sort?
    A: Stable, O(n log n), utile pour listes et grandes donnees.
21) Q: Qu'est-ce que la notation Big-O?
    A: Mesure asymptotique du temps/memoire.
22) Q: Difference O(1), O(log n), O(n)?
    A: Constante, logarithmique, lineaire.
23) Q: Qu'est-ce que un hash table?
    A: Structure associee cle->valeur, acces moyen O(1).
24) Q: Collision dans hash table?
    A: Deux cles ont meme hash; resoudre par chaining/probing.
25) Q: Qu'est-ce que un trie?
    A: Arbre pour mots, rapide pour prefixe.
26) Q: Qu'est-ce que memoization?
    A: Cache des resultats de fonction.
27) Q: Qu'est-ce que la programmation dynamique?
    A: Resoudre sous-problemes et memoriser.
28) Q: Difference DP top-down vs bottom-up?
    A: Top-down recursif; bottom-up iteratif.
29) Q: Qu'est-ce que un algorithme greedy?
    A: Choix local optimal a chaque etape.
30) Q: Exemple de greedy?
    A: Selection d'activites, Huffman.
31) Q: Qu'est-ce que la complexite spatiale?
    A: Memoire utilisee par un algorithme.
32) Q: Qu'est-ce que le backtracking?
    A: Explorer solutions avec retour arriere.
33) Q: Qu'est-ce que la recherche binaire?
    A: Chercher dans tableau trie en O(log n).
34) Q: Qu'est-ce que le pattern Factory?
    A: Creer objets sans exposer la creation.
35) Q: Pattern Builder?
    A: Construire objet complexe et lisible.
36) Q: Pattern Singleton?
    A: Une seule instance globale.
37) Q: Pattern Observer?
    A: Notifier des abonnes lors d'un changement.
38) Q: Pattern Strategy?
    A: Algorithmes interchangeables.
39) Q: Pattern Decorator?
    A: Ajouter comportements sans modifier classe.
40) Q: Pattern Adapter?
    A: Convertir interface.
41) Q: Pattern Facade?
    A: Interface simple pour sous-systeme.
42) Q: Pattern Command?
    A: Encapsuler une requete comme objet.
43) Q: Pattern State?
    A: Comportement change selon etat.
44) Q: Pattern Template Method?
    A: Squelette d'algo definissant des etapes.
45) Q: Pattern Proxy?
    A: Controle d'acces a un objet.
46) Q: Pattern Repository?
    A: Abstraction d'acces aux donnees.
47) Q: Quand utiliser un pattern?
    A: Quand il resolvra un probleme recurrent, pas par defaut.
48) Q: Risques de sur-ingenierie?
    A: Complexite inutile, maintenance difficile.
49) Q: Comment choisir une structure de donnees?
    A: Selon operations dominantes et complexites.
50) Q: Pourquoi DSA est critique en banque?
    A: Performance, fiabilite et scalabilite des traitements.
