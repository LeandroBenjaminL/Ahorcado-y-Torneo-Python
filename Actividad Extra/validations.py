"""Validaciones de entrada del simulador de torneo de fútbol."""
from errors import InvalidInputError


def validate_team_input(team: str, available_teams: list) -> None:
    """Valida que el equipo ingresado no esté vacío y esté en la lista disponible.

    Args:
        team: Nombre del equipo ingresado.
        available_teams: Lista de equipos válidos.
    """
    if not team:
        raise InvalidInputError("No ingresó ningún equipo.")
    if team not in available_teams:
        raise InvalidInputError(f"'{team}' no es un equipo válido. Elegí uno de la lista.")


def validate_yes_no(answer: str) -> bool:
    """Valida que la respuesta sea si o no.

    Args:
        answer: Respuesta ingresada por el usuario.
    """
    if answer not in ("si", "no"):
        raise InvalidInputError("Ingrese solamente si o no.")
    elif answer == "si":
        return True
    else:
        return False


def validate_score(score: str) -> int:
    """Valida que el marcador sea un número entero no negativo.

    Args:
        score: Marcador ingresado como string.

    Returns:
        El marcador convertido a entero.
    """
    try:
        value = int(score)
    except ValueError as exc:
        raise InvalidInputError("El marcador debe ser un número entero.") from exc
    if value < 0:
        raise InvalidInputError("El marcador no puede ser negativo.")
    return value
