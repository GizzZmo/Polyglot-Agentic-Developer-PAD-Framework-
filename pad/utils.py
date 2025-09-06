"""
utils.py
Hjelpefunksjoner som kan deles mellom agentene.

Dette modulet inneholder nyttige hjelpefunksjoner som brukes av flere
agenter i PAD-systemet. Funksjoner her er designet for å være generiske
og gjenbrukbare på tvers av ulike komponenter.

Functions:
    format_code_block: Formaterer kode som et konsollvennlig kodeblokk

Example:
    >>> from pad.utils import format_code_block
    >>> formatted = format_code_block("print('hello world')")
    >>> print(formatted)
"""


def format_code_block(code: str) -> str:
    """
    Formaterer kode som et konsollvennlig kodeblokk.

    Tar kildekode og wrapper den i markdown-stil kodeblokk-formatting
    for bedre presentasjon i konsoll eller dokumentasjon.

    Args:
        code (str): Kildekode som skal formateres

    Returns:
        str: Formatert kode omgitt av kodeblokk-markører

    Example:
        >>> from pad.utils import format_code_block
        >>> code = "def hello():\\n    print('world')"
        >>> formatted = format_code_block(code)
        >>> print(formatted)
        ```
        def hello():
            print('world')
        ```

    Note:
        Bruker markdown-stil ``` kodeblokk-formatering for
        konsistens med standard utviklerverktøy og dokumentasjon.
    """
    return f"```\n{code}\n```"
