from tkinter import *
from tkinter import messagebox as mb
import time
import random
import pandas as pd

events = pd.read_csv(r"D:\Python\tkinter_cat\Python-project\Events.csv")

win = Tk()
win.configure(bg="lightblue")
win.geometry("450x500")
win.title("Cat trainer")
win.resizable(False, False)

icon = PhotoImage(file=r"D:\Python\tkinter_cat\Python-project\iconCat.png")
win.iconphoto(True, icon)

logo = PhotoImage(file=r"D:\Python\tkinter_cat\Python-project\cat.png")
logo1 = Label(image=logo)

healthCat = 20
leisureCat = 20
disciplineCat = 20
trustCat = 20

start_time = None
click_flag = False

name = "Cat"

var = StringVar()
max_len = 12

def get_event(df):
    """Gets random event from the dataframe and change values accrodingly"""
    global healthCat
    global leisureCat
    global disciplineCat
    global trustCat

    event_number = random.randint(0,9)
    label_event_info.configure(text=df.at[event_number, "text"])
    if healthCat + df.at[event_number, "health"] >= 150:
        healthCat = 150
    else:
        healthCat += df.at[event_number, "health"]
    if leisureCat + df.at[event_number, "leisure"] >= 150:
        leisureCat = 150
    else:
        leisureCat += df.at[event_number, "leisure"]
    if disciplineCat + df.at[event_number, "discipline"] >= 150:
        disciplineCat = 150
    else:
        disciplineCat += df.at[event_number, "discipline"]
    if trustCat + df.at[event_number, "trust"] >= 150:
        trustCat = 150
    else:   
        trustCat += df.at[event_number, "trust"]
    l1.configure(text="health - " + str(healthCat) + "%")
    l2.configure(text="leisure - " + str(leisureCat) + "%")
    l3.configure(text="discipline - " + str(disciplineCat) + "%")
    l4.configure(text="trust - " + str(trustCat) + "%")

def update_event():
    """Recursive call for get_event function"""
    get_event(events)
    win.after(4000, update_event)

def check_stats():
    """Checks the stats of the pet, control buttons for actions and quit the game if answer is False"""
    global healthCat
    global leisureCat
    global disciplineCat
    global trustCat

    end_time = time.time()

    if healthCat <= 0 or leisureCat <= 0 or disciplineCat <= 0 or trustCat <= 0:
        answer = mb.askyesno(title="You lost", message="Do you want to play again?")
        if answer == True:
            healthCat = 20
            leisureCat = 20
            disciplineCat = 20
            trustCat = 20
            l1.configure(text="health - " + str(healthCat) + "%")
            l2.configure(text="leisure - " + str(leisureCat) + "%")
            l3.configure(text="discipline - " + str(disciplineCat) + "%")
            l4.configure(text="trust - " + str(trustCat) + "%")
        else:
            result_time = end_time - start_time
            result_time = time.strftime("%H:%M:%S", time.gmtime(result_time))
            mb.showinfo(message=f"Goodbye!, you spent {result_time} time with your pet")
            win.quit()
    
    elif healthCat >= 100 and leisureCat >= 100 and disciplineCat >= 100 and trustCat >= 100:
        answer = mb.askyesno(title="you win", message="Do you want to play again?")
        if answer == True:
            healthCat = 20
            leisureCat = 20
            disciplineCat = 20
            trustCat = 20
            l1.configure(text="health - " + str(healthCat) + "%")
            l2.configure(text="leisure - " + str(leisureCat) + "%")
            l3.configure(text="discipline - " + str(disciplineCat) + "%")
            l4.configure(text="trust - " + str(trustCat) + "%")
        else:
            result_time = end_time - start_time
            result_time = time.strftime("%H:%M:%S", time.gmtime(result_time))
            mb.showinfo(message=f"Goodbye!, you spent {result_time} time with your pet")
            win.quit()
    
    if healthCat <= 10:
        label_info.configure(text=f"Attention!\n{name}\nis hungry")
    else:
        label_info.configure(text=f"{name}\nis sated")

def update_gui():
    """Recursive call for check_stats function"""
    check_stats()
    win.after(1000, update_gui)

def health():
    """Changes the health value and updates info"""
    global healthCat
    global leisureCat
    global disciplineCat
    global trustCat
    global click_flag

    if healthCat + 10 >= 150:
        healthCat = 150
    else:
        healthCat += 10
    leisureCat -= 0
    disciplineCat -= 1
    trustCat += 2
    l1.configure(text="health - " + str(healthCat) + "%")
    l2.configure(text="leisure - " + str(leisureCat) + "%")
    l3.configure(text="discipline - " + str(disciplineCat) + "%")
    l4.configure(text="trust - " + str(trustCat) + "%")
    l5.configure(text=f"You fed {name}")
    click_flag = True
    click_block(click_flag)

def leisure():
    """Changes the leisure value and updates info"""
    global healthCat
    global leisureCat
    global disciplineCat
    global trustCat
    global click_flag

    if healthCat <= 10:
        pass
    else:
        if leisureCat + 10 >= 150:
            leisureCat = 150
        else:
            leisureCat += 10
        healthCat -= 2
        disciplineCat -= 2
        trustCat += 1
        l1.configure(text="health - " + str(healthCat) + "%")
        l2.configure(text="leisure - " + str(leisureCat) + "%")
        l3.configure(text="discipline - " + str(disciplineCat) + "%")
        l4.configure(text="trust - " + str(trustCat) + "%")
        l5.configure(text=f"You played with {name}")
        click_flag = True
        click_block(click_flag)

def discipline():
    """Changes the discipline value and updates info"""
    global healthCat
    global leisureCat
    global disciplineCat
    global trustCat
    global click_flag

    if healthCat <= 10:
        pass
    else:
        if disciplineCat + 10 >= 150:
            disciplineCat = 150
        else:
            disciplineCat += 10
        healthCat -= 5
        leisureCat -= 3
        trustCat -= 0
        l1.configure(text="health - " + str(healthCat) + "%")
        l2.configure(text="leisure - " + str(leisureCat) + "%")
        l3.configure(text="discipline - " + str(disciplineCat) + "%")
        l4.configure(text="trust - " + str(trustCat) + "%")
        l5.configure(text=f"You trained {name}")
        click_flag = True
        click_block(click_flag)

def trust():
    """Changes the trust value and updates info"""
    global healthCat
    global leisureCat
    global disciplineCat
    global trustCat
    global click_flag

    if healthCat <= 10:
        pass
    else:
        if trustCat + 10 >= 150:
            trustCat = 150
        else:
            trustCat += 10
        healthCat -= 3
        leisureCat += 1
        disciplineCat -= 2
        l1.configure(text="health - " + str(healthCat) + "%")
        l2.configure(text="leisure - " + str(leisureCat) + "%")
        l3.configure(text="discipline - " + str(disciplineCat) + "%")
        l4.configure(text="trust - " + str(trustCat) + "%")
        l5.configure(text=f"You caressed {name}")
        click_flag = True
        click_block(click_flag)

def click_block(flag):
    """Disables buttons for 1 second to prevent spam"""
    if flag:
        b1.configure(state="disabled")
        b2.configure(state="disabled")
        b3.configure(state="disabled")
        b4.configure(state="disabled")
        win.after(1000, click_allow)

def click_allow():
    """Enables buttons after blocking"""
    global click_flag
    b1.configure(state="normal")
    b2.configure(state="normal")
    b3.configure(state="normal")
    b4.configure(state="normal")
    click_flag = False

def get_name():
    """Get the name from Entry element, then delete previous elements and display the main game"""
    global name 
    global start_time
    if entry_field.get() == "":
        name = "Cat"
    else:
        name = entry_field.get()
    start_time = time.time()
    entry_field.destroy()
    button_for_name.destroy()
    label_for_name.destroy()
    label_title.configure(text=f"This is your {name}",font="Arial")
    l5.configure(text=f"your {name} is alive")
    label_title.place(x=135, y=5)
    label_info.place(x=-10, y=10)
    b1.place(x=25, y=80)
    b2.place(x=25, y=120)
    b3.place(x=25, y=160)
    b4.place(x=25, y=200)
    b5.place(x=240, y=320)
    l1.place(x=25, y=250)
    l2.place(x=25, y=280)
    l3.place(x=25, y=310)
    l4.place(x=25, y=340)
    l5.place(x=225, y=270)
    logo1.place(x=225, y=70)
    label_delimiter.place(x=0,y=380)
    label_event_info.place(x=0, y=410)
    update_gui()
    update_event()

def entry_restriction(*args):
    """Create restriction to the amount of characters (for Entry widget)"""
    string = var.get()
    if len(string) > max_len:
        var.set(string[:max_len])

var.trace_variable("w", entry_restriction)

# Initialize main elements of the game

label_title = Label(bg="lightblue",width=27, height=3, text=f"This is your {name}",font=("Arial", 12))
label_info = Label(bg="lightblue",justify="center",width=20,height=3,text=None,font=("Arial", 12))
b1 = Button(width=15,text="feed",command=health)
b2 = Button(width=15,text="play",command=leisure)
b3 = Button(width=15,text="train",command=discipline)
b4 = Button(width=15,text="caress",command=trust)
b5 = Button(width=15,text="Exit",command=quit)
l1 = Label(bg="lightblue",anchor="w",width=20,height=2,text="health - " + str(healthCat) + "%")
l2 = Label(bg="lightblue",anchor="w",width=20,height=2,text="leisure - " + str(leisureCat) + "%")
l3 = Label(bg="lightblue",anchor="w",width=20,height=2,text="discipline - " + str(disciplineCat) + "%")
l4 = Label(bg="lightblue",anchor="w",width=20,height=2,text="trust - " + str(trustCat) + "%")
l5 = Label(bg="lightblue",width=20,height=2,text=f"your {name} is alive")
label_delimiter = Label(bg="lightblue",anchor="w",width=50,height=1,text="==================================================", font=12)
label_event_info = Label(bg="lightblue",justify="center",anchor="n",width=40,height=5,text=None,font=("Arial", 14))

# Initialize hidden elements of the main game

hidden_elements = [label_title, label_info,
                   b1, b2, b3, b4, b5, l1,
                   l2, l3, l4, l5, logo1,
                   label_delimiter]

for element in hidden_elements:
    element = element.grid_forget()

# Initialize initial elements of the game (will be destroyed after button click)

entry_field = Entry(justify="center", font=("Tahoma", 12), textvariable=var)
button_for_name = Button(bg="orange",text="Name", command=get_name)
label_for_name = Label(bg="lightblue",text="Name your Cat")
label_for_name.place(x=80, y=25, width=100, height=30)
entry_field.place(x=80, y=70, width=100, height=30)
button_for_name.place(x=250, y=40, width=100, height=60)

win.mainloop()
