import tkinter as tk

root=tk.Tk()
root.title("Hola desde Tkinter")

etiqueta=tk.Label(root, text="Hello again")
etiqueta.pack()

etiqueta.config(font=("Arial",14))
etiqueta.config(bg="lightblue", fg="navy")


root.mainloop()