import tkinter as tk

def ocultar():
    etiqueta.pack_forget()

def mostrar():
    etiqueta.pack()

root=tk.Tk()

etiqueta=tk.Label(root, text="Esto es una etiqueta")
etiqueta.pack()

boton_ocultar=tk.Button(root, text="Ocultar etiqueta", command=ocultar)
boton_ocultar.pack()

boton_mostrar=tk.Button(root, text="Mostrar etiqueta", command=mostrar)
boton_mostrar.pack()


root.mainloop()
