"""
context_agent.py
Definerer Kunnskaps- og kontekst-agenten som holder oversikt over
kodebasen og avhengigheter.

Dette modulet inneholder ContextAgent, som fungerer som PAD-systemets
"langtidsminne". Agenten opprettholder en intern modell av hele kodebasen,
inkludert struktur, avhengigheter, API-er og designmønstre.

Classes:
    ContextAgent: Hovedklasse for kontekst- og kunnskapshåndtering.

Example:
    >>> from pad.context_agent import ContextAgent
    >>> context = ContextAgent()
    >>> context.update_context("Python Flask prosjekt")
    >>> print(context.get_context())
"""


class ContextAgent:
    """
    Agent for å opprettholde intern modell av kodebasen og kontekst.

    ContextAgent fungerer som PAD-systemets kunnskapsbase og langtidsminne.
    Den opprettholder en detaljert forståelse av kodebasestruktur,
    avhengigheter, API-definisjoner og designmønstre for å informere
    kodegenerering og beslutninger.

    Attributes:
        context (str): Nåværende kontekstuell informasjon om kodebasen

    Capabilities:
        - Kodebase-kartlegging og -analyse
        - Avhengighetssporing
        - API-dokumentasjon og -discovry
        - Designmønster-gjenkjenning
        - Arkitekturforståelse

    Example:
        >>> context = ContextAgent()
        >>> context.update_context("Django REST API prosjekt med PostgreSQL")
        >>> current_context = context.get_context()
    """

    def __init__(self) -> None:
        """
        Initialiserer ContextAgent med standard kontekst.

        Setter opp grunnleggende kontekstuell tilstand som kan utvides
        og oppdateres etter hvert som agenten lærer mer om kodebasen.
        """
        self.context = "Standard kontekst"

    def get_context(self) -> str:
        """
        Returnerer nåværende kontekst for kodegenerering.

        Gir tilgang til den samlede kontekstuelle informasjonen som
        ContextAgent har samlet om kodebasen. Denne informasjonen
        brukes av andre agenter for å informere deres beslutninger.

        Returns:
            str: Nåværende kontekstuell informasjon om kodebasen

        Example:
            >>> context = ContextAgent()
            >>> current_context = context.get_context()
            >>> print(current_context)
            Standard kontekst
        """
        return self.context

    def update_context(self, new_context: str) -> None:
        """
        Oppdaterer intern kontekst.

        Lar andre komponenter i systemet oppdatere ContextAgent's
        forståelse av kodebasen når ny informasjon blir tilgjengelig.

        Args:
            new_context (str): Ny kontekstuell informasjon som skal integreres

        Example:
            >>> context = ContextAgent()
            >>> context.update_context("React TypeScript prosjekt med Material-UI")
            >>> print(context.get_context())
            React TypeScript prosjekt med Material-UI

        Note:
            I en fullstendig implementasjon ville dette involvere sofistikert
            merging av ny kontekst med eksisterende kunnskap.
        """
        self.context = new_context
