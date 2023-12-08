print("Welcome to Treasure Island!\nYour mission is to find the treasure!")
choice1 = input("You're at a cross road.\nWhere do you want to go? Type \"left\" or \"right\"\n").lower()
if choice1 == 'left':
    choice2 = input("You've come to a lake.\n"
                    "There is an island in the middle of the lake.\n"
                    "Type \"wait\" to wait for a boat.\nType \"swim\" to swim across.\n").lower()
    if choice2 == "wait":
        choice3 = input("You arrived at the island unharmed.\nThere is a house with 3 doors.\n"
                        "One white, one yellow and one black.\nWhich colour do you choose?\n").lower()
        if choice3 == "white":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "black":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")

