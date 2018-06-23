from tkinter import *

card_nam =['king_of_spades.png','jack_of_clubs.png','7_of_hearts.png','9_of_clubs.png',
         '8_of_diamonds.png','4_of_clubs.png']


root = Tk()
frame = Frame(root)
frame.grid()
bottomframe = Frame(root)
bottomframe.grid()

x = 0

persist_list = []


for card in card_nam:
    
    print(card)
    
    
    photo=PhotoImage(file=card)
  
    show = Button(frame,image = photo,)
    show.image = photo
    show.grid()
    x = x + 1
   
  
##photo1=PhotoImage(file=photox[1])
##greenbutton = Button(frame, image = photo1,)
##greenbutton.grid(row=0,column=1)
##
##photo2=PhotoImage(file=photox[2])
##bluebutton = Button(frame, image = photo2,)
##bluebutton.grid(row=0,column=2)
##
##photo3=PhotoImage(file=photox[3])
##blackbutton = Button(frame, image = photo3,)
##blackbutton.grid(row=1,column=0)
##
##photo4=PhotoImage(file=photox[4])
##orangebutton = Button(frame, image = photo4)
##orangebutton.grid(row=1,column=1)
##
##photo5=PhotoImage(file=photox[5])
##plyersbutton = Button(frame, image = photo5)
##plyersbutton.grid(row=1,column=2)
##

root.mainloop()




