import tkinter

from calc import Calculator


class Handler:
    def __init__(self, button1:tkinter.Button, button2:tkinter.Button, button3:tkinter.Button,
                 button4:tkinter.Button, button5:tkinter.Button, button6:tkinter.Button,
                 button7:tkinter.Button, button8:tkinter.Button, button9:tkinter.Button,
                 button_p:tkinter.Button, button_m:tkinter.Button, button_e:tkinter.Button,
                 button_d:tkinter.Button, label: tkinter.Label, calc:Calculator):
        self.button1:tkinter.Button = button1
        self.button2:tkinter.Button = button2
        self.button3:tkinter.Button = button3
        self.button4:tkinter.Button = button4
        self.button5:tkinter.Button = button5
        self.button6:tkinter.Button = button6
        self.button7:tkinter.Button = button7
        self.button8:tkinter.Button = button8
        self.button9:tkinter.Button = button9
        self.button_p:tkinter.Button = button_p
        self.button_m:tkinter.Button = button_m
        self.button_e:tkinter.Button = button_e
        self.button_d:tkinter.Button = button_d
        self.label:tkinter.Label = label
        self.calc: Calculator = calc


    def clicked1(self):
        self.calc.answer += "1"

    def clicked2(self):
        self.calc.answer += "2"

    def clicked3(self):
        self.calc.answer += "3"

    def clicked4(self):
        self.calc.answer += "4"

    def clicked5(self):
        self.calc.answer += "5"

    def clicked6(self):
        self.calc.answer += "6"

    def clicked7(self):
        self.calc.answer += "7"

    def clicked8(self):
        self.calc.answer += "8"

    def clicked9(self):
        self.calc.answer += "9"

    def cl_plus(self):
        self.calc.operators.append('+')
        self.calc.answer += "+"
        self.label.configure(text=str(self.calc.answer))

    def cl_minus(self):
        self.calc.operators.append('-')
        self.calc.answer += "-"
        self.label.configure(text=str(self.calc.answer))

