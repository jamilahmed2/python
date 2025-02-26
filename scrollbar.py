import tkinter as tk

root = tk.Tk()
root.title("Scrollbar Example")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, height=5, width=30)
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)

for i in range(1, 51):  # Adding multiple items
    listbox.insert(tk.END, f"Item {i}")

root.mainloop()
