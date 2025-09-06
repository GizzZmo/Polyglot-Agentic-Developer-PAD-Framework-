"""
orchestrator.py
Definerer Planleggings- og orkestrerings-agenten som koordinerer alle andre agenter i PAD-systemet.
"""
from .codegen_agent import CodeGenAgent
from .qa_agent import QualityAssuranceAgent
from .context_agent import ContextAgent
from .user_agent import UserInteractionAgent

class OrchestratorAgent:
    """
    Orkestrerer agentene og prosessen fra brukerforespørsel til leveranse.
    """

    def __init__(self):
        self.user_agent = UserInteractionAgent()
        self.context_agent = ContextAgent()
        self.codegen_agent = CodeGenAgent()
        self.qa_agent = QualityAssuranceAgent()

    def run(self):
        """
        Hovedløkken for PAD-systemet. Tar imot brukerinput, planlegger og fordeler oppgaver til agentene.
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

    def plan(self, user_input: str):
        """
        Dekomponerer brukerens forespørsel til en plan.
        """
        # For demo: returnerer brukerinput som en "plan"
        return user_input
