from xml.dom import minidom
from mainListas import Nuevo
from graphviz import render
from io import open

indiceMatrices=0
DatosMatricesParaCombobox1=[] #se almacenará el nombre y las dimenciones, para poder llamar al metodo -cargarImagen-
class Lectura():

    def __init__(self):
        self.NuevaMatrizImagen=Nuevo()

    def CargarArchivoXML(self, RutaArchivoXML):   #C:/Users/samal/Desktop/lectura xml/Ejemplo_prueba.xml
        global indiceMatrices
        global DatosMatricesParaCombobox1
        iterador=0
      
        try:
            ArchivoXML=minidom.parse(RutaArchivoXML)    #obtiene el contenido del documento por medio de una ruta
            matrices=ArchivoXML.getElementsByTagName("matriz")  #toma todas las matrices(con etiqueta matriz), elemento Raiz
            NombreMatrices=ArchivoXML.getElementsByTagName("nombre")
            FilasMatrices=ArchivoXML.getElementsByTagName("filas")
            ColumnasMatrices=ArchivoXML.getElementsByTagName("columnas")
            Imagenes=ArchivoXML.getElementsByTagName("imagen")       #toma todos los datos(con etiqueta imagen)
            print("\n>>> Archivo Cargado exitosamente...<<<\n")

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
                
                indiceMatrices+=1
                DatosMatricesParaCombobox1.append(NombreMatriz)
                DatosMatricesParaCombobox1.append(Columnas)
                DatosMatricesParaCombobox1.append(Filas)
                self.NuevaMatrizImagen.AlmacenarMatriz(indiceMatrices,NombreMatriz,Imagen,Columnas,Filas)
                

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
                self.NuevaMatrizImagen.MostrarMatricesG(NombreMatriz,Columnas,Filas)   #por estar dentro del for mostrará todas las matrices guardadas
            print(">>>>>>>>>>>>>>FINALIZO ALMACENAMIENTO<<<<<<<<<<<<")
            #self.NuevaMatrizImagen.MostrarMatricesG("Matriz_2",8,8)        verificar existencia de una matriz cargada y almacenada
            #self.NuevaMatrizImagen.MostrarMatricesG("Matriz_1",10,10)
            return DatosMatricesParaCombobox1
        except FileNotFoundError:
            print("\n>>> Archivo NO existente...<<<\n")


#---------------------editar matrices----------------------
    def CargarImagen(self,NumOperacion, PnombreMatriz, Px, Py,ValX1,ValY1,ValX2,ValY2,CantElementos):
        tmp=self.NuevaMatrizImagen.ListaM.primero
        bandera=False

        #-----------Se cargará la imagen a editar
        while bandera != True:            
            
            if tmp.getNombreM() == PnombreMatriz:   #se indica que matriz se quiere editar
                datosFilaMatriz=""
                for i in range(Py):    #datoM=matriz.filas.Buscar(i).fila.primero    La matriz si inicia en 0,0
                    datoM=tmp.NewMatriz.filas.Buscar(i).fila.primero
                    siguiente=datoM.getDerecha()
                    
                    for j in range(Px):
                        if j > 0:    
                            datoM=siguiente
                            datosFilaMatriz+=datoM.getDato()
                            siguiente=siguiente.getDerecha()
                        else:
                            datosFilaMatriz+=datoM.getDato()
                bandera=True
            else:
                tmp=tmp.siguiente
        
        if NumOperacion == 1:
            self.RotacionHorizontal(PnombreMatriz,datosFilaMatriz,Px,Py)
        elif NumOperacion == 2:
            self.RotacionVertical(PnombreMatriz,datosFilaMatriz,Px,Py)
        elif NumOperacion == 31:
            self.Transpuesta_Cuadrada(PnombreMatriz,datosFilaMatriz,Px,Py)
        elif NumOperacion == 32:
            self.Transpuesta(PnombreMatriz,datosFilaMatriz,Px,Py)
        elif NumOperacion == 4:
            self.LimpiarZona(PnombreMatriz,datosFilaMatriz,Px,Py,ValX1,ValY1,ValX2,ValY2)
        
        elif NumOperacion == 5:
            self.LineaHorizontal(PnombreMatriz,datosFilaMatriz,Px,Py,ValX1,ValY1,CantElementos)
        elif NumOperacion == 6:
            self.LineaVertical(PnombreMatriz,datosFilaMatriz,Px,Py,ValX1,ValY1)
        elif NumOperacion == 7:
            self.AgregarRectangulo(PnombreMatriz,datosFilaMatriz,Px,Py,ValX1,ValY1,ValX2,ValY2)
        elif NumOperacion == 8:
            self.AgregarTriangulo(PnombreMatriz,datosFilaMatriz,Px,Py,ValX1,ValY1,CantElementos)
        
        

        elif NumOperacion == 9:
            self.CrearGrafo(PnombreMatriz,datosFilaMatriz,Px,Py)
        



    def RotacionHorizontal(self, NombreMatriz, Imagen, Columnas, Filas):
        ImagenHorizontal=""
        siguienteFila=(Filas*Columnas)-Columnas

        #Se Rota la imagen
        for i in range(Filas):
            for j in range(Columnas):
                ImagenHorizontal+=Imagen[siguienteFila+j]
            siguienteFila-=Columnas

        
        #se almacena la imagen editada
        tmp=self.NuevaMatrizImagen.ListaM.primero
        bandera=False
        siguienteFila=0

        while bandera != True: 

            if tmp.getNombreM() == NombreMatriz:
                for i in range(Filas):    #datoM=matriz.filas.Buscar(i).fila.primero    La matriz si inicia en 0,0
                    datoM=tmp.NewMatriz.filas.Buscar(i).fila.primero
                    siguiente=datoM.getDerecha()
                    
                    for j in range(Columnas):
                        if j > 0:    
                            datoM=siguiente
                            datoM.setDato(str(ImagenHorizontal[siguienteFila+j]))
                            siguiente=siguiente.getDerecha()
                        else:
                            datoM.setDato(str(ImagenHorizontal[siguienteFila+j]))
                    siguienteFila+=Columnas
                bandera=True
            else:
                tmp=tmp.siguiente


        print("SE GUARDÓ LOS CAMBIOS DE LA EDICION")
        
        print("\n--------MATRIZ HORIZONTAL")
        self.CrearGrafo(NombreMatriz,ImagenHorizontal,Columnas,Filas)
        self.NuevaMatrizImagen.MostrarMatricesG(NombreMatriz,Columnas,Filas)



    def RotacionVertical(self, NombreMatriz, Imagen, Columnas, Filas):
        ImagenVertical=""
        siguienteFila=Columnas-1

        #Se Rota la imagen
        for i in range(Filas):
            for j in range(Columnas):
                ImagenVertical+=Imagen[siguienteFila-j]
            siguienteFila+=Columnas

        
        #se almacena la imagen editada
        tmp=self.NuevaMatrizImagen.ListaM.primero
        bandera=False
        siguienteFila=0
        NombreParaNuevaImagen=""

        while bandera != True: 

            if tmp.getNombreM() == NombreMatriz:

                for i in range(Filas):    #datoM=matriz.filas.Buscar(i).fila.primero    La matriz si inicia en 0,0
                    datoM=tmp.NewMatriz.filas.Buscar(i).fila.primero
                    siguiente=datoM.getDerecha()
                    
                    for j in range(Columnas):
                        if j > 0:    
                            datoM=siguiente
                            datoM.setDato(str(ImagenVertical[siguienteFila+j]))
                            siguiente=siguiente.getDerecha()
                        else:
                            datoM.setDato(str(ImagenVertical[siguienteFila+j]))
                    siguienteFila+=Columnas
                bandera=True
            else:
                tmp=tmp.siguiente


        print("SE GUARDÓ LOS CAMBIOS DE LA EDICION")
        
        print("\n--------MATRIZ VERTICAL")
        self.CrearGrafo(NombreMatriz,ImagenVertical,Columnas,Filas)
        self.NuevaMatrizImagen.MostrarMatricesG(NombreMatriz,Columnas,Filas)


    def Transpuesta_Cuadrada(self, NombreMatriz, Imagen, Columnas, Filas):
        ImagenTranspuesta=""
        FilaConstante=(Filas*Columnas)-Columnas
        siguienteFila=FilaConstante
        aumentador=0

        #Se Rota la imagen
        for i in range(Columnas):
            for j in range(Filas):
                ImagenTranspuesta+=Imagen[siguienteFila]
                siguienteFila-=Columnas
                    
            siguienteFila=0
            aumentador+=1
            siguienteFila+=FilaConstante+aumentador

        #Si la matriz Imagen es cuadrada, es posible remplazar la antigua
        if Columnas == Filas:
            tmp=self.NuevaMatrizImagen.ListaM.primero
            bandera=False
            siguienteFila=0

            while bandera != True: 

                if tmp.getNombreM() == NombreMatriz:

                    for i in range(Filas):    #datoM=matriz.filas.Buscar(i).fila.primero    La matriz si inicia en 0,0
                        datoM=tmp.NewMatriz.filas.Buscar(i).fila.primero
                        siguiente=datoM.getDerecha()
                        
                        for j in range(Columnas):
                            if j > 0:    
                                datoM=siguiente
                                datoM.setDato(str(ImagenTranspuesta[siguienteFila+j]))
                                siguiente=siguiente.getDerecha()
                            else:
                                datoM.setDato(str(ImagenTranspuesta[siguienteFila+j]))
                        siguienteFila+=Columnas
                    bandera=True
                else:
                    tmp=tmp.siguiente
        print("SE GUARDÓ LOS CAMBIOS DE LA EDICION")
        
        print("\n--------MATRIZ TRANSPUESTA-CUADRADA")
        self.CrearGrafo(NombreMatriz,ImagenTranspuesta,Columnas,Filas)
        self.NuevaMatrizImagen.MostrarMatricesG(NombreMatriz,Columnas,Filas)
    

    #si la matriz Imagen NO es cuadrada, entonces
    #se crea una nueva matriz imagen ya que no se ha podido eliminar la anterior version
    def Transpuesta(self, NombreMatriz, Imagen, Columnas, Filas):
        global indiceMatrices
        global DatosMatricesParaCombobox1
        ImagenTranspuesta=""
        FilaConstante=(Filas*Columnas)-Columnas
        siguienteFila=FilaConstante
        aumentador=0

        #Se Rota la imagen
        for i in range(Columnas):
            for j in range(Filas):
                ImagenTranspuesta+=Imagen[siguienteFila]
                siguienteFila-=Columnas
                    
            siguienteFila=0
            aumentador+=1
            siguienteFila+=FilaConstante+aumentador

            
        #se almacenará la imagen editada
        tmp=self.NuevaMatrizImagen.ListaM.primero
        bandera=False
        siguienteFila=0

        while bandera != True: 

            if tmp.getNombreM() == NombreMatriz:
                NombreParaNuevaImagen=tmp.getNombreM()
                tmp.setNombreM("BORRAR")

                indiceMatrices+=1
                self.NuevaMatrizImagen.AlmacenarMatriz(indiceMatrices,NombreParaNuevaImagen,ImagenTranspuesta,Filas,Columnas)
                print(">> Se creó una nueva matriz Imagen<<<")

                bandera=True
            else:
                tmp=tmp.siguiente

        print("SE GUARDÓ LOS CAMBIOS DE LA EDICION")
        
        print("\n--------MATRIZ TRANSPUESTA")
        self.CrearGrafo(NombreParaNuevaImagen,ImagenTranspuesta,Filas,Columnas)
        self.NuevaMatrizImagen.MostrarMatricesG(NombreParaNuevaImagen,Filas,Columnas)

        #se actualiza la lista de nombre, para el combobox
        siguienteNombre=0
        for i in range(int(len(DatosMatricesParaCombobox1)/3)):
            if NombreParaNuevaImagen == DatosMatricesParaCombobox1[siguienteNombre]:
                DatosMatricesParaCombobox1[siguienteNombre+1]=Filas
                DatosMatricesParaCombobox1[siguienteNombre+2]=Columnas
                break
            else:
                siguienteNombre+=3

    def RetornarListaDatosParaCombobox1(self):
        return DatosMatricesParaCombobox1


    def LimpiarZona(self, NombreMatriz, Imagen, Columnas, Filas,X1,Y1,X2,Y2):
        ImagenLimpiar=""
        siguienteFila=0
        
        #Se Limpiará la sona indicada
        if X1 < Columnas and X2 < Columnas:
            if Y1 < Filas and Y2 < Filas:

                for i in range(Filas):
                    for j in range(Columnas):
                        if i>=Y1 and i<=Y2:
                            if j>=X1 and j<=X2:
                                ImagenLimpiar+="-"
                            else:
                                ImagenLimpiar+=Imagen[siguienteFila+j]
                        else:
                            ImagenLimpiar+=Imagen[siguienteFila+j]
                            
                    siguienteFila+=Columnas
                    
        #se almacena la imagen editada
        tmp=self.NuevaMatrizImagen.ListaM.primero
        bandera=False
        siguienteFila=0

        while bandera != True: 

            if tmp.getNombreM() == NombreMatriz:
                for i in range(Filas):    #datoM=matriz.filas.Buscar(i).fila.primero    La matriz si inicia en 0,0
                    datoM=tmp.NewMatriz.filas.Buscar(i).fila.primero
                    siguiente=datoM.getDerecha()
                    
                    for j in range(Columnas):
                        if j > 0:    
                            datoM=siguiente
                            datoM.setDato(str(ImagenLimpiar[siguienteFila+j]))
                            siguiente=siguiente.getDerecha()
                        else:
                            datoM.setDato(str(ImagenLimpiar[siguienteFila+j]))
                    siguienteFila+=Columnas
                bandera=True
            else:
                tmp=tmp.siguiente
        print("SE GUARDÓ LOS CAMBIOS DE LA EDICION")
        
        print("\n--------MATRIZ ZONA LIMPIA")
        self.CrearGrafo(NombreMatriz,ImagenLimpiar,Columnas,Filas)
        self.NuevaMatrizImagen.MostrarMatricesG(NombreMatriz,Columnas,Filas)



    def LineaHorizontal(self, NombreMatriz, Imagen, Columnas, Filas,X1,Y1,CantElementos):
        ImagenConLineaHorizontal=""
        siguienteFila=0
        cant1=0
        EstadoElementso=False
        
        #se agrega la linea en la imagen
        if X1 < Columnas:
            if Y1 < Filas:

                for i in range(Filas):
                    for j in range(Columnas):
                        if i>=Y1:
                            if j>=X1 and cant1 < CantElementos:
                                ImagenConLineaHorizontal+="*"
                                cant1+=1
                                EstadoElementso=True

                            elif cant1 < CantElementos and EstadoElementso==True:
                                ImagenConLineaHorizontal+="*"
                                cant1+=1
                            
                            else:
                                ImagenConLineaHorizontal+=Imagen[siguienteFila+j]
                        
                        else:
                            ImagenConLineaHorizontal+=Imagen[siguienteFila+j]
                            
                    siguienteFila+=Columnas
                
                    
        #se almacena la imagen editada
        tmp=self.NuevaMatrizImagen.ListaM.primero
        bandera=False
        siguienteFila=0

        while bandera != True: 

            if tmp.getNombreM() == NombreMatriz:
                for i in range(Filas):    #datoM=matriz.filas.Buscar(i).fila.primero    La matriz si inicia en 0,0
                    datoM=tmp.NewMatriz.filas.Buscar(i).fila.primero
                    siguiente=datoM.getDerecha()
                    
                    for j in range(Columnas):
                        if j > 0:    
                            datoM=siguiente
                            datoM.setDato(str(ImagenConLineaHorizontal[siguienteFila+j]))
                            siguiente=siguiente.getDerecha()
                        else:
                            datoM.setDato(str(ImagenConLineaHorizontal[siguienteFila+j]))
                    siguienteFila+=Columnas
                bandera=True
            else:
                tmp=tmp.siguiente
        print("SE GUARDÓ LOS CAMBIOS DE LA EDICION")
        
        print("\n--------MATRIZ LINEA HORIZONTAL")  
        self.CrearGrafo(NombreMatriz,ImagenConLineaHorizontal,Columnas,Filas)
        self.NuevaMatrizImagen.MostrarMatricesG(NombreMatriz,Columnas,Filas)



    def LineaVertical(self, NombreMatriz, Imagen, Columnas, Filas,X1,Y1):
        ImagenConLineaVertical=""
        siguienteFila=0
        for i in range(Filas):
            for j in range(Columnas):
                if i== Y1 and j ==X1:
                    ImagenConLineaVertical+='*'
                elif i> Y1 and j ==X1:
                    ImagenConLineaVertical+='*'
                else:
                    ImagenConLineaVertical+=Imagen[siguienteFila+j]              
            siguienteFila+=Columnas


        #se almacena la imagen editada
        tmp=self.NuevaMatrizImagen.ListaM.primero
        bandera=False
        siguienteFila=0

        while bandera != True: 

            if tmp.getNombreM() == NombreMatriz:
                for i in range(Filas):    #datoM=matriz.filas.Buscar(i).fila.primero    La matriz si inicia en 0,0
                    datoM=tmp.NewMatriz.filas.Buscar(i).fila.primero
                    siguiente=datoM.getDerecha()
                    
                    for j in range(Columnas):
                        if j > 0:    
                            datoM=siguiente
                            datoM.setDato(str(ImagenConLineaVertical[siguienteFila+j]))
                            siguiente=siguiente.getDerecha()
                        else:
                            datoM.setDato(str(ImagenConLineaVertical[siguienteFila+j]))
                    siguienteFila+=Columnas
                bandera=True
            else:
                tmp=tmp.siguiente

        print("SE GUARDÓ LOS CAMBIOS DE LA EDICION")
        
        print("\n--------MATRIZ LINEA VERTICAL")  
        self.CrearGrafo(NombreMatriz,ImagenConLineaVertical,Columnas,Filas)
        self.NuevaMatrizImagen.MostrarMatricesG(NombreMatriz,Columnas,Filas)

    

    def AgregarRectangulo(self, NombreMatriz, Imagen, Columnas, Filas,X1,Y1,AgregarX2,AgregarY2):
        ImagenConRectangulo=""
        siguienteFila=0
        #elementos=AgregarX2*AgregarY2

        for i in range(Filas):
            for j in range(Columnas):
                if i >= Y1 and i <= AgregarY2:
                    if j >=X1 and j <=AgregarX2:
                        ImagenConRectangulo+='*'
                    else:
                        ImagenConRectangulo+=Imagen[siguienteFila+j]
                else:
                    ImagenConRectangulo+=Imagen[siguienteFila+j]

            siguienteFila+=Columnas

        #se almacena la imagen editada
        tmp=self.NuevaMatrizImagen.ListaM.primero
        bandera=False
        siguienteFila=0

        while bandera != True: 

            if tmp.getNombreM() == NombreMatriz:
                for i in range(Filas):    #datoM=matriz.filas.Buscar(i).fila.primero    La matriz si inicia en 0,0
                    datoM=tmp.NewMatriz.filas.Buscar(i).fila.primero
                    siguiente=datoM.getDerecha()
                    
                    for j in range(Columnas):
                        if j > 0:    
                            datoM=siguiente
                            datoM.setDato(str(ImagenConRectangulo[siguienteFila+j]))
                            siguiente=siguiente.getDerecha()
                        else:
                            datoM.setDato(str(ImagenConRectangulo[siguienteFila+j]))
                    siguienteFila+=Columnas
                bandera=True
            else:
                tmp=tmp.siguiente

        print("SE GUARDÓ LOS CAMBIOS DE LA EDICION")
        
        print("\n--------MATRIZ LINEA VERTICAL")  
        self.CrearGrafo(NombreMatriz,ImagenConRectangulo,Columnas,Filas)
        self.NuevaMatrizImagen.MostrarMatricesG(NombreMatriz,Columnas,Filas)


    def AgregarTriangulo(self,NombreMatriz, Imagen, Columnas, Filas,X1,Y1,Longitud):
        ImagenConTriangulo=""
        siguienteFila=0
        contador3=0
        elementeos=Longitud*2
        bandera3=False
        #elementos=AgregarX2*AgregarY2

        for i in range(Filas):
            for j in range(Columnas):
                    if j==X1: 
                        if i >=Y1:
                            if contador3 < elementeos:
                                ImagenConTriangulo+='*'
                                contador3+=1
                            else:
                                ImagenConTriangulo+=Imagen[siguienteFila+j]
                                contador3=0
                            
                        else:
                            ImagenConTriangulo+=Imagen[siguienteFila+j]
                        
                    elif j>X1:
                        if  j >= contador3:
                            ImagenConTriangulo+='*'
                            
                        else:
                            ImagenConTriangulo+=Imagen[siguienteFila+j]
                    else:
                        ImagenConTriangulo+=Imagen[siguienteFila+j]

            siguienteFila+=Columnas

        #se almacena la imagen editada
        tmp=self.NuevaMatrizImagen.ListaM.primero
        bandera=False
        siguienteFila=0

        while bandera != True: 

            if tmp.getNombreM() == NombreMatriz:
                for i in range(Filas):    #datoM=matriz.filas.Buscar(i).fila.primero    La matriz si inicia en 0,0
                    datoM=tmp.NewMatriz.filas.Buscar(i).fila.primero
                    siguiente=datoM.getDerecha()
                    
                    for j in range(Columnas):
                        if j > 0:    
                            datoM=siguiente
                            datoM.setDato(str(ImagenConTriangulo[siguienteFila+j]))
                            siguiente=siguiente.getDerecha()
                        else:
                            datoM.setDato(str(ImagenConTriangulo[siguienteFila+j]))
                    siguienteFila+=Columnas
                bandera=True
            else:
                tmp=tmp.siguiente

        print("SE GUARDÓ LOS CAMBIOS DE LA EDICION")
        
        print("\n--------MATRIZ LINEA VERTICAL")  
        self.CrearGrafo(NombreMatriz,ImagenConTriangulo,Columnas,Filas)
        self.NuevaMatrizImagen.MostrarMatricesG(NombreMatriz,Columnas,Filas)




#------------Se crea el grafo y la imagen tipo PNG----------------------

    def CrearGrafo(self,PnombreMatriz,Imagen,Columnas,Filas):

        NombrePictureSalida=PnombreMatriz+".dot"

        Crear_escribirArchivo=open(NombrePictureSalida,'w')
        Crear_escribirArchivo.write('digraph G {\n')
        Crear_escribirArchivo.write('node [shape=plaintext] \n')
        Crear_escribirArchivo.write('a [label=<<table border="0" cellborder="1" cellspacing="0"> \n')

        indice=0
        for i in range(Filas):
            Crear_escribirArchivo.write('<tr> \n')
            for j in range(Columnas):
                if Imagen[indice] =="-":
                    Crear_escribirArchivo.write('<td> </td>\n')
                else:
                    Crear_escribirArchivo.write('<td>*</td>\n')
                indice+=1
            Crear_escribirArchivo.write('</tr>\n')
        Crear_escribirArchivo.write('</table>>];')
        Crear_escribirArchivo.write('}')
        Crear_escribirArchivo.close()

        render('dot','png',NombrePictureSalida)
        print("--- Se generó archivo .dot ---")
        
