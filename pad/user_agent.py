"""
user_agent.py
Definerer Brukerinteraksjons-agenten som håndterer kommunikasjon med brukeren.

Dette modulet inneholder UserInteractionAgent, som fungerer som hovedgrensesnittet
mellom PAD-systemet og den menneskelige brukeren. Agenten håndterer input fra
brukeren og formidler tilbakemelding fra systemet på en brukervennlig måte.

Classes:
    UserInteractionAgent: Hovedklasse for brukerinteraksjon og kommunikasjon.

Example:
    >>> from pad.user_agent import UserInteractionAgent
    >>> agent = UserInteractionAgent()
    >>> agent.provide_feedback("Kode generert successfully!")
"""


class UserInteractionAgent:
    """
    Agent for interaksjon med bruker: input og tilbakemelding.

    UserInteractionAgent fungerer som den primære kommunikasjonskanalen
    mellom PAD-systemet og brukeren. Den håndterer inputsammling,
    formidler systemtilbakemelding, og sørger for en god brukeropplevelse.

    Capabilities:
        - Inputhåndtering fra bruker
        - Formatert tilbakemelding til bruker
        - Feilhåndtering og feilmeldinger
        - Prompt engineering guidance
        - Progressrapportering

    Example:
        >>> agent = UserInteractionAgent()
        >>> user_input = agent.get_input()  # Interactive, can't demo easily
        >>> agent.provide_feedback("Operation completed successfully!")
    """

    def get_input(self) -> str:
        """
        Leser inn brukerforespørsel fra konsoll.

        Presenterer en prompt til brukeren og venter på deres input.
        Funksjonen blokkerer til brukeren har gitt input.

        Returns:
            str: Brukerens input som en streng

        Example:
            >>> agent = UserInteractionAgent()
            >>> user_input = agent.get_input()
            PAD > lag en funksjon som beregner fibonacci
            >>> print(f"Bruker sa: {user_input}")
            Bruker sa: lag en funksjon som beregner fibonacci

        Note:
            Denne metoden er interaktiv og krever brukerinteraksjon,
            så den kan ikke demonstreres i automatiserte tester.
        """
        return input("PAD > ")

    def provide_feedback(self, message: str) -> None:
        """
        Gir tilbakemelding til brukeren.

        Formaterer og presenterer meldinger fra PAD-systemet til brukeren
        på en konsistent og lesbar måte.

        Args:
            message (str): Melding som skal vises til brukeren

        Example:
            >>> agent = UserInteractionAgent()
            >>> agent.provide_feedback("Kode generert successfully!")
            [PAD]: Kode generert successfully!
            >>> agent.provide_feedback("Advarsel: Kodekvalitet kan forbedres")
            [PAD]: Advarsel: Kodekvalitet kan forbedres

        Note:
            Alle meldinger prefixes med "[PAD]:" for å identifisere
            systemtilbakemelding klart for brukeren.
        """
        print(f"[PAD]: {message}")
