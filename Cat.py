from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox as mb
import time

root = Tk()
root.geometry('400x330')
root.title('CAT')

icon = PhotoImage(file="iconCat.png")
root.iconphoto(False, icon)

logo = PhotoImage(file="Cat.png")
logo1 = Label(image=logo)

healthCat = 20
leisureCat = 20
game = True

def update_clock():
    """Функція відповідає за оновлення ігрової ситуації раз на секунду"""
    now = time.strftime("%H:%M:%S")
    root.after(1000, update_clock)
    root.after(1000, heppimin)

def heppimin():
    global healthCat
    global leisureCat
    global game

    if healthCat <= 0 or leisureCat <=0:
        answer = mb.askyesno(title="You lost", message="Do you want to play again?")
        if answer == True:
            healthCat += 50
            leisureCat += 50
        else:
            game = False
            return game
    elif healthCat >= 100 and leisureCat >= 100:
        answer2 = mb.askyesno(title="you win", message="Do you want to play again?")
        if answer2 == True:
            healthCat -= 50
            leisureCat -= 50
        else:
            game = False
            return game
    
    healthCat = healthCat - 3
    leisureCat = leisureCat - 3
    l1.configure(text="health - " + str(healthCat) + "%")
    l2.configure(text="leisure - " + str(leisureCat) + "%")

def health():
    global healthCat
    global leisureCat
    healthCat = healthCat + 10
    leisureCat = leisureCat - 2
    l1.configure(text="health - " + str(healthCat) + "%")
    l2.configure(text="leisure - " + str(leisureCat) + "%")
    l3.configure(text="your cat is health")
    if leisureCat <= 10:
        mb.showerror("Sorry", "your Cat is sad")
        leisureCat = leisureCat + 20

def leisure():
    global healthCat
    global leisureCat
    healthCat = healthCat - 2
    leisureCat = leisureCat + 10
    l1.configure(text="health - " + str(healthCat) + "%")
    l2.configure(text="leisure - " + str(leisureCat) + "%")
    l3.configure(text="your cat is laisure")
    if healthCat <= 10:
        mb.showerror("Sorry", "your Cat is ill")
        healthCat = healthCat + 20

while game == True:

    label2 = Label(width=27, height=3, text="It is your Cat",font="Arial")
    b1 = ttk.Button(width=15,text="feed",command=health)
    b2 = ttk.Button(width=15,text="caress",command=leisure)
    b3 = ttk.Button(width=15,text="train",command=health)
    b4 = ttk.Button(width=15,text="play",command=leisure)
    b5 = ttk.Button(width=15,text="Exit",command=quit)
    l1 = Label(width=20,height=3,text="health - " + str(healthCat) + "%")
    l2 = Label(width=20,height=2,text="leisure - " + str(leisureCat) + "%")
    l3 = Label(width=20,height=2,text="your cat is alive")

    label2.grid(row=0, column=2, columnspan=3, rowspan=2)
    b1.grid(row=2,column=0)
    b2.grid(row=3,column=0)
    b3.grid(row=4,column=0)
    b4.grid(row=5,column=0)
    b5.grid(row=9,column=3)
    l1.grid(row=6,column=0)
    l2.grid(row=7,column=0)
    l3.grid(row=7,column=3)
    logo1.grid(row=2, column=2, columnspan=5, rowspan=5)

    update_clock()
    root.mainloop()
else:
    mb.showinfo(text="Goodbye!")