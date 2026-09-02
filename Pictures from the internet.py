import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog as fd, Button
from tkinter import messagebox as mb
import requests

def load_pokemon():
    url = f'https://pokeapi.co/api/v2/pokemon/10'
    response = requests.get(url)
    response.raise_for_status_code()


"""   Окно   """
win = tk.Tk()
WIDTH = win.winfo_screenwidth()
HEIGHT = win.winfo_screenheight()
X = 600
Y = 500
win.geometry(f"{X}x{Y}+{WIDTH // 2 - X // 2}+{HEIGHT // 2 - Y // 2 - 20}")

"""   Кнопка   """
b = Button(win, text = 'Получить покемона', command = load_pokemon)
b.pack(pady = 10)


"""   Метка для фотографии   """
l = tk.Label(win)
l.pack(pady = 10)


win.mainloop()