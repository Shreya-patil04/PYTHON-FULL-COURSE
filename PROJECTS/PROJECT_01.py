
'''
We all have played snake, water and gun game in our childhood. 
If you haven't, google the rules of this game. 
Write a python program capable of playing this game with the user.
'''
import random

# Function to determine the winner
def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True  
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True  

# Computer's turn
print("Comp turn: Snake(s), Water(w), or Gun(g)?")
randNo = random.randint(1, 3)

if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
else:
    comp = 'g'

# Player's turn
you = input("Your turn: Snake(s), Water(w), or Gun(g)? ").strip().lower()

# Determine the result
a = gameWin(comp, you)

print(f"\nComputer chose: {comp}")
print(f"You chose: {you}")

if a is None:
    print("The game is a tie!")
elif a:
    print("You win!")
else:
    print("You lose!")