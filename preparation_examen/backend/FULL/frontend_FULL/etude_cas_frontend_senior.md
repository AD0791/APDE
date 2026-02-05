# Étude de Cas Frontend — Niveau Senior

## Guide de Préparation : Architecture Avancée, Testing, Performance, Micro-Frontends

---

Ce document couvre les compétences frontend avancées pour architecturer, tester et optimiser des applications bancaires enterprise-grade avec des considérations de scalabilité, maintenabilité et performance.

---

## Problème 1 : Architecture Hexagonale (Ports & Adapters) pour Application Bancaire

### Énoncé

Concevoir une architecture frontend découplée permettant :
- Indépendance de l'infrastructure (API REST, GraphQL, WebSockets)
- Testabilité maximale
- Remplacement facile des dépendances externes
- Isolation de la logique métier

### Solution : Structure du Projet

```
src/
├── domain/                    # Couche domaine (logique métier pure)
│   ├── entities/
│   │   ├── Account.ts
│   │   ├── Transaction.ts
│   │   └── User.ts
│   ├── use-cases/
│   │   ├── TransferMoney.ts
│   │   ├── GetAccountBalance.ts
│   │   └── GetTransactionHistory.ts
│   ├── ports/                # Interfaces (contracts)
│   │   ├── IAccountRepository.ts
│   │   ├── ITransactionRepository.ts
│   │   ├── IAuthService.ts
│   │   └── INotificationService.ts
│   └── value-objects/
│       ├── Money.ts
│       └── AccountNumber.ts
├── adapters/                  # Couche infrastructure
│   ├── api/
│   │   ├── RestAccountRepository.ts
│   │   ├── GraphQLTransactionRepository.ts
│   │   └── WebSocketNotificationService.ts
│   ├── storage/
│   │   └── LocalStorageAuthService.ts
│   └── ui/
│       ├── react/
│       │   ├── components/
│       │   └── hooks/
│       └── vue/
│           ├── components/
│           └── composables/
├── application/               # Couche application
│   ├── services/
│   │   └── AccountService.ts
│   └── dto/
│       └── TransferDTO.ts
└── tests/
    ├── unit/
    ├── integration/
    └── e2e/
```

### Solution : Domain Layer (Entités et Value Objects)

```typescript
// domain/value-objects/Money.ts

export class Money {
    private constructor(
        private readonly amount: number,
        private readonly currency: string
    ) {
        if (amount < 0) {
            throw new Error('Amount cannot be negative');
        }
        if (!currency || currency.length !== 3) {
            throw new Error('Invalid currency code');
        }
    }
    
    static fromNumber(amount: number, currency: string = 'HTG'): Money {
        return new Money(amount, currency);
    }
    
    getAmount(): number {
        return this.amount;
    }
    
    getCurrency(): string {
        return this.currency;
    }
    
    add(other: Money): Money {
        if (this.currency !== other.currency) {
            throw new Error('Cannot add money with different currencies');
        }
        return new Money(this.amount + other.amount, this.currency);
    }
    
    subtract(other: Money): Money {
        if (this.currency !== other.currency) {
            throw new Error('Cannot subtract money with different currencies');
        }
        return new Money(this.amount - other.amount, this.currency);
    }
    
    isGreaterThan(other: Money): boolean {
        if (this.currency !== other.currency) {
            throw new Error('Cannot compare money with different currencies');
        }
        return this.amount > other.amount;
    }
    
    format(): string {
        return new Intl.NumberFormat('fr-HT', {
            style: 'currency',
            currency: this.currency
        }).format(this.amount);
    }
}
```

```typescript
// domain/entities/Account.ts

import { Money } from '../value-objects/Money';

export enum AccountType {
    CHECKING = 'CHECKING',
    SAVINGS = 'SAVINGS'
}

export interface AccountProps {
    id: string;
    accountNumber: string;
    type: AccountType;
    balance: Money;
    overdraftLimit?: Money;
    ownerId: string;
    createdAt: Date;
}

export class Account {
    private constructor(private props: AccountProps) {}
    
    static create(props: AccountProps): Account {
        return new Account(props);
    }
    
    static reconstitute(props: AccountProps): Account {
        return new Account(props);
    }
    
    getId(): string {
        return this.props.id;
    }
    
    getAccountNumber(): string {
        return this.props.accountNumber;
    }
    
    getBalance(): Money {
        return this.props.balance;
    }
    
    getType(): AccountType {
        return this.props.type;
    }
    
    canWithdraw(amount: Money): boolean {
        const availableBalance = this.props.overdraftLimit
            ? this.props.balance.add(this.props.overdraftLimit)
            : this.props.balance;
        
        return availableBalance.isGreaterThan(amount) || 
               availableBalance.getAmount() === amount.getAmount();
    }
    
    withdraw(amount: Money): void {
        if (!this.canWithdraw(amount)) {
            throw new Error('Insufficient funds');
        }
        this.props.balance = this.props.balance.subtract(amount);
    }
    
    deposit(amount: Money): void {
        this.props.balance = this.props.balance.add(amount);
    }
    
    toJSON(): AccountProps {
        return { ...this.props };
    }
}
```

### Solution : Use Cases (Logique Métier)

```typescript
// domain/ports/IAccountRepository.ts

import { Account } from '../entities/Account';

export interface IAccountRepository {
    findById(id: string): Promise<Account | null>;
    findByAccountNumber(accountNumber: string): Promise<Account | null>;
    save(account: Account): Promise<void>;
    findAllByOwnerId(ownerId: string): Promise<Account[]>;
}
```

```typescript
// domain/use-cases/TransferMoney.ts

import { IAccountRepository } from '../ports/IAccountRepository';
import { ITransactionRepository } from '../ports/ITransactionRepository';
import { Money } from '../value-objects/Money';
import { Transaction, TransactionType } from '../entities/Transaction';

export interface TransferMoneyRequest {
    sourceAccountId: string;
    destinationAccountId: string;
    amount: number;
    currency: string;
    description: string;
}

export interface TransferMoneyResponse {
    transactionId: string;
    success: boolean;
    message: string;
}

export class TransferMoneyUseCase {
    constructor(
        private readonly accountRepository: IAccountRepository,
        private readonly transactionRepository: ITransactionRepository
    ) {}
    
    async execute(request: TransferMoneyRequest): Promise<TransferMoneyResponse> {
        // Validation
        if (request.amount <= 0) {
            return {
                transactionId: '',
                success: false,
                message: 'Transfer amount must be positive'
            };
        }
        
        if (request.sourceAccountId === request.destinationAccountId) {
            return {
                transactionId: '',
                success: false,
                message: 'Cannot transfer to the same account'
            };
        }
        
        // Load accounts
        const sourceAccount = await this.accountRepository.findById(
            request.sourceAccountId
        );
        const destinationAccount = await this.accountRepository.findById(
            request.destinationAccountId
        );
        
        if (!sourceAccount) {
            return {
                transactionId: '',
                success: false,
                message: 'Source account not found'
            };
        }
        
        if (!destinationAccount) {
            return {
                transactionId: '',
                success: false,
                message: 'Destination account not found'
            };
        }
        
        const transferAmount = Money.fromNumber(request.amount, request.currency);
        
        // Check if withdrawal is possible
        if (!sourceAccount.canWithdraw(transferAmount)) {
            return {
                transactionId: '',
                success: false,
                message: 'Insufficient funds'
            };
        }
        
        // Execute transfer
        try {
            sourceAccount.withdraw(transferAmount);
            destinationAccount.deposit(transferAmount);
            
            // Save changes
            await this.accountRepository.save(sourceAccount);
            await this.accountRepository.save(destinationAccount);
            
            // Create transaction record
            const transaction = Transaction.create({
                id: this.generateId(),
                accountId: request.sourceAccountId,
                type: TransactionType.TRANSFER,
                amount: transferAmount,
                description: request.description,
                destinationAccountId: request.destinationAccountId,
                timestamp: new Date()
            });
            
            await this.transactionRepository.save(transaction);
            
            return {
                transactionId: transaction.getId(),
                success: true,
                message: 'Transfer successful'
            };
        } catch (error) {
            return {
                transactionId: '',
                success: false,
                message: `Transfer failed: ${error.message}`
            };
        }
    }
    
    private generateId(): string {
        return `TXN${Date.now()}${Math.random().toString(36).substring(2, 9)}`;
    }
}
```

### Solution : Adapters (Infrastructure)

```typescript
// adapters/api/RestAccountRepository.ts

import { Account, AccountType } from '../../domain/entities/Account';
import { IAccountRepository } from '../../domain/ports/IAccountRepository';
import { Money } from '../../domain/value-objects/Money';

interface AccountDTO {
    id: string;
    accountNumber: string;
    type: string;
    balance: number;
    currency: string;
    overdraftLimit?: number;
    ownerId: string;
    createdAt: string;
}

export class RestAccountRepository implements IAccountRepository {
    constructor(private readonly apiBaseUrl: string) {}
    
    async findById(id: string): Promise<Account | null> {
        try {
            const response = await fetch(`${this.apiBaseUrl}/accounts/${id}`, {
                headers: this.getAuthHeaders()
            });
            
            if (response.status === 404) {
                return null;
            }
            
            if (!response.ok) {
                throw new Error('Failed to fetch account');
            }
            
            const dto: AccountDTO = await response.json();
            return this.toDomain(dto);
        } catch (error) {
            console.error('Error fetching account:', error);
            throw error;
        }
    }
    
    async findByAccountNumber(accountNumber: string): Promise<Account | null> {
        try {
            const response = await fetch(
                `${this.apiBaseUrl}/accounts?accountNumber=${accountNumber}`,
                { headers: this.getAuthHeaders() }
            );
            
            if (!response.ok) {
                throw new Error('Failed to fetch account');
            }
            
            const dtos: AccountDTO[] = await response.json();
            return dtos.length > 0 ? this.toDomain(dtos[0]) : null;
        } catch (error) {
            console.error('Error fetching account:', error);
            throw error;
        }
    }
    
    async save(account: Account): Promise<void> {
        try {
            const dto = this.toDTO(account);
            const response = await fetch(
                `${this.apiBaseUrl}/accounts/${account.getId()}`,
                {
                    method: 'PUT',
                    headers: {
                        ...this.getAuthHeaders(),
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(dto)
                }
            );
            
            if (!response.ok) {
                throw new Error('Failed to save account');
            }
        } catch (error) {
            console.error('Error saving account:', error);
            throw error;
        }
    }
    
    async findAllByOwnerId(ownerId: string): Promise<Account[]> {
        try {
            const response = await fetch(
                `${this.apiBaseUrl}/accounts?ownerId=${ownerId}`,
                { headers: this.getAuthHeaders() }
            );
            
            if (!response.ok) {
                throw new Error('Failed to fetch accounts');
            }
            
            const dtos: AccountDTO[] = await response.json();
            return dtos.map(dto => this.toDomain(dto));
        } catch (error) {
            console.error('Error fetching accounts:', error);
            throw error;
        }
    }
    
    private toDomain(dto: AccountDTO): Account {
        return Account.reconstitute({
            id: dto.id,
            accountNumber: dto.accountNumber,
            type: dto.type as AccountType,
            balance: Money.fromNumber(dto.balance, dto.currency),
            overdraftLimit: dto.overdraftLimit 
                ? Money.fromNumber(dto.overdraftLimit, dto.currency)
                : undefined,
            ownerId: dto.ownerId,
            createdAt: new Date(dto.createdAt)
        });
    }
    
    private toDTO(account: Account): AccountDTO {
        const props = account.toJSON();
        return {
            id: props.id,
            accountNumber: props.accountNumber,
            type: props.type,
            balance: props.balance.getAmount(),
            currency: props.balance.getCurrency(),
            overdraftLimit: props.overdraftLimit?.getAmount(),
            ownerId: props.ownerId,
            createdAt: props.createdAt.toISOString()
        };
    }
    
    private getAuthHeaders(): Record<string, string> {
        const token = localStorage.getItem('authToken');
        return token ? { 'Authorization': `Bearer ${token}` } : {};
    }
}
```

---

## Problème 2 : Testing Complet (Unit, Integration, E2E)

### Énoncé

Mettre en place une stratégie de test complète couvrant :
- Tests unitaires de la logique métier
- Tests d'intégration des composants React
- Tests E2E avec Playwright/Cypress

### Solution : Tests Unitaires (Jest)

```typescript
// tests/unit/domain/use-cases/TransferMoney.test.ts

import { TransferMoneyUseCase } from '../../../../src/domain/use-cases/TransferMoney';
import { Account, AccountType } from '../../../../src/domain/entities/Account';
import { Money } from '../../../../src/domain/value-objects/Money';
import { IAccountRepository } from '../../../../src/domain/ports/IAccountRepository';
import { ITransactionRepository } from '../../../../src/domain/ports/ITransactionRepository';

// Mock implementations
class MockAccountRepository implements IAccountRepository {
    private accounts: Map<string, Account> = new Map();
    
    async findById(id: string): Promise<Account | null> {
        return this.accounts.get(id) || null;
    }
    
    async findByAccountNumber(accountNumber: string): Promise<Account | null> {
        return Array.from(this.accounts.values()).find(
            acc => acc.getAccountNumber() === accountNumber
        ) || null;
    }
    
    async save(account: Account): Promise<void> {
        this.accounts.set(account.getId(), account);
    }
    
    async findAllByOwnerId(ownerId: string): Promise<Account[]> {
        return Array.from(this.accounts.values()).filter(
            acc => acc.toJSON().ownerId === ownerId
        );
    }
    
    seed(accounts: Account[]): void {
        accounts.forEach(acc => this.accounts.set(acc.getId(), acc));
    }
}

class MockTransactionRepository implements ITransactionRepository {
    private transactions: any[] = [];
    
    async save(transaction: any): Promise<void> {
        this.transactions.push(transaction);
    }
    
    getTransactions() {
        return this.transactions;
    }
}

describe('TransferMoneyUseCase', () => {
    let useCase: TransferMoneyUseCase;
    let accountRepository: MockAccountRepository;
    let transactionRepository: MockTransactionRepository;
    
    beforeEach(() => {
        accountRepository = new MockAccountRepository();
        transactionRepository = new MockTransactionRepository();
        useCase = new TransferMoneyUseCase(accountRepository, transactionRepository);
    });
    
    describe('Successful transfer', () => {
        it('should transfer money between accounts', async () => {
            // Arrange
            const sourceAccount = Account.create({
                id: 'ACC001',
                accountNumber: 'HTG12345678',
                type: AccountType.CHECKING,
                balance: Money.fromNumber(10000, 'HTG'),
                ownerId: 'USER001',
                createdAt: new Date()
            });
            
            const destinationAccount = Account.create({
                id: 'ACC002',
                accountNumber: 'HTG87654321',
                type: AccountType.SAVINGS,
                balance: Money.fromNumber(5000, 'HTG'),
                ownerId: 'USER002',
                createdAt: new Date()
            });
            
            accountRepository.seed([sourceAccount, destinationAccount]);
            
            // Act
            const result = await useCase.execute({
                sourceAccountId: 'ACC001',
                destinationAccountId: 'ACC002',
                amount: 3000,
                currency: 'HTG',
                description: 'Test transfer'
            });
            
            // Assert
            expect(result.success).toBe(true);
            expect(result.transactionId).toBeTruthy();
            
            const updatedSource = await accountRepository.findById('ACC001');
            const updatedDestination = await accountRepository.findById('ACC002');
            
            expect(updatedSource?.getBalance().getAmount()).toBe(7000);
            expect(updatedDestination?.getBalance().getAmount()).toBe(8000);
            
            expect(transactionRepository.getTransactions()).toHaveLength(1);
        });
    });
    
    describe('Validation errors', () => {
        it('should reject negative amount', async () => {
            const result = await useCase.execute({
                sourceAccountId: 'ACC001',
                destinationAccountId: 'ACC002',
                amount: -100,
                currency: 'HTG',
                description: 'Invalid transfer'
            });
            
            expect(result.success).toBe(false);
            expect(result.message).toContain('positive');
        });
        
        it('should reject transfer to same account', async () => {
            const result = await useCase.execute({
                sourceAccountId: 'ACC001',
                destinationAccountId: 'ACC001',
                amount: 100,
                currency: 'HTG',
                description: 'Invalid transfer'
            });
            
            expect(result.success).toBe(false);
            expect(result.message).toContain('same account');
        });
    });
    
    describe('Business rule violations', () => {
        it('should reject transfer with insufficient funds', async () => {
            const sourceAccount = Account.create({
                id: 'ACC001',
                accountNumber: 'HTG12345678',
                type: AccountType.CHECKING,
                balance: Money.fromNumber(1000, 'HTG'),
                ownerId: 'USER001',
                createdAt: new Date()
            });
            
            const destinationAccount = Account.create({
                id: 'ACC002',
                accountNumber: 'HTG87654321',
                type: AccountType.SAVINGS,
                balance: Money.fromNumber(5000, 'HTG'),
                ownerId: 'USER002',
                createdAt: new Date()
            });
            
            accountRepository.seed([sourceAccount, destinationAccount]);
            
            const result = await useCase.execute({
                sourceAccountId: 'ACC001',
                destinationAccountId: 'ACC002',
                amount: 5000,
                currency: 'HTG',
                description: 'Overdraft attempt'
            });
            
            expect(result.success).toBe(false);
            expect(result.message).toContain('Insufficient funds');
        });
    });
});
```

### Solution : Tests d'Intégration React (React Testing Library)

```typescript
// tests/integration/components/TransferForm.test.tsx

import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import '@testing-library/jest-dom';
import { TransferForm } from '../../../src/adapters/ui/react/components/TransferForm';
import { TransferMoneyUseCase } from '../../../src/domain/use-cases/TransferMoney';

// Mock use case
jest.mock('../../../src/domain/use-cases/TransferMoney');

describe('TransferForm Integration Tests', () => {
    let mockExecute: jest.Mock;
    
    beforeEach(() => {
        mockExecute = jest.fn();
        (TransferMoneyUseCase as jest.Mock).mockImplementation(() => ({
            execute: mockExecute
        }));
    });
    
    it('should render all form fields', () => {
        render(<TransferForm />);
        
        expect(screen.getByLabelText(/compte source/i)).toBeInTheDocument();
        expect(screen.getByLabelText(/compte destination/i)).toBeInTheDocument();
        expect(screen.getByLabelText(/montant/i)).toBeInTheDocument();
        expect(screen.getByLabelText(/description/i)).toBeInTheDocument();
        expect(screen.getByRole('button', { name: /effectuer/i })).toBeInTheDocument();
    });
    
    it('should show validation errors for empty fields', async () => {
        render(<TransferForm />);
        
        const submitButton = screen.getByRole('button', { name: /effectuer/i });
        fireEvent.click(submitButton);
        
        await waitFor(() => {
            expect(screen.getByText(/compte source requis/i)).toBeInTheDocument();
        });
    });
    
    it('should show error for amount exceeding limit', async () => {
        render(<TransferForm />);
        
        const amountInput = screen.getByLabelText(/montant/i);
        await userEvent.type(amountInput, '100000');
        
        fireEvent.blur(amountInput);
        
        await waitFor(() => {
            expect(screen.getByText(/montant maximum/i)).toBeInTheDocument();
        });
    });
    
    it('should successfully submit valid form', async () => {
        mockExecute.mockResolvedValue({
            success: true,
            transactionId: 'TXN123',
            message: 'Transfer successful'
        });
        
        render(<TransferForm />);
        
        // Fill form
        const sourceSelect = screen.getByLabelText(/compte source/i);
        const destinationInput = screen.getByLabelText(/compte destination/i);
        const amountInput = screen.getByLabelText(/montant/i);
        const descriptionInput = screen.getByLabelText(/description/i);
        
        await userEvent.selectOptions(sourceSelect, 'HTG12345678');
        await userEvent.type(destinationInput, 'HTG87654321');
        await userEvent.type(amountInput, '5000');
        await userEvent.type(descriptionInput, 'Test payment');
        
        // Submit
        const submitButton = screen.getByRole('button', { name: /effectuer/i });
        fireEvent.click(submitButton);
        
        // Assert
        await waitFor(() => {
            expect(mockExecute).toHaveBeenCalledWith({
                sourceAccountId: expect.any(String),
                destinationAccountId: 'HTG87654321',
                amount: 5000,
                currency: 'HTG',
                description: 'Test payment'
            });
        });
        
        await waitFor(() => {
            expect(screen.getByText(/virement effectué avec succès/i)).toBeInTheDocument();
        });
    });
    
    it('should display error message when transfer fails', async () => {
        mockExecute.mockResolvedValue({
            success: false,
            transactionId: '',
            message: 'Insufficient funds'
        });
        
        render(<TransferForm />);
        
        // Fill and submit form
        const sourceSelect = screen.getByLabelText(/compte source/i);
        const destinationInput = screen.getByLabelText(/compte destination/i);
        const amountInput = screen.getByLabelText(/montant/i);
        const descriptionInput = screen.getByLabelText(/description/i);
        
        await userEvent.selectOptions(sourceSelect, 'HTG12345678');
        await userEvent.type(destinationInput, 'HTG87654321');
        await userEvent.type(amountInput, '50000');
        await userEvent.type(descriptionInput, 'Large payment');
        
        const submitButton = screen.getByRole('button', { name: /effectuer/i });
        fireEvent.click(submitButton);
        
        await waitFor(() => {
            expect(screen.getByText(/insufficient funds/i)).toBeInTheDocument();
        });
    });
});
```

### Solution : Tests E2E (Playwright)

```typescript
// tests/e2e/transfer-flow.spec.ts

import { test, expect } from '@playwright/test';

test.describe('Money Transfer Flow', () => {
    test.beforeEach(async ({ page }) => {
        // Login
        await page.goto('http://localhost:3000/login');
        await page.fill('input[name="email"]', 'test@example.ht');
        await page.fill('input[name="password"]', 'password123');
        await page.click('button[type="submit"]');
        
        // Wait for dashboard
        await expect(page).toHaveURL(/.*dashboard/);
    });
    
    test('should complete a successful transfer', async ({ page }) => {
        // Navigate to transfer page
        await page.click('text=Effectuer un virement');
        await expect(page).toHaveURL(/.*transfer/);
        
        // Fill transfer form
        await page.selectOption('select[name="sourceAccount"]', 'HTG12345678');
        await page.fill('input[name="destinationAccount"]', 'HTG87654321');
        await page.fill('input[name="amount"]', '5000');
        await page.fill('textarea[name="description"]', 'E2E test payment');
        
        // Take screenshot before submission
        await page.screenshot({ path: 'screenshots/transfer-form-filled.png' });
        
        // Submit form
        await page.click('button:has-text("Effectuer le virement")');
        
        // Wait for success message
        await expect(page.locator('.success-message')).toBeVisible();
        await expect(page.locator('.success-message')).toContainText(/virement effectué/i);
        
        // Verify transaction appears in history
        await page.click('text=Historique');
        await expect(page.locator('.transaction-list')).toContainText('E2E test payment');
        
        // Take screenshot after success
        await page.screenshot({ path: 'screenshots/transfer-success.png' });
    });
    
    test('should show error for insufficient funds', async ({ page }) => {
        await page.click('text=Effectuer un virement');
        
        await page.selectOption('select[name="sourceAccount"]', 'HTG12345678');
        await page.fill('input[name="destinationAccount"]', 'HTG87654321');
        await page.fill('input[name="amount"]', '999999');
        await page.fill('textarea[name="description"]', 'Overdraft test');
        
        await page.click('button:has-text("Effectuer le virement")');
        
        await expect(page.locator('.error-message')).toBeVisible();
        await expect(page.locator('.error-message')).toContainText(/insufficient funds/i);
    });
    
    test('should validate form fields', async ({ page }) => {
        await page.click('text=Effectuer un virement');
        
        // Try to submit without filling
        await page.click('button:has-text("Effectuer le virement")');
        
        // Check validation errors
        await expect(page.locator('text=Compte source requis')).toBeVisible();
        await expect(page.locator('text=Compte destination requis')).toBeVisible();
        await expect(page.locator('text=Montant invalide')).toBeVisible();
    });
    
    test('should prevent transfer to same account', async ({ page }) => {
        await page.click('text=Effectuer un virement');
        
        await page.selectOption('select[name="sourceAccount"]', 'HTG12345678');
        await page.fill('input[name="destinationAccount"]', 'HTG12345678');
        await page.fill('input[name="amount"]', '1000');
        await page.fill('textarea[name="description"]', 'Same account test');
        
        await page.click('button:has-text("Effectuer le virement")');
        
        await expect(page.locator('.error-message')).toBeVisible();
        await expect(page.locator('.error-message')).toContainText(/same account/i);
    });
});
```

---

## Problème 3 : Performance Monitoring & Optimization

### Énoncé

Mettre en place un système de monitoring de performance avec :
- Core Web Vitals tracking
- Custom performance metrics
- Error tracking
- User analytics

### Solution : Performance Monitoring Service

```typescript
// services/PerformanceMonitor.ts

interface PerformanceMetrics {
    FCP: number;  // First Contentful Paint
    LCP: number;  // Largest Contentful Paint
    FID: number;  // First Input Delay
    CLS: number;  // Cumulative Layout Shift
    TTFB: number; // Time to First Byte
}

interface CustomMetric {
    name: string;
    value: number;
    timestamp: number;
    metadata?: Record<string, any>;
}

export class PerformanceMonitor {
    private static instance: PerformanceMonitor;
    private metrics: Map<string, CustomMetric[]> = new Map();
    private observer: PerformanceObserver | null = null;
    
    private constructor() {
        this.initWebVitalsTracking();
        this.initNavigationTracking();
        this.initResourceTracking();
    }
    
    static getInstance(): PerformanceMonitor {
        if (!PerformanceMonitor.instance) {
            PerformanceMonitor.instance = new PerformanceMonitor();
        }
        return PerformanceMonitor.instance;
    }
    
    private initWebVitalsTracking(): void {
        // Track FCP
        this.observeEntry('paint', (entries) => {
            const fcp = entries.find(e => e.name === 'first-contentful-paint');
            if (fcp) {
                this.recordMetric('FCP', fcp.startTime);
                this.sendToAnalytics('web_vitals', { FCP: fcp.startTime });
            }
        });
        
        // Track LCP
        this.observeEntry('largest-contentful-paint', (entries) => {
            const lcp = entries[entries.length - 1];
            if (lcp) {
                this.recordMetric('LCP', lcp.startTime);
                this.sendToAnalytics('web_vitals', { LCP: lcp.startTime });
            }
        });
        
        // Track FID
        this.observeEntry('first-input', (entries) => {
            const fid = entries[0];
            if (fid && 'processingStart' in fid) {
                const delay = fid.processingStart - fid.startTime;
                this.recordMetric('FID', delay);
                this.sendToAnalytics('web_vitals', { FID: delay });
            }
        });
        
        // Track CLS
        this.observeEntry('layout-shift', (entries) => {
            let cls = 0;
            entries.forEach(entry => {
                if ('hadRecentInput' in entry && !entry.hadRecentInput) {
                    cls += entry.value;
                }
            });
            this.recordMetric('CLS', cls);
            this.sendToAnalytics('web_vitals', { CLS: cls });
        });
    }
    
    private initNavigationTracking(): void {
        if (window.performance && window.performance.timing) {
            window.addEventListener('load', () => {
                setTimeout(() => {
                    const timing = window.performance.timing;
                    const ttfb = timing.responseStart - timing.requestStart;
                    const domContentLoaded = timing.domContentLoadedEventEnd - timing.navigationStart;
                    const loadComplete = timing.loadEventEnd - timing.navigationStart;
                    
                    this.recordMetric('TTFB', ttfb);
                    this.recordMetric('DOMContentLoaded', domContentLoaded);
                    this.recordMetric('LoadComplete', loadComplete);
                    
                    this.sendToAnalytics('navigation', {
                        TTFB: ttfb,
                        DOMContentLoaded: domContentLoaded,
                        LoadComplete: loadComplete
                    });
                }, 0);
            });
        }
    }
    
    private initResourceTracking(): void {
        this.observeEntry('resource', (entries) => {
            entries.forEach(entry => {
                if (entry.duration > 1000) {  // Track slow resources (>1s)
                    this.recordMetric(`SlowResource:${entry.name}`, entry.duration);
                    this.sendToAnalytics('slow_resource', {
                        url: entry.name,
                        duration: entry.duration,
                        type: entry.initiatorType
                    });
                }
            });
        });
    }
    
    private observeEntry(
        type: string,
        callback: (entries: PerformanceEntry[]) => void
    ): void {
        try {
            const observer = new PerformanceObserver((list) => {
                callback(list.getEntries());
            });
            observer.observe({ type, buffered: true });
        } catch (e) {
            console.warn(`PerformanceObserver not supported for type: ${type}`);
        }
    }
    
    recordMetric(name: string, value: number, metadata?: Record<string, any>): void {
        const metric: CustomMetric = {
            name,
            value,
            timestamp: Date.now(),
            metadata
        };
        
        if (!this.metrics.has(name)) {
            this.metrics.set(name, []);
        }
        this.metrics.get(name)!.push(metric);
        
        // Log to console in development
        if (process.env.NODE_ENV === 'development') {
            console.log(`[Performance] ${name}: ${value.toFixed(2)}ms`, metadata);
        }
    }
    
    markStart(name: string): void {
        performance.mark(`${name}-start`);
    }
    
    markEnd(name: string): void {
        performance.mark(`${name}-end`);
        try {
            performance.measure(name, `${name}-start`, `${name}-end`);
            const measure = performance.getEntriesByName(name, 'measure')[0];
            this.recordMetric(name, measure.duration);
        } catch (e) {
            console.warn(`Failed to measure ${name}`, e);
        }
    }
    
    getMetrics(): Map<string, CustomMetric[]> {
        return new Map(this.metrics);
    }
    
    getMetricsSummary(name: string): {
        count: number;
        avg: number;
        min: number;
        max: number;
        p50: number;
        p95: number;
        p99: number;
    } | null {
        const metricData = this.metrics.get(name);
        if (!metricData || metricData.length === 0) {
            return null;
        }
        
        const values = metricData.map(m => m.value).sort((a, b) => a - b);
        const sum = values.reduce((a, b) => a + b, 0);
        
        return {
            count: values.length,
            avg: sum / values.length,
            min: values[0],
            max: values[values.length - 1],
            p50: this.percentile(values, 50),
            p95: this.percentile(values, 95),
            p99: this.percentile(values, 99)
        };
    }
    
    private percentile(sortedArray: number[], p: number): number {
        const index = Math.ceil((p / 100) * sortedArray.length) - 1;
        return sortedArray[Math.max(0, index)];
    }
    
    private sendToAnalytics(eventName: string, data: any): void {
        // Send to your analytics service (Google Analytics, Mixpanel, etc.)
        if (typeof window.gtag === 'function') {
            window.gtag('event', eventName, data);
        }
        
        // Send to custom backend
        if (process.env.REACT_APP_ANALYTICS_URL) {
            fetch(process.env.REACT_APP_ANALYTICS_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    event: eventName,
                    data,
                    timestamp: Date.now(),
                    userAgent: navigator.userAgent,
                    url: window.location.href
                })
            }).catch(err => console.error('Analytics error:', err));
        }
    }
}

// React Hook for Performance Tracking
export function usePerformanceTracking(componentName: string) {
    React.useEffect(() => {
        const monitor = PerformanceMonitor.getInstance();
        monitor.markStart(`component:${componentName}`);
        
        return () => {
            monitor.markEnd(`component:${componentName}`);
        };
    }, [componentName]);
}

// HOC for Performance Tracking
export function withPerformanceTracking<P extends object>(
    Component: React.ComponentType<P>,
    componentName: string
) {
    return (props: P) => {
        usePerformanceTracking(componentName);
        return <Component {...props} />;
    };
}
```

---

## 📝 Checklist Frontend Senior

### Architecture
- [ ] Clean Architecture (Hexagonal/Onion)
- [ ] Domain-Driven Design concepts
- [ ] SOLID principles appliqués
- [ ] Dependency injection
- [ ] Ports & Adapters pattern

### Testing
- [ ] Tests unitaires (>80% coverage)
- [ ] Tests d'intégration
- [ ] Tests E2E (Playwright/Cypress)
- [ ] Test-Driven Development (TDD)
- [ ] Mocking et stubbing appropriés

### Performance
- [ ] Core Web Vitals optimisés
- [ ] Code splitting & lazy loading
- [ ] Performance monitoring
- [ ] Bundle size optimization
- [ ] Caching strategies

### Scalabilité
- [ ] Micro-frontends architecture
- [ ] Module Federation
- [ ] Monorepo setup (Nx/Turborepo)
- [ ] CI/CD pipeline
- [ ] Feature flags

### Sécurité
- [ ] XSS protection
- [ ] CSRF protection
- [ ] Content Security Policy
- [ ] Secure authentication (OAuth2, JWT)
- [ ] Input sanitization

---

**Compétences Maîtrisées :** Architecture avancée, Testing complet, Performance, Production-ready applications
