#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.12
# In conjunction with Tcl version 8.6
#    Apr 22, 2018 06:21:16 PM
import sys
import numpy as np
import matplotlib.pyplot as plt
import tkMessageBox
from tkFileDialog import askopenfilename
from matplotlib.ticker import FuncFormatter

import pandas as pd
import sys
from tkFileDialog import askopenfilename

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

import fo7_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel(root)
    fo7_support.init(root, top)
    root.mainloop()


w = None


def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = New_Toplevel(w)
    fo7_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:

    def browsefunc(self):
        filename = askopenfilename()
        self.Entry1.insert(0, filename)

    def browsefunc1(self):
        filename = askopenfilename()
        self.Entry1_1.insert(0, filename)

    def compare(self):
        if self.Entry1.get() == "" or self.Entry1_1.get() == "":
            tkMessageBox.showinfo("PATH", "PLEASE PROVIDE APPROPRIATE PATH")
        else:
            labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60',
                      '60-70', '70-80', '>80']
            df = pd.read_excel(self.Entry1.get(), sheet_name='Sheet1')
            count = 0
            mk = df['Merit No']
            d = df['Branch']
            a = 0

            for i in df.index:
                if d[i] == "MECHANICAL II":
                    count = count + 1

            aa = 0
            bb = 0
            cc = 0
            dd = 0
            ee = 0
            ff = 0
            gg = 0
            hh = 0
            ii = 0
            n = 0
            a = 0
            p = 0
            na = 0
            s = 0
            m = 0
            nag = 0
            b = 0
            ss = 0
            aaa = 0
            bbb = 0
            i = 0

            for i in df.index:

                for i in df.index:

                    if 0 < mk[i] <= 10000 and d[i] == "MECHANICAL II":
                        n = n + 1
                    else:
                        if 10001 < mk[i] <= 20000 and d[i] == "MECHANICAL II":
                            a = a + 1
                        else:
                            if 20001 < mk[i] <= 30000 and d[i] == "MECHANICAL II":
                                p = p + 1
                            else:
                                if 30001 < mk[i] <= 40000 and d[i] == "MECHANICAL II":
                                    na = na + 1
                                else:
                                    if 40001 < mk[i] <= 50000 and d[i] == "MECHANICAL II":
                                        s = s + 1
                                    else:
                                        if 50001 < mk[i] <= 60000 and d[i] == "MECHANICAL II":
                                            m = m + 1
                                        else:
                                            if 60001 < mk[i] <= 70000 and d[i] == "MECHANICAL II":
                                                nag = nag + 1
                                            else:
                                                if 70001 < mk[i] <= 80000 and d[i] == "MECHANICAL II":
                                                    b = b + 1
                                                else:
                                                    if 80001 < mk[i] and d[i] == "MECHANICAL II":
                                                        ss = ss + 1

            aa = n * 100 / count
            bb = a * 100 / count
            cc = p * 100 / count
            dd = na * 100 / count
            ee = s * 100 / count
            ff = m * 100 / count
            gg = nag * 100 / count
            hh = b * 100 / count
            ii = ss * 100 / count

            sizes = [aa, bb, cc, dd, ee, ff, gg, hh, ii]

            fig, ax = plt.subplots()
            n_groups = 9
            index = np.arange(n_groups)
            bar_width = 0.35
            opacity = 0.8

            rects1 = plt.bar(index, sizes, bar_width,
                             alpha=opacity,
                             color='brown',
                             label='I sheet')

            rects2 = plt.bar(index + bar_width, sizes, bar_width,
                             alpha=opacity,
                             color='yellow',
                             label='II sheet')

            for rect in rects1:
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width() / 2., 0.99 * height,
                        '%d' % int(height) + "%", ha='center', va='bottom')
            for rect in rects2:
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width() / 2., 0.99 * height,
                        '%d' % int(height) + "%", ha='center', va='bottom')

            plt.xlabel('Rank in thousand')
            plt.ylabel('Percentage')
            plt.title('Merit rank analysis')
            plt.xticks(index + bar_width,
                       ('0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '>80'))
            plt.legend()

            plt.tight_layout()
            plt.show()

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        font10 = "-family {Segoe UI} -size 12 -weight bold -slant " \
                 "roman -underline 1 -overstrike 0"
        font11 = "-family {Segoe UI} -size 14 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 12 -weight bold -slant roman" \
                " -underline 0 -overstrike 0"

        top.geometry("796x573+286+112")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.Button1 = Button(top)
        self.Button1.place(relx=0.38, rely=0.24, height=34, width=157)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font9)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''BROWSE''')
        self.Button1.configure(width=157)
        self.Button1.configure(command=self.browsefunc)

        self.Button1_1 = Button(top)
        self.Button1_1.place(relx=0.38, rely=0.51, height=34, width=157)
        self.Button1_1.configure(activebackground="#d9d9d9")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#d9d9d9")
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font=font9)
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''BROWSE''')
        self.Button1_1.configure(command=self.browsefunc1)

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.2, rely=0.37, height=40, relwidth=0.55)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=434)

        self.Entry1_1 = Entry(top)
        self.Entry1_1.place(relx=0.2, rely=0.63, height=40, relwidth=0.55)
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="black")
        self.Entry1_1.configure(insertbackground="black")
        self.Entry1_1.configure(selectbackground="#c4c4c4")
        self.Entry1_1.configure(selectforeground="black")

        self.Button2 = Button(top)
        self.Button2.place(relx=0.31, rely=0.79, height=54, width=237)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font10)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''ANALYZE''')
        self.Button2.configure(width=237)
        self.Button2.configure(command=self.compare)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.26, rely=0.07, height=41, width=354)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''COMPARITIVE ANALYSIS''')
        self.Label1.configure(width=354)


if __name__ == '__main__':
    vp_start_gui()
