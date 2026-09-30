import sys


def make_list(list):
    for i, item in enumerate(list, start=1):
        print(f"{i}. {item}")


def main_menu():
    menu_list = ["Играть", "Выход"]
    mode_list = ["Обычный режим", "Режим на время"]
    difficulty_list = ["Лёгкий", "Средний", "Сложный"]

    while True:
        print("=" * 40)
        print("ДОБРО ПОЖАЛОВАТЬ В ГЛАВНОЕ МЕНЮ".center(40))
        print("=" * 40)
        make_list(menu_list)
        print("-" * 40)

        while True:
            try:
                menu_choice = int(input("Выберите пункт меню: "))

                if menu_choice in range(1, 3):
                    break
            except ValueError:
                continue

        if menu_choice == 1:
            print("\n" + "=" * 40)
            print("ВЫБЕРИТЕ ИГРОВОЙ РЕЖИМ")
            print("=" * 40)
            make_list(mode_list)
            print("-" * 40)

            while True:
                try:
                    mode_choice = int(input("Выберите пункт меню: "))

                    if mode_choice in range(1, 3):
                        break
                except ValueError:
                    continue

            if mode_choice == 1:
                print("\n" + "=" * 40)
                print("ВЫБЕРИТЕ УРОВЕНЬ СЛОЖНОСТИ")
                print("=" * 40)
                make_list(difficulty_list)
                print("-" * 40)

                while True:
                    try:
                        difficulty_choice = int(input("Выберите пункт меню: "))

                        if difficulty_choice in range(1, 4):
                            return difficulty_choice
                    except ValueError:
                        continue
            else:
                print("Режим в разработке!")
        else:
            sys.exit()
