import tkinter as tk

answer = 0
start_state = False
plus = False
minus = False

def clicked1():
    global answer, plus, minus, start_state
    if start_state is False:
        answer = 1
        start_state = not start_state
    elif plus is True:
        answer += 1
        plus = not plus
    elif minus is True:
        answer -= 1
        minus = not minus
    enter_lb.configure(text=enter_lb.cget("text")+'1')

def clicked2():
    global answer, plus, minus, start_state
    if start_state is False:
        answer = 2
        start_state = not start_state
    elif plus is True:
        answer += 2
        plus = not plus
    elif minus is True:
        answer -= 2
        minus = not minus
    enter_lb.configure(text=enter_lb.cget("text") + '2')

def clicked3():
    global answer, plus, minus, start_state
    if start_state is False:
        answer = 3
        start_state = not start_state
    elif plus is True:
        answer += 3
        plus = not plus
    elif minus is True:
        answer -= 3
        minus = not minus
    enter_lb.configure(text=enter_lb.cget("text") + '3')

def clicked4():
    global answer, plus, minus, start_state
    if start_state is False:
        answer = 4
        start_state = not start_state
    elif plus is True:
        answer += 4
        plus = not plus
    elif minus is True:
        answer -= 4
        minus = not minus
    enter_lb.configure(text=enter_lb.cget("text") + '4')

def clicked5():
    global answer, plus, minus, start_state
    if start_state is False:
        answer = 5
        start_state = not start_state
    elif plus is True:
        answer += 5
        plus = not plus
    elif minus is True:
        answer -= 5
        minus = not minus
    enter_lb.configure(text=enter_lb.cget("text") + '5')

def clicked6():
    global answer, plus, minus, start_state
    if start_state is False:
        answer = 6
        start_state = not start_state
    elif plus is True:
        answer += 6
        plus = not plus
    elif minus is True:
        answer -= 6
        minus = not minus
    enter_lb.configure(text=enter_lb.cget("text") + '6')

def clicked7():
    global answer, plus, minus, start_state
    if start_state is False:
        answer = 7
        start_state = not start_state
    elif plus is True:
        answer += 7
        plus = not plus
    elif minus is True:
        answer -= 7
        minus = not minus
    enter_lb.configure(text=enter_lb.cget("text") + '7')

def clicked8():
    global answer, plus, minus, start_state
    if start_state is False:
        answer = 8
        start_state = not start_state
    elif plus is True:
        answer += 8
        plus = not plus
    elif minus is True:
        answer -= 8
        minus = not minus
    enter_lb.configure(text=enter_lb.cget("text") + '8')

def clicked9():
    global answer, plus, minus, start_state
    if start_state is False:
        answer = 9
        start_state = not start_state
    elif plus is True:
        answer += 9
        plus = not plus
    elif minus is True:
        answer -= 9
        minus = not minus
    enter_lb.configure(text=enter_lb.cget("text") + '9')

def cl_plus():
    global plus
    plus = True
    enter_lb.configure(text=enter_lb.cget("text") + '+')

def cl_minus():
    global minus
    minus = True
    enter_lb.configure(text=enter_lb.cget("text") + '-')

def cl_answer():
    lb.configure(text=answer)

def cl_delete():
    global answer, start_state
    answer = 0
    lb.configure(text=answer)
    enter_lb.configure(text="")
    start_state = False

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
enter_lb = tk.Label(frame, text="", anchor="e")
enter_lb.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)

lb = tk.Label(frame, text="0", anchor="e")
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