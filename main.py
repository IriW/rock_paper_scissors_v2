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
imgs = [rock, paper, scissors]

comp_choice = random.randint(0, 2)
usr_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if usr_choice < 0 or usr_choice >=3:
    print("You provided wrong value. Bye")
elif usr_choice >= 0 or usr_choice <=2:
    print(f"You chose: {imgs[usr_choice]}\nComputer chose: {imgs[comp_choice]}")
    choices_matrix = [["It's a draw.", "You lose!", "You win!"],["You win", "It's a draw.", "You lost"],["You lost", "You win", "It's a draw"]]
    print(choices_matrix[usr_choice][comp_choice])
else:
    print("How did you even get here?")