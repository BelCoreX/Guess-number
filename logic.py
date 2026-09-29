import random


def start_game(mode_choice):
    first_number = 1

    if not mode_choice:
        pass
    else:
        if mode_choice == 1:
            last_number = 100
            attempt = 7
        elif mode_choice == 2:
            last_number = 200
            attempt = 8
        else:
            last_number = 500
            attempt = 10

    computer_number = random.randint(first_number, last_number)

    while True:
        try:
            user_number = int(input(f"Введите число от {first_number} до {last_number}: "))

            if not user_number in range(first_number, last_number + 1):
                continue
        except ValueError:
            continue

        if user_number == computer_number:
            print("Вы угадали число!")
            break
        else:
            attempt -= 1

            if not attempt:
                print(f"Вы проиграли! Загаданное число было {computer_number}")
                break
            else:
                hint = "больше" if user_number < computer_number else "меньше"
                print(f"Не правильно! Попыток осталось {attempt}. Загаданное число {hint}")
