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

#Se crea una función que inserte un elemento(palabra) en T, siendo T un Trie.
def insert(T,element):
  #Se valida la entrada.
  if element == "" :
    return None
  
  element = validateInput(element)
  if element == None or element == "":
    return None
  length = len(element)

  #Se verifica si el árbol se encuentra vacío.
  if T.root == None:
    T.root = TrieNode()
    ASCIIArray = Array(74,ArrayNode())
    T.root.children = ASCIIArray
  else:
    ASCIIArray = T.root.children
    

  #ASCIIArray = T.root.children en teoria esta de mas, cuidado variable apuntador

  for i in range(0,2):
    position = hashAlphabet(element[i])
    if ASCIIArray[position] == None:
      ASCIIArray[position] = ArrayNode()
      ASCIIArray[position].key = element[i]
    if length - 1 != i:
      if i == 0: 
        if ASCIIArray[position].children == None:
          ASCIIArray[position].children = Array(74,ArrayNode())
      else:
        if ASCIIArray[position].children == None:
          ASCIIArray[position].children = LinkedList()
    else:
      ASCIIArray[position].isEndOfWord = ASCIIArray[position].isEndOfWord + 1
      return element
    if i != 1:
     ASCIIArray = ASCIIArray[position].children
             

  currentNode = ASCIIArray[position]
  #Se crea un bucle para insertar cada caracter del elemento en un nodo nuevo, recorriendo nivel por nivel del árbol.
  for i in range(2, length):
    #Se crea un TrieNode, que será el nodo insertado en una lista como hijo.  
    newNode = TrieNode()
    newNode.children = LinkedList()
    newNode.key = element[i]

    #Se verifica que tenga al menos un hijo el nodo padre.
    if currentNode.children.head != None:
      #Si tiene al menos un hijo, se recorre el nivel buscando que el caracter correpondiente coincida con la key de algún nodo.
      currentNode = currentNode.children.head
      while currentNode != None:
        if element[i] == currentNode.key:
          break
        elif currentNode.nextNode == None:
          break
        currentNode = currentNode.nextNode

      #Si no hay coincidencia, se crea un nuevo LinkedNode con su respectivo TrieNode y se inserta al final de la lista y en el árbol.
      if element[i] != currentNode.key:
        currentNode.nextNode = TrieNode()
        currentNode.nextNode = newNode
        currentNode = currentNode.nextNode
    else:
      #Si no tiene hijos, como children del nodo padre se crea una LinkedList y en su value se insertará el nodo con key igual al caracter correspondiente de la string.
      currentNode.children = LinkedList()
      currentNode.children.head = newNode
      
      #Se actualizan los nodos para recorrer el árbol.
      currentNode = currentNode.children.head
      
    #Si el nodo insertado tenía al último caracter de la string, su isEndOfWord se actualiza a true y se termina la ejecución del bucle, dejando a su children como None.
    if i == length - 1:
      currentNode.isEndOfWord = currentNode.isEndOfWord + 1
      return currentNode.key

#Input: Recibe una letra
#Output: Devuelve un codigo 
#Function: Modifica sobre la entrada para devolver un codigo de salida a corde a la posicion del caracter dentro del arreglo ASCII
def hashAlphabet(key):
    if key == None:return None
    key = ord(key)
    #Letras de la "a" a la "z" con ñ incluida
    if (key <= 122 and key >= 97) or key == 241: 
        if key == 241:
            key = 52
        else:
            key = key - 71
        return key
    #Letras de la "A" a las "Z" con Ñ incluida
    if (key <= 90 and key >= 65) or key == 209: 
        if key == 209:
            key = 53
        else:
            key = key - 65
        return key
    #Vocales con tilde, mayusculas y minusculas.
    if key == 225:#"á"
        key = 64
        return key
    if key == 233:#"é"
        key = 65
        return key
    if key == 237:#"í"
        key = 66
        return key
    if key == 243:#"ó"
        key = 67  
        return key  
    if key == 250:#"ú"
        key = 68
        return key
    if key == 193:#"Á"
        key = 69
        return key
    if key == 201:#"É"
        key = 70
        return key
    if key == 205:#"Í"
        key = 71
        return key
    if key == 211:#"Ó"
        key = 72 
        return key
    if key == 218:#"Ú"
        key = 73 
        return key
    #Numeros del 0 al 9.
    if key <= 57 and key >= 48:
        key = key + 6
        return key

#Input: Recibe un string 
#Output: Nuevo string depurado
#Function: Revisa letra por letra el string, eliminando todo caracter no permitido y devuelve un string nuevo sin estos caracteres.
def validateInput(string):
    if string == None:
        return None
    else:
        length = len(string)
        auxString = ""
        for x in range(0, length):
            key = ord(string[x])

            #Letras de la "a" a la "z" con ñ incluida
            if (key <= 122 and key >= 97) or key == 241: 
                auxString = auxString + string[x]
            #Letras de la "A" a las "Z" con Ñ incluida
            if (key <= 90 and key >= 65) or key == 209: 
                auxString = auxString + string[x]
            #Vocales con tilde, mayusculas y minusculas.
            if key == 225 or key == 233 or key == 237 or key == 243 or key == 250 or key == 193 or key == 201 or key == 205 or key == 211 or key == 218:
                auxString = auxString + string[x]
            #Numeros del 0 al 9.
            if key <= 57 and key >= 48:
                auxString = auxString + string[x]
        return auxString
