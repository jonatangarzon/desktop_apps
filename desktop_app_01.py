from tkinter import *

# ventana principal de la desktop app
ventana_principal = Tk()

# titulo de la ventana 
ventana_principal.title("sistemas guanenta")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# color de fondo de la ventana 
ventana_principal.config(bg="red")

# deshavilitar boton de maximisar
ventana_principal.resizable(0,0)

# agregamos un objeto tipo Frame sobre la ventana 
Frame_1 = Frame(ventana_principal)
Frame_1.config(bg="blue", width=480, height=240 ) 
Frame_1.place(x=10,y=10)

# Agregamos una imagen al frame
escudo = PhotoImage(file="img/escudoColegio.png")
lb_escudo = Label(Frame_1, image=escudo)
lb_escudo.place(x=10, y=20)

# bucle principal 
ventana_principal.mainloop()
