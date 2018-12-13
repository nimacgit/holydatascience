import codecs

f = codecs.open("../data/quran-simple.txt", encoding='utf-8')
book = f.readlines()
for soor in book:
    ayes = soor.split('\n')
    for aye in ayes:
        aye_metas = aye.split("|")


