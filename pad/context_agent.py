class ContextAgent:
    """
    Opprettholder intern modell av kodebase og kontekst.
    """
    def __init__(self):
        self.context = "Standard kontekst"
        self.code_history = []

    def get_context(self) -> str:
        return self.context

    def update_context(self, new_context: str):
        self.context = new_context

    def update_context_from_code(self, code: str):
        self.code_history.append(code)
        self.context = f"Seneste kodeblokk: {code[:40]}..."
