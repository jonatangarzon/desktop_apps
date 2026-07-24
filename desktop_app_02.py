from cProfile import label
from tkinter import *
from tkinter import messagebox

# ------------------------------------------
# Funciones de la app
#-------------------------------------------
def salir():
    messagebox.showinfo("Suma 1.0", "Hiso clic en el boton salir...")
    ventana_principal.destroy()

def borar():
    messagebox.showinfo("Suma 1.0 los datos seran borrados...")
    x.set("")
    y.set("")
    t_resultados.delete("1.0", "end")
    
def sumar():
    messagebox.showinfo(" suma 1,0","hizo clik en el boton de sumar...")
    z = int(x.get()) + int(y.get()) 
    t_resultados.insert(INSERT, " la suma de " + x.get() + " + " + y.get() + "casi siempre es " + str(z) + "\n")



#---------------------------------------    
# configuración de la pantalla principal
#--------------------------


# Ventana principal de la desktop app
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Sistemas Guanentá")

# tamaño de la ventana 
ventana_principal.geometry("500x500")

# color de fondo a la ventana
ventana_principal.config(bg="black")

# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#---------------------------------
# variables globales de la app
# ---------------------------------
x = IntVar()
y = IntVar()

# ------------------------------------------
# Frame entrada de datos
# ------------------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="green", width=480, height=240)
frame_entrada.place(x=10,y=10)

# Agregamos una imagen al frame
escudo = PhotoImage(file="img/escudoColegio.png")
lb_escudo = Label(frame_entrada, image=escudo)
lb_escudo.place(x=10, y=20)

# labbel para titulo de app
titulo = Label(frame_entrada, text="Suma de Números Enteros")
titulo.config(bg="yellow", fg="blue", font=("ARIAL",16))
titulo.place(x=185, y=5) 

# labbel para titulo de app
lb_x= Label(frame_entrada, text="x =")                                                                                                 
lb_x.config(bg="yellow", fg="blue", font=("ARIAL",16))                          
lb_x.place(x=180, y=80)                                                                                                         

lb_y= Label(frame_entrada, text="y =")
lb_y.config(bg="yellow", fg="blue", font=("ARIAL",16)) 
lb_y.place(x=180, y=120)


# Entrada para el valor de X
entry_x = Entry(frame_entrada, textvariable=X)
entry_x.config(bg="white", fg="black", font=("ARIAL",16))
entry_x.focus_set()
entry_x.place(x=330, y=80, width=40, height=30)                        

# Entrada para el valor de y
entry_y = Entry(frame_entrada, textvariable=Y)
entry_y.config(bg="white", fg="black", font=("ARIAL",16))
entry_y.focus_set()
entry_y.place(x=330, y=120, width=40, height=30)



# ------------------------------------------
# Frame operaciones
# ------------------------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="green", width=480, height=120)
frame_operaciones.place(x=10,y=260)

# boton para sumar
bt_sumar = Button(frame_operaciones, text="Sumar", command=sumar)
bt_sumar.place(x=45,y =45, width=100, height=30)

# boton para borrar
bt_borrar = Button(frame_operaciones, text="Borrar", command=borar)
bt_borrar.place(x=190,y =45, width=100, height=30)

# boton para salir
bt_salir = Button(frame_operaciones, text="Salir", command=salir)
bt_salir.place(x=330,y =45, width=100, height=30)



# ------------------------------------------
# Frame resultados
# ------------------------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="green", width=480, height=100)
frame_resultados.place(x=10,y=390)

# area de texto para mostrar resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="yellow", fg="black", font=("ARIAL",20))
t_resultados.place(x=10, y=10, width=460, height=80)

# bucle principal
ventana_principal.mainloop()  