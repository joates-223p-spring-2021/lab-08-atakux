
# -*- coding: utf-8 -*-
"""
Angela DeLeo
CPSC 223P-01
Tue Apr 05, 2022
atakux707@csu.fullerton.edu
"""

import random


# Hangman class.
class Hangman:
    
    def __init__(self, word, triesAllowed):
        #constructor
        self.word = word
        self.triesAllowed = triesAllowed

        #empty lists for usedLetters and correctLetters
        self.usedLetters = []
        self.correctLetters = []


    def Guess(self, letter):
        """Pass in a letter (length = 1) and check to see if it is in the word.
            If it is, replace blanks in display word with letter and return True
            If not, decrement the number of tries left and return False
        """
        if letter in self.word:
            if letter in self.usedLetters:
                return True
            else:
                self.usedLetters.append(letter)
                self.correctLetters.append(letter)
            return True

        else:
            if letter in self.usedLetters:
                return False
            else:
                self.triesAllowed -= 1
                self.usedLetters.append(letter)
            return False


    def GetNumTriesLeft(self):
        """Return the number of tries left"""
        return self.triesAllowed
    

    def GetDisplayWord(self):
        """Return the display word (with dashes where letters have not been guessed)
        i.e. the word happy with only the letter 'p' guessed so far would be '--pp-'"""
        dashed = '-'*len(self.word)
        
        for i in range(len(self.word)):
            if self.word[i] in self.correctLetters:
                dashed = dashed[ : i] + self.word[i] + dashed[i + 1 : ] 
        return dashed
    

    def GetLettersUsed(self):
        """Return a string with the list of letters that have been used"""
        used=''
        
        for l in self.usedLetters:
            used += l + '-'

        return used


    def GetGameResult(self):
        """Return True if all letters have been guessed. False otherwise"""
        dashes = self.GetDisplayWord()

        if '-' in dashes:
            return False
        else:
            return True


    def DrawGallows(self):
        """Optional: Return string representing state of gallows"""
        if self.triesAllowed >= 8:
            print("-----|\n |\n | \n | \n | \n | \n | \n |\n---")
        elif self.triesAllowed == 7:
            print("-----|\n |   |\n | \n | \n | \n | \n | \n |\n---")
        elif self.triesAllowed == 6:
            print("-----|\n |   |\n |   0\n | \n | \n | \n | \n |\n---")
        elif self.triesAllowed == 5:
            print("-----|\n |   |\n |   0\n |  /\n | \n | \n | \n |\n---")
        elif self.triesAllowed == 4:
            print("-----|\n |   |\n |   0\n |  /|\n | \n | \n | \n |\n---")
        elif self.triesAllowed == 3:
            print("-----|\n |   |\n |   0\n |  /|\\\n | \n | \n | \n |\n---")
        elif self.triesAllowed == 2:
            print("-----|\n |   |\n |   0\n |  /|\\\n |   U\n | \n | \n |\n---")
        elif self.triesAllowed == 1:
            print("-----|\n |   |\n |   0\n |  /|\\\n |   U\n |  /\n | \n |\n---")
        else:
            return


# implement the logic of your game below
if __name__=="__main__":
    # Read all the words from the hangman_words.txt file
    wordFile = open("hangman_words.txt", "r")
    wordFileText = wordFile.read()
    wordFile.close()

    playing = True    


    # Seed the random number generator with current system time
    random.seed()
    
    # Convert the string of words in wordFile to a list,
    # then get a random word using
    wordsList = list(wordFileText.split())
    randIndex = random.randint(0, len(wordsList))

    word = wordsList[randIndex]
    
    #set the amount of guesses the player gets
    if len(word) >= 8:
        tries = len(word)
    else:
        tries = 8



    # Instantiate a game using the Hangman class
    game = Hangman(word, tries)

    # Use a while loop to play the game
    while playing:
        tries = game.GetNumTriesLeft()
        game.DrawGallows()


        if tries == 0 and gameResult == False:
            print(f"You lost. The word was {word}")
            print("-----|\n |   |\n |   0\n |  /|\\\n |   U\n |  / \\\n | \n |\n---")
            print("\nThis time I win!")

            playing = False


        elif tries != 0:    
            print("Here's your word so far:", game.GetDisplayWord())
            print(f"You have {tries} guesses left\n")

            playerGuess = input("Guess a letter: ").lower()


            if len(playerGuess) > 1:
                print("Input only 1 letter please.")
            else:
                guessResult = game.Guess(playerGuess)
                gameResult = game.GetGameResult()


            if guessResult == True:
                print("Good guess! Letters used:", game.GetLettersUsed())
            else:
                print("Too bad! Letters used:", game.GetLettersUsed())


            if gameResult == True:
                print(f"Congratulations! You won!! The word was {word}")
                print("-----|\n |    \n |    \n |     \n |   0\n |  \\|/\n |   U\n |  / \\\n---")
                playing = False
            else:
                continue
