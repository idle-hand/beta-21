# black-jack - 21 - tkinter - d.howe - kingston - Canada - June - 2018
#
from tkinter import *
from tkinter.ttk import *
import random
import copy
import csv   

global count
count = 0

root = Tk()
Main_win = Frame(root).grid(row=0,column=0)


with open('newfull.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    card_names = []
    card_values = []
    for row in readCSV:
        card_name = row[0]
        card_value = row[1]
        card_names.append(card_name)
        card_values.append(card_value)
        


random.shuffle(card_names)


def hit():
    global count
    photo=PhotoImage(file=card_names[count])
    show = Button(Main_win,image = photo,)
    show.image = photo
    show.grid(row=0,column=1)
    count = count + 1

def again():
    global count
    photo=PhotoImage(file=card_names[count])
    show = Button(Main_win,image = photo,)
    show.image = photo
    show.grid(row=0,column=2)    
    count = count + 1

def stay():
    pass
    #    quit()




photo=PhotoImage(file=card_names[count])
show = Button(Main_win,image = photo,)
show.image = photo
show.grid(row=0,column=0)
count=count+1

photo=PhotoImage(file='./back.png')
show = Button(Main_win,image = photo)
show.image = photo
show.grid(row=1,column=0)
count=count+1


HitButt=Button(Main_win, text="Hit", command=hit).grid(column=0, row=3)

HitAgain=Button(Main_win, text="Again", command=again).grid(column=1, row=3)

Stand=Button(Main_win, text="Stay", command=stay).grid(column=2, row=3)

QuitBut=Button(Main_win, text="Quit", command=root.destroy).grid(column=4, row=3)

Label(Main_win,text="Bagot St. BlackJack", font=32).grid(row=4,column=2)


root.bind('<Return>', hit)
root.mainloop()

