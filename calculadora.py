from tkinter import *

ventana = Tk()
ventana.title("Calculadora de propinas")
ventana.geometry("400x400")

strTotal = StringVar()
strTotal.set("$0.00")

def calcular():
    total = float(txtCuenta.get()) + float(txtCuenta.get()) * (float(sclPropina.get()/100.0))
    strTotal.set(str(total))

lblCuenta = Label(ventana, text="Cuenta: ")
lblCuenta.pack()

txtCuenta= Entry(ventana)
txtCuenta.pack()

lblPorcentajePropina = Label(ventana, text="Porcentaje de propinas: ")
lblPorcentajePropina.pack()

sclPropina = Scale(ventana, from_=0, to_=20, orient=HORIZONTAL)
sclPropina.pack()

btnCalcular = Button(ventana, text="Calcular", command=calcular)
btnCalcular.pack()

lblTotalAPagar = Label(ventana, text="Total a pagar: ")
lblTotalAPagar.pack()

lblMontoAPagar = Label(ventana, textvariable=strTotal)
lblMontoAPagar.pack()

ventana.mainloop()