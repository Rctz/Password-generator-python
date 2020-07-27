# -*- coding: utf-8 -*-
import string
import random
import cowsay

char = string.ascii_letters + string.digits + string.punctuation # letter + number + spacial char
password = ""
cowsay.kitty("Password generator by Rctz :)")

try:
    name = input("Use for: ") # input use for
    length = int(input("Password length: ")) # input password length
    for i in range(length):
        password += random.choice(char) # random

    print(password)
    with open("password.txt", mode = "a+") as f: # write to .txt
        f.write(name + "\n")
        f.write(password + "\n\n")

except ValueError: # if wrong password length
    print("Error!: please correct password length")
