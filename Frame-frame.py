import tkinter 


ventana = tkinter.Tk()
ventana.title("Ventana con Frames")


frame1 = tkinter.Frame( bg="lightblue", width=200, height=100)
frame2 = tkinter.Frame( bg="lightgreen", width=200, height=100)
frame3 = tkinter.Frame( bg="lightyellow", width=200, height=100)
frame4 = tkinter.Frame( bg="lightcoral", width=200, height=100)

# Posicionar los frames en la ventana
frame1.grid(row=0, column=0, padx=5, pady=5)   #Con grid podemos ajustar filas y columnas (row, column), padx es el espacio entre cada frame horizontalmente y pady veticalmente 
frame2.grid(row=0, column=1, padx=5, pady=5)
frame3.grid(row=1, column=0, padx=5, pady=5)
frame4.grid(row=1, column=1, padx=5, pady=5)


button1 = tkinter.Button(frame3, text="Botón 1")
label1 = tkinter.Label(frame3, text="Etiqueta 1")
button1.pack(side="left", padx=10, pady=10)  #con side y un operador que puede ser top left o right, indicamos donde debe posicionarse dentro del frame
label1.pack(side="right", padx=10, pady=10)


button2 = tkinter.Button(frame4, text="Botón 2")
label2 = tkinter.Label(frame4, text="Etiqueta 2")
button2.pack(pady=5)
label2.pack(pady=5)

ventana.mainloop()

#hola