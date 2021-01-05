from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0
# Function to check user's guess against actual answer. 
def check_answer(guess, answer, turns):
  """ Checks answer against guess. Returns the number of turns remaining. """
  if guess > answer:
    print("Too High")
    return turns - 1
  elif guess < answer:
    print("Too Low")
    return turns - 1
  else:
    print(f"You guessed it correctly! The answer is {answer}.")

# Function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  # Choosing a random number between 1 and 100
  print("Welcome to the Number Guessing Game!")
  print("I'm guessing of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer} ")

  turns = set_difficulty()
  

  # Repeat the guessing functionality if they get it wrong
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    # Let the user guess a number
    guess = int(input("Make a guess: "))
   
    # Track the number of returns and reduce by 1 if guesser guesses wrong
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you have lost.")
      return
    elif guess != answer:
      print("Guess again")

game()
