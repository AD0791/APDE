# Fiches de Synthèse - Mémos Ultra-Rapides

**Usage:** Relecture finale avant l'examen (15-30 minutes)

---

## 📖 DÉFINITIONS EXPRESS (À CONNAÎTRE PAR CŒUR)

### 🗄️ Base de données
Un système organisé pour stocker, gérer et récupérer des données de manière structurée, fiable et efficace. Garantit l'intégrité via ACID.

### 💾 POO (Programmation Orientée Objet)
Paradigme qui organise le code en objets (instances de classes) contenant données (attributs) et comportements (méthodes). 4 piliers : Encapsulation, Abstraction, Héritage, Polymorphisme.

### 🏗️ SOLID
5 principes de conception OOP pour un code maintenable et évolutif : Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion.

### 📦 DSA (Data Structures & Algorithms)
Structures de données = façons d'organiser les données (Array, Stack, Queue, Hash Table, Tree). Algorithmes = séquences d'instructions pour résoudre un problème (recherche, tri, parcours).

### 📐 UML (Unified Modeling Language)
Langage de modélisation graphique standardisé pour visualiser, spécifier et documenter les systèmes logiciels via des diagrammes (classes, cas d'utilisation, séquence).

### 🌐 Backend
Partie serveur d'une application gérant la logique métier, les données et les API. Invisible pour l'utilisateur mais essentiel pour le traitement.

### 🔌 Networking
Ensemble des protocoles et technologies permettant la communication entre systèmes (TCP/IP, HTTP, OSI). Transport des données sur les réseaux.

### 💻 Frontend
Partie client d'une application avec laquelle l'utilisateur interagit directement : HTML (structure), CSS (style), JavaScript (comportement).

### 🔐 ACID
Propriétés garantissant la fiabilité des transactions en base de données : Atomicity (tout ou rien), Consistency (états valides), Isolation (indépendance), Durability (persistance).

### 🛡️ XSS (Cross-Site Scripting)
Attaque par injection de scripts malveillants. Prévention : utiliser textContent, échapper entrées, CSP, HttpOnly cookies.

### 🔒 CSRF (Cross-Site Request Forgery)
Attaque trompant un utilisateur authentifié pour exécuter une action. Prévention : token CSRF, SameSite cookies, vérifier Origin.

---

## 🗄️ FICHE 1: ACID (Bases de données)

| Propriété | Définition courte | Exemple |
|-----------|-------------------|---------|
| **A**tomicity | Tout ou rien | Virement: débit ET crédit, pas l'un sans l'autre |
| **C**onsistency | États valides uniquement | Solde ne peut pas être négatif (contrainte respectée) |
| **I**solation | Transactions indépendantes | 2 retraits simultanés ne causent pas d'erreur |
| **D**urability | Changements permanents | Après COMMIT, survit à une panne |

**Transaction SQL:**
```sql
BEGIN TRANSACTION;
UPDATE comptes SET solde = solde - 500 WHERE compte_id = 1;
UPDATE comptes SET solde = solde + 500 WHERE compte_id = 2;
COMMIT;  -- ou ROLLBACK
```

---

## 🏗️ FICHE 2: SOLID (Principes POO)

| Principe | Phrase clé | Violation | Solution |
|----------|-----------|-----------|----------|
| **S**ingle Responsibility | Une raison de changer | Classe fait tout | Séparer responsabilités |
| **O**pen/Closed | Ouvert extension, fermé modification | Modifier classe pour ajouter | Interfaces/abstraction |
| **L**iskov Substitution | Sous-classes substituables | Carré extends Rectangle | Abstraction correcte |
| **I**nterface Segregation | Pas de méthodes inutiles | Interface trop large | Interfaces petites/spécifiques |
| **D**ependency Inversion | Dépendre d'abstractions | Dépend de MySQL directement | Dépendre d'interface DB |

**Mnémonique:** **S**olid **O**bjects **L**ove **I**nterfaces and **D**ependencies

---

## ⚡ FICHE 3: Complexités Big O

| Notation | Nom | Exemple | Vitesse |
|----------|-----|---------|---------|
| **O(1)** | Constante | Accès array[i], push/pop stack | Très rapide |
| **O(log n)** | Logarithmique | Binary search, BST équilibré | Rapide |
| **O(n)** | Linéaire | Parcourir array, recherche linéaire | Moyen |
| **O(n log n)** | Linéarithmique | Quick sort, merge sort | Acceptable |
| **O(n²)** | Quadratique | Bubble sort, nested loops | Lent |

**Règles:**
- Supprimer constantes: O(2n) → O(n)
- Garder le pire: O(n² + n) → O(n²)
- Multiplication de boucles: 2 boucles imbriquées = O(n²)

---

## 🌐 FICHE 4: HTTP - Méthodes et Codes

### Méthodes
| Méthode | Action | Idempotent? |
|---------|--------|-------------|
| GET | Lire | Oui |
| POST | Créer | Non |
| PUT | Remplacer | Oui |
| DELETE | Supprimer | Oui |

### Codes de statut
| Code | Signification | Usage |
|------|---------------|-------|
| **200** | OK | GET/PUT/PATCH réussi |
| **201** | Created | POST réussi |
| **204** | No Content | DELETE réussi |
| **400** | Bad Request | Données invalides |
| **401** | Unauthorized | Pas authentifié |
| **403** | Forbidden | Pas autorisé |
| **404** | Not Found | Ressource inexistante |
| **500** | Internal Error | Erreur serveur |

**Mnémonique:**
- **2xx** = **Success** 🎉
- **4xx** = **Client** error (tu as merdé) 🤦
- **5xx** = **Server** error (serveur a merdé) 💥

---

## 🔌 FICHE 5: TCP vs UDP

| | TCP | UDP |
|-|-----|-----|
| **Connexion** | Oui (3-way handshake) | Non |
| **Fiabilité** | Garantie | Pas de garantie |
| **Ordre** | Maintenu | Non maintenu |
| **Vitesse** | Plus lent | Plus rapide |
| **Usage** | Web, email, fichiers | Streaming, VoIP, DNS |

**TCP 3-Way Handshake:**
1. Client → Serveur: **SYN**
2. Serveur → Client: **SYN-ACK**
3. Client → Serveur: **ACK**

**Mnémonique:** **T**rust **C**onnection **P**erfectly vs **U**nreliable **D**ata **P**ackets

---

## 🎨 FICHE 6: OSI 7 Couches

| # | Couche | Fonction | Protocoles |
|---|--------|----------|------------|
| **7** | Application | Interface utilisateur | HTTP, FTP, SMTP, DNS |
| **6** | Présentation | Format, encryption | SSL/TLS, JPEG |
| **5** | Session | Gestion sessions | NetBIOS |
| **4** | Transport | Livraison E2E | TCP, UDP |
| **3** | Réseau | Routage | IP |
| **2** | Liaison | Adressage MAC | Ethernet |
| **1** | Physique | Bits | Câbles |

**Mnémonique:** **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way

---

## 📦 FICHE 7: CSS Box Model

```
┌────── margin ──────┐
│ ┌──── border ────┐ │
│ │ ┌─ padding ─┐ │ │
│ │ │  CONTENT  │ │ │
│ │ └───────────┘ │ │
│ └───────────────┘ │
└───────────────────┘
```

**Largeur totale = margin + border + padding + width + padding + border + margin**

**box-sizing: border-box** → width inclut padding et border (recommandé!)

---

## 🔐 FICHE 8: Sécurité Frontend

### XSS (Cross-Site Scripting)
- **Attaque:** Injection de script malveillant
- **Prévention:**
  - ✅ Utiliser `textContent` au lieu de `innerHTML`
  - ✅ Échapper les entrées utilisateur
  - ✅ Content Security Policy (CSP)
  - ✅ HttpOnly cookies

### CSRF (Cross-Site Request Forgery)
- **Attaque:** Utilisateur trompé pour exécuter action
- **Prévention:**
  - ✅ Token CSRF dans chaque requête
  - ✅ SameSite cookies
  - ✅ Vérifier Origin/Referer

---

## 🔍 FICHE 9: Structures de données

| Structure | Accès | Recherche | Insertion | Usage |
|-----------|-------|-----------|-----------|-------|
| **Array** | O(1) | O(n) | O(n) | Accès direct |
| **Stack** | O(n) | O(n) | O(1) | LIFO (undo) |
| **Queue** | O(n) | O(n) | O(1) | FIFO (file) |
| **Hash Table** | N/A | O(1) | O(1) | Recherche rapide |
| **BST** | O(log n) | O(log n) | O(log n) | Données triées |

**Mnémoniques:**
- **Stack** = **S**tack of plates (pile d'assiettes)
- **Queue** = **Q**ueue at bank (file à la banque)

---

## 🎯 FICHE 10: UML Relations

| Relation | Symbole | Signification |
|----------|---------|---------------|
| Association | ——— | "utilise" |
| Agrégation | ◇——— | "a-un" (indépendant) |
| Composition | ◆——— | "possède" (dépendant) |
| Héritage | ───▷ | "est-un" |
| Réalisation | ─ ─ ▷ | "implémente" |

**Triangle d'héritage:** Pointe TOUJOURS vers le PARENT

**Multiplicité:**
- `1` = un
- `0..1` = zéro ou un
- `*` = plusieurs
- `1..*` = un ou plusieurs

---

## 📊 FICHE 11: Algorithmes de tri

| Algorithme | Meilleur | Moyen | Pire | Stable? |
|------------|----------|-------|------|---------|
| Bubble | O(n) | O(n²) | O(n²) | Oui |
| Quick | O(n log n) | O(n log n) | O(n²) | Non |
| Merge | O(n log n) | O(n log n) | O(n log n) | Oui |

**Stable:** Préserve l'ordre des éléments égaux

---

## 🗺️ FICHE 12: BFS vs DFS

| | BFS | DFS |
|-|-----|-----|
| **Structure** | Queue | Stack/Récursion |
| **Exploration** | Niveau par niveau | Profondeur d'abord |
| **Usage** | Plus court chemin | Détection cycles |
| **Complexité** | O(V + E) | O(V + E) |

**Mnémonique:**
- **B**FS = **B**roader → Queue
- **D**FS = **D**eeper → Stack

---

## ☕ FICHE 13: Java vs Python

| Concept | Python | Java |
|---------|--------|------|
| Variable | `x = 5` | `int x = 5;` |
| Print | `print("Hi")` | `System.out.println("Hi");` |
| Boolean | `True/False` | `true/false` |
| Null | `None` | `null` |
| Blocs | Indentation | Accolades `{}` |

**Pièges Java:**
- ❌ `==` pour strings → ✅ `.equals()`
- ❌ `True/False` → ✅ `true/false`
- ❌ Oublier `;` à la fin
- ❌ `ArrayList<int>` → ✅ `ArrayList<Integer>`

---

## 🔑 FICHE 14: Ports courants

| Port | Service |
|------|---------|
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS |
| 3306 | MySQL |
| 5432 | PostgreSQL |

---

## 🎬 FICHE 15: JavaScript DOM

```javascript
// Sélection
document.getElementById('id')
document.querySelector('.classe')
document.querySelectorAll('.classe')

// Modification
element.textContent = 'texte'
element.innerHTML = '<b>HTML</b>'
element.classList.add('classe')
element.style.color = 'red'

// Événements
element.addEventListener('click', function(e) {
    // Code
})

// Fetch API
const res = await fetch('/api/data')
const data = await res.json()
```

---

## 📝 FICHE 16: SQL Essentials

```sql
-- JOINs
INNER JOIN  -- Intersection
LEFT JOIN   -- Tout à gauche + correspondances

-- Agrégation
SELECT type, COUNT(*), AVG(solde)
FROM comptes
GROUP BY type
HAVING AVG(solde) > 1000

-- Transaction
BEGIN TRANSACTION;
UPDATE ...
COMMIT;  -- ou ROLLBACK
```

---

## 🧠 FICHE 17: Normalisation (DB)

| Forme | Idée clé | Objectif |
|-------|----------|----------|
| **1NF** | Valeurs atomiques | Pas de listes/colonnes multiples |
| **2NF** | Pas de dépendance partielle | Dépendre de toute la clé |
| **3NF** | Pas de dépendance transitive | Éviter redondance indirecte |

**À retenir:** normaliser = intégrité; dénormaliser = performance lecture.

---

## 📌 FICHE 18: Index (Quand/Pourquoi)

| Cas | Utilité |
|-----|---------|
| Filtre fréquent (`WHERE`) | ✅ Accélère |
| Jointure (`JOIN`) | ✅ Accélère |
| Colonne très mise à jour | ⚠️ Coût en écriture |
| Faible cardinalité | ⚠️ Index peu utile |

**Rappel:** un index = plus rapide en lecture, plus lent en écriture.

---

## 🔄 FICHE 19: Isolation & Anomalies

| Niveau | Dirty Read | Non-Repeatable | Phantom |
|--------|------------|----------------|---------|
| Read Uncommitted | Oui | Oui | Oui |
| Read Committed | Non | Oui | Oui |
| Repeatable Read | Non | Non | Oui |
| Serializable | Non | Non | Non |

**Anomalies:**
- Dirty Read = lecture non validée
- Non-Repeatable = même ligne change
- Phantom = nouvelles lignes apparaissent

---

## 🧩 FICHE 20: Design Patterns (Ultra-Rapide)

| Type | Pattern | Idée |
|------|---------|------|
| Création | Factory | Centraliser création |
| Création | Builder | Construire pas à pas |
| Structure | Adapter | Rendre compatible |
| Structure | Decorator | Ajouter sans modifier |
| Comportement | Strategy | Algorithmes interchangeables |
| Comportement | Observer | Notifier abonnés |

---

## 🏛️ FICHE 21: Architectures

| Style | Avantages | Limites |
|-------|-----------|---------|
| Monolithe | Simple, rapide à déployer | Scalabilité limitée |
| Microservices | Scalabilité, indépendance | Complexité ops |
| Event-driven | Découplage, résilience | Debug plus dur |

---

## 🧯 FICHE 22: Cache (Essentiels)

| Stratégie | Idée | Risque |
|----------|------|--------|
| Cache-aside | App lit cache puis DB | Cache miss |
| Write-through | Écrit cache + DB | Latence |
| Write-back | Écrit cache puis DB | Perte en crash |

**Règle d'or:** invalidation est le vrai problème.

---

## 🔐 FICHE 23: AuthN vs AuthZ

| Concept | Définition | Exemple |
|---------|------------|---------|
| **AuthN** | Vérifier identité | Login/mot de passe |
| **AuthZ** | Vérifier permission | Role ADMIN |

**JWT:** token signé, stateless.  
**Session:** état côté serveur.

---

## ✅ FICHE 24: Tests (Pyramide)

| Type | Portée | Outils |
|------|--------|--------|
| Unit | Petite | JUnit, pytest |
| Integration | Modules | Spring Test |
| E2E | Système complet | Cypress, Playwright |

**But:** rapide en bas, confiance en haut.

---

## 🧰 FICHE 25: Git Essentiels

| Commande | Usage |
|----------|-------|
| `git status` | état des fichiers |
| `git add .` | stage |
| `git commit -m "msg"` | commit |
| `git log --oneline` | historique |
| `git diff` | différences |

**Rappel:** commit petit = review facile.

---

## ✅ Checklist minute avant l'examen

- [ ] ACID = Atomicity, Consistency, Isolation, Durability
- [ ] SOLID = Single, Open/Closed, Liskov, Interface, Dependency
- [ ] OSI = Please Do Not Throw Sausage Pizza Away
- [ ] Box Model = margin → border → padding → content
- [ ] TCP 3-way = SYN → SYN-ACK → ACK
- [ ] HTTP codes: 2xx (succès), 4xx (client), 5xx (serveur)
- [ ] Big O: O(1) < O(log n) < O(n) < O(n log n) < O(n²)
- [ ] UML: Triangle héritage vers PARENT
- [ ] Java: true/false (minuscules), .equals() pour strings
- [ ] XSS = textContent, CSRF = token

---

**🎯 VOUS ÊTES PRÊT(E)! RESPIREZ, FAITES CONFIANCE À VOTRE PRÉPARATION!**
