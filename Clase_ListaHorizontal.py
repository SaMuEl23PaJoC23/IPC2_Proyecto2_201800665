from Clase_NodoOrtogonal import NodoOrtogonal

class ListaHorizontal():
    
    def __init__(self):
        self.primero=None
        self.ultimo=None
    
    def vacio(self):
        return self.primero==None

    def InsertarInicio(self, NodoNuevo):
        self.primero.setIzquierda(NodoNuevo)
        NodoNuevo.setDerecha(self.primero)
        self.primero=NodoNuevo
    
    def InsertarFinal(self, NodoNuevo):
        self.ultimo.setDerecha(NodoNuevo)
        NodoNuevo.setIzquierda(self.ultimo)
        self.ultimo=NodoNuevo

    def InsertarEnmedio(self, NodoNuevo): 
        tmp1=self.primero
        while tmp1.getX() < NodoNuevo.getX():
            tmp1=tmp1.getDerecha()

        tmp2=tmp1.getIzquierda()
        tmp2.setDerecha(NodoNuevo)
        NodoNuevo.setDerecha(tmp1)
        NodoNuevo.setIzquierda(tmp2)
        tmp1.setIzquierda(NodoNuevo)

    def Insertar(self, NodoNuevo):
        if self.vacio():
            self.primero=self.ultimo=NodoNuevo

        else:
            if NodoNuevo.getX() < self.primero.getX(): #Se indica que se va a inserta el nodo al --inicio--
                self.InsertarInicio(NodoNuevo)
            
            elif NodoNuevo.getX() > self.ultimo.getX(): #Se indica que se va a insertar el nodo al --final--
                self.InsertarFinal(NodoNuevo)
            
            else:
                self.InsertarEnmedio(NodoNuevo)

    def Recorrer(self):
        if not self.vacio():
            tmp = self.primero 
            while tmp != None:
                print("dato: ", tmp.getDato() , "x: ", tmp.getX() ," - y: ", tmp.getY())
                tmp=tmp.getDerecha()