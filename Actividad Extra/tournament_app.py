"""Simulador de tabla de posiciones de un torneo de fútbol.
Permite al usuario armar el torneo eligiendo equipos disponibles
desde una lista, con validación de entradas."""

from tournament import Tournament
from team import Team
from errors import InvalidInputError
from validations import validate_team_input,validate_yes_no,validate_score

# Constantes
AVAILABLE_TEAMS = [
    "argentinos juniors", "atletico tucuman", "banfield", "belgrano",
    "boca juniors", "central cordoba", "defensa y justicia",
    "estudiantes de la plata", "deportivo riestra",
    "gimnasia y esgrima de la plata", "huracan",
    "independiente", "river plate", "tigre", "san lorenzo",
]


def show_menu() -> None:
    """Muestra las opciones del menú."""
    print("\n=== Menú ===")
    print("1. Agregar equipo")
    print("2. Registrar resultado")
    print("3. Mostrar tabla")
    print("4. Eliminar equipo")
    print("5. Salir")


def show_available_teams(teams: list) -> None:
    """Muestra la lista de equipos disponibles para elegir."""

    print("\nEquipos disponibles:")
    print("| ".join(teams))
    print('\n')




def ask_input(prompt: str) -> str:
    """Pide un input hasta que sea válido."""
    while True:
        try:
            res = input(prompt).strip().lower()
            if validate_yes_no(res):
                continue
            return res
        except InvalidInputError as e:
            print(f"⚠️  Advertencia: {e}")
            continue
    
def ask_valid_input(prompt: str, validate_func, *args):
    """Solicita un input al usuario hasta recibir uno válido.
    
    Args:
        prompt: Mensaje que se muestra al usuario.
        validate_func: Función de validación a aplicar.
        *args: Argumentos adicionales para la función de validación.
    
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




def choose_team(available_teams: list) -> str:
    """
    Solicita al usuario que elija un equipo de la lista disponible.
    Repite la solicitud hasta recibir una entrada válida.

    Args:
        available_teams: Lista de equipos que aún pueden ser elegidos.

    Returns:
        El nombre del equipo elegido en minúsculas.
    """

    while True:
        try:
            user_election = input('Ingrese un equipo ').lower()
            validate_team_input(user_election,available_teams)
            return user_election
        except InvalidInputError as e:
            print(f"⚠️  Advertencia: {e}")
            print("Intente de nuevo.\n")
            continue




def add_teams_to_tournament(tournament: Tournament, team: str,teams:list,table:list) -> None:
    """
    Flujo interactivo para que el usuario agregue equipos al torneo.
    Cada equipo elegido se elimina de la lista de disponibles.

    Args:
        tournament: Instancia del torneo al que se agregarán los equipos.
    """

    new_equipe = Team(team)
    tournament.add_team(new_equipe)
    print(f'El equipo: {team} fue agregado con exito')
    teams.remove(team)
    table.append(team)







def add_team_flow(t: Tournament, teams_table: list, copy:list) -> None:
    """Flujo para agregar un equipo al torneo."""

    while True:
        try:
            show_available_teams(copy)
            new_team = choose_team(copy)
            add_teams_to_tournament(t,new_team,copy, teams_table)
            res = ask_input('¿Desea agregar otro equipo? (si/no): ')
            if res == "no":
                break
        except InvalidInputError as e:
            print(f"⚠️  Advertencia: {e}")
            print("Intente de nuevo.\n")
            continue




def register_result_flow(tournament: Tournament, teams_table: list) -> None:
    """Flujo para registrar un resultado."""
    while True:
        print(tournament)
        name_local = ask_valid_input("Ingrese el nombre del equipo local: ",
                                     validate_team_input, teams_table)
        name_visit = ask_valid_input("Ingrese el nombre del equipo visitante: ",
                                     validate_team_input, teams_table)
        local =  int (ask_valid_input("Ingrese el marcador del local: ", validate_score))
        visit = int (ask_valid_input("Ingrese el marcador del visitante: ", validate_score))
        tournament.add_result(name_local, name_visit, local, visit)
        print("El resultado fue añadido con éxito.")
        res = ask_valid_input("¿Desea agregar otro resultado? (si/no): ", validate_yes_no)
        if res == "si":
            continue
        break



def main() -> None:
    """Bucle principal del programa."""

    print("=== Bienvenido al simulador de torneo de fútbol ===\n")
    tournament = Tournament("Liga Argentina")
    teams_table = []
    available_teams_copy = AVAILABLE_TEAMS[:]

    while True:
        show_menu()
        option = input("Ingrese una opción: ").strip()

        if option == "1":
            add_team_flow(tournament, teams_table,available_teams_copy)
        elif option == "2":
            register_result_flow(tournament, teams_table)
        elif option == "3":
            print(tournament)
        elif option == "4":
            # eliminar equipo
            pass
        elif option == "5":
            print("¡FIN!")
            break
        else:
            print(" Opción inválida. Ingrese un número del 1 al 5.")
