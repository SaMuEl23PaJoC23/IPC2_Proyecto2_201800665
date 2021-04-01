from Clase_NodoHeadMatriz import NodoHeadMatriz
from Clase_MatrizOrtogonal import MatrizOrtogonal

class ListaHeadMatriz():

    def __init__(self):
        self.primero=None
        self.ultimo=None
        self.Matrix=MatrizOrtogonal()

    def vacio(self):
        return self.primero==None
    

    def Insertar(self, indice,nombreMatriz, Imagen,Px,Py):
        if self.vacio():
            self.primero=self.ultimo=NodoHeadMatriz(indice,nombreMatriz)
            self.ultimo.NewMatriz.llenar(Px,Py,Imagen) #tal vez primero
            
        else:
            NodoNuevo=NodoHeadMatriz(indice,nombreMatriz)
            self.ultimo.setSiguiente(NodoNuevo)
            NodoNuevo.setAnterior(self.ultimo)
            self.ultimo=NodoNuevo
            self.ultimo.NewMatriz.llenar(Px,Py,Imagen)

    def Recorrer(self):
        if not self.vacio():
            tmp = self.primero 
            while tmp != None:
                print("indice: ", tmp.getIndice())
                tmp=tmp.getSiguiente()
        else:
            print("vacio")

    def Buscar(self, indice):
        if not self.vacio():
            tmp=self.primero
            while tmp != None:
                if tmp.getIndice()== indice:
                    print("si existe")
                    return tmp
                tmp=tmp.getSiguiente()
        print("No existe...")
        return None