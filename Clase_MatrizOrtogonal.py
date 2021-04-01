from Clase_ListaHeadColumna import ListaHeadColumna
from Clase_ListaHeadFilas import ListaHeadFilas

from Clase_NodoOrtogonal import NodoOrtogonal
from Clase_NodoHeadColumna import NodoHeadColumna
from Clase_NodoHeadFila import NodoHeadFila

class MatrizOrtogonal():

    def __init__(self):
        self.columnas=ListaHeadColumna()
        self.filas=ListaHeadFilas()

    def Insertar(self, x, y, dato):
        NodoNuevo=NodoOrtogonal(dato,x,y)

        if self.columnas.Buscar(x) == None:
            self.columnas.Insertar(NodoHeadColumna(x))
        
        if self.filas.Buscar(y)==None:
            self.filas.Insertar(NodoHeadFila(y))
        
        tmpC=self.columnas.Buscar(x)
        tmpF=self.filas.Buscar(y)

        tmpC.columna.Insertar(NodoNuevo)
        tmpF.fila.Insertar(NodoNuevo)

        #print("se inserto en dato:",dato," X:",x," - Y:",y)

    def llenar(self,x,y,Imagen):
        siguienteLinea=0
        for i in range(y):
            for j in range(x):
                self.Insertar(j,i,Imagen[j+siguienteLinea])
            siguienteLinea+=x
        
