import create_library
import sys

def main(argv, key):
    if key == 0: #comando create
        create_library.createLibrary(argv)
    else:
        #Llamado al algoritmo de busqueda al estilo, search.search(argv)
        print("Brandom Sanderson")

if __name__ == "__main__":
    if len(sys.argv) != 3: print("invalid Input")
    else:
        if sys.argv[1] == "-create":
            main(sys.argv[2], 0)
        elif sys.argv[1] == "-search":
            main(sys.argv[2], 1)
        else:
            print("unknown command")