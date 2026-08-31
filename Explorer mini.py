import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import os   #   Модуль os даёт доступ к функциям операционной системы — то есть позволяет коду взаимодействовать с ОС


curent_path = ""


def choose_directory():
        # Открывает стандартное окно выбора папки (диалог «Обзор папок»).
        # Возвращает путь к выбранной папке как строку, либо пустую строку, если ничего не выбрано.
    folder = fd.askdirectory()

        # Удаляет весь текст, который сейчас находится в поле ввода (entry_field).
        # 0—начало текста, tk.END—конец текста; то есть очищаем всё содержимое.
    # entry_field.delete(0, tk.END)

        # Вставляет в поле ввода путь к выбранной папке (значение переменной folder) в конец строки.
        # tk.END означает позицию «в самый конец текущего текста».
    # entry_field.insert(tk.END, folder)
    open_directory(folder)


def open_directory(path):
    global curent_path
    curent_path = path
    entry_field.delete(0, tk.END)
    entry_field.insert(tk.END, path)
    listbox.delete(0, tk.END)

    try:
        items = sorted(os.listdir(path))
        for item in items:
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                listbox.insert(tk.END, f'📂 {item}')
            else:
                listbox.insert(tk.END, f'📃 {item}')
    except Exception as err:
        mb.showerror("Показывать ошибку", err)


def open_selected(event):
    selection = listbox.curselection()
    name = listbox.get(selection[0])
    name = name[2:]
    full_path = os.path.join(curent_path, name)
    if os.path.isdir(full_path):
        open_directory(full_path)


def go_back():
    global curent_path
    parent_path = os.path.dirname(curent_path)

    if parent_path != curent_path:
        open_directory(parent_path)


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

but = tk.Button(frame, text = "Назад", width=30, height=2, command = go_back)
but.pack()

entry_field = tk.Entry(frame, width=100)
entry_field.config(font='Arial 8', justify='center')
entry_field.pack(pady = 10)

gap_label = tk.Label(frame, height=1)
gap_label.pack()

but = tk.Button(frame, text = "Выбрать папку", width=30, height=2, command = choose_directory)
but.pack()

listbox = tk.Listbox(frame, height=20, width=70, font='Arial 12')
listbox.pack(pady = 10)
listbox.bind("<Double-Button-1>", open_selected)   #   Привязать двойной щелчок левой кнопкой мыши на элементе списка (Listbox) к функции open_selected».










win.mainloop()