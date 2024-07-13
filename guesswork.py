from random import *

s = int(input("Введите начало диапазона: "))
q = int(input("Введите конец диапазона: "))
num = randint(s, q)
print("Добро пожаловать в числовую угадайку")


def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= 100


def input_num():
    while True:
        guess = input(f"Введите число от {s} до {q}: ")
        if is_valid(guess):
            return int(guess)
        else:
            print("А может быть все-таки введем целое число от 1 до 100?")


def compare_num():
    count = 0
    while True:
        n = input_num()
        if n < num:
            print("Ваше число меньше загаданного, попробуйте еще разок")
            count = count + 1
            print("Количество неудачных попыток: ", count)
        elif n > num:
            print("Ваше число больше загаданного, попробуйте еще разок")
            count = count + 1
            print("Количество неудачных попыток: ", count)
        else:
            print("Вы угадали, поздравляем!")
            print("Количество неудачных попыток: ", count)
            break


compare_num()
