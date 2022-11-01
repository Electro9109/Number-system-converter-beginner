from tkinter import *
import converter


root, conv = Tk(), converter.convertor()
root.title('Number system converter')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clear():
    e.delete(0, END)

def equal():
    e.delete(0, END)

    if math == 'dtob':
        e.insert(0, conv.dectobin(fnum))
    if math == 'btod':
        e.insert(0, conv.bintodec(fnum))
    if math == 'dtoo':
        e.insert(0, conv.dectooct(fnum))
    if math == 'otod':
        e.insert(0, conv.octtodec(fnum))
    if math == 'dtoh':
        e.insert(0, conv.dectohex(fnum))
    if math == 'htod':
        e.insert(0, conv.hextodec(fnum))
    if math == 'btoo':
        e.insert(0, conv.bintooct(fnum))
    if math == 'otob':
        e.insert(0, conv.octtobin(fnum))
    if math == 'btoh':
        e.insert(0, conv.bintohex(fnum))
    if math == 'htob':
        e.insert(0, conv.hextobin(fnum))
    if math == 'otoh':
        e.insert(0, conv.octtohex(fnum))
    if math == 'htoo':
        e.insert(0, conv.hextooct(fnum))

def dectobin():
    first_number = e.get()
    global fnum
    global math
    math = 'dtob'
    fnum = (first_number)
    e.delete(0, END)

def bintodec():
    first_number = e.get()
    global fnum
    global math
    math = 'btod'
    fnum = (first_number)
    e.delete(0, END)

def dectooct():
    first_number = e.get()
    global fnum
    global math
    math = 'dtoo'
    fnum = (first_number)
    e.delete(0, END)

def octtodec():
    first_number = e.get()
    global fnum
    global math
    math = 'otod'
    fnum = (first_number)
    e.delete(0, END)

def dectohex():
    first_number = e.get()
    global fnum
    global math
    math = 'dtoh'
    fnum = (first_number)
    e.delete(0, END)

def hextodec():
    first_number = e.get()
    global fnum
    global math
    math = 'htod'
    fnum = first_number
    e.delete(0, END)

def bintooct():
    first_number = e.get()
    global fnum
    global math
    math = 'btoo'
    fnum = (first_number)
    e.delete(0, END)

def octtobin():
    first_number = e.get()
    global fnum
    global math
    math = 'otob'
    fnum = (first_number)
    e.delete(0, END)

def bintohex():
    first_number = e.get()
    global fnum
    global math
    math = 'btoh'
    fnum = (first_number)
    e.delete(0, END)

def hextobin():
    first_number = e.get()
    global fnum
    global math
    math = 'htob'
    fnum = first_number
    e.delete(0, END)

def octtohex():
    first_number = e.get()
    global fnum
    global math
    math = 'otoh'
    fnum = (first_number)
    e.delete(0, END)

def hextooct():
    first_number = e.get()
    global fnum
    global math
    math = 'htoo'
    fnum = first_number
    e.delete(0, END)

but1 = Button(root, text='1', padx=40, pady=20, bg='pink',command= lambda: button_click(1))
but2 = Button(root, text='2', padx=45, pady=20, bg='pink',command= lambda: button_click(2))
but3 = Button(root, text='3', padx=50, pady=20, bg='pink',command= lambda: button_click(3))
but4 = Button(root, text='4', padx=40, pady=20, bg='pink',command= lambda: button_click(4))
but5 = Button(root, text='5', padx=45, pady=20, bg='pink',command= lambda: button_click(5))
but6 = Button(root, text='6', padx=50, pady=20, bg='pink',command= lambda: button_click(6))
but7 = Button(root, text='7', padx=40, pady=20, bg='pink',command= lambda: button_click(7))
but8 = Button(root, text='8', padx=45, pady=20, bg='pink',command= lambda: button_click(8))
but9 = Button(root, text='9', padx=50, pady=20, bg='pink',command= lambda: button_click(9))
but0 = Button(root, text='0', padx=93, pady=20, bg='pink',command= lambda: button_click(0))
butd = Button(root, text='.', padx=42, pady=20, bg='pink',command= lambda: button_click('.'))
butA = Button(root, text='A', padx=40, pady=20, bg='pink',command= lambda: button_click('A'))
butB = Button(root, text='B', padx=44, pady=20, bg='pink',command= lambda: button_click('B'))
butC = Button(root, text='C', padx=50, pady=20, bg='pink',command= lambda: button_click('C'))
butD = Button(root, text='D', padx=40, pady=20, bg='pink',command= lambda: button_click('D'))
butE = Button(root, text='E', padx=44, pady=20, bg='pink',command= lambda: button_click('E'))
butF = Button(root, text='F', padx=50, pady=20, bg='pink',command= lambda: button_click('F'))

but_clear = Button(root, text='clear', padx=40, pady=20, bg='yellow',command=clear)
but_equal = Button(root, text='Convert', padx=84, pady=20, bg='yellow',command=equal)

dtob = Button(root, text='Dec to Bin', padx=96, pady=20, bg='#D1E231', command=dectobin)
btod = Button(root, text='Bin to Dec', padx=96, pady=20, bg='#D1E231', command=bintodec)
dtoo = Button(root, text='Dec to Oct', padx=96, pady=20, bg='#9BC4E2', command=dectooct)
otod = Button(root, text='Oct to Dec', padx=96, pady=20, bg='#9BC4E2', command=octtodec)
dtoh = Button(root, text='Dec to Hex', padx=94, pady=20, bg='#45CEA2', command=dectohex)
htod = Button(root, text='Hex to Dec', padx=94, pady=20, bg='#45CEA2', command=hextodec)

btoo = Button(root, text='Bin to Oct', padx=105, pady=20, bg='#FC74FD', command=bintooct)
otob = Button(root, text='Oct to Bin', padx=105, pady=20, bg='#FC74FD', command=octtobin)
btoh = Button(root, text='Bin to Hex', padx=105, pady=20, bg='#6666ff', command=bintohex)
htob = Button(root, text='Hex to Bin', padx=105, pady=20, bg='#6666ff', command=hextobin)
otoh = Button(root, text='Oct to Hex', padx=104, pady=20, bg='#00ff00', command=octtohex)
htoo = Button(root, text='Hex to Oct', padx=104, pady=20, bg='#00ff00', command=hextooct)

but = Button(root, text='', padx=136, pady=20, bg='black')
buT = Button(root, text='', padx=125, pady=20, bg='black')


but1.grid(row=3, column=1)
but2.grid(row=3, column=2)
but3.grid(row=3, column=3)
but4.grid(row=2, column=1)
but5.grid(row=2, column=2)
but6.grid(row=2, column=3)
but7.grid(row=1, column=1)
but8.grid(row=1, column=2)
but9.grid(row=1, column=3)
but0.grid(row=6, column=1, columnspan=2)
butd.grid(row=7, column=1)
but_clear.grid(row=6, column=3)
but_equal.grid(row=7, column=2, columnspan=2)
butA.grid(row=4, column=1)
butB.grid(row=4, column=2)
butC.grid(row=4, column=3)
butD.grid(row=5, column=1)
butE.grid(row=5, column=2)
butF.grid(row=5, column=3)


dtob.grid(row=1, column=4)
btod.grid(row=2, column=4)
dtoo.grid(row=3, column=4)
otod.grid(row=4, column=4)
dtoh.grid(row=5, column=4)
htod.grid(row=6, column=4)
btoo.grid(row=1, column=0)
otob.grid(row=2, column=0)
btoh.grid(row=3, column=0)
htob.grid(row=4, column=0)
otoh.grid(row=5, column=0)
htoo.grid(row=6, column=0)

but.grid(row=7, column=0)
buT.grid(row=7, column=4)

root.mainloop()