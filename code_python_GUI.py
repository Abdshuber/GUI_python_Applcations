' this app  to add any choses of checkbox to the list '
from tkinter import *
from tkinter import messagebox

frame_main=Tk()
frame_main.geometry('500x600')
frame_main.title('sample GUI ')

img1=PhotoImage(file='facebook.png') 
var_rad1=IntVar()
radio1=Radiobutton(frame_main,image=img1,variable=var_rad1,value=1 ,fg='blue',width=40,height=40)
radio1.place(x=10,y=100)

img2=PhotoImage(file='insta.png') 
# var_rad2=IntVar()
radio2=Radiobutton(frame_main,image=img2,variable=var_rad1,value=2,fg='red',width=40,height=40)
radio2.place(x=10,y=150)

Label(frame_main,text=' Chose Your favorit languge to put them in  the list down  <: ').place(x=140,y=90)
v_chk1=IntVar()
chk1=Checkbutton(frame_main,text='python',variable=v_chk1,onvalue=1,offvalue=0)
chk1.place(x=140,y=120)

v_chk2=IntVar()
chk2=Checkbutton(frame_main,text='Java',variable=v_chk2,onvalue=2,offvalue=0)
chk2.place(x=140,y=140)

v_chk3=IntVar()
chk3=Checkbutton(frame_main,text='Roby',variable=v_chk3,onvalue=3,offvalue=0)
chk3.place(x=140,y=160)

v_chk4=IntVar()
chk4=Checkbutton(frame_main,text='Javascript',variable=v_chk4,onvalue=4,offvalue=0)
chk4.place(x=140,y=180)

listbox=Listbox(frame_main,bg='silver',fg='black',width=30,height=20,selectmode=MULTIPLE)
listbox.place(x=200,y=240)

var_label1=StringVar()
label1=Label(frame_main,textvariable=var_label1,bg='silver',fg='black',width=50,height=1)
label1.place(x=30,y=220)

def save_fun():
    listbox.delete(0,10)            
 
    var1=v_chk1.get()    
    var2=v_chk2.get()    
    var3=v_chk3.get()    
    var4=v_chk4.get()
    if var_rad1.get()==1:
       var_label1.set(  'Hellow From FaceBook')
    elif var_rad1.get()==2:
       var_label1.set(  'Hellow From  Instagram')
    else: var_label1.set( 'NoThinks')
    
    if var1==1:
        listbox.insert(0,'Python')
    if var2==2:
        listbox.insert(0,'Java')
    if var3==3:
        listbox.insert(0,'Roby')
    if var4==4:
        listbox.insert(0,'Javascript')
        
b=Button(frame_main,bg='Silver',text='Save Data',command=save_fun)
b.place(x=30,y=300)

frame_main.mainloop()
