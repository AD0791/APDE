# Étude de Cas Backend — Niveau Moyen

## 🎯 Objectif

Créer une API bancaire production-ready avec architecture en couches, OAuth2, caching Redis, pagination, rate limiting, tests complets et documentation Swagger. Durée: 5-6 heures.

---

## 🏗️ Architecture en Couches

```
┌─────────────┐
│   Client    │
└──────┬──────┘
       │ HTTP Request
┌──────▼──────────┐
│  Controller     │ ← Routes, validation HTTP
└──────┬──────────┘
       │
┌──────▼──────────┐
│  Service        │ ← Logique métier
└──────┬──────────┘
       │
┌──────▼──────────┐
│  Repository     │ ← Accès données
└──────┬──────────┘
       │
┌──────▼──────────┐
│  Database       │ (PostgreSQL)
└─────────────────┘
```

**Avantages:**
- Séparation des responsabilités (SRP)
- Testabilité accrue
- Réutilisabilité du code
- Maintenance facilitée

---

## 📁 Structure du Projet

```
banking-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # Point d'entrée
│   ├── config.py            # Configuration
│   ├── dependencies.py      # Dépendances FastAPI
│   │
│   ├── models/              # Modèles SQLAlchemy
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── account.py
│   │   └── transaction.py
│   │
│   ├── schemas/             # Schémas Pydantic
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── account.py
│   │   └── transaction.py
│   │
│   ├── repositories/        # Accès données
│   │   ├── __init__.py
│   │   ├── user_repository.py
│   │   ├── account_repository.py
│   │   └── transaction_repository.py
│   │
│   ├── services/            # Logique métier
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── account_service.py
│   │   └── transaction_service.py
│   │
│   ├── controllers/         # Routes HTTP
│   │   ├── __init__.py
│   │   ├── auth_controller.py
│   │   ├── account_controller.py
│   │   └── transaction_controller.py
│   │
│   ├── middleware/          # Middleware
│   │   ├── __init__.py
│   │   ├── rate_limiter.py
│   │   └── logging.py
│   │
│   └── utils/               # Utilitaires
│       ├── __init__.py
│       ├── cache.py
│       └── pagination.py
│
├── tests/                   # Tests
│   ├── unit/
│   │   ├── test_services.py
│   │   └── test_repositories.py
│   └── integration/
│       └── test_api.py
│
├── requirements.txt
├── .env.example
└── docker-compose.yml       # PostgreSQL + Redis
```

---

## ⚙️ Partie 1: Configuration

### 1.1 Variables d'environnement (`.env`)

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/banking

# JWT
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

# Rate Limiting
RATE_LIMIT_PER_MINUTE=60

# API
API_VERSION=v1
DEBUG=True
```

### 1.2 Configuration centralisée (`app/config.py`)

```python
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # Database
    database_url: str
    
    # JWT
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7
    
    # Redis
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0
    
    # Rate Limiting
    rate_limit_per_minute: int = 60
    
    # API
    api_version: str = "v1"
    debug: bool = False
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()
```

### 1.3 Docker Compose (`docker-compose.yml`)

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: banking
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
```

**Lancer les services:**

```bash
docker-compose up -d
```

---

## 🗄️ Partie 2: Couche Repository

### Repository de base (`app/repositories/base_repository.py`)

```python
from typing import Generic, TypeVar, Type, Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import func

ModelType = TypeVar("ModelType")

class BaseRepository(Generic[ModelType]):
    """Repository de base avec opérations CRUD communes"""
    
    def __init__(self, model: Type[ModelType], db: Session):
        self.model = model
        self.db = db
    
    def get_by_id(self, id: int) -> Optional[ModelType]:
        return self.db.query(self.model).filter(self.model.id == id).first()
    
    def get_all(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return self.db.query(self.model).offset(skip).limit(limit).all()
    
    def create(self, obj: ModelType) -> ModelType:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj
    
    def update(self, obj: ModelType) -> ModelType:
        self.db.commit()
        self.db.refresh(obj)
        return obj
    
    def delete(self, obj: ModelType) -> None:
        self.db.delete(obj)
        self.db.commit()
    
    def count(self) -> int:
        return self.db.query(func.count(self.model.id)).scalar()
```

### Account Repository (`app/repositories/account_repository.py`)

```python
from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models.account import Account
from app.repositories.base_repository import BaseRepository

class AccountRepository(BaseRepository[Account]):
    def __init__(self, db: Session):
        super().__init__(Account, db)
    
    def get_by_account_number(self, account_number: str) -> Optional[Account]:
        return self.db.query(Account).filter(
            Account.account_number == account_number
        ).first()
    
    def get_by_owner(
        self, 
        owner_id: int, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Account]:
        return self.db.query(Account).filter(
            Account.owner_id == owner_id
        ).offset(skip).limit(limit).all()
    
    def get_by_owner_and_type(
        self, 
        owner_id: int, 
        account_type: str
    ) -> List[Account]:
        return self.db.query(Account).filter(
            and_(
                Account.owner_id == owner_id,
                Account.account_type == account_type
            )
        ).all()
    
    def count_by_owner(self, owner_id: int) -> int:
        return self.db.query(Account).filter(
            Account.owner_id == owner_id
        ).count()
```

### Transaction Repository (`app/repositories/transaction_repository.py`)

```python
from typing import List, Optional
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, desc
from app.models.transaction import Transaction
from app.repositories.base_repository import BaseRepository

class TransactionRepository(BaseRepository[Transaction]):
    def __init__(self, db: Session):
        super().__init__(Transaction, db)
    
    def get_by_account(
        self,
        account_id: int,
        skip: int = 0,
        limit: int = 100,
        type_filter: Optional[str] = None,
        from_date: Optional[datetime] = None,
        to_date: Optional[datetime] = None
    ) -> List[Transaction]:
        query = self.db.query(Transaction).filter(
            Transaction.account_id == account_id
        )
        
        # Filtres optionnels
        if type_filter:
            query = query.filter(Transaction.type == type_filter)
        
        if from_date:
            query = query.filter(Transaction.created_at >= from_date)
        
        if to_date:
            query = query.filter(Transaction.created_at <= to_date)
        
        return query.order_by(
            desc(Transaction.created_at)
        ).offset(skip).limit(limit).all()
    
    def get_total_by_type(self, account_id: int, type: str) -> float:
        result = self.db.query(
            func.sum(Transaction.amount)
        ).filter(
            and_(
                Transaction.account_id == account_id,
                Transaction.type == type
            )
        ).scalar()
        return result or 0.0
```

---

## 💼 Partie 3: Couche Service

### Account Service (`app/services/account_service.py`)

```python
from typing import List, Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.account import Account
from app.repositories.account_repository import AccountRepository
from app.schemas.account import AccountCreate, AccountUpdate
from app.utils.cache import CacheManager
import random
import string

class AccountService:
    def __init__(self, db: Session, cache: CacheManager):
        self.repository = AccountRepository(db)
        self.cache = cache
        self.db = db
    
    def _generate_account_number(self) -> str:
        """Générer un numéro de compte unique"""
        while True:
            number = "".join(random.choices(string.digits, k=12))
            if not self.repository.get_by_account_number(number):
                return number
    
    def create_account(
        self, 
        account_data: AccountCreate, 
        owner_id: int
    ) -> Account:
        """Créer un nouveau compte"""
        # Vérifier le nombre de comptes de l'utilisateur
        count = self.repository.count_by_owner(owner_id)
        if count >= 5:  # Limite de 5 comptes par utilisateur
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Maximum number of accounts reached (5)"
            )
        
        account = Account(
            account_number=self._generate_account_number(),
            account_type=account_data.account_type,
            currency=account_data.currency,
            owner_id=owner_id
        )
        
        created_account = self.repository.create(account)
        
        # Invalider le cache des comptes de l'utilisateur
        self.cache.delete(f"user_accounts:{owner_id}")
        
        return created_account
    
    def get_account(self, account_id: int, owner_id: int) -> Account:
        """Obtenir un compte par ID"""
        # Tenter de récupérer du cache
        cache_key = f"account:{account_id}"
        cached = self.cache.get(cache_key)
        
        if cached:
            account = Account(**cached)
            if account.owner_id != owner_id:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Account not found"
                )
            return account
        
        # Sinon, récupérer de la DB
        account = self.repository.get_by_id(account_id)
        
        if not account or account.owner_id != owner_id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Account not found"
            )
        
        # Mettre en cache (5 minutes)
        self.cache.set(
            cache_key, 
            account.__dict__, 
            expire=300
        )
        
        return account
    
    def list_accounts(
        self, 
        owner_id: int, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Account]:
        """Lister les comptes d'un utilisateur"""
        cache_key = f"user_accounts:{owner_id}:{skip}:{limit}"
        cached = self.cache.get(cache_key)
        
        if cached:
            return [Account(**acc) for acc in cached]
        
        accounts = self.repository.get_by_owner(owner_id, skip, limit)
        
        # Mettre en cache (2 minutes)
        self.cache.set(
            cache_key,
            [acc.__dict__ for acc in accounts],
            expire=120
        )
        
        return accounts
    
    def freeze_account(self, account_id: int, owner_id: int) -> Account:
        """Geler un compte"""
        account = self.get_account(account_id, owner_id)
        
        if account.status == "FROZEN":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Account is already frozen"
            )
        
        account.status = "FROZEN"
        updated = self.repository.update(account)
        
        # Invalider le cache
        self.cache.delete(f"account:{account_id}")
        self.cache.delete(f"user_accounts:{owner_id}")
        
        return updated
    
    def close_account(self, account_id: int, owner_id: int) -> None:
        """Fermer un compte"""
        account = self.get_account(account_id, owner_id)
        
        if account.balance != 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Cannot close account with non-zero balance: {account.balance}"
            )
        
        self.repository.delete(account)
        
        # Invalider le cache
        self.cache.delete(f"account:{account_id}")
        self.cache.delete(f"user_accounts:{owner_id}")
```

### Transaction Service avec ACID (`app/services/transaction_service.py`)

```python
from typing import List, Optional
from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.transaction import Transaction
from app.repositories.transaction_repository import TransactionRepository
from app.repositories.account_repository import AccountRepository
from app.schemas.transaction import TransactionCreate, TransferCreate
from app.utils.cache import CacheManager

class TransactionService:
    def __init__(self, db: Session, cache: CacheManager):
        self.transaction_repo = TransactionRepository(db)
        self.account_repo = AccountRepository(db)
        self.cache = cache
        self.db = db
    
    def create_transaction(
        self,
        transaction_data: TransactionCreate,
        account_id: int,
        owner_id: int
    ) -> Transaction:
        """Créer une transaction (dépôt ou retrait) avec transaction DB"""
        try:
            # Commencer une transaction DB
            account = self.account_repo.get_by_id(account_id)
            
            if not account or account.owner_id != owner_id:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Account not found"
                )
            
            if account.status == "FROZEN":
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Account is frozen"
                )
            
            # Valider le retrait
            if transaction_data.type == "RETRAIT":
                if account.balance < transaction_data.amount:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Insufficient balance. Available: {account.balance}"
                    )
                account.balance -= transaction_data.amount
            else:  # DEPOT
                account.balance += transaction_data.amount
            
            # Créer la transaction
            transaction = Transaction(
                amount=transaction_data.amount,
                type=transaction_data.type,
                description=transaction_data.description,
                account_id=account_id
            )
            
            self.account_repo.update(account)
            created_transaction = self.transaction_repo.create(transaction)
            
            # Commit automatique via repository
            
            # Invalider le cache
            self.cache.delete(f"account:{account_id}")
            self.cache.delete(f"transactions:{account_id}")
            
            return created_transaction
            
        except IntegrityError as e:
            self.db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Transaction failed due to database error"
            )
    
    def create_transfer(
        self,
        transfer_data: TransferCreate,
        owner_id: int
    ) -> dict:
        """Créer un virement entre deux comptes avec transaction ACID"""
        try:
            # Vérifier le compte source
            from_account = self.account_repo.get_by_id(
                transfer_data.from_account_id
            )
            
            if not from_account or from_account.owner_id != owner_id:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Source account not found"
                )
            
            if from_account.status == "FROZEN":
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Source account is frozen"
                )
            
            # Vérifier le compte destination
            to_account = self.account_repo.get_by_account_number(
                transfer_data.to_account_number
            )
            
            if not to_account:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Destination account not found"
                )
            
            if to_account.status == "FROZEN":
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Destination account is frozen"
                )
            
            # Vérifier que les devises correspondent
            if from_account.currency != to_account.currency:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Currency mismatch between accounts"
                )
            
            # Vérifier le solde
            if from_account.balance < transfer_data.amount:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Insufficient balance. Available: {from_account.balance}"
                )
            
            # Effectuer le virement (transaction atomique)
            from_account.balance -= transfer_data.amount
            to_account.balance += transfer_data.amount
            
            # Créer les transactions
            debit = Transaction(
                amount=transfer_data.amount,
                type="VIREMENT",
                description=f"Transfer to {to_account.account_number}: {transfer_data.description}",
                account_id=from_account.id
            )
            
            credit = Transaction(
                amount=transfer_data.amount,
                type="VIREMENT",
                description=f"Transfer from {from_account.account_number}: {transfer_data.description}",
                account_id=to_account.id
            )
            
            self.account_repo.update(from_account)
            self.account_repo.update(to_account)
            self.transaction_repo.create(debit)
            self.transaction_repo.create(credit)
            
            # Commit automatique
            
            # Invalider le cache
            self.cache.delete(f"account:{from_account.id}")
            self.cache.delete(f"account:{to_account.id}")
            self.cache.delete(f"transactions:{from_account.id}")
            self.cache.delete(f"transactions:{to_account.id}")
            
            return {
                "status": "success",
                "from_account": from_account.account_number,
                "to_account": to_account.account_number,
                "amount": transfer_data.amount,
                "currency": from_account.currency,
                "new_balance": from_account.balance
            }
            
        except IntegrityError:
            self.db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Transfer failed due to database error"
            )
    
    def list_transactions(
        self,
        account_id: int,
        owner_id: int,
        skip: int = 0,
        limit: int = 100,
        type_filter: Optional[str] = None,
        from_date: Optional[datetime] = None,
        to_date: Optional[datetime] = None
    ) -> List[Transaction]:
        """Lister les transactions d'un compte avec filtres"""
        # Vérifier que le compte appartient à l'utilisateur
        account = self.account_repo.get_by_id(account_id)
        if not account or account.owner_id != owner_id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Account not found"
            )
        
        return self.transaction_repo.get_by_account(
            account_id=account_id,
            skip=skip,
            limit=limit,
            type_filter=type_filter,
            from_date=from_date,
            to_date=to_date
        )
```

---

## 🔧 Partie 4: Utilitaires

### Cache Manager avec Redis (`app/utils/cache.py`)

```python
import redis
import json
from typing import Any, Optional
from app.config import settings

class CacheManager:
    def __init__(self):
        self.redis_client = redis.Redis(
            host=settings.redis_host,
            port=settings.redis_port,
            db=settings.redis_db,
            decode_responses=True
        )
    
    def get(self, key: str) -> Optional[Any]:
        """Récupérer une valeur du cache"""
        try:
            value = self.redis_client.get(key)
            return json.loads(value) if value else None
        except Exception as e:
            print(f"Cache get error: {e}")
            return None
    
    def set(self, key: str, value: Any, expire: int = 300) -> bool:
        """Définir une valeur dans le cache avec expiration (secondes)"""
        try:
            return self.redis_client.setex(
                key, 
                expire, 
                json.dumps(value, default=str)
            )
        except Exception as e:
            print(f"Cache set error: {e}")
            return False
    
    def delete(self, key: str) -> bool:
        """Supprimer une clé du cache"""
        try:
            return self.redis_client.delete(key) > 0
        except Exception as e:
            print(f"Cache delete error: {e}")
            return False
    
    def clear_pattern(self, pattern: str) -> int:
        """Supprimer toutes les clés correspondant au pattern"""
        try:
            keys = self.redis_client.keys(pattern)
            if keys:
                return self.redis_client.delete(*keys)
            return 0
        except Exception as e:
            print(f"Cache clear error: {e}")
            return 0

# Instance globale
cache_manager = CacheManager()
```

### Pagination (`app/utils/pagination.py`)

```python
from typing import Generic, TypeVar, List
from pydantic import BaseModel

T = TypeVar('T')

class PaginatedResponse(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    page_size: int
    total_pages: int
    
    class Config:
        from_attributes = True

def paginate(
    items: List[T],
    total: int,
    page: int,
    page_size: int
) -> PaginatedResponse[T]:
    """Créer une réponse paginée"""
    total_pages = (total + page_size - 1) // page_size
    
    return PaginatedResponse(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        total_pages=total_pages
    )
```

---

## 🚦 Partie 5: Rate Limiting

**Middleware de rate limiting (`app/middleware/rate_limiter.py`)**

```python
from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
import time
from app.utils.cache import cache_manager
from app.config import settings

class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Ignorer pour la documentation
        if request.url.path in ["/docs", "/redoc", "/openapi.json"]:
            return await call_next(request)
        
        # Identifier le client (IP)
        client_ip = request.client.host
        key = f"rate_limit:{client_ip}"
        
        # Récupérer le compteur actuel
        current_count = cache_manager.get(key)
        
        if current_count is None:
            # Première requête, initialiser le compteur
            cache_manager.set(key, 1, expire=60)
        elif int(current_count) >= settings.rate_limit_per_minute:
            # Limite atteinte
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Rate limit exceeded. Try again later."
            )
        else:
            # Incrémenter le compteur
            cache_manager.redis_client.incr(key)
        
        response = await call_next(request)
        return response
```

---

## 📊 Partie 6: Tests

### Tests unitaires des services (`tests/unit/test_account_service.py`)

```python
import pytest
from unittest.mock import Mock, MagicMock
from app.services.account_service import AccountService
from app.schemas.account import AccountCreate
from app.models.account import Account

@pytest.fixture
def mock_db():
    return Mock()

@pytest.fixture
def mock_cache():
    cache = Mock()
    cache.get = Mock(return_value=None)
    cache.set = Mock(return_value=True)
    cache.delete = Mock(return_value=True)
    return cache

@pytest.fixture
def account_service(mock_db, mock_cache):
    return AccountService(mock_db, mock_cache)

def test_create_account_success(account_service):
    """Test de création de compte réussie"""
    account_service.repository.count_by_owner = Mock(return_value=2)
    account_service.repository.get_by_account_number = Mock(return_value=None)
    account_service.repository.create = Mock(
        return_value=Account(
            id=1,
            account_number="123456789012",
            account_type="COURANT",
            balance=0.0,
            currency="HTG",
            owner_id=1
        )
    )
    
    account_data = AccountCreate(account_type="COURANT", currency="HTG")
    result = account_service.create_account(account_data, owner_id=1)
    
    assert result.id == 1
    assert result.account_type == "COURANT"
    account_service.repository.create.assert_called_once()

def test_create_account_exceeds_limit(account_service):
    """Test de création de compte au-delà de la limite"""
    account_service.repository.count_by_owner = Mock(return_value=5)
    
    account_data = AccountCreate(account_type="COURANT")
    
    with pytest.raises(HTTPException) as exc_info:
        account_service.create_account(account_data, owner_id=1)
    
    assert exc_info.value.status_code == 400
    assert "Maximum number" in exc_info.value.detail
```

### Tests d'intégration (`tests/integration/test_api.py`)

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_full_flow():
    """Test du flow complet: register -> login -> create account -> transaction"""
    
    # 1. Register
    response = client.post("/api/v1/auth/register", json={
        "email": "test@example.com",
        "password": "password123",
        "full_name": "Test User"
    })
    assert response.status_code == 201
    
    # 2. Login
    response = client.post("/api/v1/auth/login", json={
        "email": "test@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # 3. Create account
    response = client.post(
        "/api/v1/accounts",
        json={"account_type": "COURANT", "currency": "HTG"},
        headers=headers
    )
    assert response.status_code == 201
    account_id = response.json()["id"]
    
    # 4. Make deposit
    response = client.post(
        f"/api/v1/accounts/{account_id}/transactions",
        json={
            "amount": 1000.0,
            "type": "DEPOT",
            "description": "Initial deposit"
        },
        headers=headers
    )
    assert response.status_code == 201
    
    # 5. Check balance
    response = client.get(
        f"/api/v1/accounts/{account_id}/balance",
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()["balance"] == 1000.0
```

**Exécuter les tests:**

```bash
# Tests unitaires
pytest tests/unit/ -v

# Tests d'intégration
pytest tests/integration/ -v

# Tous les tests avec coverage
pytest --cov=app tests/ --cov-report=html
```

---

## 🎯 Checklist de Complétion

- [ ] ✅ Architecture en couches (Controller → Service → Repository)
- [ ] ✅ OAuth2 avec JWT et refresh tokens
- [ ] ✅ Caching Redis pour optimisation
- [ ] ✅ Transactions DB avec ACID
- [ ] ✅ Rate limiting middleware
- [ ] ✅ Pagination et filtrage
- [ ] ✅ Tests unitaires et d'intégration
- [ ] ✅ Documentation Swagger automatique
- [ ] ✅ Configuration centralisée avec .env
- [ ] ✅ Docker Compose pour PostgreSQL + Redis

---

## 🚀 Prochaines Étapes

Passez au **Niveau Senior** pour :
- Architecture hexagonale
- Domain-Driven Design
- Microservices patterns
- Event-driven architecture
- CQRS et Event Sourcing
- Observability complète

---

**Bon développement backend avancé !** 🚀
