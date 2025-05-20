import re

class Calculator:

    def __init__(self):
        self.answer = ""
        self.start_state = False
        self.plus = False
        self.minus = False
        self.operators = []

    # def clicked1(self):
    #     self.answer += "1"
    #
    # def clicked2():
    #     global answer
    #     global answer
    #     answer += "2"
    #
    # def clicked3():
    #     global answer
    #     answer += "3"
    #
    # def clicked4():
    #     global answer
    #     answer += "4"
    #
    # def clicked5():
    #     global answer
    #     answer += "5"
    #
    # def clicked6():
    #     global answer
    #     answer += "6"
    #
    # def clicked7():
    #     global answer
    #     answer += "7"
    #
    # def clicked8():
    #     global answer
    #     answer += "8"
    #
    # def clicked9():
    #     global answer
    #     answer += "9"
    #
    # def cl_plus():
    #     global answer, operators
    #     operators.append('+')
    #     answer += "+"
    #     lb.configure(text=str(answer))
    #
    # def cl_minus():
    #     global answer, operators
    #     operators.append('-')
    #     answer += "-"
    #     lb.configure(text=str(answer))

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