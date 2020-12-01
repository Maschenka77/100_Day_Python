print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

def love_calc(first_name, second_name):
  true = "true"
  love = "love"

  first_name = first_name.lower()
  second_name = second_name.lower()

  both_names = first_name + second_name

  #print(both_names)

  count_true = 0
  count_love = 0
  letter_list = []

  for i in both_names:
    
    if i in true and i not in letter_list:
      #print(f"i:{i}")
      plus_true = both_names.count(i)
      #print(f"plus_true: {plus_true}")
      count_true += plus_true
      #print(f"count_true: {count_true}")
    
    if i in love and i not in letter_list:
      plus_love = both_names.count(i)
      #print(f"plus_love: {plus_love}")
      count_love += plus_love
      #print(f"count_love: {count_love}")

    letter_list.append(i)

  love_score = str(count_true)+str(count_love)
  #print(f"love_score string: {love_score}")
  love_score = int(love_score)
  #print(f"love_score: {love_score}")

  if love_score <= 10 or love_score >= 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.\n")
  elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.\n")
  else:
    print(f"Your score is {love_score}.\n")


love_calc(name1, name2)
