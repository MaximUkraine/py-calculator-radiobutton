# Copyright (c) 2023 Maxim
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import tkinter.messagebox
from tkinter import Tk,Entry,Radiobutton,Button,Label,IntVar,messagebox,mainloop

if __name__ == "__main__":
    window = Tk()
    window.title("Калькулятор")
    window.geometry("300x400")

    action = IntVar()
    action.set(0)

    entry1 = Entry(font=("Consolas", 15), justify="right")
    entry1.place(x=50, y=20, width=200, height=30)
    entry2 = Entry(font=("Consolas", 15), justify="right")
    entry2.place(x=50, y=70, width=200, height=30)

    add_rb = Radiobutton(text="Додати", font=("Consolas", 15), variable=action, value=0)
    add_rb.place(x=50, y=110)
    subtract_rb = Radiobutton(text="Відняти", font=("Consolas", 15), variable=action, value=1)
    subtract_rb.place(x=50, y=140)
    multiple_rb = Radiobutton(text="Помножити", font=("Consolas", 15), variable=action, value=2)
    multiple_rb.place(x=50, y=170)
    divide_rb = Radiobutton(text="Поділити", font=("Consolas", 15), variable=action, value=3)
    divide_rb.place(x=50, y=200)

    info_label = Label(text="Введіть числа,\nвиберіть операцію\nта нажміть Обчислити", font=("Consolas", 15))
    info_label.place(x=45, y=290)

    def click():
        try:
            a = float(entry1.get())
            b = float(entry2.get())
            if (action.get() == 0):
                result = a + b
            elif (action.get() == 1):
                result = a - b
            elif (action.get() == 2):
                result = a * b
            else:
                if (b == 0):
                    result = "Не можна ділити на 0"
                else:
                    result = a / b
        except ValueError:
            result = "Ви не ввели числа!"
        info_label.config(text=str(result))

    button = Button(text="Обчислити", font=("Consolas", 12), command=click)
    button.place(x=50, y=240, width=200, height=30)

    mainloop()
