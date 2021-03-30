from Clase_NodoOrtogonal import NodoOrtogonal
from Clase_ListaVertical import ListaVertical
from Clase_ListaHorizontal import ListaHorizontal

from Clase_NodoHeadFila import NodoHeadFila
from Clase_ListaHeadFilas import ListaHeadFilas

from Clase_NodoHeadColumna import NodoHeadColumna
from Clase_ListaHeadColumna import ListaHeadColumna

from Clase_MatrizOrtogonal import MatrizOrtogonal


ListaV=ListaVertical()
ListaH=ListaHorizontal()

ListaCF=ListaHeadFilas()
ListaCC=ListaHeadColumna()

matriz=MatrizOrtogonal()

'''print("---lista vertical---")
ListaV.Insertar(NodoOrtogonal(10,0,1))
ListaV.Insertar(NodoOrtogonal(30,0,3))
ListaV.Insertar(NodoOrtogonal(20,0,2))
ListaV.Insertar(NodoOrtogonal(50,0,5))
ListaV.Insertar(NodoOrtogonal(40,0,4))
ListaV.Recorrer()
'''

'''print("---lista horizontal---")
ListaH.Insertar(NodoOrtogonal(10,1,0))
ListaH.Insertar(NodoOrtogonal(30,3,0))
ListaH.Insertar(NodoOrtogonal(20,2,0))
ListaH.Insertar(NodoOrtogonal(50,5,0))
ListaH.Insertar(NodoOrtogonal(40,4,0))
ListaH.Recorrer()'''

'''print("---lista HEAD Filas---")
ListaCF.Insertar(NodoHeadFila(1))
ListaCF.Insertar(NodoHeadFila(3))
ListaCF.Insertar(NodoHeadFila(2))
ListaCF.Insertar(NodoHeadFila(5))
ListaCF.Insertar(NodoHeadFila(4))
ListaCF.Recorrer()

ListaCF.Buscar(10)'''

'''print("---lista HEAD Columnas---")
ListaCC.Insertar(NodoHeadColumna(1))
ListaCC.Insertar(NodoHeadColumna(3))
ListaCC.Insertar(NodoHeadColumna(2))
ListaCC.Insertar(NodoHeadColumna(5))
ListaCC.Insertar(NodoHeadColumna(4))
ListaCC.Recorrer()

ListaCC.Buscar(12)'''

print("---MATRIZ ORTOGONAL---")
# -X-Columnas  -Y-Filas (x,y)
matriz.llenar(5,5)
#matriz.RecorrerMatriz(3,3)

print("buscando por filas:",matriz.filas.Buscar(2).fila.primero.getDerecha().getDerecha().getArriba().getDato())
print("buscando por columnas:",matriz.columnas.Buscar(1).columna.primero.getAbajo().getAbajo().getDerecha().getDato())

for i in range(5):
    datoM=matriz.filas.Buscar(i).fila.primero
    siguiente=datoM.getDerecha()
    datosFilaMatriz=""
    for j in range(5):
        if j > 0:    
            datoM=siguiente
            datosFilaMatriz+="|"+str(datoM.getDato())+"|"
            siguiente=siguiente.getDerecha()
        else:
            datosFilaMatriz+="|"+str(datoM.getDato())+"|"
        
    print(datosFilaMatriz)
