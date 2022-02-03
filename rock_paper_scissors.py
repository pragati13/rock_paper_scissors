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

import random

user=0
computer=0

run = 0
flag = True

while(flag):
  choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

  print(choice)

  if choice == 0:
    print(rock);
  elif choice == 1:
    print(paper)
  elif choice == 2:
    print(scissors)
  else:
    print("Please input a valid number.")

  computer_choice = random.randint(0,2)
  print("Computer chose:")
  if computer_choice == 0:
    print(rock);
  elif computer_choice == 1:
    print(paper)
  else:
    print(scissors)

  if choice == 0 and computer_choice == 2:
    print("You win")
    user += 1
  elif choice == 1 and computer_choice == 0:
    print("You win")
    user += 1
  elif choice == 2 and computer_choice == 1:
    print("You win")
    user += 1
  elif computer_choice == 0 and choice == 2:
    print("You lose")
    computer += 1
  elif computer_choice == 1 and choice == 0:
    print("You lose")
    computer += 1
  elif computer_choice == 2 and choice == 1:
    print("You lose")
    computer+=1
  else:
    print("Draw")
  
  if user == 5:
    print("You won the game.")
    flag = False
  elif  computer == 5:
    print("Computer wins")
    flag = False
  else:
    print("Please continue...")