# -*- coding: utf-8 -*-
from Tkinter import *
from PIL import Image, ImageTk
def page_root():
    '''  First page, 2 variables input '''
    root = Tk()
    root.geometry('760x585+280+70')
    root.title("Taxi meter")
    frame = Frame(root).pack()
    canvas = Canvas(frame, bg="white", width=750, height=580)
    canvas.pack()
    photoimage = ImageTk.PhotoImage(file="main_taxi.gif")
    canvas.create_image(365, 289, image=photoimage)
    BG_click = ImageTk.PhotoImage(Image.open("click.gif"))
    BG_click_label = Button(root, image=BG_click, cursor="hand2")
    BG_click_label.place(x=274, y=297)
    BG_calculate = ImageTk.PhotoImage(Image.open("calculate.gif"))
    BG_calculate_label = Button(root, image=BG_calculate, cursor="hand2").place(x=325, y=425)
    distanc = IntVar()
    time = IntVar()
    button_distance = Entry(root, textvariable=distanc).place(x=282, y=260)
    button_time = Entry(root, textvariable=time).place(x=282, y=380)
    mainloop()
page_root()
