from tkinter import *
import random
from tkinter import messagebox as mb
import time

win = Tk()
win.geometry("450x400")
win.title("Cat game")
win.resizable(False, False)

icon = PhotoImage(file=r"D:\Python\tkinter_cat\Python-project\iconCat.png")
win.iconphoto(True, icon)

logo = PhotoImage(file=r"D:\Python\tkinter_cat\Python-project\cat.png")
logo1 = Label(image=logo)

healthCat = 20
leisureCat = 20
disciplineCat = 20
trustCat = 20

name = "Cat"
game = True

var = StringVar()
max_len = 12

def update_clock():
    """The function is responsible for updating the game situation once per second"""
    now = time.strftime("%H:%M:%S")
    label_time.configure(text=now)
    if game == True:
        check_stats()
        win.after(1000, update_clock)

def check_stats():
    global healthCat
    global leisureCat
    global disciplineCat
    global trustCat
    global game

    if healthCat <= 0 or leisureCat <=0 or disciplineCat <=0 or trustCat <=0:
        answer = mb.askyesno(title="You lost", message="Do you want to play again?")
        if answer == True:
            healthCat = 20
            leisureCat = 20
            disciplineCat = 20
            trustCat = 20
        else:
            mb.showinfo(message="Goodbye!")
            game = False
            win.quit()
            return game
        
    elif healthCat >= 100 and leisureCat >= 100 and disciplineCat >= 100 and trustCat >= 100:
        answer = mb.askyesno(title="you win", message="Do you want to play again?")
        if answer == True:
            healthCat = 20
            leisureCat = 20
            disciplineCat = 20
            trustCat = 20
        else:
            mb.showinfo(message="Goodbye!")
            game = False
            win.quit()
            return game
    
    healthCat = healthCat - 2
    leisureCat = leisureCat - 2
    disciplineCat = disciplineCat - 2
    trustCat = trustCat - 2
    l1.configure(text="health - " + str(healthCat) + "%")
    l2.configure(text="leisure - " + str(leisureCat) + "%")
    l3.configure(text="discipline - " + str(disciplineCat) + "%")
    l4.configure(text="trust - " + str(trustCat) + "%")

def health():
    """Changes the health value and updates info"""
    global healthCat
    global leisureCat
    global disciplineCat
    global trustCat

    healthCat = healthCat + 10
    leisureCat = leisureCat - 0
    disciplineCat = disciplineCat - 1
    trustCat = trustCat + 2
    l1.configure(text="health - " + str(healthCat) + "%")
    l2.configure(text="leisure - " + str(leisureCat) + "%")
    l3.configure(text="discipline - " + str(disciplineCat) + "%")
    l4.configure(text="trust - " + str(trustCat) + "%")
    l5.configure(text=f"You fed {name}")

def leisure():
    """Changes the leisure value and updates info"""
    global healthCat
    global leisureCat
    global disciplineCat
    global trustCat

    if healthCat <= 10:
        mb.showwarning(title="Attention", message=f"{name} is hungry")
    else:
        healthCat = healthCat - 2
        leisureCat = leisureCat + 10
        disciplineCat = disciplineCat - 2
        trustCat = trustCat + 1
        l1.configure(text="health - " + str(healthCat) + "%")
        l2.configure(text="leisure - " + str(leisureCat) + "%")
        l3.configure(text="discipline - " + str(disciplineCat) + "%")
        l4.configure(text="trust - " + str(trustCat) + "%")
        l5.configure(text=f"You played with {name}")

def discipline():
    """Changes the discipline value and updates info"""
    global healthCat
    global leisureCat
    global disciplineCat
    global trustCat

    if healthCat <= 10:
        mb.showwarning(title="Attention", message=f"{name} is hungry")
    else:
        healthCat = healthCat - 5
        leisureCat = leisureCat - 3
        disciplineCat = disciplineCat + 10
        trustCat = trustCat - 0
        l1.configure(text="health - " + str(healthCat) + "%")
        l2.configure(text="leisure - " + str(leisureCat) + "%")
        l3.configure(text="discipline - " + str(disciplineCat) + "%")
        l4.configure(text="trust - " + str(trustCat) + "%")
        l5.configure(text=f"You trained {name}")

def trust():
    """Changes the trust value and updates info"""
    global healthCat
    global leisureCat
    global disciplineCat
    global trustCat

    if healthCat <= 10:
        mb.showwarning(title="Attention", message=f"{name} is hungry")
    else:
        healthCat = healthCat - 3
        leisureCat = leisureCat + 1
        disciplineCat = disciplineCat - 2
        trustCat = trustCat + 10
        l1.configure(text="health - " + str(healthCat) + "%")
        l2.configure(text="leisure - " + str(leisureCat) + "%")
        l3.configure(text="discipline - " + str(disciplineCat) + "%")
        l4.configure(text="trust - " + str(trustCat) + "%")
        l5.configure(text=f"You caressed {name}")

def entry_restriction(*args):
    """Create restriction to the amount of characters (for Entry widget)"""
    string = var.get()
    if len(string) > max_len:
        var.set(string[:max_len])

var.trace_variable("w", entry_restriction)

label_info = Label(width=27, height=3, text=f"This is your {name}",font="Arial")
label_time = Label(width=20,height=3,text=None)
b1 = Button(width=15,text="feed",command=health)
b2 = Button(width=15,text="caress",command=trust)
b3 = Button(width=15,text="train",command=discipline)
b4 = Button(width=15,text="play",command=leisure)
b5 = Button(width=15,text="Exit",command=quit)
l1 = Label(width=20,height=2,text="health - " + str(healthCat) + "%")
l2 = Label(width=20,height=2,text="leisure - " + str(leisureCat) + "%")
l3 = Label(width=20,height=2,text="discipline - " + str(disciplineCat) + "%")
l4 = Label(width=20,height=2,text="trust - " + str(trustCat) + "%")
l5 = Label(width=20,height=2,text=f"your {name} is alive")

def get_name():
    """Get the name from Entry element, then delete previous elements and display the main game"""
    global name 
    global game
    if entry_field.get() == "":
        name = "Cat"
    else:
        name = entry_field.get()
    entry_field.destroy()
    button_for_name.destroy()
    label_for_name.destroy()
    label_info.configure(text=f"This is your {name}",font="Arial")
    l5.configure(text=f"your {name} is alive")
    label_info.grid(row=0, column=2, columnspan=3, rowspan=2)
    label_time.grid(row=0,column=0)
    b1.grid(row=2,column=0)
    b2.grid(row=3,column=0)
    b3.grid(row=4,column=0)
    b4.grid(row=5,column=0)
    b5.grid(row=9,column=3)
    l1.grid(row=6,column=0)
    l2.grid(row=7,column=0)
    l3.grid(row=8,column=0)
    l4.grid(row=9,column=0)
    l5.grid(row=7,column=3)
    logo1.grid(row=2, column=2, columnspan=5, rowspan=5)
    update_clock()

# Initialize hidden elemnts of the main game

hidden_elements = [label_info, label_time,
                   b1, b2, b3, b4, b5, l1,
                   l2, l3, l4, l5, logo1]

for element in hidden_elements:
    element = element.grid_forget()

entry_field = Entry(width=10,font=("Tahoma", 14),textvariable=var)
button_for_name = Button(width=20, height=1, text="name", command=get_name)
label_for_name = Label(width=25, height=3, text="Not more than 12 characters")
label_for_name.grid(row=0, column=1, columnspan=3,)
entry_field.grid(row=1, column=0, padx=25, pady=5)
button_for_name.grid(row=1, column=3, columnspan=3, padx=5, pady=5)

win.mainloop()
