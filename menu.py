import sys


def main_menu():
    while True:
        print("=" * 40)
        print("ДОБРО ПОЖАЛОВАТЬ В ГЛАВНОЕ МЕНЮ".center(40))
        print("=" * 40)
        print("1. Играть")
        print("2. Выход")
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
            print("1. Обычный режим")
            print("2. Режим на время")
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
                print("1. Легкий")
                print("2. Средний")
                print("3. Сложный")
                print("-" * 40)

                while True:
                    try:
                        mode_choice = int(input("Выберите пункт меню: "))

                        if mode_choice in range(1, 4):
                            return mode_choice
                    except ValueError:
                        continue
            else:
                print("Режим в разработке!")
        else:
            sys.exit()
