# משחק ניחוש מספרים - גרסה ראשונה
# המחשב בוחר מספר בין 1 ל-100, ואתה מנסה לנחש אותו.

import random  # ספרייה שמגרילה מספרים אקראיים

secret = random.randint(1, 100)  # המספר הסודי
tries = 0                        # מונה ניסיונות

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100.")

while True:  # לולאה שרצה עד שמנחשים נכון
    guess_text = input("Your guess: ")

    # בדיקה שהוקלד מספר ולא משהו אחר
    if not guess_text.isdigit():
        print("Please type a number.")
        continue

    guess = int(guess_text)
    tries += 1

    if guess < secret:
        print("Too low! Try higher.")
    elif guess > secret:
        print("Too high! Try lower.")
    else:
        print(f"Correct! The number was {secret}.")
        print(f"You got it in {tries} tries.")
        break  # יציאה מהלולאה, המשחק נגמר
