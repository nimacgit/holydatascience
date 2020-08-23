import codecs
import pickle

from model import QBook

class Parser:

    def __init__(self, path="data/quran-simple.txt", encoding="utf-8", qbook=None):
        if(qbook == None):
            self.f = codecs.open(path, encoding=encoding)
            self.qbook = QBook.Book(self.f.readlines())
        else:
            self.qbook = qbook

    def read(self, path="data/quran-simple.txt", encoding='utf-8'):
        self.f = codecs.open(path, encoding=encoding)
        self.qbook = QBook.Book(self.f.readlines())

    def save(self, path="data/mybook.pkl"):
        self.bookFile = open(path, 'wb')
        pickle.dump(self.qbook, self.bookFile, pickle.HIGHEST_PROTOCOL)



