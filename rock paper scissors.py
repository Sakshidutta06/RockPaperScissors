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
fig = [rock, paper, scissors]


choicee = int(input("enter 0 for rock 1 for paper 2 for scissoors = "))
print(" ")
print("Your choice")
print(fig[choicee])
ran = random.choice(fig)
print("computers choice")
print(ran)

if choicee == 0:

    if ran == rock:
        print("its a tie")
    elif ran == paper:
        print("you lost the game")
    elif ran == scissors:
        print("you won")

elif choicee == 1:

    if ran == rock:
        print("You won")
    elif ran == paper:
        print("Its a tie")
    elif ran == scissors:
        print("you lost the game")

elif choicee == 2:

    if ran == rock:
        print("you lost the game")
    elif ran == paper:
        print("You won")
    elif ran == scissors:
        print("its a tie")
