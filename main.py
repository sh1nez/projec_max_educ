from tkinter import *
import requests as req
from bs4 import BeautifulSoup as b
import random
from PIL import ImageTk
import webbrowser


def net():
    window.destroy()


def da():
    global click
    click += 1
    btn1.destroy()
    btn2.destroy()
    l.config(text='и ещё таким же сексуальным!?')
    l2['image'] = img3
    btn3.place(x=700, y=100)


def marihuana():
    clear_all()
    window.geometry('1100x700')
    global click
    click += 1
    btn.place(x=0, y=50)
    l.place(x=0, y=0)


def marihuana_new():
    l.config(text='хочешь быть таким же успешным как я?')
    btn1.place(x=630, y=300)
    btn2.place(x=900, y=300)
    l2.place(x=0, y=50)
    btn.destroy()


def sex():
    l.destroy()
    l2.destroy()
    btn3.destroy()
    l3.pack()
    l4.place(x=500, y=300)


def link():
    l3.destroy()
    l4.destroy()
    webbrowser.open_new(r"https://maximumtest.ru/digital-skills")
    window.destroy()


window = Tk()
window.geometry('700x600')
window.title("Проект")

click = 0


def draw_menu():
    home_button = Button(text='Домой', font=(
        'Arial', 20), fg='black', command=home)
    button_one = Button(text='посмотреть анекдоты', font=(
        "Arial", 20), fg='black', command=anek)
    button_two = Button(text='Посмотреть рекламу курса', font=(
        "Arial", 20), fg='black', command=marihuana, )

    l_title = Label(text='Что бы вы хотели сделать?',
                    font=('Arial', 24), fg='white', bg='orange')
    clear_all()
    l_title.place(width=700, height=50, x=0, y=0)
    button_one.place(x=20, y=70, width=300)
    button_two.place(x=325, y=70, width=350)


def clear_all():
    all_widgets = window.place_slaves()
    for widget in all_widgets:
        widget.destroy()


def home():
    clear_all()
    draw_menu()
    l_anek.forget()


def anek():
    clear_all()
    draw_home_button()
    url = 'https://www.anekdot.ru/release/anekdot/day/'
    r = req.get(url)
    s = b(r.text, 'lxml')
    c = s.find_all('div', class_='text')
    i = random.randint(0, len(c) - 1)
    l_anek['text'] = c[i].text
    l_anek.pack()


def draw_home_button():
    home_button = Button(text='Домой', font=(
        'Arial', 20), fg='black', command=home)
    home_button.place(x=300, y=500)
    button_one = Button(text='посмотреть анекдоты', font=(
        "Arial", 20), fg='black', command=anek)
    button_two = Button(text='Посмотреть рекламу курса', font=(
        "Arial", 20), fg='black', command=marihuana, )

    l_title = Label(text='Что бы вы хотели сделать?',
                    font=('Arial', 24), fg='white', bg='orange')

    global click
    click += 1
    if click > 2:
        home_button = Button(text='Домой', font=(
            'Arial', 20), fg='black', command=home)
        home_button.destroy()

        home_button.place(x=300, y=500)
    click = 0


draw_menu()

img = ImageTk.PhotoImage(file='marihuana_na_rublevke.jpg', size='640x640')
img2 = ImageTk.PhotoImage(file='klim_pod.jpg', size='727x725')
img3 = ImageTk.PhotoImage(file='sex.jpg', size='640x640')

btn = Button(
    window,
    height=600,
    width=600,
    image=img,
    font='Arial 15 bold',
    text='марихуана',
    compound=BOTTOM,
    command=marihuana_new
)
btn1 = Button(
    window,
    height=10,
    width=10,
    font='Arial 15 bold',
    text='ДА',
    command=da,
    fg='white',
    bg='black'
)
btn2 = Button(
    window,
    height=10,
    width=10,
    font='Arial 15 bold',
    text='НЕТ',
    command=net,
    fg='white',
    bg='black'

)
btn3 = Button(
    window,
    height=10,
    width=15,
    font='Arial 44 bold',
    text='ДА!!!!',
    command=sex,
    fg='white',
    bg='black'
)

l = Label(window, text='ёу бро нажми на меня если любишь коноплю', font='Arial 20 bold', fg='white', bg='black')
l2 = Label(window, height=600, width=600, image=img2)
l3 = Label(window, text='ТАГДА ЗАПИСЫВАЙСЯ НА НАШ БИЗПЛАТНЫЙ!!! АНЛАЙН КУРС', font='Arial 20 bold', fg='white',
           bg='black')
l4 = Label(window, text='КЛИКАЙ И ЗАПИСЫВАЙСЯ!!!!', cursor="hand2", font='Arial 20 bold', fg='white', bg='black')
l4.bind("<Button-1>", link)

l_anek = Label(font=(
    'Arial', 20), fg='black', justify=CENTER, wraplength=600, pady=200)

window.mainloop()
