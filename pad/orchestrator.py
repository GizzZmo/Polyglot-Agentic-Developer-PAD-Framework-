import logging
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
        logging.basicConfig(level=logging.INFO)

    def run(self):
        while True:
            user_input = self.user_agent.get_input()
            if user_input.lower() in ["exit", "quit"]:
                print("Avslutter PAD-systemet.")
                break

            result = self.process_request(user_input)
            self.user_agent.provide_feedback(result["feedback"])
            print(result["code"])

    def plan(self, user_input: str):
        # Her kan du implementere parsing, splitting og AI-basert oppgavedeling
        return user_input

    def process_request(self, user_input: str):
        logging.info("Starter prosessering av forespørsel")
        plan = self.plan(user_input)
        code = self.codegen_agent.generate_code(plan, self.context_agent)
        feedback = self.qa_agent.validate_code(code)
        self.context_agent.update_context_from_code(code)
        return {"code": code, "feedback": feedback}
