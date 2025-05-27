import tkinter as tk
import handler
from handler import Handler


class GUI:

    def __init__(self):
        GUI.сreateWF(self)
        GUI.createButtons(self)
        GUI.createLabels(self)

        self.handler = handler
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
        self.button1 = tk.Button(self.frame, text="1", command=Handler.clicked1())
        self.button1.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)
        self.button4 = tk.Button(self.frame, text="4", command=handler.button4)
        self.button4.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)
        self.button7 = tk.Button(self.frame, text="7", command=handler.button7)
        self.button7.grid(row=4, column=0, sticky="nsew", padx=2, pady=2)

        self.button2 = tk.Button(self.frame, text="2")
        self.button2.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)
        self.button5 = tk.Button(self.frame, text="5")
        self.button5.grid(row=3, column=1, sticky="nsew", padx=2, pady=2)
        self.button8 = tk.Button(self.frame, text="8")
        self.button8.grid(row=4, column=1, sticky="nsew", padx=2, pady=2)

        self.button3 = tk.Button(self.frame, text="3")
        self.button3.grid(row=2, column=2, sticky="nsew", padx=2, pady=2)
        self.button6 = tk.Button(self.frame, text="6")
        self.button6.grid(row=3, column=2, sticky="nsew", padx=2, pady=2)
        self.button9 = tk.Button(self.frame, text="9")
        self.button9.grid(row=4, column=2, sticky="nsew", padx=2, pady=2)

        self.button_p = tk.Button(self.frame, text="+", command=handler.button_p)
        self.button_p.grid(row=2, column=3, sticky="nsew", padx=2, pady=2)
        self.button_m = tk.Button(self.frame, text="-", command=handler.button_m)
        self.button_m.grid(row=3, column=3, sticky="nsew", padx=2, pady=2)
        self.button_e = tk.Button(self.frame, text="=", command=handler.button_e)
        self.button_e.grid(row=4, column=3, sticky="nsew", padx=2, pady=2)

        self.button_d = tk.Button(self.frame, text="C", command=handler.button_d)
        self.button_d.grid(row=4, column=4, sticky="nsew", padx=2, pady=2)

    def createLabels(self):
        self.enter_lb = tk.Label(self.frame, text="0", anchor="e")
        self.enter_lb.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)
        self.lb = tk.Label(self.frame, text="", anchor="e")
        self.lb.grid(row=1, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)

w = GUI()