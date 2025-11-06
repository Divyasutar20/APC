import tkinter as tk
from tkinter import messagebox
def show_message():
    messagebox.showinfo("Hello", "This is a Tkinter message box!")
root = tk.Tk()
root.title("Tkinter Example")

button = tk.Button(root, text="Click Me", command=show_message)
button.config(font=("Arial", 16), bg="lightblue", fg="black")
button.pack(pady=20)
button2 = tk.Button(root, text="Exit", command=root.quit)
button2.config(font=("Arial", 16), bg="lightcoral", fg="black")
button2.pack(pady=20)

root.mainloop()
