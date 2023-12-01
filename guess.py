import random
secret_number = random.randint(1,100)
while True:
    print("I'm thinking of a number between 1 and 99")
    number = int(input("Try to guess the number: "))
    if number == secret_number:
        print(f"Congratulations. You guessed right! The number is {secret_number}.")
        break
    elif number < secret_number:
        print("You guessed too low, try again!")
    elif number > secret_number:
        print("You guessed too high, try again!")
    