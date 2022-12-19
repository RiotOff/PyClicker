### PyClicker [BETA 1.0]

from tkinter import * # Модуль

root = Tk() # Переменная

root['bg'] = '#fafafa' # Бэкграунд
root.title('PyClicker [BETA 1.0]') # Тайтл программы
root.geometry('500x500') # Размер окна программы
root.resizable(width=False, height=False) # Строка, непозволяющая изменять размеры программы

click = Button(text='КЛИК!', width = '100', height = '100') # Кнопка
click.pack() # Строка, заставляющая работать кнопку

root.mainloop() # Запуск