import random


#Functions which specifies the letter randomly
def random_index_letters(letters_number):

  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

  #Generate letters-string
  letters_string = ""
  #Depending on how many letters the user wants to have in the password
  #a String from the letters array is choosen randomly
  for i in range(1,letters_number+1):
   letters_string = letters_string+letters[random.randint(0,len(letters)-1)] + " "
  
  return letters_string

#Functions which specifies the number randomly
def random_index_numbers(num_number):

 numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

 #Generate numbers-string
 num_string = ""
 #Depending on how many numbers the user wants to have in the password
 #a String from the numbers array is choosen randomly
 for i in range(1,num_number+1):
   num_string = num_string+numbers[random.randint(0,len(numbers)-1)] + " "
  
 return num_string


#Functions which specifies the symbol randomly
def random_index_symbols(sym_number):

 symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

 #Generate symbol-string
 sym_string = ""
 #Depending on how many symbols the user wants to have in the password
 #a String from the symbols array is choosen randomly
 for i in range(1,sym_number+1):
   sym_string = sym_string+symbols[random.randint(0,len(symbols)-1)] + " "
  
 return sym_string


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Generate string from letters, numbers, symbols
pass_string_ordered = random_index_letters(nr_letters) + random_index_numbers(nr_numbers) + random_index_symbols(nr_symbols)

#Generate an array from string
pass_string_ordered = pass_string_ordered.split()


#Generate random password from pass_string_ordered
#The index is a random int in the range of pass_string_ordered
#When a character has been used it is deleted from the string array pass_string
#_ordered because every character, which was generated randomly before, should be
#used once in the final random password

pass_string_random = ""
for i in range(0, len(pass_string_ordered)):
  index = random.randint(0,len(pass_string_ordered)-1)
  pass_string_random = pass_string_random + pass_string_ordered[index]
  del pass_string_ordered[index]

print("Your password is: " + pass_string_random)

