import random
import time

def heads_tails():
  answer = "yes"
  while answer == "yes":
    coin = random.randint(0,1)
    print("Heads or Tails?")
    time.sleep(3)
    if coin == 0:
      print("Heads")
    elif coin == 1:
      print("Tails")
    answer = input("Do you want to flip the coin again? ")
    answer = answer.lower()

heads_tails()
    










