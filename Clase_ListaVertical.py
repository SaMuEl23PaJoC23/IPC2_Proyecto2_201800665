from Clase_NodoOrtogonal import NodoOrtogonal

class ListaVertical():

    def __init__(self):
        self.primero=None
        self.ultimo=None
    
    def vacio(self):
        return self.primero==None

    def InsertarInicio(self, NodoNuevo):
        self.primero.setArriba(NodoNuevo)
        NodoNuevo.setAbajo(self.primero)
        self.primero=NodoNuevo
    
    def InsertarFinal(self, NodoNuevo):
        self.ultimo.setAbajo(NodoNuevo)
        NodoNuevo.setArriba(self.ultimo)
        self.ultimo=NodoNuevo

    def InsertarEnmedio(self, NodoNuevo): 
        tmp1=self.primero
        while tmp1.getY() < NodoNuevo.getY():
            tmp1=tmp1.getAbajo()

        tmp2=tmp1.getArriba()
        tmp2.setAbajo(NodoNuevo)
        NodoNuevo.setAbajo(tmp1)
        NodoNuevo.setArriba(tmp2)
        tmp1.setArriba(NodoNuevo)

    def Insertar(self, NodoNuevo):
        if self.vacio():
            self.primero=self.ultimo=NodoNuevo

        else:
            if NodoNuevo.getY() < self.primero.getY(): #Se indica que se va a inserta el nodo al --inicio--
                self.InsertarInicio(NodoNuevo)
            
            elif NodoNuevo.getY() > self.ultimo.getY(): #Se indica que se va a insertar el nodo al --final--
                self.InsertarFinal(NodoNuevo)
            
            else:
                self.InsertarEnmedio(NodoNuevo)

    def Recorrer(self):
        if not self.vacio():
            tmp = self.primero 
            while tmp != None:
                print("dato: ", tmp.getDato() , "x: ", tmp.getX() ," - y: ", tmp.getY())
                tmp=tmp.getAbajo()
