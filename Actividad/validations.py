"""Validaciones de entrada del juego del ahorcado."""

from errors import EntradaInvalidaError


def validate_letter(letter: str) -> None:
    """Valida la letra ingresada por el usuario.
    Lanza EntradaInvalidaError si la entrada no es válida.
    """
    if len(letter) == 0:
        raise EntradaInvalidaError("No ingresaste nada.")
    if len(letter) > 1:
        raise EntradaInvalidaError("Solo podés ingresar una letra a la vez.")
    if not letter.isalpha():
        raise EntradaInvalidaError(f"'{letter}' no es una letra válida.")
