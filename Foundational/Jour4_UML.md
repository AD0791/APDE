# Jour 4 (24 janvier): UML - Les 3 diagrammes essentiels

**Temps estimé:** 5-6 heures  
**Priorité:** 🟡 HAUTE - Modélisation systématique en examen

---

## Definitions

UML (Unified Modeling Language) est un langage de modélisation graphique standardisé pour :

1. Visualiser les systèmes logiciels

2. Spécifier leurs structures et comportements

3. Construire des modèles cohérents

4. Documenter les décisions de conception


## 🎯 Pourquoi UML est crucial

Les examens bancaires testent systématiquement la capacité à **modéliser des systèmes**. Concentrez-vous sur **3 diagrammes** qui couvrent 90% des questions:
1. **Diagramme de classes** - Structure statique
2. **Diagramme de cas d'utilisation** - Exigences fonctionnelles
3. **Diagramme de séquence** - Interactions dynamiques

---

## 📐 A. Diagramme de classes

### Notation de base

```
┌─────────────────────────┐
│      NomClasse          │  ← Nom (gras, centré)
├─────────────────────────┤
│ - attributPrive: Type   │  ← Attributs
│ + attributPublic: Type  │
│ # attributProtege: Type │
├─────────────────────────┤
│ + methodePublique(): Type│  ← Méthodes
│ - methodePrivee(): void │
└─────────────────────────┘
```

### Symboles de visibilité

| Symbole | Visibilité | Java équivalent |
|---------|------------|-----------------|
| `+` | Public | `public` |
| `-` | Privé | `private` |
| `#` | Protégé | `protected` |
| `~` | Package | (rien) |

### Relations entre classes

| Relation | Symbole | Signification | Exemple |
|----------|---------|---------------|---------|
| **Association** | ——————— | "utilise" ou "connaît" | Client ─── Compte |
| **Agrégation** | ◇——————— | "a-un" (tout-parties, parties indépendantes) | Banque ◇─── Agences |
| **Composition** | ◆——————— | "possède" (parties détruites avec le tout) | Commande ◆─── LignesCommande |
| **Héritage** | ────▷ | "est-un" (triangle vide) | CompteEpargne ──▷ Compte |
| **Réalisation** | ─ ─ ─▷ | Implémente interface (pointillé) | Classe ─ ─ ▷ Interface |
| **Dépendance** | - - - -▷ | "utilise temporairement" | Controleur - - -▷ Service |

### Multiplicité (cardinalité)

| Notation | Signification |
|----------|---------------|
| `1` | Exactement un |
| `0..1` | Zéro ou un |
| `*` ou `0..*` | Zéro ou plusieurs |
| `1..*` | Un ou plusieurs |
| `3..5` | Entre 3 et 5 |

### Exemple complet: Système bancaire

```
                    ┌──────────────────────┐
                    │       Banque         │
                    ├──────────────────────┤
                    │ - banqueId: String   │
                    │ - nom: String        │
                    │ - adresse: String    │
                    ├──────────────────────┤
                    │ + ajouterClient()    │
                    │ + getComptes(): List │
                    └──────────┬───────────┘
                               │ 1
                               │ gère
                               ◇
                               │ *
                    ┌──────────────────────┐
                    │       Client         │
                    ├──────────────────────┤
                    │ - clientId: String   │
                    │ - nom: String        │
                    │ - prenom: String     │
                    │ - email: String      │
                    ├──────────────────────┤
                    │ + ouvrirCompte()     │
                    │ + consulterSolde()   │
                    └──────────┬───────────┘
                               │ 1
                               │ possède
                               │
                               │ 1..*
                    ┌──────────────────────┐
                    │    «abstract»        │
                    │      Compte          │
                    ├──────────────────────┤
                    │ # numeroCompte: String│
                    │ # solde: Decimal     │
                    │ # dateOuverture: Date│
                    ├──────────────────────┤
                    │ + deposer(m): void   │
                    │ + retirer(m): boolean│
                    │ + getSolde(): Decimal│
                    └──────────┬───────────┘
                               △
              ┌────────────────┼────────────────┐
              │                │                │
   ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐
   │  CompteEpargne   │ │  CompteCourant   │ │  CompteCredit    │
   ├──────────────────┤ ├──────────────────┤ ├──────────────────┤
   │- tauxInteret: %  │ │- decouvertMax: $ │ │- limiteCredit: $ │
   │- retraitsMax: int│ │- fraisCheque: $  │ │- tauxAPR: %      │
   ├──────────────────┤ ├──────────────────┤ ├──────────────────┤
   │+ calculerInteret()│ │+ traiterCheque() │ │+ effectuerAchat()│
   │+ verifierRetrait()│ │+ autoriserDecouv()│ │+ calculerMin()   │
   └──────────────────┘ └──────────────────┘ └──────────────────┘
                               │
                               │ 1..* effectue
                               │
                               ◆
                    ┌──────────────────────┐
                    │    Transaction       │
                    ├──────────────────────┤
                    │ - transactionId      │
                    │ - montant: Decimal   │
                    │ - date: DateTime     │
                    │ - type: String       │
                    ├──────────────────────┤
                    │ + valider(): boolean │
                    └──────────────────────┘
```

### Notes importantes pour dessiner

1. **Triangle d'héritage:** Toujours vers le PARENT (pointe vers le haut)
2. **Agrégation vs Composition:**
   - ◇ Agrégation = losange VIDE (parties peuvent exister seules)
   - ◆ Composition = losange PLEIN (parties détruites avec le tout)
3. **Multiplicité:** Toujours des deux côtés de la relation
4. **Classe abstraite:** Écrire `«abstract»` ou nom en _italique_
5. **Interface:** Écrire `«interface»` au-dessus du nom

---

## 🎭 B. Diagramme de cas d'utilisation

### Éléments de base

- **Acteur** (bonhomme bâton): Utilisateur ou système externe
- **Cas d'utilisation** (ovale): Fonctionnalité du système
- **Frontière système** (rectangle): Périmètre du système
- **Relations:**
  - **Association** (ligne simple): Acteur participe au cas
  - **«include»**: Comportement obligatoire (flèche pointant vers le cas inclus)
  - **«extend»**: Comportement optionnel (flèche pointant vers le cas de base)

### Règles «include» vs «extend»

| | «include» | «extend» |
|-|-----------|----------|
| **Direction** | Base → Inclus | Extension → Base |
| **Obligatoire?** | Oui, toujours exécuté | Non, conditionnel |
| **Exemple** | Retirer argent **include** Authentifier | Consulter solde **extend** Imprimer reçu |

### Exemple: Système GAB (Guichet Automatique)

```
     ┌────────────────────────────────────────────────────┐
     │               Système GAB                          │
     │                                                    │
     │      ┌─────────────┐                               │
👤───┼──────│ Retirer     │                               │
Client     │   Espèces   │                                │
     │      └──────┬──────┘                               │
     │             │                                      │
     │        «include»                                   │
     │             ↓                                      │
     │      ┌─────────────┐                               │
     │      │Authentifier │◀────┐                         │
     │      │   Client    │     │ «include»               │
     │      └─────────────┘     │                         │
     │             ↑             │                         │
     │        «include»          │                         │
     │             │             │                         │
     │      ┌─────────────┐     │                         │
     │      │ Consulter   │─────┘                         │
     │      │   Solde     │                               │
     │      └──────┬──────┘                               │
     │             │                                      │
     │       ┌─────┴─────┐                                │
     │       │ «extend»  │                                │
     │       ↓           ↓                                │
     │ ┌──────────┐ ┌──────────┐                         │
     │ │ Imprimer │ │ Envoyer  │                         │
     │ │   Reçu   │ │   SMS    │                         │
     │ └──────────┘ └──────────┘                         │
     │                                                    │
     │      ┌─────────────┐                               │
     │      │ Effectuer   │                               │
     │      │  Virement   │◀──────«include»───────┐       │
     │      └─────────────┘                       │       │
     │                                            │       │
     │      ┌─────────────┐                       │       │
     │      │ Déposer     │                       │       │
     │      │  Chèque     │───────«include»───────┘       │
     │      └─────────────┘                               │
     │                                                    │
     └────────────────────────────────────────────────────┘
              │                           │
              │                           │
            👤────────────────────────────🏦
           Client                    Système
                                    Bancaire
```

### Points clés à retenir

- **Authentifier** est `«include»` (toujours requis avant toute opération)
- **Imprimer reçu** et **Envoyer SMS** sont `«extend»` (optionnels)
- L'acteur **Client** est TOUJOURS à l'extérieur de la frontière
- Le **Système Bancaire** (acteur secondaire) peut aussi interagir

---

## 🔄 C. Diagramme de séquence

### Éléments de base

| Élément | Représentation | Usage |
|---------|----------------|-------|
| **Objet/Acteur** | Rectangle en haut | Participants |
| **Ligne de vie** | Ligne verticale pointillée | Existence temporelle |
| **Boîte d'activation** | Rectangle fin sur ligne de vie | Objet actif |
| **Message synchrone** | Flèche pleine ─────▶ | Appel bloquant |
| **Message asynchrone** | Flèche ouverte ─────▷ | Appel non-bloquant |
| **Retour** | Flèche pointillée ◀─ ─ ─ | Réponse |
| **Fragment alt** | Boîte [condition] | Alternatives |
| **Fragment loop** | Boîte [n fois] | Boucles |
| **Fragment opt** | Boîte [si condition] | Optionnel |

### Exemple: Virement bancaire avec validation

```
:Client      :GAB          :ServeurBanque   :CompteSource   :CompteDest
    │          │               │               │              │
    │ insererCarte             │               │              │
    │─────────▶│               │               │              │
    │          │ validerCarte  │               │              │
    │          │──────────────▶│               │              │
    │          │  carteValide  │               │              │
    │          │◀──────────────│               │              │
    │          │               │               │              │
    │ saisirPIN│               │               │              │
    │─────────▶│               │               │              │
    │          │  verifierPIN  │               │              │
    │          │──────────────▶│               │              │
    │          │   pinOK       │               │              │
    │          │◀──────────────│               │              │
    │          │               │               │              │
    │ choisirVirement          │               │              │
    │─────────▶│               │               │              │
    │          │               │               │              │
    │ saisirMontant(500)       │               │              │
    │─────────▶│               │               │              │
    │          │ saisirDestination             │              │
    │◀─────────│               │               │              │
    │ compte789│               │               │              │
    │─────────▶│               │               │              │
    │          │               │               │              │
    │          │  verifierSolde│               │              │
    │          │──────────────▶│──────────────▶│              │
    │          │               │   solde=1000  │              │
    │          │               │◀──────────────│              │
    ┌──────────────────────────────────────────────────────────────┐
    │ alt [solde >= 500]                                           │
    ├──────────────────────────────────────────────────────────────┤
    │          │               │ debiter(500)  │              │    │
    │          │               │──────────────▶│              │    │
    │          │               │   OK          │              │    │
    │          │               │◀──────────────│              │    │
    │          │               │               │              │    │
    │          │               │  crediter(500)               │    │
    │          │               │─────────────────────────────▶│    │
    │          │               │               │  OK          │    │
    │          │               │◀─────────────────────────────│    │
    │          │               │               │              │    │
    │          │               │ enregistrerTransaction       │    │
    │          │               │──────────────────────────────│    │
    │          │               │               │              │    │
    │          │ virementOK    │               │              │    │
    │          │◀──────────────│               │              │    │
    │          │               │               │              │    │
    │ afficherSucces           │               │              │    │
    │◀─────────│               │               │              │    │
    │          │               │               │              │    │
    ├──────────────────────────────────────────────────────────────┤
    │ [sinon] solde insuffisant                                    │
    ├──────────────────────────────────────────────────────────────┤
    │          │   erreurSolde │               │              │    │
    │          │◀──────────────│               │              │    │
    │          │               │               │              │    │
    │ afficherErreur("Solde insuffisant")       │              │    │
    │◀─────────│               │               │              │    │
    └──────────────────────────────────────────────────────────────┘
```

### Notes importantes

1. **Ordre chronologique:** De haut en bas
2. **Messages numérotés:** Optionnels mais peuvent clarifier l'ordre
3. **Fragment alt:** Toujours avec au moins 2 branches (`[condition]` et `[sinon]`)
4. **Boîtes d'activation:** Montrent quand l'objet traite activement
5. **Flèches de retour:** En pointillé, étiquetées avec valeur retournée

---

## 🎨 Exemple 2: Système de réservation de vol

### Cas d'utilisation

```
     ┌────────────────────────────────────────────┐
     │      Système de Réservation Vols          │
     │                                            │
     │      ┌───────────────┐                     │
👤───┼──────│ Rechercher    │                     │
Passager   │   Vols        │                     │
     │      └───────┬───────┘                     │
     │              │                             │
     │              │ «include»                   │
     │              ↓                             │
     │      ┌───────────────┐                     │
     │      │  Consulter    │                     │
     │      │ Disponibilité │                     │
     │      └───────────────┘                     │
     │              ↑                             │
     │              │ «include»                   │
     │              │                             │
     │      ┌───────────────┐                     │
     │      │   Réserver    │                     │
     │      │     Vol       │                     │
     │      └───────┬───────┘                     │
     │              │                             │
     │              │ «extend»                    │
     │              ↓                             │
     │      ┌───────────────┐                     │
     │      │  Choisir      │                     │
     │      │   Siège       │                     │
     │      └───────────────┘                     │
     │                                            │
     │      ┌───────────────┐                     │
     │      │   Annuler     │                     │
     │      │ Réservation   │                     │
     │      └───────────────┘                     │
     │                                            │
     └────────────────────────────────────────────┘
```

---

## ⚠️ Pièges UML courants à éviter

### Diagramme de classes

| Erreur | Problème | Correction |
|--------|----------|------------|
| Flèche d'héritage inversée | Pointe vers l'enfant | Triangle pointe vers le PARENT |
| Confondre ◇ et ◆ | Mauvais type d'agrégation | ◇ = parties indépendantes, ◆ = parties dépendantes |
| Oublier multiplicité | Relation ambiguë | Toujours indiquer (1, *, 0..1, etc.) |
| Mettre des parenthèses après méthodes sans paramètres | `getNom()` au lieu de `getNom()` | Toujours mettre `()` même sans paramètres |

### Cas d'utilisation

| Erreur | Problème | Correction |
|--------|----------|------------|
| Acteur dans la frontière | Acteur fait partie du système | Acteurs TOUJOURS à l'extérieur |
| Flèche `«include»` inversée | Direction incorrecte | De base VERS inclus |
| Flèche `«extend»` inversée | Direction incorrecte | De extension VERS base |
| Trop de détails | Cas trop technique | Rester fonctionnel, pas technique |

### Séquence

| Erreur | Problème | Correction |
|--------|----------|------------|
| Flèche de retour solide | Retour = message asynchrone | Utiliser pointillé ◀─ ─ ─ |
| Oublier boîtes d'activation | Manque de clarté | Montrer quand l'objet est actif |
| Messages non étiquetés | Ambiguïté | Toujours nommer les messages |
| Ordre incorrect | Chronologie illogique | Vérifier le flux de haut en bas |

---

## 📝 Exercices pratiques Jour 4

### Exercice 1: Diagramme de classes
**Sur papier, dessiner le diagramme de classes pour:**

Système de bibliothèque avec:
- Bibliothèque (possède des livres)
- Livre (titre, auteur, ISBN)
- Emprunteur (nom, email, téléphone)
- Emprunt (date début, date fin, statut)

Relations:
- Un emprunteur peut emprunter plusieurs livres
- Un livre peut être emprunté par un seul emprunteur à la fois
- Un emprunt concerne un livre et un emprunteur

### Exercice 2: Cas d'utilisation
**Dessiner le diagramme de cas d'utilisation pour:**

Système de banque en ligne avec au moins:
- Acteur: Client
- 5 cas d'utilisation (dont au moins 1 `«include»` et 1 `«extend»`)

### Exercice 3: Séquence
**Dessiner le diagramme de séquence pour:**

Retrait au guichet automatique:
- Acteurs/Objets: Client, GAB, ServeurBanque, Compte
- Scénario: Insertion carte, saisie PIN, choix montant, validation solde, retrait
- Inclure un fragment `alt` pour solde suffisant/insuffisant

---

## 🔎 Extension: Compréhension & Rétention (Jour 4)

### 1) Erreurs classiques
- Triangle d'héritage orienté vers l'enfant (❌) → doit pointer vers le parent (✅)
- Confondre agrégation (◇) et composition (◆)
- Oublier les multiplicités aux extrémités
- Mettre les acteurs dans la frontière système (❌)

### 2) Cas bancaire express (à dessiner)
- **Ouverture de compte** (use case + séquence)
- **Virement interne** (séquence avec contrôle solde)
- **Blocage de carte** (use case avec include/extend)

### 3) Questions type examen
- Différence association vs dépendance
- Quand utiliser un diagramme d'activité plutôt qu'une séquence?
- Donner un exemple de composition dans un domaine bancaire

---

## ✅ Checklist de révision Jour 4

- [ ] Connaître les symboles de visibilité (+, -, #, ~)
- [ ] Différencier agrégation (◇) et composition (◆)
- [ ] Dessiner correctement le triangle d'héritage (vers parent)
- [ ] Utiliser correctement les multiplicités (1, *, 0..1, 1..*)
- [ ] Comprendre `«include»` (obligatoire) vs `«extend»` (optionnel)
- [ ] Savoir que les acteurs sont HORS de la frontière système
- [ ] Dessiner les messages synchrones (pleine) vs asynchrones (ouverte)
- [ ] Utiliser les fragments alt, loop, opt
- [ ] Dessiner les boîtes d'activation sur les lignes de vie
- [ ] Faire des retours en pointillé

---

**💡 Conseil:** Pratiquez en dessinant sur papier! UML à l'examen se fait à la main avec une règle. Entraînez-vous à dessiner proprement et rapidement.

**Prochain document:** `Jour5_DSA_Structures.md` - Structures de données
