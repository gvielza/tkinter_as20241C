import tkinter as tk

root=tk.Tk()
root.geometry("200x80")
label1=tk.Label(root, text="Nombre: ")
label2=tk.Label(root, text="Contraseña: ")

entry1=tk.Entry(root)
entry2=tk.Entry(root, show="**")

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

root.mainloop()






root.mainloop()