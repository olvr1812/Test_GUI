# Шаблон для создания логики индикации
from tkinter import *
from openpyxl import load_workbook
from PIL import Image, ImageTk
from pyautogui import *
import tkcap
import pyperclip
from functools import partial

file_end = os.listdir("Screenshots")
for i in file_end:
    if i.endswith(".png"):
        os.remove("Screenshots/" + i)

class app_5_10_1:
    # Ввод переменных
    wb = load_workbook(filename='logic.xlsx', read_only=True)
    ws = wb['5_10_1']

    descriptSig = []
    nameSig = []
    diapSig = []

    im = 'Indication_5_10_1/Var1.png'

    logic = open('logic_text/logic_5_10_1.txt', encoding='utf-8').readlines()
    logic = ''.join(logic)

    for i in ws.rows:
        for k in i:
            print(k.value)
            if k == i[0]:
                descriptSig.append(k.value)
            elif k == i[1]:
                nameSig.append(k.value)
            elif k == i[2]:
                diapSig.append(k.value)

    k: IntVar = 0
    count = 1

    def __init__(self):
        # Create window
        self.win = Tk()
        self.win.title("Индикация состояния первого канала СДУ")

        # Создание панели меню
        self.menu_bar = Menu(self.win)

        self.filemenu = Menu(self.menu_bar)
        self.filemenu.add_command(label="Main", command=self.open_main)
        self.filemenu.add_command(label="Screenshot", command=self.screen)
        self.filemenu.add_command(label="Close", command=self.win.quit)

        self.menu_bar.add_cascade(label="File", menu=self.filemenu)

        # Начало таблицы
        # Создание заголовков таблицы
        self.fr_main = Frame(self.win, relief=GROOVE, bd=4)
        self.fr = Frame(self.fr_main, relief=RIDGE, bd=1, width=70)
        self.lbl0 = Label(self.fr, text="Описание\nвходного параметра", font=("Times New Roman", 11), width=23,
                          height=2)
        self.lbl1 = Label(self.fr, text="Название входного\nпараметра", font=("Times New Roman", 11), width=16,
                          height=2)
        self.lbl2 = Label(self.fr, text="Валидность\nсигнала", font=("Times New Roman", 11), width=12, height=2)
        self.lbl3 = Label(self.fr, text="Значение\nсигнала", font=("Times New Roman", 11), width=9, height=2)
        self.lbl4 = Label(self.fr, text="Физический\nдиапазон", font=("Times New Roman", 11), width=9, height=2)

        self.fr_main.pack(side=LEFT)
        self.fr.pack(side=TOP)
        self.lbl0.pack(side=LEFT)
        self.lbl1.pack(side=LEFT)
        self.lbl2.pack(side=LEFT)
        self.lbl3.pack(side=LEFT)
        self.lbl4.pack(side=LEFT)

        # Циклическое создание таблицы
        for i in range(len(app_5_10_1.descriptSig)):
            exec('self.txt{} = DoubleVar()'.format(str(i)))
            exec('self.var{} = IntVar()'.format(str(i)))
            exec('self.var{}.set(1)'.format(str(i)))

            # Начало рамки для табличных значений #############################################
            exec('self.fr{} = Frame(self.fr_main, relief="ridge", bd=1, width=70)'.format(str(i)))

            # Ячейка с описанием параметра
            exec('self.text{} = Text(self.fr{}, font=("Times New Roman", 11), height=2, width=23, wrap=WORD)'.format(
                str(i), str(i)))
            exec('self.text{}.tag_configure("center", justify="center")'.format(str(i)))
            exec('self.text{}.insert(1.0, "{}")'.format(str(i), app_5_10_1.descriptSig[i]))
            exec('self.text{}.tag_add("center", "1.0", "end")'.format(str(i)))
            exec('self.text{}.config(state=DISABLED)'.format(str(i)))

            # Ячейка с именем параметра
            exec('self.txta{} = Text(self.fr{}, font=("Times New Roman", 11), height=2, width=16, wrap=WORD)'.format(
                str(i), str(i)))
            exec('self.txta{}.tag_configure("center", justify="center")'.format(str(i)))
            exec('self.txta{}.insert(1.0, "{}")'.format(str(i), app_5_10_1.nameSig[i]))
            exec('self.txta{}.tag_add("center", "1.0", "end")'.format(str(i)))
            exec('self.txta{}.config(state=DISABLED)'.format(str(i)))

            # Ячейка с выбором валидности сигнала
            exec(
                "self.chb{} = Checkbutton(self.fr{}, text='Валиден', cursor='exchange', font=('Times New Roman', 11), variable=self.var{}, onvalue=1, offvalue=0, width=12, height=2)".format(
                    str(i), str(i), str(i)))

            # Ячейка с вводом значения параметра
            exec(
                "self.ent{} = Entry(self.fr{}, textvariable=self.txt{}, font=('Times New Roman', 11), relief=RIDGE, width=8)".format(
                    str(i), str(i), str(i)))

            # Ячейка диапазоном возможных значений
            exec('self.text{}1 = Text(self.fr{}, font=("Times New Roman", 11), height=2, width=9, wrap=WORD)'.format(
                str(i), str(i)))
            exec('self.text{}1.tag_configure("center", justify="center")'.format(str(i)))
            exec('self.text{}1.insert(1.0, "{}")'.format(str(i), app_5_10_1.diapSig[i]))
            exec('self.text{}1.tag_add("center", "1.0", "end")'.format(str(i)))
            exec('self.text{}1.config(state=DISABLED)'.format(str(i)))

            # Расположение Виджетов
            exec("self.fr{}.pack(side=TOP)".format(str(i)))
            exec('self.text{}.pack(side=LEFT)'.format(str(i)))
            exec("self.txta{}.pack(side=LEFT)".format(str(i)))
            exec("self.chb{}.pack(side=LEFT)".format(str(i)))
            exec("self.ent{}.pack(side=LEFT)".format(str(i)))
            exec("self.text{}1.pack(side=LEFT)".format(str(i)))
        # Конец таблицы ###################################################

        self.chb8 = self.chb0

        self.fr_results = Frame(self.win, relief=GROOVE, bd=4)
        self.fr_start = Frame(self.fr_results, relief="raised", bd=4, bg="black")
        self.fr_tests = Frame(self.fr_results, relief=GROOVE, bd=1, bg="black")
        self.fr_copy = Frame(self.fr_results, relief="raised", bd=4)
        self.fr_screen = Frame(self.fr_results, relief="raised", bd=4)
        self.fr_logic = Frame(self.win, relief=RIDGE, bd=6)

        self.start_bt = Button(self.fr_start, text="START", font=("Times New Roman", 20), fg="red",
                               activeforeground="#ADFF2F", cursor="hand1", command=self.chek_b1, width=11)
        self.test1 = Button(self.fr_tests, text="Вариант 1", font=("Times New Roman", 14), fg="green",
                            activeforeground="#ADFF2F", cursor="hand1", command=partial(self.tests, 1), width=9)
        self.test2 = Button(self.fr_tests, text="Вариант 2", font=("Times New Roman", 14), fg="orange",
                            activeforeground="#ADFF2F", cursor="hand1", command=partial(self.tests, 2), width=9)
        self.test3 = Button(self.fr_tests, text="Вариант 3", font=("Times New Roman", 14), fg="red",
                            activeforeground="#ADFF2F", cursor="hand1", command=partial(self.tests, 3), width=9)

        self.copy_bt = Button(self.fr_copy, text="Copy", font=('Times New Roman', 20), command=self.copy, width=11)
        self.scr_and_sv = Button(self.fr_screen, text="Save screen", font=("Times New Roman", 20), cursor="pirate",
                                 command=self.screen, width=11)
        self.canvas = Canvas(self.fr_results, relief="ridge", bd=4, height=75, width=100)

        self.text = Text(self.fr_logic, font=("Times New Roman", 12), width=90)
        self.text.insert(END, app_5_10_1.logic)
        self.text["state"] = DISABLED
        self.scr = Scrollbar(self.fr_logic)

        self.chb16["state"] = DISABLED

        self.fr_results.pack(side=LEFT, fill=BOTH)
        self.canvas.pack(side=TOP)

        # Добавим изображение
        self.image = Image.open(self.im)
        self.photo = ImageTk.PhotoImage(self.image)
        self.c_image = self.canvas.create_image(0, 0, image=self.photo, anchor='nw')

        # print(im, image, photo, c_image, sep='\n')

        self.fr_start.pack(side=TOP, pady=10)
        self.start_bt.pack()
        self.fr_tests.pack(side=TOP)
        self.test1.pack()
        self.test2.pack()
        self.test3.pack(pady=4)
        self.fr_screen.pack(side=BOTTOM)
        self.scr_and_sv.pack()
        self.fr_copy.pack(side=BOTTOM)
        self.copy_bt.pack()
        self.fr_logic.pack(side=LEFT, fill=BOTH)
        self.scr.pack(side=RIGHT, fill=Y)
        self.text.pack(side=LEFT, fill=BOTH)

        self.win.config(menu=self.menu_bar)

        self.win.update_idletasks()
        s = self.win.geometry()
        s = s.split('+')
        s = s[0].split('x')
        print(int(s[0]), int(s[1]))
        self.win.mainloop()

    def chek_b1(self):
        v_s = []
        p_s = []
        for l in range(len(app_5_10_1.descriptSig)):
            exec('v_s.append(self.var{}.get())'.format(str(l)))
            exec('p_s.append(self.txt{}.get())'.format(str(l)))

        self.im = app_5_10_1.logik_of_indication(v_s, p_s)
        self.image = Image.open(self.im)
        self.photo = ImageTk.PhotoImage(self.image)
        # c_image = canvas.create_image(60, 160, anchor=NW, image=photo)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

    def tests(self, a):
        if a == 1:
            self.txt0.set(0)
            self.txt1.set(0)
            self.txt2.set(0)
            self.txt3.set(0)
            self.txt4.set(0)
            self.txt5.set(0)
            self.txt6.set(0)
            self.txt7.set(0)
            self.txt8.set(0)
            self.txt9.set(0)
            self.txt10.set(0)
            self.txt11.set(0)
            self.txt12.set(0)
            self.txt13.set(0)
            self.txt14.set(0)
            self.txt15.set(0)
            self.txt16.set(0)
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
            self.var13.set(1)
            self.var14.set(1)
            self.var15.set(1)
        elif a == 2:
            self.txt0.set(1)
            self.txt1.set(1)
            self.txt2.set(1)
            self.txt3.set(1)
            self.txt4.set(0)
            self.txt5.set(0)
            self.txt6.set(0)
            self.txt7.set(0)
            self.txt8.set(0)
            self.txt9.set(0)
            self.txt10.set(0)
            self.txt11.set(0)
            self.txt12.set(0)
            self.txt13.set(0)
            self.txt14.set(0)
            self.txt15.set(0)
            self.txt16.set(0)
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
            self.var13.set(1)
            self.var14.set(1)
            self.var15.set(1)
        elif a == 3:
            self.var0.set(0)
            self.var1.set(0)
            self.var2.set(0)
            self.var3.set(0)
            self.var4.set(0)
            self.var5.set(0)
            self.var6.set(0)
            self.var7.set(0)
            self.var8.set(0)
            self.var9.set(0)
            self.var10.set(0)
            self.var11.set(0)
            self.var12.set(0)
            self.var13.set(0)
            self.var14.set(0)
            self.var15.set(0)


    def logik_of_indication(v_s, p_s):

        for i in p_s:
            if i == 0 or i == 1:
                if v_s[0] == 1:
                    L11V = 1
                    if p_s[0] == 1 or p_s[8] == 1:
                        L11F = 1
                    else:
                        L11F = 0
                else:
                    L11V = 0
                    L11F = 0
                if v_s[1] == 1:
                    L12V = 1
                    if p_s[1] == 1 or p_s[9] == 1:
                        L12F = 1
                    else:
                        L12F = 0
                else:
                    L12V = 0
                    L12F = 0

                if v_s[2] == 1:
                    L21V = 1
                    if p_s[2] == 1 or p_s[10] == 1:
                        L21F = 1
                    else:
                        L21F = 0
                else:
                    L21V = 0
                    L21F = 0

                if v_s[3] == 1:
                    L22V = 1
                    if p_s[3] == 1 or p_s[11] == 1:
                        L22F = 1
                    else:
                        L22F = 0
                else:
                    L22V = 0
                    L22F = 0

                if v_s[4] == 1:
                    R11V = 1
                    if p_s[4] == 1 or p_s[12] == 1:
                        R11F = 1
                    else:
                        R11F = 0
                else:
                    R11V = 0
                    R11F = 0

                if v_s[5] == 1:
                    R12V = 1
                    if p_s[5] == 1 or p_s[13] == 1:
                        R12F = 1
                    else:
                        R12F = 0
                else:
                    R12V = 0
                    R12F = 0

                if v_s[6] == 1:
                    R21V = 1
                    if p_s[6] == 1 or p_s[14] == 1:
                        R21F = 1
                    else:
                        R21F = 0
                else:
                    R21V = 0
                    R21F = 0

                if v_s[7] == 1:
                    R22V = 1
                    if p_s[7] == 1 or p_s[15] == 1:
                        R22F = 1
                    else:
                        R22F = 0
                else:
                    R22V = 0
                    R22F = 0

                if p_s[16] == 1:
                    ans = "Вариант 3"
                    txt = "Нет данных о состоянии канала 1 СДУ. Восстанавливаемый минимальный режим управления. Прямоугольник и номер индицируются янтарным цветом перечёркнутые янтарным крестом."
                    im = 'Indication_5_10_1/Var3.png'
                else:
                    if (L11V + L12V + L21V + L22V + R11V + R12V + R21V + R22V) > 6 and (
                            L11F + L12F + L21F + L22F + R11F + R12F + R21F + R22F) > 3:
                        ans = "Вариант 2"
                        txt = "Отказ канала 1 СДУ. Прямоугольник и номер индицируются янтарным цветом."
                        im = 'Indication_5_10_1/Var2.png'

                    elif (L11V + L12V + L21V + L22V + R11V + R12V + R21V + R22V) < 7 and (
                            L11F + L12F + L21F + L22F + R11F + R12F + R21F + R22F) > 2:
                        ans = "Вариант 2"
                        txt = "Отказ канала 1 СДУ. Прямоугольник и номер индицируются янтарным цветом."
                        im = 'Indication_5_10_1/Var2.png'


                    elif (L11V + L12V + L21V + L22V + R11V + R12V + R21V + R22V) < 5 and (
                            L11F + L12F + L21F + L22F + R11F + R12F + R21F + R22F) > 1:
                        ans = "Вариант 2"
                        txt = "Нормальное состояние канала 1 СДУ. Прямоугольник и номер индицируются зелёным цветом."
                        im = 'Indication_5_10_1/Var2.png'


                    elif (L11V + L12V + L21V + L22V + R11V + R12V + R21V + R22V) < 3 and (
                            L11F + L12F + L21F + L22F + R11F + R12F + R21F + R22F) > 0:
                        ans = "Вариант 2"
                        txt = "Нормальное состояние канала 1 СДУ. Прямоугольник и номер индицируются зелёным цветом."
                        im = 'Indication_5_10_1/Var2.png'


                    elif (L11V + L12V + L21V + L22V + R11V + R12V + R21V + R22V) < 2:
                        ans = "Вариант 3"
                        txt = "Нет данных о состоянии канала 1 СДУ. Восстанавливаемый минимальный режим управления. Прямоугольник и номер индицируются янтарным цветом перечёркнутые янтарным крестом."
                        im = 'Indication_5_10_1/Var3.png'

                    else:
                        ans = "Вариант 1"
                        txt = "Нормальное состояние канала 1 СДУ. Прямоугольник и номер индицируются зелёным цветом."
                        im = 'Indication_5_10_1/Var1.png'


            # print(v_s, "\n", p_s)

            else:
                print("System Error")
                im = 'Indication_5_10_1/Error.png'

            return im

    def screen(self):
        cap = tkcap.CAP(self.win)
        cap.capture("Screenshots/Screen{}.png".format(str(self.count)))
        self.count += 1

    def copy(self):
        # f = open("../../Test_log.txt", "w")
        # f.write(app_6_3_8.logic)
        # f.close()
        pyperclip.copy(app_5_10_1.logic)
        return 0

    def open_main(self):
        self.win.destroy()
        import help
        return 0


