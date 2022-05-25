from tkinter import * 
import time


root = Tk()
root.title('ClockApp')
root.geometry("600x400")

def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    
    label2.config(text=hour + ":" + minute + ":" + second)
    label2.after(1000, clock)

def update():
    label2.config(text="New Text")

label2 = Label(root, text="", font=("Times", 48), fg="blue", bg="black")
label2.pack(pady=20)

clock()

#label2.after(5000, update)





root.mainloop()
