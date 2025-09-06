import random

class CodeGenAgent:
    """
    Agent for å generere/refaktorere kode på flere språk.
    """

    SUPPORTED_LANGUAGES = ["python", "javascript", "java"]

    def generate_code(self, task_description: str, context_agent) -> str:
        """
        Generer kode med støtte for flere språk og hypotetisk LLM-integrasjon.
        """
        lang = self.detect_language(task_description)
        # TODO: Integrer f.eks. OpenAI/GPT her
        if lang == "python":
            code = f"def hello():\n    print('Hei fra PAD!')"
        elif lang == "javascript":
            code = f"function hello() {{\n  console.log('Hei fra PAD!');\n}}"
        else:
            code = f"// [Lang ikke støttet] {task_description}"
        return f"# Språk: {lang}\n{code}"

    def detect_language(self, task: str) -> str:
        for lang in self.SUPPORTED_LANGUAGES:
            if lang in task.lower():
                return lang
        return "python"  # default
