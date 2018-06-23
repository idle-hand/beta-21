from tkinter import *
from tkinter import ttk

def hit():
    quit()

    
    
root = Tk()
root.title("Bagot St. BlackJack")

card_nam =['king_of_spades.png','jack_of_clubs.png','7_of_hearts.png','9_of_clubs.png',
         '8_of_diamonds.png','back.png']
##card_nam =['king_of_spades.png','back.png','back.png','back.png','back.png','back.png']





mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

count=0

for card in card_nam:
        
        print(card)
        
        
        photo=PhotoImage(file=card)
      
        show = ttk.Button(mainframe,image = photo,)
        show.image = photo
        show.grid(row=1,column=count)
        count=count+1
        




ttk.Button(mainframe, text="Hit", command=hit).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="Quit", command=root.destroy).grid(column=3, row=3, sticky=W)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)



root.bind('<Return>', hit)

root.mainloop()
