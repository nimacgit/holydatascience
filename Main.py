from model.QBook import Book
from reader import Parser, Loader


parser = Parser.Parser()
parser.qbook.findUniqRatio()
parser.save()


qbook = Loader.loadTheBook()
print(len(qbook.uniqWords))
sorted = sorted(qbook.uniqWordsRatio, key=lambda tup: tup[1], reverse=True)
for word in sorted:
    print(word)