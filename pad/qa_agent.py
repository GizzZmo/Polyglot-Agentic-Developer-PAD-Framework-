"""
qa_agent.py
Definerer Kvalitetssikrings-agenten for statisk analyse og testkjøring.

Dette modulet inneholder QualityAssuranceAgent, som er ansvarlig for å sikre
kvalitet og integritet av generert kode. Agenten utfører statisk analyse,
kjører automatiserte tester, og validerer kodestandarder.

Classes:
    QualityAssuranceAgent: Hovedklasse for kvalitetssikring og validering.

Example:
    >>> from pad.qa_agent import QualityAssuranceAgent
    >>> qa_agent = QualityAssuranceAgent()
    >>> result = qa_agent.validate_code("print('hello world')")
    >>> print(result)
"""


class QualityAssuranceAgent:
    """
    Agent for kvalitetssikring: statisk analyse og tester.

    QualityAssuranceAgent er ansvarlig for å sikre at all generert og
    refaktorert kode oppfyller høye kvalitetsstandarder. Agenten utfører
    omfattende validering inkludert statisk analyse, testkjøring og
    sikkerhetskontroller.

    Capabilities:
        - Statisk kodeanalyse
        - Automatisert testkjøring
        - Sikkerhetstesting
        - Kodestilvalidering
        - Performance-analyse

    Example:
        >>> qa_agent = QualityAssuranceAgent()
        >>> result = qa_agent.validate_code("def hello(): print('world')")
        >>> print(result)
    """

    def validate_code(self, code: str) -> str:
        """
        Utfører grunnleggende "statisk" analyse og simulerer testkjøring.

        Analyserer gitt kode for kvalitet, stil og potensielle problemer.
        Returnerer en rapport med funn og anbefalinger.

        Args:
            code (str): Kildekode som skal valideres

        Returns:
            str: Valideringsrapport med status og eventuelle advarsler

        Example:
            >>> qa_agent = QualityAssuranceAgent()
            >>> result = qa_agent.validate_code("print('hello')")
            >>> print(result)
            Koden inneholder print-setning. (Simulert QA: OK)

        Note:
            Nåværende implementasjon er en demo som kun sjekker for print-setninger.
            I produksjon ville dette inkludere omfattende statisk analyse,
            linting, sikkerhetssjegging og automatiserte tester.
        """
        # For demo: Sjekker om "print" finnes i koden
        if "print" in code:
            return "Koden inneholder print-setning. (Simulert QA: OK)"
        return "Ingen print-setning funnet. (Simulert QA: Advarsel)"
