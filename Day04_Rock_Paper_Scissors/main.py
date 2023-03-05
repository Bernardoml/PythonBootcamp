import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer = random.randint(0, 2)

if ((player != 1) and (player != 2) and (player != 3)):
    print("Wrong choice. Game Over.")
else:
    print(choice[player])
    
print(f"Computer chose:\n{choice[computer]}")
    
if (computer == player):
    print("You tied.")
elif (computer == 2):
    if player == 1:
        print("You lost.")
    else:
        print("You won.")
elif (computer == 1):
    if player == 0:
        print("You lost.")
    else:
        print("You won.")
elif (computer == 0):
    if player == 2:
        print("You lost.")
    else:
        print("You won.")