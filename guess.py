"""

Created on May 17, 2019
@author: Pulkit Ghai

"""

from stringDatabase import stringDatabase as db
from game import gameScore as gs

class main:
    """
This is the main class handling all the input output of the system. It has two main functions:
1. def choice  and 2. checkAplhabet
"""
    def __init__(self, word):
        self.word = word
        self.currentGuess = "----"
        self.score = gs(self.word)
        self.last_guess=''
    def currentWord(self):
        print(self.word)

    def find(self, s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]

    def checkAplhabet(self, char):
        """
        This function check if the char in the parameter is in the current word or not. If not, it record it as a Missed Letter.
        Otherwise, it will use split and combine strategy to show the used the place of the character.

        Note: self.score is the object of the game class
        :param char:
        :return:
        """
        # self.currentWord()
        check = False
        index = []
        if (len(char) == 1):
            for i in self.word:

                if i == char:
                    check = True

                    break
                else:
                    check = False
        if check == True:
            index = self.find(self.word, char)
            print("You found 1 letter")
            for i in index:
                self.currentGuess = self.currentGuess[:i] + char + self.currentGuess[i + 1:]
            print("Current word:" + self.currentGuess)
            self.choice()
        elif check == False:
            print("No Letter found")
            self.score.setMissedLetters()
            print("Current word:" + self.currentGuess)
            self.choice()

    def choice(self):
        # print(self.word)
        """
        This is the main function of the class that handles the input and output. It provides the user with options and take neccss-
        actions.
        :return:
        """
        print("g = guess, t = tell me, l for a letter, and q to quit")
        while("-" in self.currentGuess):
            inp = input("")
            if inp=='g':
                guess = input("Enter the word")
                if guess == self.word:

                    print("Guess is right!")

                    self.score.makeTup(self.currentGuess, "Success")
                    # self.score.displayScore()
                    break
                else:
                    self.score.setBadGuesses()
                    print("wrong guess")
                    self.choice()
            elif inp=='t':

                self.score.makeTup(self.currentGuess, "Gave up")
                # self.score.displayScore()

                self.currentGuess = "----"
                print("The word is:"+self.word)
                print("\nCurrent Guess:----")
                self.word = db().getWord()
                self.score.setNewEntry(self.word)
                self.currentGuess = "----"
                self.choice()

            elif inp=='l':
                alphabet = input("Enter a letter")
                self.last_guess = self.currentGuess
                self.checkAplhabet(alphabet)
            elif inp == 'q':
                self.score.displayScore()
                # exit()
                break
        if('-' not in self.currentGuess):
            self.currentGuess = "----"
            self.score.makeTup(self.last_guess, "Success")
            print("you guess it !!")
            print("\nCurrent Guess:----")
            self.word = db().getWord()
            self.score.setNewEntry(self.word)
            self.currentGuess = "----"
            self.choice()





word = db().getWord()
obj = main(word)
print("** The great guessing game **\n"+"Current Guess:----")
obj.choice()
