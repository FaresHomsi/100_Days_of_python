import random
from art import logo


def random_number():
  """Returns a random number to guess"""
  rand_num = random.randint(1, 100)
  return rand_num


def easy_mode():
  is_game_over = False
  attempts = 10
  
  while not is_game_over:
    print(f"you have {attempts} attempts remaining to guess the number. ")
    user_guess = int(input("Make a guess: "))
  
    if attempts == 1:
        is_game_over = True
        print("You`ve run out of guesses, You Lose.")
      
    elif user_guess > rand_num:
      attempts -= 1
      print ("Too high. \nGuess again.")
      
    elif user_guess < rand_num:
      attempts -= 1
      print ("Too low. \nGuess again.")

    elif user_guess == rand_num:
      is_game_over = True
      print (f"You got it! The answer was {user_guess}")



def hard_mode():
  is_game_over = False
  attempts = 5
  
  while not is_game_over:
    print(f"you have {attempts} attempts remaining to guess the number. ")
    user_guess = int(input("Make a guess: "))
    
    if attempts == 1:
      is_game_over = True
      print("You`ve run out of guesses, You Lose.")
      
    elif user_guess > rand_num:
      attempts -= 1
      print ("Too high. \nGuess again.")

    elif user_guess < rand_num:
      attempts -= 1
      print ("Too low. \nGuess again.")

    elif user_guess == rand_num:
      is_game_over = True
      print (f"You got it! The answer was {user_guess}")



print(logo)

print("Welcome to the Number Guessing Game! \nI`m Thinking of a number between 1 and 100.")

rand_num = random_number()

difficulty_level = input("Choose difficulty. Type 'easy' or 'hard': \n")

if difficulty_level == "easy":
  easy_mode()

elif difficulty_level == "hard":
  hard_mode()



      
      
      
      
    
    
    
 

  

