import string, random
import pyautogui
import time
import os
from datetime import datetime

now = datetime.now()
secret_log = "log.txt"

real_now = now.strftime("%d/%m/%Y %H:%M:%S")

def crack_password():
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
                with open(secret_log, "a") as f:
                    f.writelines([f"{real_now}\n{main_2}\n{main_3}\n{main_4}", "\n"])
                quit_app()
            index += 1
        guess_attempts += 1

def read_log():
    log_check = os.path.isfile(secret_log)
    if log_check:
        with open(secret_log, "r") as logf:
            log_content = logf.read()
        print("Log file:\n" + str(log_content))
        quit_app()
    else:
        log_error()


def clear_log():
    log_check = os.path.isfile(secret_log)
    if log_check:
        confirm = input("Clear log? (y/n): ").lower()
        if confirm == "y":
            with open(secret_log, "w") as logf:
                logf.write("")
            print("Done!")
            quit_app()
        else:
            quit_app()
    else:
        log_error()

def log_error():
    print("Log not found!")
    quit_app()

def quit_app():
    input("Press Enter to exit...")
    quit()

choice = input("Welcome to Password Cracker!\n\n1) Crack password\n2) Read Log\n3) Clear Log\n4) Exit\n\nChoice: ")
if choice == "1":
    crack_password()
elif choice == "2":
    read_log()
elif choice == "3":
    clear_log()
elif choice == "4":
    quit()
else:
    raise ValueError("Invalid choice!")