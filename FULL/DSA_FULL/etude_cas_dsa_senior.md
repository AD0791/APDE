# Étude de Cas DSA — Niveau Senior

## Guide de Préparation : Graphes, DP, Optimisation

---

Ces exercices avancés exigent des choix algorithmiques solides et une analyse de complexité rigoureuse.

---

## Problème 1 : Plus Court Chemin (Dijkstra)

### Énoncé

Étant donné un graphe pondéré sans poids négatifs, trouver la distance minimale entre une source et toutes les autres.

### Approche

Utiliser Dijkstra avec une file de priorité.

### Solution Python

```python
import heapq

def dijkstra(n, edges, src):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    dist = [float('inf')] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

### Solution Java

```java
import java.util.*;

public class Dijkstra {
    static class Edge {
        int to, w;
        Edge(int to, int w) { this.to = to; this.w = w; }
    }

    public static int[] dijkstra(int n, List<int[]> edges, int src) {
        List<List<Edge>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for (int[] e : edges) {
            int u = e[0], v = e[1], w = e[2];
            graph.get(u).add(new Edge(v, w));
            graph.get(v).add(new Edge(u, w));
        }
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[src] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.add(new int[]{0, src});
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int d = cur[0], u = cur[1];
            if (d != dist[u]) continue;
            for (Edge ed : graph.get(u)) {
                int nd = d + ed.w;
                if (nd < dist[ed.to]) {
                    dist[ed.to] = nd;
                    pq.add(new int[]{nd, ed.to});
                }
            }
        }
        return dist;
    }
}
```

Complexité: O((V+E) log V).

---

## Problème 2 : Programmation Dynamique (Coin Change)

### Énoncé

Donner le nombre minimal de pièces pour atteindre un montant donné.

### Approche

DP bottom-up.

### Solution Python

```python
def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return -1 if dp[amount] == amount + 1 else dp[amount]
```

### Solution Java

```java
import java.util.Arrays;

public class CoinChange {
    public static int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;
        for (int a = 1; a <= amount; a++) {
            for (int c : coins) {
                if (a - c >= 0) {
                    dp[a] = Math.min(dp[a], dp[a - c] + 1);
                }
            }
        }
        return dp[amount] == amount + 1 ? -1 : dp[amount];
    }
}
```

Complexité: O(amount * n).

---

## Problème 3 : Détection de Cycle dans un Graphe Orienté

### Énoncé

Déterminer s'il existe un cycle dans un graphe orienté.

### Approche

DFS avec état (0=non visité, 1=en cours, 2=terminé).

### Solution Python

```python
def has_cycle(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
    state = [0] * n

    def dfs(u):
        state[u] = 1
        for v in graph[u]:
            if state[v] == 1:
                return True
            if state[v] == 0 and dfs(v):
                return True
        state[u] = 2
        return False

    for i in range(n):
        if state[i] == 0 and dfs(i):
            return True
    return False
```

### Solution Java

```java
import java.util.*;

public class CycleDirectedGraph {
    public static boolean hasCycle(int n, List<int[]> edges) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for (int[] e : edges) graph.get(e[0]).add(e[1]);
        int[] state = new int[n];

        for (int i = 0; i < n; i++) {
            if (state[i] == 0 && dfs(i, graph, state)) return true;
        }
        return false;
    }

    private static boolean dfs(int u, List<List<Integer>> graph, int[] state) {
        state[u] = 1;
        for (int v : graph.get(u)) {
            if (state[v] == 1) return true;
            if (state[v] == 0 && dfs(v, graph, state)) return true;
        }
        state[u] = 2;
        return false;
    }
}
```

Complexité: O(V+E).

---

## Problème 4 : Tri Topologique

### Énoncé

Ordonner les tâches d'un DAG selon les dépendances.

### Approche

Kahn (in-degrees).

### Solution Python

```python
from collections import deque

def topo_sort(n, edges):
    graph = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        graph[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []
```

### Solution Java

```java
import java.util.*;

public class TopoSort {
    public static List<Integer> topoSort(int n, List<int[]> edges) {
        List<List<Integer>> graph = new ArrayList<>();
        int[] indeg = new int[n];
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for (int[] e : edges) {
            graph.get(e[0]).add(e[1]);
            indeg[e[1]]++;
        }
        Deque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < n; i++) if (indeg[i] == 0) q.add(i);
        List<Integer> order = new ArrayList<>();
        while (!q.isEmpty()) {
            int u = q.poll();
            order.add(u);
            for (int v : graph.get(u)) {
                indeg[v]--;
                if (indeg[v] == 0) q.add(v);
            }
        }
        return order.size() == n ? order : Collections.emptyList();
    }
}
```

Complexité: O(V+E).

---

## Problème 5 : Union-Find (Détection de Cycle Non Orienté)

### Énoncé

Détecter s'il existe un cycle dans un graphe non orienté.

### Solution Python

```python
def has_cycle_undirected(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            parent[ra] = rb
        elif rank[ra] > rank[rb]:
            parent[rb] = ra
        else:
            parent[rb] = ra
            rank[ra] += 1
        return True

    for u, v in edges:
        if not union(u, v):
            return True
    return False
```

### Solution Java

```java
public class UnionFindCycle {
    private static int find(int[] parent, int x) {
        if (parent[x] != x) parent[x] = find(parent, parent[x]);
        return parent[x];
    }

    private static boolean union(int[] parent, int[] rank, int a, int b) {
        int ra = find(parent, a), rb = find(parent, b);
        if (ra == rb) return false;
        if (rank[ra] < rank[rb]) parent[ra] = rb;
        else if (rank[ra] > rank[rb]) parent[rb] = ra;
        else { parent[rb] = ra; rank[ra]++; }
        return true;
    }

    public static boolean hasCycle(int n, int[][] edges) {
        int[] parent = new int[n];
        int[] rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        for (int[] e : edges) {
            if (!union(parent, rank, e[0], e[1])) return true;
        }
        return false;
    }
}
```

Complexité: O(E * alpha(V)).

---

## Problème 6 : Interval Scheduling (Greedy)

### Énoncé

Sélectionner le maximum d'intervalles non chevauchants.

### Solution Python

```python
def max_non_overlapping(intervals):
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = float('-inf')
    for s, e in intervals:
        if s >= end:
            count += 1
            end = e
    return count
```

### Solution Java

```java
import java.util.*;

public class IntervalScheduling {
    public static int maxNonOverlapping(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[1]));
        int count = 0;
        int end = Integer.MIN_VALUE;
        for (int[] in : intervals) {
            if (in[0] >= end) {
                count++;
                end = in[1];
            }
        }
        return count;
    }
}
```

Complexité: O(n log n).
