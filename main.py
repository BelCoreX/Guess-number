from logic import start_game
from menu import main_menu


def main():
    mode_choice = main_menu()
    start_game(mode_choice)


if __name__ == "__main__":
    main()
