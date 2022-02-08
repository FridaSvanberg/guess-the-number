#Number Guessing Game Objectives:
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
  """Compares the guess to the awnser, and returns the amount of turns that are left."""
  if guess < answer:
    print("too low")
    return turns - 1
  elif guess > answer:
    print("too high")
    return turns - 1
  else:
    print(f"Correct! It was {answer}.\nYou win!")

def set_difficulty():
  """Uses an input to get what difficulty level"""
  level = input("How do you wanna play?\nChoose between 'easy' and 'hard: ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  elif level == "hard":
    return HARD_LEVEL_TURNS


def game():
  print("Guess between 10 and 100")
  # answer = randint(1, 100)
  answer = 37
  turns = set_difficulty()

  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts.")
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("you lose")
      return

game()