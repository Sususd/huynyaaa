from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
import sys
import time

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


def timing():
    current_time = time.strftime("%H : %M : %S")
    clock.config(text=current_time)
    clock.after(200,timing)

#окно
window = tk.Tk()
window.title("window")
window.geometry("380x380")
#logo = tk.PhotoImage(file = "m.png")

clock=Label(window,font=("times",60,"bold"),background="#455",foreground="#590")
clock.pack()
timing()

digital=Label(window,text="DigitaL",font="times 24 bold",background="#455",foreground="#590")
digital.pack()

#подключаем текстовый документ
data_file = open("wintxt.txt")
data = data_file.read()         #чтение содержимого файла
data_file.close()
w = tk.Label(window,
	text=data,
	background="#455",      #цвет фона текста
	foreground="#590")      #цвет текста
w.pack()
w.place(y=295, x=260)           #положение текста

#w1 = tk.Label(image=logo)       картинка на фон
#w1.pack()

#кнопки
btn = Button(window,
	text="OK",
	background="#390",  	#фон
	command=click_button,	#активация кнопки
	height=1,		#высота
	width=17)		#ширина
btn.pack()
btn.place(y=240, x=32)	#положение кнопки в окне
btn = Button(window,
	text="NO",
	background="#800",
	command=click_b,
	height=1,
        width=17)
btn.pack()
btn.place(y=240, x=200)

#window.resizable(False, False)  #заморозка разрешения окна
window["bg"]="gray22"
window.mainloop()
