from tkinter import *
from tkinter import messagebox

# ventana principal de la desktop app
ventana_principal = Tk()

# titulo de la ventana 
ventana_principal.title("sistemas guanenta")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# color de fondo de la ventana 
ventana_principal.config(bg="black")

# deshavilitar boton de maximisar
ventana_principal.resizable(0,0)

# ----------------------------------------------
# Frame entrada de datos
# ----------------------------------------------
Frame_entrada = Frame(ventana_principal)
Frame_entrada.config(bg="blue", width=480, height=240 ) 
Frame_entrada.place(x=10,y=10)

# Agregamos una imagen al frame
escudo = PhotoImage(file="img/escudoColegio.png")
lb_escudo = Label(Frame_entrada, image=escudo)
lb_escudo.place(x=10, y=20) 

# ----------------------------------------------
# Frame operaciones
# ---------------------------------------------- 
Frame_operaciones = Frame(ventana_principal)
Frame_operaciones.config(bg="red", width=480, height=240 ) 
Frame_operaciones.place(x=10,y=10)

# ----------------------------------------------
# Frame resultados
# ---------------------------------------------- 
Frame_resultados = Frame(ventana_principal)
Frame_resultados.config(bg="red", width=480, height=240 ) 
Frame_resultados.place(x=10,y=10)

# bucle principal 
ventana_principal.mainloop()