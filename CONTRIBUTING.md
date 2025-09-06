# Bidragsveiledning for PAD Framework

Tusen takk for din interesse i å bidra til PAD (Polyglot Agentic Developer) Framework! Dette dokumentet gir en omfattende guide for å bidra til prosjektet på en effektiv og konsistent måte.

## 📋 Innholdsfortegnelse

- [Bidragsveiledning for PAD Framework](#bidragsveiledning-for-pad-framework)
  - [📋 Innholdsfortegnelse](#-innholdsfortegnelse)
  - [🤝 Oppførselskodeks](#-oppførselskodeks)
  - [🚀 Kom i gang](#-kom-i-gang)
    - [🔧 Utviklingsmiljø](#-utviklingsmiljø)
    - [📦 Installasjon for utvikling](#-installasjon-for-utvikling)
  - [📝 Utviklingsstandard](#-utviklingsstandard)
    - [🐍 Python Kodestil](#-python-kodestil)
    - [📖 Dokumentasjon](#-dokumentasjon)
    - [🏷️ Type Hints](#️-type-hints)
  - [🧪 Testing](#-testing)
    - [🏃‍♂️ Kjøre tester](#️-kjøre-tester)
    - [✍️ Skrive tester](#️-skrive-tester)
    - [📊 Test Coverage](#-test-coverage)
  - [🔄 Bidragsprosess](#-bidragsprosess)
    - [🌿 Branching-strategi](#-branching-strategi)
    - [💬 Commit-meldinger](#-commit-meldinger)
    - [🔍 Pull Request prosess](#-pull-request-prosess)
  - [🐛 Rapportering av bugs](#-rapportering-av-bugs)
  - [💡 Foreslå nye funksjoner](#-foreslå-nye-funksjoner)
  - [🏗️ Arkitektur og design](#️-arkitektur-og-design)
    - [🎯 Designprinsipper](#-designprinsipper)
    - [🔧 Agent-utvikling](#-agent-utvikling)
  - [📚 Dokumentasjonsbidrag](#-dokumentasjonsbidrag)
  - [🔒 Sikkerhet](#-sikkerhet)
  - [🌍 Internasjonalisering](#-internasjonalisering)
  - [🏅 Anerkjennelse](#-anerkjennelse)
  - [❓ Spørsmål og støtte](#-spørsmål-og-støtte)

## 🤝 Oppførselskodeks

Vi forplikter oss til å opprettholde et åpent og inkluderende miljø. Alle bidragsytere forventes å følge vår oppførselskodeks:

- **Vær respektfull**: Behandle alle med respekt og profesjonalitet
- **Vær konstruktiv**: Gi konstruktiv tilbakemelding og kritikk
- **Vær tålmodig**: Forstå at alle har forskjellige erfaringsnivåer
- **Vær åpen**: Vær åpen for ulike perspektiver og tilnærminger
- **Vær inkluderende**: Skap et miljø hvor alle føler seg velkomne

Brudd på oppførselskodeksen kan rapporteres til prosjektvedlikeholderne.

## 🚀 Kom i gang

### 🔧 Utviklingsmiljø

**Systemkrav:**
- Python 3.9 eller nyere
- Git
- IDE med Python-støtte (anbefalt: VS Code, PyCharm)
- Docker (valgfritt, for containerisering)

**Anbefalte verktøy:**
- `pyenv` for Python versjonshåndtering
- `poetry` eller `pip-tools` for avhengighetshåndtering
- `pre-commit` for automatisk kodekvalitetskontroll

### 📦 Installasjon for utvikling

1. **Fork og klon repository:**
```bash
# Fork repository på GitHub, deretter:
git clone https://github.com/ditt-brukernavn/Polyglot-Agentic-Developer-PAD-Framework-.git
cd Polyglot-Agentic-Developer-PAD-Framework-

# Legg til upstream remote
git remote add upstream https://github.com/GizzZmo/Polyglot-Agentic-Developer-PAD-Framework-.git
```

2. **Opprett utviklingsmiljø:**
```bash
# Opprett virtuelt miljø
python -m venv venv
source venv/bin/activate  # På Windows: venv\Scripts\activate

# Installer avhengigheter
pip install -r requirements.txt

# Installer utviklingsavhengigheter
pip install -r requirements-dev.txt  # Hvis tilgjengelig
```

3. **Installer pre-commit hooks:**
```bash
pip install pre-commit
pre-commit install
```

4. **Verifiser installasjon:**
```bash
# Kjør tester
python -m pytest

# Sjekk kodestil
flake8 .

# Type checking
mypy .
```

## 📝 Utviklingsstandard

### 🐍 Python Kodestil

Vi følger **PEP 8** med noen tilpasninger:

**Linje lengde:** Maksimum 100 karakterer (ikke 79)
```python
# ✅ Riktig
def long_function_name(parameter_one: str, parameter_two: int, 
                      parameter_three: bool) -> str:
    return f"Result: {parameter_one}"

# ❌ Feil - for lang linje
def long_function_name(parameter_one: str, parameter_two: int, parameter_three: bool) -> str:
```

**Import-organisering:**
```python
# Standard library imports
import os
import sys
from typing import Dict, List, Optional

# Third-party imports
import requests
from pydantic import BaseModel

# Local imports
from pad.agents.base import BaseAgent
from pad.utils.logging import get_logger
```

**Navngivningskonvensjoner:**
- **Klasser**: `PascalCase` (eks: `CodeGenAgent`)
- **Funksjoner og variabler**: `snake_case` (eks: `generate_code`)
- **Konstanter**: `UPPER_SNAKE_CASE` (eks: `MAX_RETRY_ATTEMPTS`)
- **Private medlemmer**: prefikser med underscore (eks: `_internal_method`)

### 📖 Dokumentasjon

**Modul-docstrings:**
```python
"""
agent_base.py
Definerer base-klassen for alle PAD-agenter.

Dette modulet inneholder BaseAgent-klassen som fungerer som grunnlaget
for alle spesialiserte agenter i PAD-systemet. Den definerer felles
grensesnitt og funksjonalitet.

Classes:
    BaseAgent: Abstrakt base-klasse for alle agenter

Example:
    >>> from pad.agents.base import BaseAgent
    >>> class MyAgent(BaseAgent):
    ...     def process(self, input_data): pass
"""
```

**Klasse-docstrings:**
```python
class CodeGenAgent(BaseAgent):
    """
    Agent for polyglott kodegenerering og refaktorering.
    
    CodeGenAgent er ansvarlig for å generere høykvalitets kode på tvers
    av multiple programmeringsspråk basert på naturlig språkbeskrivelser
    og kontekstuell informasjon.
    
    Attributes:
        supported_languages (List[str]): Liste over støttede språk
        template_engine (TemplateEngine): Motor for kodescaffolds
        
    Example:
        >>> agent = CodeGenAgent()
        >>> code = agent.generate("Create a REST API endpoint", context)
    """
```

**Funksjon-docstrings:**
```python
def generate_code(self, description: str, context: CodeContext) -> GeneratedCode:
    """
    Genererer kode basert på beskrivelse og kontekst.
    
    Args:
        description (str): Naturlig språkbeskrivelse av ønsket kode
        context (CodeContext): Kontekstuell informasjon om kodebasen
        
    Returns:
        GeneratedCode: Objekt som inneholder generert kode og metadata
        
    Raises:
        ValidationError: Hvis beskrivelsen er ugyldig
        GenerationError: Hvis kodegenerering feiler
        
    Example:
        >>> result = agent.generate_code("Create a user model", context)
        >>> print(result.code)
    """
```

### 🏷️ Type Hints

Alle offentlige funksjoner **må** ha type hints:

```python
from typing import Dict, List, Optional, Union

# ✅ Riktig
def process_data(items: List[str], config: Dict[str, Any]) -> Optional[str]:
    return None

# ❌ Feil - mangler type hints
def process_data(items, config):
    return None
```

**Komplekse typer:**
```python
from typing import TypeVar, Generic, Protocol

T = TypeVar('T')

class Processor(Generic[T]):
    def process(self, item: T) -> T:
        return item

class Validatable(Protocol):
    def validate(self) -> bool: ...
```

## 🧪 Testing

### 🏃‍♂️ Kjøre tester

```bash
# Alle tester
python -m pytest

# Med verbose output
python -m pytest -v

# Spesifikk testfil
python -m pytest pad/tests/test_orchestrator.py

# Spesifikk test
python -m pytest pad/tests/test_orchestrator.py::test_plan_returns_input

# Med coverage
python -m pytest --cov=pad --cov-report=html
```

### ✍️ Skrive tester

**Test-organisering:**
```
pad/tests/
├── unit/
│   ├── test_orchestrator.py
│   ├── test_codegen_agent.py
│   └── test_qa_agent.py
├── integration/
│   ├── test_agent_communication.py
│   └── test_end_to_end.py
└── fixtures/
    ├── sample_code.py
    └── test_data.json
```

**Test-eksempel:**
```python
import pytest
from unittest.mock import Mock, patch
from pad.codegen_agent import CodeGenAgent
from pad.context_agent import ContextAgent

class TestCodeGenAgent:
    """Test suite for CodeGenAgent."""
    
    @pytest.fixture
    def agent(self):
        """Create a CodeGenAgent instance for testing."""
        return CodeGenAgent()
    
    @pytest.fixture
    def mock_context(self):
        """Create a mock ContextAgent for testing."""
        context = Mock(spec=ContextAgent)
        context.get_context.return_value = "Test context"
        return context
    
    def test_generate_code_basic(self, agent, mock_context):
        """Test basic code generation functionality."""
        # Arrange
        description = "Create a simple function"
        
        # Act
        result = agent.generate_code(description, mock_context)
        
        # Assert
        assert result is not None
        assert isinstance(result, str)
        assert description in result
        
    def test_generate_code_with_invalid_input(self, agent, mock_context):
        """Test error handling with invalid input."""
        with pytest.raises(ValueError):
            agent.generate_code("", mock_context)
    
    @patch('pad.codegen_agent.openai_client')
    def test_generate_code_with_mocked_api(self, mock_api, agent, mock_context):
        """Test code generation with mocked external API."""
        # Arrange
        mock_api.generate.return_value = "Generated code"
        
        # Act
        result = agent.generate_code("Test description", mock_context)
        
        # Assert
        assert "Generated code" in result
        mock_api.generate.assert_called_once()
```

### 📊 Test Coverage

Vi streber etter høy testkvalitet:

- **Minimum 90%** linje-coverage for alle moduler
- **100%** coverage for kritiske sikkerhetsfunksjoner
- **Integration tests** for agent-kommunikasjon
- **End-to-end tests** for komplette arbeidsflyter

## 🔄 Bidragsprosess

### 🌿 Branching-strategi

Vi bruker **Git Flow** med tilpasninger:

**Branch-typer:**
- `main`: Stabil, produksjonsklar kode
- `develop`: Integrering av nye funksjoner
- `feature/beskrivelse`: Nye funksjoner
- `bugfix/beskrivelse`: Feilrettinger
- `hotfix/beskrivelse`: Kritiske feilrettinger for produksjon

**Navngivning:**
```bash
# Funksjoner
feature/add-context-caching
feature/improve-error-handling

# Bugfixes
bugfix/fix-orchestrator-timeout
bugfix/resolve-memory-leak

# Hotfixes
hotfix/security-vulnerability-fix
```

### 💬 Commit-meldinger

Vi følger **Conventional Commits** standarden:

```bash
# Format: type(scope): description
feat(codegen): add support for Rust code generation
fix(qa): resolve static analysis timeout issue
docs(api): update CodeGenAgent documentation
test(integration): add end-to-end workflow tests
refactor(orchestrator): simplify task delegation logic
```

**Typer:**
- `feat`: Ny funksjonalitet
- `fix`: Feilrettinger
- `docs`: Dokumentasjonsendringer
- `test`: Testendringer
- `refactor`: Koderefaktorering
- `perf`: Ytelsesoptimaliseringer
- `style`: Kodestilendringer
- `ci`: CI/CD endringer

### 🔍 Pull Request prosess

1. **Opprett feature branch:**
```bash
git checkout develop
git pull upstream develop
git checkout -b feature/din-funksjon
```

2. **Implementer endringer:**
   - Følg kodestandarder
   - Skriv tester for ny funksjonalitet
   - Oppdater dokumentasjon

3. **Kjør kvalitetskontroll:**
```bash
# Tester
python -m pytest

# Kodestil
flake8 .

# Type checking
mypy .

# Sikkerhet
bandit -r pad/
```

4. **Commit og push:**
```bash
git add .
git commit -m "feat(scope): beskrivelse av endring"
git push origin feature/din-funksjon
```

5. **Opprett Pull Request:**
   - Bruk PR-template
   - Inkluder detaljert beskrivelse
   - Link til relaterte issues
   - Be om review fra relevant maintainer

**PR-template:**
```markdown
## Beskrivelse
Kort beskrivelse av endringene.

## Type endring
- [ ] Bug fix
- [ ] Ny funksjonalitet
- [ ] Refaktorering
- [ ] Dokumentasjon

## Testing
- [ ] Eksisterende tester kjører
- [ ] Nye tester lagt til
- [ ] Manuell testing utført

## Checklist
- [ ] Koden følger prosjektets stilguide
- [ ] Selvreview utført
- [ ] Kommentarer lagt til i kompleks kode
- [ ] Dokumentasjon oppdatert
```

## 🐛 Rapportering av bugs

Før du rapporterer en bug:

1. **Sjekk eksisterende issues** for duplikater
2. **Reproduser problemet** konsistent
3. **Samle relevant informasjon**

**Bug rapport template:**
```markdown
## Bug Beskrivelse
Klar beskrivelse av problemet.

## Reprodusering
Steg for å reprodusere:
1. Gå til '...'
2. Klikk på '...'
3. Se feil

## Forventet oppførsel
Beskriv hva som skulle skje.

## Skjermbilder
Legg ved skjermbilder hvis relevant.

## Miljø
- OS: [Windows/Mac/Linux]
- Python versjon: [3.9/3.10/3.11]
- PAD versjon: [0.1.0]

## Tilleggsinformasjon
Annen relevant informasjon.
```

## 💡 Foreslå nye funksjoner

**Feature request template:**
```markdown
## Funksjonsbeskrivelse
Klar beskrivelse av ønsket funksjonalitet.

## Motivasjon
Hvorfor er denne funksjonen nyttig?

## Foreslått løsning
Beskriv hvordan du ser for deg at dette implementeres.

## Alternativer
Andre løsninger du har vurdert.

## Påvirkning
Hvilke deler av systemet vil påvirkes?
```

## 🏗️ Arkitektur og design

### 🎯 Designprinsipper

1. **Single Responsibility**: Hver agent har ett klart ansvarsområde
2. **Open/Closed**: Åpen for utvidelse, lukket for modifikasjon
3. **Dependency Inversion**: Avheng av abstraksjoner, ikke konkrete implementasjoner
4. **Interface Segregation**: Små, spesifikke grensesnitt
5. **DRY (Don't Repeat Yourself)**: Eliminer kodeduplisering

### 🔧 Agent-utvikling

**Ny agent checklist:**
- [ ] Arv fra `BaseAgent`
- [ ] Implementer påkrevde metoder
- [ ] Legg til type hints
- [ ] Skriv omfattende docstrings
- [ ] Implementer feilhåndtering
- [ ] Legg til logging
- [ ] Skriv unit tests
- [ ] Skriv integrasjonstester
- [ ] Oppdater arkitekturdokumentasjon

**Agent template:**
```python
"""
new_agent.py
Beskrivelse av den nye agenten.
"""
from typing import Any, Dict
from pad.agents.base import BaseAgent
from pad.utils.logging import get_logger

logger = get_logger(__name__)

class NewAgent(BaseAgent):
    """
    Beskrivelse av agentens rolle og ansvar.
    """
    
    def __init__(self) -> None:
        """Initialize the agent."""
        super().__init__()
        logger.info("NewAgent initialized")
    
    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process input and return result.
        
        Args:
            input_data: Input data to process
            
        Returns:
            Processed result
            
        Raises:
            ProcessingError: If processing fails
        """
        try:
            # Implementation here
            result = self._do_processing(input_data)
            logger.info("Processing completed successfully")
            return result
        except Exception as e:
            logger.error(f"Processing failed: {e}")
            raise
    
    def _do_processing(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Internal processing logic."""
        # Implementation details
        pass
```

## 📚 Dokumentasjonsbidrag

Dokumentasjon er like viktig som kode:

**Dokumentasjonstyper:**
- **API-dokumentasjon**: Docstrings og API-referanser
- **Brukerveiledninger**: How-to guides og tutorials
- **Arkitekturdokumentasjon**: Tekniske spesifikasjoner
- **Bidragsveiledninger**: Dette dokumentet

**Dokumentasjonsstandard:**
- Skriv på norsk for brukervendt dokumentasjon
- Bruk engelsk for teknisk/API-dokumentasjon
- Inkluder kodeeksempler
- Hold dokumentasjonen oppdatert med kodeendringer

## 🔒 Sikkerhet

**Sikkerhetsprinsipper:**
- Aldri commit secrets eller API-nøkler
- Valider all brukerinput
- Bruk parameteriserte queries for database
- Implementer proper feilhåndtering
- Følg OWASP beste praksis

**Rapportering av sårbarheter:**
Send en e-post til sikkerhetsteamet i stedet for å opprette en offentlig issue.

## 🌍 Internasjonalisering

Selv om PAD primært er rettet mot norske utviklere, støtter vi:
- **Engelsk dokumentasjon** for tekniske detaljer
- **Norsk brukergrensesnitt** og brukerveiledninger
- **Unicode-støtte** i alle tekstfelter
- **Lokaliserte feilmeldinger**

## 🏅 Anerkjennelse

Alle bidragsytere vil bli anerkjent i:
- README.md Contributors-seksjonen
- CHANGELOG.md for hver release
- GitHub Contributors-siden

## ❓ Spørsmål og støtte

**Hvor får jeg hjelp?**
- **GitHub Discussions**: For generelle spørsmål og diskusjoner
- **GitHub Issues**: For bug-rapporter og feature requests
- **Stack Overflow**: Tag spørsmål med `pad-framework`

**Prosjektmaintainers:**
- **GizzZmo** - Hovedutvikler (@GizzZmo)

---

**Takk for at du bidrar til PAD Framework! Sammen bygger vi fremtiden for AI-assistert programvareutvikling. 🚀**