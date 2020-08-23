import pickle

def loadTheBook(path = 'data/mybook.pkl'):
    qfile = open(path, 'rb')
    qbook = pickle.load(qfile)
    return qbook
