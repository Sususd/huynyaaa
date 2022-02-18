from tkinter import *
import tkinter as tk
import tkinter.font as tkFont


clicks = 0

#скрипты для нажатия кнопок
def click_button():
        global clicks
        clicks += 1
        window.title("Clicks {}".format(clicks))
        if clicks == 10:
                window.title("A")
        if clicks == -10:
                window.title("F")

def click_b():
        global clicks
        clicks -= 1
        window.title("Clicks {}".format(clicks))
        if clicks == -10:
                window.title("F")
        if clicks == 10:
                window.title("A")

#окно
window = tk.Tk()
window.title("window")
window.geometry("400x400")
#logo = tk.PhotoImage(file = "m.png")

#подключаем текстовый документ
data_file = open("wintxt.txt")
data = data_file.read()         #чтение содержимого файла
data_file.close()
w = tk.Label(window,
	text=data,
	background="#455",      #цвет фона текста
	foreground="#590")      #цвет текста
w.pack()
w.place(x=280, y=305)           #положение текста

#w1 = tk.Label(image=logo)       картинка на фон
#w1.pack()

#кнопки
btn = Button(window,
	text="ok",
	background="#390",  	#фон
	command=click_button,	#активация кнопки
	height=5,		#высота
	width=10)		#ширина
btn.pack()
btn.place(x=195,y=150)		#положение кнопки в окне
btn = Button(window,
	text="no",
	background="#800",
	command=click_b,
	height=5,
        width=10)
btn.pack()
btn.place(x=103,y=150)

window.resizable(False, False)  #заморозка разрешения окна
window["bg"]="gray22"
window.mainloop()
