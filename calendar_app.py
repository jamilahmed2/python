import tkinter as tk
from tkcalendar import Calendar

root = tk.Tk()
root.title("Calendar Example")

cal = Calendar(root, selectmode="day", year=2025, month=2, day=26)
cal.pack(pady=20)

root.mainloop()
