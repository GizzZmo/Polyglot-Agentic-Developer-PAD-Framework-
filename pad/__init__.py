"""
PAD (Polyglot Agentic Developer) Framework
==========================================

PAD-rammeverket er et neste generasjons AI-drevet programmeringspartner som
opererer som et multi-agent system. Systemet er designet for å fungere som
en senior, flerspråklig applikasjonsutvikler som autonomt kan utføre komplekse,
fler-trinns programvareutviklingsarbeidsflyter.

Arkitektur
----------
PAD består av fem spesialiserte agenter som samarbeider:

1. **OrchestratorAgent** - Hovedkoordinator som planlegger og delegerer oppgaver
2. **CodeGenAgent** - Polyglott kodegenerering og refaktorering
3. **QualityAssuranceAgent** - Statisk analyse og kvalitetssikring
4. **ContextAgent** - Kodebase-kunnskap og konteksthåndtering
5. **UserInteractionAgent** - Brukergrensesnitt og kommunikasjon

Moduler
-------
- orchestrator: Hovedorkestrering og oppgavedelegering
- codegen_agent: Kodegenerering og refaktorering
- qa_agent: Kvalitetssikring og testing
- context_agent: Kontekst- og kunnskapshåndtering
- user_agent: Brukerinteraksjon og feedback
- utils: Delte hjelpefunksjoner

Eksempel på bruk
----------------
    >>> from pad.orchestrator import OrchestratorAgent
    >>> orchestrator = OrchestratorAgent()
    >>> orchestrator.run()  # Starter hovedløkken

Designprinsipper
----------------
- **Modularitet**: Hver agent har en klar, avgrenset ansvarsområde
- **Samarbeid**: Agenter kommuniserer og deler informasjon effektivt
- **Utvidbarhet**: Arkitekturen støtter enkelt tillegg av nye agenter
- **Kvalitet**: Innebyggd kvalitetssikring i alle trinn
- **Polyglott**: Støtte for multiple programmeringsspråk

For mer informasjon, se dokumentasjonen for hver enkelt agent og
arkitekturdokumentasjonen i docs/-mappen.
"""
