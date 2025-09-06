"""
qa_agent.py
Definerer Kvalitetssikrings-agenten for statisk analyse og testkjøring.
"""
class QualityAssuranceAgent:
    """
    Agent for kvalitetssikring: statisk analyse og tester.
    """

    def validate_code(self, code: str) -> str:
        """
        Utfører grunnleggende "statisk" analyse og simulerer testkjøring.
        """
        # For demo: Sjekker om "print" finnes i koden
        if "print" in code:
            return "Koden inneholder print-setning. (Simulert QA: OK)"
        return "Ingen print-setning funnet. (Simulert QA: Advarsel)"
