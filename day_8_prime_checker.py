def prime_checker(number):
  counter = 0
  for i in range(1,number+1):
    if number == 0 or number == 1:
      print(f"{number} is not a prime number.\n\n")
      return 0
    else:
      if number%i ==0:
        counter += 1
  if counter == 2:
    print(f"{number} is a prime number.\n\n")
  else:
    print(f"{number} is not a prime number.\n\n") 

again = True
while again:
  prime_checker(int(input("Which (integer) number do you want to check? ")))
  question = input("Do you want to check another number?(y/n)\n\n")
  if question == "N":
    again = False
    print("Bye bye!")



