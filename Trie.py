from algo1 import *
class root:
    head = None

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
    if tree == None: addRoot(tree, string)
    if string == None: return None
    string = validateInput(String(string))
    currentNode = tree.root
    length = len(string)
    for x in range(0, length): #Deberia loopear hasta length - 1 o hasta length para tomar la ultima letra? #Posible out of range
        if currentNode.children == None:
            if x==0:
                auxNode = TrieNode()
                ASCIIArray = Array(74, 0)
                auxNode.key = ASCIIArray
                auxNode.parent = currentNode
                currentNode.children = auxNode
                updateASCII(ASCIIArray, string[x])
                currentNode = auxNode
                auxNode = TrieNode()
                auxNode.key = string[x]
                auxNode.parent = tree.root
                if x == length - 1:
                    auxNode.isEndOfWord += 1
                currentNode.nextNode = auxNode
            else:
                auxNode = TrieNode()
                auxNode.key = string[x]
                auxNode.parent = currentNode
                if x == length - 1:
                    auxNode.isEndOfWord += 1
                currentNode.children = auxNode
            

                    

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
    #Letras de la "a" a la "z" con ñ incluida
    if ord(key) <= 122 or ord(key) >= 97 or ord(key) == 241: 
        if key == 241:
            key = 26
        else:
            key = key - 97
    #Letras de la "A" a las "Z" con Ñ incluida
    if ord(key) <= 90 or ord(key) >= 65 or ord(key) == 209: 
        if key == 209:
            key = 53
        else:
            key = key -65
    #Vocales con tilde, mayusculas y minusculas.
    if ord(key) == 225:#"á"
        key = 55
    if ord(key) == 233:#"é"
        key = 56 
    if ord(key) == 237:#"í"
        key = 57
    if ord(key) == 243:#"ó"
        key = 58    
    if ord(key) == 250:#"ú"
        key = 59
    if ord(key) == 193:#"Á"
        key = 60
    if ord(key) == 201:#"É"
        key = 61
    if ord(key) == 205:#"Í"
        key = 62
    if ord(key) == 211:#"Ó"
        key = 63 
    if ord(key) == 218:#"Ú"
        key = 64 
    #Numeros del 0 al 9.
    if ord(key) <= 57 or ord(key) >= 48:
        key = key + 16
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
        for x in range(0, length - 1):
            #Letras de la "a" a la "z" con ñ incluida
            if ord(string[x]) <= 122 or ord(string[x]) >= 97 or ord(string[x]) == 241: 
                auxString = auxString + string[x]
            #Letras de la "A" a las "Z" con Ñ incluida
            if ord(string[x]) <= 90 or ord(string[x]) >= 65 or ord(string[x]) == 209: 
                auxString = auxString + string[x]
            #Vocales con tilde, mayusculas y minusculas.
            if ord(string[x]) == 225 or ord(string[x]) == 233 or ord(string[x]) == 237 or ord(string[x]) == 243 or ord(string[x]) == 250 or ord(string[x]) == 193 or ord(string[x]) == 201 or ord(string[x]) == 205 or ord(string[x]) == 211 or ord(string[x]) == 218:
                auxString = auxString + string[x]
            #Numeros del 0 al 9.
            if ord(string[x]) <= 57 or ord(string[x]) >= 48:
                auxString = auxString + string[x]