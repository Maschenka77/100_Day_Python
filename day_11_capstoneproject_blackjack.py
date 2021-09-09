import random

"""Function which takes a players cards and computes the score of the hand. Returns score of the player or True when the score is over 21, shich means that the player looses."""
def compute_score(hand):
  score = 0
  for card in hand:
    if card in ['J','Q','K']:
      score = score + 10
      #two cases for ace
    elif card == 'A':
      if score <11:
        score = score + 11
      else:
        score = score + 1
    elif score > 21:
      return True
    else: 
      score = score + card
  return score

def blackjack():
  
  cards = [2,
           3,
           4,
           5,
           6,
           7,
           8,
           9,
           10,
           'J',
           'Q',
           'K',
           'A']

  player_name = input("Welcome to Blackjack! Whats your name? ")
  print(f"\nHello {player_name}!")

  player_hand = []
  dealer_hand = []

  for i in range(0,2):
    player_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))

  your_score = compute_score(player_hand)
  dealer_score = compute_score(dealer_hand)


  print(f"Your cards: {player_hand}\n")
  print(f"Your score: {your_score}\n")
  print(f"First card of dealer: {dealer_hand[0]}")
  #more = input("\nDo you want one more card?(y or n) ")
  #if more == 'y':
   # player_hand.append(random.choice(list(cards.keys())))
 # else:
    # print(f"Cards of Dealer: {dealer_hand}\n")
    # print(f"Dealer score: {dealer_score}\n")


blackjack()


