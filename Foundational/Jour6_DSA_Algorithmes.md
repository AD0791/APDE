# Jour 6 (26 janvier): DSA - Algorithmes

**Temps estimé:** 5-6 heures  
**Priorité:** 🟡 HAUTE - Algorithmes classiques très fréquents

---

## 🎯 Objectif du jour

Maîtriser les **algorithmes fondamentaux** de recherche, tri et parcours de graphes avec leurs **complexités**. Ces algorithmes sont testés régulièrement car ils révèlent la capacité d'analyse algorithmique.

---

## 🔍 1. Binary Search (Recherche binaire)

### Principe
Diviser l'espace de recherche par 2 à chaque itération.  
**PRÉREQUIS:** Tableau TRIÉ

```
Array: [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
Recherche: 23

Étape 1: mid = 16 → 23 > 16 → chercher à droite
Étape 2: mid = 56 → 23 < 56 → chercher à gauche
Étape 3: mid = 23 → Trouvé!
```

### Implémentation

```java
public int binarySearch(int[] arr, int target) {
    int low = 0;
    int high = arr.length - 1;
    
    while (low <= high) {
        // Éviter overflow: mid = (low + high) / 2
        int mid = low + (high - low) / 2;
        
        if (arr[mid] == target) {
            return mid;  // Trouvé!
        } else if (arr[mid] < target) {
            low = mid + 1;  // Chercher à droite
        } else {
            high = mid - 1;  // Chercher à gauche
        }
    }
    
    return -1;  // Non trouvé
}
```

**Complexité:**
- Temps: **O(log n)** - Divise par 2 à chaque étape
- Espace: **O(1)** - Variables constantes

### Exemple de trace
```
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91], target = 23

Itération 1:
  low=0, high=9, mid=4
  arr[4]=16 < 23 → low=5

Itération 2:
  low=5, high=9, mid=7
  arr[7]=56 > 23 → high=6

Itération 3:
  low=5, high=6, mid=5
  arr[5]=23 == 23 → Retourner 5
```

---

## 📊 2. Algorithmes de tri

### Tableau comparatif

| Algorithme | Meilleur | Moyen | Pire | Espace | Stable? |
|------------|----------|-------|------|--------|---------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | Oui |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | Non |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Oui |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Oui |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | Non |

**Tri stable:** Préserve l'ordre relatif des éléments égaux.

### A. Bubble Sort (Tri à bulles)

**Principe:** Parcourir répétitivement, échanger éléments adjacents mal ordonnés.

```java
public void bubbleSort(int[] arr) {
    int n = arr.length;
    
    for (int i = 0; i < n - 1; i++) {
        boolean swapped = false;
        
        // Derniers i éléments déjà triés
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Échanger
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = true;
            }
        }
        
        // Optimisation: si aucun échange, déjà trié
        if (!swapped) break;
    }
}
```

**Trace d'exécution:**
```
Initial: [5, 2, 8, 1, 9]

Pass 1: [2, 5, 1, 8, 9]  (9 en place)
Pass 2: [2, 1, 5, 8, 9]  (8 en place)
Pass 3: [1, 2, 5, 8, 9]  (5 en place)
Pass 4: [1, 2, 5, 8, 9]  (Déjà trié, stop)
```

**Complexité:**
- Temps: **O(n²)** moyen/pire, **O(n)** meilleur (déjà trié)
- Espace: **O(1)**

### B. Selection Sort (Tri par sélection)

**Principe:** Trouver le minimum, le placer au début, répéter.

```java
public void selectionSort(int[] arr) {
    int n = arr.length;
    
    for (int i = 0; i < n - 1; i++) {
        // Trouver index du minimum dans arr[i..n-1]
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        
        // Échanger arr[i] et arr[minIndex]
        int temp = arr[i];
        arr[i] = arr[minIndex];
        arr[minIndex] = temp;
    }
}
```

**Complexité:**
- Temps: **O(n²)** toujours
- Espace: **O(1)**

### C. Insertion Sort (Tri par insertion)

**Principe:** Comme trier des cartes à jouer - insérer chaque élément à sa place.

```java
public void insertionSort(int[] arr) {
    int n = arr.length;
    
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        
        // Décaler les éléments > key vers la droite
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        
        // Insérer key à sa position
        arr[j + 1] = key;
    }
}
```

**Complexité:**
- Temps: **O(n²)** moyen/pire, **O(n)** meilleur (presque trié)
- Espace: **O(1)**
- **Efficace pour petits tableaux ou presque triés**

### D. Quick Sort (Tri rapide)

**Principe:** Diviser pour régner - choisir un pivot, partitionner, trier récursivement.

```java
public void quickSort(int[] arr, int low, int high) {
    if (low < high) {
        // Partitionner et obtenir index du pivot
        int pivotIndex = partition(arr, low, high);
        
        // Trier récursivement les deux moitiés
        quickSort(arr, low, pivotIndex - 1);
        quickSort(arr, pivotIndex + 1, high);
    }
}

public int partition(int[] arr, int low, int high) {
    // Choisir le dernier élément comme pivot
    int pivot = arr[high];
    int i = low - 1;  // Index du plus petit élément
    
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            // Échanger arr[i] et arr[j]
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    
    // Placer le pivot à sa position finale
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;
    
    return i + 1;
}

// Appel initial: quickSort(arr, 0, arr.length - 1);
```

**Trace de partition:**
```
arr = [5, 2, 8, 1, 9], pivot = 9

Après partition: [5, 2, 8, 1, 9]  (pivot déjà en place)
                              ↑ pivot index = 4

Récursion gauche: quickSort([5, 2, 8, 1])
Récursion droite: quickSort([]) (vide)
```

**Complexité:**
- Temps: **O(n log n)** moyen, **O(n²)** pire (pivot mal choisi)
- Espace: **O(log n)** (pile de récursion)
- **Très efficace en pratique**

### E. Merge Sort (Tri fusion)

**Principe:** Diviser pour régner - diviser en deux, trier récursivement, fusionner.

```java
public void mergeSort(int[] arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        
        // Trier les deux moitiés
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        
        // Fusionner les moitiés triées
        merge(arr, left, mid, right);
    }
}

public void merge(int[] arr, int left, int mid, int right) {
    // Tailles des sous-tableaux
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    // Tableaux temporaires
    int[] L = new int[n1];
    int[] R = new int[n2];
    
    // Copier les données
    for (int i = 0; i < n1; i++) {
        L[i] = arr[left + i];
    }
    for (int j = 0; j < n2; j++) {
        R[j] = arr[mid + 1 + j];
    }
    
    // Fusionner
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    
    // Copier les éléments restants
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

// Appel initial: mergeSort(arr, 0, arr.length - 1);
```

**Complexité:**
- Temps: **O(n log n)** toujours
- Espace: **O(n)** (tableaux temporaires)
- **Stable et prévisible**

---

## 🗺️ 3. Parcours de graphes

### Représentation d'un graphe

```
    1 ─── 2
    │     │
    │     │
    3 ─── 4 ─── 5

Liste d'adjacence:
1: [2, 3]
2: [1, 4]
3: [1, 4]
4: [2, 3, 5]
5: [4]
```

### A. BFS (Breadth-First Search) - Parcours en largeur

**Principe:** Explorer niveau par niveau - utilise une **Queue**.

```java
import java.util.*;

public void BFS(Map<Integer, List<Integer>> graph, int start) {
    Set<Integer> visited = new HashSet<>();
    Queue<Integer> queue = new LinkedList<>();
    
    visited.add(start);
    queue.add(start);
    
    while (!queue.isEmpty()) {
        int node = queue.poll();
        System.out.print(node + " ");
        
        // Visiter tous les voisins
        for (int neighbor : graph.get(node)) {
            if (!visited.contains(neighbor)) {
                visited.add(neighbor);
                queue.add(neighbor);
            }
        }
    }
}
```

**Ordre de visite depuis 1:** 1, 2, 3, 4, 5

**Complexité:**
- Temps: **O(V + E)** où V = sommets, E = arêtes
- Espace: **O(V)** (queue + visited)

**Usage:** Plus court chemin (non pondéré), niveau par niveau

### B. DFS (Depth-First Search) - Parcours en profondeur

**Principe:** Explorer en profondeur d'abord - utilise une **Stack** (récursion).

```java
public void DFS(Map<Integer, List<Integer>> graph, int node, Set<Integer> visited) {
    visited.add(node);
    System.out.print(node + " ");
    
    for (int neighbor : graph.get(node)) {
        if (!visited.contains(neighbor)) {
            DFS(graph, neighbor, visited);
        }
    }
}

// Appel initial: 
// Set<Integer> visited = new HashSet<>();
// DFS(graph, 1, visited);
```

**Ordre de visite depuis 1:** 1, 2, 4, 3, 5 (dépend de l'ordre des voisins)

**Complexité:**
- Temps: **O(V + E)**
- Espace: **O(V)** (pile de récursion)

**Usage:** Détection de cycles, tri topologique, composantes connexes

### Mnémonique BFS vs DFS

- **B**FS = **B**roader first = **Queue** = Niveau par niveau
- **D**FS = **D**eeper first = **Stack**/Récursion = Explorer en profondeur

---

## 📝 Exercices pratiques Jour 6

### Exercice 1: Binary Search
**Sur papier:**
1. Tracer binary search pour chercher 38 dans [2, 5, 8, 12, 16, 23, 38, 56, 72]
2. Écrire le code de mémoire

### Exercice 2: Tri
**Sur papier:**
1. Tracer bubble sort pour [5, 2, 8, 1, 9]
2. Tracer partition de quick sort pour [5, 2, 8, 1, 9] avec pivot = 9
3. Comparer les complexités de bubble, quick et merge sort

### Exercice 3: Graphes
**Sur papier:**
1. Dessiner le graphe: 1-2, 1-3, 2-4, 3-4, 4-5
2. Tracer BFS depuis le sommet 1
3. Tracer DFS depuis le sommet 1
4. Comparer les ordres de visite

---

## 🔎 Extension: Version Python (raccourcis)

**Binary Search**
```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target: return mid
        if arr[mid] < target: lo = mid + 1
        else: hi = mid - 1
    return -1
```

**BFS**
```python
from collections import deque
def bfs(graph, start):
    q = deque([start]); seen = {start}
    while q:
        u = q.popleft()
        for v in graph[u]:
            if v not in seen:
                seen.add(v); q.append(v)
```

**DFS**
```python
def dfs(graph, u, seen):
    seen.add(u)
    for v in graph[u]:
        if v not in seen:
            dfs(graph, v, seen)
```

---

## ⚠️ Pièges algorithmes à éviter en examen

| Piège | Erreur | Correction |
|-------|--------|------------|
| **Off-by-one** | `for (i = 0; i <= n)` | `for (i = 0; i < n)` |
| **Integer overflow** | `mid = (low + high) / 2` | `mid = low + (high - low) / 2` |
| **Boucles infinies** | Oublier `low++` ou `high--` | Toujours mettre à jour les variables |
| **Cas de base récursion** | Pas de condition d'arrêt | Toujours vérifier `if (base case)` |
| **Tableau vide** | Ne pas tester `arr.length == 0` | Ajouter cas limites |

---

## ✅ Checklist de révision Jour 6

- [ ] Implémenter binary search de mémoire
- [ ] Tracer bubble sort avec un exemple
- [ ] Implémenter partition de quick sort
- [ ] Connaître les complexités de chaque tri
- [ ] Différencier tri stable vs instable
- [ ] Implémenter BFS avec Queue
- [ ] Implémenter DFS avec récursion
- [ ] Savoir quand utiliser BFS vs DFS
- [ ] Éviter integer overflow dans binary search
- [ ] Traiter les cas limites (tableau vide, un élément)

---

**💡 Conseil:** Pratiquez sur papier! Tracez l'exécution étape par étape pour bien comprendre le déroulement. C'est exactement ce qu'on vous demandera à l'examen.

**Prochain document:** `Jour7_Backend_Network_Frontend.md` - Technologies web complètes
