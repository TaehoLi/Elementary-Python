from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog

main = Tk()

def btnclick():
    name = tkinter.simpledialog.askstring("질문", "이름을 입력하시오")
    age = tkinter.simpledialog.askinteger("질문", "나이를 입력하시오")
    if name and age:
        tkinter.messagebox.showwarning("환영", str(age) + "세 " + name + "님 반갑습니다.")

btn = Button(main, text="클릭", foreground="Blue", command = btnclick)
btn.pack()

main.mainloop()
