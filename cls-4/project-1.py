
import random
import os

def guess_number():
    target_number = random.randint(1, 100)  # Fixed typo
    attempts = 0
    while True:
        try:
            guess = int(input("Enter a number: "))  # Fixed input prompt
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < target_number:
            print("Too low")
        elif guess > target_number:
            print("Too high")
        else:

            print(f"You chose the right number!{target_number}")
            print(f"It took you {attempts} attempts.")
            break


guess_number()


import zipfile
with zipfile.ZipFile("new.zip", "w") as file:
    zip.write("project-1.py")