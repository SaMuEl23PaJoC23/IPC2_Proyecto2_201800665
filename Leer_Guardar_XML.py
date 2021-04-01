from xml.dom import minidom
from mainListas import Nuevo

class Lectura():

    def __init__(self):
        self.NuevaMatrizImagen=Nuevo()
        
    def CargarArchivoXML(self, RutaArchivoXML):   #C:/Users/samal/Desktop/lectura xml/Ejemplo_prueba.xml
        try:                                     #C:/Users/samal/Desktop/entrada1.xml

            ArchivoXML=minidom.parse(RutaArchivoXML)    #obtiene el contenido del documento por medio de una ruta
            matrices=ArchivoXML.getElementsByTagName("matriz")  #toma todas las matrices(con etiqueta matriz), elemento Raiz
            NombreMatrices=ArchivoXML.getElementsByTagName("nombre")
            FilasMatrices=ArchivoXML.getElementsByTagName("filas")
            ColumnasMatrices=ArchivoXML.getElementsByTagName("columnas")
            Imagenes=ArchivoXML.getElementsByTagName("imagen")       #toma todos los datos(con etiqueta imagen)
            print("\n>>> Archivo Cargado exitosamente...<<<\n")

            iterador=0

            for matriz in matrices: #se itera por la cantidad de etiquetas -matriz- que encuentre
                NombreMatriz=NombreMatrices[iterador].firstChild.data
                Filas=int(FilasMatrices[iterador].firstChild.data)
                Columnas=int(ColumnasMatrices[iterador].firstChild.data)
                Imagen=Imagenes[iterador].firstChild.data

                #Se elimina espacios y saltos de linea dentro de la imagen
                while "\n" in Imagen or "			" in Imagen or "    " in Imagen:
                    Imagen=Imagen.replace("			","")   
                    Imagen=Imagen.replace("\n","")
                    Imagen=Imagen.replace("    ","")

                self.NuevaMatrizImagen.AlmacenarMatriz((iterador+1),NombreMatriz,Imagen,Columnas,Filas)
                

                '''#Se meustra la matriz cargada en consola
                print("---------------------------------------")
                print("Nombre Matriz:",NombreMatriz)
                print("filas:",Filas)
                print("columnas:",Columnas)

                siguienteLineaImagen=0
                for i in range(Filas):  #Se muestra la imagen almacenada en una variable
                    Newlinea=""
                    for j in range(Columnas):
                        Newlinea+=Imagen[j+siguienteLineaImagen]
                    print(Newlinea)
                    siguienteLineaImagen+=Columnas            
        
                iterador+=1
                print("----------------------------------------") '''
                iterador+=1
                #self.NuevaMatrizImagen.MostrarMatricesG(NombreMatriz,Columnas,Filas)
            print(">>>>>>>>>>>>>>FINALIZO ALMACENAMIENTO<<<<<<<<<<<<")
            self.NuevaMatrizImagen.MostrarMatricesG("Matriz_2",8,8)
            self.NuevaMatrizImagen.MostrarMatricesG("Matriz_1",10,10)
        except FileNotFoundError:
            print("\n>>> Archivo NO existente...<<<\n")

        
