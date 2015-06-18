# -*- coding: utf-8 -*-

from tkinter import *
import random

window = Tk() # Janela do app
canvas = Canvas(window, width = 500, height = 400) # área para desenha
canvas.pack()


def sierpinski(x1, y1, x2, y2, x3, y3, n):
    """
    Função recursiva que computa triângulo de Sierpinski
    :param n: Número de recursões
    """
    if n == 0:
        canvas.create_line(x1, y1, x2, y2)
        canvas.create_line(x2, y2, x3, y3)
        canvas.create_line(x3, y3, x1, y1)
    else:
        sierpinski(x1, y1, (x1 + x2)/2, (y1 + y2)/2, (x1 + x3)/2, (y1 + y3)/2, n-1)
        sierpinski((x1 + x2)/2, (y1 + y2)/2, x2, y2, (x2 + x3)/2, (y2 + y3)/2, n-1)
        sierpinski((x1 + x3)/2, (y1 + y3)/2, (x2 + x3)/2, (y2 + y3)/2, x3, y3, n-1)


a = (250,100)
b = (350,300)
c = (150, 300)

sierpinski(a[0], a[1], b[0], b[1], c[0], c[1], 4)

window.mainloop()