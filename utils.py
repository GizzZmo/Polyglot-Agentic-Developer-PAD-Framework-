"""
utils.py
Hjelpefunksjoner som kan deles mellom agentene.
"""

def format_code_block(code: str) -> str:
    """
    Formaterer kode som et konsollvennlig kodeblokk.
    """
    return f"```\n{code}\n```"
