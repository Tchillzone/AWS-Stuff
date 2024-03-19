import random

def guess_game():
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low! Try a higher number.")
        elif guess > number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You've guessed the number {number} correctly in {attempts} attempts!")
            break
    else:
        print(f"Sorry, you've run out of attempts. The number was {number}.")

if __name__ == "__main__":
    guess_game()

