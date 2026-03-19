"""Módulo principal del juego del ahorcado."""
import random
from errors import InvalidInputError
from validations import validate_letter
from categories import choose_category, CATEGORY_ITEMS




def ask_continue(prompt: str) -> bool:
    """Pregunta al usuario si desea continuar. Devuelve True si elige si."""
    while True:
        try:
            choice = input(prompt).strip().lower()
            if choice == 'si':
                return True
            elif choice == 'no':
                return False
            else:
                raise InvalidInputError('Ingrese solamente si o no')
        except InvalidInputError as e:
            print(f'Entrada no válida: {e}')

def build_progress(word: str, guessed: list) -> str:
    """Construye y devuelve el progreso actual de la palabra.
    Las letras adivinadas se muestran, el resto como guiones.
    """
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    return progress

def check_win(progress: str) -> bool:
    """Devuelve True si no quedan letras por adivinar."""
    if "_" not in progress:
        return True
    return False



def show_status(attempts: int, guessed: list) -> None:
    """Muestra los intentos restantes y las letras ya usadas."""
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")


def check_letter(letter: str, word: str, guessed: list, attempts: int,points: int) -> tuple:
    """Verifica si la letra está en la palabra y actualiza el estado.
    Devuelve los intentos restantes actualizados.
    """
    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        points -= 1
        print("Esa letra no está en la palabra.")
    print()
    return  attempts, points

def play_round(word: str) -> None:
    """Ejecuta una ronda completa con la palabra dada."""
    points = 6
    guessed = []
    attempts = 6
    while attempts > 0:
        progress = build_progress(word, guessed)
        print(progress)
        if check_win(progress):
            print(f"¡Ganaste! Tu puntaje fue: {points} puntos")
            break
        show_status(attempts, guessed)
        try:
            letter = input("Ingresá una letra: ")
            validate_letter(letter)
            attempts, points= check_letter(letter, word,guessed, attempts,points)
        except InvalidInputError as e:
            print(f'Entrada no válida: {e}')
            continue
    else:
        print(f"¡Perdiste! La palabra era: {word}... Tu puntaje es de: {points}")



def play_game() -> None:
    """Punto de entrada del juego. Elige la palabra e inicia la partida."""

    print("¡Bienvenido al Ahorcado!")
    print()
    available_categories = CATEGORY_ITEMS.copy()
    while available_categories:
        # El usuario elige una categoría, devuelve su nombre y lista de palabras
        category_name, words = choose_category(available_categories)
        print(f'Estas en la categoria: {category_name}')
        # Mezcla las palabras para que salgan en orden aleatorio
        words = random.sample(words, len(words))
        # Elimina la categoría ya jugada para que no vuelva a aparecer
        del available_categories[category_name]
        # Juega una ronda por cada palabra hasta agotar la categoría
        while words:
            word = words.pop()
            play_round(word)
            if not ask_continue('¿Desea jugar con otra palabra? (si/no): '):
                break
        if not ask_continue('¿Desea jugar otra categoría? (si/no): '):
            break
