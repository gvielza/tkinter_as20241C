import tkinter as tk

def mostrar_nombre():
    nombre=entrada.get()
    etiqueta.config(text=f"Hola {nombre}") 

main=tk.Tk()
main.geometry("400x300")

main.title("Mi primera app con tkinter")

etiqueta=tk.Label(main, text="Hola!!!")
boton=tk.Button(main, text="Haz click", command=mostrar_nombre)
entrada=tk.Entry(main)


etiqueta.pack()
entrada.pack()
boton.pack()

main.mainloop()