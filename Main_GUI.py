from tkinter import *
import tkinter.ttk as ttk
import indicate_6_3_8
from PIL import Image, ImageTk
import ewd_logic_of_indication
import fctl_logic_of_indication
import pfd_logic_of_indication
from tkinter.messagebox import *
import sys
import os



class main_app:
    # Window's interface.
    def __init__(self, master):
        # Variables for new windows
        self.app = None
        self.newWindow = None

        # The path to the working folder
        application_path = None
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
        ttk.Style().configure("TButton", padding=3, relief="raise",  background="black", width=5, height=3)
        # Style is set.

        self.img_PFD = Image.open(config_path + '/PFD.jpg')
        self.img_EWD = Image.open(config_path + '/EWD.png')
        self.img_FCTL = Image.open(config_path + '/FCTL.png')

        self.img_PFD_res = self.img_PFD.resize((250, 250), Image.ANTIALIAS)
        self.img_EWD_res = self.img_EWD.resize((447, 250), Image.ANTIALIAS)
        self.img_FCTL_res = self.img_FCTL.resize((279, 250), Image.ANTIALIAS)

        self.pfd = ImageTk.PhotoImage(self.img_PFD_res)
        self.ewd = ImageTk.PhotoImage(self.img_EWD_res)
        self.fctl = ImageTk.PhotoImage(self.img_FCTL_res)

        # Main window and frames
        self.master = master
        self.master.title("Analysis of display logic")
        w = self.master.winfo_screenwidth()
        h = self.master.winfo_screenheight()
        w = w / 2
        h = h / 2
        w = int(w - 525)
        h = int(h - 300)
        self.master.geometry("1050x315+{}+{}".format(w, h))
        self.master.resizable(False, False)
        self.master_fr = Frame(self.master, bg='black')
        self.frame = Frame(self.master_fr, bg='black')
        self.fr_PFD = LabelFrame(self.frame, bg='black', text="Логика индикации PFD", foreground='white')
        self.fr_EWD = LabelFrame(self.frame, bg='black', text="Логика индикации EWD", foreground='white')
        self.fr_FCTL = LabelFrame(self.frame, bg='black', text="Логика индикации FCTL", foreground='white')
        self.fr_for_close = Frame()

        self.btnChoosePFD = Button(self.fr_PFD, image=self.pfd, command=lambda: self.choose_logic('pfd'))
        self.btnChooseEWD = Button(self.fr_EWD, image=self.ewd, command=lambda: self.choose_logic('ewd'))
        self.btnChooseFCTL = Button(self.fr_FCTL, image=self.fctl, command=lambda: self.choose_logic('fctl'))
        self.btn2 = Button(self.master_fr, text='Exit', bg='black', height=3, width=14)
        self.btn2.bind('<Button-1>', self.close_windows)

        self.master_fr.pack()
        self.frame.pack(side=TOP)
        self.fr_PFD.pack(side=LEFT, fill=Y)
        self.fr_EWD.pack(side=LEFT, fill=Y)
        self.fr_FCTL.pack(side=LEFT, fill=Y)
        self.btnChoosePFD.pack(side=BOTTOM, pady=5, padx=5)
        self.btnChooseEWD.pack(side=BOTTOM, pady=5, padx=5)
        self.btnChooseFCTL.pack(side=BOTTOM, pady=5, padx=5)
        self.btn2.pack(side=LEFT)

    # Запуск нового окна
    def choose_logic(self, var_of_display):
        self.newWindow = Toplevel(self.master)
        if var_of_display == "pfd":
            self.app = pfd_logic_of_indication.pwd_logic(self.newWindow)
        elif var_of_display == 'ewd':
            self.app = ewd_logic_of_indication.ewd_logic(self.newWindow)
        elif var_of_display == "fctl":
            self.app = fctl_logic_of_indication.fctl_logic(self.newWindow)
        else:
            self.error = showerror(title='Critical error', message='Приложение будет закрыто')
            self.master.quit()
            self.newWindow = None

        if self.newWindow is not None:
            self.newWindow.mainloop()
            self.master.wm_state('iconic')

    def close_windows(self, event):
        self.master.destroy()



if __name__ == '__main__':
    root = Tk()
    app = main_app(root)
    root.mainloop()