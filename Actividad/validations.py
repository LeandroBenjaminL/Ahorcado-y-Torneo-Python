"""Validaciones de entrada del juego del ahorcado."""

from errors import InvalidInputError


def validate_letter(letter: str) -> None:
    """Valida la letra ingresada por el usuario.
    Lanza EntradaInvalidaError si la entrada no es válida.
    """
    if len(letter) == 0:
        raise InvalidInputError("No ingresaste nada.")
    if len(letter) > 1:
        raise InvalidInputError("Solo podés ingresar una letra a la vez.")
    if not letter.isalpha():
        raise InvalidInputError(f"'{letter}' no es una letra válida.")
