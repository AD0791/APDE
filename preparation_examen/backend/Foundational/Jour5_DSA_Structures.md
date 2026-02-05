# Jour 5 (25 janvier): DSA - Structures de données

**Temps estimé:** 6-7 heures  
**Priorité:** 🟡 HAUTE - Fondamental pour tout développeur

---

## 📖 Définition essentielle

>**Définition DSA (Data Structures & Algorithms)**: Les structures de données sont des **façons d'organiser et de stocker les données** en mémoire pour permettre un accès et une modification efficaces. C'est comme choisir le bon type de rangement (tiroir, étagère, classeur) pour différents types d'objets.

**En résumé**, les structures de données c'est :
- ✅ Organiser les données de façon optimale
- ✅ Choisir la bonne structure pour le bon usage
- ✅ Comprendre les compromis (temps vs espace)
- ✅ Optimiser les performances (accès, recherche, insertion, suppression)

**Pourquoi c'est important ?**
- Un bon choix de structure = application rapide et efficace
- Un mauvais choix = lenteur, gaspillage de mémoire, bugs

**Exemples bancaires :**
- **Stack** pour l'historique d'annulation de transactions
- **Queue** pour la file d'attente de traitement de virements
- **Hash Table** pour rechercher rapidement un compte par son numéro
- **BST** pour maintenir les transactions triées par date

---

## 🎯 Objectif du jour

Maîtriser les **structures de données essentielles** et leurs **complexités temporelles**. Ces structures apparaissent fréquemment dans les examens techniques car elles testent la compréhension algorithmique fondamentale.

---

## 📊 Tableau des complexités temporelles

| Structure | Accès | Recherche | Insertion | Suppression | Espace |
|-----------|-------|-----------|-----------|-------------|--------|
| **Array** | O(1) | O(n) | O(n) | O(n) | O(n) |
| **Stack** | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Queue** | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Linked List** | O(n) | O(n) | O(1)* | O(1)* | O(n) |
| **Hash Table** | N/A | O(1) avg | O(1) avg | O(1) avg | O(n) |
| **Binary Search Tree** | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |

**\* Si position connue**

---

## 📚 1. Stack (Pile) - LIFO (Last In First Out)

### Concept
**Dernier entré, premier sorti** - comme une pile d'assiettes.

### Opérations principales
```
┌─────┐
│  5  │ ← top (sommet)
├─────┤
│  3  │
├─────┤
│  7  │
├─────┤
│  2  │ ← bottom
└─────┘

push(8)  → Ajoute 8 au sommet
pop()    → Retire et retourne 5
peek()   → Retourne 5 sans retirer
isEmpty()→ Retourne false
```

### Implémentation avec array

```java
public class Stack {
    private int[] array;
    private int top;
    private int capacity;
    
    public Stack(int size) {
        array = new int[size];
        capacity = size;
        top = -1;  // Pile vide
    }
    
    // Ajouter un élément - O(1)
    public void push(int x) {
        if (top >= capacity - 1) {
            throw new RuntimeException("Stack Overflow");
        }
        top++;
        array[top] = x;
    }
    
    // Retirer un élément - O(1)
    public int pop() {
        if (top < 0) {
            throw new RuntimeException("Stack Underflow");
        }
        int x = array[top];
        top--;
        return x;
    }
    
    // Voir le sommet - O(1)
    public int peek() {
        if (top < 0) {
            throw new RuntimeException("Stack Empty");
        }
        return array[top];
    }
    
    // Vérifier si vide - O(1)
    public boolean isEmpty() {
        return top < 0;
    }
    
    // Taille actuelle - O(1)
    public int size() {
        return top + 1;
    }
}
```

### Cas d'usage bancaire
- **Annulation de transactions** (undo)
- **Historique de navigation**
- **Évaluation d'expressions** (parenthèses)
- **Pile d'appels de fonctions**

---

## 📚 2. Queue (File) - FIFO (First In First Out)

### Concept
**Premier entré, premier sorti** - comme une file d'attente.

```
Front                      Rear
  ↓                         ↓
┌────┬────┬────┬────┬────┐
│ 12 │ 8  │ 15 │ 7  │ 23 │
└────┴────┴────┴────┴────┘

enqueue(42) → Ajoute 42 à la fin (rear)
dequeue()   → Retire et retourne 12 (front)
peek()      → Retourne 12 sans retirer
```

### Implémentation circulaire

```java
public class Queue {
    private int[] array;
    private int front;
    private int rear;
    private int count;
    private int capacity;
    
    public Queue(int size) {
        array = new int[size];
        capacity = size;
        front = 0;
        rear = -1;
        count = 0;
    }
    
    // Ajouter à la fin - O(1)
    public void enqueue(int x) {
        if (count >= capacity) {
            throw new RuntimeException("Queue Full");
        }
        rear = (rear + 1) % capacity;  // Circulaire!
        array[rear] = x;
        count++;
    }
    
    // Retirer du début - O(1)
    public int dequeue() {
        if (count <= 0) {
            throw new RuntimeException("Queue Empty");
        }
        int x = array[front];
        front = (front + 1) % capacity;  // Circulaire!
        count--;
        return x;
    }
    
    // Voir le premier - O(1)
    public int peek() {
        if (count <= 0) {
            throw new RuntimeException("Queue Empty");
        }
        return array[front];
    }
    
    // Vérifier si vide - O(1)
    public boolean isEmpty() {
        return count == 0;
    }
    
    // Taille actuelle - O(1)
    public int size() {
        return count;
    }
}
```

### Cas d'usage bancaire
- **File d'attente de transactions à traiter**
- **Gestion des requêtes serveur**
- **Buffer de messages**
- **Traitement en lot (batch)**

---

## 🔗 3. Linked List (Liste chaînée)

### Concept
Séquence de nœuds où chaque nœud contient **données + pointeur vers le suivant**.

```
  head
   ↓
┌────┬───┐    ┌────┬───┐    ┌────┬───┐    ┌────┬───┐
│ 5  │ ●─┼───▶│ 12 │ ●─┼───▶│ 8  │ ●─┼───▶│ 3  │ X │
└────┴───┘    └────┴───┘    └────┴───┘    └────┴───┘
```

### Structure du nœud

```java
public class Node {
    int data;
    Node next;
    
    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}
```

### Opérations principales

```java
public class LinkedList {
    private Node head;
    
    // Insertion en tête - O(1)
    public void insertAtHead(int value) {
        Node newNode = new Node(value);
        newNode.next = head;
        head = newNode;
    }
    
    // Insertion en fin - O(n)
    public void insertAtTail(int value) {
        Node newNode = new Node(value);
        
        if (head == null) {
            head = newNode;
            return;
        }
        
        Node current = head;
        while (current.next != null) {
            current = current.next;
        }
        current.next = newNode;
    }
    
    // Recherche - O(n)
    public Node search(int value) {
        Node current = head;
        while (current != null) {
            if (current.data == value) {
                return current;
            }
            current = current.next;
        }
        return null;
    }
    
    // Suppression - O(n)
    public boolean delete(int value) {
        if (head == null) return false;
        
        // Cas spécial: supprimer la tête
        if (head.data == value) {
            head = head.next;
            return true;
        }
        
        Node current = head;
        while (current.next != null) {
            if (current.next.data == value) {
                current.next = current.next.next;
                return true;
            }
            current = current.next;
        }
        return false;
    }
    
    // Afficher - O(n)
    public void display() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }
    
    // Compter les nœuds - O(n)
    public int count() {
        int c = 0;
        Node current = head;
        while (current != null) {
            c++;
            current = current.next;
        }
        return c;
    }
}
```

### Avantages vs Array
- ✅ Insertion/suppression en tête: O(1) vs O(n)
- ✅ Taille dynamique (pas de capacité fixe)
- ❌ Accès par index: O(n) vs O(1)
- ❌ Plus de mémoire (pointeurs)

---

## 🗂️ 4. Hash Table (Table de hachage)

### Concept
Stocke paires **clé-valeur** avec recherche O(1) via fonction de hachage.

```
Clé: "alice" → hash("alice") = 3 → Index 3 dans array

Array interne:
Index 0: null
Index 1: ("bob", 87)
Index 2: null
Index 3: ("alice", 95)
Index 4: ("charlie", 92)
Index 5: null
```

### Fonction de hachage simple

```java
public int hash(String key, int tableSize) {
    int hash = 0;
    for (int i = 0; i < key.length(); i++) {
        hash = (hash + key.charAt(i)) % tableSize;
    }
    return hash;
}
```

### Résolution de collisions

**Collision:** Deux clés différentes donnent le même hash.

#### Méthode 1: Chaînage (Chaining)
```
Index 3: ("alice", 95) → ("david", 88) → null
```

#### Méthode 2: Adressage ouvert (Linear Probing)
```
Index 3 occupé → Essayer index 4, 5, 6... jusqu'à trouver vide
```

### Utilisation en Java

```java
import java.util.HashMap;

HashMap<String, Integer> scores = new HashMap<>();
scores.put("Alice", 95);        // O(1)
int score = scores.get("Alice"); // O(1)
boolean exists = scores.containsKey("Alice"); // O(1)
scores.remove("Alice");         // O(1)
```

### Cas d'usage bancaire
- **Recherche de compte par numéro** (O(1) vs O(n))
- **Cache de transactions récentes**
- **Index de clients par email**

---

## 🌳 5. Binary Search Tree (Arbre binaire de recherche)

### Propriété BST
- Tous les nœuds à **gauche < racine**
- Tous les nœuds à **droite > racine**

```
          15
        /    \
       10     20
      /  \   /  \
     5   12 17  25
```

### Structure du nœud

```java
public class TreeNode {
    int data;
    TreeNode left;
    TreeNode right;
    
    public TreeNode(int data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}
```

### Opérations principales

```java
public class BinarySearchTree {
    private TreeNode root;
    
    // Insertion - O(log n) moyen, O(n) pire
    public TreeNode insert(TreeNode root, int value) {
        if (root == null) {
            return new TreeNode(value);
        }
        
        if (value < root.data) {
            root.left = insert(root.left, value);
        } else if (value > root.data) {
            root.right = insert(root.right, value);
        }
        
        return root;
    }
    
    // Recherche - O(log n) moyen, O(n) pire
    public TreeNode search(TreeNode root, int value) {
        if (root == null || root.data == value) {
            return root;
        }
        
        if (value < root.data) {
            return search(root.left, value);
        }
        return search(root.right, value);
    }
    
    // Minimum - O(log n)
    public TreeNode findMin(TreeNode root) {
        while (root.left != null) {
            root = root.left;
        }
        return root;
    }
    
    // Maximum - O(log n)
    public TreeNode findMax(TreeNode root) {
        while (root.right != null) {
            root = root.right;
        }
        return root;
    }
}
```

### Traversées d'arbres

#### Inorder (Gauche-Racine-Droite) - Donne ordre trié!
```java
public void inorder(TreeNode node) {
    if (node == null) return;
    inorder(node.left);
    System.out.print(node.data + " ");
    inorder(node.right);
}
// Pour l'arbre ci-dessus: 5, 10, 12, 15, 17, 20, 25
```

#### Preorder (Racine-Gauche-Droite) - Pour copier l'arbre
```java
public void preorder(TreeNode node) {
    if (node == null) return;
    System.out.print(node.data + " ");
    preorder(node.left);
    preorder(node.right);
}
// Pour l'arbre ci-dessus: 15, 10, 5, 12, 20, 17, 25
```

#### Postorder (Gauche-Droite-Racine) - Pour supprimer l'arbre
```java
public void postorder(TreeNode node) {
    if (node == null) return;
    postorder(node.left);
    postorder(node.right);
    System.out.print(node.data + " ");
}
// Pour l'arbre ci-dessus: 5, 12, 10, 17, 25, 20, 15
```

### Mnémonique traversées
- **IN**order = **IN**térieur d'abord (gauche-racine-droite) → **Ordre trié**
- **PRE**order = **PRE**fixe (racine en premier)
- **POST**order = **POST**pone racine (racine à la fin)

---

## 📝 Exercices pratiques Jour 5

### Exercice 1: Stack
**Sur papier, implémenter:**
1. Push, pop, peek, isEmpty
2. Trace d'exécution pour: push(5), push(3), pop(), push(7), peek(), pop()

### Exercice 2: Queue circulaire
**Sur papier, implémenter:**
1. Enqueue, dequeue avec indices circulaires
2. Dessiner l'état après: enqueue(5), enqueue(3), dequeue(), enqueue(7)

### Exercice 3: Linked List
**Sur papier, implémenter:**
1. InsertAtHead, search, delete
2. Dessiner la liste après: insert(5), insert(3), insert(7), delete(3)

### Exercice 4: BST
**Sur papier:**
1. Dessiner le BST après insertion de: 15, 10, 20, 5, 12, 25, 17
2. Écrire le résultat des 3 traversées (inorder, preorder, postorder)

---

## 🔎 Extension: Compréhension & Rétention (Jour 5)

### 1) Mini-récap (quand utiliser quoi)
- **Stack:** historique/undo
- **Queue:** file d'attente, BFS
- **HashMap:** accès rapide clé → valeur
- **BST:** données triées + recherche log

### 2) Exemples Python rapides

**Stack**
```python
stack = []
stack.append(5)
stack.pop()
```

**Queue**
```python
from collections import deque
q = deque()
q.append(5)
q.popleft()
```

**HashMap**
```python
freq = {}
freq["a"] = freq.get("a", 0) + 1
```

### 3) Questions type examen
- Pourquoi une HashMap peut tomber à O(n) dans le pire cas?
- Différence Array vs LinkedList
- Quand préférer un BST à un tableau trié?

---

## ✅ Checklist de révision Jour 5

- [ ] Implémenter Stack avec push/pop/peek
- [ ] Implémenter Queue circulaire
- [ ] Implémenter LinkedList insertion/recherche/suppression
- [ ] Comprendre résolution de collisions (chaînage vs probing)
- [ ] Implémenter BST insertion/recherche
- [ ] Écrire les 3 traversées d'arbre (inorder, preorder, postorder)
- [ ] Connaître les complexités de chaque structure
- [ ] Savoir quand utiliser quelle structure

---

**💡 Conseil:** Pratiquez sur papier! Dessinez les états intermédiaires des structures après chaque opération. Cela vous aidera à visualiser et à détecter les erreurs.

**Prochain document:** `Jour6_DSA_Algorithmes.md` - Algorithmes de tri et recherche
