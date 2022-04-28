#PROBLEM 2
from tkinter import *
def demoColorChange(): btn.configure(bg="yellow", fg="black")
window = Tk()

window.title("Special Midterm Examination in OOP")
window.geometry("500x400+20+10")
btn = Button(window, text = "Click to change color", command=demoColorChange)
btn.place(x= 190, y= 180)


window.mainloop()