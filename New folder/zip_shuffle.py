# black-jack - 21 - tkinter - d.howe - kingston - Canada - June - 2018
#
from tkinter import *
from tkinter.ttk import *
import random
import copy
import csv   

global count
global col_count

count = 0
col_count = 0
card_count = 0
house_col = 0



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



deck = list(zip(card_names, card_values))

random.shuffle(deck)

for name, value in deck:
    print (name, value)




def hit():
    global count
    global col_count

    photo=PhotoImage(file=card_names[count])
    show = Button(Main_win,image = photo,)
    show.image = photo
    show.grid(row=0,column=col_count)
    col_count = col_count + 1
    count = count + 1
   
def stay():
    global count
    global house_col
    #    quit()
    photo=PhotoImage(file=card_names[count])
    show = Button(Main_win,image = photo)
    show.image = photo
    show.grid(row=1,column=house_col)
    count=count+1
    house_col = house_col + 1



photo=PhotoImage(file=card_names[count])
show = Button(Main_win,image = photo,)
show.image = photo
show.grid(row=0,column=0)
count=count+1
col_count = col_count + 1

photo=PhotoImage(file=card_names[count])
show = Button(Main_win,image = photo,)
show.image = photo
show.grid(row=0,column=1)
count=count+1
col_count = col_count + 1


photo=PhotoImage(file='./back.png')
show = Button(Main_win,image = photo)
show.image = photo
show.grid(row=1,column=0)





HitButt=Button(Main_win, text="Hit", command=hit).grid(column=0, row=3)
Stand=Button(Main_win, text="Stay", command=stay).grid(column=1, row=3)
QuitBut=Button(Main_win, text="Quit", command=root.destroy).grid(column=2, row=3)
Label(Main_win,text="Bagot St. BlackJack", font=32).grid(row=4,column=1)


root.bind('<Return>', hit)
root.mainloop()
