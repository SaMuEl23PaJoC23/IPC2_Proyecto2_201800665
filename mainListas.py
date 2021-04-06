from Clase_NodoOrtogonal import NodoOrtogonal
from Clase_ListaVertical import ListaVertical
from Clase_ListaHorizontal import ListaHorizontal

from Clase_NodoHeadFila import NodoHeadFila
from Clase_ListaHeadFilas import ListaHeadFilas

from Clase_NodoHeadColumna import NodoHeadColumna
from Clase_ListaHeadColumna import ListaHeadColumna

from Clase_MatrizOrtogonal import MatrizOrtogonal

from Clase_ListaHeadMatriz import ListaHeadMatriz
from Clase_NodoHeadMatriz import NodoHeadMatriz

class Nuevo():

    def __init__(self):
        self.ListaM=ListaHeadMatriz()
        #self.matriz=MatrizOrtogonal()

    def AlmacenarMatriz(self, Indice, NombreMatriz, Imagen, Px, Py):
        self.ListaM.Insertar(Indice, NombreMatriz, Imagen, Px, Py)

    #recorrer despues de que ya se encuentre almacenado los datos en la matriz ortogonal
    def MostrarMatricesG(self,PnombreMatriz, Px, Py):

        tmp=self.ListaM.primero
        #matriz.llenar(3,3)

        bandera=False
        while bandera != True:
                
            if tmp.getNombreM() == PnombreMatriz: 
                for i in range(Py):    #datoM=matriz.filas.Buscar(i).fila.primero    La matriz si inicia en 0,0
                    datoM=tmp.NewMatriz.filas.Buscar(i).fila.primero
                    siguiente=datoM.getDerecha()
                    datosFilaMatriz=""

                    for j in range(Px):
                        if j > 0:    
                            datoM=siguiente
                            datosFilaMatriz+="|"+str(datoM.getDato())+"|"
                            siguiente=siguiente.getDerecha()
                        else:
                            datosFilaMatriz+="|"+str(datoM.getDato())+"|"
                        
                    print(datosFilaMatriz)

                #tmp=tmp.siguiente para poder recorrer al siguiente, por ende a los todos
                bandera=True
                print("-------------------")
                
            else:
                tmp=tmp.siguiente