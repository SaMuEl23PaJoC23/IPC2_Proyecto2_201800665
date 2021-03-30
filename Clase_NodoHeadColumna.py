from Clase_ListaVertical import ListaVertical

class NodoHeadColumna():

    def __init__(self, x):
        self.x=x
        self.siguiente=None
        self.anterior=None
        self.columna=ListaVertical()

#------ metodos get -------
    def getX(self):
        return self.x

    def getSiguiente(self):
        return self.siguiente
    
    def getAnterior(self):
        return self.anterior

    def getColumna(self):
        return self.columna

#------ metodos set --------
    def setX(self, x):
        self.x=x
    
    def setSiguiente(self, siguiente):
        self.siguiente=siguiente
    
    def setAnterior(self, anterior):
        self.anterior=anterior
    
    def setColumna(self, columna):
        self.columna=columna