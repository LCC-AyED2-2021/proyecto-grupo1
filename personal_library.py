from algo1 import *
from linkedlist import *
import os
import pickle
import sys
import Trie

#Input: Dos variable, argv tipo Str y key tipo Int.
#Output: No presenta.
#Function: Invoca a la funcion create library o a search library segun lo precisado por el usuario.
def main(argv, key):
    if key == 0: #Comando create
        createLibrary(argv)
    else: #Comando search
        searchWord(argv)


#Input: recibe una direccion de ficheros
#Output: devuelve un arreglo con la libreria de Trie almacenados
#Funcion: Dado un directorio, la funcion createLibrary crea un arreglo de n elementos, para los cuales creara un Trie por cada elemento.
def createLibrary(localPath):
    if os.path.isdir(localPath) == False: 
      print("invalid directory")
      return None
    directory = os.listdir(localPath) #Lista con los nombres de los .txt
    if len(directory) == 0: 
      print("Empty directory")
      return None
    library = Array(len(directory), Array(2, None)) #Arreglo donde almacenar los nombres de los .txt y sus respectivos Trie's
    lengthDir = len(directory)
    for x in range(0, lengthDir):
        trie = Trie.Trie()
        if os.path.isfile(localPath+ "/" + directory[x]) == False:
          print("Error file missing")
          return None
        currentTxt = open(localPath+ "/" + directory[x], encoding='utf-8')
        currentLine = currentTxt.read()
        length = len(currentLine)
        auxString = ""
        for n in range(0, length): #Loop que recorre completamente el texto dentro de .txt y va almacenando las palabras dentro de un Trie
            if currentLine[n] != " " and currentLine[n] != "." and currentLine[n] != "," and currentLine[n] != "?" and currentLine[n] != "!" and currentLine[n] != "\n":
                auxString = auxString + currentLine[n]
            else: #Fin de una palabra
                Trie.insert(trie, auxString)
                auxString = ""
        library.data[x].data[0] = directory[x] #Almacenamiento del nombre del .txt dentro de la libreria
        library.data[x].data[1] = trie #Almacenamiento del Trie del .txt dentro de la libreria
        currentTxt.close
    saveLibrary(library) #Al terminar, se guarda la libreria en el directorio actual
    return library

#Input: Recibe una esctructura que contiene los nombres de los .txt y ademas contiene los Trie de cada .txt
#Output: No presenta
#Function: Se encarga de guardar en memoria la estructura en la que se encuentran almacenados los trie .txt y los titulos de los mismos
def saveLibrary(library):
    if library == None: return None
    path = os.getcwd() #Obtenemos la direccion donde se almacenara library.
    with open(path + "/library", "wb") as storeLib:
        pickle.dump(library, storeLib)
    print("library created successfully")
    return storeLib

#Input: Recibe una palabra.
#Output: No presenta.
#Function: Busca en una librería todos los archivos que contengan la palabra y los imprime de mayor a menor según su relevancia.
def searchWord(word):
  word = Trie.validateInput(word) #Se valida la entrada.
  if word == "":
    print("There is no word to search.")
    return
  
  path = os.getcwd() #Se accede a la librería.
  if os.path.isfile(path +'/library') == False: 
    print("It is not possible to search for words in an empty library.")
    return None    
  with open(path +'/library', 'br') as f: 
    library = pickle.load(f)
  
  wordsList = LinkedList() 
  for i in range (0,len(library)):  #Bucle que recorre cada documento buscando la palabra.
    counter = 0
    currentNode = library[i][1].root.children
    condition = True
    for j in range(0,len(word)): #Se asume que la palabra existe en el Trie correspondiente al documento, hasta que el bucle encuentre una letra de la palabra que no se presente.
      if currentNode == None: 
        condition = False
        break
      value = word[counter]
      position = Trie.hashAlphabet(value)
      if j < 2: #Si no se encuentra la letra, la condición se vuelve falsa y se corta el bucle.
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
      
      if j != len(word) - 1: #Si la letra se encontró y no es la última, se actualiza la variable para recorrer el Trie.
        if j == 0:
          currentNode = currentNode[position].children
        else:
          if j == 1:
            currentNode = currentNode[position].children.head
          else:
            currentNode = currentNode.children.head
        counter = counter + 1 
      else: #Si la letra se encontró y es la última, se guarda la relevancia del Nodo, siempre que su isEndOfWord sea mayor que 0.
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
      
    if condition: #Si la condición no se volvió falsa, se agrega el documento a la LinkedList con su relevancia y su nombre.
      auxString = String(library[i][0])
      add(wordsList,relevance,substr(auxString,0,len(auxString)-4))

  if wordsList.head == None: #Se imprime la LinkedList ordenada, si es que no se encuentra vacía.
    print("no document found.")
  else: 
    print("Search results for “", word ,"”:")
    if wordsList.head.nextNode == None:
      print("_",  wordsList.head.name, "- Relevancia:", wordsList.head.value)
    else:
      wordsList = MergeSort(wordsList) #Función que ordena la LinkedList.
      currentNode = wordsList.head
      while currentNode != None:
        print("_", currentNode.name, "- Relevancia:", currentNode.value)
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
