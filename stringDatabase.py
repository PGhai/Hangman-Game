import random as r

class stringDatabase:
    def __init__(self):
        self.words_list = []

    def getWord(self):
        with open("F:/Winters19/comp/four_letters.txt", "r") as file:
            for line in file:
                words = line.replace("\n", "").split(" ")
                self.words_list = self.words_list + words

        word = r.choice(self.words_list)
        return word

# ab =  stringDatabase()
# print (ab.getWord())