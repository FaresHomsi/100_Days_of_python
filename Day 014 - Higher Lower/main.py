import random
import art 
from game_data import data
from replit import clear 

def format_data(choice):
  """Takes the account data and returns the printable format."""
  choice_name = choice['name']
  choice_descr = choice['description']
  choice_country = choice['country']
  return f"{choice_name}, a {choice_descr}, from {choice_country}."


def check_answer(guess, a_followers, b_followers):
  """Take the user guess and followers counts and returns if they got it right. """
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
    
# Display art
print(art.logo)
game_should_continue = True
score = 0
choice_b = random.choice(data)

# Make the game repeatable 
while game_should_continue:
  # Generate a random account from the game data.
  choice_a = choice_b
  choice_b = random.choice(data)
  while choice_a == choice_b:
    choice_b = random.choice(data)
  
  print(f"Compare A: {format_data(choice_a)}")
  print(art.vs)
  print(f"Against B: {format_data(choice_b)}")
  
  
  # Ask user for a guess 
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  # Check if user is correct 
  ## Get follower count of each account 
  choice_a_followers = choice_a['follower_count']
  choice_b_followers = choice_b['follower_count']
  is_correct = check_answer(guess, choice_a_followers, choice_b_followers)

  clear()
  print(art.logo)
  # Give user feedback on thier guess 
  # Score keeping 
  if  is_correct:
    score += 1
    print(f"You`re Right! Current Score: {score}.")
  else:
    game_should_continue = False
    print(f"Sorry, That`s Wrong. Final Score: {score}.")
