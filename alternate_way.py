import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0

logo = """
 _____                       _   _            _   _                 _               
|  __ \                     | | | |          | \ | |               | |              
| |  \/_   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/  \__|_| |_|\___| \_| \_/\__,_|_| |_| |_|_.__/ \___|_|
"""
print(logo)
def check_answer(guess, answer, turns):
  """Checks answer against guess and returns the number of turns left"""
  if guess > answer:
    print("Too high")
    return turns -1
  elif guess < answer:
    print("Too low.")
    return turns -1
  else:
    print(f"You got it! The answer was {answer}")
    
# make a functon to set difficulty
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
  

def game():
  # Choosing a random number from 1 to 100
  print("Welcome the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = random.randint(1, 100)
  print(f"the correct answer is {answer}")
  turns = set_difficulty()
  
  
  # Repeat the guessing functionality if they get it wrong
  guess = 0
  while guess != answer:
    # Let the user guess the number
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess:\n"))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses you lose.")
      return
    elif guess != answer:
      print("Guess again")
  # Function to check users guess against the actual answer
    
  
  # Track the number of guess and reduce it by 1 if they get it wrong

game()
