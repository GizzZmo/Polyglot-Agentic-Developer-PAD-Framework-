# Arkitektur og Agentroller for PAD Framework

## Oversikt

PAD benytter en sentral orkestreringsagent som koordinerer fire spesialiserte agenter:
- Kodegenerering
- Kvalitetssikring
- Kontekst/kunskap
- Brukerinteraksjon

## Agentroller

**OrchestratorAgent**
- Hovedansvar: Planlegging, koordinering, delegering av utviklingsoppgaver.

**CodeGenAgent**
- Hovedansvar: Generere, refaktorere og optimalisere kode på tvers av språk.

**QualityAssuranceAgent**
- Hovedansvar: Statisk analyse, kjøring av tester og validering av kodekvalitet.

**ContextAgent**
- Hovedansvar: Holde orden på kodebase, avhengigheter og API-strukturer.

**UserInteractionAgent**
- Hovedansvar: All kommunikasjon med bruker, tilbakemeldinger og guiding.

## Dataflyt

1. Bruker sender forespørsel via UserInteractionAgent.
2. OrchestratorAgent bryter ned forespørselen og fordeler deloppgaver.
3. CodeGenAgent genererer kode basert på plan og kontekst.
4. QualityAssuranceAgent kontrollerer kodekvalitet.
5. Feedback sendes tilbake til bruker.

Se mermaid-diagram for visuell oversikt.
