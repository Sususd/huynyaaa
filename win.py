from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
import sys
import time


clicks = 0

n = 0

def b1(event):                       #ненужно, но прикольно)))))
        e = tk.Label(window,
                text="Left Click",
                foreground="#499",
                background="#455")
        e.pack()
        e.place(y=150, x=0)
        window.after(1000, destroy_widget, e)

def b3(event):
        c = tk.Label(window,
                text="Right Click",
                foreground="#499",
                background="#455")
        c.pack()
        c.place(y=150, x=447)
        window.after(1000, destroy_widget, c)

def destroy_widget(widget):            #что бы стереть всплывающий текст
        widget.destroy()

def move(event):                       #слежка за положенем курсора в окне
        x = event.x
        y = event.y
        s = "|o_0| {}x{}".format(x, y)
        window.title(s)

#скрипты для кнопок
def click_button():
        global clicks                              #тыркалка в названии окна
        clicks += 1
        window.title("Clicks {}".format(clicks))
        if clicks == 1000:
                window.title("openrc")
        if clicks == -1000:
                window.title("systemd")

        global n                                    #тыркалка
        n += 1
        label['text'] = str(n)

def click_b():
        global clicks
        clicks += 1
        window.title("Clicks {}".format(clicks))
        if clicks == -1000:                         #безсмысленно и безполезно
                window.title("systemd")             #просто есть
        if clicks == 1000:
                window.title("openrc")

        global n
        n -= 1
        label['text'] = str(n)

def timing():                     #часы
        current_time = time.strftime("%H : %M : %S")
        clock.config(text=current_time)
        clock.after(200,timing)

#окно
window = tk.Tk()
window.title("window")
window.geometry("515x380")

label = Label(window,              #конфиг тыркалки
        text= str(n),
        font = ("Helvetica", 60),
        background="#203",
        foreground="#900")
label.pack()
label.place(y=310, x=0)

window.bind('<Button-1>', b1)      #привязка тыркалки
window.bind('<Button-3>', b3)
window.bind('<Motion>', move)

clock=tk.Label(window,             #конфиг часов
        font=("times",80,"bold"),
        background="#203",
        foreground="#499")
clock.pack()
clock.place(x=5, y=50)
timing()

digital=Label(window,              #подпись под часами
        text="DigitaL",
        font="times 24 bold",
        background="#203",
        foreground="#590")
digital.pack()
digital.place(x=205, y=127)

#подключаем текстовый документ
data_file = open("wintxt.txt")
data = data_file.read()         #чтение содержимого файла
data_file.close()
w = tk.Label(window,
	text=data,
	background="#203",      #цвет фона текста
	foreground="#499")      #цвет текста
w.pack()
w.place(y=310, x=400)           #положение текста

#кнопки
btn = Button(window,
	text="OK",
	background="#390",  	#фон
	command=click_button,	#активация кнопки
	height=3,		#высота
	width=17)
btn.pack()
btn.place(y=240, x=110)	        #положение кнопки в окне
btn = Button(window,
	text="NO",
	background="#900",
	command=click_b,
	height=3,
        width=17)
btn.pack()
btn.place(y=240, x=260)

window.resizable(False, False)  #заморозка разрешения окна
window["bg"]="#203"
window.mainloop()

