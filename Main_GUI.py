from tkinter import *
import tkinter.ttk as ttk
import Second_win
from PIL import Image, ImageTk
import ewd_logic_of_indication
import pfd_logic_of_indication
from tkinter.messagebox import *
import sys
import os


class Main_app:
    # Window's interface.
    def __init__(self, master):

        # The path to the working folder
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path) + "/appdata"

        # Setting style.
        style = ttk.Style()
        style.map("C.TButton",
                  foreground=[('pressed', 'red'), ('active', 'red')],
                  background=[('pressed', '!disabled', 'black'), ('active', 'black')]
                  )
        ttk.Style().configure("TButton", padding=5, relief="raise",  background="black")
        # Style is set.

        self.img_PFD = Image.open(config_path + '/PFD.jpg')
        self.img_EWD = Image.open(config_path + '/EWD.png')
        self.img_FCTL = Image.open(config_path + '/FCTL.png')

        self.img_PFD_res = self.img_PFD.resize((250, 250), Image.ANTIALIAS)
        self.img_EWD_res = self.img_EWD.resize((447, 250), Image.ANTIALIAS)
        self.img_FCTL_res = self.img_FCTL.resize((335, 300), Image.ANTIALIAS)

        self.pfd = ImageTk.PhotoImage(self.img_PFD_res)
        self.ewd = ImageTk.PhotoImage(self.img_EWD_res)
        self.fctl = ImageTk.PhotoImage(self.img_FCTL_res)


        self.master = master
        self.master.geometry('1080x350+100+100')
        self.master_fr = Frame(self.master, bg='black')
        self.frame = Frame(self.master_fr, bg='black')
        self.fr_for_imgbtn = Frame(self.master_fr, bg='black')

        self.btnChooseEWD = Button(self.fr_for_imgbtn, image=self.ewd, command=lambda: self.choose_logic('ewd'))
        self.btnChoosePFD = Button(self.fr_for_imgbtn, image=self.pfd, command=lambda: self.choose_logic('pfd'))
        self.btnChooseFCTL = Button(self.fr_for_imgbtn, image=self.fctl, command=lambda: self.choose_logic('fCtl'))
        self.btn2 = ttk.Button(self.master_fr, text='Exit', style="C.TButton")
        self.btn2.bind('<Button-1>', self.close_windows)

        self.master_fr.pack()
        self.fr_for_imgbtn.pack()
        self.btnChoosePFD.pack(side=LEFT, pady=5, padx=5)
        self.btnChooseEWD.pack(side=LEFT, pady=5, padx=5)
        self.btnChooseFCTL.pack(side=LEFT, pady=5, padx=5)
        self.btn2.pack()
        self.frame.pack()

    # Запуск нового окна
    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Second_win.app_6_3_8(self.newWindow)

    def choose_logic(self, var_of_display):
        if var_of_display == "pfd":
            self.newWindow = Toplevel(self.master)
            self.app = pfd_logic_of_indication.pwd_logic(self.newWindow)
            print("Открыть окно PFD")
        elif var_of_display == 'ewd':
            self.newWindow = Toplevel(self.master)
            self.app = ewd_logic_of_indication.ewd_logic(self.newWindow)
        elif var_of_display == "fctl":
            print("Открыть окно FCTL")
        else:
            self.error = showerror(title='Critical error', message='Приложение будет закрыто')
            self.master.quit()
            self.newWindow = None
        if self.newWindow is not None:
            self.newWindow.mainloop()
            self.master.wm_state('iconic')


    def close_windows(self, event):
        self.master.destroy()


def main(): 
    root = Tk()
    app = Main_app(root)
    root.mainloop()


if __name__ == '__main__':
    main()