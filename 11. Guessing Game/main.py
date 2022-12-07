import os
import random
from art import logo


def generate_number():
  number = []
  for n in range(1, 101):
    number.append(n)
  return random.choice(number)


def difficulty():
  os.system('cls')
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  print(f"Psst, the correct answer is {random_number}")
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  return level


def game(level):
  level_chosen = False
  while not level_chosen:
    if level == "easy":
      life = 10
      level_chosen = True
    elif level == "hard":
      life = 5
      level_chosen = True
    else:
      level = input("Choose a correct difficulty: ")
  end_of_game = False
  while not end_of_game:
    if life > 0:
      print(f"You've {life} attempts remaining to guess the number.")
      guess = int(input("Make a guess: "))
      if random_number == guess:
        print(f"You got it! The answer was {random_number}")
        end_of_game = True
      elif random_number > guess:
        print("Too low.")
        life -= 1
        if life > 0:
          print("Guess again.")
      elif random_number < guess:
        print("Too high.")
        life -= 1
        if life > 0:
          print("Guess again.")
    else:
      end_of_game = True
      print("You've run out of guesses, you lose.")


again = "y"
while again == "y":
  random_number = generate_number()
  game(difficulty())
  again = input(
    "Do you want to guess a number again? Type 'y' to play again or 'n' to stop: "
  )
