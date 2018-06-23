from tkinter import *

photox =['king_of_spades.png','jack_of_clubs.png','7_of_hearts.png','9_of_clubs.png',
         '8_of_diamonds.png','4_of_clubs.png']




root = Tk()
frame = Frame(root)
frame.grid()

x = 0

while x < 6:
    print(photox[x])
    x = x + 1
    

bottomframe = Frame(root)
bottomframe.grid()

photo=PhotoImage(file=photox[0])
redbutton = Button(frame,image = photo,)
redbutton.grid(row=0,column=0)

photo1=PhotoImage(file=photox[1])
greenbutton = Button(frame, image = photo1,)
greenbutton.grid(row=0,column=1)

photo2=PhotoImage(file=photox[2])
bluebutton = Button(frame, image = photo2,)
bluebutton.grid(row=0,column=2)

photo3=PhotoImage(file=photox[3])
blackbutton = Button(frame, image = photo3,)
blackbutton.grid(row=1,column=0)

photo4=PhotoImage(file=photox[4])
orangebutton = Button(frame, image = photo4)
orangebutton.grid(row=1,column=1)

photo5=PhotoImage(file=photox[5])
plyersbutton = Button(frame, image = photo5)
plyersbutton.grid(row=1,column=2)


root.mainloop()




