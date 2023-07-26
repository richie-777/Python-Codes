from art import logo
import random
print(logo)

easy =10
hard =5
turns = 0

print("Welcome to the Number Guessing Game!")
print("I'm Thinking of the Numbers between 1 and 100.")

def play():
  is_over = False
  difficulty = input("Choose the difficulty. Type 'easy' or 'hard' : ").lower()
  if difficulty == 'easy':
    turns = easy
  elif difficulty == 'hard':
    turns = hard

  n = random.randint(1,100)
  print(n)
  
  for _ in range(turns):
    while not is_over and turns > 0:  
      print(f"You have {turns} attempts to guess the Number.")
      turns-=1
      num = int(input("Make a Guess: "))
      if num == n: 
        print(f'You got it. The number is : {n}')
        is_over = True
      elif num > n: print('too high!')
      elif num < n: print('too low!')
      # print(f"You have {turns} attempts to guess the Number.")
  print("You have run out of guesses, You lose!")

def play_again():
  again = input("type 'y' to play again and 'n' to stop playing.").lower()
  if again == 'y':
    play()
    play_again()
  elif again == 'n':
    is_over = True

play()
play_again()


