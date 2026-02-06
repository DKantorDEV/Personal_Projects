import random

def get_valid_guess():
    """Handles input and ensures it is a valid integer"""
    while True:
        try:
            guess = int(input("What is your guess?: "))
            if 1 <= guess <= 100:
                return guess
            print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input! Please enter a whole number in the range!")

# ---------------------------------------------------------------------------------------------------------------------

def play_round():
    """Contains the logic for a single round of the game"""
    computer_number = random.randint(1, 100)
    count = 0

    while True:
        guess = get_valid_guess()
        count += 1

        if guess < computer_number:
            print("Too Low!")
        elif guess > computer_number:
            print("Too High!")
        else:
            print(f"\nCorrect! It took you {count} guesses.")
            break

# ---------------------------------------------------------------------------------------------------------------------

def main():
    """Main menu and game loop"""
    print("\nWelcome to the Higher or Lower Game!")

    while True:
        play_round()

        again = input("\nPlay Again? (Y) or (N): ").lower().strip()
        if again != "y":
            print("\nThanks for playing!")
            break

# ---------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------------------------------------------------------