from time import sleep
def new_game():
  user_name = input("What is your name? ")
  print(f"Hello {user_name}, Welcome to our quiz game!")
  sleep(1)
  print("This is a quiz testing your general knowledge. There are 10 questions in total.")
  sleep(0.5)
  print("Let's get started! Please choose either option a, b, c or d")
  sleep(0.5)
  print()
  score = 0

  for question in questions:
    print(question)
    sleep(0.5)
    for options in questions[question]:
      print(f"{options}. {questions[question][options]}")
      sleep(0.5)
    answer = input("Enter your answer: ").upper()
    if answer == correct_options[question]:
      print("Correct!")
      score += 1
    else:
      print("Wrong!")
      sleep(0.5)
      print("The correct answer is: ", correct_options[question])
    sleep(0.5)
    print("Your score is: ", score)
  if score == 10:
    print("Congratulations! You got a perfect score")
  elif score > 7 and score < 10:
    print(f"Congratulations! You have passed the test with a score of {score} out of 10")
  else:
    print(f"Your final score is: {score} out of 10")

def play_again():
  response = input("Do you want to play again? (yes/no) ")
  response = response.upper()
  if response == "YES":
    return True
  else:
    return False


questions = {
  "Who wrote the play Romeo and Juliet?": {"A": "Charlie",
                                              "B": "Williams Shakespeare",
                                              "C": "Jane Austen",
                                              "D": "Mark Twain"},

  "What is the longest river in the world?": {"A": "Nile", 
                                              "B": "Amazon",
                                              "C": "Mississippi",
                                              "D": "Missouri"},

  "What is the capital of France?": {"A": "Paris",
                                      "B": "London",
                                      "C": "Rome",
                                      "D": "Madrid"},

  "What is the smallest prime number?": {"A": "2",
                                          "B": "3",
                                          "C": "5",
                                          "D": "7"},

  "What is the chemical symbol for gold?": {"A": "Go",
                                              "B": "Gd",
                                              "C": "Au",
                                              "D": "Ad"},

  "Who painted the Mona Lisa?": {"A": "Pablo Picasso",
                                  "B": "Leonardo Da Vinci",
                                  "C": "John Adams",
                                  "D": "Michelangelo"},

  "Which ocean is the largest on earth?": {"A": "Pacific",
                                              "B": "Atlantic",
                                              "C": "Indian",
                                              "D": "Arctic"},

  "What is the capital of Japan?": {"A": "Beijing",
                                      "B": "Tokyo",
                                      "C": "Delhi",
                                      "D": "Shanghai"},

  "Which element has the chemical symbol H?": {"A": "Hydrogen",
                                                  "B": "Helium",
                                                  "C": "Oxygen",
                                                  "D": "Carbon"},

  "Who created Python?": {"A": "Guido van Rossum",
                          "B": "James Gosling",
                          "C": "Steve Harvey",
                          "D": "Elon Musk"},
}

correct_options = {
  "Who wrote the play Romeo and Juliet?": "B",
  "What is the longest river in the world?": "A",
  "What is the capital of France?": "A",
  "What is the smallest prime number?": "A",
  "What is the chemical symbol for gold?": "C",
  "Who painted the Mona Lisa?": "B",
  "Which ocean is the largest on earth?": "A",
  "What is the capital of Japan?": "B",
  "Which element has the chemical symbol H?": "A",
  "Who created Python?": "A",
}

new_game()

while play_again():
  new_game()

print("Thanks for playing!")

