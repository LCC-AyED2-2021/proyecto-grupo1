from algo1 import *
from Trie import *
import pickle

#Definimos la estructura LinkedList.
class LinkedList:
  head=None

#Definimos la estructura Node.
class Node:
  value = None
  name = None 
  nextNode = None

#Se crea una función que calcule el número de elementos de una lista.
def length(L):
  #Se crea una variable que indique la cantidad de elementos de L.
  contador = 0

  #Se crea una nueva variable de tipo Node.
  currentNode = L.head

  #Se recorre la lista.
  while currentNode != None:
    currentNode = currentNode.nextNode
    contador = contador + 1
  
  #Finalmente, se devuelve el valor de la variable creada al comienzo de la función.
  return contador

#Se crea una función que agregue un elemento al comienzo de L, siendo L una LinkedList.
def add(L, element, document):

  #Se crea una nueva variable de tipo Node que en value lleva element y se inserta en el comienzo de L.
  newNode = Node()
  newNode.value = element
  newNode.name = document
  newNode.nextNode = L.head
  L.head = newNode
  return

#Se crea una función que inserte un elemento en una posición determinada de una lista.
def insert(L,element,position,document):
  #Se crea una variable que indique la cantidad de elementos de L.
  contador = length(L)

  #Se verifica si la posición ingresada es válida.
  if position < 0 or position > contador:
    #Si la posición ingresada no es válida, se devuelve None.
    return None
  elif position == 0:
    #Si la posición es la inicial, simplemente se llama a add.
    add(L,element,document)
  else:
    #Si la posición ingresada es válida se procede a insertar el elemento, comenzando por crear una nueva variable de tipo Node.
    currentNode = L.head
    #Se crea otra variable de tipo Node que en value lleve element.
    newNode = Node()
    newNode.value = element
    newNode.name = document

    #Se verifica si la lista contiene nodos.
    if currentNode == None:
      #Si la lista no contiene nodos, entonces la segunda variable creada será el único nodo de la misma.
      L.head = newNode
    else:
      #Si la lista contiene uno o más nodos se procede a insertar el elemento en la posición correspondiente, comenzando por crea una variable que indique la posición de cada nodo cuando se recorra la lista.
      currentpos = 0

      #Se recorre la lista.
      while currentNode != None and currentpos < position - 1:
        currentNode = currentNode.nextNode
        currentpos = currentpos + 1

      #Una vez se llega a la posción deseada, se inserta a element.
      newNode.nextNode = currentNode.nextNode
      currentNode.nextNode = newNode
    
    #Finalmente se devuelve la posición indicada.
    return position

def addEnd(L, value, name):
    if L.head == None:
        add(L, value, name)
    else:
        newNode = Node()
        newNode.value = value
        newNode.name = name
        currentNode = L.head
        while currentNode.nextNode != None:
            currentNode = currentNode.nextNode
        currentNode.nextNode = newNode
        return "OK"

def MergeSort(L):
    if L.head == None:
        return
    else:
        return MergeSortR(L)

def MergeSortR(L):
    if L.head.nextNode == None:
        return L
    
    tamaño = length(L)
    midPos = int(tamaño/2)
    leftList = LinkedList()
    rightList = LinkedList()
    currentNode = L.head
    if tamaño % 2 == 0: 
        centinel = midPos
    else:
        centinel = midPos + 1

    for x in range(0, midPos):
        addEnd(leftList, currentNode.value, currentNode.name)
        currentNode = currentNode.nextNode
    
    for x in range(0, centinel):
        addEnd(rightList, currentNode.value, currentNode.name)
        currentNode = currentNode.nextNode

    leftList = MergeSortR(leftList)
    rightList = MergeSortR(rightList)

    return Merge(leftList, rightList)

def Merge(L, R):
    auxList = LinkedList()
    currentNodeL = L.head
    currentNodeR = R.head
    counter = 0
    while currentNodeL != None or currentNodeR != None:
        if currentNodeL != None and currentNodeR != None:
            if currentNodeL.value > currentNodeR.value:
                insert(auxList, currentNodeL.value, counter, currentNodeL.name)
                currentNodeL = currentNodeL.nextNode
            else:
                insert(auxList, currentNodeR.value, counter, currentNodeR.name)
                currentNodeR = currentNodeR.nextNode
        elif currentNodeL == None:
            insert(auxList, currentNodeR.value, counter, currentNodeR.name)
            currentNodeR = currentNodeR.nextNode
        elif currentNodeR == None:
            insert(auxList, currentNodeL.value, counter, currentNodeL.name)
            currentNodeL = currentNodeL.nextNode
        counter += 1 
    return auxList
  
def searchWord(path,word):
  word = validateInput(word)
  if word == "":
    print("There is no word to search.")
    return
  
  with open('C:\Test-Dataset/library', 'br') as f:
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
      position = hashAlphabet(value)
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