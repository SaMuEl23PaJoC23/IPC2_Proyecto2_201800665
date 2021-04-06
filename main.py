from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser as wb


from Leer_Guardar_XML import Lectura

leer_guardar_Archivo=Lectura()


#----------------------------------------------------------------
#imagen="----------\n-***-***--\n--*--***--\n--*--*----\n-***-*----\n----------\n-***-***--\n-*-----*--\n-***-***--\n----------"
#---------------ventana principal---------------
VentanaRaiz=Tk()
VentanaRaiz.config(bg="darkred")
VentanaRaiz.geometry("1250x400")
#VentanaRaiz.resizable(FALSE,FALSE)
ListaDatosCbox1=[]
ListaNombresCbox1=[]
ListaCombobox2=[]
TipoOpcion=0

#---------Metodos para los botones--------------
def Ventana_AbrirArchivoXML():
    global ListaDatosCbox1
    global ListaNombresCbox1
    ListaNombresCbox1=[]

    RutaArchivo=filedialog.askopenfilename(title="Abrir archivo")
    print(RutaArchivo)  #Muestra la direccion del archivo encontrado
    if RutaArchivo != "":
        print(">> Archivo cargado exitosamente <<\n")
        BotonOperaciones.config(state=NORMAL)
        BotonReportes.config(state=NORMAL)

        ListaDatosCbox1=leer_guardar_Archivo.CargarArchivoXML(RutaArchivo)

        siguienteNombre=0
        for i in range(int(len(ListaDatosCbox1)/3)):
            ListaNombresCbox1.append(ListaDatosCbox1[siguienteNombre])
            siguienteNombre+=3
        
    else:
        print("\n!!! ARCHIVO NO SELECCIONADO !!!\n")

#------ventana Operaciones------------
def Ventana_ParaOperaciones():
    VentanaOperaciones=Tk()
    VentanaOperaciones.resizable(FALSE,FALSE)
    
    def Operar_unaImagen():
        global ListaDatosCbox1
        global ListaNombresCbox1
        

        bandera=False
        PosDimenciones=1
        while bandera != True:
            if  Combobox1.get()==ListaDatosCbox1[PosDimenciones-1]: #Se busca el nombre seleccionado, para luego mandar sus dimenciones en la siguiente funcion
                if TipoOpcion==1:
                    leer_guardar_Archivo.CargarImagen(1,Combobox1.get(),int(ListaDatosCbox1[PosDimenciones]),int(ListaDatosCbox1[PosDimenciones+1]),0,0,0,0,0)
                    bandera=True
                elif TipoOpcion==2:
                    leer_guardar_Archivo.CargarImagen(2,Combobox1.get(),int(ListaDatosCbox1[PosDimenciones]),int(ListaDatosCbox1[PosDimenciones+1]),0,0,0,0,0)
                    bandera=True
                elif TipoOpcion==3:
                    if ListaDatosCbox1[PosDimenciones]==ListaDatosCbox1[PosDimenciones+1]:
                        leer_guardar_Archivo.CargarImagen(31,Combobox1.get(),int(ListaDatosCbox1[PosDimenciones]),int(ListaDatosCbox1[PosDimenciones+1]),0,0,0,0,0)
                        bandera=True
                    else:
                        ListaNombresCbox1=[]
                        leer_guardar_Archivo.CargarImagen(32,Combobox1.get(),int(ListaDatosCbox1[PosDimenciones]),int(ListaDatosCbox1[PosDimenciones+1]),0,0,0,0,0)
                
                        ListaDatosCbox1=leer_guardar_Archivo.RetornarListaDatosParaCombobox1()
                        print(ListaDatosCbox1)
                        siguienteNombre=0
                        for i in range(int(len(ListaDatosCbox1)/3)):
                            ListaNombresCbox1.append(ListaDatosCbox1[siguienteNombre])
                            siguienteNombre+=3
                        bandera=True

                elif TipoOpcion==4:
                    if CuadroX1.get()=="" or CuadroX2.get()=="" or CuadroY1.get()=="" or CuadroY2=="":
                        AvisoFaltaCoordenada()

                    elif int(CuadroX1.get()) > int(ListaDatosCbox1[PosDimenciones]):
                        messagebox.showinfo("ALERT", "Coordenada -X1- fuera de rango")
                    
                    elif int(CuadroX2.get()) > int(ListaDatosCbox1[PosDimenciones]):
                        messagebox.showinfo("ALERT", "Coordenada -X2- fuera de rango")
                    
                    elif int(CuadroY1.get()) > int(ListaDatosCbox1[PosDimenciones+1]):
                        messagebox.showinfo("ALERT", "Coordenada -Y1- fuera de rango")
                    
                    elif int(CuadroY2.get()) > int(ListaDatosCbox1[PosDimenciones+1]):
                        messagebox.showinfo("ALERT", "Coordenada -Y2- fuera de rango")

                    else:
                        leer_guardar_Archivo.CargarImagen(4,Combobox1.get(),int(ListaDatosCbox1[PosDimenciones]),int(ListaDatosCbox1[PosDimenciones+1]),int(CuadroX1.get()),int(CuadroY1.get()),int(CuadroX2.get()),int(CuadroY2.get()),0)
                        bandera=True

                elif TipoOpcion==5:

                    if CuadroX1.get()=="" or CuadroY1.get()=="":
                        AvisoFaltaCoordenada()

                    elif int(CuadroX1.get()) > int(ListaDatosCbox1[PosDimenciones]):
                        messagebox.showinfo("ALERT", "Coordenada -X1- fuera de rango")
                    
                    elif int(CuadroY1.get()) > int(ListaDatosCbox1[PosDimenciones+1]):
                        messagebox.showinfo("ALERT", "Coordenada -Y1- fuera de rango")

                    else:
                        leer_guardar_Archivo.CargarImagen(5,Combobox1.get(),int(ListaDatosCbox1[PosDimenciones]),int(ListaDatosCbox1[PosDimenciones+1]),int(CuadroX1.get()),int(CuadroY1.get()),0,0,int(CuadroCantElementos.get()))
                        bandera=True

                elif TipoOpcion==6:
                    if CuadroX1.get()=="" or CuadroY1.get()=="":
                        AvisoFaltaCoordenada()

                    elif int(CuadroX1.get()) > int(ListaDatosCbox1[PosDimenciones]):
                        messagebox.showinfo("ALERT", "Coordenada -X1- fuera de rango")
                    
                    elif int(CuadroY1.get()) > int(ListaDatosCbox1[PosDimenciones+1]):
                        messagebox.showinfo("ALERT", "Coordenada -Y1- fuera de rango")

                    else:
                        leer_guardar_Archivo.CargarImagen(6,Combobox1.get(),int(ListaDatosCbox1[PosDimenciones]),int(ListaDatosCbox1[PosDimenciones+1]),int(CuadroX1.get()),int(CuadroY1.get()),0,0,0)
                        bandera=True
                        
                elif TipoOpcion==7:
                    if CuadroX1.get()=="" or CuadroY1.get()=="":
                        AvisoFaltaCoordenada()

                    elif int(CuadroX1.get()) > int(ListaDatosCbox1[PosDimenciones]):
                        messagebox.showinfo("ALERT", "Coordenada -X1- fuera de rango")
                    
                    elif int(CuadroY1.get()) > int(ListaDatosCbox1[PosDimenciones+1]):
                        messagebox.showinfo("ALERT", "Coordenada -Y1- fuera de rango")

                    elif int(CuadroX2.get()) > int(ListaDatosCbox1[PosDimenciones]) or int(CuadroX2.get())+int(CuadroX1.get()) > int(ListaDatosCbox1[PosDimenciones]):
                        messagebox.showinfo("ALERT", "Coordenada -X2- fuera de rango")
                    
                    elif int(CuadroY2.get()) > int(ListaDatosCbox1[PosDimenciones+1]) or int(CuadroY2.get())+int(CuadroY1.get()) > int(ListaDatosCbox1[PosDimenciones+1]):
                        messagebox.showinfo("ALERT", "Coordenada -Y2- fuera de rango")

                    else:
                        leer_guardar_Archivo.CargarImagen(7,Combobox1.get(),int(ListaDatosCbox1[PosDimenciones]),int(ListaDatosCbox1[PosDimenciones+1]),int(CuadroX1.get()),int(CuadroY1.get()),int(CuadroX2.get()),int(CuadroY2.get()),0)
                        bandera=True
                    
                
                elif TipoOpcion==8:
                    if CuadroX1.get()=="" or CuadroY1.get()=="":
                        AvisoFaltaCoordenada()

                    elif int(CuadroX1.get()) > int(ListaDatosCbox1[PosDimenciones]):
                        messagebox.showinfo("ALERT", "Coordenada -X1- fuera de rango")
                    
                    elif int(CuadroY1.get()) > int(ListaDatosCbox1[PosDimenciones+1]):
                        messagebox.showinfo("ALERT", "Coordenada -Y1- fuera de rango")

                    else:
                        leer_guardar_Archivo.CargarImagen(8,Combobox1.get(),int(ListaDatosCbox1[PosDimenciones]),int(ListaDatosCbox1[PosDimenciones+1]),int(CuadroX1.get()),int(CuadroY1.get()),0,0,int(CuadroCantElementos.get()))
                        bandera=True
                    

                else:
                    messagebox.showinfo("ALERT","!! Debe seleccionar una operación !!")
                    break
                if bandera ==True:
                    MostrarResultadoImagen()

                Cancelar1()
            else:
                PosDimenciones+=3
    
    def MostrarImagen():
        bandera=False
        PosDimenciones=1
        while bandera != True:
                
            if  Combobox1.get()==ListaDatosCbox1[PosDimenciones-1]:
                leer_guardar_Archivo.CargarImagen(9,Combobox1.get(),int(ListaDatosCbox1[PosDimenciones]),int(ListaDatosCbox1[PosDimenciones+1]),0,0,0,0,0)
                Imagen_matriz=Image.open(Combobox1.get()+'.dot.png')
                NuevaImagen_matriz=Imagen_matriz.resize((200,200))
                RenderizarImagen=ImageTk.PhotoImage(NuevaImagen_matriz)
                EtiquetaImagenSolo1Matriz=Label(VentanaRaiz, image=RenderizarImagen)
                EtiquetaImagenSolo1Matriz.image=RenderizarImagen
                EtiquetaImagenSolo1Matriz.place(x=10,y=120)
                bandera=True
            else:
                PosDimenciones+=1
    
    def MostrarResultadoImagen():
        bandera=False
        PosDimenciones=1
        while bandera != True:
                
            if  Combobox1.get()==ListaDatosCbox1[PosDimenciones-1]:
                Imagen_matriz=Image.open(Combobox1.get()+'.dot.png')
                NuevaImagen_matriz=Imagen_matriz.resize((200,200))
                RenderizarImagen=ImageTk.PhotoImage(NuevaImagen_matriz)
                EtiquetaImagenResultadoSolo1Matriz=Label(VentanaRaiz, image=RenderizarImagen)
                EtiquetaImagenResultadoSolo1Matriz.image=RenderizarImagen
                EtiquetaImagenResultadoSolo1Matriz.place(x=240,y=120)
                bandera=True
            else:
                PosDimenciones+=1

        
    def Op1():
        global TipoOpcion
        TipoOpcion=1
        bt2.config(state=DISABLED)
        bt3.config(state=DISABLED)
        bt4.config(state=DISABLED)
        bt5.config(state=DISABLED)
        bt6.config(state=DISABLED)
        bt7.config(state=DISABLED)
        bt8.config(state=DISABLED)

    def Op2():
        global TipoOpcion
        TipoOpcion=2
        bt1.config(state=DISABLED)
        bt3.config(state=DISABLED)
        bt4.config(state=DISABLED)
        bt5.config(state=DISABLED)
        bt6.config(state=DISABLED)
        bt7.config(state=DISABLED)
        bt8.config(state=DISABLED)
    
    def Op3():
        global TipoOpcion
        TipoOpcion=3
        bt1.config(state=DISABLED)
        bt2.config(state=DISABLED)
        bt4.config(state=DISABLED)
        bt5.config(state=DISABLED)
        bt6.config(state=DISABLED)
        bt7.config(state=DISABLED)
        bt8.config(state=DISABLED)
    
    def Op4():
        global TipoOpcion
        TipoOpcion=4
        bt1.config(state=DISABLED)
        bt2.config(state=DISABLED)
        bt3.config(state=DISABLED)
        bt5.config(state=DISABLED)
        bt6.config(state=DISABLED)
        bt7.config(state=DISABLED)
        bt8.config(state=DISABLED)
        DesbloquearCoordenadas()
    
    def Op5():
        global TipoOpcion
        TipoOpcion=5
        bt1.config(state=DISABLED)
        bt2.config(state=DISABLED)
        bt3.config(state=DISABLED)
        bt4.config(state=DISABLED)
        bt6.config(state=DISABLED)
        bt7.config(state=DISABLED)
        bt8.config(state=DISABLED)

        CuadroX1.config(state=NORMAL)
        CuadroY1.config(state=NORMAL)
        CuadroCantElementos.config(state=NORMAL)
    
    def Op6():
        global TipoOpcion
        TipoOpcion=6
        bt1.config(state=DISABLED)
        bt2.config(state=DISABLED)
        bt3.config(state=DISABLED)
        bt4.config(state=DISABLED)
        bt5.config(state=DISABLED)
        bt7.config(state=DISABLED)
        bt8.config(state=DISABLED)

        CuadroX1.config(state=NORMAL)
        CuadroY1.config(state=NORMAL)

    def Op7():
        global TipoOpcion
        TipoOpcion=7
        bt1.config(state=DISABLED)
        bt2.config(state=DISABLED)
        bt3.config(state=DISABLED)
        bt4.config(state=DISABLED)
        bt5.config(state=DISABLED)
        bt6.config(state=DISABLED)
        bt8.config(state=DISABLED)
        DesbloquearCoordenadas()

    def Op8():
        global TipoOpcion
        TipoOpcion=8
        bt1.config(state=DISABLED)
        bt2.config(state=DISABLED)
        bt3.config(state=DISABLED)
        bt4.config(state=DISABLED)
        bt5.config(state=DISABLED)
        bt6.config(state=DISABLED)
        bt7.config(state=DISABLED)
        CuadroCantElementos.config(state=NORMAL)
        CuadroX1.config(state=NORMAL)
        CuadroY1.config(state=NORMAL)

    

    def Cancelar1():
        global TipoOpcion
        TipoOpcion=0
        bt1.config(state=NORMAL)
        bt2.config(state=NORMAL)
        bt3.config(state=NORMAL)
        bt4.config(state=NORMAL)
        bt5.config(state=NORMAL)
        bt6.config(state=NORMAL)
        bt7.config(state=NORMAL)
        bt8.config(state=NORMAL)
        BloquearCoordenadas()

    def DesbloquearCoordenadas():
        CuadroX1.config(state=NORMAL)
        CuadroY1.config(state=NORMAL)
        CuadroX2.config(state=NORMAL)
        CuadroY2.config(state=NORMAL)
    
    def BloquearCoordenadas():
        CuadroY2.config(state=DISABLED)
        CuadroX1.config(state=DISABLED)
        CuadroY1.config(state=DISABLED)
        CuadroX2.config(state=DISABLED)
        CuadroCantElementos.config(state=DISABLED)

    def AvisoFaltaCoordenada():
        messagebox.showinfo("ALERT","!! Debe llenar todos los espacios de coordenadas !!")

    #Componentes Ventana Operaciones
    panelMatrices=Frame(VentanaOperaciones,width=300, height=200, bg="darkred")
    panelMatrices.pack(fill="x")

    CuadX1=IntVar()
    CuadX2=IntVar()
    CuadY1=IntVar()
    CuadY2=IntVar()
    CuadCantElementos=IntVar()
    
    #-------componentes para operaciones de una matriz----------
    EtiquetaTituloUnaMatriz=Label(panelMatrices, text="OPERACIONES CON UNA MATRIZ")
    EtiquetaTituloUnaMatriz.grid(row=0, column=0, padx=10, pady=5)

    EtiquetaUnaMatriz=Label(panelMatrices, text="Elija una Matriz:",bg="orange")
    EtiquetaUnaMatriz.grid(row=1, column=0, padx=10, pady=2, sticky="e")

    Combobox1=ttk.Combobox(panelMatrices, value=ListaNombresCbox1, width=10)
    Combobox1.current(0)
    Combobox1.grid(row=1,column=1, padx=10, pady=5)

    etiqueta1=Label(panelMatrices,text="ELIJA UNA OPERACION:",bg="orange").grid(row=2,column=0,sticky="w")
    bt1=Button(panelMatrices,text="Rotación Horizontal",command=Op1, bd=5)
    bt1.grid(row=3,column=0, padx=10,pady=1,sticky="w")
    bt2=Button(panelMatrices,text="Rotación Vertical",command=Op2, bd=5)
    bt2.grid(row=4,column=0, padx=10,pady=1,sticky="w")
    bt3=Button(panelMatrices,text="Transpuesta",command=Op3, bd=5)
    bt3.grid(row=5,column=0, padx=10,pady=1,sticky="w")
    bt4=Button(panelMatrices,text="Limpiar Zona",command=Op4, bd=5)
    bt4.grid(row=6,column=0, padx=10,pady=1,sticky="w")
    bt5=Button(panelMatrices,text="Agregar Línea horizontal",command=Op5, bd=5)
    bt5.grid(row=7,column=0, padx=10,pady=1,sticky="w")
    bt6=Button(panelMatrices,text="Agregar Línea Vertical",command=Op6, bd=5)
    bt6.grid(row=8,column=0, padx=10,pady=1,sticky="w")
    bt7=Button(panelMatrices,text="Rotación Rectángulo",command=Op7, bd=5)
    bt7.grid(row=9,column=0, padx=10,pady=1,sticky="w")
    bt8=Button(panelMatrices,text="Agregar Triángulo Rectángulo",command=Op8, bd=5)
    bt8.grid(row=10,column=0, padx=10,pady=1,sticky="w")

    
    etiqueta1=Label(panelMatrices,text="Imagen:",bg="darkred")
    etiqueta1.grid(row=12,column=0)
    etiqueta1=Label(panelMatrices,text="Resultado:",bg="darkred")
    etiqueta1.grid(row=12,column=2)
    btMostrar1=Button(panelMatrices,text="MOSTRAR",command=MostrarImagen, bd=5,bg="green")
    btMostrar1.grid(row=12,column=3, padx=10,pady=5)    

    BotonOperar1=Button(panelMatrices, text="OPERAR",command=Operar_unaImagen)
    BotonOperar1.grid(row=1,column=2, padx=10, pady=10)

    BotonCancelar=Button(panelMatrices, text="CANCELAR",command=Cancelar1,bg="black",foreground="white")
    BotonCancelar.grid(row=5,column=2, padx=10, pady=10)

    etiquetaMensaje=Label(panelMatrices,text="Inicio Coordenadas")
    etiquetaMensaje.grid(row=6,column=2,sticky="e")
    etiquetaX1=Label(panelMatrices,text="X1=")
    etiquetaX1.grid(row=7,column=2,sticky="e")
    CuadroX1=Entry(panelMatrices,state=DISABLED,width=4,bg="orange",textvariable=CuadX1)
    CuadroX1.grid(row=7,column=3,sticky="w")
    etiquetaY1=Label(panelMatrices,text="Y1=")
    etiquetaY1.grid(row=8,column=2,sticky="e")
    CuadroY1=Entry(panelMatrices,state=DISABLED,width=4,bg="orange",textvariable=CuadY1)
    CuadroY1.grid(row=8,column=3,sticky="w")

    etiquetaMensaje=Label(panelMatrices,text="Fin Coordenadas")
    etiquetaMensaje.grid(row=6,column=4,stick="e")
    etiquetaX2=Label(panelMatrices,text="X2=")
    etiquetaX2.grid(row=7,column=4,sticky="e")
    CuadroX2=Entry(panelMatrices,state=DISABLED,width=4,bg="orange",textvariable=CuadX2)
    CuadroX2.grid(row=7,column=5,sticky="w")
    etiquetaY2=Label(panelMatrices,text="Y2=")
    etiquetaY2.grid(row=8,column=4,sticky="e")
    CuadroY2=Entry(panelMatrices,state=DISABLED,width=4,bg="orange",textvariable=CuadY2)
    CuadroY2.grid(row=8,column=5,sticky="w")

    EtiquetaCantElementos=Label(panelMatrices,text="CANTIDAD ELEMENTOS=")
    EtiquetaCantElementos.grid(row=10,column=2,sticky="e")
    CuadroCantElementos=Entry(panelMatrices,state=DISABLED,width=7,bg="orange",textvariable=CuadCantElementos)
    CuadroCantElementos.grid(row=10,column=3,sticky="w")

    #---------Separacion-----------
    EtiquetaEspacio=Label(panelMatrices, text="                           ", bg="darkred")
    EtiquetaEspacio.grid(row=0, column=3, padx=10, pady=10)

    #-----------Componentes para operaciones de dos matrices-------------
    EtiquetaTituloUnaMatriz=Label(panelMatrices, text="OPERACIONES CON DOS MATRICES")
    EtiquetaTituloUnaMatriz.grid(row=0, column=4, padx=10, pady=10)

    EtiquetaUnaMatriz=Label(panelMatrices, text="Elija una Matriz:")
    EtiquetaUnaMatriz.grid(row=1, column=4, padx=10, pady=10)

    BotonPrueba2=Button(panelMatrices, text="cb 1-para2") #cambiarlo despues por un combobox
    BotonPrueba2.grid(row=1,column=5, padx=10, pady=10)

    EtiquetaUnaMatriz=Label(panelMatrices, text="Elija una Matriz:")
    EtiquetaUnaMatriz.grid(row=2, column=4, padx=10, pady=10)

    BotonPrueba3=Button(panelMatrices, text="cb 2- para2") #cambiarlo despues por un combobox
    BotonPrueba3.grid(row=2,column=5, padx=10, pady=10)

    BotonOperar1=Button(panelMatrices, text="OPERAR")
    BotonOperar1.grid(row=2,column=6, padx=10, pady=10)
    
#---------ayuda---------------
def MostrarArchivo():
    #wb.open_new(r'/[IPC2]Proyecto_2.pdf')
    VentanaAyuda=Tk()

    VentanaAyuda.config(bg="orange")
    VentanaAyuda.geometry("300x200")
    etiqueta2=Label(VentanaAyuda,text="Datos Personales")
    etiqueta2.place(x=10,y=10)
    etiqueta2=Label(VentanaAyuda,text="NOMBRE: Samuel Alejandro Pajoc Raymundo",bg="orange")
    etiqueta2.place(x=10,y=50)

    etiqueta2=Label(VentanaAyuda,text="CARNÉ: 201800665",bg="orange")
    etiqueta2.place(x=10,y=90)

    etiqueta2=Label(VentanaAyuda,text="Ingeniería en Ciencias y Sistemas",bg="orange")
    etiqueta2.place(x=10,y=130)

    etiqueta2=Label(VentanaAyuda,text="4to. Semestre",bg="orange")
    etiqueta2.place(x=10,y=170)
    etiqueta2=Label(VentanaAyuda,text="Laboratirio Introducción a la programación 2",bg="orange")
    etiqueta2.place(x=10,y=210)






#-------Componentes Ventana Principal----------

BotonCargarXML=Button(VentanaRaiz,text="CARGAR ARCHIVO",command=Ventana_AbrirArchivoXML)
BotonCargarXML.place(x=10,y=10)

BotonOperaciones=Button(VentanaRaiz,text="Operaciones",state=DISABLED,command=Ventana_ParaOperaciones)
BotonOperaciones.place(x=125,y=10)

BotonReportes=Button(VentanaRaiz,text="Reportes", state=DISABLED)
BotonReportes.place(x=205,y=10)

BotonAyuda=Button(VentanaRaiz,text="Ayuda",command=MostrarArchivo)
BotonAyuda.place(x=265,y=10)

lb1=Label(VentanaRaiz, text="OPERACIÓNES CON -UNA- IMAGEN:",bg="darkred")
lb1.place(x=120,y=60)

lb1=Label(VentanaRaiz, text="Imagen:")
lb1.place(x=100,y=90)

lb1=Label(VentanaRaiz, text="Resultado:")
lb1.place(x=300,y=90)

EtiquetaImagenSolo1Matriz=Label(VentanaRaiz, text="Esperando una matriz imagen", width=30, height=15)
EtiquetaImagenSolo1Matriz.place(x=10,y=120)

EtiquetaImagenResultadoSolo1Matriz=Label(VentanaRaiz, text="Esperando RESULTADO ", width=30, height=15)
EtiquetaImagenResultadoSolo1Matriz.place(x=240,y=120)

lb1=Label(VentanaRaiz, text="OPERACIÓNES CON -DOS- IMAGENES:",bg="darkred")
lb1.place(x=760,y=60)

lb1=Label(VentanaRaiz, text="Imagen 1:")
lb1.place(x=630,y=90)

lb1=Label(VentanaRaiz, text="Imagen 2:")
lb1.place(x=840,y=90)

lb1=Label(VentanaRaiz, text="Resultado:")
lb1.place(x=1080,y=90)

EtiquetaImagenMatriz1=Label(VentanaRaiz, text="Esperando matriz imagen", width=30, height=15)
EtiquetaImagenMatriz1.place(x=550,y=120)

EtiquetaImagenMatriz2=Label(VentanaRaiz, text="Esperando matriz imagen", width=30, height=15)
EtiquetaImagenMatriz2.place(x=770,y=120)

EtiquetaImagenResultadoMatrices=Label(VentanaRaiz, text="Esperando RESULTADO", width=30, height=15)
EtiquetaImagenResultadoMatrices.place(x=1000,y=120)

VentanaRaiz.mainloop()