# Étude de Cas Backend — Niveau Basique

## 🎯 Objectif

Créer une API REST complète pour un système bancaire simple avec authentification, CRUD de comptes, et gestion de transactions. Durée: 3-4 heures.

---

## 📋 Prérequis

- Python 3.9+ OU Node.js 18+ OU Java 17+
- Connaissance de base en programmation
- Compréhension de HTTP et JSON
- Base de données (PostgreSQL ou SQLite)

---

## 🏗️ Architecture MVC

```
┌─────────────┐
│  Client     │ (Postman, Frontend)
└──────┬──────┘
       │ HTTP Request
┌──────▼──────────┐
│  Controller     │ ← Routes, validation basique
└──────┬──────────┘
       │
┌──────▼──────────┐
│  Model          │ ← Logique métier + DB
└──────┬──────────┘
       │
┌──────▼──────────┐
│  Database       │ (PostgreSQL)
└─────────────────┘
```

---

## 📁 Structure du Projet

### Python (FastAPI)

```
banking-api/
├── main.py              # Point d'entrée
├── models.py            # Modèles DB
├── auth.py              # Authentification
├── database.py          # Configuration DB
├── schemas.py           # Validation Pydantic
├── requirements.txt     # Dépendances
└── tests/
    └── test_api.py
```

### Node.js (Express)

```
banking-api/
├── index.js             # Point d'entrée
├── models/
│   ├── account.js
│   └── transaction.js
├── routes/
│   ├── auth.js
│   └── accounts.js
├── middleware/
│   └── auth.js
├── config/
│   └── database.js
└── package.json
```

---

## 🚀 Partie 1: Configuration Initiale

### Python (FastAPI)

**1. Installer les dépendances**

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic python-jose passlib bcrypt
```

**2. Configuration de la base de données (`database.py`)**

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@localhost/banking"
# Pour SQLite: DATABASE_URL = "sqlite:///./banking.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Dependency pour obtenir une session DB"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

**3. Modèles de données (`models.py`)**

```python
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    accounts = relationship("Account", back_populates="owner")

class Account(Base):
    __tablename__ = "accounts"
    
    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String, unique=True, index=True, nullable=False)
    account_type = Column(String, nullable=False)  # COURANT, EPARGNE
    balance = Column(Float, default=0.0)
    currency = Column(String, default="HTG")
    owner_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    owner = relationship("User", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account")

class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)  # DEPOT, RETRAIT, VIREMENT
    description = Column(String)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    account = relationship("Account", back_populates="transactions")
```

**4. Schémas de validation (`schemas.py`)**

```python
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    full_name: str

class UserResponse(BaseModel):
    id: int
    email: str
    full_name: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class AccountCreate(BaseModel):
    account_type: str = Field(..., regex="^(COURANT|EPARGNE)$")
    currency: str = "HTG"

class AccountResponse(BaseModel):
    id: int
    account_number: str
    account_type: str
    balance: float
    currency: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class TransactionCreate(BaseModel):
    amount: float = Field(..., gt=0)
    type: str = Field(..., regex="^(DEPOT|RETRAIT)$")
    description: Optional[str] = None

class TransactionResponse(BaseModel):
    id: int
    amount: float
    type: str
    description: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True
```

---

## 🔐 Partie 2: Authentification

**Module d'authentification (`auth.py`)**

```python
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from database import get_db
import models

# Configuration
SECRET_KEY = "votre-cle-secrete-changez-moi"  # À mettre dans .env
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()

def hash_password(password: str) -> str:
    """Hasher un mot de passe"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Vérifier un mot de passe"""
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Créer un JWT token"""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    """Obtenir l'utilisateur actuel à partir du token"""
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise credentials_exception
    
    return user
```

---

## 🌐 Partie 3: API REST Endpoints

**Application principale (`main.py`)**

```python
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import engine, get_db
from auth import (
    hash_password, 
    verify_password, 
    create_access_token, 
    get_current_user,
    ACCESS_TOKEN_EXPIRE_MINUTES
)
from datetime import timedelta
import random
import string

# Créer les tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Banking API", version="1.0.0")

def generate_account_number() -> str:
    """Générer un numéro de compte unique"""
    return "".join(random.choices(string.digits, k=12))

# ============= AUTHENTICATION =============

@app.post("/auth/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Créer un nouveau utilisateur"""
    # Vérifier si l'email existe déjà
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    
    # Créer l'utilisateur
    hashed_pwd = hash_password(user.password)
    db_user = models.User(
        email=user.email,
        hashed_password=hashed_pwd,
        full_name=user.full_name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

@app.post("/auth/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    """Authentifier un utilisateur et retourner un token"""
    user = db.query(models.User).filter(models.User.email == email).first()
    
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password"
        )
    
    access_token = create_access_token(
        data={"sub": str(user.id)},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email,
            "full_name": user.full_name
        }
    }

# ============= ACCOUNTS =============

@app.post("/accounts", response_model=schemas.AccountResponse, status_code=201)
def create_account(
    account: schemas.AccountCreate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Créer un nouveau compte pour l'utilisateur connecté"""
    db_account = models.Account(
        account_number=generate_account_number(),
        account_type=account.account_type,
        currency=account.currency,
        owner_id=current_user.id
    )
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    
    return db_account

@app.get("/accounts", response_model=List[schemas.AccountResponse])
def list_accounts(
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Lister tous les comptes de l'utilisateur"""
    accounts = db.query(models.Account).filter(
        models.Account.owner_id == current_user.id
    ).all()
    return accounts

@app.get("/accounts/{account_id}", response_model=schemas.AccountResponse)
def get_account(
    account_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Obtenir les détails d'un compte"""
    account = db.query(models.Account).filter(
        models.Account.id == account_id,
        models.Account.owner_id == current_user.id
    ).first()
    
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    
    return account

@app.delete("/accounts/{account_id}", status_code=204)
def delete_account(
    account_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Fermer un compte (le supprimer)"""
    account = db.query(models.Account).filter(
        models.Account.id == account_id,
        models.Account.owner_id == current_user.id
    ).first()
    
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    
    # Vérifier que le solde est à zéro
    if account.balance != 0:
        raise HTTPException(
            status_code=400,
            detail="Cannot close account with non-zero balance"
        )
    
    db.delete(account)
    db.commit()
    
    return None

# ============= TRANSACTIONS =============

@app.post("/accounts/{account_id}/transactions", 
          response_model=schemas.TransactionResponse,
          status_code=201)
def create_transaction(
    account_id: int,
    transaction: schemas.TransactionCreate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Créer une transaction (dépôt ou retrait)"""
    # Vérifier que le compte existe et appartient à l'utilisateur
    account = db.query(models.Account).filter(
        models.Account.id == account_id,
        models.Account.owner_id == current_user.id
    ).first()
    
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    
    # Valider le retrait
    if transaction.type == "RETRAIT":
        if account.balance < transaction.amount:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient balance. Current: {account.balance}"
            )
        account.balance -= transaction.amount
    else:  # DEPOT
        account.balance += transaction.amount
    
    # Créer la transaction
    db_transaction = models.Transaction(
        amount=transaction.amount,
        type=transaction.type,
        description=transaction.description,
        account_id=account_id
    )
    
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    
    return db_transaction

@app.get("/accounts/{account_id}/transactions",
         response_model=List[schemas.TransactionResponse])
def list_transactions(
    account_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Lister toutes les transactions d'un compte"""
    # Vérifier que le compte existe et appartient à l'utilisateur
    account = db.query(models.Account).filter(
        models.Account.id == account_id,
        models.Account.owner_id == current_user.id
    ).first()
    
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    
    transactions = db.query(models.Transaction).filter(
        models.Transaction.account_id == account_id
    ).order_by(models.Transaction.created_at.desc()).all()
    
    return transactions

@app.get("/accounts/{account_id}/balance")
def get_balance(
    account_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Obtenir le solde d'un compte"""
    account = db.query(models.Account).filter(
        models.Account.id == account_id,
        models.Account.owner_id == current_user.id
    ).first()
    
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    
    return {
        "account_id": account.id,
        "account_number": account.account_number,
        "balance": account.balance,
        "currency": account.currency
    }

# ============= HEALTH CHECK =============

@app.get("/health")
def health_check():
    """Vérifier que l'API est en ligne"""
    return {"status": "healthy", "service": "banking-api"}

# Lancer l'application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

---

## 🧪 Partie 4: Tests

**Tests basiques (`tests/test_api.py`)**

```python
from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

def test_health_check():
    """Test de santé de l'API"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_register_user():
    """Test d'inscription"""
    response = client.post("/auth/register", json={
        "email": "test@example.com",
        "password": "password123",
        "full_name": "Test User"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_login():
    """Test de connexion"""
    # D'abord, créer un utilisateur
    client.post("/auth/register", json={
        "email": "login@example.com",
        "password": "password123",
        "full_name": "Login User"
    })
    
    # Puis, se connecter
    response = client.post("/auth/login", params={
        "email": "login@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_create_account_authenticated():
    """Test de création de compte avec authentification"""
    # Créer un utilisateur et obtenir un token
    client.post("/auth/register", json={
        "email": "account@example.com",
        "password": "password123",
        "full_name": "Account User"
    })
    
    login_response = client.post("/auth/login", params={
        "email": "account@example.com",
        "password": "password123"
    })
    token = login_response.json()["access_token"]
    
    # Créer un compte
    response = client.post(
        "/accounts",
        json={"account_type": "COURANT", "currency": "HTG"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["account_type"] == "COURANT"
    assert data["balance"] == 0.0

def test_create_transaction():
    """Test de création de transaction"""
    # Setup: créer utilisateur, login, créer compte
    client.post("/auth/register", json={
        "email": "trans@example.com",
        "password": "password123",
        "full_name": "Trans User"
    })
    
    login_response = client.post("/auth/login", params={
        "email": "trans@example.com",
        "password": "password123"
    })
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    account_response = client.post(
        "/accounts",
        json={"account_type": "COURANT"},
        headers=headers
    )
    account_id = account_response.json()["id"]
    
    # Créer une transaction de dépôt
    response = client.post(
        f"/accounts/{account_id}/transactions",
        json={
            "amount": 1000.0,
            "type": "DEPOT",
            "description": "Dépôt initial"
        },
        headers=headers
    )
    assert response.status_code == 201
    data = response.json()
    assert data["amount"] == 1000.0
    assert data["type"] == "DEPOT"

def test_insufficient_balance():
    """Test de retrait avec solde insuffisant"""
    # Setup
    client.post("/auth/register", json={
        "email": "insuf@example.com",
        "password": "password123",
        "full_name": "Insuf User"
    })
    
    login_response = client.post("/auth/login", params={
        "email": "insuf@example.com",
        "password": "password123"
    })
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    account_response = client.post(
        "/accounts",
        json={"account_type": "COURANT"},
        headers=headers
    )
    account_id = account_response.json()["id"]
    
    # Tenter un retrait sans solde
    response = client.post(
        f"/accounts/{account_id}/transactions",
        json={
            "amount": 100.0,
            "type": "RETRAIT",
            "description": "Tentative de retrait"
        },
        headers=headers
    )
    assert response.status_code == 400
    assert "Insufficient balance" in response.json()["detail"]
```

**Exécuter les tests:**

```bash
pytest tests/ -v
```

---

## 🚀 Partie 5: Lancer l'Application

**1. Créer la base de données PostgreSQL**

```bash
# Se connecter à PostgreSQL
psql -U postgres

# Créer la base de données
CREATE DATABASE banking;

# Créer un utilisateur
CREATE USER bankinguser WITH PASSWORD 'password123';
GRANT ALL PRIVILEGES ON DATABASE banking TO bankinguser;
```

**2. Lancer l'API**

```bash
# Avec rechargement automatique
uvicorn main:app --reload

# L'API est disponible sur http://localhost:8000
# Documentation interactive: http://localhost:8000/docs
```

---

## 🧪 Partie 6: Tester avec Postman

### 1. Créer un utilisateur

```
POST http://localhost:8000/auth/register
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "securepass123",
  "full_name": "John Doe"
}
```

### 2. Se connecter

```
POST http://localhost:8000/auth/login?email=john@example.com&password=securepass123
```

Copier le `access_token` de la réponse.

### 3. Créer un compte (avec token)

```
POST http://localhost:8000/accounts
Authorization: Bearer <votre_token_ici>
Content-Type: application/json

{
  "account_type": "COURANT",
  "currency": "HTG"
}
```

### 4. Faire un dépôt

```
POST http://localhost:8000/accounts/1/transactions
Authorization: Bearer <votre_token_ici>
Content-Type: application/json

{
  "amount": 5000.0,
  "type": "DEPOT",
  "description": "Dépôt initial"
}
```

### 5. Consulter le solde

```
GET http://localhost:8000/accounts/1/balance
Authorization: Bearer <votre_token_ici>
```

---

## 📝 Exercices Pratiques

### Exercice 1: Ajouter la gestion d'erreurs

Améliorer la gestion d'erreurs avec des messages personnalisés:

```python
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"error": "Invalid value", "detail": str(exc)}
    )
```

### Exercice 2: Ajouter un middleware de logging

```python
import logging
import time
from fastapi import Request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    
    logger.info(
        f"{request.method} {request.url.path} "
        f"- Status: {response.status_code} "
        f"- Duration: {duration:.2f}s"
    )
    
    return response
```

### Exercice 3: Ajouter la validation de devise

Créer une liste de devises autorisées:

```python
ALLOWED_CURRENCIES = ["HTG", "USD", "EUR"]

class AccountCreate(BaseModel):
    account_type: str = Field(..., regex="^(COURANT|EPARGNE)$")
    currency: str = "HTG"
    
    @validator('currency')
    def validate_currency(cls, v):
        if v not in ALLOWED_CURRENCIES:
            raise ValueError(f"Currency must be one of {ALLOWED_CURRENCIES}")
        return v
```

### Exercice 4: Ajouter un endpoint de virement

Créer un endpoint pour transférer de l'argent entre comptes:

```python
class TransferCreate(BaseModel):
    from_account_id: int
    to_account_number: str
    amount: float = Field(..., gt=0)
    description: Optional[str] = None

@app.post("/transfers", status_code=201)
def create_transfer(
    transfer: TransferCreate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Vérifier le compte source
    from_account = db.query(models.Account).filter(
        models.Account.id == transfer.from_account_id,
        models.Account.owner_id == current_user.id
    ).first()
    
    if not from_account:
        raise HTTPException(status_code=404, detail="Source account not found")
    
    # Vérifier le compte destination
    to_account = db.query(models.Account).filter(
        models.Account.account_number == transfer.to_account_number
    ).first()
    
    if not to_account:
        raise HTTPException(status_code=404, detail="Destination account not found")
    
    # Vérifier le solde
    if from_account.balance < transfer.amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")
    
    # Effectuer le virement
    from_account.balance -= transfer.amount
    to_account.balance += transfer.amount
    
    # Créer les transactions
    debit = models.Transaction(
        amount=transfer.amount,
        type="VIREMENT",
        description=f"Virement vers {to_account.account_number}: {transfer.description}",
        account_id=from_account.id
    )
    
    credit = models.Transaction(
        amount=transfer.amount,
        type="VIREMENT",
        description=f"Virement de {from_account.account_number}: {transfer.description}",
        account_id=to_account.id
    )
    
    db.add(debit)
    db.add(credit)
    db.commit()
    
    return {
        "status": "success",
        "from_account": from_account.account_number,
        "to_account": to_account.account_number,
        "amount": transfer.amount,
        "new_balance": from_account.balance
    }
```

---

## 🎯 Checklist de Complétion

Après avoir terminé cette étude de cas, vous devriez avoir:

- [ ] ✅ Une API REST fonctionnelle avec FastAPI
- [ ] ✅ Authentification JWT avec tokens
- [ ] ✅ CRUD complet pour les comptes
- [ ] ✅ Gestion de transactions (dépôt, retrait)
- [ ] ✅ Validation des données avec Pydantic
- [ ] ✅ Gestion d'erreurs appropriée
- [ ] ✅ Tests unitaires de base
- [ ] ✅ Documentation automatique (Swagger)
- [ ] ✅ Base de données PostgreSQL connectée
- [ ] ✅ Code organisé en modules

---

## 🚀 Prochaines Étapes

Une fois ce niveau maîtrisé, passez au **Niveau Moyen** pour apprendre:

- Architecture en couches (Controller → Service → Repository)
- OAuth2 et refresh tokens
- Caching avec Redis
- Pagination et filtrage avancés
- Tests d'intégration
- Documentation API avancée

---

## 📚 Ressources Complémentaires

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/)
- [JWT Introduction](https://jwt.io/introduction)
- [REST API Best Practices](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)

---

**Bon développement backend !** 🚀
