'''
Main hangman game.
'''

from string import ascii_lowercase
from choose_word_for_game import choose_word


def get_length_of_word():
    # This function ask player how many letters should the word that he is going to guess consist.
    while True:
        wordLength = input(
            'How many minimum letters should the word consist of?(not more than 12)')
        try:
            wordLength = int(wordLength)
            if 1 <= wordLength <= 12:
                return wordLength
            else:
                print("That is not between 1 and 12.")
        except ValueError:
            print("You can use only numbers")


def get_number_of_attempts():
    # Get user-inputted number of incorrect attempts for the game.
    while True:
        numberOfAttempts = input(
            'How many incorrect tries do you need? (between 1 and 20): ')
        try:
            numberOfAttempts = int(numberOfAttempts)
            if 1 <= numberOfAttempts <= 20:
                return numberOfAttempts
            else:
                print('{0} is not between 1 and 20'.format(numberOfAttempts))
        except ValueError:
            print('{0} is not an integer'.format(
                numberOfAttempts))


# Function that shows actual state of word.

def display_word(word, wordLetters):
    # display letter if it is in wordLetters list as True if not display '*'
    displayedWord = ''.join(
        [letter
         if wordLetters[i]else '*' for i,
         letter in enumerate(word)])
    return displayedWord


def get_next_letter(guessedLetters):
    # Ask player which letter he/she wants to check next.
    while True:
        nextLetter = input("Choose the next letter: ").lower()
        if len(nextLetter) != 1:
            print('You can write only one character at time')
        elif nextLetter not in ascii_lowercase:
            print('You can use only letters')
        elif nextLetter in guessedLetters:
            print('That letter was guessed before')
        else:
            guessedLetters.append(nextLetter)
            return nextLetter


def play_hangman():
    # Set all variables needed in game.
    numberOfAttempts = get_number_of_attempts()
    word = choose_word(get_length_of_word())
    wordLetters = [letter not in ascii_lowercase for letter in word]
    guessedLetters = []
    wordGuessed = False

   # Main loop for game.
    while numberOfAttempts > 0 and not wordGuessed:

        print('Word: {0}'.format(display_word(word, wordLetters)))
        print('You have {0} attempts remaining.'.format(numberOfAttempts))

        nextLetter = get_next_letter(guessedLetters)

        if nextLetter in word:
            print('{0} is in the word'.format(nextLetter))

            for i in range(len(word)):
                if word[i] == nextLetter:
                    wordLetters[i] = True
        else:
            print('{0} is not in the word.'.format(nextLetter))
            numberOfAttempts -= 1

        # Check if word is solved or not if list is full of True word is solved.
        if False not in wordLetters:
            wordGuessed = True
    if wordGuessed:
        print('Congratulations! You won!')
    else:
        print('You lost, your word is:', word)


play_hangman()
