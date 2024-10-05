import random
from colorama import Fore, Back, Style, init

init(autoreset=True)

print(Fore.YELLOW + "Welcome to Guess A Number game! 🎯")
print("I'm thinking of a number between 1 and 100.")
print("You have to guess the number in 7 attempts.")

number = random.randint(1, 100)
guess_count = 0

while guess_count < 7:
    try:
        guess = int(input(Fore.LIGHTBLUE_EX + "Enter your guess: "))
        guess_count += 1

        if guess < number:
            print(Fore.LIGHTGREEN_EX + "Your guess is too low.")
        elif guess > number:
            print(Fore.RED + "Your guess is too high.")
        else:
            print(Fore.GREEN + "🎉 Congratulations! You guessed the number in", guess_count, "attempts.")
            break
    except ValueError:
        print(Fore.RED + "❌ Invalid input! Please enter a valid number.")

else:
    print(Back.LIGHTMAGENTA_EX + Fore.BLACK + f"Sorry, you did not guess the number. The number was {number}.")
