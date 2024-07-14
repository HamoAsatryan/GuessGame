from random import *

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
chars = ""

n = int(input("Enter the number of passwords to generate passwords: "))
length = int(input("Enter the length of the password: "))
add_digit = input("Whether to include the numbers? (y = yes, n = no)").strip()
add_lowercase = input("Include lowercase letters? (y = yes, n = no)").strip()
add_uppercase = input("Include capital letters? (y = yes, n = no)").strip()
add_punctuation = input(
    "Include symbols such as !#$%&*+-=?@^_? (y = yes, n = no)"
).strip()
remove_badsymbols = input("Exclude characters il1Lo0O? (y = yes, n = no)").strip()

if add_digit.lower() == "y":
    chars += digits
if add_lowercase.lower() == "y":
    chars += lowercase_letters
if add_uppercase.lower() == "y":
    chars += uppercase_letters
if add_punctuation.lower() == "y":
    chars += punctuation
if remove_badsymbols.lower() == "y":
    for c in "il1Lo0O":
        chars = chars.replace(c, "")


def generate_password(length, chars):
    password = ""
    for _ in range(length):
        password += choice(chars)
    return password


for _ in range(n):
    password = generate_password(length, chars)
    print(password)
