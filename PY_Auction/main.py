from replit import clear
from art import logo
print(logo)
#HINT: You can call clear() to clear the output in the console.

bids = {}
bidding_finished = False

def highest_bid(record):
  high = 0
  winner =''
  for bidder in record:
    amount = record[bidder]
    if amount > high:
      high = amount
      winner = bidder
  print(f"The wiwnner is {winner} wiwth highest bid of ${high}.")
  

while not bidding_finished:
  name = input("Enter the name: \n")
  price = int(input("Enter the Bid Amount: \n"))
  bids[name] = price
  print(bids)
  cont = input("Are there any other bidders? type 'yes' or 'no'.")
  if cont == 'no':
    bidding_finished = True
    highest_bid(bids)
  elif cont == 'yes':
    clear()
  
