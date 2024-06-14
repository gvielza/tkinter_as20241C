import tkinter as tk

def habilitar():
    boton.config(state="normal")

def deshabilitar():
    boton.config(state="disabled")

root=tk.Tk()
boton=tk.Button(root, text="Haz click!", state="disabled")
boton.pack()

boton_habilitar=tk.Button(root, text="Habilitar Botòn ", command=habilitar)
boton_habilitar.pack()

boton_deshabilitar=tk.Button(root, text="Habilitar Botòn ", command=deshabilitar)
boton_deshabilitar.pack()


root.mainloop()