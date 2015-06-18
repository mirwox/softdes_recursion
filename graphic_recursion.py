# -*- coding: utf-8 -*-
"""
Este programa faz bastante uso da biblioteca tkinter e da
classe Canvas. Há um bom tutorial sobre este assunto no endereço
http://effbot.org/tkinterbook/canvas.htm

Existe uma referência aqui:
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html

"""


from tkinter import *
import random

window = Tk() # Janela do app
canvas = Canvas(window, width = 500, height = 400) # área para desenha
canvas.pack()


def sierpinski(a, b, c, n):
    if n == 0:
        canvas.create_line(a[0],a[1], b[0], b[1])
        canvas.create_line(b[0],b[1], c[0], c[1])
        canvas.create_line(c[0],c[1], a[0], a[1])
    else:
        sierpinski()





canvas.create_line(0,0, 200,200)



window.mainloop()