import random

def choose_word():
    # Choose random word from wordlist
    chosen_word = random.choice(wordlist)
    # generate array of chars
    chosen_word_list = list(chosen_word)
    return chosen_word_list

# Let the user guess a letter
def guess():
    user_guess = input("Please choose a letter: ").lower()
    return user_guess


def game_logic(word):
    # ASCII Art

    winner = '''
    /                    \
    |     Aou are a      |
    |     winner!         |
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
    stages = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']

    # Hangman stages are the player lives
    chosen_word_list = choose_word()
    player_lives = 6
    word_length = len(chosen_word_list)

    # List with blanks
    display = []

    # Generate blanks
    for i in range(word_length):
        display.append("_")

    # print(chosen_word_list)

    # This variable is needed to specifiy if the game came to an end
    not_finished = True

    while not_finished:
        char_guessed = guess()


        # Check if the letter was guessed right and create an array of positions with true/false
        positions = []
        for letter in chosen_word_list:
            is_in_word = False
            if letter == char_guessed:
                is_in_word = True
            positions.append(is_in_word)

        # This variable is needed if the user guesses a wrong word. Than it becomes False and the programm knows
        # that the guessed letter is not in the chosen word
        true_not_in_positions = True
        if True in positions:
            true_not_in_positions = False

        # Reveal letter on the  right position
        for i in positions:
            if i:
                index = positions.index(i)
                display[index] = char_guessed
                # The True position has to become False because index() always looks for the first occurrence of an
                # Element
                positions[index] = False
                print(display)
        # When there aren't any blanks left in display, the player guessed the whole word and won the game
        if "_" not in display:
            not_finished = False
            print("You won!")
            print(winner)
        # if true is not in positions player lives go down, if they reach zero the game is over and the
        # player has lost the game
        if true_not_in_positions:
            print(stages[player_lives - 1])
            player_lives -= 1
            if player_lives == 0:
                not_finished = False
                print("You lose!")

    again = input("Do you want to play again? (Y/N)")
    if again == "Y":
        game_logic(choose_word())
    else:
        print('Bye Bye!')




# generate array of words from text files
wordlist = list()
file = open("day_7_wordlist.txt", "r")
for line in file:
    line = line.strip()
    wordlist.append(line)
file.close()


game_logic(choose_word())


