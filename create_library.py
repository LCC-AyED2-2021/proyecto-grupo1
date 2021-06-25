from Trie import *
from algo1 import *
import os
import pickle

#Input: recibe una direccion de ficheros
#Output: devuelve un arreglo con la libreria de Trie almacenados
#Funcion: Dado un directorio, la funcion createLibrary crea un arreglo de n elementos, para los cuales creara un Trie por cada elemento.
def createLibrary(localPath):
    directory = os.listdir(localPath)
    library = Array(len(directory), Array(2, None))
    for x in range(0, len(directory)):
        trie = Trie()
        currentTxt = open(localPath+ "/" + directory[x], encoding='utf-8')
        currentLine = currentTxt.read()
        length = len(currentLine)
        auxString = ""
        for n in range(0, length):
            if currentLine[n] != " " and currentLine[n] != "." and currentLine[n] != "," and currentLine[n] != "?" and currentLine[n] != "!" and currentLine[n] != "\n":
                auxString = auxString + currentLine[n]
            else:
                insert(trie, auxString)
                auxString = ""
        library.data[x].data[0] = directory[x]
        library.data[x].data[1] = trie
    currentTxt.close
    saveLibrary(library, localPath)
    return library

def saveLibrary(library, localPath):
    if library == None: return None
    with open(localPath + "/library", "xb") as storeLib:
        pickle.dump(library, storeLib)
    return storeLib
