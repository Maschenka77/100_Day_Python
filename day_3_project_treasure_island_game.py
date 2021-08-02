import time

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


def gameover():
  print("Game over!")

def win_the_game_or_not():
  print("You step into the room and see a big treasure in the center.")
  open = input("Do you want to open it? (yes or no) ")
  open = open.lower()
  if open == "yes":
    print('You open the chest. On its bottom lies a note. You read the note: "The greatest treasure of all is love."')
    time.sleep(6)
    print("Just kidding! The chest is full of gold and diamants. You somehow manage to take it all with you. From now on you live a glamurous and wild live!")
    car()
  elif open == "no":
    print("You decide, that you allready have everything in your live and don't need the money. It was a nice adventure but now your satisfied and go back home.")
  else:
    print("Invalid input!")
    win_the_game_or_not()


def choose_door():

  print("As you wait, suddenly three doors appear out of nowhere infront of you.")
  color = input("Do you want to go through the red, blue, or green door? ")
  color = color.lower()
  if color == "red":
    print("As you step into the room everything explodes and you burn in the fire.")
    gameover()
  elif color == "blue":
    print("You are eaten by a bunch of aggressive, gigantic wasps.")
    gameover()
  elif color == "green":
    win_the_game_or_not()
    

def way_to_treasure():
  
  print("You follow the path, which lies ahead you.")
  print("Then you reach a fork in the road.")
  direction = input("Do you want to go left or right? ")
  direction = direction.lower()
  if direction == "right":
    print("Oh no, you fell into a hole.")
    gameover()
  elif direction == "left":
    action = input("Do you want to swim or wait? ")
    action = action.lower()
    if action == "swim":
      print("You where attacked by a huge monster, which was lurking under the water.")
      gameover()
    elif action == "wait":
      choose_door()
    else:
      print("Invalid input!")
      way_to_treasure()
  else:
    print("Invalid input!")
    way_to_treasure()



def car():
  print('''
                              _.-="_-         _
                         _.-="   _-          | ||"""""""---._______     __..
             ___.===""""-.______-,,,,,,,,,,,,`-''----" """""       """""  __'
      __.--""     __        ,'                   o \           __        [__|
 __-""=======.--""  ""--.=================================.--""  ""--.=======:
]       [w] : /        \ : |========================|    : /        \ :  [w] :
V___________:|          |: |========================|    :|          |:   _-"
 V__________: \        / :_|=======================/_____: \        / :__-"
 -----------'  "-____-"  `-------------------------------'  "-____-"
''')

way_to_treasure()
