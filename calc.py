import re

class Calculator:

    def __init__(self):
        self.answer = ""
        self.start_state = False
        self.plus = False
        self.minus = False
        self.operators = []


    def cl_answer(self):
        temp = re.split(r'[+-]+', self.answer)
        print(temp)
        number_list = [float(i) for i in temp]
        print(number_list)
        if number_list is not None:
            otvet = float(number_list[0])
            if self.operators is not None:
                for i in range(0, len(self.operators)):
                    if self.operators[i] == "+":
                        otvet += float(number_list[i + 1])
                        print(otvet)
                    elif self.operators[i] == '-':
                        otvet -= float(number_list[i + 1])
        else:
            otvet = 0


    #
    # def cl_delete():
    #     global answer
    #     answer = ""
    #     enter_lb.configure(text="")
    #     lb.configure(text="")