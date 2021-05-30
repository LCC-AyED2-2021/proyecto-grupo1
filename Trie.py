from algo1 import *
class root:
    root = None

class TrieNode:
    key = None
    isEndOfWord = 0
    nextNode = None
    parent = None
    children = None

#Input: 
#Output:
#Function:
def insert(tree, string):
    if tree.root == None: tree = addRoot(tree)
    if string == None: return None
    string = validateInput(String(string))
    currentNode = tree.root.children
    length = len(string)
    x = 0
    while x != length:
        if x == length - 1:
            isEndOfWord = 1
        else:
            isEndOfWord = 0
        if x == 0 :
            currentNode = caseOfLevel0(tree, string[x], currentNode, isEndOfWord)
            x += 1
        else:
            if currentNode.children == None: #Primer nodo hijo
                auxNode = TrieNode()
                auxNode.key = string[x]
                auxNode.isEndOfWord = auxNode.isEndOfWord + isEndOfWord        
                auxNode.parent = currentNode
                currentNode.children = auxNode
                currentNode = auxNode
                x += 1
            else: #El nodo ya tiene al menos un hijo
                parentNode = currentNode #Se guarda el nodo padre
                currentNode = currentNode.children
                while currentNode.nextNode != None:
                    if currentNode.key == string[x]: #Si ya existe la key a insertar, entonces avanzamos por ella
                        currentNode.isEndOfWord = currentNode.isEndOfWord + isEndOfWord
                        x += 1
                        break
                if currentNode.key == string[x]: #Si ya existe la key a insertar, entonces avanzamos por ella
                    currentNode.isEndOfWord = currentNode.isEndOfWord + isEndOfWord
                    x += 1
                else: #La key a insertar no se encuentra dentro de los hijos de parentNode
                    auxNode = TrieNode()
                    auxNode.key = string[x]
                    auxNode.parent = parentNode 
                    auxNode.isEndOfWord = auxNode.isEndOfWord + isEndOfWord
                    currentNode.nextNode = auxNode
                    currentNode = auxNode
                    x += 1


def caseOfLevel0(tree, char, currentNode, isEndOfWord):#Revisar esta funcion, tratar de bajar la complejidad a la hora de leerla.
    if currentNode == None: 
        createASCIINode(tree)
    updateASCII(tree.root.children.key, char)
    currentNode = tree.root.children
    if currentNode.nextNode == None: #Caso 1: El nodo a insertar es el primero del Trie, despues del ASCIINode
        auxNode = TrieNode()
        auxNode.key = char
        auxNode.parent = tree.root
        auxNode.isEndOfWord = isEndOfWord + auxNode.isEndOfWord
        currentNode.nextNode = auxNode
        return auxNode
    else:
        while currentNode.nextNode != None: #Caso 2: El nodo a insertar no es el primero despues de ASCIINode
            if currentNode.key == char: #La key ya existe dentro del Trie
                currentNode.isEndOfWord = currentNode.isEndOfWord + isEndOfWord
                return currentNode
            else:
                currentNode = currentNode.nextNode
        if currentNode.key == char and currentNode.nextNode == None: #Revision del ultimo elemento por condicion currentNode.nextNode
            currentNode.isEndOfWord = currentNode.isEndOfWord + isEndOfWord
            return currentNode
        else:
            auxNode = TrieNode()
            auxNode.key = char
            auxNode.parent = tree.root
            auxNode.isEndOfWord = auxNode.isEndOfWord + isEndOfWord
            currentNode.nextNode = auxNode
            return auxNode


def createASCIINode(tree):
    if tree.root == None: return None
    currentNode = tree.root
    currentNode.children = TrieNode()
    currentNode.children.key = Array(74, 0)
    currentNode.parent = tree.root               

#Input: Array Ascii y una letra
#Output: Ascii actualizado
#Function: Se encarga de cambiar los valores 0 por valor 1 en la celda que le corresponde a la letra dentro del arreglo ASCII
def updateASCII(AsciiArray,key):
    if key == None or AsciiArray == None: return None
    else:
        key = hashAlphabet(key)
        AsciiArray[key] = 1
        return AsciiArray

                

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

#Input: tree =(Variable vacia)
#Output: No presenta
#Function: Se encarga de convertir una variable vacia en una variable de tipo root, para usarla de raiz en el arbol
def addRoot(tree):
    if tree != None: return None
    tree = root()
    auxNode = TrieNode()
    tree.root = auxNode
    return tree

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