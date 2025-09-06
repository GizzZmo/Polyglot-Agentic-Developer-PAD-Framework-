"""
codegen_agent.py
Definerer Kode-genererings-agenten som håndterer generering, refaktorering og optimalisering av kode.
"""
from .context_agent import ContextAgent

class CodeGenAgent:
    """
    Agent for å generere og refaktorere kode på flere språk.
    """

    def generate_code(self, task_description: str, context_agent: ContextAgent) -> str:
        """
        Genererer kode basert på en oppgavebeskrivelse og kontekst.
        """
        # For demo: Returnerer et dummy-kodesnutt
        context = context_agent.get_context()
        return f"# Generert kode for: {task_description}\n# Kontekst: {context}\nprint('Hei, verden!')"
