#Definimos la estructura LinkedList.
class LinkedList:
  head=None

#Definimos la estructura Node.
class Node:
  value = None
  name = None 
  nextNode = None

#Input: Recibe una LinkedList L.
#Output: Cantidad de elementos de la LinkedList.
#Function: Calcula el número de elementos de una lista.
def length(L):
  contador = 0
  currentNode = L.head
  while currentNode != None: #Se recorre la lista hasta el final.
    currentNode = currentNode.nextNode
    contador = contador + 1
  return contador #Se devuelve el valor de la variable contador.

#Input: Recibe una LinkedList L, un valor element y una cadena document.
#Output: No presenta.
#Function: Agrega un elemento al comienzo de L
def add(L, element, document):
  newNode = Node()
  newNode.value = element
  newNode.name = document
  newNode.nextNode = L.head
  L.head = newNode
  return

#Input: Recibe una LinkedList L, un valor element, una posición position y una cadena document.
#Output: position.
#Function: Inserte un elemento en una posición determinada de L.
def insert(L,element,position,document):
  contador = length(L)
  if position < 0 or position > contador:
    return None #Si la posición ingresada no es válida, se devuelve None.
  elif position == 0:
    add(L,element,document) #Si la posición es la inicial, se llama a add.
  else: #Si la posición ingresada es válida se inserta donde corresponde.
    currentNode = L.head
    newNode = Node()
    newNode.value = element
    newNode.name = document
    if currentNode == None:
      L.head = newNode #Si L no contiene nodos, el elemento será el único nodo de la misma.
    else:
      currentpos = 0
      while currentNode != None and currentpos < position - 1: #Se recorre la lista.
        currentNode = currentNode.nextNode
        currentpos = currentpos + 1
      newNode.nextNode = currentNode.nextNode #Una vez se llega a la posción deseada, se inserta element.
      currentNode.nextNode = newNode
    return position

#Input: L = lista; value = int; name = Str
#Output: No presenta
#Function: Se encarga de añadir un nodo nuevo al final de una lista
def addEnd(L, value, name):
    if L.head == None: #Si la lista esta vacia, se invoca a un add normal.
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

#Input: Recibe una lista
#Output: Lista ordenada de mayor a menor
#Function: Ordena una lista de mayor a menor atraves de la tecnica "divide and conquer"
def MergeSort(L): #Funcion wrapper
    if L.head == None: #Validacion de entradas
        return
    else:
        return MergeSortR(L)

#Input: Recibe una lista
#Output: Lista ordenada de mayor a menor
#Function: Ordena una lista de mayor a menor atraves de la tecnica "divide and conquer". (Divide)
def MergeSortR(L):
    if L.head.nextNode == None: #Valida entradas, caso de parada
        return L
    
    tamaño = length(L)
    midPos = int(tamaño/2)
    leftList = LinkedList()
    rightList = LinkedList()
    currentNode = L.head
    if tamaño % 2 == 0: #Se busca que la lista sea par, esto es para que a la hora de la division no genere problemas
        centinel = midPos
    else:
        centinel = midPos + 1 #Variable centinel se utiliza para lograr una buena division de listas

    for x in range(0, midPos):
        addEnd(leftList, currentNode.value, currentNode.name)
        currentNode = currentNode.nextNode
    
    for x in range(0, centinel):
        addEnd(rightList, currentNode.value, currentNode.name)
        currentNode = currentNode.nextNode

    leftList = MergeSortR(leftList) #Llamado recursivo para ir subdividiendo las listas hasta que queden de un solo nodo
    rightList = MergeSortR(rightList)

    return Merge(leftList, rightList)

#Input: Recibe dos listas, que son sublistas de una mas grande. L = leftList ; R= rightList
#Output: Devuelve una lista auxiliar ordenada
#Function: Se encarga de mezclar y ordenar dichas sublistas, generando una lista mas grande ya ordenada. (Conquer)
def Merge(L, R):
    auxList = LinkedList()
    currentNodeL = L.head
    currentNodeR = R.head
    counter = 0
    while currentNodeL != None or currentNodeR != None: #Se recorren ambas listas hasta que queden completamente recorridas
        if currentNodeL != None and currentNodeR != None: #Caso donde ambas lista no han sido recorridas en su totalidad
            if currentNodeL.value > currentNodeR.value:
                insert(auxList, currentNodeL.value, counter, currentNodeL.name)
                currentNodeL = currentNodeL.nextNode
            else:
                insert(auxList, currentNodeR.value, counter, currentNodeR.name)
                currentNodeR = currentNodeR.nextNode
        elif currentNodeL == None: #Caso donde la lista de la izquierda fue recorrida en su totalidad
            insert(auxList, currentNodeR.value, counter, currentNodeR.name)
            currentNodeR = currentNodeR.nextNode
        elif currentNodeR == None: #Caso donde la lista de la derecha fue recorrida en su totalidad
            insert(auxList, currentNodeL.value, counter, currentNodeL.name)
            currentNodeL = currentNodeL.nextNode
        counter += 1 
    return auxList
