"""Simulador de tabla de posiciones de un torneo de fútbol.
Permite al usuario armar el torneo eligiendo equipos disponibles
desde una lista, con validación de entradas."""

from tournament import Tournament
from team import Team
from errors import InvalidInputError
from validations import validate_team_input, validate_yes_no, validate_score

# Constantes
AVAILABLE_TEAMS = [
    "argentinos juniors", "atletico tucuman", "banfield", "belgrano",
    "boca juniors", "central cordoba", "defensa y justicia",
    "estudiantes de la plata", "deportivo riestra",
    "gimnasia y esgrima de la plata", "huracan",
    "independiente", "river plate", "tigre", "san lorenzo",
]


def show_menu() -> None:
    """Muestra las opciones del menú principal."""
    print("\n=== Menú ===")
    print("1. Agregar equipo")
    print("2. Registrar resultado")
    print("3. Mostrar tabla")
    print("4. Eliminar equipo")
    print("5. Salir")


def show_available_teams(teams: list) -> None:
    """Muestra la lista de equipos disponibles en formato de columnas.

    Args:
        teams: Lista de equipos disponibles para mostrar.
    """
    if not teams:
        print('No hay equipos disponibles para agregar')
        return None
    print("\nEquipos disponibles:")
    cols = 3
    for i, team in enumerate(teams):
        print(f"{team:<35}", end="")  # ancho fijo de 35 caracteres
        if (i + 1) % cols == 0:      # salto de línea cada 3 equipos
            print()
    print('\n')


def ask_valid_input(prompt: str, validate_func, *args):
    """Solicita un input al usuario hasta recibir uno válido.

    Repite la solicitud si la validación falla, mostrando el error al usuario.

    Args:
        prompt: Mensaje que se muestra al usuario.
        validate_func: Función de validación a aplicar sobre el input.
        *args: Argumentos adicionales requeridos por validate_func.

    Returns:
        El resultado de validate_func si devuelve algo, o el valor ingresado.
    """
    while True:
        try:
            value = input(prompt).strip().lower()
            result = validate_func(value, *args)
            return result if result is not None else value
        except InvalidInputError as e:
            print(f"⚠️  Advertencia: {e}")
            print("Intente de nuevo.\n")
            continue


def choose_team(available_teams: list) -> str:
    """Solicita al usuario que elija un equipo de la lista disponible.

    Args:
        available_teams: Lista de equipos que aún pueden ser elegidos.

    Returns:
        El nombre del equipo elegido en minúsculas.
    """
    return ask_valid_input("Ingrese un equipo: ", validate_team_input, available_teams)


def add_teams_to_tournament(tournament: Tournament, team: str, teams: list, table: list) -> None:
    """Agrega un equipo al torneo y lo elimina de la lista de disponibles.

    Args:
        tournament: Instancia del torneo al que se agregará el equipo.
        team: Nombre del equipo a agregar.
        teams: Lista de equipos disponibles — se elimina el equipo elegido.
        table: Lista de equipos ya agregados al torneo.
    """
    new_team = Team(team)
    tournament.add_team(new_team)
    print(f'El equipo: {team} fue agregado con exito')
    teams.remove(team)
    table.append(team)

def delete_team(t:Tournament, teams_table:list):
    """ Elimina un equipo del torneo"""
    show_available_teams(teams_table)
    team_delete = ask_valid_input('Ingrese el nombre del equipo que desee eliminar',
                                   validate_team_input, teams_table)
    t.remove_team(team_delete)
    teams_table.remove(team_delete)

def add_team_flow(t: Tournament, teams_table: list, copy: list) -> None:
    """Flujo interactivo para agregar equipos al torneo.

    Muestra los equipos disponibles, solicita la elección del usuario
    y repite hasta que el usuario decida no agregar más equipos.

    Args:
        t: Instancia del torneo.
        teams_table: Lista de equipos ya agregados al torneo.
        copy: Copia de la lista de equipos disponibles para elegir.
    """
    while True:
        try:
            if not copy:
                print(' No se puede agragar equipos. ')
                return
            show_available_teams(copy)
            new_team = choose_team(copy)
            add_teams_to_tournament(t, new_team, copy, teams_table)
            # Pregunta si desea agregar otro equipo — devuelve bool
            res = ask_valid_input('¿Desea agregar otro equipo? (si/no): ', validate_yes_no)
            if not res:
                break
        except InvalidInputError as e:
            print(f"⚠️  Advertencia: {e}")
            print("Intente de nuevo.\n")
            continue


def register_result_flow(tournament: Tournament, teams_table: list) -> None:
    """Flujo interactivo para registrar el resultado de un partido.

    Solicita los equipos y marcadores, valida cada entrada por separado
    y registra el resultado en el torneo.

    Args:
        tournament: Instancia del torneo donde se registrará el resultado.
        teams_table: Lista de equipos válidos para validar los nombres ingresados.
    """
    while True:
        print(tournament)
        # Solicita y valida el nombre de cada equipo
        name_local = ask_valid_input("Ingrese el nombre del equipo local: ",
                                     validate_team_input, teams_table)
        name_visit = ask_valid_input("Ingrese el nombre del equipo visitante: ",
                                     validate_team_input, teams_table)
        # Solicita y valida los marcadores — validate_score devuelve int
        local = int(ask_valid_input("Ingrese el marcador del local: ", validate_score))
        visit = int(ask_valid_input("Ingrese el marcador del visitante: ", validate_score))
        tournament.add_result(name_local, name_visit, local, visit)
        print("El resultado fue añadido con éxito.")
        # Pregunta si desea registrar otro resultado — devuelve bool
        res = ask_valid_input("¿Desea agregar otro resultado? (si/no): ", validate_yes_no)
        if res:
            continue
        break


def main() -> None:
    """Bucle principal del programa. Inicializa el torneo y gestiona el menú."""
    print("=== Bienvenido al simulador de torneo de fútbol ===\n")
    tournament = Tournament("Liga Argentina")
    teams_table = []
    available_teams_copy = AVAILABLE_TEAMS[:]

    while True:
        show_menu()
        option = input("Ingrese una opción: ").strip()

        if option == "1":
            add_team_flow(tournament, teams_table, available_teams_copy)
        elif option == "2":
            register_result_flow(tournament, teams_table)
        elif option == "3":
            # Muestra la tabla ordenada por puntaje
            print(tournament)
        elif option == "4":
            delete_team(tournament, teams_table)
        elif option == "5":
            print("¡FIN!")
            break
        else:
            print(" Opción inválida. Ingrese un número del 1 al 5.")
