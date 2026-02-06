import random

def rock_paper_scissors():

    user_input = int(input("Choose (0) for Rock, (1) for Paper or (2) for Scissors: "))
    computer_input = random.randint(0, 2)

    if user_input < 0 or user_input > 2:
        print("That is not a choice.")
        return

    if user_input == 0 and computer_input == 2:
        print("You chose Rock and Computer chose Scissors: YOU WIN!")
    elif user_input == 1 and computer_input == 0:
        print("You chose Paper and Computer chose Rock: YOU WIN!")
    elif user_input == 2 and computer_input == 1:
        print("You chose Scissors and Computer chose Paper: YOU WIN!")
    elif computer_input == 0 and user_input == 2:
        print("You chose Scissors and Computer chose Rock: YOU LOSE!")
    elif computer_input == 1 and user_input == 0:
        print("You chose Rock and Computer chose Paper: YOU LOSE!")
    elif computer_input == 2 and user_input == 1:
        print("You chose Paper and Computer chose Scissors: YOU LOSE!")
    else:
        print("Its a Tie!")

playing = True

while playing:

    rock_paper_scissors()

    play_again = input("\nWant to play again? (Y) or (N): ").lower()

    if play_again == "y":
        playing = True
    else:
        print("\nThanks for Playing!")
        playing = False