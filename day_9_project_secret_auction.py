import os


def name():
  name = input("Whats your name? ")
  return name

def bid():
  dollars = input("How much do you want to bid? $")
  return dollars

def find_min(bidders_dict):
  values = []
  #loop through dictionary
  for key, value in bidders_dict.items():
    #append values to value list to compare them
    values.append(value)
    #find current maximum of values
    max_value = max(values)
    #if current value is the same as the maximum, make key the maximum bidder
    if value == max_value:
       max_bidder = key
  print(f"Bidder {max_bidder} won with a bid of {max_value}! ")
  
bids_and_bidders = {}

again = True

while again:
  my_name = name()
  #append new entries to dict.
  bids_and_bidders[my_name] = bid()
  #print(bids_and_bidders)
  cont = input("Do you have more bids? (yes/no) ")
  os.system('clear')
  if cont == "no":
    again = False


find_min(bids_and_bidders)
