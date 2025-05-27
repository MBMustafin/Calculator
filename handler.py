import tkinter as tk
from locale import windows_locale


class Handler:
    def clicked1(self):
        self.answer += "1"

    def clicked2(self):
        global answer
        global answer
        answer += "2"

    def clicked3(self):
        global answer
        answer += "3"

    def clicked4(self):
        global answer
        answer += "4"

    def clicked5(self):
        global answer
        answer += "5"

    def clicked6(self):
        global answer
        answer += "6"

    def clicked7(self):
        global answer
        answer += "7"

    def clicked8(self):
        global answer
        answer += "8"

    def clicked9(self):
        global answer
        answer += "9"

    def cl_plus(self):
        global answer, operators
        operators.append('+')
        answer += "+"
        lb.configure(text=str(answer))

    def cl_minus(self):
        global answer, operators
        operators.append('-')
        answer += "-"
        lb.configure(text=str(answer))

