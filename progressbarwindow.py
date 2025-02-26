from tkinter import *
from tkinter.ttk import *
import time

def bar():
    for i in range(0, 110, 10):  # Increment in steps of 10
        progress['value'] = i
        tk.update_idletasks()
        time.sleep(0.5)
    open_new_window()

def open_new_window():
    new_window = Toplevel(tk)
    new_window.title("New Window")
    new_window.geometry("300x200")
    Label(new_window, text="Progress Complete!", font=("Arial", 14)).pack(pady=20)

tk = Tk()
tk.title("Progress Bar Example")
tk.geometry("400x200")

progress = Progressbar(tk, orient=HORIZONTAL, length=200, mode='determinate')
progress.pack(pady=20)

Button(tk, text="Start", command=bar).pack()

tk.mainloop()
