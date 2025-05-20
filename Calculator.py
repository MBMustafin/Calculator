import tkinter as tk
import re

answer = ""
start_state = False
plus = False
minus = False

operators = []

def clicked1():
    global answer
    answer += "1"

def clicked2():
    global answer
    global answer
    answer += "2"

def clicked3():
    global answer
    answer += "3"

def clicked4():
    global answer
    answer += "4"

def clicked5():
    global answer
    answer += "5"

def clicked6():
    global answer
    answer += "6"

def clicked7():
    global answer
    answer += "7"

def clicked8():
    global answer
    answer += "8"

def clicked9():
    global answer
    answer += "9"

def cl_plus():
    global answer, operators
    operators.append('+')
    answer += "+"
    lb.configure(text=str(answer))


def cl_minus():
    global answer, operators
    operators.append('-')
    answer += "-"
    lb.configure(text=str(answer))

def cl_answer():
    global answer
    temp = re.split(r'[+-]+', answer)
    print(temp)
    number_list = [float(i) for i in temp]
    print(number_list)
    if number_list is not None:
        otvet = float(number_list[0])
        if operators is not None:
            for i in range(0, len(operators)):
                if operators[i] == "+":
                   otvet += float(number_list[i + 1])
                   print(otvet)
                elif operators[i] == '-':
                    otvet -= float(number_list[i + 1])
    else:
        otvet = 0

    enter_lb.configure(text=str(otvet))





def cl_delete():
    global answer
    answer = ""
    enter_lb.configure(text="")
    lb.configure(text="")



window = tk.Tk()
window.title("Калькулятор")
window.geometry('400x400')

# Главный фрейм с растягиванием
frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.9)

# Настройка весов столбцов и строк для растягивания
for i in range(5):
    frame.columnconfigure(i, weight=1)
for i in range(5):
    frame.rowconfigure(i, weight=1)

# Метки
enter_lb = tk.Label(frame, text="0", anchor="e")
enter_lb.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)
lb = tk.Label(frame, text="", anchor="e")
lb.grid(row=1, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)

# Кнопки с растягиванием (sticky="nsew")
button1 = tk.Button(frame, text="1", command=clicked1)
button1.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)
button4 = tk.Button(frame, text="4", command=clicked4)
button4.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)
button7 = tk.Button(frame, text="7", command=clicked7)
button7.grid(row=4, column=0, sticky="nsew", padx=2, pady=2)

button2 = tk.Button(frame, text="2", command=clicked2)
button2.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)
button5 = tk.Button(frame, text="5", command=clicked5)
button5.grid(row=3, column=1, sticky="nsew", padx=2, pady=2)
button8 = tk.Button(frame, text="8", command=clicked8)
button8.grid(row=4, column=1, sticky="nsew", padx=2, pady=2)

button3 = tk.Button(frame, text="3", command=clicked3)
button3.grid(row=2, column=2, sticky="nsew", padx=2, pady=2)
button6 = tk.Button(frame, text="6", command=clicked6)
button6.grid(row=3, column=2, sticky="nsew", padx=2, pady=2)
button9 = tk.Button(frame, text="9", command=clicked9)
button9.grid(row=4, column=2, sticky="nsew", padx=2, pady=2)

button_p = tk.Button(frame, text="+", command=cl_plus)
button_p.grid(row=2, column=3, sticky="nsew", padx=2, pady=2)
button_m = tk.Button(frame, text="-", command=cl_minus)
button_m.grid(row=3, column=3, sticky="nsew", padx=2, pady=2)
button_e = tk.Button(frame, text="=", command=cl_answer)
button_e.grid(row=4, column=3, sticky="nsew", padx=2, pady=2)

button_d = tk.Button(frame, text="C", command=cl_delete)
button_d.grid(row=4, column=4, sticky="nsew", padx=2, pady=2)

window.mainloop()