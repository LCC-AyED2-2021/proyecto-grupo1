from Trie import *
import os
from algo1 import *
localPath = os.listdir("C:\DataTest")
library = Array(len(localPath), Array(2, None))
print(len(localPath))
for x in range(0, len(localPath)):
    trie = Trie()
    currentTxt = open("C:\DataTest/" + localPath[x], encoding='utf-8')
    currentLine = currentTxt.read()
    length = len(currentLine)
    auxString = ""
    for n in range(0, length):
        if currentLine[n] != " " and currentLine[n] != "." and currentLine[n] != "," and currentLine[n] != "?" and currentLine[n] != "!" and currentLine[n] != "\n":
            auxString = auxString + currentLine[n]
        else:
            insert(trie, auxString)
            auxString = ""
    library.data[x].data[0] = localPath[x]
    library.data[x].data[1] = trie
currentTxt.close