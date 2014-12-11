# -*- coding: utf-8 -*-
from Tkinter import *
from math import *
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

def mquit():
    ''' exit programe '''
    mExit = tkMessageBox.askokcancel(title="Quit",message="Are You Sure")
    if mExit > 0:
        page_two.destroy()
        return
def main2():
    ''' back page_root '''
    page_two.destroy()
    page_root()
def show_detail():
    ''' show_detail '''
    root.destroy()

    kilometre = int(distanc.get())
    minute = int(time.get())
    if kilometre <= 1:
        price = 35
    elif kilometre <= 12:
        price = 35 + (kilometre-1)*5
    elif kilometre <= 20:
        price = 90 + (kilometre-12)*5.5
    elif kilometre <= 40:
        price = 134 + (kilometre-20)*6
    elif kilometre <= 60:
        price = 254 + (kilometre-40)*6.5
    elif kilometre <= 80:
        price = 384 + (kilometre-60)*7.5
    else:
        price = 534 + (kilometre-80)*8.5
    ''' price '''
    price = int(price)
    ''' price time '''
    minute1 = int(floor((minute*1.50)/2)*2)
    ''' sum price + time '''
    total = price + minute1

    global page_two
    page_two = Tk()
    page_two.title("Taxi meter")
    page_two.geometry('760x585+280+70')
    
    frame = Frame(page_two).pack()
    canvas = Canvas(frame, bg="white", width=750, height=580)
    canvas.pack()
    photoimage = ImageTk.PhotoImage(file="main_output.gif")
    canvas.create_image(365, 289, image=photoimage)

    Label(page_two,text = kilometre, fg = "red", font = "Times 15 bold").place(x=525,y=190) # output ระยะทาง
    Label(page_two,text = minute, fg = "red", font = "Times 15 bold").place(x=525,y=228) # output เผื่อเวลารถติด
    Label(page_two,text = price, fg = "red", font = "Times 15 bold").place(x=525,y=265) # output ราคาระยะทาง
    Label(page_two,text = minute1, fg = "red", font = "Times 15 bold").place(x=525,y=305) # output ราคาเวลา
    Label(page_two,text = total, fg = "red", font = "Times 30 bold").place(x=484,y=352) # output ราคารวม

    BG_home = ImageTk.PhotoImage(Image.open("home.gif")) #PIC_BG_click
    BG_click_home = Button(page_two, image=BG_home, cursor="hand2",command=main2).place(x=55,y=420)#label_PIC_BG_click

    BG_exit = ImageTk.PhotoImage(Image.open("exit.gif")) #PIC_BG_click
    BG_click_exit = Button(page_two, image=BG_exit, cursor="hand2", command=mquit).place(x=147,y=420)#label_PIC_BG_click
    
    mainloop()
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
    distanc = StringVar()
    time = StringVar()
    button_distance = Entry(root, textvariable=distanc).place(x=282, y=260)
    button_time = Entry(root, textvariable=time).place(x=282, y=380)
    mainloop()
page_root()
