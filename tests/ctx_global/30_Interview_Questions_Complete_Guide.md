# 30 Essential Interview Questions - Complete Solutions Guide

**Prepared for:** Alexandro Disla - Analyst-Programmer Exam Preparation  
**Date:** January 2026  
**Format:** Detailed explanations with code in Python and Java

---

## 📚 TABLE OF CONTENTS

1. **Frontend (Questions 1-6)** - React, CSS, HTML, JavaScript, Caching
2. **Backend (Questions 7-12)** - REST API, ACID, Authentication, Design Patterns
3. **DSA - Data Structures & Algorithms (Questions 13-22)** - Arrays, Trees, Graphs, Sorting, Searching
4. **DP - Dynamic Programming (Questions 23-27)** - Classic DP Problems
5. **UML (Questions 28-30)** - Class, Sequence, Use Case Diagrams

---

# 🎨 PART 1: FRONTEND (Questions 1-6)

---

## Question 1: Explain the Virtual DOM in React and how it improves performance

### Answer:

The **Virtual DOM (VDOM)** is a lightweight JavaScript representation of the actual DOM. It's a programming concept where a "virtual" representation of the UI is kept in memory and synced with the "real" DOM through a process called **reconciliation**.

### How It Works:

```
┌─────────────────────────────────────────────────────────────┐
│                    VIRTUAL DOM PROCESS                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. State Change Occurs                                      │
│         ↓                                                    │
│  2. New Virtual DOM Tree Created                             │
│         ↓                                                    │
│  3. Diffing: Compare New VDOM with Previous VDOM             │
│         ↓                                                    │
│  4. Calculate Minimum Changes Needed                         │
│         ↓                                                    │
│  5. Batch Updates to Real DOM (Reconciliation)               │
│         ↓                                                    │
│  6. Browser Repaints Only Changed Elements                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Why It's Faster:

1. **Batch Updates**: Instead of updating the DOM for each change, React batches multiple changes together
2. **Minimal DOM Manipulation**: Only the specific elements that changed are updated
3. **Diffing Algorithm**: O(n) complexity algorithm to find differences efficiently

### React Example:

```jsx
import React, { useState } from 'react';

function AccountBalance() {
    const [balance, setBalance] = useState(10000);
    const [transactions, setTransactions] = useState([]);
    
    const handleDeposit = (amount) => {
        // When state changes, React:
        // 1. Creates new Virtual DOM
        // 2. Compares with previous Virtual DOM
        // 3. Only updates the balance display, not entire page
        setBalance(prev => prev + amount);
        setTransactions(prev => [
            ...prev, 
            { type: 'deposit', amount, date: new Date() }
        ]);
    };
    
    return (
        <div className="account-container">
            <h2>Balance: <span>{balance.toFixed(2)} HTG</span></h2>
            <button onClick={() => handleDeposit(500)}>Deposit 500 HTG</button>
            <ul className="transactions">
                {transactions.map((t, index) => (
                    <li key={index}>{t.type}: {t.amount} HTG</li>
                ))}
            </ul>
        </div>
    );
}
```

### Key Interview Points:
- Virtual DOM is NOT faster than direct DOM for single updates
- Its advantage is in **batching** and **minimizing** updates
- React uses a **reconciliation algorithm** with O(n) complexity
- Keys help React identify which items have changed in lists

---

## Question 2: Explain the CSS Box Model in detail

### Answer:

The **CSS Box Model** is the foundation of layout in CSS. Every HTML element is treated as a rectangular box consisting of four layers.

```
┌─────────────────────────────── MARGIN ────────────────────────────────┐
│                                                                        │
│    ┌─────────────────────────── BORDER ───────────────────────────┐   │
│    │                                                               │   │
│    │    ┌─────────────────── PADDING ─────────────────────┐       │   │
│    │    │                                                  │       │   │
│    │    │    ┌─────────────────────────────────────┐      │       │   │
│    │    │    │              CONTENT                 │      │       │   │
│    │    │    │           (width × height)           │      │       │   │
│    │    │    └─────────────────────────────────────┘      │       │   │
│    │    │                                                  │       │   │
│    │    └──────────────────────────────────────────────────┘       │   │
│    │                                                               │   │
│    └───────────────────────────────────────────────────────────────┘   │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### CSS Example:

```css
/* Standard Box Model (content-box) - DEFAULT */
.card-content-box {
    width: 300px;
    height: 200px;
    padding: 20px;
    border: 5px solid #333;
    margin: 15px;
    
    /* Total Width = 300 + 20*2 + 5*2 + 15*2 = 380px */
}

/* Border-Box Model (RECOMMENDED) */
.card-border-box {
    box-sizing: border-box;  /* Include padding and border in width */
    width: 300px;            /* This IS the total width (excluding margin) */
    padding: 20px;
    border: 5px solid #333;
    margin: 15px;
    
    /* Content Width = 300 - 20*2 - 5*2 = 250px */
}

/* Best Practice: Apply border-box to all elements */
*, *::before, *::after {
    box-sizing: border-box;
}
```

### Key Interview Points:
1. **content-box** (default): width/height only includes content
2. **border-box**: width/height includes content + padding + border
3. **Margin collapse**: Vertical margins collapse to the larger value
4. **Margin** can be negative; **padding** cannot

---

## Question 3: What is Event Delegation in JavaScript?

### Answer:

**Event Delegation** is attaching a single event listener to a parent element instead of multiple listeners to child elements. It leverages **event bubbling**.

```
┌────────────────────────────────────────────────────────────┐
│                     EVENT BUBBLING                          │
├────────────────────────────────────────────────────────────┤
│                                                             │
│   Click on button                                           │
│        ↓                                                    │
│   Button receives event (TARGET PHASE)                      │
│        ↓                                                    │
│   Event bubbles up to parent div (BUBBLING PHASE)          │
│        ↓                                                    │
│   Event bubbles up to document                              │
│                                                             │
└────────────────────────────────────────────────────────────┘
```

### Without Event Delegation (BAD):

```javascript
// ❌ BAD: Adding listener to each button - memory inefficient
const buttons = document.querySelectorAll('.transaction-btn');
buttons.forEach(button => {
    button.addEventListener('click', function(e) {
        console.log('Transaction:', this.dataset.transactionId);
    });
});
```

### With Event Delegation (GOOD):

```javascript
// ✅ GOOD: Single listener on parent
document.getElementById('transaction-list').addEventListener('click', function(e) {
    // Check if clicked element is a button
    if (e.target.matches('.transaction-btn')) {
        const transactionId = e.target.dataset.transactionId;
        handleTransaction(transactionId);
    }
    
    if (e.target.matches('.delete-btn')) {
        const itemId = e.target.closest('.transaction-item').dataset.id;
        deleteTransaction(itemId);
    }
});

// Benefits:
// 1. Single event listener for all buttons
// 2. Works with dynamically added elements
// 3. Better memory efficiency
```

### Key Interview Points:
1. **Event Bubbling**: Events bubble up from target to ancestors
2. **e.target**: The actual element that was clicked
3. **e.currentTarget**: The element the listener is attached to
4. **Performance**: O(1) instead of O(n) for n elements
5. **Dynamic Content**: Works with elements added after page load

---

## Question 4: Explain Browser Caching Strategies

### Answer:

### HTTP Cache Headers:

| Header | Purpose | Example |
|--------|---------|---------|
| `Cache-Control` | Main caching directive | `max-age=31536000` |
| `ETag` | Resource version identifier | `"abc123"` |
| `Last-Modified` | When resource was last changed | `Tue, 21 Jan 2026 10:00:00 GMT` |

### Cache-Control Values:

```
┌────────────────────────────────────────────────────────────────┐
│                    CACHE-CONTROL DIRECTIVES                     │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  PUBLIC vs PRIVATE                                              │
│  ├── public    → Can be cached by browsers AND CDNs            │
│  └── private   → Only browser can cache (sensitive data)       │
│                                                                 │
│  FRESHNESS                                                      │
│  ├── max-age=3600      → Fresh for 1 hour                      │
│  └── no-cache          → Always validate with server           │
│                                                                 │
│  VALIDATION                                                     │
│  ├── no-store    → Never cache (sensitive data!)               │
│  └── must-revalidate → Must check when stale                   │
│                                                                 │
└────────────────────────────────────────────────────────────────┘
```

### Caching by Resource Type:

```javascript
// Static assets - Cache for 1 year
app.use('/static', express.static('public', {
    maxAge: '1y',
    immutable: true
}));

// HTML - Always revalidate
app.get('/', (req, res) => {
    res.setHeader('Cache-Control', 'no-cache');
    res.sendFile('index.html');
});

// API - Sensitive data - Never cache
app.get('/api/account/balance', (req, res) => {
    res.setHeader('Cache-Control', 'private, no-store');
    res.json({ balance: 50000 });
});
```

### Key Interview Points:
1. **no-store** for sensitive banking data
2. **Cache busting** with file hashes: `app.a1b2c3.js`
3. **ETag/Last-Modified** for conditional requests (304 Not Modified)

---

## Question 5: Difference between `==` and `===` in JavaScript

### Answer:

| Operator | Name | Comparison | Type Coercion |
|----------|------|------------|---------------|
| `==` | Loose Equality | Value only | Yes (converts types) |
| `===` | Strict Equality | Value AND Type | No |

### Examples:

```javascript
// ==================== LOOSE EQUALITY (==) ====================
console.log(5 == '5');           // true  (string → number)
console.log(true == 1);          // true  (true → 1)
console.log(null == undefined);  // true  (special case)
console.log('' == 0);            // true  ('' → 0)

// ==================== STRICT EQUALITY (===) ====================
console.log(5 === '5');          // false (number !== string)
console.log(true === 1);         // false (boolean !== number)
console.log(null === undefined); // false (different types)

// ==================== BANKING EXAMPLE ====================
const userInput = '500';
const expectedAmount = 500;

// ❌ BAD - Could cause bugs
if (userInput == expectedAmount) { }

// ✅ GOOD - Explicit conversion then strict comparison
const parsedAmount = parseFloat(userInput);
if (parsedAmount === expectedAmount) { }

// ✅ String comparison
const accountNum1 = "12345";
const accountNum2 = "12345";
if (accountNum1 === accountNum2) { }  // Always use === for strings
```

### Key Interview Points:
1. **Always use `===`** in production code
2. `null == undefined` is `true`, but `null === undefined` is `false`
3. `NaN === NaN` is `false` (use `Number.isNaN()`)

---

## Question 6: Explain React Hooks: useState, useEffect, useCallback

### Answer:

### useState - State Management:

```jsx
import React, { useState } from 'react';

function BankAccount() {
    // Basic useState
    const [balance, setBalance] = useState(0);
    
    // useState with object
    const [account, setAccount] = useState({
        number: '',
        holder: '',
        type: 'savings'
    });
    
    // ✅ GOOD: Use functional update for state based on previous state
    const deposit = (amount) => {
        setBalance(prevBalance => prevBalance + amount);
    };
    
    // ✅ GOOD: Spread previous state when updating objects
    const updateAccountHolder = (name) => {
        setAccount(prev => ({ ...prev, holder: name }));
    };
    
    return (
        <div>
            <h2>Balance: {balance.toLocaleString()} HTG</h2>
            <button onClick={() => deposit(500)}>Deposit 500</button>
        </div>
    );
}
```

### useEffect - Side Effects:

```jsx
import React, { useState, useEffect } from 'react';

function AccountDashboard({ accountId }) {
    const [account, setAccount] = useState(null);
    const [loading, setLoading] = useState(true);
    
    // Effect runs when accountId changes
    useEffect(() => {
        let isMounted = true;
        
        async function fetchAccount() {
            setLoading(true);
            const response = await fetch(`/api/accounts/${accountId}`);
            const data = await response.json();
            
            if (isMounted) {
                setAccount(data);
                setLoading(false);
            }
        }
        
        fetchAccount();
        
        // Cleanup function
        return () => { isMounted = false; };
    }, [accountId]);  // Dependency array
    
    // Effect that runs once (on mount)
    useEffect(() => {
        console.log('Component mounted');
        return () => console.log('Component unmounting');
    }, []);  // Empty array = run once
    
    if (loading) return <div>Loading...</div>;
    return <div>Account: {account?.number}</div>;
}
```

### useCallback - Memoized Functions:

```jsx
import React, { useState, useCallback, memo } from 'react';

// Memoized child component
const TransactionItem = memo(({ transaction, onDelete }) => {
    return (
        <div>
            <span>{transaction.type}: {transaction.amount}</span>
            <button onClick={() => onDelete(transaction.id)}>Delete</button>
        </div>
    );
});

function TransactionList() {
    const [transactions, setTransactions] = useState([]);
    
    // ✅ WITH useCallback: Function reference stays stable
    const handleDelete = useCallback((id) => {
        setTransactions(prev => prev.filter(t => t.id !== id));
    }, []);  // Empty deps = function never changes
    
    return (
        <div>
            {transactions.map(t => (
                <TransactionItem
                    key={t.id}
                    transaction={t}
                    onDelete={handleDelete}
                />
            ))}
        </div>
    );
}
```

### Dependency Array Rules:

```
┌────────────────────────────────────────────────────────────────┐
│                    useEffect DEPENDENCY ARRAY                   │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  useEffect(() => { }, [])       → Run ONCE on mount            │
│  useEffect(() => { }, [dep])    → Run when dep changes         │
│  useEffect(() => { })           → Run on EVERY render          │
│                                                                 │
└────────────────────────────────────────────────────────────────┘
```

---

# 🔧 PART 2: BACKEND (Questions 7-12)

---

## Question 7: Explain REST API design principles

### Answer:

### HTTP Methods:

| Method | CRUD | Idempotent | Example |
|--------|------|------------|---------|
| **GET** | Read | Yes | `GET /accounts/123` |
| **POST** | Create | No | `POST /accounts` |
| **PUT** | Replace | Yes | `PUT /accounts/123` |
| **PATCH** | Update | No | `PATCH /accounts/123` |
| **DELETE** | Delete | Yes | `DELETE /accounts/123` |

### URL Design:

```
✅ GOOD:
GET    /api/v1/accounts                    # List accounts
GET    /api/v1/accounts/123                # Get account 123
POST   /api/v1/accounts                    # Create account
GET    /api/v1/accounts/123/transactions   # Account's transactions

❌ BAD:
GET    /api/v1/getAccount/123              # Verb in URL
POST   /api/v1/createAccount               # Verb in URL
```

### Python (FastAPI) Implementation:

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from decimal import Decimal

app = FastAPI()

class AccountCreate(BaseModel):
    holder_name: str
    account_type: str
    initial_deposit: Decimal = 0

class Account(BaseModel):
    id: str
    account_number: str
    holder_name: str
    balance: Decimal
    status: str

# GET /accounts - List all
@app.get("/api/v1/accounts", response_model=List[Account])
async def list_accounts(status: Optional[str] = None, page: int = 1):
    # Return filtered, paginated accounts
    pass

# GET /accounts/{id} - Get one
@app.get("/api/v1/accounts/{account_id}", response_model=Account)
async def get_account(account_id: str):
    account = accounts_db.get(account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

# POST /accounts - Create
@app.post("/api/v1/accounts", response_model=Account, status_code=201)
async def create_account(account: AccountCreate):
    # Create and return new account
    pass

# DELETE /accounts/{id} - Delete
@app.delete("/api/v1/accounts/{account_id}", status_code=204)
async def delete_account(account_id: str):
    # Delete account, return 204 No Content
    pass
```

### Java (Spring Boot) Implementation:

```java
@RestController
@RequestMapping("/api/v1/accounts")
public class AccountController {
    
    @Autowired
    private AccountService accountService;
    
    // GET /accounts - List all
    @GetMapping
    public ResponseEntity<Page<Account>> listAccounts(
            @RequestParam(required = false) String status,
            Pageable pageable) {
        return ResponseEntity.ok(accountService.findAll(status, pageable));
    }
    
    // GET /accounts/{id} - Get one
    @GetMapping("/{id}")
    public ResponseEntity<Account> getAccount(@PathVariable UUID id) {
        Account account = accountService.findById(id)
            .orElseThrow(() -> new ResourceNotFoundException("Account not found"));
        return ResponseEntity.ok(account);
    }
    
    // POST /accounts - Create
    @PostMapping
    public ResponseEntity<Account> createAccount(@Valid @RequestBody AccountCreateDTO dto) {
        Account account = accountService.create(dto);
        return ResponseEntity.status(HttpStatus.CREATED).body(account);
    }
    
    // DELETE /accounts/{id} - Delete
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteAccount(@PathVariable UUID id) {
        accountService.delete(id);
        return ResponseEntity.noContent().build();  // 204
    }
}
```

### HTTP Status Codes:

| Code | Name | When to Use |
|------|------|-------------|
| **200** | OK | Successful GET, PUT, PATCH |
| **201** | Created | Successful POST |
| **204** | No Content | Successful DELETE |
| **400** | Bad Request | Validation error |
| **401** | Unauthorized | Not authenticated |
| **403** | Forbidden | Not authorized |
| **404** | Not Found | Resource doesn't exist |
| **500** | Internal Error | Server error |

---

## Question 8: Explain ACID properties with banking example

### Answer:

```
┌─────────────────────────────────────────────────────────────────┐
│                    ACID PROPERTIES                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ATOMICITY (All or Nothing)                                      │
│  └── Transaction is indivisible - ALL succeed or NONE do        │
│                                                                  │
│  CONSISTENCY (Valid State to Valid State)                        │
│  └── Database rules are never violated                          │
│                                                                  │
│  ISOLATION (Transactions Don't Interfere)                        │
│  └── Concurrent transactions appear to run sequentially         │
│                                                                  │
│  DURABILITY (Committed = Permanent)                              │
│  └── Committed transactions survive crashes                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Banking Transfer Example:

```
BEFORE:  Alice: 1000 HTG    Bob: 500 HTG    Total: 1500 HTG

TRANSACTION:
┌─────────────────────────────────────────────────────────┐
│  BEGIN TRANSACTION                                       │
│  ├── 1. Check Alice balance >= 500  ✓                   │
│  ├── 2. Debit Alice: 1000 - 500 = 500                   │
│  ├── 3. Credit Bob: 500 + 500 = 1000                    │
│  COMMIT                                                  │
└─────────────────────────────────────────────────────────┘

AFTER:   Alice: 500 HTG     Bob: 1000 HTG   Total: 1500 HTG

ACID GUARANTEES:
• Atomicity: Both debit AND credit happen, or neither
• Consistency: Total money unchanged (1500 HTG)
• Isolation: Other transactions see before OR after state
• Durability: Transfer survives server crash after COMMIT
```

### SQL Implementation:

```sql
-- Schema with constraints for CONSISTENCY
CREATE TABLE accounts (
    account_id INT PRIMARY KEY AUTO_INCREMENT,
    account_number VARCHAR(20) UNIQUE NOT NULL,
    balance DECIMAL(15, 2) NOT NULL DEFAULT 0.00,
    CONSTRAINT chk_balance CHECK (balance >= 0)
);

-- Transfer Stored Procedure
DELIMITER //
CREATE PROCEDURE TransferMoney(
    IN p_source_id INT,
    IN p_dest_id INT,
    IN p_amount DECIMAL(15, 2)
)
BEGIN
    DECLARE v_source_balance DECIMAL(15, 2);
    
    -- ATOMICITY: Rollback on any error
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
    END;
    
    START TRANSACTION;
    
    -- ISOLATION: Lock rows with FOR UPDATE
    SELECT balance INTO v_source_balance
    FROM accounts WHERE account_id = p_source_id
    FOR UPDATE;
    
    SELECT * FROM accounts WHERE account_id = p_dest_id
    FOR UPDATE;
    
    -- CONSISTENCY: Check business rules
    IF v_source_balance >= p_amount THEN
        UPDATE accounts SET balance = balance - p_amount
        WHERE account_id = p_source_id;
        
        UPDATE accounts SET balance = balance + p_amount
        WHERE account_id = p_dest_id;
        
        -- DURABILITY: COMMIT writes to disk
        COMMIT;
    ELSE
        ROLLBACK;
    END IF;
END //
DELIMITER ;
```

### Python Implementation:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from decimal import Decimal

class BankingService:
    def __init__(self, database_url: str):
        self.engine = create_engine(database_url)
        self.Session = sessionmaker(bind=self.engine)
    
    @contextmanager
    def get_session(self):
        session = self.Session()
        try:
            yield session
            session.commit()  # DURABILITY
        except Exception:
            session.rollback()  # ATOMICITY
            raise
        finally:
            session.close()
    
    def transfer_money(self, source_id: int, dest_id: int, amount: Decimal):
        with self.get_session() as session:
            # ISOLATION: Lock rows
            source = session.query(Account).filter(
                Account.id == source_id
            ).with_for_update().first()
            
            dest = session.query(Account).filter(
                Account.id == dest_id
            ).with_for_update().first()
            
            # CONSISTENCY: Validate
            if source.balance < amount:
                raise ValueError("Insufficient balance")
            
            # Perform transfer
            source.balance -= amount
            dest.balance += amount
            
            # DURABILITY: commit() in context manager
```

### Java Implementation:

```java
@Service
public class TransferService {
    
    @Autowired
    private AccountRepository accountRepository;
    
    @Transactional(isolation = Isolation.SERIALIZABLE)
    public void transferMoney(UUID sourceId, UUID destId, BigDecimal amount) {
        // ISOLATION: Pessimistic locking
        Account source = accountRepository
            .findByIdWithLock(sourceId, LockModeType.PESSIMISTIC_WRITE)
            .orElseThrow(() -> new AccountNotFoundException(sourceId));
        
        Account dest = accountRepository
            .findByIdWithLock(destId, LockModeType.PESSIMISTIC_WRITE)
            .orElseThrow(() -> new AccountNotFoundException(destId));
        
        // CONSISTENCY: Validate
        if (source.getBalance().compareTo(amount) < 0) {
            throw new InsufficientBalanceException();
        }
        
        // Perform transfer
        source.setBalance(source.getBalance().subtract(amount));
        dest.setBalance(dest.getBalance().add(amount));
        
        accountRepository.save(source);
        accountRepository.save(dest);
        
        // ATOMICITY & DURABILITY: @Transactional handles commit/rollback
    }
}
```

---

## Question 9: Authentication vs Authorization

### Answer:

| Aspect | Authentication (AuthN) | Authorization (AuthZ) |
|--------|------------------------|----------------------|
| **Question** | "Who are you?" | "What can you do?" |
| **Verification** | Identity | Permissions |
| **Failure Code** | 401 Unauthorized | 403 Forbidden |

```
┌─────────────────────────────────────────────────────────────────┐
│                  AUTHENTICATION → AUTHORIZATION                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   USER REQUEST                                                   │
│        ↓                                                         │
│   ┌─────────────────────────────┐                               │
│   │    AUTHENTICATION           │                               │
│   │    "Who are you?"           │                               │
│   │    • Username/Password      │                               │
│   │    • JWT Token              │                               │
│   └──────────────┬──────────────┘                               │
│          ┌──────┴──────┐                                        │
│     ✓ Valid       ✗ Invalid → 401 Unauthorized                  │
│          ↓                                                       │
│   ┌─────────────────────────────┐                               │
│   │    AUTHORIZATION            │                               │
│   │    "What can you do?"       │                               │
│   │    • Role-based (RBAC)      │                               │
│   │    • Permission-based       │                               │
│   └──────────────┬──────────────┘                               │
│          ┌──────┴──────┐                                        │
│     ✓ Allowed → 200    ✗ Denied → 403 Forbidden                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Python (FastAPI) Implementation:

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from enum import Enum

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Role(str, Enum):
    CUSTOMER = "customer"
    TELLER = "teller"
    ADMIN = "admin"

# Role permissions mapping
ROLE_PERMISSIONS = {
    Role.CUSTOMER: ["read:own_account", "transfer:own"],
    Role.TELLER: ["read:any_account", "create:account"],
    Role.ADMIN: ["read:any_account", "create:account", "manage:users"],
}

# AUTHENTICATION: Get current user from token
async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = get_user(username)
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user

# AUTHORIZATION: Check permission
def require_permission(permission: str):
    async def checker(user = Depends(get_current_user)):
        user_permissions = ROLE_PERMISSIONS.get(user.role, [])
        if permission not in user_permissions:
            raise HTTPException(status_code=403, detail="Permission denied")
        return user
    return checker

# Usage
@app.get("/accounts/{account_id}")
async def get_account(account_id: str, user = Depends(get_current_user)):
    # Customer can only view own account
    if user.role == Role.CUSTOMER and account_id not in user.accounts:
        raise HTTPException(status_code=403, detail="Cannot view this account")
    return {"account_id": account_id}

@app.post("/accounts")
async def create_account(
    data: dict,
    user = Depends(require_permission("create:account"))
):
    # Only teller/admin can create accounts
    return {"created_by": user.username}
```

### Java (Spring Security) Implementation:

```java
@RestController
@RequestMapping("/api/v1")
public class AccountController {
    
    // AUTHENTICATION: Spring Security handles via SecurityFilterChain
    
    // AUTHORIZATION: Method-level security
    @GetMapping("/accounts/{id}")
    @PreAuthorize("hasRole('ADMIN') or @accountService.isOwner(#id, principal)")
    public ResponseEntity<Account> getAccount(@PathVariable UUID id) {
        return ResponseEntity.ok(accountService.findById(id));
    }
    
    @PostMapping("/accounts")
    @PreAuthorize("hasAnyRole('TELLER', 'ADMIN')")
    public ResponseEntity<Account> createAccount(@RequestBody AccountDTO dto) {
        return ResponseEntity.status(201).body(accountService.create(dto));
    }
    
    @DeleteMapping("/accounts/{id}")
    @PreAuthorize("hasRole('ADMIN')")
    public ResponseEntity<Void> deleteAccount(@PathVariable UUID id) {
        accountService.delete(id);
        return ResponseEntity.noContent().build();
    }
}

// Security Configuration
@Configuration
@EnableWebSecurity
@EnableMethodSecurity
public class SecurityConfig {
    
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .csrf(csrf -> csrf.disable())
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/v1/public/**").permitAll()
                .requestMatchers("/api/v1/**").authenticated()
            )
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(Customizer.withDefaults()));
        
        return http.build();
    }
}
```

---

## Question 10: Explain the Singleton Design Pattern

### Answer:

**Singleton** ensures a class has only ONE instance and provides a global access point.

### Use Cases in Banking:
- Database connection pool
- Configuration manager
- Logging service
- Cache manager

### Python Implementation:

```python
# Method 1: Using __new__
class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        self.connection = "Connected to database"
        print("Database connection established")
    
    def query(self, sql):
        return f"Executing: {sql}"

# Usage
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True - same instance

# Method 2: Thread-safe with Lock
import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # Double-check
                    cls._instance = super().__new__(cls)
        return cls._instance

# Method 3: Using decorator
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Configuration:
    def __init__(self):
        self.settings = {"db_host": "localhost"}
```

### Java Implementation:

```java
// Method 1: Eager Initialization
public class EagerSingleton {
    private static final EagerSingleton INSTANCE = new EagerSingleton();
    
    private EagerSingleton() {}
    
    public static EagerSingleton getInstance() {
        return INSTANCE;
    }
}

// Method 2: Bill Pugh (RECOMMENDED - Thread-safe, Lazy)
public class Configuration {
    
    private Map<String, String> settings;
    
    // Private constructor
    private Configuration() {
        settings = new HashMap<>();
        loadSettings();
    }
    
    // Static inner class - loaded only when getInstance() called
    private static class ConfigurationHolder {
        private static final Configuration INSTANCE = new Configuration();
    }
    
    // Public access method
    public static Configuration getInstance() {
        return ConfigurationHolder.INSTANCE;
    }
    
    private void loadSettings() {
        settings.put("db.host", "localhost");
        settings.put("db.port", "5432");
    }
    
    public String getSetting(String key) {
        return settings.get(key);
    }
}

// Usage
Configuration config1 = Configuration.getInstance();
Configuration config2 = Configuration.getInstance();
System.out.println(config1 == config2);  // true

// Method 3: Enum Singleton (Most robust)
public enum DatabaseConnection {
    INSTANCE;
    
    private Connection connection;
    
    DatabaseConnection() {
        // Initialize connection
    }
    
    public Connection getConnection() {
        return connection;
    }
}

// Usage
DatabaseConnection.INSTANCE.getConnection();
```

---

## Question 11: Explain the Factory Design Pattern

### Answer:

**Factory Pattern** creates objects without exposing creation logic. The client uses a common interface.

### Python Implementation:

```python
from abc import ABC, abstractmethod
from decimal import Decimal

# Abstract Product
class Account(ABC):
    def __init__(self, account_number: str, balance: Decimal = Decimal('0')):
        self.account_number = account_number
        self.balance = balance
    
    @abstractmethod
    def calculate_interest(self) -> Decimal:
        pass
    
    @abstractmethod
    def get_monthly_fee(self) -> Decimal:
        pass

# Concrete Products
class SavingsAccount(Account):
    def __init__(self, account_number: str, balance: Decimal = Decimal('0')):
        super().__init__(account_number, balance)
        self.interest_rate = Decimal('0.03')  # 3%
    
    def calculate_interest(self) -> Decimal:
        return self.balance * self.interest_rate / 12
    
    def get_monthly_fee(self) -> Decimal:
        return Decimal('0') if self.balance >= 1000 else Decimal('5')

class CheckingAccount(Account):
    def __init__(self, account_number: str, balance: Decimal = Decimal('0')):
        super().__init__(account_number, balance)
        self.overdraft_limit = Decimal('500')
    
    def calculate_interest(self) -> Decimal:
        return Decimal('0')  # No interest
    
    def get_monthly_fee(self) -> Decimal:
        return Decimal('10')

class CreditAccount(Account):
    def __init__(self, account_number: str, balance: Decimal = Decimal('0')):
        super().__init__(account_number, balance)
        self.credit_limit = Decimal('5000')
        self.apr = Decimal('0.18')  # 18% APR
    
    def calculate_interest(self) -> Decimal:
        if self.balance < 0:  # Balance owed
            return abs(self.balance) * self.apr / 12
        return Decimal('0')
    
    def get_monthly_fee(self) -> Decimal:
        return Decimal('25')

# Factory
class AccountFactory:
    @staticmethod
    def create_account(account_type: str, account_number: str, 
                       initial_balance: Decimal = Decimal('0')) -> Account:
        account_types = {
            'savings': SavingsAccount,
            'checking': CheckingAccount,
            'credit': CreditAccount
        }
        
        account_class = account_types.get(account_type.lower())
        if not account_class:
            raise ValueError(f"Unknown account type: {account_type}")
        
        return account_class(account_number, initial_balance)

# Usage
savings = AccountFactory.create_account('savings', 'SAV001', Decimal('5000'))
checking = AccountFactory.create_account('checking', 'CHK001', Decimal('1000'))
credit = AccountFactory.create_account('credit', 'CRD001')

print(f"Savings interest: {savings.calculate_interest()}")
print(f"Checking fee: {checking.get_monthly_fee()}")
```

### Java Implementation:

```java
// Abstract Product
public interface Account {
    String getAccountNumber();
    BigDecimal getBalance();
    BigDecimal calculateInterest();
    BigDecimal getMonthlyFee();
}

// Concrete Products
public class SavingsAccount implements Account {
    private String accountNumber;
    private BigDecimal balance;
    private static final BigDecimal INTEREST_RATE = new BigDecimal("0.03");
    
    public SavingsAccount(String accountNumber, BigDecimal balance) {
        this.accountNumber = accountNumber;
        this.balance = balance;
    }
    
    @Override
    public String getAccountNumber() { return accountNumber; }
    
    @Override
    public BigDecimal getBalance() { return balance; }
    
    @Override
    public BigDecimal calculateInterest() {
        return balance.multiply(INTEREST_RATE).divide(new BigDecimal("12"), 2, RoundingMode.HALF_UP);
    }
    
    @Override
    public BigDecimal getMonthlyFee() {
        return balance.compareTo(new BigDecimal("1000")) >= 0 
            ? BigDecimal.ZERO 
            : new BigDecimal("5");
    }
}

public class CheckingAccount implements Account {
    private String accountNumber;
    private BigDecimal balance;
    
    public CheckingAccount(String accountNumber, BigDecimal balance) {
        this.accountNumber = accountNumber;
        this.balance = balance;
    }
    
    @Override
    public String getAccountNumber() { return accountNumber; }
    
    @Override
    public BigDecimal getBalance() { return balance; }
    
    @Override
    public BigDecimal calculateInterest() { return BigDecimal.ZERO; }
    
    @Override
    public BigDecimal getMonthlyFee() { return new BigDecimal("10"); }
}

// Factory
public class AccountFactory {
    
    public static Account createAccount(String type, String accountNumber, 
                                        BigDecimal initialBalance) {
        switch (type.toLowerCase()) {
            case "savings":
                return new SavingsAccount(accountNumber, initialBalance);
            case "checking":
                return new CheckingAccount(accountNumber, initialBalance);
            case "credit":
                return new CreditAccount(accountNumber, initialBalance);
            default:
                throw new IllegalArgumentException("Unknown account type: " + type);
        }
    }
}

// Usage
Account savings = AccountFactory.createAccount("savings", "SAV001", new BigDecimal("5000"));
Account checking = AccountFactory.createAccount("checking", "CHK001", new BigDecimal("1000"));
```

---

## Question 12: Explain the Observer Design Pattern

### Answer:

**Observer Pattern** defines a one-to-many dependency. When one object changes state, all dependents are notified.

### Use Cases in Banking:
- Account balance change notifications
- Transaction alerts (SMS, Email, Push)
- Fraud detection alerts

### Python Implementation:

```python
from abc import ABC, abstractmethod
from typing import List
from decimal import Decimal
from datetime import datetime

# Observer Interface
class AccountObserver(ABC):
    @abstractmethod
    def notify(self, account_number: str, event_type: str, data: dict):
        pass

# Concrete Observers
class EmailNotifier(AccountObserver):
    def notify(self, account_number: str, event_type: str, data: dict):
        print(f"📧 EMAIL to {data.get('email')}: "
              f"Account {account_number} - {event_type}: {data}")

class SMSNotifier(AccountObserver):
    def notify(self, account_number: str, event_type: str, data: dict):
        print(f"📱 SMS to {data.get('phone')}: "
              f"Account {account_number} - {event_type}")

class FraudDetector(AccountObserver):
    def notify(self, account_number: str, event_type: str, data: dict):
        amount = data.get('amount', 0)
        if event_type == 'withdrawal' and amount > 10000:
            print(f"🚨 FRAUD ALERT: Large withdrawal of {amount} from {account_number}")

class AuditLogger(AccountObserver):
    def notify(self, account_number: str, event_type: str, data: dict):
        timestamp = datetime.now().isoformat()
        print(f"📝 AUDIT LOG [{timestamp}]: {account_number} - {event_type} - {data}")

# Subject (Observable)
class BankAccount:
    def __init__(self, account_number: str, holder_email: str, holder_phone: str):
        self.account_number = account_number
        self.holder_email = holder_email
        self.holder_phone = holder_phone
        self.balance = Decimal('0')
        self._observers: List[AccountObserver] = []
    
    def attach(self, observer: AccountObserver):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer: AccountObserver):
        self._observers.remove(observer)
    
    def _notify_observers(self, event_type: str, data: dict):
        data['email'] = self.holder_email
        data['phone'] = self.holder_phone
        for observer in self._observers:
            observer.notify(self.account_number, event_type, data)
    
    def deposit(self, amount: Decimal):
        self.balance += amount
        self._notify_observers('deposit', {
            'amount': float(amount),
            'new_balance': float(self.balance)
        })
    
    def withdraw(self, amount: Decimal) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            self._notify_observers('withdrawal', {
                'amount': float(amount),
                'new_balance': float(self.balance)
            })
            return True
        return False

# Usage
account = BankAccount("ACC001", "alice@email.com", "+509-1234-5678")

# Attach observers
account.attach(EmailNotifier())
account.attach(SMSNotifier())
account.attach(FraudDetector())
account.attach(AuditLogger())

# Perform operations - all observers notified
account.deposit(Decimal('5000'))
account.withdraw(Decimal('500'))
account.withdraw(Decimal('15000'))  # Triggers fraud alert
```

### Java Implementation:

```java
import java.util.*;
import java.math.BigDecimal;
import java.time.LocalDateTime;

// Observer Interface
public interface AccountObserver {
    void notify(String accountNumber, String eventType, Map<String, Object> data);
}

// Concrete Observers
public class EmailNotifier implements AccountObserver {
    @Override
    public void notify(String accountNumber, String eventType, Map<String, Object> data) {
        System.out.println("📧 EMAIL to " + data.get("email") + 
            ": Account " + accountNumber + " - " + eventType);
    }
}

public class SMSNotifier implements AccountObserver {
    @Override
    public void notify(String accountNumber, String eventType, Map<String, Object> data) {
        System.out.println("📱 SMS to " + data.get("phone") + 
            ": Account " + accountNumber + " - " + eventType);
    }
}

public class FraudDetector implements AccountObserver {
    @Override
    public void notify(String accountNumber, String eventType, Map<String, Object> data) {
        BigDecimal amount = (BigDecimal) data.get("amount");
        if ("withdrawal".equals(eventType) && 
            amount.compareTo(new BigDecimal("10000")) > 0) {
            System.out.println("🚨 FRAUD ALERT: Large withdrawal from " + accountNumber);
        }
    }
}

// Subject (Observable)
public class BankAccount {
    private String accountNumber;
    private String holderEmail;
    private String holderPhone;
    private BigDecimal balance = BigDecimal.ZERO;
    private List<AccountObserver> observers = new ArrayList<>();
    
    public BankAccount(String accountNumber, String email, String phone) {
        this.accountNumber = accountNumber;
        this.holderEmail = email;
        this.holderPhone = phone;
    }
    
    public void attach(AccountObserver observer) {
        observers.add(observer);
    }
    
    public void detach(AccountObserver observer) {
        observers.remove(observer);
    }
    
    private void notifyObservers(String eventType, Map<String, Object> data) {
        data.put("email", holderEmail);
        data.put("phone", holderPhone);
        for (AccountObserver observer : observers) {
            observer.notify(accountNumber, eventType, data);
        }
    }
    
    public void deposit(BigDecimal amount) {
        balance = balance.add(amount);
        Map<String, Object> data = new HashMap<>();
        data.put("amount", amount);
        data.put("newBalance", balance);
        notifyObservers("deposit", data);
    }
    
    public boolean withdraw(BigDecimal amount) {
        if (balance.compareTo(amount) >= 0) {
            balance = balance.subtract(amount);
            Map<String, Object> data = new HashMap<>();
            data.put("amount", amount);
            data.put("newBalance", balance);
            notifyObservers("withdrawal", data);
            return true;
        }
        return false;
    }
}

// Usage
public class Main {
    public static void main(String[] args) {
        BankAccount account = new BankAccount("ACC001", "alice@email.com", "+509-1234");
        
        account.attach(new EmailNotifier());
        account.attach(new SMSNotifier());
        account.attach(new FraudDetector());
        
        account.deposit(new BigDecimal("5000"));
        account.withdraw(new BigDecimal("15000"));  // Triggers fraud alert
    }
}
```

---

# 📊 PART 3: DSA - Data Structures & Algorithms (Questions 13-22)

---

## Question 13: Implement a Stack (LIFO)

### Answer:

**Stack**: Last In, First Out - like a stack of plates.

### Operations:
- `push(item)`: Add to top - O(1)
- `pop()`: Remove from top - O(1)
- `peek()`: View top - O(1)
- `isEmpty()`: Check if empty - O(1)

### Python Implementation:

```python
class Stack:
    def __init__(self):
        self._items = []
    
    def push(self, item):
        """Add item to top of stack - O(1)"""
        self._items.append(item)
    
    def pop(self):
        """Remove and return top item - O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items.pop()
    
    def peek(self):
        """View top item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items[-1]
    
    def is_empty(self):
        """Check if stack is empty - O(1)"""
        return len(self._items) == 0
    
    def size(self):
        """Return number of items - O(1)"""
        return len(self._items)

# Usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())   # 30
print(stack.peek())  # 20
```

### Java Implementation:

```java
public class Stack<T> {
    private Object[] items;
    private int top;
    private int capacity;
    
    public Stack(int capacity) {
        this.capacity = capacity;
        this.items = new Object[capacity];
        this.top = -1;
    }
    
    public void push(T item) {
        if (top >= capacity - 1) {
            throw new RuntimeException("Stack Overflow");
        }
        items[++top] = item;
    }
    
    @SuppressWarnings("unchecked")
    public T pop() {
        if (isEmpty()) {
            throw new RuntimeException("Stack Underflow");
        }
        return (T) items[top--];
    }
    
    @SuppressWarnings("unchecked")
    public T peek() {
        if (isEmpty()) {
            throw new RuntimeException("Stack is empty");
        }
        return (T) items[top];
    }
    
    public boolean isEmpty() {
        return top < 0;
    }
    
    public int size() {
        return top + 1;
    }
}

// Usage
Stack<Integer> stack = new Stack<>(10);
stack.push(10);
stack.push(20);
System.out.println(stack.pop());  // 20
```

---

## Question 14: Implement a Queue (FIFO)

### Answer:

**Queue**: First In, First Out - like a line at the bank.

### Python Implementation:

```python
class Queue:
    def __init__(self):
        self._items = []
    
    def enqueue(self, item):
        """Add item to rear - O(1)"""
        self._items.append(item)
    
    def dequeue(self):
        """Remove and return front item - O(n) for list, O(1) for deque"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items.pop(0)
    
    def peek(self):
        """View front item - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items[0]
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)

# Efficient implementation using deque
from collections import deque

class EfficientQueue:
    def __init__(self):
        self._items = deque()
    
    def enqueue(self, item):
        self._items.append(item)  # O(1)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items.popleft()  # O(1)
    
    def is_empty(self):
        return len(self._items) == 0
```

### Java Implementation:

```java
public class Queue<T> {
    private Object[] items;
    private int front;
    private int rear;
    private int count;
    private int capacity;
    
    public Queue(int capacity) {
        this.capacity = capacity;
        this.items = new Object[capacity];
        this.front = 0;
        this.rear = -1;
        this.count = 0;
    }
    
    public void enqueue(T item) {
        if (count >= capacity) {
            throw new RuntimeException("Queue is full");
        }
        rear = (rear + 1) % capacity;  // Circular
        items[rear] = item;
        count++;
    }
    
    @SuppressWarnings("unchecked")
    public T dequeue() {
        if (isEmpty()) {
            throw new RuntimeException("Queue is empty");
        }
        T item = (T) items[front];
        front = (front + 1) % capacity;  // Circular
        count--;
        return item;
    }
    
    @SuppressWarnings("unchecked")
    public T peek() {
        if (isEmpty()) {
            throw new RuntimeException("Queue is empty");
        }
        return (T) items[front];
    }
    
    public boolean isEmpty() {
        return count == 0;
    }
    
    public int size() {
        return count;
    }
}
```

---

## Question 15: Implement Binary Search

### Answer:

**Binary Search** finds an element in a **sorted** array by repeatedly dividing the search space in half.

**Time Complexity**: O(log n)  
**Space Complexity**: O(1) iterative, O(log n) recursive

### Python Implementation:

```python
def binary_search_iterative(arr: list, target: int) -> int:
    """
    Find target in sorted array.
    Returns index if found, -1 if not found.
    Time: O(log n), Space: O(1)
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        # Avoid integer overflow
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    
    return -1  # Not found

def binary_search_recursive(arr: list, target: int, left: int, right: int) -> int:
    """Recursive implementation."""
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Usage
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(binary_search_iterative(arr, 23))  # 5
print(binary_search_iterative(arr, 100)) # -1
```

### Java Implementation:

```java
public class BinarySearch {
    
    // Iterative
    public static int binarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return -1;
    }
    
    // Recursive
    public static int binarySearchRecursive(int[] arr, int target, 
                                            int left, int right) {
        if (left > right) {
            return -1;
        }
        
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            return binarySearchRecursive(arr, target, mid + 1, right);
        } else {
            return binarySearchRecursive(arr, target, left, mid - 1);
        }
    }
    
    public static void main(String[] args) {
        int[] arr = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
        System.out.println(binarySearch(arr, 23));  // 5
    }
}
```

---

## Question 16: Implement Quick Sort

### Answer:

**Quick Sort** uses divide-and-conquer: pick a pivot, partition array around it, recursively sort subarrays.

**Time Complexity**: O(n log n) average, O(n²) worst  
**Space Complexity**: O(log n)

### Python Implementation:

```python
def quick_sort(arr: list) -> list:
    """Quick sort - modifies array in place."""
    _quick_sort_helper(arr, 0, len(arr) - 1)
    return arr

def _quick_sort_helper(arr: list, low: int, high: int):
    if low < high:
        # Partition and get pivot index
        pivot_index = _partition(arr, low, high)
        
        # Recursively sort left and right of pivot
        _quick_sort_helper(arr, low, pivot_index - 1)
        _quick_sort_helper(arr, pivot_index + 1, high)

def _partition(arr: list, low: int, high: int) -> int:
    """
    Partition array around pivot (last element).
    Returns final position of pivot.
    """
    pivot = arr[high]  # Choose last element as pivot
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap
    
    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Usage
arr = [64, 34, 25, 12, 22, 11, 90]
quick_sort(arr)
print(arr)  # [11, 12, 22, 25, 34, 64, 90]

# Trace for [5, 2, 8, 1, 9]:
# pivot=9, after partition: [5, 2, 8, 1, 9], pivot_idx=4
# Recurse on [5, 2, 8, 1]:
#   pivot=1, after partition: [1, 2, 8, 5], pivot_idx=0
#   Recurse on [2, 8, 5]:
#     pivot=5, after partition: [2, 5, 8], pivot_idx=1
# Final: [1, 2, 5, 8, 9]
```

### Java Implementation:

```java
public class QuickSort {
    
    public static void quickSort(int[] arr) {
        quickSort(arr, 0, arr.length - 1);
    }
    
    private static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pivotIndex = partition(arr, low, high);
            quickSort(arr, low, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, high);
        }
    }
    
    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;
        
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                // Swap arr[i] and arr[j]
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        
        // Place pivot in correct position
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        
        return i + 1;
    }
    
    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        quickSort(arr);
        System.out.println(Arrays.toString(arr));
    }
}
```

---

## Question 17: Implement Merge Sort

### Answer:

**Merge Sort** divides array in half, recursively sorts each half, then merges them.

**Time Complexity**: O(n log n) always  
**Space Complexity**: O(n)

### Python Implementation:

```python
def merge_sort(arr: list) -> list:
    """Merge sort - returns new sorted array."""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left: list, right: list) -> list:
    """Merge two sorted arrays."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# In-place merge sort
def merge_sort_inplace(arr: list, left: int, right: int):
    if left < right:
        mid = left + (right - left) // 2
        merge_sort_inplace(arr, left, mid)
        merge_sort_inplace(arr, mid + 1, right)
        merge_inplace(arr, left, mid, right)

def merge_inplace(arr: list, left: int, mid: int, right: int):
    """Merge two halves in place."""
    # Create temp arrays
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

# Usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # [11, 12, 22, 25, 34, 64, 90]
```

### Java Implementation:

```java
public class MergeSort {
    
    public static void mergeSort(int[] arr) {
        mergeSort(arr, 0, arr.length - 1);
    }
    
    private static void mergeSort(int[] arr, int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;
            
            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);
            
            merge(arr, left, mid, right);
        }
    }
    
    private static void merge(int[] arr, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;
        
        int[] L = new int[n1];
        int[] R = new int[n2];
        
        for (int i = 0; i < n1; i++) {
            L[i] = arr[left + i];
        }
        for (int j = 0; j < n2; j++) {
            R[j] = arr[mid + 1 + j];
        }
        
        int i = 0, j = 0, k = left;
        
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }
        
        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }
        
        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }
}
```

---

## Question 18: Implement BFS (Breadth-First Search)

### Answer:

**BFS** explores a graph level by level using a Queue.

**Use cases**: Shortest path (unweighted), level-order traversal

### Python Implementation:

```python
from collections import deque

def bfs(graph: dict, start) -> list:
    """
    Breadth-First Search - explores level by level.
    graph: adjacency list {node: [neighbors]}
    Returns: list of nodes in BFS order
    """
    visited = set()
    queue = deque([start])
    result = []
    
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

def bfs_shortest_path(graph: dict, start, end) -> list:
    """Find shortest path using BFS."""
    if start == end:
        return [start]
    
    visited = {start}
    queue = deque([(start, [start])])
    
    while queue:
        node, path = queue.popleft()
        
        for neighbor in graph.get(node, []):
            if neighbor == end:
                return path + [neighbor]
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return []  # No path found

# Usage
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2, 6],
    6: [3, 5]
}

print(bfs(graph, 1))  # [1, 2, 3, 4, 5, 6]
print(bfs_shortest_path(graph, 1, 6))  # [1, 3, 6]
```

### Java Implementation:

```java
import java.util.*;

public class BFS {
    
    public static List<Integer> bfs(Map<Integer, List<Integer>> graph, int start) {
        List<Integer> result = new ArrayList<>();
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();
        
        visited.add(start);
        queue.offer(start);
        
        while (!queue.isEmpty()) {
            int node = queue.poll();
            result.add(node);
            
            for (int neighbor : graph.getOrDefault(node, Collections.emptyList())) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.offer(neighbor);
                }
            }
        }
        
        return result;
    }
    
    public static void main(String[] args) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        graph.put(1, Arrays.asList(2, 3));
        graph.put(2, Arrays.asList(1, 4, 5));
        graph.put(3, Arrays.asList(1, 6));
        graph.put(4, Arrays.asList(2));
        graph.put(5, Arrays.asList(2, 6));
        graph.put(6, Arrays.asList(3, 5));
        
        System.out.println(bfs(graph, 1));  // [1, 2, 3, 4, 5, 6]
    }
}
```

---

## Question 19: Implement DFS (Depth-First Search)

### Answer:

**DFS** explores as deep as possible before backtracking, using recursion or a Stack.

**Use cases**: Cycle detection, topological sort, path finding

### Python Implementation:

```python
def dfs_recursive(graph: dict, start, visited: set = None) -> list:
    """DFS using recursion."""
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    
    return result

def dfs_iterative(graph: dict, start) -> list:
    """DFS using explicit stack."""
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            result.append(node)
            
            # Add neighbors in reverse order for same order as recursive
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result

def has_cycle(graph: dict) -> bool:
    """Detect cycle in directed graph using DFS."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph}
    
    def dfs(node):
        color[node] = GRAY  # Being processed
        
        for neighbor in graph.get(node, []):
            if color[neighbor] == GRAY:  # Back edge = cycle
                return True
            if color[neighbor] == WHITE and dfs(neighbor):
                return True
        
        color[node] = BLACK  # Finished
        return False
    
    for node in graph:
        if color[node] == WHITE:
            if dfs(node):
                return True
    
    return False

# Usage
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [6],
    6: []
}

print(dfs_recursive(graph, 1))  # [1, 2, 4, 5, 6, 3]
print(dfs_iterative(graph, 1))  # [1, 2, 4, 5, 6, 3]
```

### Java Implementation:

```java
import java.util.*;

public class DFS {
    
    // Recursive DFS
    public static List<Integer> dfsRecursive(Map<Integer, List<Integer>> graph, 
                                              int start) {
        List<Integer> result = new ArrayList<>();
        Set<Integer> visited = new HashSet<>();
        dfsHelper(graph, start, visited, result);
        return result;
    }
    
    private static void dfsHelper(Map<Integer, List<Integer>> graph, int node,
                                  Set<Integer> visited, List<Integer> result) {
        visited.add(node);
        result.add(node);
        
        for (int neighbor : graph.getOrDefault(node, Collections.emptyList())) {
            if (!visited.contains(neighbor)) {
                dfsHelper(graph, neighbor, visited, result);
            }
        }
    }
    
    // Iterative DFS
    public static List<Integer> dfsIterative(Map<Integer, List<Integer>> graph, 
                                              int start) {
        List<Integer> result = new ArrayList<>();
        Set<Integer> visited = new HashSet<>();
        Stack<Integer> stack = new Stack<>();
        
        stack.push(start);
        
        while (!stack.isEmpty()) {
            int node = stack.pop();
            
            if (!visited.contains(node)) {
                visited.add(node);
                result.add(node);
                
                List<Integer> neighbors = graph.getOrDefault(node, 
                    Collections.emptyList());
                for (int i = neighbors.size() - 1; i >= 0; i--) {
                    if (!visited.contains(neighbors.get(i))) {
                        stack.push(neighbors.get(i));
                    }
                }
            }
        }
        
        return result;
    }
}
```

---

## Question 20: Implement a Binary Search Tree (BST)

### Answer:

**BST Property**: Left subtree < Node < Right subtree

### Python Implementation:

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Insert value into BST - O(log n) average, O(n) worst."""
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value) -> bool:
        """Search for value - O(log n) average."""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value) -> bool:
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def inorder(self) -> list:
        """Inorder traversal - returns sorted list."""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def find_min(self):
        """Find minimum value - O(log n)."""
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.value
    
    def find_max(self):
        """Find maximum value - O(log n)."""
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.value

# Usage
bst = BST()
for val in [15, 10, 20, 5, 12, 17, 25]:
    bst.insert(val)

print(bst.inorder())    # [5, 10, 12, 15, 17, 20, 25] - sorted!
print(bst.search(12))   # True
print(bst.find_min())   # 5
print(bst.find_max())   # 25
```

### Java Implementation:

```java
public class BST {
    
    private class TreeNode {
        int value;
        TreeNode left, right;
        
        TreeNode(int value) {
            this.value = value;
        }
    }
    
    private TreeNode root;
    
    public void insert(int value) {
        root = insertRecursive(root, value);
    }
    
    private TreeNode insertRecursive(TreeNode node, int value) {
        if (node == null) {
            return new TreeNode(value);
        }
        
        if (value < node.value) {
            node.left = insertRecursive(node.left, value);
        } else {
            node.right = insertRecursive(node.right, value);
        }
        
        return node;
    }
    
    public boolean search(int value) {
        return searchRecursive(root, value);
    }
    
    private boolean searchRecursive(TreeNode node, int value) {
        if (node == null) {
            return false;
        }
        if (value == node.value) {
            return true;
        }
        if (value < node.value) {
            return searchRecursive(node.left, value);
        }
        return searchRecursive(node.right, value);
    }
    
    public List<Integer> inorder() {
        List<Integer> result = new ArrayList<>();
        inorderRecursive(root, result);
        return result;
    }
    
    private void inorderRecursive(TreeNode node, List<Integer> result) {
        if (node != null) {
            inorderRecursive(node.left, result);
            result.add(node.value);
            inorderRecursive(node.right, result);
        }
    }
}
```

---

## Question 21: Implement a HashMap (Hash Table)

### Answer:

**HashMap** stores key-value pairs with O(1) average lookup using hashing.

### Python Implementation:

```python
class HashMap:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]
        self.load_factor_threshold = 0.75
    
    def _hash(self, key) -> int:
        """Hash function."""
        return hash(key) % self.capacity
    
    def put(self, key, value):
        """Insert or update key-value pair - O(1) average."""
        if self.size / self.capacity >= self.load_factor_threshold:
            self._resize()
        
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # Check if key exists, update value
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # Key doesn't exist, add new pair
        bucket.append((key, value))
        self.size += 1
    
    def get(self, key, default=None):
        """Get value by key - O(1) average."""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        return default
    
    def remove(self, key) -> bool:
        """Remove key-value pair - O(1) average."""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
        
        return False
    
    def contains(self, key) -> bool:
        """Check if key exists - O(1) average."""
        index = self._hash(key)
        return any(k == key for k, v in self.buckets[index])
    
    def _resize(self):
        """Double capacity when load factor exceeded."""
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

# Usage
hm = HashMap()
hm.put("account_001", 5000)
hm.put("account_002", 3000)
print(hm.get("account_001"))  # 5000
print(hm.contains("account_003"))  # False
```

### Java Implementation:

```java
public class HashMap<K, V> {
    
    private class Entry {
        K key;
        V value;
        Entry next;  // For chaining
        
        Entry(K key, V value) {
            this.key = key;
            this.value = value;
        }
    }
    
    private Entry[] buckets;
    private int size;
    private int capacity;
    private static final double LOAD_FACTOR = 0.75;
    
    @SuppressWarnings("unchecked")
    public HashMap(int capacity) {
        this.capacity = capacity;
        this.buckets = (Entry[]) new Object[capacity];
        this.size = 0;
    }
    
    public HashMap() {
        this(16);
    }
    
    private int hash(K key) {
        return Math.abs(key.hashCode()) % capacity;
    }
    
    public void put(K key, V value) {
        if ((double) size / capacity >= LOAD_FACTOR) {
            resize();
        }
        
        int index = hash(key);
        Entry current = buckets[index];
        
        while (current != null) {
            if (current.key.equals(key)) {
                current.value = value;  // Update
                return;
            }
            current = current.next;
        }
        
        // Add new entry at head
        Entry newEntry = new Entry(key, value);
        newEntry.next = buckets[index];
        buckets[index] = newEntry;
        size++;
    }
    
    public V get(K key) {
        int index = hash(key);
        Entry current = buckets[index];
        
        while (current != null) {
            if (current.key.equals(key)) {
                return current.value;
            }
            current = current.next;
        }
        
        return null;
    }
    
    public boolean containsKey(K key) {
        return get(key) != null;
    }
    
    @SuppressWarnings("unchecked")
    private void resize() {
        Entry[] oldBuckets = buckets;
        capacity *= 2;
        buckets = (Entry[]) new Object[capacity];
        size = 0;
        
        for (Entry entry : oldBuckets) {
            while (entry != null) {
                put(entry.key, entry.value);
                entry = entry.next;
            }
        }
    }
}
```

---

## Question 22: Reverse a Linked List

### Answer:

### Python Implementation:

```python
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_iterative(head: ListNode) -> ListNode:
    """Reverse linked list iteratively - O(n) time, O(1) space."""
    prev = None
    current = head
    
    while current:
        next_node = current.next  # Save next
        current.next = prev        # Reverse link
        prev = current             # Move prev forward
        current = next_node        # Move current forward
    
    return prev

def reverse_recursive(head: ListNode) -> ListNode:
    """Reverse linked list recursively - O(n) time, O(n) space."""
    if head is None or head.next is None:
        return head
    
    new_head = reverse_recursive(head.next)
    head.next.next = head  # Make next node point back
    head.next = None       # Remove old forward link
    
    return new_head

# Helper function to create list
def create_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper to print list
def print_list(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    print(" -> ".join(map(str, values)))

# Usage
head = create_list([1, 2, 3, 4, 5])
print_list(head)  # 1 -> 2 -> 3 -> 4 -> 5

reversed_head = reverse_iterative(head)
print_list(reversed_head)  # 5 -> 4 -> 3 -> 2 -> 1
```

### Java Implementation:

```java
public class LinkedListReversal {
    
    public static class ListNode {
        int value;
        ListNode next;
        
        ListNode(int value) {
            this.value = value;
        }
    }
    
    // Iterative - O(n) time, O(1) space
    public static ListNode reverseIterative(ListNode head) {
        ListNode prev = null;
        ListNode current = head;
        
        while (current != null) {
            ListNode nextNode = current.next;
            current.next = prev;
            prev = current;
            current = nextNode;
        }
        
        return prev;
    }
    
    // Recursive - O(n) time, O(n) space
    public static ListNode reverseRecursive(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        ListNode newHead = reverseRecursive(head.next);
        head.next.next = head;
        head.next = null;
        
        return newHead;
    }
}
```

---

# 🧮 PART 4: DYNAMIC PROGRAMMING (Questions 23-27)

---

## Question 23: Fibonacci Sequence

### Answer:

**Problem**: Calculate the nth Fibonacci number (0, 1, 1, 2, 3, 5, 8, ...)

### Python Implementation:

```python
# Method 1: Recursive (exponential time - BAD)
def fib_recursive(n: int) -> int:
    """O(2^n) time - very slow!"""
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# Method 2: Memoization (Top-down DP)
def fib_memo(n: int, memo: dict = None) -> int:
    """O(n) time, O(n) space."""
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# Method 3: Tabulation (Bottom-up DP)
def fib_tabulation(n: int) -> int:
    """O(n) time, O(n) space."""
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

# Method 4: Space Optimized
def fib_optimized(n: int) -> int:
    """O(n) time, O(1) space - BEST."""
    if n <= 1:
        return n
    
    prev2, prev1 = 0, 1
    
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1

# Usage
print(fib_optimized(10))  # 55
```

### Java Implementation:

```java
public class Fibonacci {
    
    // Memoization
    public static long fibMemo(int n, Map<Integer, Long> memo) {
        if (memo == null) memo = new HashMap<>();
        if (memo.containsKey(n)) return memo.get(n);
        if (n <= 1) return n;
        
        long result = fibMemo(n - 1, memo) + fibMemo(n - 2, memo);
        memo.put(n, result);
        return result;
    }
    
    // Tabulation
    public static long fibTab(int n) {
        if (n <= 1) return n;
        
        long[] dp = new long[n + 1];
        dp[1] = 1;
        
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        return dp[n];
    }
    
    // Space Optimized
    public static long fibOptimized(int n) {
        if (n <= 1) return n;
        
        long prev2 = 0, prev1 = 1;
        
        for (int i = 2; i <= n; i++) {
            long current = prev1 + prev2;
            prev2 = prev1;
            prev1 = current;
        }
        
        return prev1;
    }
}
```

---

## Question 24: Climbing Stairs

### Answer:

**Problem**: You can climb 1 or 2 stairs at a time. How many ways to reach the top of n stairs?

```
Example: n = 3
Ways: [1,1,1], [1,2], [2,1] = 3 ways
```

### Python Implementation:

```python
def climb_stairs(n: int) -> int:
    """
    Dynamic Programming solution.
    dp[i] = number of ways to reach stair i
    dp[i] = dp[i-1] + dp[i-2] (come from 1 or 2 stairs below)
    
    Time: O(n), Space: O(1)
    """
    if n <= 2:
        return n
    
    # Same as Fibonacci!
    prev2, prev1 = 1, 2
    
    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1

# With memoization
def climb_stairs_memo(n: int, memo: dict = None) -> int:
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    if n <= 2:
        return n
    
    memo[n] = climb_stairs_memo(n - 1, memo) + climb_stairs_memo(n - 2, memo)
    return memo[n]

# Usage
print(climb_stairs(5))  # 8
```

### Java Implementation:

```java
public static int climbStairs(int n) {
    if (n <= 2) return n;
    
    int prev2 = 1, prev1 = 2;
    
    for (int i = 3; i <= n; i++) {
        int current = prev1 + prev2;
        prev2 = prev1;
        prev1 = current;
    }
    
    return prev1;
}
```

---

## Question 25: Coin Change (Minimum Coins)

### Answer:

**Problem**: Given coins of different denominations and a total amount, find the minimum number of coins needed.

```
Example: coins = [1, 2, 5], amount = 11
Answer: 3 (5 + 5 + 1)
```

### Python Implementation:

```python
def coin_change(coins: list, amount: int) -> int:
    """
    DP: dp[i] = minimum coins needed for amount i
    dp[i] = min(dp[i], dp[i - coin] + 1) for each coin
    
    Time: O(amount * len(coins)), Space: O(amount)
    """
    # Initialize with infinity (impossible)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins needed for amount 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Example trace for coins=[1,2,5], amount=11:
# dp[0] = 0
# dp[1] = dp[0] + 1 = 1  (use coin 1)
# dp[2] = dp[0] + 1 = 1  (use coin 2)
# dp[3] = dp[1] + 1 = 2  (use coin 2)
# dp[4] = dp[2] + 1 = 2  (use coin 2)
# dp[5] = dp[0] + 1 = 1  (use coin 5)
# dp[6] = dp[5] + 1 = 2  (use coin 1)
# dp[7] = dp[5] + 1 = 2  (use coin 2)
# dp[10] = dp[5] + 1 = 2 (use coin 5)
# dp[11] = dp[10] + 1 = 3 (use coin 1)

# Usage
print(coin_change([1, 2, 5], 11))  # 3
print(coin_change([2], 3))         # -1 (impossible)
```

### Java Implementation:

```java
public static int coinChange(int[] coins, int amount) {
    int[] dp = new int[amount + 1];
    Arrays.fill(dp, amount + 1);  // Impossible value
    dp[0] = 0;
    
    for (int i = 1; i <= amount; i++) {
        for (int coin : coins) {
            if (coin <= i) {
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
    }
    
    return dp[amount] > amount ? -1 : dp[amount];
}
```

---

## Question 26: Longest Common Subsequence (LCS)

### Answer:

**Problem**: Find the longest subsequence common to two strings.

```
Example: text1 = "ABCDGH", text2 = "AEDFHR"
LCS = "ADH" (length 3)
```

### Python Implementation:

```python
def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    DP: dp[i][j] = LCS of text1[0:i] and text2[0:j]
    
    If text1[i-1] == text2[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1
    Else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    Time: O(m * n), Space: O(m * n)
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def lcs_with_string(text1: str, text2: str) -> str:
    """Return the actual LCS string."""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Backtrack to find LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))

# Usage
print(longest_common_subsequence("ABCDGH", "AEDFHR"))  # 3
print(lcs_with_string("ABCDGH", "AEDFHR"))            # "ADH"
```

### Java Implementation:

```java
public static int longestCommonSubsequence(String text1, String text2) {
    int m = text1.length(), n = text2.length();
    int[][] dp = new int[m + 1][n + 1];
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    
    return dp[m][n];
}
```

---

## Question 27: 0/1 Knapsack Problem

### Answer:

**Problem**: Given weights and values of n items, find maximum value that can be put in a knapsack of capacity W.

```
Example: 
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7
Answer: 9 (items with weight 3 and 4, values 4 and 5)
```

### Python Implementation:

```python
def knapsack(weights: list, values: list, capacity: int) -> int:
    """
    DP: dp[i][w] = max value using first i items with capacity w
    
    If weight[i-1] <= w:
        dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i-1]] + value[i-1])
    Else:
        dp[i][w] = dp[i-1][w]
    
    Time: O(n * W), Space: O(n * W)
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item i
            dp[i][w] = dp[i - 1][w]
            
            # Take item i (if it fits)
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
    
    return dp[n][capacity]

def knapsack_optimized(weights: list, values: list, capacity: int) -> int:
    """Space optimized - O(W) space."""
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        # Traverse backwards to avoid using updated values
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]

# Usage
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7
print(knapsack(weights, values, capacity))  # 9
```

### Java Implementation:

```java
public static int knapsack(int[] weights, int[] values, int capacity) {
    int n = weights.length;
    int[][] dp = new int[n + 1][capacity + 1];
    
    for (int i = 1; i <= n; i++) {
        for (int w = 0; w <= capacity; w++) {
            dp[i][w] = dp[i - 1][w];  // Don't take
            
            if (weights[i - 1] <= w) {
                dp[i][w] = Math.max(
                    dp[i][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                );
            }
        }
    }
    
    return dp[n][capacity];
}
```

---

# 📐 PART 5: UML (Questions 28-30)

---

## Question 28: Draw a UML Class Diagram for a Banking System

### Answer:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        BANKING SYSTEM CLASS DIAGRAM                          │
└─────────────────────────────────────────────────────────────────────────────┘

                           ┌──────────────────────┐
                           │        Bank          │
                           ├──────────────────────┤
                           │ - bankId: String     │
                           │ - name: String       │
                           │ - address: String    │
                           ├──────────────────────┤
                           │ + addClient()        │
                           │ + getClients(): List │
                           └──────────┬───────────┘
                                      │ 1
                                      │ manages
                                      ◇
                                      │ *
                           ┌──────────────────────┐
                           │       Client         │
                           ├──────────────────────┤
                           │ - clientId: String   │
                           │ - name: String       │
                           │ - email: String      │
                           │ - phone: String      │
                           ├──────────────────────┤
                           │ + openAccount()      │
                           │ + getAccounts(): List│
                           └──────────┬───────────┘
                                      │ 1
                                      │ owns
                                      │
                                      │ 1..*
                           ┌──────────────────────┐
                           │    «abstract»        │
                           │      Account         │
                           ├──────────────────────┤
                           │ # accountNumber: String│
                           │ # balance: Decimal   │
                           │ # status: String     │
                           ├──────────────────────┤
                           │ + deposit(amount)    │
                           │ + withdraw(amount)   │
                           │ + getBalance(): Decimal│
                           └──────────┬───────────┘
                                      △
             ┌────────────────────────┼────────────────────────┐
             │                        │                        │
  ┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
  │  SavingsAccount  │    │ CheckingAccount  │    │  CreditAccount   │
  ├──────────────────┤    ├──────────────────┤    ├──────────────────┤
  │- interestRate: % │    │- overdraftLimit  │    │- creditLimit     │
  │- withdrawLimit   │    │- checkFee        │    │- apr: %          │
  ├──────────────────┤    ├──────────────────┤    ├──────────────────┤
  │+ calcInterest()  │    │+ processCheck()  │    │+ makePurchase()  │
  └──────────────────┘    └──────────────────┘    └──────────────────┘
             │
             │ 1..*
             │ has
             ◆
             │
  ┌──────────────────────┐
  │    Transaction       │
  ├──────────────────────┤
  │ - transactionId      │
  │ - amount: Decimal    │
  │ - type: String       │
  │ - timestamp: DateTime│
  │ - status: String     │
  ├──────────────────────┤
  │ + execute(): boolean │
  │ + cancel()           │
  └──────────────────────┘
```

### Relationships:

| Symbol | Relationship | Meaning |
|--------|--------------|---------|
| `───────` | Association | "uses" or "knows" |
| `◇───────` | Aggregation | "has-a" (independent) |
| `◆───────` | Composition | "owns" (dependent lifecycle) |
| `────▷` | Inheritance | "is-a" (extends) |
| `─ ─ ▷` | Realization | "implements" (interface) |

### Multiplicity:
- `1` = exactly one
- `*` = zero or more
- `1..*` = one or more
- `0..1` = zero or one

---

## Question 29: Draw a UML Sequence Diagram for ATM Withdrawal

### Answer:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ATM WITHDRAWAL SEQUENCE DIAGRAM                           │
└─────────────────────────────────────────────────────────────────────────────┘

:Customer     :ATM            :BankServer       :Account         :Transaction
    │           │                  │                │                  │
    │ insertCard│                  │                │                  │
    │──────────>│                  │                │                  │
    │           │                  │                │                  │
    │           │ validateCard     │                │                  │
    │           │─────────────────>│                │                  │
    │           │   cardValid      │                │                  │
    │           │<─────────────────│                │                  │
    │           │                  │                │                  │
    │ enterPIN  │                  │                │                  │
    │──────────>│                  │                │                  │
    │           │ verifyPIN        │                │                  │
    │           │─────────────────>│                │                  │
    │           │   pinOK          │                │                  │
    │           │<─────────────────│                │                  │
    │           │                  │                │                  │
    │selectWithdraw(500)           │                │                  │
    │──────────>│                  │                │                  │
    │           │                  │                │                  │
    │           │ checkBalance(500)│                │                  │
    │           │─────────────────>│ getBalance     │                  │
    │           │                  │───────────────>│                  │
    │           │                  │   balance=1000 │                  │
    │           │                  │<───────────────│                  │
    │           │   balanceOK      │                │                  │
    │           │<─────────────────│                │                  │
    │           │                  │                │                  │
    ┌───────────────────────────────────────────────────────────────────────┐
    │ alt [balance >= 500]                                                   │
    ├───────────────────────────────────────────────────────────────────────┤
    │           │ processWithdraw  │                │                  │    │
    │           │─────────────────>│ debit(500)     │                  │    │
    │           │                  │───────────────>│                  │    │
    │           │                  │   success      │                  │    │
    │           │                  │<───────────────│                  │    │
    │           │                  │                │                  │    │
    │           │                  │ createTransaction                 │    │
    │           │                  │────────────────────────────────────>   │
    │           │                  │   transactionId                   │    │
    │           │                  │<────────────────────────────────────   │
    │           │                  │                │                  │    │
    │           │   withdrawalOK   │                │                  │    │
    │           │<─────────────────│                │                  │    │
    │           │                  │                │                  │    │
    │dispenseCash                  │                │                  │    │
    │<──────────│                  │                │                  │    │
    │           │                  │                │                  │    │
    │printReceipt                  │                │                  │    │
    │<──────────│                  │                │                  │    │
    ├───────────────────────────────────────────────────────────────────────┤
    │ [else] insufficient balance                                            │
    ├───────────────────────────────────────────────────────────────────────┤
    │           │ insufficientFunds│                │                  │    │
    │           │<─────────────────│                │                  │    │
    │           │                  │                │                  │    │
    │displayError("Insufficient funds")             │                  │    │
    │<──────────│                  │                │                  │    │
    └───────────────────────────────────────────────────────────────────────┘
    │           │                  │                │                  │
    │ ejectCard │                  │                │                  │
    │<──────────│                  │                │                  │
    │           │                  │                │                  │
```

### Key Elements:
- **Lifelines**: Vertical dashed lines showing object existence
- **Activation boxes**: Rectangles showing when object is active
- **Messages**: Arrows (solid = synchronous, dashed = return)
- **alt fragment**: Alternative flows (if/else)
- **loop fragment**: Repeated actions
- **opt fragment**: Optional actions

---

## Question 30: Draw a UML Use Case Diagram for Online Banking

### Answer:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       ONLINE BANKING USE CASE DIAGRAM                        │
└─────────────────────────────────────────────────────────────────────────────┘

     ┌───────────────────────────────────────────────────────────────────┐
     │                    Online Banking System                           │
     │                                                                    │
     │                                                                    │
     │        ┌─────────────────┐                                        │
     │        │    View         │                                        │
👤────┼────────│   Account      │                                        │
Customer      │   Balance      │                                        │
     │        └────────┬────────┘                                        │
     │                 │                                                  │
     │            «include»                                               │
     │                 ▼                                                  │
     │        ┌─────────────────┐                                        │
     │        │   Authenticate  │◀──────────────────────────┐            │
     │        │     User        │                           │            │
     │        └─────────────────┘                      «include»         │
     │                 ▲                                    │            │
     │            «include»                                 │            │
     │                 │                                    │            │
     │        ┌─────────────────┐                           │            │
👤────┼────────│    Transfer    │───────────────────────────┤            │
Customer      │     Money      │                           │            │
     │        └────────┬────────┘                           │            │
     │                 │                                    │            │
     │           «extend»                                   │            │
     │                 ▼                                    │            │
     │        ┌─────────────────┐                           │            │
     │        │ Send Transfer   │                           │            │
     │        │  Notification   │                           │            │
     │        └─────────────────┘                           │            │
     │                                                      │            │
     │        ┌─────────────────┐                           │            │
👤────┼────────│  Pay Bills     │───────────────────────────┘            │
Customer      │                │                                        │
     │        └─────────────────┘                                        │
     │                                                                    │
     │        ┌─────────────────┐                                        │
👤────┼────────│ View Transaction│                                       │
Customer      │    History      │                                        │
     │        └─────────────────┘                                        │
     │                                                                    │
     │        ┌─────────────────┐                                        │
     │        │   Manage        │                                        │
👤────┼────────│   Accounts     │                                        │
Teller        │                │                                        │
     │        └─────────────────┘                                        │
     │                                                                    │
     │        ┌─────────────────┐                                        │
     │        │   Approve       │                                        │
👤────┼────────│    Loans       │                                        │
Manager       │                │                                        │
     │        └─────────────────┘                                        │
     │                                                                    │
     │        ┌─────────────────┐                                        │
     │        │  Generate       │                                        │
👤────┼────────│   Reports      │                                        │
Admin         │                │                                        │
     │        └─────────────────┘                                        │
     │                                                                    │
     └───────────────────────────────────────────────────────────────────┘
                             │
                             │
                           🏦
                     External Bank
                       (Actor)
```

### Use Case Diagram Elements:

| Element | Symbol | Description |
|---------|--------|-------------|
| **Actor** | 👤 Stick figure | External entity (user, system) |
| **Use Case** | Oval | Functionality provided |
| **System Boundary** | Rectangle | Scope of the system |
| **Association** | Line | Actor participates in use case |
| **«include»** | Dashed arrow | Required behavior |
| **«extend»** | Dashed arrow | Optional behavior |
| **Generalization** | Arrow with triangle | Actor inheritance |

### Key Rules:
1. **Actors are OUTSIDE the system boundary**
2. **«include»** arrow points FROM base TO included use case
3. **«extend»** arrow points FROM extension TO base use case
4. Use cases describe WHAT the system does, not HOW

---

# 📋 QUICK REFERENCE CHEAT SHEET

## Complexity Summary

| Algorithm/Structure | Time (Average) | Time (Worst) | Space |
|---------------------|----------------|--------------|-------|
| Binary Search | O(log n) | O(log n) | O(1) |
| Quick Sort | O(n log n) | O(n²) | O(log n) |
| Merge Sort | O(n log n) | O(n log n) | O(n) |
| BFS/DFS | O(V + E) | O(V + E) | O(V) |
| HashMap | O(1) | O(n) | O(n) |
| BST | O(log n) | O(n) | O(n) |

## HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Server Error |

## ACID Properties

- **A**tomicity: All or nothing
- **C**onsistency: Valid state to valid state
- **I**solation: Transactions don't interfere
- **D**urability: Committed = permanent

## SOLID Principles

- **S**ingle Responsibility: One reason to change
- **O**pen/Closed: Open for extension, closed for modification
- **L**iskov Substitution: Subtypes must be substitutable
- **I**nterface Segregation: No unused methods
- **D**ependency Inversion: Depend on abstractions

---

**Good luck with your exam! 🎯**
