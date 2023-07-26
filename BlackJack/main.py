import random 
from replit import clear
import art 
# game_over = False

def deal_card():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards)==21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score , computer_score):
  if user_score == computer_score:
    return "draw!"
  elif computer_score == 0:
    return "Lose, opponent has Blakjack"
  elif user_score == 0:
    return "Win with a blakjack"
  elif user_score > 21:
    return "you went over, You lose"
  elif computer_score > 21:
    return "opponent went over, You win"
  elif user_score > computer_score:
    return "you Won"
  else:
    return "You Lose"
  
def play_game():
  print(art.logo)
  user_cards = []
  computer_cards = []
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  game_over = False
  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"{user_cards} and {user_score}")
    print(f"{computer_cards} and {computer_score}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card and 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        game_over = True
  
  while computer_score != 0 and computer_score <17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f" your final hand: {user_cards}, final score is: {user_score}.")
  print(f" computer's final hand: {computer_cards}, final score is: {computer_score}.")
  print(compare(user_score, computer_score))

play_game()
while input("Do you want to play BlackJack again? typr 'y' for yes and 'n' for no: ") == 'y':
  clear()
  play_game()
