# Jour 7 (27 janvier): Backend, Networking & Frontend (ENRICHI)

**Temps estimé:** 5-6 heures  
**Priorité:** 🟢 MOYENNE - Compléter les connaissances web

---

## 🎯 Objectif du jour

Couvrir les **bases du backend, networking et surtout FRONTEND** en détail. Le frontend est souvent testé en examen et ce document contient un contenu très enrichi sur HTML5, CSS3, JavaScript DOM, événements, AJAX, frameworks, et sécurité.

---

## 🌐 PARTIE 1: BACKEND - REST API

### Principes REST (Representational State Transfer)

| Principe | Description | Exemple |
|----------|-------------|---------|
| **Stateless** | Chaque requête contient toutes les infos nécessaires | Pas de session serveur |
| **Client-Server** | Séparation des préoccupations | Frontend ≠ Backend |
| **Cacheable** | Réponses marquées comme cacheables ou non | Headers HTTP |
| **Uniform Interface** | Interface uniforme (URIs, méthodes HTTP) | GET /users/123 |
| **Layered System** | Architecture en couches | Load balancer, cache, serveur |

### Méthodes HTTP et codes de statut

| Méthode | Action | Exemple | Idempotent? |
|---------|--------|---------|-------------|
| **GET** | Lire | GET /comptes/123 | Oui |
| **POST** | Créer | POST /comptes | Non |
| **PUT** | Remplacer | PUT /comptes/123 | Oui |
| **PATCH** | Modifier partiellement | PATCH /comptes/123 | Non |
| **DELETE** | Supprimer | DELETE /comptes/123 | Oui |

### Codes de statut HTTP à MÉMORISER

| Code | Catégorie | Signification | Quand utiliser |
|------|-----------|---------------|----------------|
| **200** | Succès | OK | GET, PUT, PATCH réussis |
| **201** | Succès | Created | POST réussi (ressource créée) |
| **204** | Succès | No Content | DELETE réussi (pas de body) |
| **400** | Client | Bad Request | Erreurs de validation, données invalides |
| **401** | Client | Unauthorized | Non authentifié (pas de token) |
| **403** | Client | Forbidden | Authentifié mais pas autorisé |
| **404** | Client | Not Found | Ressource inexistante |
| **500** | Serveur | Internal Server Error | Erreur serveur non gérée |
| **503** | Serveur | Service Unavailable | Service temporairement indisponible |

### Exemple d'API REST bancaire

```
GET    /api/v1/comptes           → Liste tous les comptes
GET    /api/v1/comptes/{id}      → Détails d'un compte
POST   /api/v1/comptes           → Créer un compte
PUT    /api/v1/comptes/{id}      → Remplacer un compte
PATCH  /api/v1/comptes/{id}      → Modifier un compte
DELETE /api/v1/comptes/{id}      → Supprimer un compte

GET    /api/v1/comptes/{id}/transactions  → Transactions d'un compte
POST   /api/v1/virements          → Effectuer un virement
```

---

## 🔌 PARTIE 2: NETWORKING

### Modèle OSI - 7 couches

| Couche | Nom | Fonction | Protocoles | Équipement |
|--------|-----|----------|------------|------------|
| **7** | Application | Interface utilisateur | HTTP, HTTPS, FTP, SMTP, DNS | - |
| **6** | Présentation | Formatage, encryption | SSL/TLS, JPEG, MPEG | - |
| **5** | Session | Gestion des sessions | NetBIOS, RPC | - |
| **4** | Transport | Livraison bout-en-bout | TCP, UDP | - |
| **3** | Réseau | Adressage logique, routage | IP, ICMP, ARP | Routeur |
| **2** | Liaison | Adressage physique (MAC) | Ethernet, PPP | Switch |
| **1** | Physique | Transmission bits | Câbles, Wi-Fi, Fibre | Hub, Câbles |

**Mnémonique:** **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way

### TCP vs UDP

| Caractéristique | TCP | UDP |
|-----------------|-----|-----|
| **Connexion** | Orienté connexion (3-way handshake) | Sans connexion |
| **Fiabilité** | Garantie de livraison, réordonne paquets | Pas de garantie |
| **Ordre** | Maintient l'ordre des paquets | Pas d'ordre garanti |
| **Vitesse** | Plus lent (overhead) | Plus rapide |
| **Contrôle de flux** | Oui | Non |
| **Usage** | Web (HTTP), email (SMTP), fichiers (FTP) | Streaming, VoIP, DNS, jeux |
| **Overhead** | Plus élevé | Minimal |

### TCP 3-Way Handshake

```
Client                Server
   │                     │
   │──── SYN ──────────▶│  (1) Client demande connexion
   │                     │
   │◀─── SYN-ACK ───────│  (2) Serveur accepte
   │                     │
   │──── ACK ──────────▶│  (3) Client confirme
   │                     │
   │ Connexion établie   │
```

### HTTP vs HTTPS

| HTTP | HTTPS |
|------|-------|
| Port 80 | Port 443 |
| Non chiffré (plain text) | Chiffré via TLS/SSL |
| Vulnérable aux attaques MITM | Protégé contre interception |
| Pas d'authentification serveur | Certificat SSL valide le serveur |
| Plus rapide | Légèrement plus lent (chiffrement) |

### Ports courants à mémoriser

| Port | Service | Protocole |
|------|---------|-----------|
| **20/21** | FTP (transfert fichiers) | TCP |
| **22** | SSH (connexion sécurisée) | TCP |
| **23** | Telnet (connexion non sécurisée) | TCP |
| **25** | SMTP (envoi email) | TCP |
| **53** | DNS (résolution noms) | UDP/TCP |
| **80** | HTTP (web) | TCP |
| **110** | POP3 (réception email) | TCP |
| **143** | IMAP (réception email) | TCP |
| **443** | HTTPS (web sécurisé) | TCP |
| **3306** | MySQL | TCP |
| **5432** | PostgreSQL | TCP |

---

## 💻 PARTIE 3: FRONTEND (ENRICHI)

### 📄 A. HTML5 - Structure et Sémantique

#### Structure HTML5 de base

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Système bancaire en ligne">
    <title>Banque Unibank - Accueil</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#accueil">Accueil</a></li>
                <li><a href="#comptes">Mes comptes</a></li>
                <li><a href="#virements">Virements</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <section id="comptes">
            <h1>Mes comptes</h1>
            <article class="compte">
                <h2>Compte courant</h2>
                <p>Solde: 5000 HTG</p>
            </article>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2026 Unibank Haiti</p>
    </footer>
    
    <script src="script.js"></script>
</body>
</html>
```

#### Balises sémantiques HTML5

| Balise | Usage | Exemple |
|--------|-------|---------|
| `<header>` | En-tête de page/section | Logo, navigation |
| `<nav>` | Navigation | Menu principal |
| `<main>` | Contenu principal | Unique par page |
| `<section>` | Section thématique | Section "Comptes" |
| `<article>` | Contenu autonome | Article blog, produit |
| `<aside>` | Contenu annexe | Sidebar, pub |
| `<footer>` | Pied de page/section | Copyright, liens |
| `<figure>` | Contenu illustratif | Image + légende |
| `<figcaption>` | Légende de figure | Description image |
| `<time>` | Date/heure | `<time datetime="2026-01-21">` |

#### Formulaires HTML5 avec validation

```html
<form id="formulaire-virement" action="/api/virements" method="POST">
    <!-- Input texte avec validation -->
    <label for="beneficiaire">Bénéficiaire:</label>
    <input type="text" 
           id="beneficiaire" 
           name="beneficiaire" 
           required 
           minlength="3"
           maxlength="50"
           pattern="[A-Za-zÀ-ÿ\s]+"
           placeholder="Nom complet">
    
    <!-- Input email avec validation -->
    <label for="email">Email:</label>
    <input type="email" 
           id="email" 
           name="email" 
           required
           placeholder="exemple@email.com">
    
    <!-- Input numérique -->
    <label for="montant">Montant (HTG):</label>
    <input type="number" 
           id="montant" 
           name="montant" 
           required
           min="1"
           max="100000"
           step="0.01">
    
    <!-- Select -->
    <label for="compte-source">Compte source:</label>
    <select id="compte-source" name="compte_source" required>
        <option value="">-- Choisir --</option>
        <option value="001">Compte courant - 001</option>
        <option value="002">Compte épargne - 002</option>
    </select>
    
    <!-- Date -->
    <label for="date-execution">Date d'exécution:</label>
    <input type="date" 
           id="date-execution" 
           name="date_execution"
           min="2026-01-21"
           required>
    
    <!-- Textarea -->
    <label for="description">Description:</label>
    <textarea id="description" 
              name="description" 
              rows="3"
              maxlength="200"></textarea>
    
    <!-- Checkbox -->
    <label>
        <input type="checkbox" name="confirmation" required>
        Je confirme les informations
    </label>
    
    <!-- Radio buttons -->
    <fieldset>
        <legend>Type de virement:</legend>
        <label>
            <input type="radio" name="type" value="immediat" checked>
            Immédiat
        </label>
        <label>
            <input type="radio" name="type" value="differe">
            Différé
        </label>
    </fieldset>
    
    <button type="submit">Effectuer le virement</button>
    <button type="reset">Réinitialiser</button>
</form>
```

#### Types d'inputs HTML5

| Type | Validation automatique | Exemple |
|------|------------------------|---------|
| `text` | Aucune | `<input type="text">` |
| `email` | Format email | `<input type="email">` |
| `number` | Numérique | `<input type="number" min="0" max="100">` |
| `tel` | Téléphone | `<input type="tel" pattern="[0-9]{10}">` |
| `url` | URL valide | `<input type="url">` |
| `date` | Date | `<input type="date">` |
| `time` | Heure | `<input type="time">` |
| `password` | Masqué | `<input type="password">` |
| `search` | Recherche | `<input type="search">` |
| `color` | Sélecteur couleur | `<input type="color">` |

---

### 🎨 B. CSS3 - Mise en page et Design

#### Box Model - Concept FONDAMENTAL

```
┌─────────────── margin ────────────────┐
│ ┌──────────── border ──────────────┐ │
│ │ ┌──────── padding ────────────┐ │ │
│ │ │                              │ │ │
│ │ │        CONTENT               │ │ │
│ │ │      width x height          │ │ │
│ │ │                              │ │ │
│ │ └──────────────────────────────┘ │ │
│ └──────────────────────────────────┘ │
└──────────────────────────────────────┘

Largeur totale = margin + border + padding + width + padding + border + margin
```

#### Exemple pratique

```css
.compte-card {
    /* Content */
    width: 300px;
    height: 200px;
    
    /* Padding (espace interne) */
    padding: 20px;
    
    /* Border */
    border: 2px solid #333;
    border-radius: 10px;
    
    /* Margin (espace externe) */
    margin: 15px;
    
    /* Autres propriétés */
    background-color: #f5f5f5;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

/* Box-sizing: border-box → width inclut padding et border */
.compte-card-alt {
    box-sizing: border-box;  /* Recommandé! */
    width: 300px;  /* Largeur finale exacte */
    padding: 20px;
    border: 2px solid #333;
}
```

#### Sélecteurs CSS essentiels

```css
/* Sélecteur d'élément */
p { color: blue; }

/* Sélecteur de classe */
.compte { background: #eee; }

/* Sélecteur d'ID (unique) */
#header-principal { height: 60px; }

/* Sélecteur descendant */
nav a { text-decoration: none; }

/* Sélecteur enfant direct */
nav > ul > li { display: inline-block; }

/* Sélecteur d'attribut */
input[type="email"] { border: 1px solid blue; }
input[required] { border-left: 3px solid red; }

/* Pseudo-classes */
a:hover { color: red; }
a:visited { color: purple; }
input:focus { outline: 2px solid blue; }
li:first-child { font-weight: bold; }
li:last-child { margin-bottom: 0; }
tr:nth-child(even) { background: #f9f9f9; }

/* Pseudo-éléments */
p::before { content: "→ "; }
p::after { content: " ←"; }
p::first-letter { font-size: 2em; }
```

#### Flexbox - Layout moderne

```css
/* Container flex */
.container-comptes {
    display: flex;
    flex-direction: row;  /* row | column | row-reverse | column-reverse */
    justify-content: space-between;  /* flex-start | center | space-between | space-around */
    align-items: center;  /* flex-start | center | flex-end | stretch */
    flex-wrap: wrap;  /* nowrap | wrap | wrap-reverse */
    gap: 20px;  /* Espace entre items */
}

/* Items flex */
.compte-item {
    flex: 1;  /* Grossit pour remplir l'espace */
    /* flex: 0 0 300px;  → Ne grandit pas, ne rétrécit pas, base 300px */
    min-width: 250px;
}
```

#### Grid Layout - Grilles avancées

```css
.dashboard {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;  /* 3 colonnes */
    grid-template-rows: auto 1fr auto;  /* 3 lignes */
    grid-gap: 20px;
    height: 100vh;
}

/* Exemple: Dashboard bancaire */
.dashboard-bancaire {
    display: grid;
    grid-template-areas:
        "header header header"
        "sidebar main aside"
        "footer footer footer";
    grid-template-columns: 250px 1fr 300px;
    grid-template-rows: 60px 1fr 50px;
    gap: 15px;
}

.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main-content { grid-area: main; }
.aside-info { grid-area: aside; }
.footer { grid-area: footer; }
```

#### Responsive Design avec Media Queries

```css
/* Mobile First */
.container {
    width: 100%;
    padding: 10px;
}

/* Tablettes (768px et plus) */
@media (min-width: 768px) {
    .container {
        width: 750px;
        margin: 0 auto;
    }
    
    .compte-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
    }
}

/* Desktop (1024px et plus) */
@media (min-width: 1024px) {
    .container {
        width: 960px;
    }
    
    .compte-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}

/* Large Desktop (1200px et plus) */
@media (min-width: 1200px) {
    .container {
        width: 1140px;
    }
}
```

#### Animations et Transitions CSS

```css
/* Transition simple */
.bouton {
    background-color: #007bff;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: all 0.3s ease;  /* propriété durée fonction */
}

.bouton:hover {
    background-color: #0056b3;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

/* Animation avec @keyframes */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.compte-card {
    animation: fadeIn 0.5s ease-in-out;
}

/* Animation de chargement */
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.loader {
    border: 4px solid #f3f3f3;
    border-top: 4px solid #3498db;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    animation: spin 1s linear infinite;
}
```

---

### ⚡ C. JavaScript - DOM et Événements

#### Sélection d'éléments

```javascript
// Sélectionner par ID
const header = document.getElementById('header');

// Sélectionner par classe (premier élément)
const compte = document.querySelector('.compte');

// Sélectionner par classe (tous les éléments)
const comptes = document.querySelectorAll('.compte');

// Sélectionner par balise
const paragraphes = document.getElementsByTagName('p');

// Sélectionner par classe (tous)
const cards = document.getElementsByClassName('card');

// Sélectionner par attribut data-*
const boutonValider = document.querySelector('[data-action="valider"]');
```

#### Manipulation du DOM

```javascript
// Modifier le contenu texte
element.textContent = 'Nouveau texte';
element.innerHTML = '<strong>Texte HTML</strong>';

// Modifier les attributs
element.setAttribute('data-id', '123');
element.getAttribute('data-id');  // "123"
element.removeAttribute('disabled');

// Modifier les classes
element.classList.add('actif');
element.classList.remove('inactif');
element.classList.toggle('visible');
element.classList.contains('actif');  // true/false

// Modifier le style
element.style.color = 'red';
element.style.backgroundColor = '#f0f0f0';
element.style.display = 'none';

// Créer et ajouter des éléments
const nouveauDiv = document.createElement('div');
nouveauDiv.textContent = 'Nouveau compte';
nouveauDiv.classList.add('compte-card');
document.getElementById('liste-comptes').appendChild(nouveauDiv);

// Insérer avant un élément
parent.insertBefore(nouveauDiv, elementExistant);

// Supprimer un élément
element.remove();  // Méthode moderne
parent.removeChild(element);  // Ancienne méthode
```

#### Événements

```javascript
// Événement click
document.getElementById('bouton-virement').addEventListener('click', function(e) {
    console.log('Virement cliqué');
    // e.preventDefault();  // Empêcher comportement par défaut
});

// Événement submit de formulaire
document.getElementById('formulaire').addEventListener('submit', function(e) {
    e.preventDefault();  // Empêcher rechargement page
    
    // Récupérer les valeurs
    const beneficiaire = document.getElementById('beneficiaire').value;
    const montant = parseFloat(document.getElementById('montant').value);
    
    // Valider
    if (montant <= 0) {
        alert('Montant invalide');
        return;
    }
    
    // Traiter...
    console.log(`Virement de ${montant} HTG vers ${beneficiaire}`);
});

// Événement input (changement en temps réel)
document.getElementById('montant').addEventListener('input', function(e) {
    const valeur = e.target.value;
    console.log('Montant saisi:', valeur);
});

// Événement change (après changement)
document.getElementById('compte-source').addEventListener('change', function(e) {
    const compteChoisi = e.target.value;
    console.log('Compte sélectionné:', compteChoisi);
});

// Événement mouseover/mouseout
element.addEventListener('mouseover', function() {
    this.style.backgroundColor = '#f0f0f0';
});

element.addEventListener('mouseout', function() {
    this.style.backgroundColor = 'white';
});

// Événement keypress
document.getElementById('recherche').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        console.log('Recherche:', this.value);
    }
});

// Délégation d'événements (pour éléments dynamiques)
document.getElementById('liste-comptes').addEventListener('click', function(e) {
    if (e.target.classList.contains('bouton-details')) {
        const compteId = e.target.dataset.compteId;
        afficherDetails(compteId);
    }
});
```

#### Exemple complet: Liste de comptes dynamique

```javascript
// Données
const comptes = [
    { id: 1, numero: '001', type: 'Courant', solde: 5000 },
    { id: 2, numero: '002', type: 'Épargne', solde: 15000 },
    { id: 3, numero: '003', type: 'Crédit', solde: -2000 }
];

// Afficher les comptes
function afficherComptes() {
    const container = document.getElementById('liste-comptes');
    container.innerHTML = '';  // Vider
    
    comptes.forEach(compte => {
        const card = document.createElement('div');
        card.className = 'compte-card';
        card.innerHTML = `
            <h3>Compte ${compte.type}</h3>
            <p>Numéro: ${compte.numero}</p>
            <p class="${compte.solde >= 0 ? 'solde-positif' : 'solde-negatif'}">
                Solde: ${compte.solde.toFixed(2)} HTG
            </p>
            <button class="btn-details" data-id="${compte.id}">Détails</button>
        `;
        container.appendChild(card);
    });
    
    // Ajouter événements aux boutons
    document.querySelectorAll('.btn-details').forEach(btn => {
        btn.addEventListener('click', function() {
            const id = parseInt(this.dataset.id);
            const compte = comptes.find(c => c.id === id);
            alert(`Détails du compte ${compte.numero}`);
        });
    });
}

// Appeler au chargement
document.addEventListener('DOMContentLoaded', afficherComptes);
```

---

### 🌐 D. AJAX et Fetch API

#### XMLHttpRequest (ancienne méthode)

```javascript
function chargerComptes() {
    const xhr = new XMLHttpRequest();
    
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {  // Requête terminée
            if (xhr.status === 200) {  // Succès
                const comptes = JSON.parse(xhr.responseText);
                afficherComptes(comptes);
            } else {
                console.error('Erreur:', xhr.status);
            }
        }
    };
    
    xhr.open('GET', '/api/comptes', true);
    xhr.setRequestHeader('Authorization', 'Bearer ' + token);
    xhr.send();
}
```

#### Fetch API (moderne) - GET

```javascript
// Requête GET simple
fetch('/api/comptes')
    .then(response => {
        if (!response.ok) {
            throw new Error('Erreur HTTP: ' + response.status);
        }
        return response.json();
    })
    .then(comptes => {
        console.log('Comptes reçus:', comptes);
        afficherComptes(comptes);
    })
    .catch(error => {
        console.error('Erreur:', error);
        alert('Impossible de charger les comptes');
    });

// Avec async/await (préféré)
async function chargerComptes() {
    try {
        const response = await fetch('/api/comptes', {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem('token')
            }
        });
        
        if (!response.ok) {
            throw new Error('Erreur HTTP: ' + response.status);
        }
        
        const comptes = await response.json();
        afficherComptes(comptes);
    } catch (error) {
        console.error('Erreur:', error);
        alert('Impossible de charger les comptes');
    }
}
```

#### Fetch API - POST

```javascript
async function effectuerVirement(data) {
    try {
        const response = await fetch('/api/virements', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + localStorage.getItem('token')
            },
            body: JSON.stringify(data)
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.message || 'Erreur inconnue');
        }
        
        const resultat = await response.json();
        alert('Virement effectué avec succès!');
        return resultat;
    } catch (error) {
        console.error('Erreur:', error);
        alert('Erreur: ' + error.message);
    }
}

// Utilisation
const dataVirement = {
    compteSource: '001',
    compteDestination: '002',
    montant: 500,
    description: 'Virement test'
};
effectuerVirement(dataVirement);
```

#### Fetch API - PUT et DELETE

```javascript
// PUT - Mise à jour
async function modifierCompte(id, data) {
    const response = await fetch(`/api/comptes/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        },
        body: JSON.stringify(data)
    });
    return await response.json();
}

// DELETE - Suppression
async function supprimerCompte(id) {
    const response = await fetch(`/api/comptes/${id}`, {
        method: 'DELETE',
        headers: {
            'Authorization': 'Bearer ' + token
        }
    });
    return response.status === 204;  // No Content
}
```

---

### 🛡️ E. Sécurité Frontend

#### XSS (Cross-Site Scripting)

**Attaque:** Injection de script malveillant dans une page web.

```javascript
// ❌ DANGEREUX - XSS possible
const nom = "<script>alert('XSS')</script>";
element.innerHTML = nom;  // Le script s'exécute!

// ✅ SÛR - Échappe automatiquement
element.textContent = nom;  // Affiche le texte tel quel

// ✅ SÛR - Validation et échappement
function echapperHTML(texte) {
    const div = document.createElement('div');
    div.textContent = texte;
    return div.innerHTML;
}

// ✅ SÛR - Utiliser une bibliothèque comme DOMPurify
const contenuPropre = DOMPurify.sanitize(contenuUtilisateur);
element.innerHTML = contenuPropre;
```

**Prévention XSS:**
- ✅ Utiliser `textContent` au lieu de `innerHTML`
- ✅ Valider et échapper toutes les entrées utilisateur
- ✅ Utiliser Content Security Policy (CSP)
- ✅ HttpOnly cookies (pour tokens)

#### CSRF (Cross-Site Request Forgery)

**Attaque:** Utilisateur authentifié trompé pour exécuter une action.

**Exemple d'attaque:**
```html
<!-- Page malveillante -->
<img src="https://banque.com/api/virement?vers=attaquant&montant=10000">
<!-- Si l'utilisateur est connecté, le virement s'exécute! -->
```

**Prévention CSRF:**

```javascript
// ✅ Token CSRF dans chaque requête
async function effectuerAction(data) {
    const csrfToken = document.querySelector('meta[name="csrf-token"]').content;
    
    const response = await fetch('/api/action', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRF-Token': csrfToken
        },
        body: JSON.stringify(data)
    });
    return await response.json();
}

// ✅ SameSite cookies
// Côté serveur: Set-Cookie: token=...; SameSite=Strict; Secure; HttpOnly

// ✅ Vérifier Origin/Referer
// Côté serveur: vérifier que la requête vient du bon domaine
```

#### Stockage sécurisé

```javascript
// ❌ DANGEREUX - localStorage vulnérable à XSS
localStorage.setItem('token', 'secret-token-123');

// ✅ PRÉFÉRÉ - Cookies HttpOnly (côté serveur)
// Set-Cookie: token=secret; HttpOnly; Secure; SameSite=Strict

// Si localStorage nécessaire (pas pour tokens sensibles):
// - Chiffrer les données
// - Tokens courts (expiration rapide)
// - Validation stricte de l'origine
```

#### Validation côté client

```javascript
function validerVirement(data) {
    // Validation montant
    if (typeof data.montant !== 'number' || data.montant <= 0) {
        throw new Error('Montant invalide');
    }
    
    if (data.montant > 100000) {
        throw new Error('Montant trop élevé');
    }
    
    // Validation numéro de compte (format)
    const regexCompte = /^[0-9]{3,10}$/;
    if (!regexCompte.test(data.compteDestination)) {
        throw new Error('Numéro de compte invalide');
    }
    
    // Validation email
    const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (data.email && !regexEmail.test(data.email)) {
        throw new Error('Email invalide');
    }
    
    return true;
}
```

---

### 📚 F. Frameworks Frontend (concepts de base)

#### React - Composants

```javascript
// Composant fonctionnel
function CompteCarte({ numero, type, solde }) {
    return (
        <div className="compte-card">
            <h3>Compte {type}</h3>
            <p>Numéro: {numero}</p>
            <p className={solde >= 0 ? 'positif' : 'negatif'}>
                Solde: {solde.toFixed(2)} HTG
            </p>
        </div>
    );
}

// Utilisation
function App() {
    const comptes = [
        { numero: '001', type: 'Courant', solde: 5000 },
        { numero: '002', type: 'Épargne', solde: 15000 }
    ];
    
    return (
        <div>
            <h1>Mes comptes</h1>
            {comptes.map((compte, index) => (
                <CompteCarte key={index} {...compte} />
            ))}
        </div>
    );
}
```

#### Angular - Composants

```typescript
// compte.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-compte-carte',
  template: `
    <div class="compte-card">
      <h3>Compte {{type}}</h3>
      <p>Numéro: {{numero}}</p>
      <p [class.positif]="solde >= 0" [class.negatif]="solde < 0">
        Solde: {{solde | number:'1.2-2'}} HTG
      </p>
    </div>
  `
})
export class CompteCarteComponent {
  @Input() numero: string;
  @Input() type: string;
  @Input() solde: number;
}
```

#### Vue.js - Composants

```javascript
// CompteCard.vue
<template>
  <div class="compte-card">
    <h3>Compte {{ type }}</h3>
    <p>Numéro: {{ numero }}</p>
    <p :class="solde >= 0 ? 'positif' : 'negatif'">
      Solde: {{ solde.toFixed(2) }} HTG
    </p>
  </div>
</template>

<script>
export default {
  props: ['numero', 'type', 'solde']
}
</script>
```

---

## 📝 Exercices pratiques Jour 7

### Exercice 1: HTML/CSS
**Sur papier, écrire le HTML et CSS pour:**
- Une carte de compte avec nom, numéro, solde
- Utiliser Flexbox pour centrer le contenu
- Ajouter un hover effect

### Exercice 2: JavaScript DOM
**Sur papier, écrire le JavaScript pour:**
- Sélectionner tous les éléments avec classe `.compte`
- Ajouter un événement click sur chaque compte
- Afficher le numéro de compte dans une alert

### Exercice 3: Fetch API
**Sur papier, écrire une fonction async/await pour:**
- Faire un GET sur `/api/comptes`
- Gérer les erreurs avec try/catch
- Afficher les comptes dans le DOM

### Exercice 4: Sécurité
**Expliquer en 2-3 phrases:**
1. Qu'est-ce que XSS et comment le prévenir?
2. Qu'est-ce que CSRF et comment le prévenir?
3. Pourquoi utiliser HttpOnly cookies pour les tokens?

---

## ✅ Checklist de révision Jour 7

### Backend & Networking
- [ ] Connaître les 5 méthodes HTTP et leurs usages
- [ ] Mémoriser 10 codes de statut HTTP
- [ ] Réciter les 7 couches OSI avec mnémonique
- [ ] Différencier TCP et UDP (5 points)
- [ ] Expliquer le TCP 3-way handshake
- [ ] Différencier HTTP et HTTPS
- [ ] Mémoriser 8 ports courants

### Frontend
- [ ] Connaître 10 balises sémantiques HTML5
- [ ] Expliquer le Box Model CSS
- [ ] Utiliser Flexbox pour layout
- [ ] Écrire une media query responsive
- [ ] Sélectionner éléments DOM (5 méthodes)
- [ ] Manipuler le DOM (create, append, remove)
- [ ] Ajouter événements (click, submit, input)
- [ ] Utiliser Fetch API avec async/await
- [ ] Expliquer XSS et CSRF avec prévention
- [ ] Différencier textContent et innerHTML

---

**💡 Conseil:** Le frontend est vaste! Concentrez-vous sur les bases solides: HTML sémantique, Box Model CSS, manipulation DOM JavaScript, et sécurité XSS/CSRF.

**Prochain document:** `Jour8_Revision_Simulation.md` - Consolidation finale
