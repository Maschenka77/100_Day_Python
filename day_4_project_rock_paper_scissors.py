import time
import random

print("Welcome to Rock, Paper, Scissors!")
good_luck = '''
 ____________________
/       Good         \
|                    
|        Luck!       |
\____________________/
         !  !
         !  !
         L_ !
        / _)!
       / /__L
 _____/ (____)
        (____)
 _____  (____)
      \_(____)
         !  !
         !  !
         \__/
'''

print(good_luck)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



def game():

  lost = 0
  won = 0
  draw = 0
  all = 0

  cont = "y"

  while cont == "y":
    all += 1
    hand_list = [rock, paper, scissors]

    user_input = input("Make your choice. Type 0 for rock, 1 for paper or 2 for scissors. ")
    user_input = int(user_input)
    #index generated through user_input
    user_choice = hand_list[user_input]

    print(user_choice)
    time.sleep(1.5)

    #to generate the right index
    length = len(hand_list)-1
    #generating the index for the random op. choice
    op_index = random.randint(0,length)
    op_choice = hand_list[op_index]
  
    print(op_choice)

    if user_choice == op_choice:
      print("It's a draw!")
      draw += 1
    elif user_choice == rock and op_choice == paper:
      print("You loose!")
      lost += 1
    elif user_choice == paper and op_choice == scissors:
      print("You lose!")
      lost += 1
    elif user_choice == scissors and op_choice == rock:
      print("You lose!")
      lost += 1
    else:
      print("You win!")
      won += 1

    cont = input("Do you want to play again? (y or n)")
    cont = cont.lower()
    


  if cont == "n":
    print(f"You played {all} times.")
    print(f"You had {draw} draws, lost {lost} times and won {won} times.")
    print(f"Your winning rate is {round(won/all, 2)}.")
    print("Thank you for playing. Bye bye!")
  

game()
