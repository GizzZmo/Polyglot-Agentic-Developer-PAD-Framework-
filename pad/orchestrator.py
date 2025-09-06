"""
orchestrator.py
Definerer Planleggings- og orkestrerings-agenten som koordinerer alle andre
agenter i PAD-systemet.

Dette modulet inneholder hovedorkestreringen for PAD-systemet. OrchestratorAgent
fungerer som den sentrale koordinatoren som mottar brukerforespørsler, bryter
dem ned i håndterbare oppgaver, og delegerer dem til de respektive spesialiserte
agentene.

Classes:
    OrchestratorAgent: Hovedorkestreringsklasse som koordinerer alle agenter.

Example:
    >>> from pad.orchestrator import OrchestratorAgent
    >>> orchestrator = OrchestratorAgent()
    >>> orchestrator.run()
"""
from .codegen_agent import CodeGenAgent
from .qa_agent import QualityAssuranceAgent
from .context_agent import ContextAgent
from .user_agent import UserInteractionAgent


class OrchestratorAgent:
    """
    Orkestrerer agentene og prosessen fra brukerforespørsel til leveranse.

    OrchestratorAgent er den sentrale komponenten i PAD-systemet som koordinerer
    alle andre agenter. Den mottar brukerforespørsler, planlegger utviklingsoppgaver,
    og delegerer spesifikke oppgaver til de respektive agentene.

    Attributes:
        user_agent (UserInteractionAgent): Håndterer brukerinteraksjon
        context_agent (ContextAgent): Administrerer kodebase-kontekst
        codegen_agent (CodeGenAgent): Genererer og refaktorerer kode
        qa_agent (QualityAssuranceAgent): Utfører kvalitetssikring

    Example:
        >>> orchestrator = OrchestratorAgent()
        >>> orchestrator.run()
    """

    def __init__(self) -> None:
        """
        Initialiserer OrchestratorAgent med alle nødvendige agenter.

        Oppretter instanser av alle spesialiserte agenter som trengs for å
        håndtere komplekse utviklingsoppgaver.
        """
        self.user_agent = UserInteractionAgent()
        self.context_agent = ContextAgent()
        self.codegen_agent = CodeGenAgent()
        self.qa_agent = QualityAssuranceAgent()

    def run(self) -> None:
        """
        Hovedløkken for PAD-systemet. Tar imot brukerinput,
        planlegger og fordeler oppgaver til agentene.

        Denne metoden implementerer hovedarbeidsflyt:
        1. Mottar brukerinput via UserInteractionAgent
        2. Planlegger oppgaver basert på input
        3. Delegerer kodegenerering til CodeGenAgent
        4. Utfører kvalitetssikring via QualityAssuranceAgent
        5. Gir tilbakemelding til brukeren

        Løkken fortsetter til brukeren velger å avslutte med 'exit' eller 'quit'.

        Raises:
            KeyboardInterrupt: Hvis brukeren avbryter med Ctrl+C
        """
        while True:
            user_input = self.user_agent.get_input()
            if user_input.lower() in ["exit", "quit"]:
                print("Avslutter PAD-systemet.")
                break

            task_plan = self.plan(user_input)
            code = self.codegen_agent.generate_code(task_plan, self.context_agent)
            if code:
                qa_result = self.qa_agent.validate_code(code)
                self.user_agent.provide_feedback(qa_result)
            else:
                self.user_agent.provide_feedback("Ingen kode generert.")

    def plan(self, user_input: str) -> str:
        """
        Dekomponerer brukerens forespørsel til en plan.

        Tar en naturlig språkforespørsel fra brukeren og konverterer den til
        en strukturert plan som kan delegeres til spesialiserte agenter.

        Args:
            user_input (str): Brukerens forespørsel i naturlig språk

        Returns:
            str: Strukturert plan for å håndtere forespørselen

        Note:
            Nåværende implementasjon er en demo som returnerer input direkte.
            I en fullstendig implementasjon ville dette involvere LLM-basert
            planlegging og oppgavedekomponering.
        """
        # For demo: returnerer brukerinput som en "plan"
        return user_input
