# API Referanse - PAD Framework

Denne dokumenten gir en detaljert oversikt over alle offentlige API-er i PAD Framework. Hver agent og deres tilhørende metoder er dokumentert med eksempler og bruksscenarier.

## 📋 Innholdsfortegnelse

- [Orchestrator Agent API](#orchestrator-agent-api)
- [Code Generation Agent API](#code-generation-agent-api)
- [Quality Assurance Agent API](#quality-assurance-agent-api)
- [Context Agent API](#context-agent-api)
- [User Interaction Agent API](#user-interaction-agent-api)
- [Utility Functions API](#utility-functions-api)
- [Error Handling](#error-handling)
- [Type Definitions](#type-definitions)

## Orchestrator Agent API

### `class OrchestratorAgent`

Hovedorkestreringen som koordinerer alle andre agenter i PAD-systemet.

#### `__init__() -> None`

Initialiserer OrchestratorAgent med alle nødvendige agenter.

```python
from pad.orchestrator import OrchestratorAgent

orchestrator = OrchestratorAgent()
```

#### `run() -> None`

Starter hovedløkken for PAD-systemet.

**Beskrivelse:** Kjører kontinuerlig løkke som:
1. Mottar brukerinput
2. Planlegger oppgaver
3. Delegerer til agenter
4. Presenterer resultater

**Raises:**
- `KeyboardInterrupt`: Hvis brukeren avbryter med Ctrl+C

**Eksempel:**
```python
orchestrator = OrchestratorAgent()
try:
    orchestrator.run()
except KeyboardInterrupt:
    print("Avslutter PAD-systemet")
```

#### `plan(user_input: str) -> str`

Dekomponerer brukerforespørsel til strukturert plan.

**Parametere:**
- `user_input` (str): Brukerens forespørsel i naturlig språk

**Returnerer:**
- `str`: Strukturert plan for oppgaveløsning

**Eksempel:**
```python
orchestrator = OrchestratorAgent()
plan = orchestrator.plan("Lag en REST API for brukeradministrasjon")
print(f"Generert plan: {plan}")
```

---

## Code Generation Agent API

### `class CodeGenAgent`

Agent for polyglott kodegenerering og refaktorering.

#### `generate_code(task_description: str, context_agent: ContextAgent) -> str`

Genererer kode basert på oppgavebeskrivelse og kontekst.

**Parametere:**
- `task_description` (str): Naturlig språkbeskrivelse av ønsket kode
- `context_agent` (ContextAgent): Agent som gir kontekstuell informasjon

**Returnerer:**
- `str`: Generert kildekode med kommentarer og metadata

**Raises:**
- `ValidationError`: Hvis task_description er tom eller ugyldig
- `ContextError`: Hvis kontekst ikke kan hentes
- `GenerationError`: Hvis kodegenerering feiler

**Eksempel:**
```python
from pad.codegen_agent import CodeGenAgent
from pad.context_agent import ContextAgent

codegen = CodeGenAgent()
context = ContextAgent()
context.update_context("Python Flask prosjekt")

code = codegen.generate_code(
    "Lag en funksjon som validerer e-postadresser",
    context
)
print(code)
```

**Utdata-eksempel:**
```python
# Generert kode for: Lag en funksjon som validerer e-postadresser
# Kontekst: Python Flask prosjekt
import re
from typing import bool

def validate_email(email: str) -> bool:
    """
    Validerer om en gitt streng er en gyldig e-postadresse.
    
    Args:
        email (str): E-postadresse som skal valideres
        
    Returns:
        bool: True hvis e-posten er gyldig, False ellers
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
```

---

## Quality Assurance Agent API

### `class QualityAssuranceAgent`

Agent for kvalitetssikring gjennom statisk analyse og testing.

#### `validate_code(code: str) -> str`

Utfører omfattende kvalitetsvalidering av gitt kode.

**Parametere:**
- `code` (str): Kildekode som skal valideres

**Returnerer:**
- `str`: Detaljert kvalitetsrapport med funn og anbefalinger

**Validering inkluderer:**
- Syntakskorrekthet
- Kodestil og PEP 8-samsvar
- Potensielle bugs og logiske feil
- Sikkerhetssårbarheter
- Ytelseskonsiderasjoner

**Eksempel:**
```python
from pad.qa_agent import QualityAssuranceAgent

qa = QualityAssuranceAgent()
code_to_validate = """
def unsafe_function(user_input):
    exec(user_input)  # Sikkerhetsproblem!
    return "OK"
"""

report = qa.validate_code(code_to_validate)
print(report)
```

**Rapport-eksempel:**
```
=== KVALITETSRAPPORT ===

🔴 KRITISKE PROBLEMER:
- Linje 2: Bruk av exec() med brukerinput (Sikkerhetssårbarhet)
- Linje 1: Mangler type hints

🟡 ADVARSLER:
- Funksjon mangler docstring
- Ingen input-validering

🟢 POSITIVE FUNN:
- Konsistent innrykk
- Enkel funksjonsstruktur

SAMLET SCORE: 3/10
ANBEFALING: Krever betydelige forbedringer før produksjon
```

---

## Context Agent API

### `class ContextAgent`

Agent for kodebase-kunnskap og konteksthåndtering.

#### `__init__() -> None`

Initialiserer ContextAgent med grunnleggende kontekst.

```python
from pad.context_agent import ContextAgent

context = ContextAgent()
```

#### `get_context() -> str`

Henter gjeldende kontekstuell informasjon.

**Returnerer:**
- `str`: Strukturert kontekstinformasjon om kodebasen

**Eksempel:**
```python
context = ContextAgent()
current_context = context.get_context()
print(f"Gjeldende kontekst: {current_context}")
```

#### `update_context(new_context: str) -> None`

Oppdaterer intern kontekstmodell.

**Parametere:**
- `new_context` (str): Ny kontekstuell informasjon

**Kontekst-eksempler:**
```python
context = ContextAgent()

# Prosjekttype
context.update_context("Django REST API prosjekt")

# Teknologistabel
context.update_context("Python 3.9, PostgreSQL, Redis, Docker")

# Arkitekturmønster
context.update_context("Mikrotjeneste-arkitektur med API Gateway")

# Framework-spesifikk
context.update_context("React TypeScript med Material-UI komponenter")
```

**Avansert kontekst-håndtering:**
```python
# JSON-struktur for kompleks kontekst
import json

complex_context = {
    "project_type": "E-commerce platform",
    "technologies": {
        "backend": ["Python", "Django", "PostgreSQL"],
        "frontend": ["React", "TypeScript", "Redux"],
        "infrastructure": ["Docker", "Kubernetes", "AWS"]
    },
    "patterns": ["Repository pattern", "Command pattern"],
    "apis": [
        {"name": "User API", "version": "v1", "endpoint": "/api/v1/users"},
        {"name": "Product API", "version": "v2", "endpoint": "/api/v2/products"}
    ]
}

context.update_context(json.dumps(complex_context))
```

---

## User Interaction Agent API

### `class UserInteractionAgent`

Agent for brukerinteraksjon og kommunikasjon.

#### `get_input() -> str`

Henter input fra brukeren via konsoll.

**Returnerer:**
- `str`: Brukerens input som streng

**Bemerk:** Denne metoden er interaktiv og blokkerer til brukerinput mottas.

```python
from pad.user_agent import UserInteractionAgent

user_agent = UserInteractionAgent()
user_request = user_agent.get_input()
```

#### `provide_feedback(message: str) -> None`

Formidler tilbakemelding til brukeren.

**Parametere:**
- `message` (str): Melding som skal vises til brukeren

**Tilbakemeldingstyper:**
```python
user_agent = UserInteractionAgent()

# Informasjon
user_agent.provide_feedback("Kodegenerering startet...")

# Suksess
user_agent.provide_feedback("✅ Kode generert suksessfullt!")

# Advarsel
user_agent.provide_feedback("⚠️ Advarsel: Kodekvalitet kan forbedres")

# Feil
user_agent.provide_feedback("❌ Feil: Ugyldig syntaks oppdaget")

# Formatert kode
code_block = '''
def hello_world():
    print("Hello, World!")
'''
user_agent.provide_feedback(f"Generert kode:\n```python{code_block}```")
```

---

## Utility Functions API

### `format_code_block(code: str) -> str`

Formaterer kode for konsollvisning.

**Parametere:**
- `code` (str): Råkode som skal formateres

**Returnerer:**
- `str`: Formatert kode med markdown-stil blokker

**Eksempel:**
```python
from pad.utils import format_code_block

raw_code = "def hello():\n    print('world')"
formatted = format_code_block(raw_code)
print(formatted)
```

**Utdata:**
```
```
def hello():
    print('world')
```
```

---

## Error Handling

PAD Framework definerer spesifikke exception-typer for ulike feilscenarier:

### `ValidationError`

Kastes når input-validering feiler.

```python
from pad.exceptions import ValidationError

try:
    codegen.generate_code("", context)
except ValidationError as e:
    print(f"Valideringsfeil: {e}")
```

### `ContextError`

Kastes ved problemer med konteksthenting.

```python
from pad.exceptions import ContextError

try:
    context = context_agent.get_context()
except ContextError as e:
    print(f"Kontekstfeil: {e}")
```

### `GenerationError`

Kastes ved feil i kodegenerering.

```python
from pad.exceptions import GenerationError

try:
    code = codegen.generate_code(description, context)
except GenerationError as e:
    print(f"Genereringsfeil: {e}")
```

---

## Type Definitions

PAD Framework bruker omfattende type hints for bedre utvikleropplevelse:

### Grunnleggende typer

```python
from typing import Dict, List, Optional, Union, Any

# Agent-kommunikasjon
AgentResponse = Dict[str, Any]
TaskDescription = str
ContextData = Dict[str, Union[str, List[str], Dict[str, Any]]]

# Kodegenerering
LanguageType = Literal["python", "javascript", "typescript", "java", "go", "rust"]
CodeMetadata = Dict[str, Union[str, int, float, List[str]]]

# Kvalitetssikring
QualityScore = float  # 0.0 - 10.0
QualityIssue = Dict[str, Union[str, int, str]]  # severity, line, message
```

### Avanserte typer

```python
from dataclasses import dataclass
from enum import Enum
from typing import Protocol

class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class GeneratedCode:
    """Representerer generert kode med metadata."""
    content: str
    language: LanguageType
    framework: Optional[str]
    dependencies: List[str]
    quality_score: QualityScore
    created_at: datetime

class Validatable(Protocol):
    """Protocol for validerbare objekter."""
    def validate(self) -> bool: ...

class Agent(Protocol):
    """Protocol for alle agenter."""
    def process(self, input_data: Any) -> Any: ...
```

### Eksempel på type-sikker koding

```python
from typing import List
from pad.types import GeneratedCode, LanguageType

def batch_generate_code(
    descriptions: List[str], 
    target_language: LanguageType
) -> List[GeneratedCode]:
    """
    Genererer kode for flere beskrivelser.
    
    Args:
        descriptions: Liste med kodebeskrivelser
        target_language: Målprogrammeringsspråk
        
    Returns:
        Liste med GeneratedCode objekter
    """
    results: List[GeneratedCode] = []
    
    for desc in descriptions:
        code = codegen.generate_code(desc, context)
        result = GeneratedCode(
            content=code,
            language=target_language,
            framework=None,
            dependencies=[],
            quality_score=8.5,
            created_at=datetime.now()
        )
        results.append(result)
    
    return results
```

---

## Avanserte bruksscenarier

### Integrert arbeidsflyt

```python
from pad.orchestrator import OrchestratorAgent
from pad.codegen_agent import CodeGenAgent
from pad.qa_agent import QualityAssuranceAgent
from pad.context_agent import ContextAgent
from pad.user_agent import UserInteractionAgent

# Sett opp agenter
orchestrator = OrchestratorAgent()
codegen = CodeGenAgent()
qa = QualityAssuranceAgent()
context = ContextAgent()
user_agent = UserInteractionAgent()

# Konfigurer kontekst
context.update_context("Python Flask REST API med SQLAlchemy")

# Generer kode
task = "Opprett en User model med validering"
generated_code = codegen.generate_code(task, context)

# Kvalitetssikring
qa_report = qa.validate_code(generated_code)

# Brukerrapport
user_agent.provide_feedback(f"Kode generert: {generated_code}")
user_agent.provide_feedback(f"Kvalitetsrapport: {qa_report}")
```

### Batch-operasjoner

```python
tasks = [
    "Opprett User model",
    "Lag authentication middleware", 
    "Implementer CRUD endpoints",
    "Legg til input validering"
]

results = []
for task in tasks:
    try:
        code = codegen.generate_code(task, context)
        quality = qa.validate_code(code)
        results.append({
            "task": task,
            "code": code,
            "quality": quality
        })
    except Exception as e:
        user_agent.provide_feedback(f"Feil ved {task}: {e}")

# Sammendrag
user_agent.provide_feedback(f"Fullført {len(results)} av {len(tasks)} oppgaver")
```

Denne API-referansen gir et omfattende overblikk over PAD Framework's programmatiske grensesnitt. For flere eksempler og detaljert brukerveiledning, se [brukermanualen](USER_GUIDE.md) og [arkitekturdokumentasjonen](docs/architecture.md).