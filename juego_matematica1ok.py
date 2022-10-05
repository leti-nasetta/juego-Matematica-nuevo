from tkinter import *
from tkinter import Frame
from tkinter import Toplevel
from tkinter import messagebox

ventana = Tk()
ventana.title("ADIVINO TU NUMERO") 
width= ventana.winfo_screenwidth() 
height= ventana.winfo_screenheight() 
ventana.geometry("%dx%d" % (width, height))
ventana.resizable(width=False, height=False)
ventana.configure(bg="black")
imagen=PhotoImage(file="fondoTkinter1.png")
background =Label(ventana,image = imagen)
background.place(x=0, y=0, relwidth=1, relheight=1)


def finalizar():
    ventana = Tk()
    ventana.title("ADIVINO TU NUMERO") 
    width= ventana.winfo_screenwidth() 
    height= ventana.winfo_screenheight() 
    ventana.geometry("%dx%d" % (width, height))
    ventana.resizable(width=False, height=False)
    ventana.configure(bg="black")
    etiqInicio= Label(ventana,width = 45, height= 2, borderwidth = 10,relief="groove", text = "¡COMENCEMOS!",anchor= 'center',font= ("Comic Sans MS",30), bg ="magenta2" )
    etiqInicio.place(x=100, y= 100)
    etiqJugar = Label(ventana,width = 45, height= 2, borderwidth = 10,relief="groove", text = "Para empezar, pulsa el botón de JUGAR",anchor= 'center',font= ("Comic Sans MS",30), bg ="magenta2" )
    etiqJugar.place(x=100, y= 300)
    boton_jugar = Button(ventana, command = sigVentana, borderwidth=10, text = " JUGAR ", width = 10,font = ("Comic Sans MS",30),  bg = "#66FFFF",relief="groove")
    boton_jugar.place(x=500, y= 500)

    
def sigVentana():
    ventana.withdraw() 
    ventana2 = Toplevel() 
    width= ventana2.winfo_screenwidth()
    height= ventana2.winfo_screenheight()
    ventana2.geometry("%dx%d" % (width, height))
    ventana2.resizable(width=False, height=False)
    ventana2.config(bg="black")
    

    def español():
        ventana2.withdraw() 
        ventana3Es = Toplevel() 
        width= ventana3Es.winfo_screenwidth()
        height= ventana3Es.winfo_screenheight()
        ventana3Es.geometry("%dx%d" % (width, height))
        ventana3Es.resizable(width=False, height=False)
        ventana3Es.config(bg="black")
        
        resta = IntVar(value="")
        suma = IntVar(value="")
        def clear():
            suma.set("")
            resta.set("")
        def validar():
            try:
                valor1= suma.get()
                valor2= resta.get()
                return True
            except:
                messagebox.showwarning("Error","Debe ingresar dos valores numericos")
                clear()
                return False
                
                
        
        def seguirEs():
            if validar():
                ventana3Es.withdraw() 
                ventana4Es = Toplevel() 
                width= ventana4Es.winfo_screenwidth()
                height= ventana4Es.winfo_screenheight()
                ventana4Es.geometry("%dx%d" % (width, height))
                ventana4Es.resizable(width=False, height=False)
                ventana4Es.config(bg="black")
        
            def resAdivinado(): 
                digito1=(int(suma.get() + (resta.get()))/2)
                digito2=(int(suma.get() - (resta.get()))/2)
                var= int(digito1),int(digito2)
                return resultado.set(var)
                

            etiqNumAdivinadoEs=Label(ventana4Es,width = 45, height= 3, borderwidth = 10,relief="ridge", text = "El número que pensaste es : ",anchor= 'center',font= ("Comic Sans MS",30), bg ="#66FFFF" )
            etiqNumAdivinadoEs.place(x=100, y= 20)
            botonMostrar=Button(ventana4Es,command=resAdivinado,width=15, height=2,text="Mostrar Número",relief="ridge", borderwidth = 10,font= ("Comic Sans MS",30), bg ="#66FFFF")
            botonMostrar.place(x=450,y=450)
            digito1=IntVar()
            digito2=IntVar()
            resultado=IntVar(value="")
            numAdivinadoEs=Label(ventana4Es, width=10,height= 2, borderwidth=10, textvariable= resultado,relief="ridge",font= ("Comic Sans MS bold",50), bg ="magenta2")
            numAdivinadoEs.place(x=450,y=250)
            botonFinalizar=Button(ventana4Es, command=finalizar,width=20, height=1,text="FINALIZAR", borderwidth = 10,font= ("Comic Sans MS",20), bg ="tomato" )
            botonFinalizar.place(x=900,y=500)

           
        etiqEspañol= Label(ventana3Es,width = 45, height= 1, borderwidth = 10,relief="ridge", text = " Pensá un número de dos dígitos que no se repitan entre sí ",anchor= 'center',font= ("Comic Sans MS",30), bg ="#66FFFF" )
        etiqEspañol.place(x=100, y= 50)
        etiqNumSuma=Label(ventana3Es,width = 45, height= 1, borderwidth = 10,relief="ridge", text = " Ahora sumá los dos dígitos ",anchor= 'center',font= ("Comic Sans MS",30), bg ="#66FFFF" )
        etiqNumSuma.place(x=100, y= 150)
        etiqIngSuma = Label(ventana3Es,width = 20, height= 1, borderwidth = 10,relief="ridge", text = "Escribí el resultado aquí:",anchor= 'center',font= ("Comic Sans MS",28), bg ="#66FFFF" )
        etiqIngSuma.place(x=100, y= 250)
        suma = IntVar(value="")
        resSuma = Entry(ventana3Es, justify= "left",width=20, borderwidth = 10,textvariable=suma, font= ("Comic Sans MS",30),bg = "tomato")
        resSuma.place(x = 700 , y =250)
        etiqNumResta=Label(ventana3Es,width = 45, height= 1, borderwidth = 10,relief="ridge", text = " Ahora restá los dos dígitos ",anchor= 'center',font= ("Comic Sans MS",30), bg ="#66FFFF" )
        etiqNumResta.place(x=100, y= 350)
        etiqIngResta = Label(ventana3Es,width = 20, height= 1, borderwidth = 10,relief="ridge", text = "Escribí el resultado aquí:",anchor= 'center',font= ("Comic Sans MS",28), bg ="#66FFFF" )
        etiqIngResta.place(x=100, y= 450)
        resta = IntVar(value="")
        resResta = Entry(ventana3Es, justify= "left",width=20, borderwidth = 10,textvariable=resta, font= ("Comic Sans MS",30),bg = "tomato")
        resResta.place(x = 700 , y =450)
        botonContinuar = Button(ventana3Es, borderwidth = 10,command = seguirEs, text = " CONTINUAR ", width = 10,font = ("Comic Sans MS",30),  bg = "#66FFFF")
        botonContinuar.place(x=500, y= 550)

     


    def ingles():
        ventana2.withdraw() 
        ventana3In = Toplevel() 
        width= ventana3In.winfo_screenwidth()
        height= ventana3In.winfo_screenheight()
        ventana3In.geometry("%dx%d" % (width, height))
        ventana3In.resizable(width=False, height=False)
        ventana3In.config(bg="black")


        restaIn = IntVar(value="")
        sumaIn = IntVar(value="")
        def clearIn():
            sumaIn.set("")
            restaIn.set("")
        def validar():
            try:
                valor1= sumaIn.get()
                valor2= restaIn.get()
                return True
            except:
                messagebox.showwarning("Error","You must enter numerical values")
                clearIn()
                return False  

        def seguirIng():
            if validar():
                ventana3In.withdraw() 
                ventana4In = Toplevel() 
                width= ventana4In.winfo_screenwidth()
                height= ventana4In.winfo_screenheight()
                ventana4In.geometry("%dx%d" % (width, height))
                ventana4In.resizable(width=False, height=False)
                ventana4In.config(bg="black")

            def resAdivinadoIn(): 
                digito1In=(int(sumaIn.get() + (restaIn.get()))/2)
                digito2In=(int(sumaIn.get() - (restaIn.get()))/2)
                varIn= int(digito1In),int(digito2In)
                return resultadoIn.set(varIn)
                

            etiqNumAdivinadoIn=Label(ventana4In,width = 45, height= 3, borderwidth = 10,relief="ridge", text = "The number you thought of is : ",anchor= 'center',font= ("Comic Sans MS",30), bg ="#66FFFF" )
            etiqNumAdivinadoIn.place(x=100, y= 20)
            botonMostrarIn=Button(ventana4In,command=resAdivinadoIn,width = 15,relief="ridge", height= 2,text=" Show Number", borderwidth = 10,font= ("Comic Sans MS",30), bg ="#66FFFF")
            botonMostrarIn.place(x=450,y=450)
            digitoIn=IntVar()
            digito2In=IntVar()
            resultadoIn=IntVar(value="")
            numAdivinadoIn=Label(ventana4In, width=10,height= 2,borderwidth=10,relief="ridge", textvariable= resultadoIn,font= ("Comic Sans MS bold",50), bg ="tomato")
            numAdivinadoIn.place(x=450,y=250)
            botonFinalizarIn=Button(ventana4In, command=finalizar,width=20, height=1,text="FINISH", borderwidth = 10,font= ("Comic Sans MS",20), bg ="tomato" )
            botonFinalizarIn.place(x=900,y=500)

        etiqIngles= Label(ventana3In,width = 45, height= 1, borderwidth = 10,relief="ridge", text = " Think of a two-digit number (not repeating each other). ",anchor= 'center',font= ("Comic Sans MS",30), bg ="#66FFFF" )
        etiqIngles.place(x=100, y= 50)
        etiqNumSumaIn=Label(ventana3In,width = 45, height= 1, borderwidth = 10,relief="ridge", text = " Now add the two digits ",anchor= 'center',font= ("Comic Sans MS",30), bg ="#66FFFF" )
        etiqNumSumaIn.place(x=100, y= 150)
        etiqIngSumaIn = Label(ventana3In,width = 20, height= 1, borderwidth = 10,relief="ridge", text = "Write the result here:",anchor= 'center',font= ("Comic Sans MS",28), bg ="#66FFFF" )
        etiqIngSumaIn.place(x=100, y= 250)
        sumaIn = IntVar(value="")
        resSumaIn = Entry(ventana3In, justify= "left",width=20, borderwidth = 10,textvariable=sumaIn, font= ("Comic Sans MS",30),bg = "tomato")
        resSumaIn.place(x = 700 , y =250)
        etiqNumRestaIn=Label(ventana3In,width = 45, height= 1, borderwidth = 10,relief="ridge", text = "Now subtract the two digits ",anchor= 'center',font= ("Comic Sans MS",30), bg ="#66FFFF" )
        etiqNumRestaIn.place(x=100, y= 350)
        etiqIngRestaIn = Label(ventana3In,width = 20, height= 1, borderwidth = 10,relief="ridge", text = "Write the result here:",anchor= 'center',font= ("Comic Sans MS",28), bg ="#66FFFF" )
        etiqIngRestaIn.place(x=100, y= 450)
        restaIn = IntVar(value="")
        resRestaIn = Entry(ventana3In, justify= "left",width=20, borderwidth = 10,textvariable=restaIn, font= ("Comic Sans MS",30),bg = "tomato")
        resRestaIn.place(x = 700 , y =450)
        botonContinuarIn = Button(ventana3In, borderwidth = 10,command = seguirIng, text = " CONTINUE ", width = 10,font = ("Comic Sans MS",30),  bg = "#66FFFF")
        botonContinuarIn.place(x=500, y= 550)

       

    etSelIdioma = Label(ventana2,width = 45, height= 2, borderwidth = 4,relief="ridge", text = "Selecciona el idioma ",anchor= 'center',font= ("Comic Sans MS",30), bg ="magenta2" )
    etSelIdioma.place(x=100, y= 150)
    boton_ingles = Button(ventana2, command = ingles, text = " INGLES ",borderwidth=10, width = 10,font = ("Comic Sans MS",30),  bg = "#66FFFF")
    boton_ingles.place(x=800, y= 400)
    boton_spanish = Button(ventana2, command = español, text = " ESPAÑOL ",borderwidth=10, width = 10,font = ("Comic Sans MS",30),  bg = "#66FFFF")
    boton_spanish.place(x=200, y= 400)
    ventana2.mainloop()


etiqInicio= Label(ventana,width = 45, height= 2, borderwidth = 10,relief="groove", text = "¡COMENCEMOS!",anchor= 'center',font= ("Comic Sans MS",30), bg ="magenta2" )
etiqInicio.place(x=100, y= 100)
etiqJugar = Label(ventana,width = 45, height= 2, borderwidth = 10,relief="groove", text = "Para empezar, pulsa el botón de JUGAR",anchor= 'center',font= ("Comic Sans MS",30), bg ="magenta2" )
etiqJugar.place(x=100, y= 300)
boton_jugar = Button(ventana, command = sigVentana, borderwidth=10, text = " JUGAR ", width = 10,font = ("Comic Sans MS",30),  bg = "#66FFFF",relief="groove")
boton_jugar.place(x=500, y= 500)
ventana.mainloop()