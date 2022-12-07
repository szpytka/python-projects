import os
import random
from game_data import data
from art import logo, vs


def game():
  ingame = True
  option_one = {}
  option_two = {}
  option_one = a_data
  option_two = b_data
  score = score_data
  while ingame:
    os.system('cls')
    print(logo)
    print(
      f"Compare A: {option_one['name']}, a {option_one['description']}, from {option_one['country']}"
    )
    aFollowers = option_one['follower_count']
    print(vs)
    print(
      f"Against B: {option_two['name']}, a {option_two['description']}, from {option_two['country']}"
    )
    bFollowers = option_two['follower_count']
    who = (input("Who has more followers? Type 'A' or 'B': ")).lower()
    chosen = False
    while not chosen:
      if who == 'a':
        guess = aFollowers
        chosen = True
      elif who == 'b':
        guess = bFollowers
        chosen = True
      else:
        who = (input("Type 'A' or 'B': ")).lower()
    if guess > bFollowers:
      option_two = random.choice(data)
      score = score + 1
    elif guess > aFollowers:
      option_one = option_two
      option_two = random.choice(data)
      score = score + 1
    else:
      os.system('cls')
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      ingame = False
    


game_start = True
while game_start:
  a_data = random.choice(data)
  b_data = random.choice(data)
  score_data = 0
  game()
  again = input("Do you want to play again? Type 'y' or 'n': ")
  if again == 'n':
    game_start = False
