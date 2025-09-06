"""
Tester for OrchestratorAgent.
"""
from pad.orchestrator import OrchestratorAgent


def test_plan_returns_input() -> None:
    orchestrator = OrchestratorAgent()
    inp = "lag en funksjon som skriver ut hei"
    assert orchestrator.plan(inp) == inp
