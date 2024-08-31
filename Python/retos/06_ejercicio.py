import tkinter
import time
ventana = tkinter.Tk()
ventana.title('Reloj digital')
ventana.geometry("300x200")

imagen_fondo = tkinter.PhotoImage(file="log_nombre.png")  # Reemplaza "fondo.png" con la ruta de tu imagen

# Crea un label para la imagen de fondo
label_fondo = tkinter.Label(ventana, image=imagen_fondo)
label_fondo.place(x=0, y=0, width=1, height=1)



def actualizar_reloj():
    hora_actual = time.strftime("%H:%M:%S")
    etiqueta.config(text=hora_actual)
    etiqueta.after(1000, actualizar_reloj)


etiqueta = tkinter.Label(ventana, font=("arial", 50) , fg="black")
etiqueta.pack(anchor="center")

actualizar_reloj()

ventana.mainloop()

'''ventana.geometry("500x400") # Para las dimensiones de la ventana. 

etiqueta = tkinter.Label(ventana, text = "Hola mundo!", bg = "Gray") # Para crear una etiqueta en nuestra ventana (titulo)
etiqueta.pack(fill = tkinter.X) # Para llevar la etiqueta a la ventana

def saludo_botón(nombre):
    print("Hola " + nombre)

botón_aceptar = tkinter.Button(ventana, text = "Aceptar", command = lambda: saludo_botón("Python"))
botón_aceptar.pack()

caja_texto = tkinter.Entry(ventana)
caja_texto.pack()

ventana.mainloop()'''



