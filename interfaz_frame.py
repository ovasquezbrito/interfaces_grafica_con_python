from tkinter import *

root=Tk()

root.title("Ventana Principal")

root.resizable(1,1)
root.iconbitmap("logo.ico")


miFrame = Frame(root)
miFrame.pack()
miFrame.config(width=400, height=300)
miFrame.config(cursor="pirate")
miFrame.config(bg="red")
miFrame.config(bd="10")
miFrame.config(relief="ridge")

root.config(cursor="boat")
root.config(bg="blue")
root.config(bd="25")
root.config(relief="sunken")

root.mainloop()