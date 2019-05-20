

freq_dict ={
'a':8.17,
'b':1.49,
'c':2.78,
'd':4.25,
'e':12.70,
'f':2.23,
'g':2.02,
'h':6.09,
'i':6.97,
'j':0.15,
'k':0.77,
'l':4.03,
'm':2.41,
'n':6.75,
'o':7.51,
'p':1.93,
'q':0.10,
'r':5.99,
's':6.33,
't':9.06,
'u':2.76,
'v':0.98,
'w':2.36,
'x':0.15,
'y':1.97,
'z':0.07
}


class gameScore:

    def __init__(self, word):
        self.list_of_tuples = []
        self.Game = 0
        self.Word = word
        self.Status = ""
        self.BadGuesses = 0
        self.MissedLetters = 0
        self.Score = 0

    def setGame(self):
        self.Game += 1

    def setStatus(self, status):
        self.Status = status

    def setBadGuesses(self):
        self.BadGuesses += 1



    def setMissedLetters(self):
        self.MissedLetters += 1

    def computeScore(self, GuessWord):
        TotalScore =0
        for i in range(0,len(self.Word)):
            if(GuessWord[i] != self.Word[i]):
                TotalScore = TotalScore + freq_dict[self.Word[i]]
        self.Score = float("{0:.2f}".format(TotalScore))
        if(self.MissedLetters != 0):
            self.Score = float("{0:.2f}".format(self.Score / self.MissedLetters))
        if(self.BadGuesses != 0):
            self.Score = float("{0:.2f}".format(self.Score - self.BadGuesses*(self.Score/10)))


    def setNewEntry(self,word):
        self.Game +=1
        self.Word = word
        self.Status = ""
        self.BadGuesses = 0
        self.MissedLetters = 0
        self.Score = 0


    def makeTup(self,guessWord,status):

        if(status != "Gave up"):
            self.computeScore(guessWord)
            self.Status = status
            tup = (self.Game+1,self.Word,self.Status,self.BadGuesses,self.MissedLetters,self.Score)
            self.list_of_tuples.append(tup)
        elif status == "Gave up":

            TotalScore = 0
            for i in range(0, len(self.Word)):
                if (guessWord[i] == self.Word[i]):
                    TotalScore = TotalScore - freq_dict[self.Word[i]]
            self.Score = float("{0:.2f}".format(TotalScore))
            if (self.BadGuesses != 0):
                self.Score = float("{0:.2f}".format(self.Score - self.BadGuesses * (self.Score / 10)))
            if (self.MissedLetters != 0):
                self.Score = float("{0:.2f}".format(self.Score / self.MissedLetters))
            self.Status = status
            tup = (self.Game, self.Word, self.Status, self.BadGuesses, self.MissedLetters, self.Score)
            self.list_of_tuples.append(tup)


    def displayScore(self):
        column_width = 15
        print("Game".ljust(column_width), end='')
        print("Word".ljust(column_width), end='')
        print("Status".ljust(column_width), end='')
        print("Bad Guess".ljust(column_width), end='')
        print("Missed Letters".ljust(column_width), end='')
        print("Score".ljust(column_width))

        print("---------------".ljust(column_width), end='')
        print("---------------".ljust(column_width), end='')
        print("---------------".ljust(column_width), end='')
        print("---------------".ljust(column_width), end='')
        print("---------------".ljust(column_width), end='')
        print("---------------".ljust(column_width))
        MainScore = 0
        for i in self.list_of_tuples:

            for el in range(len(i)):
                if(el!= len(i)-1):
                    print(str(i[el]).ljust(column_width), end='')
                else:
                    MainScore = MainScore + i[el]
                    print(str(i[el]).ljust(column_width))
            # result = ''.join(str(i))
        print("Total Score:" + str(MainScore))
