# DSA FULL — Guide Complet des Structures de Données et Algorithmes

## 📋 Vue d'Ensemble

Ce dossier contient des études de cas complètes sur les Data Structures & Algorithms (structures de données et algorithmes), organisées par niveau de difficulté. Chaque étude présente des problèmes classiques d'entretiens techniques avec des solutions optimisées en Python et Java, dans un contexte bancaire.

---

## 🎯 Structure des Études de Cas

### **Niveau Basique** (`etude_cas_dsa_basique.md`)
**Durée estimée :** 3-4 heures  
**Prérequis :** Bases de programmation (boucles, conditions, fonctions)

**Structures de données :**
- **Arrays/Lists** — Manipulation de tableaux
- **Hash Tables** — Dictionnaires et lookup O(1)
- **Stacks** — LIFO (Last In First Out)
- **Queues** — FIFO (First In First Out)
- **Linked Lists** — Listes chaînées

**Algorithmes :**
- Two Sum — Recherche de paires
- Parenthèses valides — Validation avec stack
- Premier caractère unique — Comptage de fréquences
- Recherche binaire — O(log n)
- Fusion de tableaux triés — Two pointers
- Inversion de liste chaînée — Manipulation de pointeurs

**Complexités visées :** O(1), O(n), O(log n)

**Compétences acquises :**
- ✅ Manipulation efficace de tableaux
- ✅ Utilisation de hash tables pour optimisation
- ✅ Maîtrise des stacks et queues
- ✅ Algorithmes de recherche classiques
- ✅ Analyse de complexité temporelle et spatiale

---

### **Niveau Moyen** (`etude_cas_dsa_moyen.md`)
**Durée estimée :** 4-5 heures  
**Prérequis :** Niveau basique + complexités algorithmiques

**Structures de données :**
- **Trees** — Arbres binaires et BST
- **Heaps** — Min-heap et Max-heap
- **Graphs** — Représentation et traversée
- **Deque** — Double-ended queue

**Algorithmes :**
- Sous-tableau de somme K — Prefix sum
- Fenêtre glissante — Sliding window
- Traversée d'arbre (BFS, DFS) — Level order
- Top K éléments — Heap
- Détection de cycle — Graph traversal
- Plus court chemin — BFS sur graphe

**Patterns algorithmiques :**
- Sliding Window
- Two Pointers avancé
- Prefix Sum / Cumulative
- BFS / DFS
- Heap operations

**Compétences acquises :**
- ✅ Manipulation d'arbres binaires
- ✅ Utilisation de heaps pour optimisation
- ✅ Algorithmes sur graphes
- ✅ Patterns de sliding window
- ✅ Optimisation avec structures avancées

---

### **Niveau Senior** (`etude_cas_dsa_senior.md`)
**Durée estimée :** 6-8 heures  
**Prérequis :** Niveau moyen + expérience en optimisation

**Structures de données :**
- **Tries** — Arbres de préfixes
- **Union-Find** — Disjoint sets
- **Segment Trees** — Requêtes sur intervalles
- **Fenwick Trees** — Binary Indexed Tree

**Algorithmes :**
- Programmation dynamique — DP classiques
- Backtracking — Génération de solutions
- Algorithmes de graphes avancés — Dijkstra, Kruskal
- String matching — KMP, Rabin-Karp
- Divide and Conquer — Merge sort, Quick select

**Patterns avancés :**
- Dynamic Programming (Memoization, Tabulation)
- Greedy Algorithms
- Backtracking avec pruning
- Advanced Graph Algorithms
- String Algorithms

**Compétences acquises :**
- ✅ Résolution de problèmes DP
- ✅ Algorithmes de graphes avancés
- ✅ Optimisation complexe
- ✅ Structures de données spécialisées
- ✅ Analyse d'algorithmes sophistiqués

---

## 📚 Complexités Algorithmiques

### Complexité Temporelle (Time Complexity)

| Notation | Nom | Exemple d'opération |
|----------|-----|---------------------|
| O(1) | Constant | Accès à un index, hash lookup |
| O(log n) | Logarithmique | Binary search, heap operations |
| O(n) | Linéaire | Linear search, array traversal |
| O(n log n) | Linéarithmique | Merge sort, heap sort |
| O(n²) | Quadratique | Nested loops, bubble sort |
| O(2ⁿ) | Exponentiel | Recursive fibonacci naïf |

### Complexité Spatiale (Space Complexity)

| Notation | Description | Exemple |
|----------|-------------|---------|
| O(1) | Espace constant | Variables simples |
| O(n) | Espace linéaire | Tableau de taille n |
| O(log n) | Espace logarithmique | Recursion balanced tree |
| O(n²) | Espace quadratique | Matrice n×n |

---

## 🎓 Structures de Données par Niveau

### Basique
```
Array/List     → Accès O(1), Insertion O(n)
Hash Table     → Lookup O(1), Insert O(1)
Stack          → Push/Pop O(1)
Queue          → Enqueue/Dequeue O(1)
Linked List    → Insert début O(1), Search O(n)
```

### Moyen
```
Binary Tree    → Search O(log n) si balanced
BST            → Insert/Search O(log n) moyenne
Heap           → Insert/Delete O(log n)
Graph          → BFS/DFS O(V + E)
Deque          → Insert/Delete aux deux bouts O(1)
```

### Senior
```
Trie           → Search/Insert O(m) où m = longueur
Union-Find     → Union/Find O(α(n)) ≈ O(1)
Segment Tree   → Query/Update O(log n)
Fenwick Tree   → Query/Update O(log n)
AVL/Red-Black  → All ops O(log n) garanti
```

---

## 💡 Patterns Algorithmiques Essentiels

### 1. Two Pointers
**Quand l'utiliser :** Tableaux triés, palindromes, paires avec somme

```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current = nums[left] + nums[right]
        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1
    return []
```

**Complexité :** O(n) temps, O(1) espace

---

### 2. Sliding Window
**Quand l'utiliser :** Sous-tableaux, sous-chaînes de taille k

```python
def max_sum_subarray(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i-k] + nums[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

**Complexité :** O(n) temps, O(1) espace

---

### 3. Fast & Slow Pointers
**Quand l'utiliser :** Détection de cycle, middle of linked list

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

**Complexité :** O(n) temps, O(1) espace

---

### 4. BFS (Breadth-First Search)
**Quand l'utiliser :** Plus court chemin, level-order traversal

```python
from collections import deque

def bfs(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result
```

**Complexité :** O(V + E) où V = vertices, E = edges

---

### 5. DFS (Depth-First Search)
**Quand l'utiliser :** Backtracking, validation, paths

```python
def dfs_recursive(node, visited):
    if node is None or node in visited:
        return
    
    visited.add(node)
    process(node)
    
    for neighbor in node.neighbors:
        dfs_recursive(neighbor, visited)
```

**Complexité :** O(V + E)

---

### 6. Dynamic Programming
**Quand l'utiliser :** Optimisation, comptage, sous-problèmes chevauchants

```python
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
```

**Complexité :** O(n) avec memoization vs O(2ⁿ) sans

---

## 🔍 Guide de Sélection d'Algorithme

### Vous devez...

**Chercher un élément ?**
- Tableau non trié → Linear search O(n)
- Tableau trié → Binary search O(log n)
- Hash table → Lookup O(1)

**Trouver le maximum/minimum ?**
- Une seule passe → Linear scan O(n)
- Top K éléments → Heap O(n log k)
- Stream de données → Min/Max heap

**Trier des données ?**
- Small dataset → Insertion sort O(n²)
- General purpose → Quick sort O(n log n) avg
- Guaranteed O(n log n) → Merge sort
- Counting sort si range limité → O(n + k)

**Parcourir un graphe ?**
- Plus court chemin → BFS
- Explorer tous les chemins → DFS
- Chemin pondéré → Dijkstra
- Détection de cycle → Union-Find ou DFS

**Optimiser un problème ?**
- Sous-problèmes chevauchants → Dynamic Programming
- Choix optimal local → Greedy
- Explorer toutes solutions → Backtracking

---

## 📖 Problèmes Classiques par Catégorie

### Arrays
- ✅ Two Sum
- ✅ Best Time to Buy and Sell Stock
- ✅ Maximum Subarray (Kadane)
- ✅ Product of Array Except Self
- ✅ Rotate Array

### Strings
- ✅ Valid Palindrome
- ✅ Longest Substring Without Repeating
- ✅ Anagram Detection
- ✅ String to Integer (atoi)
- ✅ Longest Common Prefix

### Linked Lists
- ✅ Reverse Linked List
- ✅ Merge Two Sorted Lists
- ✅ Detect Cycle
- ✅ Remove Nth Node From End
- ✅ Intersection of Two Lists

### Trees
- ✅ Maximum Depth
- ✅ Same Tree
- ✅ Invert Binary Tree
- ✅ Level Order Traversal
- ✅ Validate BST

### Graphs
- ✅ Number of Islands
- ✅ Clone Graph
- ✅ Course Schedule
- ✅ Word Ladder
- ✅ Network Delay Time

### Dynamic Programming
- ✅ Climbing Stairs
- ✅ Coin Change
- ✅ Longest Increasing Subsequence
- ✅ 0/1 Knapsack
- ✅ Edit Distance

---

## 🛠️ Outils et Configuration

### Environnement Python

```bash
# Python 3.9+
python --version

# Installer les outils
pip install pytest  # Testing
pip install black   # Formatting
pip install mypy    # Type checking

# Mesurer la performance
import time
import tracemalloc

start = time.time()
tracemalloc.start()

# Votre code ici

print(f"Time: {time.time() - start:.4f}s")
print(f"Memory: {tracemalloc.get_traced_memory()[1] / 1024 / 1024:.2f} MB")
tracemalloc.stop()
```

### Environnement Java

```bash
# Java 17+
java --version

# Maven project structure
mkdir -p src/main/java/com/banque/dsa
mkdir -p src/test/java/com/banque/dsa

# Compile et run
javac -d bin src/main/java/com/banque/dsa/*.java
java -cp bin com.banque.dsa.Main

# Mesurer la performance
long startTime = System.nanoTime();
// Votre code ici
long endTime = System.nanoTime();
System.out.println("Time: " + (endTime - startTime) / 1_000_000 + "ms");
```

---

## 🎯 Objectifs d'Apprentissage

### Niveau Basique ✅
Après ce niveau, vous devriez pouvoir :
- [ ] Résoudre des problèmes Two Sum en O(n)
- [ ] Utiliser des stacks pour validation
- [ ] Implémenter une recherche binaire
- [ ] Manipuler des linked lists
- [ ] Analyser la complexité de base

### Niveau Moyen ✅
Après ce niveau, vous devriez pouvoir :
- [ ] Utiliser sliding window efficacement
- [ ] Traverser des arbres (BFS/DFS)
- [ ] Résoudre des problèmes de heaps
- [ ] Appliquer prefix sum
- [ ] Optimiser avec structures avancées

### Niveau Senior ✅
Après ce niveau, vous devriez pouvoir :
- [ ] Résoudre des problèmes DP classiques
- [ ] Implémenter Dijkstra et autres algos de graphe
- [ ] Utiliser tries pour string matching
- [ ] Optimiser avec segment trees
- [ ] Analyser des algorithmes complexes

---

## 📚 Ressources Complémentaires

### Livres Essentiels
- **"Introduction to Algorithms"** — Cormen, Leiserson, Rivest (CLRS)
  - *La bible des algorithmes*
- **"Cracking the Coding Interview"** — Gayle Laakmann McDowell
  - *Guide pratique pour entretiens*
- **"Algorithm Design Manual"** — Steven Skiena
  - *Approche pragmatique et exemples*

### Plateformes de Pratique
- **LeetCode** — 2000+ problèmes, contests
- **HackerRank** — Challenges et certifications
- **Codeforces** — Competitive programming
- **AlgoExpert** — Vidéos explicatives détaillées

### Sites de Référence
- [VisuAlgo](https://visualgo.net/) — Visualisation d'algorithmes
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/) — Complexités
- [CP-Algorithms](https://cp-algorithms.com/) — Algorithmes compétitifs

### Chaînes YouTube
- **Abdul Bari** — Excellentes explications théoriques
- **Tushar Roy** — Approche pratique
- **Back To Back SWE** — Interviews et explanations
- **NeetCode** — Solutions LeetCode optimisées

---

## 💼 Application en Contexte Bancaire

### Transactions
```
Array/List        → Historique de transactions
Hash Table        → Lookup rapide par ID
Stack             → Undo/Redo d'opérations
Queue             → File d'attente de traitement
```

### Comptes et Relations
```
Tree              → Hiérarchie de comptes
Graph             → Relations clients/comptes
BFS               → Détection de fraude (graphes)
Union-Find        → Groupes de comptes liés
```

### Analyse et Reporting
```
Sliding Window    → Moyennes mobiles
Prefix Sum        → Sommes cumulatives
Heap              → Top K transactions
Segment Tree      → Requêtes sur périodes
```

### Optimisation
```
Dynamic Prog.     → Optimisation de portefeuille
Greedy            → Allocation de ressources
Backtracking      → Génération de combinaisons
Binary Search     → Recherche de seuils
```

---

## 🎓 Stratégie d'Entretien Technique

### Avant l'Entretien (Préparation)
1. **Pratiquer 150+ problèmes** sur LeetCode (Easy: 50, Medium: 80, Hard: 20)
2. **Maîtriser les patterns** — Two pointers, sliding window, BFS/DFS
3. **Comprendre les complexités** — Toujours analyser O(n)
4. **Coder à la main** — S'exercer sans IDE

### Pendant l'Entretien (Méthodologie)
1. **Clarifier le problème** — Exemples, edge cases, contraintes
2. **Discuter l'approche** — Brute force puis optimisation
3. **Analyser la complexité** — Avant de coder
4. **Coder proprement** — Variables claires, modulaire
5. **Tester avec exemples** — Edge cases, null, vide
6. **Optimiser si possible** — Trade-offs temps/espace

### Checklist Mentale
```
☐ Ai-je compris le problème ?
☐ Ai-je discuté des edge cases ?
☐ Quelle est ma complexité ?
☐ Puis-je faire mieux ?
☐ Mon code compile-t-il ?
☐ Ai-je testé avec des exemples ?
```

---

## 🔧 Templates de Code

### Binary Search Template

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found
```

### BFS Template

```python
from collections import deque

def bfs(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

### DFS Template

```python
def dfs(node, visited):
    if not node or node in visited:
        return
    
    visited.add(node)
    
    # Process node
    process(node)
    
    # Recurse
    for neighbor in node.neighbors:
        dfs(neighbor, visited)
```

### DP Template (Memoization)

```python
def dp_problem(n, memo={}):
    # Base case
    if n <= 1:
        return n
    
    # Check memo
    if n in memo:
        return memo[n]
    
    # Recursive case
    memo[n] = dp_problem(n-1, memo) + dp_problem(n-2, memo)
    
    return memo[n]
```

---

## 🚀 Prochaines Étapes

Après avoir maîtrisé les DSA :

1. **Pratiquez régulièrement** — Au moins 1 problème par jour
2. **Participez à des contests** — LeetCode Weekly, Codeforces
3. **Lisez des solutions** — Apprenez des approches alternatives
4. **Enseignez à d'autres** — Expliquer solidifie la compréhension
5. **Appliquez dans vos projets** — Utilisez les bonnes structures

---

**Dernière mise à jour :** Janvier 2026

**Bon entraînement algorithmique !** 🚀
