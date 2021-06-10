import os
from tkinter import *
from tkinter import messagebox

##############################################################
root = Tk()
root.title("Power OS")
root.geometry("400x300")

type = IntVar()
timeout = StringVar()
delay = StringVar()

Label1 = Label(text="Enter timeout value:")
Label1.pack()
Label1.place(x=0,y=0)

Label2 = Label(text="Test button:")
Label2.pack()
Label2.place(x=0,y=50)

timeout_entry = Entry(textvariable=timeout)
timeout_entry.place(x=120,y=0)


def type_select():
    if type == 1:
        s = int(timeout.get())
        delay.set(s)
    elif type == 2:
        s = int(timeout.get())*60
        delay.set(s)
    elif type == 3:
        s = int(timeout.get())*60**2
        delay.set(s)

rb = Radiobutton(root, text="Seconds", variable=type, value=1, command=type_select)
rb.pack
rb.place(x=100,y=160)
rb1 = Radiobutton(root, text="Minutes", variable=type, value=2, command=type_select)
rb1.pack
rb1.place(x=100,y=180)
rb2 = Radiobutton(root, text="Hours", variable=type, value=3, command=type_select)
rb2.pack
rb2.place(x=100,y=200)

def show_message():
    messagebox.showinfo("Timeout", timeout.get())

def click_button():
    os.system("shutdown /s /t " + str(delay.get()))
def click_button1():
    os.system("shutdown /r /t " + str(delay.get()))
def click_button2():
    os.system("shutdown /h")
def click_button3():
    os.system("shutdown /a")



message_button = Button(text="Click Me", command=show_message)
message_button.pack()
message_button.place(x=70,y=50)

btn = Button(text="Shutdown", command=click_button)
btn.pack()
btn.place(x=20, y=160)

btn1 = Button(text="Reboot", command=click_button1)
btn1.pack()
btn1.place(x=20, y=190)

btn2 = Button(text="Sleep mode", command=click_button2)
btn2.pack()
btn2.place(x=20, y=220)

btn3 = Button(text="Decline", command=click_button3)
btn3.pack()
btn3.place(x=20, y=250)

root.mainloop()

##############################################################