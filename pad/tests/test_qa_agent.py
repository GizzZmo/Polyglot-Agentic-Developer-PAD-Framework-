"""
Tester for QualityAssuranceAgent.
"""
from pad.qa_agent import QualityAssuranceAgent


def test_validate_code_print_ok() -> None:
    agent = QualityAssuranceAgent()
    result = agent.validate_code("print('ok')")
    assert "OK" in result


def test_validate_code_no_print_warn() -> None:
    agent = QualityAssuranceAgent()
    result = agent.validate_code("x = 1")
    assert "Advarsel" in result
