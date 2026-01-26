# Étude de Cas DSA — Niveau Moyen

## Guide de Préparation : Hashing, Two Pointers, Arbres

---

Ce document intermédiaire propose des exercices typiques d'entretiens pour tester les structures de données et les algorithmes optimisés.

---

## Problème 1 : Sous-tableau de Somme K

### Énoncé

Étant donné un tableau d'entiers, retourner le nombre de sous-tableaux dont la somme vaut K.

### Approche

Utiliser un dictionnaire de préfixes.

### Solution Python

```python
from collections import defaultdict

def subarray_sum(nums, k):
    count = 0
    prefix = 0
    freq = defaultdict(int)
    freq[0] = 1
    for n in nums:
        prefix += n
        count += freq[prefix - k]
        freq[prefix] += 1
    return count
```

### Solution Java

```java
import java.util.HashMap;
import java.util.Map;

public class SubarraySum {
    public static int subarraySum(int[] nums, int k) {
        int count = 0;
        int prefix = 0;
        Map<Integer, Integer> freq = new HashMap<>();
        freq.put(0, 1);
        for (int n : nums) {
            prefix += n;
            count += freq.getOrDefault(prefix - k, 0);
            freq.put(prefix, freq.getOrDefault(prefix, 0) + 1);
        }
        return count;
    }
}
```

Complexité: O(n) temps, O(n) espace.

---

## Problème 2 : Fenêtre Glissante (Max dans chaque fenêtre)

### Énoncé

Donner le maximum de chaque fenêtre de taille k.

### Approche

Deque monotone pour garder les indices utiles.

### Solution Python

```python
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()
    result = []
    for i, n in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= n:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

### Solution Java

```java
import java.util.ArrayDeque;
import java.util.Deque;

public class SlidingWindowMax {
    public static int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> dq = new ArrayDeque<>();
        int[] res = new int[nums.length - k + 1];
        int idx = 0;
        for (int i = 0; i < nums.length; i++) {
            while (!dq.isEmpty() && dq.peekFirst() <= i - k) dq.pollFirst();
            while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) dq.pollLast();
            dq.addLast(i);
            if (i >= k - 1) res[idx++] = nums[dq.peekFirst()];
        }
        return res;
    }
}
```

Complexité: O(n) temps, O(n) espace.

---

## Problème 3 : Traversée d'Arbre Binaire (Level Order)

### Énoncé

Retourner les valeurs des nœuds niveau par niveau.

### Approche

BFS avec une file.

### Solution Python

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    res, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res
```

### Solution Java

```java
import java.util.*;

public class LevelOrderTraversal {
    public static List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            int size = q.size();
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                level.add(node.val);
                if (node.left != null) q.add(node.left);
                if (node.right != null) q.add(node.right);
            }
            res.add(level);
        }
        return res;
    }
}
```

Complexité: O(n) temps, O(n) espace.

---

## Problème 4 : Longest Substring Sans Répétition

### Énoncé

Trouver la longueur de la plus longue sous-chaîne sans caractères répétés.

### Approche

Fenêtre glissante avec positions des caractères.

### Solution Python

```python
def length_of_longest_substring(s):
    last = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        best = max(best, right - left + 1)
    return best
```

### Solution Java

```java
import java.util.HashMap;
import java.util.Map;

public class LongestSubstring {
    public static int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> last = new HashMap<>();
        int left = 0, best = 0;
        for (int right = 0; right < s.length(); right++) {
            char ch = s.charAt(right);
            if (last.containsKey(ch) && last.get(ch) >= left) {
                left = last.get(ch) + 1;
            }
            last.put(ch, right);
            best = Math.max(best, right - left + 1);
        }
        return best;
    }
}
```

Complexité: O(n) temps, O(k) espace.

---

## Problème 5 : Top K Fréquences

### Énoncé

Retourner les k éléments les plus fréquents d'un tableau.

### Approche

HashMap + heap.

### Solution Python

```python
import heapq
from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)
    return [n for n, _ in heapq.nlargest(k, count.items(), key=lambda x: x[1])]
```

### Solution Java

```java
import java.util.*;

public class TopKFrequent {
    public static int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int n : nums) freq.put(n, freq.getOrDefault(n, 0) + 1);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> b[1] - a[1]);
        for (Map.Entry<Integer, Integer> e : freq.entrySet()) {
            pq.add(new int[]{e.getKey(), e.getValue()});
        }
        int[] res = new int[k];
        for (int i = 0; i < k; i++) res[i] = pq.poll()[0];
        return res;
    }
}
```

Complexité: O(n log n) temps, O(n) espace.

---

## Problème 6 : Valider un BST

### Énoncé

Vérifier si un arbre binaire est un BST valide.

### Solution Python

```python
def is_valid_bst(root):
    def dfs(node, lo, hi):
        if not node:
            return True
        if not (lo < node.val < hi):
            return False
        return dfs(node.left, lo, node.val) and dfs(node.right, node.val, hi)
    return dfs(root, float('-inf'), float('inf'))
```

### Solution Java

```java
public class ValidateBST {
    public static boolean isValidBST(TreeNode root) {
        return dfs(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private static boolean dfs(TreeNode node, long lo, long hi) {
        if (node == null) return true;
        if (node.val <= lo || node.val >= hi) return false;
        return dfs(node.left, lo, node.val) && dfs(node.right, node.val, hi);
    }
}
```

Complexité: O(n) temps, O(h) espace.
