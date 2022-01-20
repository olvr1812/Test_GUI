from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from pandas import *
from functools import partial
from pyautogui import *
import pyperclip
import tkcap

#import Main_GUI
#from Main_GUI import Main_app
import Main_GUI


class app_6_3_8(Main_GUI.main_app):
    # Определение рабочей папки
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)

    config_path = os.path.join(application_path) + "/appdata"

    # Очистка папки Screenshots
    file_end = os.listdir(config_path + "/Screenshots")
    for i in file_end:
        if i.endswith(".png"):
            os.remove(config_path + "/Screenshots/" + i)
    count = 1

    # Ввод переменных
    xl_new = read_excel(config_path + '/logic.xlsx')

    descriptSig = xl_new['Описание входного параметра'].tolist()
    nameSig = xl_new['Название входного параметра'].tolist()
    rangeSig = xl_new['Физический диапазон'].tolist()
    print(descriptSig)

    im = config_path + '/Indication_6_3_8/Var4.png'

    logic = open(config_path + '/logic_text/logic_6_3_8.txt', encoding='utf-8').readlines()
    logic = ''.join(logic)

    def chek_b1(self):
        v_s = []
        p_s = []
        for l in range(len(app_6_3_8.descriptSig)):
            exec('v_s.append(self.var{}.get())'.format(str(l)))
            exec('p_s.append(self.txt{}.get())'.format(str(l)))

        self.im = app_6_3_8.logik_of_indication(v_s, p_s)
        self.image = Image.open(self.im)
        self.photo = ImageTk.PhotoImage(self.image)
        # c_image = canvas.create_image(60, 160, anchor=NW, image=photo)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

    def logik_of_indication(v_s, p_s):
        if 0 <= p_s[0] <= 24 and 0 <= p_s[1] <= 24 and 0 <= p_s[2] <= 36 and 0 <= p_s[3] <= 36 and 0 <= p_s[4] <= 1 \
                and 0 <= p_s[5] <= 1 and 0 <= p_s[6] <= 1 and 0 <= p_s[7] <= 1 and 0 <= p_s[8] <= 6 and 0 <= p_s[9] <= 4 \
                and 0 <= p_s[10] <= 1 and 0 <= p_s[11] <= 1 and 0 <= p_s[12] <= 1:
            if v_s[8] == 1 and (v_s[0] == 1 or v_s[1] == 1) and (v_s[2] == 1 or v_s[3] == 1) and v_s[8] == 1 and \
                    p_s[10] == 1:


                if p_s[8] == 0 and p_s[9] == 0:  # СУМК = 0 РУМК = 0
                    if (v_s[4] == 0 or v_s[5] == 0) and (v_s[6] == 0 or v_s[7] == 0):
                        if (p_s[0] == 0 or p_s[1] == 0) and (p_s[2] == 0 or p_s[3] == 0):
                            print('Вариант 4 | FLAP 0 - надпись отсутствует')
                            im = app_6_3_8.config_path + "/Indication_6_3_8/Var4.png"

                        else:
                            #print('Вариант 5 | FLAP 0 - цвет голубой')
                            im = app_6_3_8.config_path + "/Indication_6_3_8/Var5.png"
                    else:
                        #print('Вариант 6 | FLAP 0 - цвет янтарный')
                        im = app_6_3_8.config_path + "/Indication_6_3_8/Var6.png"

                elif p_s[8] == 1 and p_s[9] == 0:  # СУМК = 1 РУМК = 0
                    if (p_s[4] == 0 or p_s[5] == 0) and (p_s[6] == 0 or p_s[7] == 0):
                        if (p_s[0] == 0 or p_s[1] == 0) and (p_s[2] == 1 or p_s[3] == 1):
                            #print('Вариант 21 | FLAP ICE - зеленый')
                            im = app_6_3_8.config_path + "/Indication_6_3_8/Var21.png"
                        else:
                            #print('Вариант 20 | FLAP ICE - цвет голубой')
                            im = app_6_3_8.config_path + "/Indication_6_3_8/Var20.png"
                    else:
                        #print('Вариант 22 | FLAP ICE - цвет янтарный')
                        im = app_6_3_8.config_path + "/Indication_6_3_8/Var22.png"

                elif p_s[8] == 2 and p_s[9] == 1:  # СУМК 2 РУМК = 1
                    if (p_s[4] == 0 or p_s[5] == 0) and (p_s[6] == 0 or p_s[7] == 0):
                        if (p_s[0] == 18 or p_s[1] == 18) and (p_s[2] == 3 or p_s[3] == 3):
                            #print('Вариант 7 | FLAP 1 - зеленый')
                            im = app_6_3_8.config_path + "/Indication_6_3_8/Var7.png"
                        else:
                            #print('Вариант 8 | FLAP 1 - цвет голубой')
                            im = app_6_3_8.config_path + "/Indication_6_3_8/Var8.png"
                    else:
                        #print('Вариант 9 | FLAP 1 - цвет янтарный')
                        im = app_6_3_8.config_path + "/Indication_6_3_8/Var9.png"

                elif p_s[8] == 3 and p_s[9] == 1:  # СУМК = 3 РУМК = 1
                    if (p_s[4] == 0 or p_s[5] == 0) and (p_s[6] == 0 or p_s[7] == 0):
                        if (p_s[0] == 18 or p_s[1] == 18) and (p_s[2] == 9 or p_s[3] == 9):
                            #print('Вариант 10 | FLAP 1 + F - зеленый')
                            im = app_6_3_8.config_path + "/Indication_6_3_8/Var10.png"
                        else:
                            #print('Вариант 11 | FLAP 1 + F - цвет голубой')
                            im = app_6_3_8.config_path + "/Indication_6_3_8/Var11.png"
                    else:
                        #print('Вариант 12 | FLAP 1 + F - цвет янтарный')
                        im = app_6_3_8.config_path + "/Indication_6_3_8/Var12.png"

                elif p_s[8] == 4 and p_s[9] == 2:  # СУМК = 4 РУМК = 2
                    if (p_s[4] == 0 or p_s[5] == 0) and (p_s[6] == 0 or p_s[7] == 0):
                        if (p_s[0] == 24 or p_s[1] == 24) and (p_s[2] == 16 or p_s[3] == 16):
                            #print('Вариант 13 | FLAP 2 - зеленый')
                            im = app_6_3_8.config_path + "/Indication_6_3_8/Var13.png"
                        else:
                            #print('Вариант 14 | FLAP 2 - цвет голубой')
                            im = app_6_3_8.config_path + "/Indication_6_3_8/Var14.png"
                    else:
                        #print('Вариант 15 | FLAP 2 - цвет янтарный')
                        im = app_6_3_8.config_path + "/Indication_6_3_8/Var15.png"

                elif p_s[8] == 5 and p_s[9] == 3:
                    if (p_s[4] == 0 or p_s[5] == 0) and (p_s[6] == 0 or p_s[7] == 0):
                        if (p_s[0] == 24 or p_s[1] == 24) and (p_s[2] == 25 or p_s[3] == 25):
                            #print('Вариант 16 | FLAP 3 - зеленый')
                            im = app_6_3_8.config_path + "/Indication_6_3_8/Var16.png"
                        else:
                            #print('Вариант 17 | FLAP 3 - цвет голубой')
                            im = app_6_3_8.config_path + "/Indication_6_3_8/Var17.png"
                    else:
                        #print('Вариант 18 | FLAP 3 - цвет янтарный')
                        im = app_6_3_8.config_path + "/Indication_6_3_8/Var18.png"
                elif p_s[8] == 6 and p_s[9] == 4:
                    if (p_s[4] == 0 or p_s[5] == 0) and (p_s[6] == 0 or p_s[7] == 0):
                        if (p_s[0] == 24 or p_s[1] == 24) and (p_s[2] == 36 or p_s[3] == 36):
                            if p_s[11] == 1:
                                if v_s[10] == 1 and v_s[11] == 1 and p_s[12] == 1:
                                    #print('Вариант 23 | FULL-S/A - цвет зеленый')
                                    im = app_6_3_8.config_path + "/Indication_6_3_8/Var23.png"
                                else:
                                    #print('Вариант 24 | FULL-S/A - цвет янтарный')
                                    im = app_6_3_8.config_path + "/Indication_6_3_8/Var24.png"
                            else:
                                #print('Вариант 1 | FULL - цвет зеленый')
                                im = app_6_3_8.config_path + "/Indication_6_3_8/Var1.png"
                        else:
                            #print('Вариант 2 | FULL - цвет синий')
                            im = app_6_3_8.config_path + "/Indication_6_3_8/Var2.png"
                    else:
                        #print('Вариант 3 | FULL - цвет янтарный')
                        im = app_6_3_8.config_path + "/Indication_6_3_8/Var3.png"
                else:
                    #print('Вариант 3 | FULL - цвет янтарный')
                    im = app_6_3_8.config_path + "/Indication_6_3_8/Var3.png"
            else:
                #print('Вариант 19 | XXXX')
                im = app_6_3_8.config_path + "/Indication_6_3_8/Var19.png"
        else:
            im = app_6_3_8.config_path + "/Indication_6_3_8/Error.png"
        # print(v_s, "\n", p_s)
        return im

    def screen(self):
        cap = tkcap.CAP(self.win)
        cap.capture(app_6_3_8.config_path + "/Screenshots/Screen{}.png".format(str(self.count)))
        self.count += 1

    def copy(self):
        pyperclip.copy(app_6_3_8.logic)
        return 0

    def tests(self, a):
        if a == 1:
            self.txt0.set(0) # DPK1
            self.txt1.set(0) # DPK2
            self.txt2.set(1) # DZK1
            self.txt3.set(1) # DZK2
            self.txt4.set(0) # FLAPS_1_FAULT
            self.txt5.set(0) # FLAPS_2_FAULT
            self.txt6.set(0) # SLATS_1_FAULT
            self.txt7.set(0) # SLATS_2_FAULT
            self.txt8.set(1) # X_MHZN
            self.txt9.set(0) # X_FCM
            self.txt10.set(1) # X_FCM_valid
            self.txt11.set(0) # S/A
            self.txt12.set(0) # S/A_FEEDBACK
            self.var0.set(1)
            self.var1.set(1)
            self.var2.set(1)
            self.var3.set(1)
            self.var4.set(1)
            self.var5.set(1)
            self.var6.set(1)
            self.var7.set(1)
            self.var8.set(1)
            self.var9.set(1)
            self.var10.set(1)
            self.var11.set(1)
            self.var12.set(1)
        elif a == 2:
            self.txt0.set(18)  # DPK1
            self.txt1.set(18)  # DPK2
            self.txt2.set(3)  # DZK1
            self.txt3.set(3)  # DZK2
            self.txt4.set(0)  # FLAPS_1_FAULT
            self.txt5.set(0)  # FLAPS_2_FAULT
            self.txt6.set(0)  # SLATS_1_FAULT
            self.txt7.set(0)  # SLATS_2_FAULT
            self.txt8.set(2)  # X_MHZN
            self.txt9.set(1)  # X_FCM
            self.txt10.set(1)  # X_FCM_valid
            self.txt11.set(0)  # S/A
            self.txt12.set(0)  # S/A_FEEDBACK
            self.var0.set(1)
            self.var1.set(1)
            self.var2.set(1)
            self.var3.set(1)
            self.var4.set(1)
            self.var5.set(1)
            self.var6.set(1)
            self.var7.set(1)
            self.var8.set(1)
            self.var9.set(1)
            self.var10.set(1)
            self.var11.set(1)
            self.var12.set(1)
        elif a == 3:
            self.txt0.set(18)  # DPK1
            self.txt1.set(18)  # DPK2
            self.txt2.set(9)  # DZK1
            self.txt3.set(9)  # DZK2
            self.txt4.set(0)  # FLAPS_1_FAULT
            self.txt5.set(0)  # FLAPS_2_FAULT
            self.txt6.set(0)  # SLATS_1_FAULT
            self.txt7.set(0)  # SLATS_2_FAULT
            self.txt8.set(3)  # X_MHZN
            self.txt9.set(1)  # X_FCM
            self.txt10.set(1)  # X_FCM_valid
            self.txt11.set(0)  # S/A
            self.txt12.set(0)  # S/A_FEEDBACK
            self.var0.set(1)
            self.var1.set(1)
            self.var2.set(1)
            self.var3.set(1)
            self.var4.set(1)
            self.var5.set(1)
            self.var6.set(1)
            self.var7.set(1)
            self.var8.set(1)
            self.var9.set(1)
            self.var10.set(1)
            self.var11.set(1)
            self.var12.set(1)
        elif a == 4:
            self.txt0.set(24)  # DPK1
            self.txt1.set(24)  # DPK2
            self.txt2.set(16)  # DZK1
            self.txt3.set(16)  # DZK2
            self.txt4.set(0)  # FLAPS_1_FAULT
            self.txt5.set(0)  # FLAPS_2_FAULT
            self.txt6.set(0)  # SLATS_1_FAULT
            self.txt7.set(0)  # SLATS_2_FAULT
            self.txt8.set(4)  # X_MHZN
            self.txt9.set(2)  # X_FCM
            self.txt10.set(1)  # X_FCM_valid
            self.txt11.set(0)  # S/A
            self.txt12.set(0)  # S/A_FEEDBACK
            self.var0.set(1)
            self.var1.set(1)
            self.var2.set(1)
            self.var3.set(1)
            self.var4.set(1)
            self.var5.set(1)
            self.var6.set(1)
            self.var7.set(1)
            self.var8.set(1)
            self.var9.set(1)
            self.var10.set(1)
            self.var11.set(1)
            self.var12.set(1)
        elif a == 5:
            self.txt0.set(24)  # DPK1
            self.txt1.set(24)  # DPK2
            self.txt2.set(25)  # DZK1
            self.txt3.set(25)  # DZK2
            self.txt4.set(0)  # FLAPS_1_FAULT
            self.txt5.set(0)  # FLAPS_2_FAULT
            self.txt6.set(0)  # SLATS_1_FAULT
            self.txt7.set(0)  # SLATS_2_FAULT
            self.txt8.set(5)  # X_MHZN
            self.txt9.set(3)  # X_FCM
            self.txt10.set(1)  # X_FCM_valid
            self.txt11.set(0)  # S/A
            self.txt12.set(0)  # S/A_FEEDBACK
            self.var0.set(1)
            self.var1.set(1)
            self.var2.set(1)
            self.var3.set(1)
            self.var4.set(1)
            self.var5.set(1)
            self.var6.set(1)
            self.var7.set(1)
            self.var8.set(1)
            self.var9.set(1)
            self.var10.set(1)
            self.var11.set(1)
            self.var12.set(1)
        elif a == 6:
            self.txt0.set(24)  # DPK1
            self.txt1.set(24)  # DPK2
            self.txt2.set(36)  # DZK1
            self.txt3.set(36)  # DZK2
            self.txt4.set(0)  # FLAPS_1_FAULT
            self.txt5.set(0)  # FLAPS_2_FAULT
            self.txt6.set(0)  # SLATS_1_FAULT
            self.txt7.set(0)  # SLATS_2_FAULT
            self.txt8.set(6)  # X_MHZN
            self.txt9.set(4)  # X_FCM
            self.txt10.set(1)  # X_FCM_valid
            self.txt11.set(0)  # S/A
            self.txt12.set(0)  # S/A_FEEDBACK
            self.var0.set(1)
            self.var1.set(1)
            self.var2.set(1)
            self.var3.set(1)
            self.var4.set(1)
            self.var5.set(1)
            self.var6.set(1)
            self.var7.set(1)
            self.var8.set(1)
            self.var9.set(1)
            self.var10.set(1)
            self.var11.set(1)
            self.var12.set(1)

    def __init__(self, master):
        self.win = master
        # Create window
        self.win.title("Логика индикации конфигурации механизации крыла")

        # Style for button
        style = ttk.Style()
        style.configure("TButton", font=("Times New Roman", 14))
        style.map("C.TButton",
                  foreground=[('pressed', 'red'), ('active', 'green')],
                  )

        # Label menu
        self.img1 = Image.open(app_6_3_8.config_path + "/logo.png")
        self.img2 = Image.open(app_6_3_8.config_path + "/ssj1.png")
        self.img3 = Image.open(app_6_3_8.config_path + "/ssj2.png")

        self.width = 400

        self.ratio = (self.width / 3000)
        self.height = int((float(self.img1.size[1]) * float(self.ratio)))
        self.imag1 = self.img1.resize((300, self.height), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(self.imag1)

        self.imag2 = self.img2.resize((self.width, 150), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(self.imag2)

        self.imag3 = self.img3.resize((self.width, 150), Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(self.imag3)

        self.fr_back = Frame(self.win, bg='#ececec')
        self.fr_back.pack(side=TOP, fill=X)

        self.panel2 = Label(self.fr_back, image=self.image2)
        self.panel2.pack(side=LEFT)

        self.panel1 = Label(self.fr_back, image=self.image1)
        self.panel1.pack(side=LEFT, expand=YES)

        self.panel3 = Label(self.fr_back, image=self.image3)
        self.panel3.pack(side=RIGHT)

        # Создание панели меню
        self.menu_bar = Menu(self.win)

        self.filemenu = Menu(self.menu_bar)
        # self.filemenu.add_command(label="Main", command=self.open_main)
        self.filemenu.add_command(label="Screenshot", command=self.screen)
        self.filemenu.add_command(label="Close", command=self.close_windows)

        self.menu_bar.add_cascade(label="File", menu=self.filemenu)

        # Начало таблицы
        # Создание заголовков таблицы
        self.fr_main = Frame(self.win, relief=GROOVE, bd=1, bg='black')
        self.fr = Frame(self.fr_main, relief=RIDGE, bd=1, width=70, bg='black')
        self.lbl0 = Label(self.fr, text="Описание\nвходного параметра", font=("Times New Roman", 11), width=24,
                          height=2, bg='#ececec')
        self.lbl1 = Label(self.fr, text="Название входного\nпараметра", font=("Times New Roman", 11), width=16,
                          height=2, bg='#ececec')
        self.lbl2 = Label(self.fr, text="Валидность\nсигнала", font=("Times New Roman", 11), width=12, height=2, bg='#ececec')
        self.lbl3 = Label(self.fr, text="Значение\nсигнала", font=("Times New Roman", 11), width=9, height=2, bg='#ececec')
        self.lbl4 = Label(self.fr, text="Физический\nдиапазон", font=("Times New Roman", 11), width=9, height=2, bg='#ececec')

        self.fr_main.pack(side=LEFT)
        self.fr.pack(side=TOP)
        self.lbl0.pack(side=LEFT)
        self.lbl1.pack(side=LEFT)
        self.lbl2.pack(side=LEFT)
        self.lbl3.pack(side=LEFT)
        self.lbl4.pack(side=LEFT)

        # Циклическое создание таблицы
        for i in range(len(app_6_3_8.descriptSig)):
            exec('self.txt{} = DoubleVar()'.format(str(i)))
            exec('self.var{} = IntVar()'.format(str(i)))
            exec('self.var{}.set(1)'.format(str(i)))

            # Начало рамки для табличных значений #############################################
            exec('self.fr{} = Frame(self.fr_main, relief=GROOVE, bd=1, width=70, bg="black")'.format(str(i)))

            # Ячейка с описанием параметра
            exec('self.text{} = Text(self.fr{}, font=("Times New Roman", 11), height=2, width=23, wrap=WORD, '
                 'bg ="#ececec")'.format(str(i), str(i)))
            exec('self.text{}.tag_configure("center", justify="center")'.format(str(i)))
            exec('self.text{}.insert(1.0, "{}")'.format(str(i), app_6_3_8.descriptSig[i]))
            exec('self.text{}.tag_add("center", "1.0", "end")'.format(str(i)))
            exec('self.text{}.config(state=DISABLED)'.format(str(i)))

            # Ячейка с именем параметра
            exec('self.lbl{} = Label(self.fr{}, text="{}", font=("Times New Roman", 11), width=16, height=2)'.format(
                str(i), str(i), app_6_3_8.nameSig[i]))

            # Ячейка с выбором валидности сигнала
            exec(
                "self.chb{} = Checkbutton(self.fr{}, text='Валиден', cursor='exchange', font=('Times New Roman', 11), variable=self.var{}, onvalue=1, offvalue=0, width=12, height=2)".format(
                    str(i), str(i), str(i)))

            # Ячейка с вводом значения параметра
            exec(
                "self.ent{} = Entry(self.fr{}, textvariable=self.txt{}, font=('Times New Roman', 11), relief=GROOVE, width=8)".format(
                    str(i), str(i), str(i)))

            # Ячейка c диапазоном возможных значений
            exec('self.text{}1 = Text(self.fr{}, font=("Times New Roman", 11), height=2, width=9, wrap=WORD, bg="#ececec")'.format(
                str(i), str(i)))
            exec('self.text{}1.tag_configure("center", justify="center")'.format(str(i)))
            exec('self.text{}1.insert(1.0, "{}")'.format(str(i), app_6_3_8.rangeSig[i]))
            exec('self.text{}1.tag_add("center", "1.0", "end")'.format(str(i)))
            exec('self.text{}1.config(state=DISABLED)'.format(str(i)))

            # Расположение Виджетов
            exec("self.fr{}.pack(side=TOP)".format(str(i)))
            exec('self.text{}.pack(side=LEFT)'.format(str(i)))
            exec("self.lbl{}.pack(side=LEFT, fill=Y)".format(str(i)))
            exec("self.chb{}.pack(side=LEFT)".format(str(i)))
            exec("self.ent{}.pack(side=LEFT, fill=Y)".format(str(i)))
            exec("self.text{}1.pack(side=LEFT, fill=Y)".format(str(i)))
        # Конец таблицы ###################################################

        self.fr_results = Frame(self.win, bg='#ececec')

        self.fr_tests = Frame(self.fr_results, relief=GROOVE)
        self.fr_tests_l = Frame(self.fr_tests)
        self.fr_tests_r = Frame(self.fr_tests)
        self.fr_copy_and_screen = Frame(self.fr_results)
        self.fr_logic = Frame(self.win, relief=RIDGE, bd=6)

        self.start_bt = ttk.Button(self.fr_results, text="START", cursor="hand1", command=self.chek_b1,
                                   style="C.TButton")

        self.test1 = ttk.Button(self.fr_tests_l, text="FLAP ICE", cursor="hand1", command=partial(self.tests, 1),
                                style="C.TButton")
        self.test2 = ttk.Button(self.fr_tests_r, text="FLAP 1", cursor="hand1", command=partial(self.tests, 2),
                                style="C.TButton")
        self.test3 = ttk.Button(self.fr_tests_l, text="FLAP 1+F", cursor="hand1", command=partial(self.tests, 3),
                                style="C.TButton")
        self.test4 = ttk.Button(self.fr_tests_r, text="FLAP 2", cursor="hand1", command=partial(self.tests, 4),
                                style="C.TButton")
        self.test5 = ttk.Button(self.fr_tests_l, text="FLAP 3", cursor="hand1", command=partial(self.tests, 5),
                                style="C.TButton", width=10)
        self.test6 = ttk.Button(self.fr_tests_r, text="FULL", cursor="hand1", command=partial(self.tests, 6),
                                style="C.TButton", width=10)
        self.btn_copy = Button(self.fr_copy_and_screen, text="Copy", font=('Times New Roman', 14), command=self.copy,
                               width=11, cursor="hand1")
        self.btn_screenshot = Button(self.fr_copy_and_screen, text="Save screen", font=("Times New Roman", 14),
                                     cursor="hand1", command=self.screen, width=11)
        self.canvas = Canvas(self.fr_results, relief="ridge", bd=4, height=47, width=138)

        self.scr = Scrollbar(self.fr_logic, orient=VERTICAL)
        self.text = Text(self.fr_logic, font=("Times New Roman", 12), width=90, yscrollcommand=self.scr.set)
        self.text.insert(END, app_6_3_8.logic)
        self.text["state"] = DISABLED

        self.scr.config(command=self.text)

        self.chb4["state"] = DISABLED
        self.chb5["state"] = DISABLED
        self.chb6["state"] = DISABLED
        self.chb7["state"] = DISABLED
        self.chb10["state"] = DISABLED
        self.txt10.set(1)

        self.fr_results.pack(side=LEFT, fill=BOTH)
        self.canvas.pack(side=TOP)

        # Добавим изображение
        self.image = Image.open(self.im)
        self.photo = ImageTk.PhotoImage(self.image)
        self.c_image = self.canvas.create_image(0, 0, image=self.photo, anchor='nw')

        # print(im, image, photo, c_image, sep='\n')

        self.start_bt.pack()
        self.fr_tests.pack(side=TOP)
        self.fr_tests_l.pack(side=LEFT)
        self.fr_tests_r.pack(side=RIGHT)
        self.test1.pack(fill=BOTH)
        self.test2.pack(fill=BOTH)
        self.test3.pack(fill=BOTH)
        self.test4.pack(fill=BOTH)
        self.test5.pack(fill=BOTH)
        self.test6.pack(fill=BOTH)
        self.fr_copy_and_screen.pack(side=BOTTOM)
        self.btn_screenshot.pack(side=LEFT)
        self.btn_copy.pack(side=LEFT)
        self.fr_logic.pack(side=LEFT, fill=BOTH)
        self.scr.pack(side=RIGHT, fill=Y)
        self.text.pack(side=LEFT, fill=BOTH)

        self.win.config(menu=self.menu_bar)

    def close_windows(self):
        self.win.destroy()
