from tkinter import *
from tkinter.ttk import *
import time

def bar():
    for i in range(0, 110, 10):  # Increment in steps of 10
        progress['value'] = i
        percentage_label.config(text=f"{i}%")  # Update percentage label
        tk.update_idletasks()
        time.sleep(0.5)

tk = Tk()
tk.title("Progress Bar with Percentage")
tk.geometry("400x200")

progress = Progressbar(tk, orient=HORIZONTAL, length=200, mode='determinate')
progress.pack(pady=20)

percentage_label = Label(tk, text="0%", font=("Arial", 12))  # Label for percentage
percentage_label.pack()

Button(tk, text="Start", command=bar).pack()

tk.mainloop()
