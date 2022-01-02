import string, random
import pyautogui
import time
from datetime import datetime

now = datetime.now()

real_now = now.strftime("%d/%m/%Y %H:%M:%S")

guess_attempts = 0
list_chars = list(string.printable)
clue = []
password_guess = ""
password_input = pyautogui.password("Enter password: ")

start_time = time.time()

for a in password_input:
    clue.append("?")

while password_input != password_guess:
    time.sleep(0.1)
    index = 0
    random_chars = random.choices(list_chars, k=len(password_input))
    patch_2 = f"Password: {clue}"
    patch = f"<==={random_chars}===>, "
    print(patch + patch_2)
    print()
    while index < len(password_input):
        if password_input[index] == random_chars[index]:
            clue[index] = random_chars[index]
            password_guess = "".join(clue)
        if password_guess == password_input:
            end_time = time.time()
            main = f"\n\nList result: {clue}"
            main_2 = f"\nYour password: {password_guess}"
            main_4 = f"Guessed attempts: {guess_attempts} times guess"
            main_3 = "Time: " + str(int(end_time - start_time)) + " seconds"
            print(main)
            print(main_2)
            print(main_3)
            print(main_4)
            input("Press any key to exit...")
            with open("log.txt", "a") as f:
                f.writelines([f"{real_now}\n{main_2}\n{main_3}\n{main_4}", "\n"])
            break
        index += 1
    guess_attempts += 1