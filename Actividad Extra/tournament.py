"""Definición de la clase Tournament para gestionar un torneo de fútbol."""
from team import Team

class Tournament:
    """Representa un torneo de fútbol con equipos y resultados."""
    def __init__(self ,tournament_name: str):
        """
        Inicializa un torneo vacío con nombre, equipos y resultados.

        Args:
            tournament_name: Nombre del torneo.
        """
        self.tournament_name = tournament_name
        self.teams_table = [] # Lista de objetos Team participantes

    def __str__(self):
        """
        Representación legible del torneo con sus equipos.

        Returns:
            String con el nombre del torneo y la lista de equipos.
        """
        # Reordena la tabla de equipos de mayor a menor puntaje.
        # sorted() devuelve una nueva lista ordenada que reemplaza la original.
        # key=lambda t: t.points indica el criterio de ordenamiento (puntos de cada equipo).
        # reverse=True invierte el orden para obtener de mayor a menor.
        self.teams_table = sorted(self.teams_table, key=lambda t: t.points, reverse=True)
        res = f'torneo: {self.tournament_name}\n'
        for team in self.teams_table:
            res += f"  - {team}\n"
        return res

    def add_team(self, e: Team):
        """
        Agrega un equipo a la lista de participantes del torneo.

        Args:
            team: Instancia de Team a agregar.
        """
        self.teams_table.append(e)

    def remove_team(self, team_name: str) -> None:
        """Elimina un equipo del torneo por su nombre."""
        self.teams_table = [t for t in self.teams_table if t.team_name != team_name]

    def add_result(self, local_team: str, visit_team: str, score1: int, score2: int):
        """
        Registra el resultado de un partido en la tabla de resultados.

        Args:
            local_team: Nombre del equipo local.
            visit_team: Nombre del equipo visitante.
            score1: Goles del equipo local
            score2: Goles del equipo visitante
        """
        # Busca el objeto Team cuyo nombre coincide con local_team dentro de la tabla de equipos.
        # next() devuelve el primer resultado encontrado de la expresión generadora.
        team1 = next ((t for t in self.teams_table if t.team_name == local_team))
        # Busca el objeto Team cuyo nombre coincide con visit_team dentro de la tabla de equipos.
        team2 = next ((t for t in self.teams_table if t.team_name == visit_team))
        if score1 == score2:
            team1.new_game(0,1,0)
            team2.new_game(0,1,0)
        elif score1 > score2:
            team1.new_game(1,0,0)
            team2.new_game(0,0,1)
        else:
            team1.new_game(0,0,1)
            team2.new_game(1,0,0)
