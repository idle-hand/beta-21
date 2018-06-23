from tkinter import *
from tkinter.ttk import *
import random
import copy

import csv   


root = Tk()

Main_win = Frame(root).grid()



with open('new_cards.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    card_names = []
#    card_values = [] # will need to update csv file new.csv
    for row in readCSV:
        card_name = row[0]
#       card_value = row[1]

        card_names.append(card_name)
#        card_values.append(card_value)






Label(Main_win,text="Welcome to Bagot St. BlackJack", font=32).grid(row=3,column=3)

for card in card_names:
    print(card)





def hit():
    quit()
    

count=0

    
for i in range(5):
    photo=PhotoImage(file=card_names[count])
      
    show = Button(Main_win,image = photo,)
    show.image = photo
    show.grid(row=1,column=count)
    count=count+1

HitButt=Button(Main_win, text="Hit", command=hit).grid(column=2, row=3, sticky=W)
QuitBut=Button(Main_win, text="Quit", command=root.destroy).grid(column=3, row=3, sticky=W)

root.bind('<Return>', hit)

root.mainloop()

