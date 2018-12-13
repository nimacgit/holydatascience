import codecs
import pickle

from model import QBook

f = codecs.open("../data/quran-simple.txt", encoding='utf-8')
qbook = QBook.Book(f.readlines())
bookFile = open('../data/mybook.pkl', 'wb')


for word in qbook.uniqWords:
    print(word)
print(len(qbook.book))
print(len(qbook.words))
print(len(qbook.uniqWords))
pickle.dump(qbook, bookFile, pickle.HIGHEST_PROTOCOL)

