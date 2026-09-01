import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog as fd
from tkinter import messagebox as mb


def open_file():
    try:
        path = fd.askopenfilename(title="Выберите один файл")
        if path:
            img = Image.open(path)
            win_width = 500
            win_height = 500
               #   метод изменяет размер изображения так, чтобы оно вписалось в заданные размеры, сохраняя при этом пропорции
            img.thumbnail((win_width, win_height))

            imgtk = ImageTk.PhotoImage(img)   #   ImageTk.PhotoImage() — это класс из библиотеки PIL/Pillow
                                              #   Он принимает объект Image (из PIL) и создаёт объект, который можно использовать в Tkinter
                                              #   Tkinter не умеет работать с PIL-объектами напрямую, нужен этот "переводчик"

            l.config(image=imgtk)             #   Назначает изображение виджету l (Label)
            l.image = imgtk                   #   Сохраняет ссылку на изображение в самом виджете.

    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")


"""   Окно   """
win = tk.Tk()
WIDTH = win.winfo_screenwidth()
HEIGHT = win.winfo_screenheight()
X = 600
Y = 500
win.geometry(f"{X}x{Y}+{WIDTH // 2 - X // 2}+{HEIGHT // 2 - Y // 2 - 20}")


"""   Меню   """
menubar = tk.Menu(win)     # Создаем объект главного меню, который будет содержать все подменю
win.config(menu=menubar)   # Устанавливаем созданное меню как строку меню для окна root

   #   СОЗДАЕМ ПОДМЕНЮ (выпадающее меню)
my_menu = tk.Menu(menubar, tearoff=0)   # Создаем подменю, которое будет привязано к menubar
                                        # tearoff=0 отключает возможность "оторвать" меню от окна (убирает пунктирную линию сверху)

   #   ПРИВЯЗЫВАЕМ ПОДМЕНЮ К ГЛАВНОЙ СТРОКЕ МЕНЮ
menubar.add_cascade(
    label="Меню",   # Название, которое будет отображаться в строке меню
    menu=my_menu)   # Указываем, какое подменю будет открываться при клике на "Меню"

   #   ДОБАВЛЯЕМ КОМАНДЫ В МЕНЮ (основная часть)
   #   Добавляем первую команду
my_menu.add_command(
    label="Открыть файл",   # Текст, который будет отображаться в меню
    command=open_file)      # Функция, которая выполнится при клике

   #   Добавляем вторую команду
my_menu.add_command(
    label="Закрыть файл",   # Текст пункта меню
    command=win.destroy)    # Действие при клике


"""   Метка для фотографии   """
l = tk.Label(win)
l.pack(pady = 10)


win.mainloop()