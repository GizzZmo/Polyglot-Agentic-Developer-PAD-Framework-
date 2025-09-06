"""
Tester for UserInteractionAgent (kun feedback-funksjon, input kan ikke automatiseres enkelt).
"""
from pad.user_agent import UserInteractionAgent

def test_provide_feedback_prints(capsys):
    agent = UserInteractionAgent()
    agent.provide_feedback("hei")
    captured = capsys.readouterr()
    assert "[PAD]: hei" in captured.out
