from algo1 import *

#Definimos la estructura ArrayNode.
class ArrayNode:
  key = None
  children = None
  isEndOfWord = 0

#Definimos la estructura LinkedList.
class LinkedList:
  head=None

#Definimos la estructura Trie.
class Trie:
  root = None

#Definimos la estructura TrieNode.
class TrieNode:
  key = None
  children = None
  nextNode = None
  isEndOfWord = 0

#Input: Recibe un Trie T y una palabra element.
#Output: La key de la última letra de la palabra.
#Function: Inserta en T todas las letras de la palabra element que no se encuentren ya insertadas.
def insert(T,element):
  if element == "" : #Se valida la entrada.
    return None
  element = validateInput(element)
  if element == None or element == "":
    return None
  
  length = len(element)
  if T.root == None: #Si el árbol se encuentra vacío se crea su primer nivel, que es un array con 65 slots, uno para cada caracter de hashAlphabet(). Tendrá como hijo(s) otro(s) array(s) del mismo tipo.
    T.root = TrieNode()
    ASCIIArray = Array(65,ArrayNode())
    T.root.children = ASCIIArray
  else:
    ASCIIArray = T.root.children #Variable apuntador.

  for i in range(0,2): #Bucle para insertar las dos primeras letras de la palabra, si es que tiene y no se encuentran ya insertadas.
    position = hashAlphabet(element[i])
    if ASCIIArray[position] == None: #Si la letra no existe, se agrega como un ArrayNode().
      ASCIIArray[position] = ArrayNode()
      ASCIIArray[position].key = element[i]
    if length - 1 != i:
      if i == 0: 
        if ASCIIArray[position].children == None: #Si la letra no es la última, estamos en el primer nivel y no existe un hijo de la letra, este se crea como un array vacío.
          ASCIIArray[position].children = Array(65,ArrayNode())
      else:
        if ASCIIArray[position].children == None: #Si la letra no es la última, estamos en el segundo nivel y no existe un hijo de la letra, este se crea como una LinkedList vacía.
          ASCIIArray[position].children = LinkedList()
    else: #Si la letra es la última de la palabra, se incrementa en uno su valor de isEndOfWord.
      ASCIIArray[position].isEndOfWord = ASCIIArray[position].isEndOfWord + 1
      ASCIIArray[position].children = LinkedList()
      return element
    if i != 1:
      ASCIIArray = ASCIIArray[position].children #Se actualiza la variable apuntador.
  currentNode = ASCIIArray[position]
  for i in range(2, length): #Bucle para insertar el resto de caracteres de element en un nodo nuevo, si es que no se encuentran ya insertados.
    newNode = TrieNode()
    newNode.children = LinkedList()
    newNode.key = element[i]
    if currentNode.children.head != None:  #Si tiene al menos un hijo el nodo padre, se recorre el nivel buscando que el caracter correpondiente coincida con la key de algún nodo.
      currentNode = currentNode.children.head
      while currentNode != None:
        if element[i] == currentNode.key:
          break
        elif currentNode.nextNode == None:
          break
        currentNode = currentNode.nextNode
      if element[i] != currentNode.key: #Si no hay coincidencia, se inserta al final de la LinkedList el TrieNode.
        currentNode.nextNode = TrieNode()
        currentNode.nextNode = newNode
        currentNode = currentNode.nextNode
    else: #Si no tiene hijos, como children del nodo padre se crea una LinkedList y en ella se inserta el TrieNode.
      currentNode.children = LinkedList()
      currentNode.children.head = newNode
      currentNode = currentNode.children.head  #Se actualiza la variable para recorrer el árbol.
    if i == length - 1: #Si el nodo insertado tenía al último caracter de la string, su isEndOfWord se aumenta en uno y se termina la ejecución del bucle, dejando a su children como None.
      currentNode.isEndOfWord = currentNode.isEndOfWord + 1
      return currentNode.key

#Input: Recibe un caracter.
#Output: Una posición en un arreglo de 65 slots.
#Function: Según el código ASCII del caracter, devuelve su posición correspondiente en un arreglo de 65 slots.
def hashAlphabet(key):
  if key == None:
    return None
  key = ord(key)
  if key <= 122 and key >= 97: #Letras de la "a" a la "z"
    key = key - 71
    return key
  if key <= 90 and key >= 65: #Letras de la "A" a las "Z" 
    key = key - 65
    return key
  if key <= 57 and key >= 48: #Numeros del 0 al 9.
    key = key + 4
    return key
  if key == 45: #Guión medio.
    key = 62
    return key
  if key == 8217: #Apóstrofe.
    key = 63
    return key
  if key == 38: #Ampersand.
    key = 64
    return key

#Input: Recibe un string.
#Output: Nuevo string depurado.
#Function: Revisa letra por letra el string, eliminando todo caracter no permitido y devuelve un string nuevo sin estos caracteres.
def validateInput(string):
  length = len(string)
  auxString = ""
  for x in range(0, length):
    key = ord(string[x])
    if key <= 122 and key >= 97: #Letras de la "a" a la "z"
      auxString = auxString + string[x]
    if key <= 90 and key >= 65: #Letras de la "A" a las "Z"
      auxString = auxString + string[x]
    if key <= 57 and key >= 48: #Numeros del 0 al 9.
      auxString = auxString + string[x]
    if key == 45: #Guión medio.
      auxString = auxString + string[x]
    if key == 8217: #Apóstrofe.
      auxString = auxString + string[x]
    if key == 38: #Ampersand.
      auxString = auxString + string[x]
  return auxString 
