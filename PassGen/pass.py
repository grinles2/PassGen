# импорты

from tkinter import *
from random import choice

# функции
def randomize():
    PassL = e.get() # получаем длину пороля
    e.delete(0, END) # всё с него
    for i in range(int(PassL)):
        e.insert(0, choice(alphabet)) # добавляем пароль в текст поле


def SavePass():
    PassPrefix = "Пароль"
    Pass = e.get() # получить пароль из текст поля
    root.clipboard_clear()
    root.clipboard_append(Pass) # вставить в буфер обмена
    print(Pass)
    with open("password.txt", "a", encoding="UTF-8") as file: # записываем пароль
        file.write(f"{PassPrefix} --->>> {Pass}\n")


root = Tk()
root.title("Генератор Паролей")
root.geometry("400x200")
root.config(bg = "cyan")
root.iconbitmap('logo.ico') # лого
root.resizable(width=False, height=False) # запрет на расширение


alphabet = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "t", "u", "v", "w", "x", "y", "z",
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "j", "K", "L", "M", "N", "O", "P", "Q", "R", "T", "U", "V", "W", "X", "Y", "Z",
            "!", "@", "$", "&", "*", "#", "?"
            ] # словарь

e = Entry(root, font = "Ariel 13") # текстовое поле
e.place(relx= 0.5, y=20, anchor=CENTER)  # координаты текстового поля

btn = Button(root, text="Сгенерировать", font= ("Seymour One", 17, "bold"), command=randomize) # отпровляемся к функц randomize
btn.place(relx=0.5, y=70, anchor= CENTER)

btn = Button(root, text="Сохранить Пароль", font= ("Seymour One", 17, "bold"), command=SavePass) # отпровляемся к функц SavePass
btn.place(relx=0.5, y=120, anchor= CENTER)


root.mainloop()   # показываем окно