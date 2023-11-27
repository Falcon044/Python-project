from tkinter import *
from tkinter import messagebox as mb
import time
import random
import pandas as pd

events = pd.read_csv(r"D:\Python\tkinter_cat\Python-project\Events.csv")

win = Tk()
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
game = True

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
    win.after(5000, update_event)

def check_stats():
    """Checks the stats of the pet, control buttons for actions and quit the game if answer is False"""
    global healthCat
    global leisureCat
    global disciplineCat
    global trustCat
    global game
    end_time = time.time()

    if healthCat <= 0 or leisureCat <= 0 or disciplineCat <= 0 or trustCat <= 0:
        answer = mb.askyesno(title="You lost", message="Do you want to play again?")
        if answer == True:
            healthCat = 20
            leisureCat = 20
            disciplineCat = 20
            trustCat = 20
        else:
            result_time = end_time - start_time
            result_time = time.strftime("%H:%M:%S", time.gmtime(result_time))
            mb.showinfo(message=f"Goodbye!, you spent {result_time} time with your pet")
            game = False
            win.quit()
    
    elif healthCat >= 100 and leisureCat >= 100 and disciplineCat >= 100 and trustCat >= 100:
        answer = mb.askyesno(title="you win", message="Do you want to play again?")
        if answer == True:
            healthCat = 20
            leisureCat = 20
            disciplineCat = 20
            trustCat = 20
        else:
            result_time = end_time - start_time
            result_time = time.strftime("%H:%M:%S", time.gmtime(result_time))
            mb.showinfo(message=f"Goodbye!, you spent {result_time} time with your pet")
            game = False
            win.quit()
    
    if healthCat <= 10:
        label_info.configure(text=f"Attention!\n{name}\nis hungry")
    else:
        label_info.configure(text=f"{name}\nis sated")

    # if healthCat >= 140:
    #     b1.configure(state="disabled")
    # elif leisureCat >= 140:
    #     b2.configure(state="disabled")
    # elif disciplineCat >= 140:
    #     b3.configure(state="disabled")
    # elif trustCat >= 140:
    #     b3.configure(state="disabled")
    # else:
    #     b1.configure(state="normal")
    #     b2.configure(state="normal")
    #     b3.configure(state="normal")
    #     b4.configure(state="normal")

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

def entry_restriction(*args):
    """Create restriction to the amount of characters (for Entry widget)"""
    string = var.get()
    if len(string) > max_len:
        var.set(string[:max_len])

var.trace_variable("w", entry_restriction)

label_title = Label(width=27, height=3, text=f"This is your {name}",font="Arial")
label_info = Label(width=20,height=3,text=None)
b1 = Button(width=15,text="feed",command=health)
b2 = Button(width=15,text="play",command=leisure)
b3 = Button(width=15,text="train",command=discipline)
b4 = Button(width=15,text="caress",command=trust)
b5 = Button(width=15,text="Exit",command=quit)
l1 = Label(width=20,height=2,text="health - " + str(healthCat) + "%")
l2 = Label(width=20,height=2,text="leisure - " + str(leisureCat) + "%")
l3 = Label(width=20,height=2,text="discipline - " + str(disciplineCat) + "%")
l4 = Label(width=20,height=2,text="trust - " + str(trustCat) + "%")
l5 = Label(width=20,height=2,text=f"your {name} is alive")
label_event_info = Label(width=30,height=15,text=None,)

def get_name():
    """Get the name from Entry element, then delete previous elements and display the main game"""
    global name 
    global game
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
    label_title.grid(row=0, column=2, columnspan=3, rowspan=2)
    label_info.grid(row=0,column=0)
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
    label_event_info.grid(row=10,column=3)
    update_gui()
    update_event()


# Initialize hidden elemnts of the main game

hidden_elements = [label_title, label_info,
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
