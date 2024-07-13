from random import *

s = int(input("Enter the beginning of the range: "))
q = int(input("Enter the end of the range: "))
num = randint(s, q)
print("Welcome to the numerical guessing game")


def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= 100


def input_num():
    while True:
        guess = input(f"Enter a number from {s} to {q}: ")
        if is_valid(guess):
            return int(guess)
        else:
            print("Can we still enter an integer from 1 to 100?")


def compare_num():
    count = 0
    while True:
        n = input_num()
        if n < num:
            print("Your number is lower than your guess, try again.")
            count = count + 1
            print("failure rate: ", count)
        elif n > num:
            print("Your number is higher than your guess, try again.")
            count = count + 1
            print("failure rate: ", count)
        else:
            print("You guessed it, congratulations!")
            print("failure rate: ", count)
            break


compare_num()
