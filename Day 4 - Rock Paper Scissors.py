
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
images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 0 and user_choice <= 2:
    print(images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("Yay! You win!")
elif computer_choice == 0 and user_choice == 2:
    print("Oh no! You lose!")
elif computer_choice > user_choice:
    print("Oh no! You lose!")
elif user_choice > computer_choice:
    print("Yay! You win!")
elif computer_choice == user_choice:
    print("Oops! It's a draw!")