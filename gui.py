# -*- coding: utf-8 -*-
from Tkinter import *
from PIL import Image, ImageTk
import webbrowser
import tkMessageBox
def google_map(event):
    ''' Connect to GoogleMap '''
    webbrowser.open_new("https://www.google.co.th/maps/dir///@13.7245995,100.6331106,11z")
def check_error():
    ''' Check the input '''
    try:
        distanc1 = int(distanc.get())
        time1 = int(time.get())
        show_detail()
    except ValueError:
        tkMessageBox.showerror("Error input", "No valid integer! Please try again ...")
def show_detail():
    ''' show_detail '''
    root.destroy()
def page_root():
    '''  First page, 2 variables input '''
    global distanc
    global time
    global root
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
    BG_click_label.bind("<Button-1>", google_map)
    BG_calculate = ImageTk.PhotoImage(Image.open("calculate.gif"))
    BG_calculate_label = Button(root, image=BG_calculate, command=check_error, cursor="hand2").place(x=325,y=425)
    distanc = IntVar()
    time = IntVar()
    button_distance = Entry(root, textvariable=distanc).place(x=282, y=260)
    button_time = Entry(root, textvariable=time).place(x=282, y=380)
    mainloop()
page_root()
