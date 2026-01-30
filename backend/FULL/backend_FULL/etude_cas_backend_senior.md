# Étude de Cas Backend — Niveau Senior

## 🎯 Objectif

Concevoir et implémenter un système bancaire avec architecture hexagonale, Domain-Driven Design, microservices, event sourcing, CQRS, monitoring complet et patterns de résilience. Durée: 8-10 heures.

---

## 🏗️ Architecture Hexagonale (Ports & Adapters)

```
┌──────────────────────────────────────────────────────┐
│                   ADAPTERS (Drivers)                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │   REST   │  │  GraphQL │  │   CLI    │          │
│  │  API     │  │   API    │  │          │          │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘          │
└───────┼─────────────┼─────────────┼─────────────────┘
        │             │             │
        ▼             ▼             ▼
┌──────────────────────────────────────────────────────┐
│                    PORTS (Inbound)                   │
│  ┌────────────────────────────────────────────────┐ │
│  │        Application Services / Use Cases        │ │
│  └──────────────────┬─────────────────────────────┘ │
└─────────────────────┼───────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────┐
│                DOMAIN CORE (Business Logic)          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │ Entities │  │  Value   │  │  Domain  │          │
│  │          │  │  Objects │  │  Events  │          │
│  └──────────┘  └──────────┘  └──────────┘          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │ Aggregates│  │ Services │  │  Rules   │          │
│  └──────────┘  └──────────┘  └──────────┘          │
└─────────────────────┬───────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────┐
│                PORTS (Outbound)                      │
│  ┌────────────────────────────────────────────────┐ │
│  │    Repository / Message Bus / External APIs    │ │
│  └──────────────────┬─────────────────────────────┘ │
└─────────────────────┼───────────────────────────────┘
        │             │             │
        ▼             ▼             ▼
┌──────────────────────────────────────────────────────┐
│              ADAPTERS (Driven)                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │ PostgreSQL│  │  Redis   │  │ RabbitMQ │          │
│  │  (Write)  │  │  (Read)  │  │ (Events) │          │
│  └──────────┘  └──────────┘  └──────────┘          │
└──────────────────────────────────────────────────────┘
```

**Principes:**
- Le domaine ne dépend de rien (pas de framework, pas de DB)
- Les adaptateurs dépendent des ports
- Inversion de dépendances (Dependency Inversion Principle)
- Testabilité maximale

---

## 📁 Structure du Projet (Hexagonal + DDD)

```
banking-platform/
├── src/
│   ├── domain/                      # CŒUR (pas de dépendances externes)
│   │   ├── account/
│   │   │   ├── entities/
│   │   │   │   ├── account.py       # Entité Account
│   │   │   │   └── transaction.py
│   │   │   ├── value_objects/
│   │   │   │   ├── account_id.py
│   │   │   │   ├── money.py
│   │   │   │   └── account_number.py
│   │   │   ├── aggregates/
│   │   │   │   └── account_aggregate.py
│   │   │   ├── events/
│   │   │   │   ├── account_created.py
│   │   │   │   ├── money_deposited.py
│   │   │   │   └── money_withdrawn.py
│   │   │   ├── repositories/
│   │   │   │   └── account_repository.py  # Interface (Port)
│   │   │   └── services/
│   │   │       └── account_domain_service.py
│   │   │
│   │   ├── transfer/
│   │   │   ├── entities/
│   │   │   │   └── transfer.py
│   │   │   ├── events/
│   │   │   │   └── transfer_completed.py
│   │   │   └── saga/
│   │   │       └── transfer_saga.py   # Saga pattern
│   │   │
│   │   └── shared/
│   │       ├── base_entity.py
│   │       ├── base_aggregate.py
│   │       ├── domain_event.py
│   │       └── result.py
│   │
│   ├── application/                 # Use Cases / Application Services
│   │   ├── commands/
│   │   │   ├── create_account_command.py
│   │   │   ├── deposit_money_command.py
│   │   │   └── withdraw_money_command.py
│   │   ├── queries/
│   │   │   ├── get_account_balance_query.py
│   │   │   └── list_transactions_query.py
│   │   ├── handlers/
│   │   │   ├── command_handlers.py
│   │   │   └── query_handlers.py
│   │   └── ports/                   # Ports (Interfaces)
│   │       ├── inbound/
│   │       │   ├── account_service_port.py
│   │       │   └── transaction_service_port.py
│   │       └── outbound/
│   │           ├── event_bus_port.py
│   │           └── notification_port.py
│   │
│   ├── infrastructure/              # Adapters (Driven)
│   │   ├── persistence/
│   │   │   ├── postgres/
│   │   │   │   ├── account_postgres_repository.py
│   │   │   │   ├── event_store_postgres.py
│   │   │   │   └── models.py
│   │   │   └── redis/
│   │   │       └── account_redis_read_model.py
│   │   │
│   │   ├── messaging/
│   │   │   ├── rabbitmq_event_bus.py
│   │   │   └── kafka_event_bus.py
│   │   │
│   │   ├── external/
│   │   │   └── notification_service_adapter.py
│   │   │
│   │   └── config/
│   │       ├── database.py
│   │       ├── message_broker.py
│   │       └── settings.py
│   │
│   ├── interfaces/                  # Adapters (Drivers)
│   │   ├── rest/
│   │   │   ├── api/
│   │   │   │   ├── v1/
│   │   │   │   │   ├── account_controller.py
│   │   │   │   │   └── transaction_controller.py
│   │   │   │   └── dependencies.py
│   │   │   ├── middleware/
│   │   │   │   ├── circuit_breaker.py
│   │   │   │   └── resilience.py
│   │   │   └── main.py
│   │   │
│   │   └── graphql/
│   │       └── schema.py
│   │
│   └── shared/                      # Shared kernel
│       ├── monitoring/
│       │   ├── metrics.py
│       │   └── tracing.py
│       └── utils/
│           └── logging.py
│
├── tests/
│   ├── unit/
│   │   ├── domain/
│   │   └── application/
│   ├── integration/
│   └── e2e/
│
├── docker-compose.yml
├── k8s/                             # Kubernetes manifests
└── requirements.txt
```

---

## 🎯 Partie 1: Domain Layer (Core)

### 1.1 Value Objects (`src/domain/account/value_objects/money.py`)

```python
from dataclasses import dataclass
from decimal import Decimal
from typing import Self

@dataclass(frozen=True)
class Money:
    """Value Object représentant une somme d'argent"""
    amount: Decimal
    currency: str
    
    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Amount cannot be negative")
        if not self.currency or len(self.currency) != 3:
            raise ValueError("Currency must be 3-letter code")
    
    def add(self, other: 'Money') -> 'Money':
        """Additionner deux montants"""
        if self.currency != other.currency:
            raise ValueError(f"Cannot add {self.currency} and {other.currency}")
        return Money(self.amount + other.amount, self.currency)
    
    def subtract(self, other: 'Money') -> 'Money':
        """Soustraire deux montants"""
        if self.currency != other.currency:
            raise ValueError(f"Cannot subtract {other.currency} from {self.currency}")
        result = self.amount - other.amount
        if result < 0:
            raise ValueError("Result cannot be negative")
        return Money(result, self.currency)
    
    def is_greater_than(self, other: 'Money') -> bool:
        """Comparer deux montants"""
        if self.currency != other.currency:
            raise ValueError("Cannot compare different currencies")
        return self.amount > other.amount
    
    def __str__(self) -> str:
        return f"{self.amount:.2f} {self.currency}"
```

### 1.2 Domain Events (`src/domain/account/events/account_created.py`)

```python
from datetime import datetime
from dataclasses import dataclass
from src.domain.shared.domain_event import DomainEvent

@dataclass
class AccountCreated(DomainEvent):
    """Event émis lors de la création d'un compte"""
    account_id: str
    owner_id: str
    account_type: str
    currency: str
    timestamp: datetime
    
    def event_name(self) -> str:
        return "account.created"

@dataclass
class MoneyDeposited(DomainEvent):
    """Event émis lors d'un dépôt"""
    account_id: str
    amount: str  # Sérialisé comme string pour éviter les problèmes
    currency: str
    transaction_id: str
    timestamp: datetime
    
    def event_name(self) -> str:
        return "money.deposited"

@dataclass
class MoneyWithdrawn(DomainEvent):
    """Event émis lors d'un retrait"""
    account_id: str
    amount: str
    currency: str
    transaction_id: str
    timestamp: datetime
    
    def event_name(self) -> str:
        return "money.withdrawn"
```

### 1.3 Aggregate (`src/domain/account/aggregates/account_aggregate.py`)

```python
from typing import List, Optional
from datetime import datetime
from src.domain.shared.base_aggregate import BaseAggregate
from src.domain.account.value_objects.money import Money
from src.domain.account.events.account_created import (
    AccountCreated, 
    MoneyDeposited, 
    MoneyWithdrawn
)
from src.domain.shared.result import Result

class AccountAggregate(BaseAggregate):
    """Aggregate Root pour Account"""
    
    def __init__(
        self,
        account_id: str,
        owner_id: str,
        account_type: str,
        balance: Money,
        status: str = "ACTIVE"
    ):
        super().__init__()
        self.account_id = account_id
        self.owner_id = owner_id
        self.account_type = account_type
        self.balance = balance
        self.status = status
        self._version = 0
    
    @classmethod
    def create(
        cls,
        account_id: str,
        owner_id: str,
        account_type: str,
        currency: str
    ) -> Result['AccountAggregate']:
        """Factory method pour créer un nouveau compte"""
        try:
            # Validation
            if account_type not in ["COURANT", "EPARGNE"]:
                return Result.failure("Invalid account type")
            
            # Créer l'aggregate
            balance = Money(Decimal("0"), currency)
            account = cls(account_id, owner_id, account_type, balance)
            
            # Émettre l'event
            event = AccountCreated(
                account_id=account_id,
                owner_id=owner_id,
                account_type=account_type,
                currency=currency,
                timestamp=datetime.utcnow()
            )
            account.add_domain_event(event)
            
            return Result.success(account)
        except Exception as e:
            return Result.failure(str(e))
    
    def deposit(self, amount: Money) -> Result[None]:
        """Déposer de l'argent"""
        # Validation des règles métier
        if self.status != "ACTIVE":
            return Result.failure("Account is not active")
        
        if amount.currency != self.balance.currency:
            return Result.failure("Currency mismatch")
        
        try:
            # Modifier l'état
            self.balance = self.balance.add(amount)
            
            # Émettre l'event
            event = MoneyDeposited(
                account_id=self.account_id,
                amount=str(amount.amount),
                currency=amount.currency,
                transaction_id=self._generate_transaction_id(),
                timestamp=datetime.utcnow()
            )
            self.add_domain_event(event)
            
            return Result.success(None)
        except Exception as e:
            return Result.failure(str(e))
    
    def withdraw(self, amount: Money) -> Result[None]:
        """Retirer de l'argent"""
        # Validation des règles métier
        if self.status != "ACTIVE":
            return Result.failure("Account is not active")
        
        if amount.currency != self.balance.currency:
            return Result.failure("Currency mismatch")
        
        if not self.balance.is_greater_than(amount) and self.balance.amount != amount.amount:
            return Result.failure(f"Insufficient balance. Available: {self.balance}")
        
        try:
            # Modifier l'état
            self.balance = self.balance.subtract(amount)
            
            # Émettre l'event
            event = MoneyWithdrawn(
                account_id=self.account_id,
                amount=str(amount.amount),
                currency=amount.currency,
                transaction_id=self._generate_transaction_id(),
                timestamp=datetime.utcnow()
            )
            self.add_domain_event(event)
            
            return Result.success(None)
        except Exception as e:
            return Result.failure(str(e))
    
    def freeze(self) -> Result[None]:
        """Geler le compte"""
        if self.status == "FROZEN":
            return Result.failure("Account is already frozen")
        
        self.status = "FROZEN"
        return Result.success(None)
    
    def _generate_transaction_id(self) -> str:
        """Générer un ID de transaction unique"""
        import uuid
        return str(uuid.uuid4())
```

### 1.4 Repository Interface (Port) (`src/domain/account/repositories/account_repository.py`)

```python
from abc import ABC, abstractmethod
from typing import Optional
from src.domain.account.aggregates.account_aggregate import AccountAggregate

class IAccountRepository(ABC):
    """Port (interface) pour le repository de comptes"""
    
    @abstractmethod
    async def save(self, account: AccountAggregate) -> None:
        """Sauvegarder un compte"""
        pass
    
    @abstractmethod
    async def get_by_id(self, account_id: str) -> Optional[AccountAggregate]:
        """Récupérer un compte par ID"""
        pass
    
    @abstractmethod
    async def get_by_owner(self, owner_id: str) -> list[AccountAggregate]:
        """Récupérer tous les comptes d'un propriétaire"""
        pass
    
    @abstractmethod
    async def exists(self, account_id: str) -> bool:
        """Vérifier si un compte existe"""
        pass
```

---

## 📦 Partie 2: Application Layer (CQRS)

### 2.1 Commands (`src/application/commands/create_account_command.py`)

```python
from dataclasses import dataclass

@dataclass
class CreateAccountCommand:
    """Command pour créer un compte"""
    owner_id: str
    account_type: str
    currency: str

@dataclass
class DepositMoneyCommand:
    """Command pour déposer de l'argent"""
    account_id: str
    amount: str
    currency: str

@dataclass
class WithdrawMoneyCommand:
    """Command pour retirer de l'argent"""
    account_id: str
    amount: str
    currency: str
```

### 2.2 Queries (`src/application/queries/get_account_balance_query.py`)

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class GetAccountBalanceQuery:
    """Query pour obtenir le solde d'un compte"""
    account_id: str

@dataclass
class ListTransactionsQuery:
    """Query pour lister les transactions"""
    account_id: str
    from_date: Optional[str] = None
    to_date: Optional[str] = None
    page: int = 1
    page_size: int = 20
```

### 2.3 Command Handlers (`src/application/handlers/command_handlers.py`)

```python
from decimal import Decimal
from src.application.commands.create_account_command import (
    CreateAccountCommand,
    DepositMoneyCommand,
    WithdrawMoneyCommand
)
from src.domain.account.aggregates.account_aggregate import AccountAggregate
from src.domain.account.repositories.account_repository import IAccountRepository
from src.domain.account.value_objects.money import Money
from src.application.ports.outbound.event_bus_port import IEventBus
from src.domain.shared.result import Result
import uuid

class CreateAccountCommandHandler:
    """Handler pour CreateAccountCommand"""
    
    def __init__(self, repository: IAccountRepository, event_bus: IEventBus):
        self.repository = repository
        self.event_bus = event_bus
    
    async def handle(self, command: CreateAccountCommand) -> Result[str]:
        """Gérer la création d'un compte"""
        # Générer un ID unique
        account_id = str(uuid.uuid4())
        
        # Créer l'aggregate
        result = AccountAggregate.create(
            account_id=account_id,
            owner_id=command.owner_id,
            account_type=command.account_type,
            currency=command.currency
        )
        
        if result.is_failure:
            return Result.failure(result.error)
        
        account = result.value
        
        # Sauvegarder
        await self.repository.save(account)
        
        # Publier les events
        for event in account.domain_events:
            await self.event_bus.publish(event)
        
        account.clear_domain_events()
        
        return Result.success(account_id)

class DepositMoneyCommandHandler:
    """Handler pour DepositMoneyCommand"""
    
    def __init__(self, repository: IAccountRepository, event_bus: IEventBus):
        self.repository = repository
        self.event_bus = event_bus
    
    async def handle(self, command: DepositMoneyCommand) -> Result[None]:
        """Gérer un dépôt"""
        # Récupérer l'aggregate
        account = await self.repository.get_by_id(command.account_id)
        
        if not account:
            return Result.failure("Account not found")
        
        # Exécuter la logique métier
        amount = Money(Decimal(command.amount), command.currency)
        result = account.deposit(amount)
        
        if result.is_failure:
            return result
        
        # Sauvegarder
        await self.repository.save(account)
        
        # Publier les events
        for event in account.domain_events:
            await self.event_bus.publish(event)
        
        account.clear_domain_events()
        
        return Result.success(None)
```

---

## 🔌 Partie 3: Infrastructure Layer (Adapters)

### 3.1 Event Sourcing (`src/infrastructure/persistence/postgres/event_store_postgres.py`)

```python
from typing import List
from sqlalchemy import Column, String, Text, DateTime, Integer
from sqlalchemy.orm import Session
from datetime import datetime
import json
from src.domain.shared.domain_event import DomainEvent

class EventStoreModel:
    """Modèle pour stocker les events"""
    __tablename__ = "event_store"
    
    id = Column(Integer, primary_key=True)
    aggregate_id = Column(String, index=True, nullable=False)
    event_type = Column(String, nullable=False)
    event_data = Column(Text, nullable=False)
    version = Column(Integer, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class EventStorePostgres:
    """Event Store avec PostgreSQL"""
    
    def __init__(self, db: Session):
        self.db = db
    
    async def append(
        self, 
        aggregate_id: str, 
        events: List[DomainEvent], 
        expected_version: int
    ) -> None:
        """Ajouter des events à l'event store"""
        # Vérifier la version (optimistic concurrency)
        current_version = self.db.query(EventStoreModel).filter(
            EventStoreModel.aggregate_id == aggregate_id
        ).count()
        
        if current_version != expected_version:
            raise Exception("Concurrency conflict")
        
        # Ajouter les events
        for i, event in enumerate(events):
            event_model = EventStoreModel(
                aggregate_id=aggregate_id,
                event_type=event.event_name(),
                event_data=json.dumps(event.__dict__, default=str),
                version=expected_version + i + 1,
                timestamp=event.timestamp
            )
            self.db.add(event_model)
        
        self.db.commit()
    
    async def get_events(self, aggregate_id: str) -> List[dict]:
        """Récupérer tous les events d'un aggregate"""
        events = self.db.query(EventStoreModel).filter(
            EventStoreModel.aggregate_id == aggregate_id
        ).order_by(EventStoreModel.version).all()
        
        return [
            {
                "event_type": e.event_type,
                "event_data": json.loads(e.event_data),
                "version": e.version,
                "timestamp": e.timestamp
            }
            for e in events
        ]
```

### 3.2 RabbitMQ Event Bus (`src/infrastructure/messaging/rabbitmq_event_bus.py`)

```python
import pika
import json
from src.application.ports.outbound.event_bus_port import IEventBus
from src.domain.shared.domain_event import DomainEvent

class RabbitMQEventBus(IEventBus):
    """Adapter pour RabbitMQ"""
    
    def __init__(self, host: str, port: int):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host, port=port)
        )
        self.channel = self.connection.channel()
        
        # Déclarer l'exchange
        self.channel.exchange_declare(
            exchange='banking.events',
            exchange_type='topic',
            durable=True
        )
    
    async def publish(self, event: DomainEvent) -> None:
        """Publier un event"""
        message = json.dumps(event.__dict__, default=str)
        
        self.channel.basic_publish(
            exchange='banking.events',
            routing_key=event.event_name(),
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2,  # Persistent
                content_type='application/json'
            )
        )
    
    async def subscribe(self, event_type: str, handler):
        """S'abonner à un type d'event"""
        # Créer une queue pour ce handler
        queue_name = f"queue.{event_type}.{handler.__name__}"
        
        self.channel.queue_declare(queue=queue_name, durable=True)
        self.channel.queue_bind(
            exchange='banking.events',
            queue=queue_name,
            routing_key=event_type
        )
        
        def callback(ch, method, properties, body):
            event_data = json.loads(body)
            handler(event_data)
            ch.basic_ack(delivery_tag=method.delivery_tag)
        
        self.channel.basic_consume(
            queue=queue_name,
            on_message_callback=callback
        )
        
        self.channel.start_consuming()
```

### 3.3 Circuit Breaker Pattern (`src/interfaces/rest/middleware/circuit_breaker.py`)

```python
from enum import Enum
from datetime import datetime, timedelta
from typing import Callable, Any
import asyncio

class CircuitState(Enum):
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Failing, reject requests
    HALF_OPEN = "half_open"  # Testing if service recovered

class CircuitBreaker:
    """Pattern Circuit Breaker pour résilience"""
    
    def __init__(
        self,
        failure_threshold: int = 5,
        timeout: int = 60,
        expected_exception: Exception = Exception
    ):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.expected_exception = expected_exception
        
        self.failure_count = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED
    
    async def call(self, func: Callable, *args, **kwargs) -> Any:
        """Exécuter une fonction protégée par le circuit breaker"""
        if self.state == CircuitState.OPEN:
            if self._should_attempt_reset():
                self.state = CircuitState.HALF_OPEN
            else:
                raise Exception("Circuit breaker is OPEN")
        
        try:
            result = await func(*args, **kwargs)
            self._on_success()
            return result
        except self.expected_exception as e:
            self._on_failure()
            raise e
    
    def _on_success(self):
        """Appelé lors d'un succès"""
        self.failure_count = 0
        self.state = CircuitState.CLOSED
    
    def _on_failure(self):
        """Appelé lors d'un échec"""
        self.failure_count += 1
        self.last_failure_time = datetime.now()
        
        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN
    
    def _should_attempt_reset(self) -> bool:
        """Vérifier si on doit tenter de réinitialiser"""
        return (
            self.last_failure_time is not None and
            datetime.now() - self.last_failure_time >= timedelta(seconds=self.timeout)
        )

# Usage
external_api_circuit_breaker = CircuitBreaker(
    failure_threshold=5,
    timeout=60
)

async def call_external_api():
    return await external_api_circuit_breaker.call(some_external_service.call)
```

---

## 📊 Partie 4: Monitoring & Observability

### 4.1 Prometheus Metrics (`src/shared/monitoring/metrics.py`)

```python
from prometheus_client import Counter, Histogram, Gauge
import time

# Compteurs
http_requests_total = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

transactions_total = Counter(
    'transactions_total',
    'Total transactions',
    ['type', 'status']
)

# Histogrammes (pour latence)
http_request_duration = Histogram(
    'http_request_duration_seconds',
    'HTTP request duration',
    ['method', 'endpoint']
)

transaction_duration = Histogram(
    'transaction_duration_seconds',
    'Transaction processing duration',
    ['type']
)

# Gauges (valeurs instantanées)
active_accounts = Gauge(
    'active_accounts_total',
    'Number of active accounts'
)

total_balance = Gauge(
    'total_balance_amount',
    'Total balance across all accounts',
    ['currency']
)

# Décorateur pour mesurer la latence
def measure_latency(metric: Histogram):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = await func(*args, **kwargs)
                return result
            finally:
                duration = time.time() - start_time
                metric.observe(duration)
        return wrapper
    return decorator

# Usage
@measure_latency(transaction_duration.labels(type='deposit'))
async def process_deposit(account_id: str, amount: float):
    # Processing logic
    pass
```

### 4.2 Distributed Tracing avec OpenTelemetry

```python
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Configuration
trace.set_tracer_provider(TracerProvider())
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(jaeger_exporter)
)

tracer = trace.get_tracer(__name__)

# Usage dans les services
class AccountService:
    async def create_account(self, command):
        with tracer.start_as_current_span("create_account") as span:
            span.set_attribute("owner_id", command.owner_id)
            span.set_attribute("account_type", command.account_type)
            
            # Business logic
            result = await self._process_creation(command)
            
            span.set_attribute("account_id", result.account_id)
            return result
```

### 4.3 Structured Logging

```python
import structlog
from datetime import datetime

# Configuration
structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.stdlib.BoundLogger,
    logger_factory=structlog.stdlib.LoggerFactory(),
)

logger = structlog.get_logger()

# Usage
logger.info(
    "account_created",
    account_id="123e4567-e89b-12d3-a456-426614174000",
    owner_id="user-456",
    account_type="COURANT",
    currency="HTG"
)

logger.error(
    "transaction_failed",
    account_id="123",
    amount=1000.0,
    reason="insufficient_balance",
    available_balance=500.0
)
```

---

## 🧪 Partie 5: Tests

### 5.1 Tests Unitaires du Domain

```python
import pytest
from decimal import Decimal
from src.domain.account.aggregates.account_aggregate import AccountAggregate
from src.domain.account.value_objects.money import Money

def test_create_account():
    """Test de création d'un compte"""
    result = AccountAggregate.create(
        account_id="acc-123",
        owner_id="user-456",
        account_type="COURANT",
        currency="HTG"
    )
    
    assert result.is_success
    account = result.value
    assert account.account_id == "acc-123"
    assert account.balance.amount == Decimal("0")
    assert len(account.domain_events) == 1
    assert account.domain_events[0].event_name() == "account.created"

def test_deposit_money():
    """Test de dépôt d'argent"""
    result = AccountAggregate.create("acc-1", "user-1", "COURANT", "HTG")
    account = result.value
    
    money = Money(Decimal("1000"), "HTG")
    deposit_result = account.deposit(money)
    
    assert deposit_result.is_success
    assert account.balance.amount == Decimal("1000")
    assert len(account.domain_events) == 2  # Created + Deposited

def test_withdraw_insufficient_balance():
    """Test de retrait avec solde insuffisant"""
    result = AccountAggregate.create("acc-1", "user-1", "COURANT", "HTG")
    account = result.value
    
    money = Money(Decimal("1000"), "HTG")
    withdraw_result = account.withdraw(money)
    
    assert withdraw_result.is_failure
    assert "Insufficient balance" in withdraw_result.error
```

### 5.2 Tests d'Intégration

```python
import pytest
from httpx import AsyncClient
from src.interfaces.rest.main import app

@pytest.mark.asyncio
async def test_create_account_e2e():
    """Test end-to-end de création de compte"""
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Login
        login_response = await client.post("/api/v1/auth/login", json={
            "email": "test@example.com",
            "password": "password123"
        })
        token = login_response.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}
        
        # Create account
        response = await client.post(
            "/api/v1/accounts",
            json={"account_type": "COURANT", "currency": "HTG"},
            headers=headers
        )
        
        assert response.status_code == 201
        data = response.json()
        assert "account_id" in data
        assert data["balance"] == "0.00"
```

---

## 🎯 Checklist de Complétion

- [ ] ✅ Architecture hexagonale implémentée
- [ ] ✅ Domain-Driven Design avec aggregates
- [ ] ✅ Event Sourcing avec event store
- [ ] ✅ CQRS (Command/Query separation)
- [ ] ✅ Message bus (RabbitMQ/Kafka)
- [ ] ✅ Saga pattern pour transactions distribuées
- [ ] ✅ Circuit breaker pour résilience
- [ ] ✅ Monitoring (Prometheus + Grafana)
- [ ] ✅ Distributed tracing (Jaeger)
- [ ] ✅ Structured logging
- [ ] ✅ Tests unitaires du domain
- [ ] ✅ Tests d'intégration
- [ ] ✅ Tests E2E

---

## 📚 Ressources Complémentaires

- **Architecture:** "Clean Architecture" - Robert C. Martin
- **DDD:** "Domain-Driven Design" - Eric Evans
- **Microservices:** "Building Microservices" - Sam Newman
- **Patterns:** "Enterprise Integration Patterns" - Gregor Hohpe
- **Event Sourcing:** [Greg Young's Blog](https://cqrs.wordpress.com/)

---

**Félicitations ! Vous maîtrisez maintenant l'architecture backend de niveau senior !** 🚀
