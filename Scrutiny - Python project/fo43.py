#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.12
# In conjunction with Tcl version 8.6
#    Apr 04, 2018 11:39:24 PM

import sys
import matplotlib.pyplot as plt
import tkMessageBox
from tkFileDialog import askopenfilename
import fo73
import subprocess
import pandas as pd
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

import fo3_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel(root)
    fo3_support.init(root, top)
    root.mainloop()


w = None


def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = New_Toplevel(w)
    fo3_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:

    def com(self):
        subprocess.call(" python fO73.py 1", shell=True)

    def browsefunc(self):
        filename = askopenfilename()
        self.Entry1.insert(0, filename)

    def gender(self):
        if (self.Entry1.get() == ""):
            tkMessageBox.showinfo("PATH", "PLEASE PROVIDE APPROPRIATE PATH")
        else:
            labels = ['MALE', 'FEMALE']
            colors = ['red', 'green']
            count = 0

            m = 0
            f = 0
            a = 0
            b = 0
            df = pd.read_excel(self.Entry1.get(), sheet_name='Sheet1')
            g = df['Gender']
            d = df['Branch']
            a = 0

            for i in df.index:
                if d[i] == "COMPUTER":
                    count = count + 1

            for i in df.index:
                if g[i] == "Male" and d[i] == "COMPUTER":
                    a = a + 1
                elif g[i] == "MALE" and d[i] == "COMPUTER":
                    a = a + 1
                elif g[i] == "Female" and d[i] == "COMPUTER":
                    b = b + 1
                elif g[i] == "Female" and d[i] == "COMPUTER":
                    b = b + 1




            m = a * 100 / count
            f = b * 100 / count
            sizes = [m, f]

            plt.title('Gender Analysis')
            plt.pie(sizes, labels=labels, colors=colors, shadow=True, autopct='%.3f')
            plt.show()

    def university(self):

        if (self.Entry1.get() == ""):
            tkMessageBox.showinfo("PATH", "PLEASE PROVIDE APPROPRIATE PATH")
        else:
            labels = ['North Maharashtra', 'Amravati', 'Pune', 'NA', 'S.R.T.M.U', 'Mumbai', 'Nagpur', 'B.A.M.U',
                      'Shivaji']
            colors = ['red', 'green', 'yellow', 'blue', 'orange', 'violet', 'pink', 'lightskyblue', 'cyan']
            count = 0

            m = 0
            f = 0
            a = 0
            b = 0
            df = pd.read_excel(self.Entry1.get(), sheet_name='Sheet1')
            h = df['Home University']
            d = df['Branch']
            a = 0

            for i in df.index:
                if d[i] == "COMPUTER":
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
            for i in df.index:
                    if h[i] == "North Maharashtra" and d[i] == "COMPUTER":
                        n = n + 1
                    elif h[i] == "NORTH MAHARASHTRA" and d[i] == "COMPUTER":
                        n = n + 1
                    elif h[i] == "Amravati" and d[i] == "COMPUTER":
                        a = a + 1
                    elif h[i] == "AMRAVATI" and d[i] == "COMPUTER":
                        a = a + 1
                    elif h[i] == "Pune" and d[i] == "COMPUTER":
                        p = p + 1
                    elif h[i] == "PUNE" and d[i] == "COMPUTER":
                        p = p + 1
                    elif h[i] == "NA" and d[i] == "COMPUTER":
                        na = na + 1
                    elif h[i] == "na" and d[i] == "COMPUTER":
                        na = na + 1
                    elif h[i] == "S.R.T.M.U." and d[i] == "COMPUTER":
                        s = s + 1
                    elif h[i] == "Mumbai" and d[i] == "COMPUTER":
                        m = m + 1
                    elif h[i] == "MUMBAI" and d[i] == "COMPUTER":
                        m = m + 1
                    elif h[i] == "Nagpur" and d[i] == "COMPUTER":
                        nag = nag + 1
                    elif h[i] == "NAGPUR" and d[i] == "COMPUTER":
                        nag = nag + 1
                    elif h[i] == "B.A.M.U." and d[i] == "COMPUTER":
                        b = b + 1
                    elif h[i] == "Shivaji + Solapur" and d[i] == "COMPUTER":
                        ss = ss + 1
                    elif h[i] == "SHIVAJI + SOLAPUR" and d[i] == "COMPUTER":
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
            plt.title('University Analysis')
            plt.pie(sizes, labels=labels, colors=colors, shadow=True, autopct='%0.3f')
            plt.axis('equal')
            plt.show()

    def category(self):

        if (self.Entry1.get() == ""):
            tkMessageBox.showinfo("PATH", "PLEASE PROVIDE APPROPRIATE PATH")
        else:
            labels = ['OPEN', 'DT/VJ', 'SC', 'OBC', 'NT 2(NT-C)', 'NT 3(NT-D)', 'ST', 'NA', 'NT 1(NT-B)']
            colors = ['red', 'green', 'yellow', 'blue', 'orange', 'violet', 'pink', 'lightskyblue', 'cyan']
            count = 0
            df = pd.read_excel(self.Entry1.get(), sheet_name='Sheet1')
            c = df['Category']
            d = df['Branch']
            a = 0

            for i in df.index:
                if d[i] == "COMPUTER":
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


            for i in df.index:
                if c[i] == "Open" and d[i] == "COMPUTER":
                    n = n + 1
                elif c[i] == "OPEN" and d[i] == "COMPUTER":
                    n = n + 1
                elif c[i] == "DT/VJ" and d[i] == "COMPUTER":
                    a = a + 1
                elif c[i] == "SC" and d[i] == "COMPUTER":
                    p = p + 1
                elif c[i] == "OBC" and d[i] == "COMPUTER":
                    na = na + 1
                elif c[i] == "NT 2 (NT-C)" and d[i] == "COMPUTER":
                    s = s + 1
                elif c[i] == "NT 2(NT-C)" and d[i] == "COMPUTER":
                    s = s + 1
                elif c[i] == "NT 3 (NT-D)" and d[i] == "COMPUTER":
                    m = m + 1
                elif c[i] == "NT 3(NT-D)" and d[i] == "COMPUTER":
                    m = m + 1
                elif c[i] == "ST" and d[i] == "COMPUTER":
                    nag = nag + 1
                elif c[i] == "NA" and d[i] == "COMPUTER":
                    b = b + 1
                elif c[i] == "NT 1 (NT-B)" and d[i] == "COMPUTER":
                    ss = ss + 1
                elif c[i] == "NT 1(NT-B)" and d[i] == "COMPUTER":
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

            plt.pie(sizes, labels=labels, colors=colors, shadow=True, autopct='%0.3f')
            plt.title('Category Analysis')
            plt.axis('equal')
            plt.show()

    def meritrank(self):

        if (self.Entry1.get() == ""):
            tkMessageBox.showinfo("PATH", "PLEASE PROVIDE APPROPRIATE PATH")
        else:
            labels = ['0-10,000', '10,001-20,000', '20,001-30,000', '30,001-40,000', '40,001-50,000', '50,001-60,000',
                      '60,001-70,000', '70,001-80,000', '>80,001']
            colors = ['red', 'green', 'yellow', 'blue', 'orange', 'violet', 'pink', 'lightskyblue', 'cyan']
            df = pd.read_excel(self.Entry1.get(), sheet_name='Sheet1')
            count = 0
            mk = df['Merit No']
            d = df['Branch']
            a = 0

            for i in df.index:
                if d[i] == "COMPUTER":
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
            i =0

            for i in df.index:

                if 0 < mk[i] <= 10000 and d[i] == "COMPUTER":
                    n = n + 1
                else:
                    if 10001 < mk[i] <= 20000 and d[i] == "COMPUTER":
                        a = a + 1
                    else:
                        if 20001 < mk[i] <= 30000 and d[i] == "COMPUTER":
                            p = p + 1
                        else:
                            if 30001 < mk[i] <= 40000 and d[i] == "COMPUTER":
                                na = na + 1
                            else:
                                if 40001 < mk[i] <= 50000 and d[i] == "COMPUTER":
                                    s = s + 1
                                else:
                                    if 50001 < mk[i] <= 60000 and d[i] == "COMPUTER":
                                        m = m + 1
                                    else:
                                        if 60001 < mk[i] <= 70000 and d[i] == "COMPUTER":
                                            nag = nag + 1
                                        else:
                                            if 70001 < mk[i] <= 80000 and d[i] == "COMPUTER":
                                                b = b + 1
                                            else:
                                                if 80001 < mk[i] and d[i] == "COMPUTER":
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

            plt.pie(sizes, labels=labels, colors=colors, shadow=True, autopct='%0.3f')
            plt.title('Merit Rank Analysis')
            plt.axis('equal')
            plt.show()

    def merit12(self):
        if (self.Entry1.get() == ""):
            tkMessageBox.showinfo("PATH", "PLEASE PROVIDE APPROPRIATE PATH")
        else:
            labels = ['40%-50%', '50%-60%', '60%-70%', '70%-80%', '80%-90%', '90%-100%']
            colors = ['red', 'green', 'yellow', 'blue', 'pink', 'cyan']


            df = pd.read_excel(self.Entry1.get(), sheet_name='Sheet1')
            count = 0
            ma = df['12th']
            d = df['Branch']
            a = 0

            for i in df.index:
                if d[i] == "COMPUTER":
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
            for i in df.index:

                if 40 < ma[i] <= 50 and d[i] == "COMPUTER":
                    n = n + 1
                else:
                    if 50.001 < ma[i] <= 60 and d[i] == "COMPUTER":
                        a = a + 1
                    else:
                        if 60.001 < ma[i] <= 70 and d[i] == "COMPUTER":
                            p = p + 1
                        else:
                            if 70.001 < ma[i] <= 80 and d[i] == "COMPUTER":
                                na = na + 1
                            else:
                                if 80.001 < ma[i] <= 90 and d[i] == "COMPUTER":
                                    s = s + 1
                                else:
                                    if 90.001 < ma[i] <= 100 and d[i] == "COMPUTER":
                                        m = m + 1

            aa = n * 100 / count
            bb = a * 100 / count
            cc = p * 100 / count
            dd = na * 100 / count
            ee = s * 100 / count
            ff = m * 100 / count

            sizes = [aa, bb, cc, dd, ee, ff]

            plt.pie(sizes, labels=labels, colors=colors, shadow=True, autopct='%0.3f')
            plt.title('12th Merit Analysis')
            plt.axis('equal')
            plt.show()

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        font9 = "-family {Segoe UI} -size 12 -weight bold -slant roman" \
                " -underline 1 -overstrike 0"

        top.geometry("1139x640+109+115")
        top.title("New Toplevel")
        top.configure(background="#595959")

        self.Label1 = Label(top)
        self.Label1.place(relx=0.27, rely=0.36, height=41, width=474)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''ANALYZE''')
        self.Label1.configure(width=474)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.04, rely=0.56, height=44, width=187)
        self.Button1.configure(activebackground="#176b0e")
        self.Button1.configure(activeforeground="white")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''GENDER''')
        self.Button1.configure(command=self.gender)
        self.Button1.configure(width=187)

        self.Button1_1 = Button(top)
        self.Button1_1.place(relx=0.42, rely=0.56, height=44, width=187)
        self.Button1_1.configure(activebackground="#176b0e")
        self.Button1_1.configure(activeforeground="white")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#d9d9d9")
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''HOME UNIVERSITY''')
        self.Button1_1.configure(command=self.university)

        self.Button1_1_1 = Button(top)
        self.Button1_1_1.place(relx=0.23, rely=0.56, height=44, width=187)
        self.Button1_1_1.configure(activebackground="#176b0e")
        self.Button1_1_1.configure(activeforeground="white")
        self.Button1_1_1.configure(activeforeground="#000000")
        self.Button1_1_1.configure(background="#d9d9d9")
        self.Button1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1_1.configure(foreground="#000000")
        self.Button1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1_1.configure(highlightcolor="black")
        self.Button1_1_1.configure(pady="0")
        self.Button1_1_1.configure(text='''CATEGORY''')
        self.Button1_1_1.configure(command=self.category)

        self.Button1_1_1_1 = Button(top)
        self.Button1_1_1_1.place(relx=0.61, rely=0.56, height=44, width=187)
        self.Button1_1_1_1.configure(activebackground="#176b0e")
        self.Button1_1_1_1.configure(activeforeground="white")
        self.Button1_1_1_1.configure(activeforeground="#000000")
        self.Button1_1_1_1.configure(background="#d9d9d9")
        self.Button1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1_1_1.configure(foreground="#000000")
        self.Button1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1_1_1.configure(highlightcolor="black")
        self.Button1_1_1_1.configure(pady="0")
        self.Button1_1_1_1.configure(text='''MERIT RANK''')
        self.Button1_1_1_1.configure(command=self.meritrank)

        self.Button1_1_1_1_1 = Button(top)
        self.Button1_1_1_1_1.place(relx=0.81, rely=0.56, height=44, width=187)
        self.Button1_1_1_1_1.configure(activebackground="#176b0e")
        self.Button1_1_1_1_1.configure(activeforeground="white")
        self.Button1_1_1_1_1.configure(activeforeground="#000000")
        self.Button1_1_1_1_1.configure(background="#d9d9d9")
        self.Button1_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1_1_1_1.configure(foreground="#000000")
        self.Button1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1_1_1_1.configure(highlightcolor="black")
        self.Button1_1_1_1_1.configure(pady="0")
        self.Button1_1_1_1_1.configure(text='''12TH MERIT''')
        self.Button1_1_1_1_1.configure(command=self.merit12)

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.17, rely=0.08, height=40, relwidth=0.6)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Button2 = Button(top)
        self.Button2.place(relx=0.39, rely=0.19, height=34, width=217)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''BROWSE PATH''')
        self.Button2.configure(width=217)
        self.Button2.configure(command=self.browsefunc)

        self.Button1_1_1_1_1_1 = Button(top)
        self.Button1_1_1_1_1_1.place(relx=0.32, rely=0.8, height=44, width=397)
        self.Button1_1_1_1_1_1.configure(activebackground="#176b0e")
        self.Button1_1_1_1_1_1.configure(activeforeground="white")
        self.Button1_1_1_1_1_1.configure(activeforeground="#000000")
        self.Button1_1_1_1_1_1.configure(background="#d9d9d9")
        self.Button1_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1_1_1_1_1.configure(font=10)
        self.Button1_1_1_1_1_1.configure(foreground="#000000")
        self.Button1_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1_1_1_1_1.configure(highlightcolor="black")
        self.Button1_1_1_1_1_1.configure(pady="0")
        self.Button1_1_1_1_1_1.configure(text='''COMPARITIVE ANALYSIS''')
        self.Button1_1_1_1_1_1.configure(width=397)
        self.Button1_1_1_1_1_1.configure(command=self.com)


if __name__ == '__main__':
    vp_start_gui()
