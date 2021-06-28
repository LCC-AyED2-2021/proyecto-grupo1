from algo1 import *
from linkedlist import *
import os
import pickle
import sys
import Trie

def main(argv, key):
    if key == 0: #comando create
        createLibrary(argv)
    else:
        searchWord(argv)
        #Llamado al algoritmo de busqueda al estilo, search.search(argv)

#Input: recibe una direccion de ficheros
#Output: devuelve un arreglo con la libreria de Trie almacenados
#Funcion: Dado un directorio, la funcion createLibrary crea un arreglo de n elementos, para los cuales creara un Trie por cada elemento.
def createLibrary(localPath):
    directory = os.listdir(localPath)
    library = Array(len(directory), Array(2, None))
    lengthDir = len(directory)
    for x in range(0, lengthDir):
        trie = Trie.Trie()
        currentTxt = open(localPath+ "/" + directory[x], encoding='utf-8')
        currentLine = currentTxt.read()
        length = len(currentLine)
        auxString = ""
        for n in range(0, length):
            if currentLine[n] != " " and currentLine[n] != "." and currentLine[n] != "," and currentLine[n] != "?" and currentLine[n] != "!" and currentLine[n] != "\n":
                auxString = auxString + currentLine[n]
            else:
                Trie.insert(trie, auxString)
                auxString = ""
        library.data[x].data[0] = directory[x]
        library.data[x].data[1] = trie
        currentTxt.close
    saveLibrary(library)
    return library

def saveLibrary(library):
    if library == None: return None
    path = os.getcwd()
    with open(path + "/library", "xb") as storeLib:
        pickle.dump(library, storeLib)
    return storeLib
  
def searchWord(word):
  word = Trie.validateInput(word)
  if word == "":
    print("There is no word to search.")
    return
  path = os.getcwd()

  with open(path +'/library', 'br') as f:
    library = pickle.load(f)
  wordsList = LinkedList()
  for i in range (0,len(library)):
    counter = 0
    currentNode = library[i][1].root.children
    condition = True
    for j in range(0,len(word)):
      if currentNode == None:
        condition = False
        break
      value = word[counter]
      position = Trie.hashAlphabet(value)
      if j < 2:
        if currentNode[position] == None or currentNode[position].key != value:
          condition = False
          break
      else:
        while currentNode != None:
          if currentNode.key == value:
            break
          currentNode = currentNode.nextNode
        if currentNode == None:
          condition = False
          break
      
      if j != len(word) - 1:
        if j == 0:
          currentNode = currentNode[position].children
        else:
          if j == 1:
            currentNode = currentNode[position].children.head
          else:
            currentNode = currentNode.children.head
        counter = counter + 1 
      else:
        if j < 2:
          if currentNode[position].isEndOfWord == 0:
            condition = False
            break
          else:
            relevance = currentNode[position].isEndOfWord
        else:
          if currentNode.isEndOfWord == 0:
            condition = False
            break
          else:
            relevance = currentNode.isEndOfWord  
      
    if condition:
      auxString = String(library[i][0])
      add(wordsList,relevance,substr(auxString,0,len(auxString)-4))

  if wordsList.head == None:
    print("no document found.")
  else:
    print("Search results for “", word ,"”:")
    if wordsList.head.nextNode == None:
      print("_",  wordsList.head.name)
    else:
      wordsList = MergeSort(wordsList)
      currentNode = wordsList.head
      while currentNode != None:
        print("_", currentNode.name)
        currentNode = currentNode.nextNode
  return


if __name__ == "__main__":
    if len(sys.argv) != 3: print("invalid Input")
    else:
        if sys.argv[1] == "-create":
            main(sys.argv[2], 0)
        elif sys.argv[1] == "-search":
            main(sys.argv[2], 1)
        else:
            print("unknown command")