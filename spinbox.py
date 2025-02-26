import tkinter as tk

root = tk.Tk()
root.title("Spinbox Example")

tk.Label(root, text="Select a number:").pack(pady=5)

spinbox = tk.Spinbox(root, from_=1, to=10)
spinbox.pack(pady=10)

root.mainloop()
