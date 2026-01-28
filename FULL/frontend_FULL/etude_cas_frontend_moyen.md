# Étude de Cas Frontend — Niveau Moyen

## Guide de Préparation : React, State Management, API Integration

---

Ce document couvre les compétences frontend intermédiaires pour construire des applications bancaires avec React/Vue, intégration d'API REST, gestion d'état globale, et patterns avancés de composants.

---

## Problème 1 : Dashboard Bancaire avec React et Hooks

### Énoncé

Créer un tableau de bord bancaire avec React utilisant :
- Hooks modernes (useState, useEffect, useContext, useReducer)
- Appels API asynchrones
- Composants réutilisables
- Gestion d'état optimisée

### Solution : Architecture de l'Application

```
src/
├── components/
│   ├── AccountCard.jsx
│   ├── TransactionList.jsx
│   ├── QuickActions.jsx
│   └── LoadingSpinner.jsx
├── hooks/
│   ├── useAccount.js
│   └── useTransactions.js
├── context/
│   └── AuthContext.jsx
├── services/
│   └── api.js
├── App.jsx
└── index.js
```

### Solution : Service API

```javascript
// services/api.js

const API_BASE_URL = 'https://api.banque.example.ht';

// Generic fetch with error handling
async function apiFetch(endpoint, options = {}) {
    const token = localStorage.getItem('authToken');
    
    const config = {
        ...options,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': token ? `Bearer ${token}` : '',
            ...options.headers
        }
    };
    
    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, config);
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.message || 'Une erreur est survenue');
        }
        
        return await response.json();
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
}

// Account API
export const accountAPI = {
    getAccounts: () => apiFetch('/accounts'),
    
    getAccountById: (id) => apiFetch(`/accounts/${id}`),
    
    getBalance: (accountId) => apiFetch(`/accounts/${accountId}/balance`),
    
    transfer: (data) => apiFetch('/transactions/transfer', {
        method: 'POST',
        body: JSON.stringify(data)
    })
};

// Transaction API
export const transactionAPI = {
    getTransactions: (accountId, params = {}) => {
        const queryString = new URLSearchParams(params).toString();
        return apiFetch(`/accounts/${accountId}/transactions?${queryString}`);
    },
    
    getTransactionById: (id) => apiFetch(`/transactions/${id}`),
    
    createTransaction: (data) => apiFetch('/transactions', {
        method: 'POST',
        body: JSON.stringify(data)
    })
};
```

### Solution : Custom Hooks

```javascript
// hooks/useAccount.js

import { useState, useEffect } from 'react';
import { accountAPI } from '../services/api';

export function useAccount(accountId) {
    const [account, setAccount] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    useEffect(() => {
        let isMounted = true;
        
        async function fetchAccount() {
            try {
                setLoading(true);
                setError(null);
                const data = await accountAPI.getAccountById(accountId);
                
                if (isMounted) {
                    setAccount(data);
                }
            } catch (err) {
                if (isMounted) {
                    setError(err.message);
                }
            } finally {
                if (isMounted) {
                    setLoading(false);
                }
            }
        }
        
        if (accountId) {
            fetchAccount();
        }
        
        return () => {
            isMounted = false;
        };
    }, [accountId]);
    
    const refresh = async () => {
        try {
            setLoading(true);
            const data = await accountAPI.getAccountById(accountId);
            setAccount(data);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };
    
    return { account, loading, error, refresh };
}
```

```javascript
// hooks/useTransactions.js

import { useState, useEffect, useCallback } from 'react';
import { transactionAPI } from '../services/api';

export function useTransactions(accountId, initialFilters = {}) {
    const [transactions, setTransactions] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [filters, setFilters] = useState(initialFilters);
    const [pagination, setPagination] = useState({
        page: 1,
        pageSize: 10,
        total: 0
    });
    
    const fetchTransactions = useCallback(async () => {
        if (!accountId) return;
        
        try {
            setLoading(true);
            setError(null);
            
            const params = {
                ...filters,
                page: pagination.page,
                pageSize: pagination.pageSize
            };
            
            const data = await transactionAPI.getTransactions(accountId, params);
            
            setTransactions(data.transactions);
            setPagination(prev => ({
                ...prev,
                total: data.total
            }));
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    }, [accountId, filters, pagination.page, pagination.pageSize]);
    
    useEffect(() => {
        fetchTransactions();
    }, [fetchTransactions]);
    
    const updateFilters = (newFilters) => {
        setFilters(prev => ({ ...prev, ...newFilters }));
        setPagination(prev => ({ ...prev, page: 1 }));
    };
    
    const nextPage = () => {
        setPagination(prev => ({ ...prev, page: prev.page + 1 }));
    };
    
    const prevPage = () => {
        setPagination(prev => ({ 
            ...prev, 
            page: Math.max(1, prev.page - 1) 
        }));
    };
    
    return {
        transactions,
        loading,
        error,
        filters,
        pagination,
        updateFilters,
        nextPage,
        prevPage,
        refresh: fetchTransactions
    };
}
```

### Solution : Context pour l'Authentification

```javascript
// context/AuthContext.jsx

import React, { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    
    useEffect(() => {
        // Check for stored auth token
        const token = localStorage.getItem('authToken');
        const userData = localStorage.getItem('userData');
        
        if (token && userData) {
            setUser(JSON.parse(userData));
        }
        
        setLoading(false);
    }, []);
    
    const login = async (email, password) => {
        try {
            const response = await fetch('https://api.banque.example.ht/auth/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password })
            });
            
            if (!response.ok) {
                throw new Error('Identifiants invalides');
            }
            
            const data = await response.json();
            
            localStorage.setItem('authToken', data.token);
            localStorage.setItem('userData', JSON.stringify(data.user));
            
            setUser(data.user);
            return data;
        } catch (error) {
            throw error;
        }
    };
    
    const logout = () => {
        localStorage.removeItem('authToken');
        localStorage.removeItem('userData');
        setUser(null);
    };
    
    const value = {
        user,
        login,
        logout,
        isAuthenticated: !!user,
        loading
    };
    
    return (
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    );
}

export function useAuth() {
    const context = useContext(AuthContext);
    if (!context) {
        throw new Error('useAuth must be used within AuthProvider');
    }
    return context;
}
```

### Solution : Composants React

```javascript
// components/AccountCard.jsx

import React from 'react';
import { useAccount } from '../hooks/useAccount';
import LoadingSpinner from './LoadingSpinner';

export default function AccountCard({ accountId }) {
    const { account, loading, error, refresh } = useAccount(accountId);
    
    if (loading) return <LoadingSpinner />;
    
    if (error) {
        return (
            <div className="error-card">
                <p>Erreur: {error}</p>
                <button onClick={refresh}>Réessayer</button>
            </div>
        );
    }
    
    if (!account) return null;
    
    const formatCurrency = (amount) => {
        return new Intl.NumberFormat('fr-HT', {
            style: 'currency',
            currency: 'HTG'
        }).format(amount);
    };
    
    return (
        <div className="account-card">
            <div className="account-header">
                <h3>{account.type}</h3>
                <span className="account-number">{account.number}</span>
            </div>
            
            <div className="account-balance">
                <span className="label">Solde disponible</span>
                <span className="amount">
                    {formatCurrency(account.balance)}
                </span>
            </div>
            
            {account.type === 'COURANT' && account.overdraftLimit && (
                <div className="overdraft-info">
                    <span>Découvert autorisé:</span>
                    <span>{formatCurrency(account.overdraftLimit)}</span>
                </div>
            )}
            
            <button onClick={refresh} className="refresh-btn">
                🔄 Actualiser
            </button>
        </div>
    );
}
```

```javascript
// components/TransactionList.jsx

import React, { useState } from 'react';
import { useTransactions } from '../hooks/useTransactions';

export default function TransactionList({ accountId }) {
    const [filterType, setFilterType] = useState('ALL');
    
    const {
        transactions,
        loading,
        error,
        filters,
        pagination,
        updateFilters,
        nextPage,
        prevPage
    } = useTransactions(accountId, { type: filterType });
    
    const handleFilterChange = (type) => {
        setFilterType(type);
        updateFilters({ type: type === 'ALL' ? undefined : type });
    };
    
    const formatDate = (dateString) => {
        return new Intl.DateTimeFormat('fr-HT', {
            year: 'numeric',
            month: 'short',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        }).format(new Date(dateString));
    };
    
    const formatAmount = (amount, type) => {
        const formatted = new Intl.NumberFormat('fr-HT', {
            minimumFractionDigits: 2
        }).format(Math.abs(amount));
        
        const prefix = type === 'DEPOT' ? '+' : '-';
        return `${prefix}${formatted} HTG`;
    };
    
    const getTypeColor = (type) => {
        const colors = {
            DEPOT: 'green',
            RETRAIT: 'red',
            VIREMENT: 'blue'
        };
        return colors[type] || 'gray';
    };
    
    if (loading && transactions.length === 0) {
        return <div className="loading">Chargement des transactions...</div>;
    }
    
    return (
        <div className="transaction-list">
            <div className="transaction-header">
                <h2>Transactions</h2>
                <div className="filter-buttons">
                    {['ALL', 'DEPOT', 'RETRAIT', 'VIREMENT'].map(type => (
                        <button
                            key={type}
                            className={`filter-btn ${filterType === type ? 'active' : ''}`}
                            onClick={() => handleFilterChange(type)}
                        >
                            {type === 'ALL' ? 'Tous' : type}
                        </button>
                    ))}
                </div>
            </div>
            
            {error && <div className="error">{error}</div>}
            
            <div className="transactions">
                {transactions.length === 0 ? (
                    <div className="no-transactions">
                        Aucune transaction trouvée
                    </div>
                ) : (
                    transactions.map(transaction => (
                        <div key={transaction.id} className="transaction-item">
                            <div className="transaction-icon">
                                <span 
                                    className={`type-badge ${getTypeColor(transaction.type)}`}
                                >
                                    {transaction.type}
                                </span>
                            </div>
                            
                            <div className="transaction-details">
                                <p className="description">{transaction.description}</p>
                                <p className="date">{formatDate(transaction.date)}</p>
                            </div>
                            
                            <div className={`transaction-amount ${getTypeColor(transaction.type)}`}>
                                {formatAmount(transaction.amount, transaction.type)}
                            </div>
                        </div>
                    ))
                )}
            </div>
            
            {transactions.length > 0 && (
                <div className="pagination">
                    <button 
                        onClick={prevPage} 
                        disabled={pagination.page === 1}
                    >
                        Précédent
                    </button>
                    
                    <span>
                        Page {pagination.page} sur {Math.ceil(pagination.total / pagination.pageSize)}
                    </span>
                    
                    <button 
                        onClick={nextPage}
                        disabled={pagination.page * pagination.pageSize >= pagination.total}
                    >
                        Suivant
                    </button>
                </div>
            )}
        </div>
    );
}
```

### Solution : CSS Modules

```css
/* components/AccountCard.module.css */

.accountCard {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 15px;
    padding: 1.5rem;
    color: white;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    transition: transform 0.3s ease;
}

.accountCard:hover {
    transform: translateY(-5px);
}

.accountHeader {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
}

.accountNumber {
    font-size: 0.9rem;
    opacity: 0.9;
}

.accountBalance {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.label {
    font-size: 0.9rem;
    opacity: 0.9;
}

.amount {
    font-size: 2rem;
    font-weight: 700;
}

.overdraftInfo {
    display: flex;
    justify-content: space-between;
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid rgba(255, 255, 255, 0.3);
    font-size: 0.9rem;
}

.refreshBtn {
    margin-top: 1rem;
    background: rgba(255, 255, 255, 0.2);
    border: none;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 5px;
    cursor: pointer;
    transition: background 0.3s;
}

.refreshBtn:hover {
    background: rgba(255, 255, 255, 0.3);
}
```

### Solution : App.jsx Principal

```javascript
// App.jsx

import React from 'react';
import { AuthProvider, useAuth } from './context/AuthContext';
import AccountCard from './components/AccountCard';
import TransactionList from './components/TransactionList';
import './App.css';

function Dashboard() {
    const { user, logout } = useAuth();
    
    return (
        <div className="dashboard">
            <header className="dashboard-header">
                <h1>Bienvenue, {user?.name}</h1>
                <button onClick={logout} className="logout-btn">
                    Déconnexion
                </button>
            </header>
            
            <div className="accounts-grid">
                {user?.accounts?.map(accountId => (
                    <AccountCard key={accountId} accountId={accountId} />
                ))}
            </div>
            
            {user?.accounts?.[0] && (
                <div className="transactions-section">
                    <TransactionList accountId={user.accounts[0]} />
                </div>
            )}
        </div>
    );
}

function LoginForm() {
    const [email, setEmail] = React.useState('');
    const [password, setPassword] = React.useState('');
    const [error, setError] = React.useState('');
    const [loading, setLoading] = React.useState(false);
    
    const { login } = useAuth();
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setLoading(true);
        
        try {
            await login(email, password);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };
    
    return (
        <div className="login-container">
            <form onSubmit={handleSubmit} className="login-form">
                <h1>Connexion Bancaire</h1>
                
                {error && <div className="error-message">{error}</div>}
                
                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                />
                
                <input
                    type="password"
                    placeholder="Mot de passe"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
                
                <button type="submit" disabled={loading}>
                    {loading ? 'Connexion...' : 'Se connecter'}
                </button>
            </form>
        </div>
    );
}

function App() {
    return (
        <AuthProvider>
            <AppContent />
        </AuthProvider>
    );
}

function AppContent() {
    const { isAuthenticated, loading } = useAuth();
    
    if (loading) {
        return <div className="loading-screen">Chargement...</div>;
    }
    
    return isAuthenticated ? <Dashboard /> : <LoginForm />;
}

export default App;
```

---

## Problème 2 : Gestion d'État avec useReducer

### Énoncé

Implémenter un gestionnaire de formulaire complexe de virement avec validation en temps réel utilisant useReducer.

### Solution

```javascript
// components/TransferForm.jsx

import React, { useReducer } from 'react';

// Action types
const ACTIONS = {
    UPDATE_FIELD: 'UPDATE_FIELD',
    VALIDATE_FIELD: 'VALIDATE_FIELD',
    SUBMIT_START: 'SUBMIT_START',
    SUBMIT_SUCCESS: 'SUBMIT_SUCCESS',
    SUBMIT_ERROR: 'SUBMIT_ERROR',
    RESET: 'RESET'
};

// Validation functions
const validators = {
    sourceAccount: (value) => {
        if (!value) return 'Compte source requis';
        return null;
    },
    destinationAccount: (value) => {
        if (!value) return 'Compte destination requis';
        if (value.length < 10) return 'Numéro de compte invalide';
        return null;
    },
    amount: (value, state) => {
        if (!value || value <= 0) return 'Montant invalide';
        if (value > state.maxAmount) return `Montant maximum: ${state.maxAmount} HTG`;
        return null;
    },
    description: (value) => {
        if (!value) return 'Description requise';
        if (value.length < 3) return 'Description trop courte';
        return null;
    }
};

// Initial state
const initialState = {
    fields: {
        sourceAccount: '',
        destinationAccount: '',
        amount: '',
        description: ''
    },
    errors: {},
    touched: {},
    isSubmitting: false,
    submitError: null,
    submitSuccess: false,
    maxAmount: 50000
};

// Reducer
function transferReducer(state, action) {
    switch (action.type) {
        case ACTIONS.UPDATE_FIELD:
            return {
                ...state,
                fields: {
                    ...state.fields,
                    [action.field]: action.value
                },
                touched: {
                    ...state.touched,
                    [action.field]: true
                },
                errors: {
                    ...state.errors,
                    [action.field]: validators[action.field]?.(action.value, state) || null
                }
            };
        
        case ACTIONS.VALIDATE_FIELD:
            return {
                ...state,
                errors: {
                    ...state.errors,
                    [action.field]: validators[action.field]?.(
                        state.fields[action.field],
                        state
                    ) || null
                }
            };
        
        case ACTIONS.SUBMIT_START:
            return {
                ...state,
                isSubmitting: true,
                submitError: null,
                submitSuccess: false
            };
        
        case ACTIONS.SUBMIT_SUCCESS:
            return {
                ...state,
                isSubmitting: false,
                submitSuccess: true,
                fields: initialState.fields,
                touched: {},
                errors: {}
            };
        
        case ACTIONS.SUBMIT_ERROR:
            return {
                ...state,
                isSubmitting: false,
                submitError: action.error
            };
        
        case ACTIONS.RESET:
            return initialState;
        
        default:
            return state;
    }
}

export default function TransferForm() {
    const [state, dispatch] = useReducer(transferReducer, initialState);
    
    const handleChange = (field, value) => {
        dispatch({
            type: ACTIONS.UPDATE_FIELD,
            field,
            value
        });
    };
    
    const handleBlur = (field) => {
        dispatch({
            type: ACTIONS.VALIDATE_FIELD,
            field
        });
    };
    
    const isFormValid = () => {
        return Object.keys(state.fields).every(field => {
            const error = validators[field]?.(state.fields[field], state);
            return !error;
        });
    };
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        
        if (!isFormValid()) {
            // Validate all fields
            Object.keys(state.fields).forEach(field => {
                dispatch({ type: ACTIONS.VALIDATE_FIELD, field });
            });
            return;
        }
        
        dispatch({ type: ACTIONS.SUBMIT_START });
        
        try {
            // Simulate API call
            await new Promise(resolve => setTimeout(resolve, 2000));
            
            // In real app: await accountAPI.transfer(state.fields);
            
            dispatch({ type: ACTIONS.SUBMIT_SUCCESS });
        } catch (error) {
            dispatch({
                type: ACTIONS.SUBMIT_ERROR,
                error: error.message
            });
        }
    };
    
    const formatCurrency = (value) => {
        return new Intl.NumberFormat('fr-HT').format(value);
    };
    
    return (
        <div className="transfer-form-container">
            <h2>Effectuer un Virement</h2>
            
            {state.submitSuccess && (
                <div className="success-message">
                    ✓ Virement effectué avec succès!
                </div>
            )}
            
            {state.submitError && (
                <div className="error-message">
                    ✗ {state.submitError}
                </div>
            )}
            
            <form onSubmit={handleSubmit} className="transfer-form">
                <div className="form-group">
                    <label htmlFor="sourceAccount">Compte source</label>
                    <select
                        id="sourceAccount"
                        value={state.fields.sourceAccount}
                        onChange={(e) => handleChange('sourceAccount', e.target.value)}
                        onBlur={() => handleBlur('sourceAccount')}
                        className={state.errors.sourceAccount && state.touched.sourceAccount ? 'error' : ''}
                    >
                        <option value="">Sélectionner un compte</option>
                        <option value="HTG12345678">HTG12345678 - Compte Courant</option>
                        <option value="HTG87654321">HTG87654321 - Compte Épargne</option>
                    </select>
                    {state.errors.sourceAccount && state.touched.sourceAccount && (
                        <span className="error-text">{state.errors.sourceAccount}</span>
                    )}
                </div>
                
                <div className="form-group">
                    <label htmlFor="destinationAccount">Compte destination</label>
                    <input
                        id="destinationAccount"
                        type="text"
                        placeholder="Ex: HTG98765432"
                        value={state.fields.destinationAccount}
                        onChange={(e) => handleChange('destinationAccount', e.target.value)}
                        onBlur={() => handleBlur('destinationAccount')}
                        className={state.errors.destinationAccount && state.touched.destinationAccount ? 'error' : ''}
                    />
                    {state.errors.destinationAccount && state.touched.destinationAccount && (
                        <span className="error-text">{state.errors.destinationAccount}</span>
                    )}
                </div>
                
                <div className="form-group">
                    <label htmlFor="amount">
                        Montant (HTG)
                        <span className="max-amount">
                            Maximum: {formatCurrency(state.maxAmount)} HTG
                        </span>
                    </label>
                    <input
                        id="amount"
                        type="number"
                        step="0.01"
                        placeholder="0.00"
                        value={state.fields.amount}
                        onChange={(e) => handleChange('amount', parseFloat(e.target.value) || '')}
                        onBlur={() => handleBlur('amount')}
                        className={state.errors.amount && state.touched.amount ? 'error' : ''}
                    />
                    {state.errors.amount && state.touched.amount && (
                        <span className="error-text">{state.errors.amount}</span>
                    )}
                </div>
                
                <div className="form-group">
                    <label htmlFor="description">Description</label>
                    <textarea
                        id="description"
                        rows="3"
                        placeholder="Ex: Paiement loyer janvier"
                        value={state.fields.description}
                        onChange={(e) => handleChange('description', e.target.value)}
                        onBlur={() => handleBlur('description')}
                        className={state.errors.description && state.touched.description ? 'error' : ''}
                    />
                    {state.errors.description && state.touched.description && (
                        <span className="error-text">{state.errors.description}</span>
                    )}
                </div>
                
                <div className="form-actions">
                    <button
                        type="button"
                        onClick={() => dispatch({ type: ACTIONS.RESET })}
                        className="btn-secondary"
                    >
                        Annuler
                    </button>
                    <button
                        type="submit"
                        disabled={state.isSubmitting || !isFormValid()}
                        className="btn-primary"
                    >
                        {state.isSubmitting ? 'Traitement...' : 'Effectuer le virement'}
                    </button>
                </div>
            </form>
        </div>
    );
}
```

---

## Problème 3 : Optimisation des Performances

### Énoncé

Optimiser les performances d'une liste de 1000+ transactions avec :
- React.memo pour éviter les re-renders
- useMemo et useCallback
- Virtualisation de liste

### Solution : Liste Virtualisée

```javascript
// components/VirtualizedTransactionList.jsx

import React, { useMemo, useCallback } from 'react';
import { FixedSizeList as List } from 'react-window';

// Memoized transaction row component
const TransactionRow = React.memo(({ transaction, style }) => {
    const formatAmount = (amount, type) => {
        const formatted = new Intl.NumberFormat('fr-HT', {
            minimumFractionDigits: 2
        }).format(Math.abs(amount));
        const prefix = type === 'DEPOT' ? '+' : '-';
        return `${prefix}${formatted} HTG`;
    };
    
    const formatDate = (dateString) => {
        return new Intl.DateTimeFormat('fr-HT', {
            month: 'short',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        }).format(new Date(dateString));
    };
    
    return (
        <div style={style} className="transaction-row">
            <div className="transaction-type">
                <span className={`badge ${transaction.type.toLowerCase()}`}>
                    {transaction.type}
                </span>
            </div>
            <div className="transaction-description">
                {transaction.description}
            </div>
            <div className="transaction-date">
                {formatDate(transaction.date)}
            </div>
            <div className={`transaction-amount ${transaction.type.toLowerCase()}`}>
                {formatAmount(transaction.amount, transaction.type)}
            </div>
        </div>
    );
});

export default function VirtualizedTransactionList({ transactions }) {
    // Memoize filtered/sorted transactions
    const processedTransactions = useMemo(() => {
        return transactions.sort((a, b) => 
            new Date(b.date) - new Date(a.date)
        );
    }, [transactions]);
    
    // Memoize row renderer
    const Row = useCallback(({ index, style }) => {
        const transaction = processedTransactions[index];
        return <TransactionRow transaction={transaction} style={style} />;
    }, [processedTransactions]);
    
    return (
        <div className="virtualized-list">
            <List
                height={600}
                itemCount={processedTransactions.length}
                itemSize={80}
                width="100%"
            >
                {Row}
            </List>
        </div>
    );
}
```

---

## 📝 Checklist Frontend Moyen

### React/Vue
- [ ] Composants fonctionnels avec hooks
- [ ] Custom hooks pour logique réutilisable
- [ ] Context API pour état global
- [ ] useReducer pour état complexe
- [ ] Gestion du cycle de vie (useEffect)

### Performance
- [ ] React.memo pour éviter re-renders inutiles
- [ ] useMemo pour calculs coûteux
- [ ] useCallback pour fonctions stables
- [ ] Lazy loading de composants
- [ ] Virtualisation pour grandes listes

### API & Async
- [ ] Appels API avec fetch/axios
- [ ] Gestion des erreurs
- [ ] États de chargement
- [ ] Retry logic
- [ ] Annulation de requêtes (AbortController)

### Architecture
- [ ] Séparation des préoccupations
- [ ] Services API isolés
- [ ] Custom hooks métier
- [ ] Composants réutilisables
- [ ] Props validation (PropTypes/TypeScript)

---

**Prochaine étape :** Étude de cas Frontend Niveau Senior (Architecture, Testing, Performance avancée)
