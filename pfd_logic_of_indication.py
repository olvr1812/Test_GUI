from tkinter import *
from pyautogui import *
from PIL import Image, ImageTk
from pandas import *
import indicate_6_3_8


class pwd_logic:
    def __init__(self, master):

        # Определение рабочей папки
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path) + "/appdata"

        xl_new = read_excel(config_path + '/List_indication.xlsx')

        PFD_logic = xl_new['Индикация PFD'].dropna().tolist()
        print(PFD_logic)

        self.choose_indicate = 'Индикация не выбрана'
        self.acts = PFD_logic
        print(PFD_logic)

        self.img_PFD = Image.open(config_path +'/PFD.jpg')
        self.img_PFD = self.img_PFD.resize((422, 410), Image.ANTIALIAS)
        self.ewd = ImageTk.PhotoImage(self.img_PFD)

        # Create window.
        self.win = master
        self.win.title('Индикация PFD')
        self.win.geometry('715x422')

        # Create frames.
        self.fr_main = Frame(self.win)
        self.fr_list_box = Frame(self.fr_main)

        # Button for close.
        self.btn_close = Button(self.fr_main, text='Close', command=self.close_window)

        self.canvas = Canvas(self.win, width=765, height=422)
        self.image = self.canvas.create_image(0, 0, image=self.ewd, anchor=NW)

        self.scroll_x = Scrollbar(self.fr_list_box, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.fr_list_box, orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.pack(side=BOTTOM, fill=X)

        self.lb = Listbox(self.fr_list_box, xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set, width=30)

        self.scroll_y.config(command=self.lb.yview)
        self.scroll_x.config(command=self.lb.xview)




        for i in self.acts:
            self.lb.insert(END, i)

        self.lb.bind("<<ListboxSelect>>", self.select_indicate)

        self.lb.pack(fill=Y)

        self.var = StringVar()
        self.btn_open_logic = Button(self.fr_main, text='Open')
        self.btn_open_logic.bind('<Button-1>', self.open_indicate)
        self.btn_open_logic.pack()

        self.fr_main.pack(side=LEFT, fill=Y)
        self.canvas.pack(side=RIGHT)
        self.fr_list_box.pack(fill=Y)
        self.btn_close.pack()

    def open_indicate(self, event):
        if self.choose_indicate == 'Индикация положения РУМК':
            self.newWindow = Toplevel(self.win)
            self.app = Second_win.app_6_3_8(self.newWindow)
        else:
            self.var.set('Данный параметр не задан')

    def select_indicate(self, val):
        #print(val)
        sender = val.widget
        idx = sender.curselection()
        self.choose_indicate = sender.get(idx)
        self.btn_open_logic.focus_set()
        print("It's work")



    def close_window(self):
        self.win.destroy()
