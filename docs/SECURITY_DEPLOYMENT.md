# Sikkerhet og Deployment Guide for PAD Framework

Dette dokumentet dekker viktige sikkerhetsaspekter og deployment-strategier for PAD Framework i produksjonsmiljøer.

## 📋 Innholdsfortegnelse

- [Sikkerhetsoversikt](#sikkerhetsoversikt)
- [Autentisering og autorisasjon](#autentisering-og-autorisasjon)
- [Data sikkerhet](#data-sikkerhet)
- [Nettverkssikkerhet](#nettverkssikkerhet)
- [Deployment strategier](#deployment-strategier)
- [Overvåking og logging](#overvåking-og-logging)
- [Backup og gjenoppretting](#backup-og-gjenoppretting)
- [Compliance og regulering](#compliance-og-regulering)

## Sikkerhetsoversikt

### 🛡️ Sikkerhetsprinsipper

PAD Framework følger industry-standard sikkerhetsprinsipper:

- **Defense in Depth**: Flere lag av sikkerhet
- **Principle of Least Privilege**: Minimal nødvendig tilgang
- **Zero Trust**: Aldri stol, alltid verifiser
- **Security by Design**: Sikkerhet bygget inn fra starten
- **Continuous Monitoring**: Kontinuerlig overvåking og respons

### Trusselmodell

#### Potensielle trusler
1. **Kode-injeksjon**: Ondsinnet kode via brukerinput
2. **Data lekkasje**: Eksponering av sensitiv kode eller data
3. **Privilege escalation**: Uautorisert tilgangsøkning
4. **Denial of Service**: Overbelastningsangrep
5. **Man-in-the-middle**: Avlytting av kommunikasjon

#### Risikovurdering
| Trussel | Sannsynlighet | Påvirkning | Risiko | Tiltak |
|---------|---------------|------------|--------|---------|
| Kode-injeksjon | Høy | Kritisk | **Kritisk** | Input validering, sandboxing |
| Data lekkasje | Middels | Høy | **Høy** | Kryptering, tilgangskontroll |
| Privilege escalation | Lav | Høy | **Middels** | RBAC, audit logging |
| DoS | Middels | Middels | **Middels** | Rate limiting, load balancing |
| MITM | Lav | Høy | **Middels** | TLS/SSL, certificate pinning |

## Autentisering og autorisasjon

### Autentiseringsmetoder

#### 1. API Key Authentication (Grunnleggende)
```python
# Miljøvariabler for API-nøkler
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=ant-...

# Sikker lagring
import os
from cryptography.fernet import Fernet

def encrypt_api_key(key: str) -> str:
    """Krypterer API-nøkkel for sikker lagring."""
    f = Fernet(os.environ.get('ENCRYPTION_KEY'))
    return f.encrypt(key.encode()).decode()

def decrypt_api_key(encrypted_key: str) -> str:
    """Dekrypterer API-nøkkel for bruk."""
    f = Fernet(os.environ.get('ENCRYPTION_KEY'))
    return f.decrypt(encrypted_key.encode()).decode()
```

#### 2. OAuth 2.0 / OpenID Connect (Anbefalt for produksjon)
```python
from authlib.integrations.flask_client import OAuth

oauth = OAuth(app)
oauth.register(
    name='github',
    client_id=os.environ.get('GITHUB_CLIENT_ID'),
    client_secret=os.environ.get('GITHUB_CLIENT_SECRET'),
    server_metadata_url='https://github.com/.well-known/openid_configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)
```

#### 3. JWT Tokens for API-tilgang
```python
import jwt
from datetime import datetime, timedelta

def generate_jwt_token(user_id: str, permissions: list) -> str:
    """Genererer JWT token med brukerrettigheter."""
    payload = {
        'user_id': user_id,
        'permissions': permissions,
        'exp': datetime.utcnow() + timedelta(hours=24),
        'iat': datetime.utcnow(),
        'iss': 'pad-framework'
    }
    return jwt.encode(payload, os.environ.get('JWT_SECRET'), algorithm='HS256')

def verify_jwt_token(token: str) -> dict:
    """Verifiserer og dekoder JWT token."""
    try:
        payload = jwt.decode(
            token, 
            os.environ.get('JWT_SECRET'), 
            algorithms=['HS256']
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise AuthenticationError("Token utløpt")
    except jwt.InvalidTokenError:
        raise AuthenticationError("Ugyldig token")
```

### Autorisasjon (RBAC)

#### Rollebasert tilgangskontroll
```python
from enum import Enum
from dataclasses import dataclass
from typing import List, Set

class Permission(Enum):
    CODE_GENERATE = "code:generate"
    CODE_ANALYZE = "code:analyze"
    PROJECT_READ = "project:read"
    PROJECT_WRITE = "project:write"
    ADMIN_ACCESS = "admin:access"

@dataclass
class Role:
    name: str
    permissions: Set[Permission]

# Predefinerte roller
ROLES = {
    'developer': Role('developer', {
        Permission.CODE_GENERATE,
        Permission.CODE_ANALYZE,
        Permission.PROJECT_READ
    }),
    'lead': Role('lead', {
        Permission.CODE_GENERATE,
        Permission.CODE_ANALYZE,
        Permission.PROJECT_READ,
        Permission.PROJECT_WRITE
    }),
    'admin': Role('admin', {
        Permission.CODE_GENERATE,
        Permission.CODE_ANALYZE,
        Permission.PROJECT_READ,
        Permission.PROJECT_WRITE,
        Permission.ADMIN_ACCESS
    })
}

def check_permission(user_role: str, required_permission: Permission) -> bool:
    """Sjekker om bruker har nødvendig tillatelse."""
    role = ROLES.get(user_role)
    return role and required_permission in role.permissions
```

## Data sikkerhet

### Datakryptering

#### 1. Data at Rest
```python
from cryptography.fernet import Fernet
import sqlite3
import json

class EncryptedStorage:
    """Kryptert datalager for sensitiv informasjon."""
    
    def __init__(self, encryption_key: bytes):
        self.cipher = Fernet(encryption_key)
    
    def store_context(self, project_id: str, context_data: dict) -> None:
        """Lagrer prosjektkontext kryptert."""
        encrypted_data = self.cipher.encrypt(
            json.dumps(context_data).encode()
        )
        
        with sqlite3.connect('pad_secure.db') as conn:
            conn.execute(
                "INSERT OR REPLACE INTO project_contexts (id, data) VALUES (?, ?)",
                (project_id, encrypted_data)
            )
    
    def retrieve_context(self, project_id: str) -> dict:
        """Henter og dekrypterer prosjektkontext."""
        with sqlite3.connect('pad_secure.db') as conn:
            result = conn.execute(
                "SELECT data FROM project_contexts WHERE id = ?",
                (project_id,)
            ).fetchone()
            
        if result:
            decrypted_data = self.cipher.decrypt(result[0])
            return json.loads(decrypted_data.decode())
        return {}
```

#### 2. Data in Transit
```python
import ssl
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.ssl_ import create_urllib3_context

class SecureHTTPAdapter(HTTPAdapter):
    """HTTP adapter med forbedret TLS-sikkerhet."""
    
    def init_poolmanager(self, *args, **kwargs):
        context = create_urllib3_context()
        context.set_ciphers('ECDHE+AESGCM:ECDHE+CHACHA20:DHE+AESGCM:DHE+CHACHA20:!aNULL:!MD5:!DSS')
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        kwargs['ssl_context'] = context
        return super().init_poolmanager(*args, **kwargs)

# Bruk i API-kall
session = requests.Session()
session.mount('https://', SecureHTTPAdapter())
```

### Input-validering og sanitisering

```python
import re
from typing import Any
from pydantic import BaseModel, validator
import bleach

class CodeGenerationRequest(BaseModel):
    """Validert forespørsel for kodegenerering."""
    description: str
    language: str
    framework: str = None
    
    @validator('description')
    def validate_description(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError('Beskrivelse kan ikke være tom')
        if len(v) > 10000:
            raise ValueError('Beskrivelse for lang (maks 10000 tegn)')
        
        # Fjern potensielt farlige tegn
        cleaned = bleach.clean(v, tags=[], strip=True)
        return cleaned
    
    @validator('language')
    def validate_language(cls, v):
        allowed_languages = {'python', 'javascript', 'typescript', 'java', 'go', 'rust'}
        if v.lower() not in allowed_languages:
            raise ValueError(f'Språk må være ett av: {allowed_languages}')
        return v.lower()

def sanitize_code_input(code: str) -> str:
    """Sanitiserer kodeinput for sikker prosessering."""
    # Fjern farlige mønstre
    dangerous_patterns = [
        r'exec\s*\(',
        r'eval\s*\(',
        r'__import__\s*\(',
        r'open\s*\(',
        r'subprocess\.',
        r'os\.system'
    ]
    
    for pattern in dangerous_patterns:
        if re.search(pattern, code, re.IGNORECASE):
            raise SecurityError(f"Farlig mønster oppdaget: {pattern}")
    
    return code
```

## Nettverkssikkerhet

### Rate Limiting

```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import redis

# Redis for distributed rate limiting
redis_client = redis.Redis(host='localhost', port=6379, db=0)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    storage_uri="redis://localhost:6379",
    default_limits=["1000 per hour", "100 per minute"]
)

@app.route("/api/generate")
@limiter.limit("10 per minute")
def generate_code():
    """Kodegenerering med rate limiting."""
    pass

@app.route("/api/analyze")
@limiter.limit("50 per minute")
def analyze_code():
    """Kodeanalyse med rate limiting."""
    pass
```

### Firewall og nettverkssegmentering

```yaml
# Docker network configuration
version: '3.8'
services:
  pad-api:
    build: .
    networks:
      - frontend
      - backend
    ports:
      - "8080:8080"
    
  pad-db:
    image: postgres:13
    networks:
      - backend
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets:
      - db_password
    
  pad-redis:
    image: redis:6
    networks:
      - backend
    command: redis-server --requirepass ${REDIS_PASSWORD}

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true

secrets:
  db_password:
    external: true
```

## Deployment strategier

### Docker Deployment

#### 1. Multi-stage Docker build
```dockerfile
# Multi-stage build for security
FROM python:3.9-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.9-slim

# Opprett non-root bruker
RUN groupadd -r paduser && useradd -r -g paduser paduser

# Kopier kun nødvendige filer
COPY --from=builder /root/.local /home/paduser/.local
COPY pad/ /app/pad/
COPY main.py /app/

# Sett riktige tillatelser
RUN chown -R paduser:paduser /app
USER paduser

WORKDIR /app
ENV PATH=/home/paduser/.local/bin:$PATH

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8080/health')"

EXPOSE 8080
CMD ["python", "main.py"]
```

#### 2. Docker Compose for produksjon
```yaml
version: '3.8'

services:
  pad-app:
    build: .
    restart: unless-stopped
    environment:
      - DATABASE_URL=postgresql://paduser:${DB_PASSWORD}@pad-db:5432/paddb
      - REDIS_URL=redis://pad-redis:6379
      - JWT_SECRET=${JWT_SECRET}
      - ENCRYPTION_KEY=${ENCRYPTION_KEY}
    depends_on:
      - pad-db
      - pad-redis
    networks:
      - pad-network
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.pad.rule=Host(`pad.example.com`)"
      - "traefik.http.routers.pad.tls=true"
      - "traefik.http.routers.pad.tls.certresolver=letsencrypt"

  pad-db:
    image: postgres:13
    restart: unless-stopped
    environment:
      POSTGRES_DB: paddb
      POSTGRES_USER: paduser
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - pad-db-data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    networks:
      - pad-network

  pad-redis:
    image: redis:6
    restart: unless-stopped
    command: redis-server --requirepass ${REDIS_PASSWORD}
    volumes:
      - pad-redis-data:/data
    networks:
      - pad-network

  traefik:
    image: traefik:v2.5
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - traefik-certs:/certificates
    command:
      - --providers.docker=true
      - --entrypoints.web.address=:80
      - --entrypoints.websecure.address=:443
      - --certificatesresolvers.letsencrypt.acme.email=admin@example.com
      - --certificatesresolvers.letsencrypt.acme.storage=/certificates/acme.json
      - --certificatesresolvers.letsencrypt.acme.httpchallenge.entrypoint=web
    networks:
      - pad-network

volumes:
  pad-db-data:
  pad-redis-data:
  traefik-certs:

networks:
  pad-network:
    driver: bridge
```

### Kubernetes Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: pad-framework
  namespace: pad-production
spec:
  replicas: 3
  selector:
    matchLabels:
      app: pad-framework
  template:
    metadata:
      labels:
        app: pad-framework
    spec:
      serviceAccountName: pad-service-account
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        runAsGroup: 1000
        fsGroup: 1000
      containers:
      - name: pad-app
        image: pad-framework:latest
        securityContext:
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: true
          capabilities:
            drop:
            - ALL
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: pad-secrets
              key: database-url
        - name: JWT_SECRET
          valueFrom:
            secretKeyRef:
              name: pad-secrets
              key: jwt-secret
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
```

## Overvåking og logging

### Structured Logging

```python
import structlog
import logging
from pythonjsonlogger import jsonlogger

# Konfigurer structured logging
logging.basicConfig(
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    level=logging.INFO
)

structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer()
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()

# Sikkerhet-spesifikk logging
def log_security_event(event_type: str, user_id: str, details: dict):
    """Logger sikkerhetshendelser for analyse."""
    logger.warning(
        "security_event",
        event_type=event_type,
        user_id=user_id,
        details=details,
        severity="high"
    )

# Eksempel
log_security_event(
    "failed_authentication",
    "unknown",
    {"ip": "192.168.1.100", "attempts": 5}
)
```

### Metrics og alerting

```python
from prometheus_client import Counter, Histogram, generate_latest
import time

# Prometheus metrics
REQUEST_COUNT = Counter('pad_requests_total', 'Total requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('pad_request_duration_seconds', 'Request latency')
SECURITY_EVENTS = Counter('pad_security_events_total', 'Security events', ['type'])

def monitor_endpoint(func):
    """Decorator for endpoint monitoring."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            REQUEST_COUNT.labels(method='POST', endpoint=func.__name__).inc()
            return result
        except Exception as e:
            SECURITY_EVENTS.labels(type='error').inc()
            raise
        finally:
            REQUEST_LATENCY.observe(time.time() - start_time)
    return wrapper

@app.route('/metrics')
def metrics():
    """Prometheus metrics endpoint."""
    return generate_latest()
```

## Backup og gjenoppretting

### Automated Backup Strategy

```bash
#!/bin/bash
# backup.sh - Automatisert backup av PAD Framework data

set -euo pipefail

BACKUP_DIR="/backups/pad-framework"
DATE=$(date +%Y%m%d_%H%M%S)
RETENTION_DAYS=30

# Database backup
pg_dump $DATABASE_URL > "$BACKUP_DIR/db_$DATE.sql"

# Redis backup
redis-cli --rdb "$BACKUP_DIR/redis_$DATE.rdb"

# Configuration backup
tar -czf "$BACKUP_DIR/config_$DATE.tar.gz" /app/config/

# Encrypt backups
gpg --cipher-algo AES256 --compress-algo 2 --symmetric \
    --output "$BACKUP_DIR/backup_$DATE.gpg" \
    "$BACKUP_DIR/db_$DATE.sql"

# Cleanup old backups
find $BACKUP_DIR -name "*.sql" -mtime +$RETENTION_DAYS -delete
find $BACKUP_DIR -name "*.rdb" -mtime +$RETENTION_DAYS -delete
find $BACKUP_DIR -name "*.tar.gz" -mtime +$RETENTION_DAYS -delete

# Upload to cloud storage (eksempel med AWS S3)
aws s3 cp "$BACKUP_DIR/backup_$DATE.gpg" s3://pad-backups/
```

### Disaster Recovery Plan

```yaml
# disaster-recovery.yml
apiVersion: v1
kind: ConfigMap
metadata:
  name: disaster-recovery-plan
data:
  recovery_steps: |
    1. Assess damage scope
    2. Activate backup infrastructure
    3. Restore database from latest backup
    4. Restore application configuration
    5. Validate data integrity
    6. Resume operations
    7. Perform post-incident review
  
  rto: "4 hours"  # Recovery Time Objective
  rpo: "1 hour"   # Recovery Point Objective
```

## Compliance og regulering

### GDPR Compliance

```python
from datetime import datetime, timedelta
from typing import Optional

class GDPRCompliance:
    """GDPR compliance utilities."""
    
    def anonymize_user_data(self, user_id: str) -> None:
        """Anonymiserer brukerdata i henhold til GDPR."""
        with database.transaction():
            # Anonymiser personlige data
            database.execute(
                "UPDATE users SET name = 'ANONYMIZED', email = 'ANONYMIZED' WHERE id = ?",
                (user_id,)
            )
            
            # Behold anonymiserte metadata for analyse
            database.execute(
                "UPDATE user_sessions SET user_id = 'ANONYMIZED' WHERE user_id = ?",
                (user_id,)
            )
    
    def export_user_data(self, user_id: str) -> dict:
        """Eksporterer all brukerdata for GDPR compliance."""
        user_data = {}
        
        # Hent brukerinfo
        user_data['profile'] = database.fetch_one(
            "SELECT * FROM users WHERE id = ?", (user_id,)
        )
        
        # Hent prosjektdata
        user_data['projects'] = database.fetch_all(
            "SELECT * FROM projects WHERE owner_id = ?", (user_id,)
        )
        
        # Hent generert kode (anonymisert)
        user_data['generated_code'] = database.fetch_all(
            "SELECT created_at, language, anonymized_content FROM code_generation WHERE user_id = ?",
            (user_id,)
        )
        
        return user_data
    
    def schedule_data_deletion(self, user_id: str, deletion_date: datetime) -> None:
        """Planlegger automatisk sletting av data."""
        database.execute(
            "INSERT INTO scheduled_deletions (user_id, deletion_date) VALUES (?, ?)",
            (user_id, deletion_date)
        )
```

### Audit Logging

```python
from dataclasses import dataclass
from enum import Enum
import json

class AuditEventType(Enum):
    USER_LOGIN = "user_login"
    CODE_GENERATION = "code_generation"
    DATA_ACCESS = "data_access"
    CONFIGURATION_CHANGE = "config_change"
    SECURITY_EVENT = "security_event"

@dataclass
class AuditEvent:
    event_type: AuditEventType
    user_id: str
    timestamp: datetime
    resource: str
    action: str
    details: dict
    ip_address: str
    user_agent: str

class AuditLogger:
    """Audit logging for compliance."""
    
    def log_event(self, event: AuditEvent) -> None:
        """Logger audit event til database og fil."""
        
        # Database logging
        database.execute(
            """INSERT INTO audit_log 
               (event_type, user_id, timestamp, resource, action, details, ip_address, user_agent)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                event.event_type.value,
                event.user_id,
                event.timestamp,
                event.resource,
                event.action,
                json.dumps(event.details),
                event.ip_address,
                event.user_agent
            )
        )
        
        # Structured file logging
        audit_logger.info(
            "audit_event",
            **event.__dict__
        )

# Brukseksempel
def generate_code_with_audit(user_id: str, request_data: dict, ip: str, user_agent: str):
    """Kodegenerering med audit logging."""
    audit = AuditLogger()
    
    audit.log_event(AuditEvent(
        event_type=AuditEventType.CODE_GENERATION,
        user_id=user_id,
        timestamp=datetime.utcnow(),
        resource="code_generator",
        action="generate",
        details={"language": request_data.get("language"), "size": len(request_data.get("description", ""))},
        ip_address=ip,
        user_agent=user_agent
    ))
    
    # Utfør kodegenerering
    result = code_generator.generate(request_data)
    return result
```

---

## Sikkerhetscheckliste for deployment

### Pre-deployment
- [ ] Alle secrets i miljøvariabler/secrets management
- [ ] TLS/SSL konfigurert og testet
- [ ] Rate limiting implementert
- [ ] Input validering på alle endpoints
- [ ] Audit logging aktivert
- [ ] Backup-rutiner testet
- [ ] Security scanning fullført
- [ ] GDPR compliance verifisert

### Post-deployment
- [ ] Monitoring og alerting fungerer
- [ ] Security events logges korrekt
- [ ] Performance innenfor forventede rammer
- [ ] Backup-prosedyrer fungerer
- [ ] Disaster recovery plan testet
- [ ] Penetration testing utført
- [ ] Compliance audit fullført

---

**Sikkerhet er ikke et mål, men en kontinuerlig prosess. Hold PAD Framework oppdatert og følg beste praksis for sikker utvikling! 🔒**