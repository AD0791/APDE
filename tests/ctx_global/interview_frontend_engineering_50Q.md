# Frontend Engineering (50 Questions + Reponses)

Contexte: entretien pour analyste programmeur - unibankhaiti.

1) Q: Qu'est-ce que le DOM et pourquoi est-il important?
   A: Le DOM est la representation objet d'une page HTML; il permet a JS de lire/modifier la structure, le style et le contenu.
2) Q: Difference entre HTML, CSS et JavaScript?
   A: HTML structure le contenu, CSS le style, JS ajoute comportement et logique.
3) Q: Que fait le reflow (layout) et quand se produit-il?
   A: Calcul de la geometrie des elements; se produit lors de changements de style/DOM qui affectent la mise en page.
4) Q: Difference entre reflow et repaint?
   A: Reflow recalcule positions/taille; repaint redessine pixels sans changer la mise en page.
5) Q: Qu'est-ce que le event loop en JavaScript?
   A: Mecanisme qui execute la pile d'appels puis les taches asynchrones via la file de micro/macro-taches.
6) Q: Difference entre microtasks et macrotasks?
   A: Microtasks (Promise) s'executent avant le prochain rendu; macrotasks (setTimeout) apres.
7) Q: Que sont les closures et a quoi servent-elles?
   A: Fonctions qui capturent leur environnement; utiles pour l'encapsulation et les callbacks.
8) Q: Difference entre var, let, const?
   A: var a portee fonction et hoisting; let/const a portee bloc; const interdit la reassignment.
9) Q: Qu'est-ce que la delegation d'evenements?
   A: Attacher un seul listener a un parent pour gerer les events de ses enfants via bubbling.
10) Q: Comment prevenir un memory leak en front?
    A: Nettoyer timers, listeners, references DOM, annuler requetes et observers.
11) Q: Qu'est-ce que le Critical Rendering Path?
    A: Etapes: DOM, CSSOM, render tree, layout, paint; optimiser en reduisant blocage.
12) Q: Pourquoi utiliser defer/async sur les scripts?
    A: defer retarde execution apres parsing; async charge/exécute des que pret, ordre non garanti.
13) Q: Difference entre SPA et MPA?
    A: SPA charge une page et navigue via JS; MPA recharge a chaque page.
14) Q: Qu'est-ce que le CORS?
    A: Regles navigateur qui controlent les requetes cross-origin via en-tetes.
15) Q: Que fait un preflight OPTIONS?
    A: Verifie si la requete cross-origin est autorisee avant l'envoi.
16) Q: Cookies vs localStorage vs sessionStorage?
    A: Cookies envoyes au serveur; localStorage persistant; sessionStorage par onglet/session.
17) Q: Qu'est-ce qu'un service worker?
    A: Script en arriere-plan pour cache, offline, push, interception fetch.
18) Q: Strategies de cache HTTP?
    A: Cache-Control (max-age, no-cache), ETag, Last-Modified.
19) Q: Difference entre cache client et CDN?
    A: Cache client = navigateur; CDN = edge proche utilisateur pour statiques.
20) Q: Qu'est-ce que le HTTP/2 et son avantage?
    A: Multiplexage des requetes sur une connexion, head-of-line reduit.
21) Q: A quoi sert le HTTP/3?
    A: QUIC/UDP, meilleure latence et reprise connexion.
22) Q: Comment fonctionne un bundler (Webpack/Vite)?
    A: Regroupe modules, transpile, optimise et genere assets.
23) Q: Pourquoi utiliser tree shaking?
    A: Eliminer le code non utilise pour reduire la taille.
24) Q: Difference entre CSR et SSR?
    A: CSR rend cote client; SSR genere HTML cote serveur, meilleur SEO.
25) Q: A quoi sert l'hydratation?
    A: Rendre interactif un HTML SSR en attachant JS cote client.
26) Q: Qu'est-ce que CSS specificity?
    A: Regles de priorite des selecteurs; id > classe > element.
27) Q: Quand utiliser flexbox vs grid?
    A: Flexbox pour alignement 1D; grid pour layouts 2D.
28) Q: Qu'est-ce que le box model?
    A: Content, padding, border, margin; calcule taille totale d'un element.
29) Q: Difference entre position relative/absolute/fixed/sticky?
    A: relative decale sur place; absolute par rapport au parent positionne; fixed au viewport; sticky mix.
30) Q: Qu'est-ce que BEM?
    A: Convention de nommage CSS pour composants (Block__Element--Modifier).
31) Q: A quoi sert ARIA?
    A: Ameliorer l'accessibilite pour technologies d'assistance.
32) Q: Qu'est-ce que lazy loading?
    A: Charger ressources au besoin pour performance.
33) Q: Comment optimiser les images?
    A: Formats modernes (webp/avif), tailles responsives, compression.
34) Q: Difference entre debounce et throttle?
    A: Debounce retarde jusqu'a pause; throttle limite a une frequence.
35) Q: Qu'est-ce que XSS et comment prevenir?
    A: Injection de scripts; utiliser escaping, CSP, validation.
36) Q: Qu'est-ce que CSP?
    A: Content Security Policy limite sources scripts/styles pour securite.
37) Q: Qu'est-ce que CSRF et comment prevenir cote front?
    A: Requetes forgees; utiliser tokens CSRF, sameSite cookies.
38) Q: Que signifie "immutable state" en React?
    A: Ne pas muter l'etat; creer de nouvelles copies pour re-render fiable.
39) Q: Qu'est-ce que Virtual DOM?
    A: Representation en memoire du DOM pour diff/patch efficaces.
40) Q: Quand utiliser useMemo/useCallback?
    A: Memoriser valeurs/fonctions pour eviter recalculs inutiles.
41) Q: Que sont les hooks en React?
    A: Fonctions pour utiliser state/effects dans composants fonctionnels.
42) Q: Difference entre props et state?
    A: props viennent du parent; state est interne au composant.
43) Q: Qu'est-ce que le hydration mismatch?
    A: Difference HTML SSR vs client; cause warnings et bugs.
44) Q: Qu'est-ce qu'une "rendering waterfall"?
    A: Requetes sequentielles bloquantes; optimiser avec prefetch/parallel.
45) Q: Qu'est-ce que un Web Component?
    A: Custom elements, shadow DOM, encapsulation native.
46) Q: A quoi sert le shadow DOM?
    A: Encapsuler styles/structure pour eviter conflits.
47) Q: Difference entre GET et POST?
    A: GET pour lecture (idempotent), POST pour creation/modif.
48) Q: Qu'est-ce que fetch API et comment gerer erreurs?
    A: API promesse pour requetes; verifier response.ok et catch.
49) Q: Pourquoi utiliser TypeScript en front?
    A: Typage statique, meilleure maintenabilite et refactor.
50) Q: Comment tester le front?
    A: Unit tests (Jest), integration (RTL), e2e (Cypress/Playwright).
