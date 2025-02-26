import tkinter as tk

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("300x200")
    tk.Label(new_window, text="This is a top-level window").pack(pady=20)

root = tk.Tk()
root.title("Main Window")

tk.Button(root, text="Open Window", command=open_new_window).pack(pady=20)

root.mainloop()
