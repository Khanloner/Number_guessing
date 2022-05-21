import random
def guessing_fun(guess_number, attempts):
  correct = False
  for i in range(0,attempts):    
    print(f"You have {attempts - i} attempt to guess the number")
    guess = int(input("Make a guess"))
    if guess > guess_number:
      print("Too high")
      print("Try again")
    elif guess < guess_number:
      print("Too low")
      print("Try again")
    else:
      print("yes you got it correctly")
      correct = True
      break
  return correct

def easy(guess_number, attempts):
  
  win_lose = guessing_fun(guess_number, attempts)
  if win_lose == True:
    print("You guessed correctly")
  else:
    print("You were not able to guess better luck try next time")
    
def hard(guess_number, attempts):
  win_lose = guessing_fun(guess_number, attempts)
  if win_lose == True:
    print("You guessed correctly")
  else:
    print("You were not able to guess better luck try next time")

number = random.randint(1,100)
logo = """
 _____                       _   _            _   _                 _               
|  __ \                     | | | |          | \ | |               | |              
| |  \/_   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/  \__|_| |_|\___| \_| \_/\__,_|_| |_| |_|_.__/ \___|_|
"""
print(logo)
print(number)
print("Welcome to the Number Guessing Game?")
print("The number ranges from 1 to 100.")
difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard'")
level = {
"easy": easy,
"hard": hard
}
      
guess_attempt = 0
if difficulty_level == "easy":
  guess_attempt = 10
  level["easy"](number, guess_attempt)
else:
  guess_attempt = 5
  level["hard"](number, guess_attempt)