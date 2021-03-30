from Clase_ListaHorizontal import ListaHorizontal

class NodoHeadFila():

    def __init__(self, y):
        self.y=y
        self.siguiente=None
        self.anterior=None
        self.fila=ListaHorizontal()

#------ metodos get -------
    def getY(self):
        return self.y

    def getSiguiente(self):
        return self.siguiente
    
    def getAnterior(self):
        return self.anterior

    def getFila(self):
        return self.fila

#------ metodos set --------
    def setY(self, y):
        self.y=y
    
    def setSiguiente(self, siguiente):
        self.siguiente=siguiente
    
    def setAnterior(self, anterior):
        self.anterior=anterior
    
    def setFila(self, fila):
        self.fila=fila