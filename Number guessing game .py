#multiplayer version of Game 1
import random
def game():
    t = random.randint(0, 100)
    c = 0
    while True:
        i = int(input("Enter a number between 0 and 100 - "))
        if (i < 0 or i > 100):
            print("Wrong input, try again")
            c = c + 1
        elif (i < t):
            print("Guess is too low, try again")
            c = c + 1
        elif (i > t):
            print("Guess is too high, try again")
            c = c + 1
        elif (i == t):
            print("Congratulations, you guesses the correct number")
            c = c + 1
            print("No. of attempts taken = ", c)
            return c
        else:
            print("Wrong input, try again")
            c = c + 1

while True:
    choice = int(input('''
Enter 1 for Single Player
Enter 2 for Muttiplayer
Enter 3 to Exit
'''))
    if choice == 1:
        print("Single Player mode")
        game()

    elif choice == 2:
        print("Multiplayer mode")
        print("Player 1")
        input("Enter to start")
        p1 = game()
        print("Player 2")
        input("Enter to start")
        p2 = game()
        if p1 == p2:
            print("Game tied")
        elif p1 > p2:
            print("Player 1 won")
        else:
            print("Player 2 won")

    elif choice == 3:
        print("Exiting game")
        break

    else:
        print("Invalid Input")