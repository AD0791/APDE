# Étude de Cas DSA — Niveau Basique

## Guide de Préparation : Structures et Algorithmes Fondamentaux

---

Ce document regroupe des exercices DSA classiques de niveau débutant, avec solutions en Python et Java. Chaque solution indique l'approche et la complexité.

---

## Problème 1 : Somme de Deux Nombres (Two Sum)

### Énoncé

Étant donné un tableau d'entiers et une cible, retourner les indices de deux nombres dont la somme est égale à la cible.

### Approche

Utiliser une table de hachage pour stocker les valeurs déjà vues.

### Solution Python

```python
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        need = target - n
        if need in seen:
            return [seen[need], i]
        seen[n] = i
    return []
```

### Solution Java

```java
import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int need = target - nums[i];
            if (seen.containsKey(need)) {
                return new int[]{seen.get(need), i};
            }
            seen.put(nums[i], i);
        }
        return new int[]{};
    }
}
```

Complexité: O(n) temps, O(n) espace.

---

## Problème 2 : Parenthèses Valides

### Énoncé

Vérifier si une chaîne contenant (), {}, [] est bien parenthésée.

### Approche

Utiliser une pile pour associer ouvrants/fermants.

### Solution Python

```python
def is_valid(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack
```

### Solution Java

```java
import java.util.ArrayDeque;
import java.util.Deque;

public class ValidParentheses {
    public static boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char ch : s.toCharArray()) {
            if (ch == '(' || ch == '[' || ch == '{') {
                stack.push(ch);
            } else {
                if (stack.isEmpty()) return false;
                char open = stack.pop();
                if ((ch == ')' && open != '(') ||
                    (ch == ']' && open != '[') ||
                    (ch == '}' && open != '{')) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
```

Complexité: O(n) temps, O(n) espace.

---

## Problème 3 : Premier Caractère Unique

### Énoncé

Retourner l'index du premier caractère non répété dans une chaîne.

### Approche

Compter les fréquences, puis relire la chaîne.

### Solution Python

```python
from collections import Counter

def first_unique_char(s):
    counts = Counter(s)
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1
```

### Solution Java

```java
public class FirstUniqueChar {
    public static int firstUniqueChar(String s) {
        int[] count = new int[26];
        for (char ch : s.toCharArray()) {
            count[ch - 'a']++;
        }
        for (int i = 0; i < s.length(); i++) {
            if (count[s.charAt(i) - 'a'] == 1) {
                return i;
            }
        }
        return -1;
    }
}
```

Complexité: O(n) temps, O(1) espace.

---

## Problème 4 : Recherche Binaire

### Énoncé

Trouver l'index d'une cible dans un tableau trié, ou -1 si absent.

### Solution Python

```python
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

### Solution Java

```java
public class BinarySearch {
    public static int search(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return -1;
    }
}
```

Complexité: O(log n) temps, O(1) espace.

---

## Problème 5 : Fusion de Deux Tableaux Triés

### Énoncé

Fusionner deux tableaux triés en un seul tableau trié.

### Solution Python

```python
def merge_sorted(a, b):
    i = j = 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i]); i += 1
        else:
            res.append(b[j]); j += 1
    res.extend(a[i:])
    res.extend(b[j:])
    return res
```

### Solution Java

```java
public class MergeSorted {
    public static int[] merge(int[] a, int[] b) {
        int[] res = new int[a.length + b.length];
        int i = 0, j = 0, k = 0;
        while (i < a.length && j < b.length) {
            if (a[i] <= b[j]) res[k++] = a[i++];
            else res[k++] = b[j++];
        }
        while (i < a.length) res[k++] = a[i++];
        while (j < b.length) res[k++] = b[j++];
        return res;
    }
}
```

Complexité: O(n+m) temps, O(n+m) espace.

---

## Problème 6 : Inverser une Liste Chaînée

### Énoncé

Inverser une liste chaînée simple.

### Solution Python

```python
def reverse_list(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev
```

### Solution Java

```java
public class ReverseList {
    public static ListNode reverse(ListNode head) {
        ListNode prev = null;
        ListNode cur = head;
        while (cur != null) {
            ListNode nxt = cur.next;
            cur.next = prev;
            prev = cur;
            cur = nxt;
        }
        return prev;
    }
}
```

Complexité: O(n) temps, O(1) espace.
