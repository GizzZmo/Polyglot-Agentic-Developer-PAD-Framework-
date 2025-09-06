"""
codegen_agent.py
Definerer Kode-genererings-agenten som håndterer generering,
refaktorering og optimalisering av kode.

Dette modulet inneholder CodeGenAgent, som er ansvarlig for all kodegenerering
i PAD-systemet. Agenten er designet for å være polyglott og kan generere kode
i flere programmeringsspråk basert på naturlig språkbeskrivelser og kontekstuell
informasjon.

Classes:
    CodeGenAgent: Hovedklasse for kodegenerering og refaktorering.

Example:
    >>> from pad.codegen_agent import CodeGenAgent
    >>> from pad.context_agent import ContextAgent
    >>> agent = CodeGenAgent()
    >>> context = ContextAgent()
    >>> code = agent.generate_code("lag en funksjon som returnerer sum", context)
"""
from .context_agent import ContextAgent


class CodeGenAgent:
    """
    Agent for å generere og refaktorere kode på flere språk.

    CodeGenAgent er en polyglott AI-agent som kan generere, refaktorere og
    optimalisere kode basert på naturlig språkbeskrivelser. Agenten integrer
    med ContextAgent for å opprettholde awareness av eksisterende kodebase
    og avhengigheter.

    Capabilities:
        - Generere kode i multiple programmeringsspråk
        - Refaktorere eksisterende kode
        - Optimalisere kodeytelse
        - Opprettholde kodestil og konvensjoner

    Example:
        >>> agent = CodeGenAgent()
        >>> context = ContextAgent()
        >>> code = agent.generate_code("lag en REST API endpoint", context)
    """

    def generate_code(self, task_description: str,
                      context_agent: ContextAgent) -> str:
        """
        Genererer kode basert på en oppgavebeskrivelse og kontekst.

        Tar en naturlig språkbeskrivelse av en programmeringsoppgave og
        genererer relevant kode. Bruker kontekst fra ContextAgent for å
        sikre at generert kode integrerer godt med eksisterende kodebase.

        Args:
            task_description (str): Beskrivelse av oppgaven i naturlig språk
            context_agent (ContextAgent): Agent som gir kontekstuell informasjon
                om eksisterende kodebase, avhengigheter og konvensjoner

        Returns:
            str: Generert kode som oppfyller oppgavebeskrivelsen

        Example:
            >>> agent = CodeGenAgent()
            >>> context = ContextAgent()
            >>> code = agent.generate_code("lag en funksjon som beregner factorial", context)
            >>> print(code)
            # Generert kode for: lag en funksjon som beregner factorial
            # Kontekst: Standard kontekst
            print('Hei, verden!')

        Note:
            Nåværende implementasjon er en demo. I produksjon ville denne
            integrere med LLM-er for faktisk kodegenerering.
        """
        # For demo: Returnerer et dummy-kodesnutt
        context = context_agent.get_context()
        return (f"# Generert kode for: {task_description}\n"
                f"# Kontekst: {context}\nprint('Hei, verden!')")

