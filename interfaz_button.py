from tkinter import *


def sumar():
    resp.set(int(var1.get()) + int(var2.get()))

def restar():
    resp.set(int(var1.get()) - int(var2.get()))

root=Tk()
root.title("Ventana Principal")
root.iconbitmap("logo.ico")

frame = Frame(root)
frame.pack()

# Declaramos variables
var1 = StringVar()
var2 = StringVar()
resp = StringVar()

input_1 = Entry(frame)
input_1.pack()
input_1.config(bd=10, font=("Curier, 20"), textvariable=var1)

input_2 = Entry(frame)
input_2.pack()
input_2.config(bd=10, font=("Curier, 20"), textvariable=var2)

input_3 = Entry(frame)
input_3.pack()
input_3.config(bd=10, font=("Curier, 20"), state="disable", textvariable=resp)


btn1 = Button(frame, text= "Sumar")
btn1.pack()
btn1.config(bd=10, font=("Curier, 10"), command=sumar)

btn2 = Button(frame, text= "Restar")
btn2.pack()
btn2.config(bd=10, font=("Curier, 10"), command=restar)


root.mainloop()