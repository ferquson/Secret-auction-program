from art import logo
from replit import clear
#HINT: You can call clear() to clear the output in the console.

availability_of_bidders = True
print(logo + "\n" + "Welcome to the secret auction program")
bidders_and_bids = {}

while availability_of_bidders:
  name = input("Enter your name: ")
  try:  
    bid = int(input("Enter your bid: $"))
  except ValueError:
    print("You had to enter count of money you bid")
    continue
  bidders = {}
  bidders_and_bids[name] = bid
  availability_of_other_bidders = None
  availability_of_other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.('no' is default) \n")
  
  if availability_of_other_bidders == "yes":
    availability_of_bidders = True
    clear()
  
  elif availability_of_other_bidders == "no":
    availability_of_bidders = False
    clear()
  
  else:
    availability_of_bidders = False
    clear()
    
#winner determining algorythm
bidders_list = []
bids_list = []
for bidder in bidders_and_bids:
  bidders_list.append(bidder)
  bids_list.append(bidders_and_bids[bidder])
x = {"names":bidders_list, "bids":bids_list}
winner_index = bids_list.index(max(bids_list))
print("The winner is " + bidders_list[winner_index] + " with a bid of $" + str(bids_list[winner_index]))