from tkinter import *

root=Tk()
root.title("Ventana Principal")
root.iconbitmap("logo.ico")

frame = Frame(root, width=500, height=400)
frame.pack()

entrada = Entry(frame)
entrada.grid(row=0, column=1)

entrada1 = Entry(frame)
entrada1.grid(row=1, column=1)
entrada1.config(show="*")

label1 = Label(frame, text="Nombre: ")
label1.grid(row=0, column=0, sticky="w", padx=5, pady=5)

label2 = Label(frame, text="Password: ")
label2.grid(row=1, column=0, padx=5, pady=5)

root.mainloop()