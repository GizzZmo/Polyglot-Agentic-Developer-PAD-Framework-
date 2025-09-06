"""
Tester for ContextAgent.
"""
from pad.context_agent import ContextAgent

def test_context_update_and_get():
    agent = ContextAgent()
    agent.update_context("ny kontekst")
    assert agent.get_context() == "ny kontekst"
