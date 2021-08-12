def encrypt(text_to_encode, shift_num):
  #list which contains the encoded letters
  cipher_text = []
  for letter in text_to_encode:
    #if the char is not a space char, the letter can be encrypt
    if letter in alphabet:
      #get the index of the letter in alphabet list
      index = alphabet.index(letter)
      #compute a new shift number with modulo 26, important for shift-numbers, which #exeed 26
      new_shift_num = shift_num%26
      #compute the new index for the encrypted letter
      new_index = (index + new_shift_num)-26
      #save new letter and append it to the cipher_text list
      new_letter = alphabet[new_index]
      cipher_text.append(new_letter)
    else:
      cipher_text.append(letter)

   #generate a string from the list and print it to the user
  cipher_text = ''.join(cipher_text)
  print(f"The encoded text is: {cipher_text}")



def decrypt(text_to_decode, shift_num):
  #list which contains the decoded letters
  decoded_text = []
  for letter in text_to_decode:
    #if the char is not a space char, the letter can be decoded
    if letter in alphabet:
      #get the index of the letter in alphabet list
      index = alphabet.index(letter)
      #compute a new shift number with modulo 26, important for shift-numbers, which #exeed 26
      new_shift_num = shift_num%26
      #compute the new index for the decoded letter
      new_index = (index - new_shift_num)
      #save new letter and append it to the decoded_text list
      new_letter = alphabet[new_index]
      decoded_text.append(new_letter)
    else:
      decoded_text.append(letter)
  
  #generate a string from the list and print it to the user
  decoded_text = ''.join(decoded_text)
  print(f"The encoded text is: {decoded_text}")


def decode_encode():
  
  again = True
  while again == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction.lower() == 'encode':
      encrypt(text, shift)

    if direction.lower() == 'decode':
      decrypt(text, shift)

    ask_user =input("Do you want to encode or decode another message? (y/n) ")
    print("\n\n")
    if ask_user == 'n':
      again = False
      print("Bye bye!")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

decode_encode()



