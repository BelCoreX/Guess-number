import random


def start_game():
    first_number = 1

    while True:
        difficulty = input("Уровень сложности (лёгкий/средний/сложный): ").strip().lower()

        if difficulty == "легкий" or difficulty == "лёгкий":
            last_number = 100
            attempt = 7
            break
        elif difficulty == "средний":
            last_number = 200
            attempt = 8
            break
        elif difficulty == "сложный":
            last_number = 500
            attempt = 10
            break
        else:
            continue

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
