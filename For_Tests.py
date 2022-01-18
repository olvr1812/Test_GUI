from tkinter import *
import sys
import time
import os

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

config_path = os.path.join(application_path)

root = Tk()

ans = 'NO'

frameCnt = 58
frames = [PhotoImage(file=config_path + '/mygif.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

frameCnt1 = 16
frames1 = [PhotoImage(file=config_path + '/ZZ5H.gif',format = 'giff -index %i' %(i)) for i in range(frameCnt1)]
btn = Button(root, text='Получить бабки', command=lambda: OuEEE())
btn.pack()


def update(ind, gifka, frameCnt, widj, speed):

    frame = gifka[ind]
    ind += 1
    v = speed
    if ind == frameCnt:
        ind = 0

    widj.configure(image=frame)
    widj.after(v, update, ind, gifka, frameCnt, widj, v)

label = Label(root)
label1 = Label(root, bg='black')

def OuEEE():
    if label:
        label.pack_forget()
    label.pack(side=RIGHT)
    label.after(0, update, 0, frames, frameCnt, label, 40)
    label1.pack_forget()

if ans == 'NO':
    label1.pack(side=LEFT)
    label1.after(0, update, 0, frames1, frameCnt1, label1, 60)






root.mainloop()
