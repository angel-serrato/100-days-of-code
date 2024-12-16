import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))
random_choice = random.randint(0,2)
print("You chose:")
if user_choice == 0:
    print(f"Rock\n{rock}")
elif user_choice == 1:
    print(f"Paper\n{paper}")
elif user_choice == 2:
    print(f"Scissors\n{scissors}")
else:
    print(f"You didn't choose correctly.")
print("The computer chose:")
if random_choice == 0:
    print(f"Rock\n{rock}")
elif random_choice == 1:
    print(f"Paper\n{paper}")
else:
    print(f"Scissors\n{scissors}")
if user_choice == 0 and random_choice == 2:
    print("You win!")
elif user_choice == 1 and random_choice == 0:
    print("You win!")
elif user_choice == 2 and random_choice == 1:
    print("You win!")
elif user_choice == 0 and random_choice == 0 or user_choice == 1 and random_choice == 1 or user_choice == 2 and random_choice == 2:
    print("It's a tie!")
else:
    print("You lose!")