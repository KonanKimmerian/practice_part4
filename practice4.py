from tkinter import *


class tk_class(Tk):
    def __init__(self):
        super(tk_class, self).__init__()

    def create_label(self, text: str, x: int, y: int, is_bold: bool):
        c1 = None
        if is_bold:
            c1 = Label(self, text=text, font='Arial 12 bold')
        else:
            c1 = Label(self, text=text, font='Arial 12')
        c1.place(x=x, y=y)

    def create_ent(self, font, bg, justify, str, x, y, width, height):
        ent = Entry(self, font=font, bg=bg, justify=justify)
        ent.insert(END, str)
        ent.place(x=x, y=y, width=width, height=height)
        return ent

    def create_scale(self, x, y, command):
        scale = Scale(self, orient=HORIZONTAL, length=50, from_=0, to=10, command=command)
        scale.place(x=x, y=y)
        return scale

    def create_btn(self, text, x, y, clicked):
        btn = Button(self, text=text, command=clicked)
        btn.place(x=x, y=y)


def pizza_scale_clicked(val=0):
    count = int(val)
    price = int(p1.get())
    pizza_var.set(str(count * price))


def icecream_scale_clicked(val=0):
    count = int(val)
    price = int(p2.get())
    icecream_var.set(str(count * price))


def cake_scale_clicked(val=0):
    count = int(val)
    price = int(p3.get())
    cake_var.set(str(count * price))


def juice_scale_clicked(val=0):
    count = int(val)
    price = int(p4.get())
    juice_var.set(str(count * price))

def btn_clicked():
    totel = pizza_var.get() + icecream_var.get() + cake_var.get() + juice_var.get()
    if var_ch1.get():
        totel += 3
    if var_ch2.get():
        totel +=3
    if var_ch3.get():
        totel +=3
    if var_ch4.get():
        totel +=3

    tot_var.set(totel)



win = tk_class()
win.geometry('650x300')
win.create_label('Найменування', 20, 20, True)
win.create_label('Пiца', 20, 60, False)
win.create_label('Морозиво', 20, 100, False)
win.create_label('Тiстечко', 20, 140, False)
win.create_label('Сiк', 20, 180, False)
win.create_label('Вартiсть замовлення', 20, 220, False)
win.create_label('Цiна, грн', 150, 20, True)
win.create_label('Кiлькiсть', 230, 20, True)
win.create_label('Вартiсть, грн', 310, 20, True)

p1 = win.create_ent('Arial 12', 'sky blue', 'center', '75', 150, 60, 60, 30)
p2 = win.create_ent('Arial 12', 'sky blue', 'center', '12', 150, 100, 60, 30)
p3 = win.create_ent('Arial 12', 'sky blue', 'center', '16', 150, 140, 60, 30)
p4 = win.create_ent('Arial 12', 'sky blue', 'center', '8', 150, 180, 60, 30)

pizza_var = IntVar(value=0)
c1 = Label(win, text='0', font='Arial 12', bg='deep sky blue', textvariable=pizza_var)
c1.place(x=310, y=60, width=60, height=30)

icecream_var = IntVar(value=0)
c2 = Label(win, text='0', font='Arial 12', bg='deep sky blue', textvariable=icecream_var)
c2.place(x=310, y=100, width=60, height=30)

cake_var = IntVar(value=0)
c3 = Label(win, text='0', font='Arial 12', bg='deep sky blue', textvariable=cake_var)
c3.place(x=310, y=140, width=60, height=30)

juice_var = IntVar(value=0)
c4 = Label(win, text='0', font='Arial 12', bg='deep sky blue', textvariable=juice_var)
c4.place(x=310, y=180, width=60, height=30)

s1 = win.create_scale(230, 50, pizza_scale_clicked)

s2 = win.create_scale(230, 90, icecream_scale_clicked)

s3 = win.create_scale(230, 130, cake_scale_clicked)

s4 = win.create_scale(230, 170, juice_scale_clicked)

tot_var = IntVar(value=0)
tot = Label(win, text='0', font='Arial 12', bg='deep sky blue', textvariable=tot_var)
tot.place(x=200, y=220, width=60, height=30)
win.create_label('грн', 270, 220, False)

win.create_btn('Розрахувати', 310, 220, btn_clicked)

win.create_label('Добавки до пiци, 3 грн', 440, 20, True)

var_ch1 = IntVar()
ch1 = Checkbutton(win, text='Майонез', font='Arial 12', variable=var_ch1)
ch1.place(x=440, y=60)

var_ch2 = IntVar()
ch2 = Checkbutton(win, text='Кетчуп', font='Arial 12', variable=var_ch2)
ch2.place(x=440, y=100)

var_ch3 = IntVar()
ch3 = Checkbutton(win, text='Соус', font='Arial 12', variable=var_ch3)
ch3.place(x=440, y=140)

var_ch4 = IntVar()
ch4 = Checkbutton(win, text="Ананаси", font='Arial 12', variable=var_ch4)
ch4.place(x=440, y=180)


win.mainloop()
