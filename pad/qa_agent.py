import subprocess
import tempfile

class QualityAssuranceAgent:
    """
    Agent for kvalitetssikring: statisk analyse og tester.
    """

    def validate_code(self, code: str) -> str:
        """
        Kjører flake8 statisk analyse på Python-kode.
        """
        if "def " in code:
            with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as tmp:
                tmp.write(code.encode("utf-8"))
                tmp.flush()
                try:
                    result = subprocess.run(
                        ["flake8", tmp.name],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        timeout=5,
                    )
                    if result.stdout:
                        return f"Flake8-feil:\n{result.stdout.decode()}"
                    return "Koden er PEP8-kompatibel."
                except Exception as e:
                    return f"Statisk analyse feilet: {str(e)}"
        return "Ingen validerbar Python-funksjon funnet."
