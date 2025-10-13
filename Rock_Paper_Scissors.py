import random as ra

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
game = [rock, paper, scissors]
# Rock breaks Scissors.
# Scissors cuts Paper.
# Paper covers Rock.
print("Welcome To The Rock, Paper, Scissors game!")
# take user choice
user = int(input("Type 0 for Rock\n 1 for Paper\n 2 for Scissors\n"))
# computer choice
computer = ra.randint(0,2)

if 0 <= user <= 2:
    print(game[user])
    print("Computer choice:", game[computer])
    if user == computer:
        print("It's a draw")
    elif (user == 0 and computer == 2) or (user > computer):
        print("You win !")
    else:
        print("You lose!")
else:
    print("You enter an invalid number, You lose !")
