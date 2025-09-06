"""
main.py
Starter PAD-systemet ved å initialisere og koordinere alle agentene.
"""
from pad.orchestrator import OrchestratorAgent


def main() -> None:
    """
    Oppstartspunkt for PAD-systemet.
    """
    orchestrator = OrchestratorAgent()
    orchestrator.run()


if __name__ == "__main__":
    main()
