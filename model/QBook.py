
class Book:

    def __init__(self, file):
        self.book = file
        self.aye = []
        self.soore = []
        self.aye_meta = []
        self.words = []
        self.uniqWords = []
        self.basicInstruction()
        self.findUniqs()

    def basicInstruction(self):
        for soor in self.book:
            if(len(soor) <= 2):
                continue
            self.soore.append(soor)
            ayes = soor.split('\n')
            for aye in ayes:
                if(len(aye) <= 2):
                    continue
                aye_metas = aye.split("|")
                if len(aye_metas) > 2:
                    self.aye.append(aye_metas[2])
                    self.aye_meta.append((aye_metas[0], aye_metas[1]))
                    for word in aye_metas[2].split(" "):
                        self.words.append(word)

    def findUniqs(self):
        for word in self.words:
            isin = False
            for uWord in self.uniqWords:
                if uWord == word:
                    isin = True
            if not isin:
                self.uniqWords.append(word)