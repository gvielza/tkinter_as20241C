import tkinter as tk
'''Descripción: Debes crear una aplicación tkinter simple que funcione como una calculadora de propinas.
 La aplicación debe tener una interfaz con un campo de entrada para el monto de la cuenta y botones para calcular
  la propina. Debes usar etiquetas para mostrar los resultados.'''


main = tk.Tk()
main.title("Propinas")
main.geometry("300x200")

def calcular_propina():
    cuenta = float(entry.get())
    propina = cuenta * 0.15
    label_propina.config(text=f"Propina 10%: ${cuenta * 0.1:.2f}\nPropina 15%: ${propina:.2f} \nPropina 20%: ${cuenta * 0.20:.2f}")

label = tk.Label(main, text="Ingresa el monto de la cuenta")
label.pack()

entry = tk.Entry(main)
entry.pack()

label_propina = tk.Label(main, text="")
label_propina.pack()



button = tk.Button(main, text="Calcular propina", command=calcular_propina)
button.pack()

def limpiar():
    entry.delete(0, tk.END)
    label_propina.config(text="")

button=tk.Button(main, text="Limpiar", command=limpiar)
button.pack()



tk.mainloop()