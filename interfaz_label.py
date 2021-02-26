from tkinter import *

root=Tk()
 
# Agregar imagen

imagen = PhotoImage(file="carita.gif")

label = Label(root, image=imagen)
label.pack()

"""
#Cambiar el texto dinámicamente 
newText = StringVar()
newText.set("Texto Nuevo Modificado")

root.title("Label")
root.config(width=400, height=300)
root.iconbitmap("logo.ico")

#Primer Método
label = Label(root, text="Hola Mundo")
label.place(x=100, y=50)
label.config(bg="red", fg="white", font=("Curier", 20),textvariable=newText)

#Segundo Método
Label(root, text="Bienvenido").place(x=100, y=100)

"""

root.mainloop()