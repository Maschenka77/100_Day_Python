import random

"""Function which takes a players cards and computes the score of the hand. Returns score of the player or True when the score is over 21, which means that the player looses."""
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

"""Function which asks the user wether the user wants to play one more game of blackjack."""
def one_more_game():
  more = input("One more game? y/n ")
  if more == "y":
    blackjack()
  else:
    print("Bye Bye!")
    
"""Function which takes the players and the dealers score and computes if 
    it is a draw, or if the player looses or wins. The palyer is then asked
    wether he wants to play one more game."""
def who_wins(d_score, p_score):
  if d_score == p_score:
        print("It´s a draw!")
        one_more_game()
  elif d_score > p_score:
        print("The Dealer wins!")
        one_more_game()
  elif d_score < p_score and d_score >= 17:
        print("Congratulations, you win!")
        one_more_game()

"""A function which takes players/dealers hand their scores and a set of cards
    as arguments, asks the player wether he wants one more card, gives the dealer
    more cards if his score is under 17 and computes (by using the who_wins() function) the outcome of the game. """
def more_cards(p_hand,d_hand, d_score, p_score, cards):
  more = True
  #as long as more is True, the player is asked wether he wants one more card
  while more:
    answer = input("Do you want one more card? y/n ")
    if answer == "y":
      card = random.choice(cards)
      #append card to hand
      p_hand.append(card)
      p_score = compute_score(p_hand)
      print(f"\nYour card: {card}. \nYour new score is {p_score}.\n")
      #is the score over 21? The player looses
      if p_score > 21:
        print("Your score is too high, you loose!")
        print(f"\nHand of dealer: {d_hand}.\nDealer score: {d_score}.\n")
        more = False
        one_more_game()
    #if player do not want more cards
    elif answer == "n":
      more = False
      print(f"\nHand of dealer: {d_hand}.\nDealer score: {d_score}.\n")
      #check dealers score
      if d_score >= 17:
        who_wins(d_score,p_score)
      else:
        #give dealer more cards if his score is under 17
        while d_score < 17:
          print("Dealers score is under 17. Dealer needs to take one more card.")
          card = random.choice(cards)
          d_hand.append(card)
          d_score = compute_score(d_hand)
          print(f"\nDealers card: {card}. \nDealers new score is {d_score}.\n")
          #dealers score is to high
          if d_score>21:
            print("Dealers score is too high.\nCongratulations, you win!")
            one_more_game()
          else:
            who_wins(d_score, p_score)

 
"""Function the game is running in. THe card set is defined, initial hands and
   scores are computed and the more_cards() function is called."""
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

  #initial hands
  player_hand = []
  dealer_hand = []

  for i in range(0,2):
    player_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))

  #initial scores
  your_score = compute_score(player_hand)
  dealer_score = compute_score(dealer_hand)


  print(f"Your cards: {player_hand}\n")
  print(f"Your score: {your_score}\n")
  print(f"First card of dealer: {dealer_hand[0]}")
 

  more_cards(player_hand, dealer_hand, dealer_score, your_score, cards)


blackjack()

#Output could be improved, text is displayed too fast.


