import random


CHECK_WELCOME = True
def welcome():
    global CHECK_WELCOME
    if CHECK_WELCOME:
        print('Привет! давай сыграем в игру "угадай число"\nЯ загадаю число от 1 до 100, твоя задача УГАДАТЬ).')
    CHECK_WELCOME = False


def replay() -> bool:
    """Сыграем еще раз?"""
    while True:
        otvet = input('Сыграем еще раз? (Да/Нет): ').lower()
        if otvet == "да":
            return True
        elif otvet == "нет":
            return False
        else:
            print("Некорректный ввод")


def user_input() -> int:
    while True:
        y = input("Введите число: ")
        if y.isdigit():
            return int(y)
        print("Некорректный ввод")


def game():
    x = random.randint(1, 100)
    n = 1
    y = user_input()
    while x != y:
        n += 1
        if y > x:
            print("Упс! много")
        elif y < x:
            print("Ах! мало")
        y = user_input()
    print(f"Молодец попал! кол-во попыток {n}")


def main_loop():
    welcome()
    game()
    if replay():
        main_loop()


main_loop()
