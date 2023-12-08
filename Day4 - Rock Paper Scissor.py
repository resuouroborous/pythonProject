import random


def play_game():
    user_choice = input("Enter your choice (rock/paper/scissors): ")
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"You chose {user_choice}, computer chose {computer_choice}.")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        print("You won!")
    else:
        print("Computer won!")


while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break


play_game()