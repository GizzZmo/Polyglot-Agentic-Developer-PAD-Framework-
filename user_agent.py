"""
user_agent.py
Definerer Brukerinteraksjons-agenten som håndterer kommunikasjon med brukeren.
"""

class UserInteractionAgent:
    """
    Agent for interaksjon med bruker: input og tilbakemelding.
    """

    def get_input(self) -> str:
        """
        Leser inn brukerforespørsel fra konsoll.
        """
        return input("PAD > ")

    def provide_feedback(self, message: str):
        """
        Gir tilbakemelding til brukeren.
        """
        print(f"[PAD]: {message}")
