from Clase_MatrizOrtogonal import MatrizOrtogonal
class NodoHeadMatriz():

    def __init__(self, indice, nombreM):
        self.indice=indice
        self.nombreM=nombreM
        self.siguiente=None
        self.anterior=None
        self.NewMatriz=MatrizOrtogonal()

#------ metodos get -------
    def getIndice(self):
        return self.indice
    
    def getNombreM(self):
        return self.nombreM

    def getSiguiente(self):
        return self.siguiente
    
    def getAnterior(self):
        return self.anterior

    def getNewMatriz(self):
        return self.NewMatriz

#------ metodos set --------
    def setIndice(self, indice):
        self.indice=indice

    def setnombreM(self, nombreM):
        self.nombreM=nombreM
    
    def setPx(self, Px):
        self.Px=Px
    
    def setPy(self, PY):
        self.Py=PY
    
    def setSiguiente(self, siguiente):
        self.siguiente=siguiente
    
    def setAnterior(self, anterior):
        self.anterior=anterior
    
    def setNewMatriz(self, NewMatriz):
        self.NewMatriz=NewMatriz