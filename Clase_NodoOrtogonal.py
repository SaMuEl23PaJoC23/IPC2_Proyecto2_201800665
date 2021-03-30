class NodoOrtogonal():

    def __init__(self, dato, x, y):
        self.dato=dato
        self.x=x
        self.y=y
        self.arriba=None
        self.abajo=None
        self.izquierda=None
        self.derecha=None

#------Metodos get -------------
    def getDato(self):
        return self.dato
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getArriba(self):
        return self.arriba
    
    def getAbajo(self):
        return self.abajo
    
    def getIzquierda(self):
        return self.izquierda
    
    def getDerecha(self):
        return self.derecha
#------Metodos set ----------------
    def setDato(self, dato):
        self.dato=dato

    def setX(self, x):
        self.x = x
    
    def setY(self, y):
        self.y = y
    
    def setArriba(self, arriba):
        self.arriba = arriba
    
    def setAbajo(self, abajo):
        self.abajo = abajo
    
    def setIzquierda(self, izquierda):
        self.izquierda = izquierda
    
    def setDerecha(self, derecha):
        self.derecha = derecha