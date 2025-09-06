"""
Tester for CodeGenAgent.
"""
from pad.codegen_agent import CodeGenAgent
from pad.context_agent import ContextAgent


def test_generate_code_includes_task() -> None:
    agent = CodeGenAgent()
    context = ContextAgent()
    code = agent.generate_code("skriv ut hei", context)
    assert "skriv ut hei" in code
