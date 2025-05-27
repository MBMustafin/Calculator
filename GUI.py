import tkinter
import tkinter as tk

from calc import Calculator
from handler import Handler


class GUI:

    def __init__(self):
        GUI.сreateWF(self)
        self.calc = Calculator()
        self.handler = Handler(self.button1, self.button2, self.button3,
                               self.button4, self.button5, self.button6,
                               self.button7, self.button8, self.button9,
                               self.button_p, self.button_m, self.button_e, self.button_d, self.label, self.calc)

        GUI.createButtons(self)
        GUI.createLabels(self)

        self.window.mainloop()

    def сreateWF(self):
        self.window = tk.Tk()
        self.window.geometry('400x400')

        self.frame = tk.Frame(self.window)
        self.frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.9)

        for i in range(5):
            self.frame.columnconfigure(i, weight=1)
        for i in range(5):
            self.frame.rowconfigure(i, weight=1)

    def createButtons(self):
        self.button1 = tk.Button(self.frame, text="1", command=self.handler.clicked1())
        self.button1.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)
        self.button4 = tk.Button(self.frame, text="4", command=self.handler.clicked4())
        self.button4.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)
        self.button7 = tk.Button(self.frame, text="7", command=self.handler.clicked7())
        self.button7.grid(row=4, column=0, sticky="nsew", padx=2, pady=2)

        self.button2 = tk.Button(self.frame, text="2", command=self.handler.clicked2())
        self.button2.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)
        self.button5 = tk.Button(self.frame, text="5", command=self.handler.clicked5())
        self.button5.grid(row=3, column=1, sticky="nsew", padx=2, pady=2)
        self.button8 = tk.Button(self.frame, text="8", command=self.handler.clicked8())
        self.button8.grid(row=4, column=1, sticky="nsew", padx=2, pady=2)

        self.button3 = tk.Button(self.frame, text="3", command=self.handler.clicked3())
        self.button3.grid(row=2, column=2, sticky="nsew", padx=2, pady=2)
        self.button6 = tk.Button(self.frame, text="6", command=self.handler.clicked6())
        self.button6.grid(row=3, column=2, sticky="nsew", padx=2, pady=2)
        self.button9 = tk.Button(self.frame, text="9", command=self.handler.clicked9())
        self.button9.grid(row=4, column=2, sticky="nsew", padx=2, pady=2)

        self.button_p = tk.Button(self.frame, text="+", command=self.handler.cl_plus())
        self.button_p.grid(row=2, column=3, sticky="nsew", padx=2, pady=2)
        self.button_m = tk.Button(self.frame, text="-", command=self.handler.cl_minus())
        self.button_m.grid(row=3, column=3, sticky="nsew", padx=2, pady=2)
        self.button_e = tk.Button(self.frame, text="=", command=self.handler.calc.cl_answer())
        self.button_e.grid(row=4, column=3, sticky="nsew", padx=2, pady=2)

        self.button_d = tk.Button(self.frame, text="C", command=self.handler.button_d())
        self.button_d.grid(row=4, column=4, sticky="nsew", padx=2, pady=2)

    def createLabels(self):
        self.enter_lb = tk.Label(self.frame, text="0", anchor="e")
        self.enter_lb.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)
        self.label = tk.Label(self.frame, text="", anchor="e")
        self.label.grid(row=1, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)

w = GUI()

















