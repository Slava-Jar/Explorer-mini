import tkinter as tk

win = tk.Tk()

WIDTH = win.winfo_screenwidth()
HEIGHT = win.winfo_screenheight()
X = 700
Y = 500
#   размер и расположение окна в центре экрана"{ширина}x{высота}+{смещение_X}+{смещение_Y}" (через плюс, без запятых).
win.geometry(f"{X}x{Y}+{WIDTH // 2 - X // 2}+{HEIGHT // 2 - Y // 2 - 20}")
win.title('Мини проводник')
frame = tk.Frame(win)
frame.pack(pady = 10)

entry_field = tk.Entry(frame, width=50)
entry_field.config(font='Arial 15', justify='center')
entry_field.pack(pady = 10)

gap_label = tk.Label(frame, height=1)
gap_label.pack()

but = tk.Button(frame, text = "Выбрать папку", width=30, height=2)
but.pack()

listbox = tk.Listbox(frame, height=20, width=95)
listbox.pack(pady = 10)











win.mainloop()