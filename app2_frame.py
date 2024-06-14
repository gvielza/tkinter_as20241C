import tkinter as tk

root=tk.Tk()
root.title("Hola desde Tkinter")

frame1=tk.Frame(root,borderwidth=2,relief="groove")
frame1.pack(side="left",padx=10, pady=10)

frame2=tk.Frame(root,borderwidth=2,relief="groove")
frame2.pack(side="left",padx=10, pady=10)

label1=tk.Label(frame1, text="Frame 1")
label1.pack()

label2=tk.Label(frame1, text="Frame 2")
label2.pack()


root.mainloop()