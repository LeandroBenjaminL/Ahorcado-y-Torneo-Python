"""Módulo de categorías y selección de palabras para el ahorcado."""
from errors import InvalidInputError

CATEGORY_ITEMS = {
    "tecnology": ["python", "variable", "funcion", "bucle", "entero", "programa", "codigo"],
    "social": ["amistad", "familia", "escuela", "trabajo", "reunion", "partido", "equipo"],
    "nature": ["montaña", "oceano", "bosque", "desierto", "volcan", "laguna", "pradera"],
    "house": ["cocina", "ventana", "escalera", "dormitorio", "balcon", "jardin", "garage"],
}


def show_categories(categories: dict) -> None:
    """Muestra las categorías disponibles con sus palabras."""
    for cat,words in categories.items():
        print(f' - {cat}: {", " .join(words)}')
        print()

def choose_category() -> list:
    """Solicita al usuario que elija una categoría.
    Devuelve la lista de palabras de la categoría elegida.
    """
    while True:
        show_categories(CATEGORY_ITEMS)
        try:
            user_election = input('Elije una categoria válida').strip().lower()
            if user_election in CATEGORY_ITEMS:
                return  CATEGORY_ITEMS[user_election]
            raise InvalidInputError('Ingrese una categoria válida')

        except InvalidInputError as e:
            print(f'Entrada no válida: {e}')
            continue
