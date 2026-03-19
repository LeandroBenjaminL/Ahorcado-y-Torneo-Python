"""Definición de la clase Team para representar un equipo de fútbol."""
class Team:
    """Representa un equipo participante en el torneo."""
    def __init__(self, team_name: str ):
        """
        Inicializa un equipo con su nombre.

        Args:
            team_name: Nombre del equipo.
        """
        self.team_name = team_name  # Nombre del equipo en minúsculas
        self.wins = 0
        self.draws = 0
        self.losses = 0

    def __str__(self):
        """
        Representación legible del equipo.

        Returns:
            El nombre del equipo como string.
        """
        return f'{self.team_name} : {self.wins} | {self.draws} | {self.losses} | {self.points} '
    def new_game(self, win: int, draws: int, losses: int):
        """s"""
        self.wins += win
        self.draws += draws
        self.losses += losses

    @property
    def points(self):
        """Calcula los puntos totales en base a victorias y empates """
        return (self.wins * 3) + (self.draws * 1)
