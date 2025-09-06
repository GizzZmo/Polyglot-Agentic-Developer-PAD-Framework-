"""
context_agent.py
Definerer Kunnskaps- og kontekst-agenten som holder oversikt over kodebasen og avhengigheter.
"""

class ContextAgent:
    """
    Agent for å opprettholde intern modell av kodebasen og kontekst.
    """

    def __init__(self):
        self.context = "Standard kontekst"

    def get_context(self) -> str:
        """
        Returnerer nåværende kontekst for kodegenerering.
        """
        return self.context

    def update_context(self, new_context: str):
        """
        Oppdaterer intern kontekst.
        """
        self.context = new_context
