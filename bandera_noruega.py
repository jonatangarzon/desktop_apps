from tkinter import *

# ventana principal de la desktop app
ventana_principal = Tk()

# titulo de la ventana 
ventana_principal.title("sistemas guanenta")

# tamaño de la ventana
ventana_principal.geometry("1000x700")

# color de fondo de la ventana 
ventana_principal.config(bg="white")

# deshavilitar boton de maximisar
ventana_principal.resizable(0,0)

# agregamos un objeto tipo Frame sobre la ventana 
Frame_1 = Frame(ventana_principal)
Frame_1.config(bg="red", width=350, height=300 ) 
Frame_1.place(x=0,y=0) 

# agregamos un objeto tipo Frame sobre la ventana 
Frame_2 = Frame(ventana_principal)
Frame_2.config(bg="red", width=550, height=500 ) 
Frame_2.place(x=550,y =450) 

# agregamos un objeto tipo Frame sobre la ventana 
Frame_3 = Frame(ventana_principal)
Frame_3.config(bg="red", width=350, height=300 ) 
Frame_3.place(x=0,y =450) 

# agregamos un objeto tipo Frame sobre la ventana 
Frame_4 = Frame(ventana_principal)
Frame_4.config(bg="red", width=450, height=300 ) 
Frame_4.place(x=550,y =0) 

# agregamos un objeto tipo Frame sobre la ventana 
Frame_1 = Frame(ventana_principal)
Frame_1.config(bg="blue", width=100, height=700 ) 
Frame_1.place(x=401,y =0) 

# agregamos un objeto tipo Frame sobre la ventana 
Frame_1 = Frame(ventana_principal)
Frame_1.config(bg="blue", width=1000, height=70 ) 
Frame_1.place(x=0,y =341) 

# bucle principal 
ventana_principal.mainloop()