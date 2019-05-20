from stringDatabase import stringDatabase as db
from game import gameScore as gs

class main:

    def __init__(self, word):
        self.word = word
        self.currentGuess = "----"
        self.score = gs(self.word)

    def currentWord(self):
        print(self.word)

    def find(self, s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]

    def checkAplhabet(self, char):
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
            self.choice()

    def choice(self):
        # print(self.word)
        print("g = guess, t = tell me, l for a letter, and q to quit")
        while( "-" in self.currentGuess):
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
                self.currentGuess = self.word
                self.score.makeTup(self.currentGuess, "Gave up")
                # self.score.displayScore()

                self.currentGuess = "----"
                print("The word is:"+self.word)
                print("\nCurrent Guess:----")
                break
            elif inp=='l':
                alphabet = input("Enter a letter")
                self.checkAplhabet(alphabet)
            elif inp == 'q':
                self.score.displayScore()
                exit()
        if('-' not in self.currentGuess):
            self.score.makeTup(self.currentGuess, "Success")


        self.word = db().getWord()
        self.score.setNewEntry(self.word)
        self.choice()


word = db().getWord()
obj = main(word)
print("** The great guessing game **\n"+"Current Guess:----")
obj.choice()
