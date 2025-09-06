class UserInteractionAgent:
    """
    Agent for interaksjon med bruker: støtter CLI og API.
    """
    def get_input(self) -> str:
        return input("PAD > ")

    def provide_feedback(self, message: str):
        print(f"[PAD]: {message}")

    def api_feedback(self, message: str):
        return {"feedback": message}
