#multiplayer version of Game 1
import random
def game(k):
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
            print("Game over for player ",k)
            c = c + 1
            print("No. of attempts taken = ", c)
            return c
            break;
        else:
            print("Wrong input, try again")
            c = c + 1
print("Player 1")
input("Enter to start")
p1=game(1)
print("Player 2")
input("Enter to start")
p2=game(2)
if(p1<p2):
    print("Player 1 won")
elif(p2>p1):
    print("Player 2 won")
else:
    print("Game tied")