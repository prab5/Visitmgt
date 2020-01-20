from tkinter import *

#This is function to be used later
#def function1():


window=Tk()

F1=Frame(window)
F1.pack(side=TOP,padx=20,pady=20,fill=BOTH,expand=YES)

L1=Label(F1,text='WELCOME ADMININSTRATOR :',bg='light green',font=("Courier", 25))

L1.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=TOP)


##

F2=Frame(window)
F2.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES)

L2=Label(F2,text='NAME :',bg='light blue')
L2.pack(fill=BOTH,expand=YES,padx=5,side=LEFT)


E2=Entry(F2)
E2.pack(side=RIGHT,fill=BOTH,expand=YES,padx=5,pady=5)




F3=Frame(window)
F3.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES)

L3=Label(F3,text='PASSWORD :',bg='light blue')
L3.pack(fill=BOTH,expand=YES,padx=5,side=LEFT)


E3=Entry(F3)
E3.pack(side=RIGHT,fill=BOTH,expand=YES,padx=5,pady=5)


##
F4=Frame(window)
F4.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES)
#B4=Button(F4,text='Login/LogOut',bg='gold',command=function1())
#B4.pack(side=RIGHT,fill=BOTH,expand=YES,padx=5,pady=5)

B4=Button(F4,text='Login/LogOut',bg='gold')
B4.pack(side=RIGHT,fill=BOTH,expand=YES,padx=5,pady=5)

window.mainloop()          
