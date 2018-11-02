from tkinter import *
main = Tk()
main.title("TK Test")
main.geometry("300x200")

lbl = Label(main, text="Label", font = "Arial 20")
lbl.pack()
apple = Button(main, text="Apple", foreground="Red")
apple.pack()
orange = Button(main, text="orange", foreground="Green")
orange.pack()

main.mainloop()
