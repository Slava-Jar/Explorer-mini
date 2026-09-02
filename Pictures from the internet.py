import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog as fd, Button
from tkinter import messagebox as mb
import requests
from io import BytesIO
from tkinter import ttk


def load_pokemon():

    number = sb.get()

    url = f"https://pokeapi.co/api/v2/pokemon/{number}"

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print(f"Имя {data['name']}")
    print(f"Рост {data['height']}")
    print(f"Вес {data['weight']}")
    print(f"Опыт {data['base_experience']}")

    img_url = data['sprites']['other']['official-artwork']['front_default']

    response = requests.get(img_url)
    response.raise_for_status()

    img = Image.open(BytesIO(response.content))
    img.thumbnail((500, 500))

    imgtk = ImageTk.PhotoImage(img)
    l.configure(image=imgtk)
    l.image = imgtk


def start_loading():
    pb.start(10)
    b.config(state='disabled')
    win.after(2000, load_pokemon)


"""   Окно   """
win = tk.Tk()
WIDTH = win.winfo_screenwidth()
HEIGHT = win.winfo_screenheight()
X = 600
Y = 700
win.geometry(f"{X}x{Y}+{WIDTH // 2 - X // 2}+{HEIGHT // 2 - Y // 2 - 20}")

"""   Кнопка   """
b = Button(win, text = 'Получить покемона', command = start_loading)
b.pack(pady = 10)


sb = ttk.Spinbox(win, from_ = 1, to = 1025, width = 30)
sb.pack(pady = 10)


"""   Метка для фотографии   """
l = ttk.Label(win)
l.pack(pady = 10)


pb = ttk.Progressbar(win, mode = 'indeterminate', length = 200)
pb.pack(pady = 10)

win.mainloop()


