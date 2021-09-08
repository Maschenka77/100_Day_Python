import random

cards = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']

def to_much(hand):
  points = sum(hand)
  if points > 21:
    return True
  else:
    return False

def blackjack():

  cards = {2:2,
           3:3,
           4:4,
           5:5,
           6:6,
           7:7,
           8:8,
           9:9,
           10:10,
           'J':10,
           'Q':10,
           'K':10,
           'A':11}

  player_name = input("Welcome to Blackjack! Whats your name? ")
  print(f"\nHello {player_name}!")

  player_hand = []
  dealer_hand = []

  for i in range(0,2):
    player_hand.append(random.choice(list(cards.keys())))
    dealer_hand.append(random.choice(list(cards.keys())))

  your_score = 0

  print(f"Your cards: {player_hand}\n")
  #print(f"Your score: your_score}\n")
  print(f"First card of dealer: {dealer_hand[0]}")


blackjack()


