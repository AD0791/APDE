# Étude de Cas Frontend — Niveau Basique

## Guide de Préparation : HTML, CSS, JavaScript et DOM Fundamentaux

---

Ce document couvre les compétences frontend essentielles pour développer une interface bancaire simple et interactive. Vous apprendrez à manipuler le DOM, gérer les événements, valider des formulaires et créer des composants réutilisables en JavaScript vanilla.

---

## Problème 1 : Formulaire de Création de Compte avec Validation

### Énoncé

Créer un formulaire HTML permettant l'inscription d'un nouveau client avec validation en temps réel :
- Nom complet (requis, min 3 caractères)
- Email (format valide)
- Téléphone (10 chiffres)
- Type de compte (Courant/Épargne)
- Montant initial (minimum 100 HTG)

### Solution HTML

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Création de Compte Bancaire</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Ouvrir un Compte</h1>
        <form id="accountForm" novalidate>
            <div class="form-group">
                <label for="fullName">Nom Complet *</label>
                <input 
                    type="text" 
                    id="fullName" 
                    name="fullName" 
                    required 
                    minlength="3"
                    placeholder="Jean Pierre Dupont"
                >
                <span class="error" id="fullNameError"></span>
            </div>

            <div class="form-group">
                <label for="email">Email *</label>
                <input 
                    type="email" 
                    id="email" 
                    name="email" 
                    required
                    placeholder="jean.dupont@example.ht"
                >
                <span class="error" id="emailError"></span>
            </div>

            <div class="form-group">
                <label for="phone">Téléphone *</label>
                <input 
                    type="tel" 
                    id="phone" 
                    name="phone" 
                    required
                    pattern="[0-9]{10}"
                    placeholder="3712345678"
                >
                <span class="error" id="phoneError"></span>
            </div>

            <div class="form-group">
                <label for="accountType">Type de Compte *</label>
                <select id="accountType" name="accountType" required>
                    <option value="">-- Choisir --</option>
                    <option value="COURANT">Compte Courant</option>
                    <option value="EPARGNE">Compte Épargne</option>
                </select>
                <span class="error" id="accountTypeError"></span>
            </div>

            <div class="form-group">
                <label for="initialAmount">Dépôt Initial (HTG) *</label>
                <input 
                    type="number" 
                    id="initialAmount" 
                    name="initialAmount" 
                    required
                    min="100"
                    step="0.01"
                    placeholder="1000.00"
                >
                <span class="error" id="initialAmountError"></span>
            </div>

            <button type="submit" class="btn-primary">Créer le Compte</button>
        </form>

        <div id="result" class="result hidden"></div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

### Solution CSS

```css
/* styles.css */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
}

.container {
    background: white;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
    max-width: 500px;
    width: 100%;
}

h1 {
    color: #333;
    margin-bottom: 1.5rem;
    text-align: center;
}

.form-group {
    margin-bottom: 1.5rem;
}

label {
    display: block;
    margin-bottom: 0.5rem;
    color: #555;
    font-weight: 500;
}

input, select {
    width: 100%;
    padding: 0.75rem;
    border: 2px solid #e0e0e0;
    border-radius: 5px;
    font-size: 1rem;
    transition: border-color 0.3s;
}

input:focus, select:focus {
    outline: none;
    border-color: #667eea;
}

input.invalid {
    border-color: #e74c3c;
}

input.valid {
    border-color: #27ae60;
}

.error {
    display: block;
    color: #e74c3c;
    font-size: 0.875rem;
    margin-top: 0.25rem;
    min-height: 1.25rem;
}

.btn-primary {
    width: 100%;
    padding: 1rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}

.btn-primary:active {
    transform: translateY(0);
}

.result {
    margin-top: 1.5rem;
    padding: 1rem;
    border-radius: 5px;
    text-align: center;
}

.result.success {
    background-color: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
}

.result.error {
    background-color: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
}

.hidden {
    display: none;
}

/* Responsive */
@media (max-width: 600px) {
    .container {
        padding: 1.5rem;
    }
    
    h1 {
        font-size: 1.5rem;
    }
}
```

### Solution JavaScript

```javascript
// script.js

// Validation rules
const validationRules = {
    fullName: {
        required: true,
        minLength: 3,
        message: 'Le nom doit contenir au moins 3 caractères'
    },
    email: {
        required: true,
        pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
        message: 'Veuillez entrer un email valide'
    },
    phone: {
        required: true,
        pattern: /^[0-9]{10}$/,
        message: 'Le téléphone doit contenir 10 chiffres'
    },
    accountType: {
        required: true,
        message: 'Veuillez sélectionner un type de compte'
    },
    initialAmount: {
        required: true,
        min: 100,
        message: 'Le montant minimum est de 100 HTG'
    }
};

// Get form elements
const form = document.getElementById('accountForm');
const resultDiv = document.getElementById('result');

// Validate single field
function validateField(fieldName, value) {
    const rules = validationRules[fieldName];
    
    if (rules.required && !value.trim()) {
        return { valid: false, message: 'Ce champ est requis' };
    }
    
    if (rules.minLength && value.length < rules.minLength) {
        return { valid: false, message: rules.message };
    }
    
    if (rules.pattern && !rules.pattern.test(value)) {
        return { valid: false, message: rules.message };
    }
    
    if (rules.min && parseFloat(value) < rules.min) {
        return { valid: false, message: rules.message };
    }
    
    return { valid: true, message: '' };
}

// Show error message
function showError(fieldName, message) {
    const errorElement = document.getElementById(`${fieldName}Error`);
    const inputElement = document.getElementById(fieldName);
    
    errorElement.textContent = message;
    inputElement.classList.add('invalid');
    inputElement.classList.remove('valid');
}

// Clear error message
function clearError(fieldName) {
    const errorElement = document.getElementById(`${fieldName}Error`);
    const inputElement = document.getElementById(fieldName);
    
    errorElement.textContent = '';
    inputElement.classList.remove('invalid');
    inputElement.classList.add('valid');
}

// Add real-time validation to each field
Object.keys(validationRules).forEach(fieldName => {
    const field = document.getElementById(fieldName);
    
    field.addEventListener('blur', () => {
        const validation = validateField(fieldName, field.value);
        if (!validation.valid) {
            showError(fieldName, validation.message);
        } else {
            clearError(fieldName);
        }
    });
    
    field.addEventListener('input', () => {
        const validation = validateField(fieldName, field.value);
        if (validation.valid) {
            clearError(fieldName);
        }
    });
});

// Handle form submission
form.addEventListener('submit', (e) => {
    e.preventDefault();
    
    // Validate all fields
    let isValid = true;
    const formData = {};
    
    Object.keys(validationRules).forEach(fieldName => {
        const field = document.getElementById(fieldName);
        const validation = validateField(fieldName, field.value);
        
        if (!validation.valid) {
            showError(fieldName, validation.message);
            isValid = false;
        } else {
            clearError(fieldName);
            formData[fieldName] = field.value;
        }
    });
    
    if (isValid) {
        // Simulate account creation
        createAccount(formData);
    }
});

// Simulate account creation (would be an API call in real app)
function createAccount(data) {
    resultDiv.classList.remove('hidden', 'error');
    resultDiv.classList.add('success');
    
    const accountNumber = `HTG${Date.now().toString().slice(-8)}`;
    
    resultDiv.innerHTML = `
        <h3>✓ Compte créé avec succès !</h3>
        <p><strong>Numéro de compte:</strong> ${accountNumber}</p>
        <p><strong>Titulaire:</strong> ${data.fullName}</p>
        <p><strong>Type:</strong> ${data.accountType}</p>
        <p><strong>Solde initial:</strong> ${parseFloat(data.initialAmount).toFixed(2)} HTG</p>
    `;
    
    // Reset form
    form.reset();
    
    // Clear validation classes
    document.querySelectorAll('input, select').forEach(field => {
        field.classList.remove('valid', 'invalid');
    });
}
```

---

## Problème 2 : Affichage Dynamique de la Liste des Transactions

### Énoncé

Créer une interface affichant une liste de transactions avec :
- Filtrage par type (Dépôt/Retrait/Virement)
- Tri par date ou montant
- Total dynamique

### Solution HTML

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Historique des Transactions</title>
    <link rel="stylesheet" href="transactions.css">
</head>
<body>
    <div class="container">
        <h1>Historique des Transactions</h1>
        
        <div class="controls">
            <div class="filter-group">
                <label for="typeFilter">Type:</label>
                <select id="typeFilter">
                    <option value="ALL">Tous</option>
                    <option value="DEPOT">Dépôt</option>
                    <option value="RETRAIT">Retrait</option>
                    <option value="VIREMENT">Virement</option>
                </select>
            </div>
            
            <div class="filter-group">
                <label for="sortBy">Trier par:</label>
                <select id="sortBy">
                    <option value="date">Date (récent)</option>
                    <option value="date-asc">Date (ancien)</option>
                    <option value="amount-desc">Montant (décroissant)</option>
                    <option value="amount-asc">Montant (croissant)</option>
                </select>
            </div>
        </div>
        
        <div class="summary">
            <div class="summary-item">
                <span>Total Dépôts:</span>
                <span id="totalDeposits" class="amount positive">0 HTG</span>
            </div>
            <div class="summary-item">
                <span>Total Retraits:</span>
                <span id="totalWithdrawals" class="amount negative">0 HTG</span>
            </div>
            <div class="summary-item">
                <span>Solde Net:</span>
                <span id="netBalance" class="amount">0 HTG</span>
            </div>
        </div>
        
        <div id="transactionsList"></div>
    </div>
    
    <script src="transactions.js"></script>
</body>
</html>
```

### Solution CSS

```css
/* transactions.css */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f5f7fa;
    padding: 2rem;
}

.container {
    max-width: 900px;
    margin: 0 auto;
    background: white;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
    color: #333;
    margin-bottom: 1.5rem;
}

.controls {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.5rem;
    flex-wrap: wrap;
}

.filter-group {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.filter-group label {
    font-weight: 500;
    color: #555;
}

select {
    padding: 0.5rem;
    border: 2px solid #e0e0e0;
    border-radius: 5px;
    font-size: 0.95rem;
    cursor: pointer;
}

.summary {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-bottom: 2rem;
    padding: 1rem;
    background: #f8f9fa;
    border-radius: 5px;
}

.summary-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.amount {
    font-weight: 600;
    font-size: 1.1rem;
}

.amount.positive {
    color: #27ae60;
}

.amount.negative {
    color: #e74c3c;
}

.transaction-card {
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 1rem;
    margin-bottom: 0.75rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: transform 0.2s, box-shadow 0.2s;
}

.transaction-card:hover {
    transform: translateX(5px);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.transaction-info {
    flex: 1;
}

.transaction-type {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.type-DEPOT {
    background-color: #d4edda;
    color: #155724;
}

.type-RETRAIT {
    background-color: #f8d7da;
    color: #721c24;
}

.type-VIREMENT {
    background-color: #d1ecf1;
    color: #0c5460;
}

.transaction-date {
    color: #888;
    font-size: 0.9rem;
}

.transaction-amount {
    font-size: 1.25rem;
    font-weight: 700;
}

.no-transactions {
    text-align: center;
    color: #888;
    padding: 2rem;
}
```

### Solution JavaScript

```javascript
// transactions.js

// Sample transaction data
const transactions = [
    { id: 1, type: 'DEPOT', amount: 5000, date: '2024-01-15T10:30:00', description: 'Dépôt initial' },
    { id: 2, type: 'RETRAIT', amount: 1000, date: '2024-01-16T14:20:00', description: 'Retrait guichet' },
    { id: 3, type: 'DEPOT', amount: 3000, date: '2024-01-18T09:15:00', description: 'Virement reçu' },
    { id: 4, type: 'VIREMENT', amount: 2000, date: '2024-01-20T11:45:00', description: 'Paiement facture' },
    { id: 5, type: 'RETRAIT', amount: 500, date: '2024-01-22T16:00:00', description: 'ATM retrait' },
    { id: 6, type: 'DEPOT', amount: 7500, date: '2024-01-25T08:30:00', description: 'Salaire' },
    { id: 7, type: 'RETRAIT', amount: 1500, date: '2024-01-26T13:10:00', description: 'Achat supermarché' },
    { id: 8, type: 'VIREMENT', amount: 3500, date: '2024-01-27T10:00:00', description: 'Paiement loyer' }
];

let filteredTransactions = [...transactions];

// Get DOM elements
const typeFilter = document.getElementById('typeFilter');
const sortBy = document.getElementById('sortBy');
const transactionsList = document.getElementById('transactionsList');
const totalDeposits = document.getElementById('totalDeposits');
const totalWithdrawals = document.getElementById('totalWithdrawals');
const netBalance = document.getElementById('netBalance');

// Format date
function formatDate(dateString) {
    const date = new Date(dateString);
    return new Intl.DateTimeFormat('fr-HT', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    }).format(date);
}

// Format amount
function formatAmount(amount) {
    return new Intl.NumberFormat('fr-HT', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    }).format(amount);
}

// Calculate summary statistics
function updateSummary() {
    const deposits = filteredTransactions
        .filter(t => t.type === 'DEPOT')
        .reduce((sum, t) => sum + t.amount, 0);
    
    const withdrawals = filteredTransactions
        .filter(t => t.type === 'RETRAIT' || t.type === 'VIREMENT')
        .reduce((sum, t) => sum + t.amount, 0);
    
    const net = deposits - withdrawals;
    
    totalDeposits.textContent = `${formatAmount(deposits)} HTG`;
    totalWithdrawals.textContent = `${formatAmount(withdrawals)} HTG`;
    netBalance.textContent = `${formatAmount(net)} HTG`;
    netBalance.className = `amount ${net >= 0 ? 'positive' : 'negative'}`;
}

// Render transactions
function renderTransactions() {
    if (filteredTransactions.length === 0) {
        transactionsList.innerHTML = '<div class="no-transactions">Aucune transaction trouvée</div>';
        return;
    }
    
    transactionsList.innerHTML = filteredTransactions.map(transaction => `
        <div class="transaction-card">
            <div class="transaction-info">
                <span class="transaction-type type-${transaction.type}">
                    ${transaction.type}
                </span>
                <p>${transaction.description}</p>
                <p class="transaction-date">${formatDate(transaction.date)}</p>
            </div>
            <div class="transaction-amount ${transaction.type === 'DEPOT' ? 'positive' : 'negative'}">
                ${transaction.type === 'DEPOT' ? '+' : '-'}${formatAmount(transaction.amount)} HTG
            </div>
        </div>
    `).join('');
    
    updateSummary();
}

// Filter transactions
function filterTransactions() {
    const type = typeFilter.value;
    const sort = sortBy.value;
    
    // Filter by type
    filteredTransactions = type === 'ALL' 
        ? [...transactions]
        : transactions.filter(t => t.type === type);
    
    // Sort
    switch(sort) {
        case 'date':
            filteredTransactions.sort((a, b) => new Date(b.date) - new Date(a.date));
            break;
        case 'date-asc':
            filteredTransactions.sort((a, b) => new Date(a.date) - new Date(b.date));
            break;
        case 'amount-desc':
            filteredTransactions.sort((a, b) => b.amount - a.amount);
            break;
        case 'amount-asc':
            filteredTransactions.sort((a, b) => a.amount - b.amount);
            break;
    }
    
    renderTransactions();
}

// Event listeners
typeFilter.addEventListener('change', filterTransactions);
sortBy.addEventListener('change', filterTransactions);

// Initial render
filterTransactions();
```

---

## Problème 3 : Calculatrice de Prêt Interactif

### Énoncé

Créer une calculatrice permettant de simuler un prêt bancaire avec :
- Montant du prêt
- Taux d'intérêt annuel
- Durée en mois
- Calcul de la mensualité et du coût total

### Solution HTML + JavaScript Complet

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Calculatrice de Prêt</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #3498db, #8e44ad);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        
        .calculator {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
            max-width: 500px;
            width: 100%;
        }
        
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 1.5rem;
        }
        
        .input-group {
            margin-bottom: 1.5rem;
        }
        
        label {
            display: block;
            margin-bottom: 0.5rem;
            color: #555;
            font-weight: 600;
        }
        
        .input-wrapper {
            position: relative;
        }
        
        input[type="range"] {
            width: 100%;
            margin-bottom: 0.5rem;
        }
        
        .value-display {
            display: flex;
            justify-content: space-between;
            font-size: 1.1rem;
            color: #3498db;
            font-weight: 700;
        }
        
        input[type="number"] {
            width: 100%;
            padding: 0.75rem;
            border: 2px solid #e0e0e0;
            border-radius: 5px;
            font-size: 1rem;
        }
        
        .results {
            background: #f8f9fa;
            padding: 1.5rem;
            border-radius: 10px;
            margin-top: 2rem;
        }
        
        .result-item {
            display: flex;
            justify-content: space-between;
            padding: 0.75rem 0;
            border-bottom: 1px solid #e0e0e0;
        }
        
        .result-item:last-child {
            border-bottom: none;
            margin-top: 0.5rem;
            padding-top: 1rem;
            border-top: 2px solid #3498db;
        }
        
        .result-label {
            font-weight: 500;
            color: #555;
        }
        
        .result-value {
            font-weight: 700;
            font-size: 1.2rem;
            color: #3498db;
        }
        
        .result-value.highlight {
            color: #27ae60;
            font-size: 1.5rem;
        }
        
        .chart-container {
            margin-top: 1.5rem;
            padding: 1rem;
            background: white;
            border-radius: 5px;
        }
        
        .chart-bar {
            display: flex;
            margin: 0.5rem 0;
            align-items: center;
        }
        
        .chart-label {
            width: 100px;
            font-size: 0.9rem;
            color: #555;
        }
        
        .chart-visual {
            flex: 1;
            height: 30px;
            border-radius: 5px;
            margin: 0 1rem;
            position: relative;
            overflow: hidden;
        }
        
        .chart-fill {
            height: 100%;
            border-radius: 5px;
            transition: width 0.3s ease;
        }
        
        .principal-bar {
            background: #3498db;
        }
        
        .interest-bar {
            background: #e74c3c;
        }
        
        .chart-value {
            min-width: 80px;
            text-align: right;
            font-weight: 600;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="calculator">
        <h1>💰 Calculatrice de Prêt</h1>
        
        <div class="input-group">
            <label for="loanAmount">Montant du Prêt</label>
            <div class="input-wrapper">
                <input type="range" id="loanAmount" min="10000" max="1000000" step="10000" value="100000">
                <div class="value-display">
                    <span id="loanAmountValue">100,000</span>
                    <span>HTG</span>
                </div>
            </div>
        </div>
        
        <div class="input-group">
            <label for="interestRate">Taux d'Intérêt Annuel (%)</label>
            <div class="input-wrapper">
                <input type="range" id="interestRate" min="1" max="20" step="0.1" value="8.5">
                <div class="value-display">
                    <span id="interestRateValue">8.5</span>
                    <span>%</span>
                </div>
            </div>
        </div>
        
        <div class="input-group">
            <label for="loanTerm">Durée (Mois)</label>
            <div class="input-wrapper">
                <input type="range" id="loanTerm" min="6" max="360" step="6" value="60">
                <div class="value-display">
                    <span id="loanTermValue">60</span>
                    <span>mois (<span id="yearsValue">5</span> ans)</span>
                </div>
            </div>
        </div>
        
        <div class="results">
            <div class="result-item">
                <span class="result-label">Mensualité:</span>
                <span class="result-value highlight" id="monthlyPayment">0 HTG</span>
            </div>
            <div class="result-item">
                <span class="result-label">Montant Total:</span>
                <span class="result-value" id="totalPayment">0 HTG</span>
            </div>
            <div class="result-item">
                <span class="result-label">Intérêts Totaux:</span>
                <span class="result-value" id="totalInterest">0 HTG</span>
            </div>
        </div>
        
        <div class="chart-container">
            <h3 style="margin-bottom: 1rem; color: #333;">Répartition</h3>
            <div class="chart-bar">
                <span class="chart-label">Principal:</span>
                <div class="chart-visual">
                    <div class="chart-fill principal-bar" id="principalBar"></div>
                </div>
                <span class="chart-value" id="principalValue">0 HTG</span>
            </div>
            <div class="chart-bar">
                <span class="chart-label">Intérêts:</span>
                <div class="chart-visual">
                    <div class="chart-fill interest-bar" id="interestBar"></div>
                </div>
                <span class="chart-value" id="interestValue">0 HTG</span>
            </div>
        </div>
    </div>
    
    <script>
        // Get all inputs
        const loanAmountInput = document.getElementById('loanAmount');
        const interestRateInput = document.getElementById('interestRate');
        const loanTermInput = document.getElementById('loanTerm');
        
        // Get display elements
        const loanAmountValue = document.getElementById('loanAmountValue');
        const interestRateValue = document.getElementById('interestRateValue');
        const loanTermValue = document.getElementById('loanTermValue');
        const yearsValue = document.getElementById('yearsValue');
        
        // Get result elements
        const monthlyPayment = document.getElementById('monthlyPayment');
        const totalPayment = document.getElementById('totalPayment');
        const totalInterest = document.getElementById('totalInterest');
        const principalBar = document.getElementById('principalBar');
        const interestBar = document.getElementById('interestBar');
        const principalValue = document.getElementById('principalValue');
        const interestValue = document.getElementById('interestValue');
        
        // Format number with commas
        function formatNumber(num) {
            return new Intl.NumberFormat('fr-HT', {
                minimumFractionDigits: 0,
                maximumFractionDigits: 0
            }).format(num);
        }
        
        // Calculate loan
        function calculateLoan() {
            const principal = parseFloat(loanAmountInput.value);
            const annualRate = parseFloat(interestRateInput.value);
            const months = parseInt(loanTermInput.value);
            
            // Update display values
            loanAmountValue.textContent = formatNumber(principal);
            interestRateValue.textContent = annualRate;
            loanTermValue.textContent = months;
            yearsValue.textContent = (months / 12).toFixed(1);
            
            // Calculate monthly interest rate
            const monthlyRate = annualRate / 100 / 12;
            
            // Calculate monthly payment using amortization formula
            // M = P * [r(1+r)^n] / [(1+r)^n - 1]
            const monthlyPaymentAmount = principal * 
                (monthlyRate * Math.pow(1 + monthlyRate, months)) / 
                (Math.pow(1 + monthlyRate, months) - 1);
            
            const totalPaymentAmount = monthlyPaymentAmount * months;
            const totalInterestAmount = totalPaymentAmount - principal;
            
            // Update results
            monthlyPayment.textContent = `${formatNumber(monthlyPaymentAmount)} HTG`;
            totalPayment.textContent = `${formatNumber(totalPaymentAmount)} HTG`;
            totalInterest.textContent = `${formatNumber(totalInterestAmount)} HTG`;
            
            // Update chart
            const principalPercentage = (principal / totalPaymentAmount) * 100;
            const interestPercentage = (totalInterestAmount / totalPaymentAmount) * 100;
            
            principalBar.style.width = `${principalPercentage}%`;
            interestBar.style.width = `${interestPercentage}%`;
            
            principalValue.textContent = `${formatNumber(principal)} HTG`;
            interestValue.textContent = `${formatNumber(totalInterestAmount)} HTG`;
        }
        
        // Add event listeners
        loanAmountInput.addEventListener('input', calculateLoan);
        interestRateInput.addEventListener('input', calculateLoan);
        loanTermInput.addEventListener('input', calculateLoan);
        
        // Initial calculation
        calculateLoan();
    </script>
</body>
</html>
```

---

## Problème 4 : Modal de Confirmation de Transaction

### Énoncé

Créer un modal réutilisable pour confirmer une transaction avant son exécution.

### Solution Complète

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Modal de Confirmation</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: Arial, sans-serif;
            padding: 2rem;
            background: #f5f7fa;
        }
        
        .container {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            padding: 2rem;
            border-radius: 10px;
        }
        
        h1 {
            margin-bottom: 1.5rem;
        }
        
        .btn {
            padding: 1rem 2rem;
            border: none;
            border-radius: 5px;
            font-size: 1rem;
            cursor: pointer;
            margin-right: 1rem;
            transition: transform 0.2s;
        }
        
        .btn:active {
            transform: scale(0.95);
        }
        
        .btn-danger {
            background: #e74c3c;
            color: white;
        }
        
        .btn-primary {
            background: #3498db;
            color: white;
        }
        
        /* Modal styles */
        .modal-overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5);
            z-index: 1000;
            animation: fadeIn 0.3s;
        }
        
        .modal-overlay.active {
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .modal {
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
            max-width: 500px;
            width: 90%;
            animation: slideUp 0.3s;
        }
        
        .modal-header {
            padding: 1.5rem;
            border-bottom: 1px solid #e0e0e0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .modal-header h2 {
            margin: 0;
            color: #333;
        }
        
        .close-btn {
            background: none;
            border: none;
            font-size: 1.5rem;
            cursor: pointer;
            color: #888;
        }
        
        .close-btn:hover {
            color: #333;
        }
        
        .modal-body {
            padding: 1.5rem;
        }
        
        .transaction-details {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 5px;
            margin: 1rem 0;
        }
        
        .detail-row {
            display: flex;
            justify-content: space-between;
            padding: 0.5rem 0;
            border-bottom: 1px solid #e0e0e0;
        }
        
        .detail-row:last-child {
            border-bottom: none;
        }
        
        .detail-label {
            font-weight: 600;
            color: #555;
        }
        
        .detail-value {
            color: #333;
        }
        
        .modal-footer {
            padding: 1.5rem;
            border-top: 1px solid #e0e0e0;
            display: flex;
            justify-content: flex-end;
            gap: 1rem;
        }
        
        .btn-secondary {
            background: #95a5a6;
            color: white;
        }
        
        .btn-success {
            background: #27ae60;
            color: white;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        @keyframes slideUp {
            from {
                transform: translateY(50px);
                opacity: 0;
            }
            to {
                transform: translateY(0);
                opacity: 1;
            }
        }
        
        .result-message {
            margin-top: 1rem;
            padding: 1rem;
            border-radius: 5px;
            display: none;
        }
        
        .result-message.success {
            background: #d4edda;
            color: #155724;
            display: block;
        }
        
        .result-message.error {
            background: #f8d7da;
            color: #721c24;
            display: block;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Effectuer une Transaction</h1>
        
        <button class="btn btn-primary" onclick="openModal('RETRAIT', 5000)">
            Retirer 5,000 HTG
        </button>
        
        <button class="btn btn-danger" onclick="openModal('VIREMENT', 10000)">
            Virement 10,000 HTG
        </button>
        
        <div id="resultMessage" class="result-message"></div>
    </div>
    
    <!-- Modal -->
    <div id="modalOverlay" class="modal-overlay">
        <div class="modal">
            <div class="modal-header">
                <h2>Confirmer la Transaction</h2>
                <button class="close-btn" onclick="closeModal()">&times;</button>
            </div>
            <div class="modal-body">
                <p>Veuillez vérifier les détails de votre transaction :</p>
                <div class="transaction-details">
                    <div class="detail-row">
                        <span class="detail-label">Type:</span>
                        <span class="detail-value" id="modalType"></span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Montant:</span>
                        <span class="detail-value" id="modalAmount"></span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Compte:</span>
                        <span class="detail-value">HTG12345678</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Date:</span>
                        <span class="detail-value" id="modalDate"></span>
                    </div>
                </div>
                <p style="color: #e74c3c; font-weight: 600;">
                    ⚠️ Cette action est irréversible
                </p>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" onclick="closeModal()">
                    Annuler
                </button>
                <button class="btn btn-success" onclick="confirmTransaction()">
                    Confirmer
                </button>
            </div>
        </div>
    </div>
    
    <script>
        let currentTransaction = null;
        
        function openModal(type, amount) {
            currentTransaction = { type, amount };
            
            document.getElementById('modalType').textContent = type;
            document.getElementById('modalAmount').textContent = `${formatNumber(amount)} HTG`;
            document.getElementById('modalDate').textContent = formatDate(new Date());
            
            document.getElementById('modalOverlay').classList.add('active');
        }
        
        function closeModal() {
            document.getElementById('modalOverlay').classList.remove('active');
            currentTransaction = null;
        }
        
        function confirmTransaction() {
            const resultMessage = document.getElementById('resultMessage');
            
            // Simulate transaction processing
            setTimeout(() => {
                resultMessage.className = 'result-message success';
                resultMessage.textContent = `✓ Transaction ${currentTransaction.type} de ${formatNumber(currentTransaction.amount)} HTG effectuée avec succès`;
                
                closeModal();
                
                // Hide message after 5 seconds
                setTimeout(() => {
                    resultMessage.className = 'result-message';
                }, 5000);
            }, 500);
        }
        
        function formatNumber(num) {
            return new Intl.NumberFormat('fr-HT').format(num);
        }
        
        function formatDate(date) {
            return new Intl.DateTimeFormat('fr-HT', {
                year: 'numeric',
                month: 'long',
                day: 'numeric',
                hour: '2-digit',
                minute: '2-digit'
            }).format(date);
        }
        
        // Close modal when clicking outside
        document.getElementById('modalOverlay').addEventListener('click', (e) => {
            if (e.target === e.currentTarget) {
                closeModal();
            }
        });
        
        // Close modal with Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                closeModal();
            }
        });
    </script>
</body>
</html>
```

---

## 📝 Checklist Frontend Basique

### HTML
- [ ] Sémantique correcte (header, main, section, article)
- [ ] Formulaires avec validation (required, pattern, type)
- [ ] Attributs d'accessibilité (aria-label, role)

### CSS
- [ ] Flexbox et Grid pour le layout
- [ ] Responsive design (media queries)
- [ ] Transitions et animations CSS
- [ ] Variables CSS (--primary-color)

### JavaScript
- [ ] Manipulation du DOM (querySelector, getElementById)
- [ ] Événements (addEventListener)
- [ ] Validation de formulaires
- [ ] Gestion d'état simple (variables)
- [ ] Fonctions pures et réutilisables

### Bonnes Pratiques
- [ ] Code lisible et commenté
- [ ] Séparation des préoccupations (HTML/CSS/JS)
- [ ] Gestion d'erreurs
- [ ] UX intuitive (feedback visuel, messages clairs)

---

**Prochaine étape :** Étude de cas Frontend Niveau Moyen (React/Vue, API calls, state management)
