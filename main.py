from logic import start_game
from menu import main_menu


def main():
    difficulty_choice = main_menu()
    start_game(difficulty_choice)


if __name__ == "__main__":
    main()
