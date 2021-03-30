from Clase_NodoHeadColumna import NodoHeadColumna

class ListaHeadColumna():

    def __init__(self):
        self.primero=None
        self.ultimo=None

    def vacio(self):
        return self.primero==None

    def InsertarInicio(self, NodoNuevo):
        self.primero.setAnterior(NodoNuevo)
        NodoNuevo.setSiguiente(self.primero)
        self.primero=NodoNuevo
    
    def InsertarFinal(self, NodoNuevo):
        self.ultimo.setSiguiente(NodoNuevo)
        NodoNuevo.setAnterior(self.ultimo)
        self.ultimo=NodoNuevo

    def InsertarEnmedio(self, NodoNuevo): 
        tmp1=self.primero
        while tmp1.getX() < NodoNuevo.getX():
            tmp1=tmp1.getSiguiente()

        tmp2=tmp1.getAnterior()
        tmp2.setSiguiente(NodoNuevo)
        NodoNuevo.setSiguiente(tmp1)
        NodoNuevo.setAnterior(tmp2)
        tmp1.setAnterior(NodoNuevo)

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
                print("x: ", tmp.getX())
                tmp=tmp.getSiguiente()

    def Buscar(self, x):
        if not self.vacio():
            tmp=self.primero
            while tmp != None:
                if tmp.getX()== x:
                    #print("si existe")
                    return tmp
                tmp=tmp.getSiguiente()
        #print("No existe...")
        return None