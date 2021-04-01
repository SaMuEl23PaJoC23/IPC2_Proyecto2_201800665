from Leer_Guardar_XML import Lectura
from tkinter import *
from tkinter import filedialog

from Leer_Guardar_XML import Lectura

leer_guardar_Archivo=Lectura()


#leerArchivo=Lectura()

#leerArchivo.CargarArchivoXML("C:/Users/samal/Desktop/archivos de prueba xml/entrada2.xml")  #C:/Users/samal/Desktop/archivos de prueba xml/entrada1.xml

#imagen="----------\n-***-***--\n--*--***--\n--*--*----\n-***-*----\n----------\n-***-***--\n-*-----*--\n-***-***--\n----------"

#---------------ventana principal---------------
VentanaRaiz=Tk()
VentanaRaiz.resizable(FALSE,FALSE)
#---------Metodos para los botones--------------
def Ventana_AbrirArchivoXML():
    RutaArchivo=filedialog.askopenfilename(title="Abrir archivo")
    print(RutaArchivo)  #Muestra la direccion del archivo encontrado
    if RutaArchivo != "":
        print(">> Archivo cargado exitosamente <<\n")
        BotonOperaciones.config(state=NORMAL)
        BotonReportes.config(state=NORMAL)

        leer_guardar_Archivo.CargarArchivoXML(RutaArchivo)
        
    else:
        print("\n!!! ARCHIVO NO SELECCIONADO !!!\n")


#-------Componentes Ventana----------
#---------principales----------
PanelPrincipal=Frame(VentanaRaiz, width=500, height=700, bg="darkred")
PanelPrincipal.pack()

panelImagenes=Frame(VentanaRaiz,width=300, height=200, bg="orange")
panelImagenes.pack()

BotonCargarXML=Button(PanelPrincipal,text="CARGAR ARCHIVO", command=Ventana_AbrirArchivoXML)
BotonCargarXML.grid(row=0, column=0, padx=10, pady=10)

BotonOperaciones=Button(PanelPrincipal,text="Operaciones", state=DISABLED)
BotonOperaciones.grid(row=0, column=1, padx=10, pady=10)

BotonReportes=Button(PanelPrincipal,text="Reportes", state=DISABLED)
BotonReportes.grid(row=0, column=2, padx=10, pady=10)

BotonAyuda=Button(PanelPrincipal,text="Ayuda")
BotonAyuda.grid(row=0, column=3, padx=10, pady=10)

EtiquetaImagen1=Label(panelImagenes, text="aqui iria una imagen", width=30, height=15)
EtiquetaImagen1.grid(row=0, column=0, padx=10, pady=10)

EtiquetaImagen2=Label(panelImagenes, text="aqui iria otra imagen", width=30, height=15)
EtiquetaImagen2.grid(row=0, column=1, padx=10, pady=10)

VentanaRaiz.mainloop()