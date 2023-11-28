import random
print("Welcome to rock, paper, scissors. Good luck!")
user_choice = int(input("Enter your choice ( 0 for rock, 1 for paper, or 2 for scissors): "))
computer_choice = random.randint(0,2)
print(f"computer chose {computer_choice}")

if computer_choice == user_choice:
  print("its a tie")
elif user_choice >= 3:
  print("Invalid choice")
elif computer_choice == 2 and user_choice == 0:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose!")
elif user_choice > computer_choice:
  print("You win!")
else:
  print("You lose!")