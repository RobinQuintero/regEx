from tkinter import *
import re


ventana = Tk()
ventana.title('Evaluar expresión')
ventana.geometry('600x150')

expresion = StringVar()
frase = StringVar()
imprimir = StringVar()

frame1 = Frame(ventana)
frame1.pack()

label1 = Label(frame1, text="Expresión regular: ")
label1.grid(row=1, column=1)

entrada1 = Entry(frame1, textvariable=expresion, width="60")
entrada1.grid(row=1, column=2)

label2 = Label(frame1, text="Frase: ")
label2.grid(row=2, column=1)

entrada2 = Entry(frame1, textvariable=frase, width="60")
entrada2.grid(row=2, column=2)

respuesta = Label(frame1, text="")
respuesta.grid(row=6, column=2)

def evaluar(expresion, frase):
    global respuesta
    resultado = ""
    regex = re.compile(expresion)
    if(regex.search(frase)):
        resultado = regex.search(frase).group(0)
    if(resultado == frase):
        if(expresion==""):
            respuesta.config(text="La expresión regular está vacía")
        else:
            respuesta.config(text="La frase es válida")
    else:
        respuesta.config(text="La frase no es válida")

boton = Button(frame1, text="Evaluar", command=lambda:evaluar(expresion.get(), frase.get()))
boton.grid(row=3, column=2)
ventana.mainloop()