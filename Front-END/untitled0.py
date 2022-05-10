import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import IntVar
def form():
    conn=sqlite3.connect('44.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS hello(
                                    first text(255) NOT NULL,last text(255) NOT NULL,email text(255) NOT NULL)''')
    conn.execute("insert into hello (first,last,email,mobile)values('"+t1.get()+"','"+t2.get()+"','"+t6.get()+"')")
    conn.commit()
    conn.close()

root=tk.Tk()
root.title("FORM")
root.geometry("870x780")
root.configure(background="#96f7c5")

first = IntVar(root,value=' ')
l1=tk.Label(root,bg="#96f7c5",text="First Name :")
l1.grid(row=0,sticky="w")
t1=tk.Entry(root)
t1.grid(row=0,ipadx=30,column=1,pady=10)

last = IntVar(root,value=' ')
l2=tk.Label(root,bg="#96f7c5",text="Last Name :")
l2.grid(row=1,sticky="w")
t2=tk.Entry(root)
t2.grid(row=1,ipadx=30,column=1,pady=10)

l3=tk.Label(root,bg="#96f7c5",text="Date of Birth :")
l3.grid(row=3,sticky="w")

t3=ttk.Combobox(root, width = 5,text="Day")
t3.set("Day")
t3['values'] = ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
t3.grid(row=3,column=2,sticky='nsew',padx=2,pady=10)

t4=ttk.Combobox(root, width = 10,text="Month")
t4['values'] = (' January',  ' February', ' March', ' April', ' May', ' June', ' July', ' August', ' September', ' October', ' November', ' December')
t4.grid(row=3,column=1,sticky='nsew',padx=2,pady=10)
t4.set("Month")

t5=ttk.Combobox(root, width = 10,text="Year")
t5['values'] = (1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018)
t5.set("Year")
t5.grid(row=3,column=3,sticky='nsew',padx=2,pady=10)

email = IntVar(root,value=' ')
l6=tk.Label(root,bg="#96f7c5",text="Email ID :")
l6.grid(row=4,sticky="w")
t6=tk.Entry(root)
t6.grid(row=4,column=1,ipadx=30,pady=10)

l7=tk.Label(root,bg="#96f7c5",text="Mobile Number :")
l7.grid(row=5,sticky="w")
t7=ttk.Entry(root)
t7.grid(row=5,column=1,ipadx=30,pady=10)

l8=tk.Label(root,bg="#96f7c5",text="Gender :")
l8.grid(row=6,sticky="w")
rb1=tk.Radiobutton(root,text='Male',width=5,anchor=tk.W,value=1,bg="#96f7c5", command=form)
rb1.grid(row=6,column=1,sticky="nsew")
rb1=tk.Radiobutton(root,text='Female',width=5,anchor=tk.W,value=2,bg="#96f7c5", command=form)
rb1.grid(row=6,column=2,sticky="nsew")

l9=tk.Label(root,text='Address :',bg='#96f7c5',width=20,anchor=tk.W)
l9.grid(row=7,column=0)
t9=tk.Text(root,height=5, width=30)
t9.grid(row=7,column=1,columnspan=2,sticky='w',pady=10)

l10=tk.Label(root,bg="#96f7c5",text="City :")
l10.grid(row=8,sticky="w")
t10=ttk.Entry(root)
t10.grid(row=8,column=1,ipadx=30,pady=10)

l11=tk.Label(root,bg="#96f7c5",text="Pin Code :")
l11.grid(row=9,sticky="w")
t11=ttk.Entry(root)
t11.grid(row=9,column=1,ipadx=30,pady=10)

l12=tk.Label(root,bg="#96f7c5",text="State :")
l12.grid(row=10,sticky="w")
t12=ttk.Entry(root)
t12.grid(row=10,column=1,ipadx=30,pady=10)

l13=tk.Label(root,bg="#96f7c5",text="Country :")
l13.grid(row=11,sticky="w")
t13=ttk.Entry(root)
t13.grid(row=11,column=1,ipadx=30,pady=10)

l14=tk.Label(root,text="Hobbies :",bg='#96f7c5',width=20,anchor=tk.W)
l14.grid(row=12,column=0)
cb1=tk.Checkbutton(root,text="Drawing",bg='#96f7c5')
cb1.grid(row=12,column=1,sticky=tk.W,pady=1)
cb2=tk.Checkbutton(root,text="Singing",padx=8,bg='#96f7c5')
cb2.grid(row=12,column=1,sticky=tk.E,pady=1)
cb3=tk.Checkbutton(root,text="Dancing",padx=5,bg='#96f7c5')
cb3.grid(row=12,column=2,sticky=tk.W,pady=1)
cb4=tk.Checkbutton(root,text="Sketching",padx=5,bg='#96f7c5')
cb4.grid(row=12,column=2,sticky=tk.E,pady=1)
cb5=tk.Checkbutton(root,text="Other",bg='#96f7c5')
cb5.grid(row=13,column=1,sticky=tk.W,pady=10)
t14=tk.Entry(root,width=15)
t14.grid(row=13,column=1,columnspan=2,pady=10) 

l15=tk.Label(root,text="Qualification :",bg='#96f7c5',anchor=tk.W)
l15.grid(row=14,column=0,sticky="w")
l16=tk.Label(root,text="S.No.Examination",bg='#96f7c5',anchor=tk.W)
l16.grid(row=14,column=1,sticky="w")
l17=tk.Label(root,text="Board",bg='#96f7c5',anchor=tk.W)
l17.grid(row=14,column=2) 
l18=tk.Label(root,text="Percentage",bg='#96f7c5',anchor=tk.W)
l18.grid(row=14,column=3)         
l19=tk.Label(root,text="Year of Passing",bg='#96f7c5',anchor=tk.W)
l19.grid(row=14,column=4) 

l20=tk.Label(root,text="1     Class X",bg='#96f7c5',anchor=tk.W)
l20.grid(row=15,column=1,sticky="w")
l19=tk.Label(root,text="2     Class XII",bg='#96f7c5',anchor=tk.W)
l19.grid(row=16,column=1,sticky="w")  
l20=tk.Label(root,text="3     Graduation",bg='#96f7c5',anchor=tk.W)
l20.grid(row=17,column=1,sticky="w")
l21=tk.Label(root,text="4     Masters",bg='#96f7c5',anchor=tk.W)
l21.grid(row=18,column=1,sticky="w")    
t15=tk.Entry(root,width=25)
t15.grid(row=15,column=2,padx=2,pady=6)
t16=tk.Entry(root,width=25)
t16.grid(row=15,column=3,pady=6)
t17=tk.Entry(root,width=25)
t17.grid(row=15,column=4,pady=6)

t18=tk.Entry(root,width=25)
t18.grid(row=16,column=2,padx=2,pady=6)
t19=tk.Entry(root,width=25)
t19.grid(row=16,column=3,pady=6)
t20=tk.Entry(root,width=25)
t20.grid(row=16,column=4,pady=6)

t21=tk.Entry(root,width=25)
t21.grid(row=17,column=2,padx=2,pady=6)
t22=tk.Entry(root,width=25)
t22.grid(row=17,column=3,pady=6)
t23=tk.Entry(root,width=25)
t23.grid(row=17,column=4,pady=6)

t24=tk.Entry(root,width=25)
t24.grid(row=18,column=2,padx=2,pady=6)
t25=tk.Entry(root,width=25)
t25.grid(row=18,column=3,padx=2,pady=6)
t26=tk.Entry(root,width=25)
t26.grid(row=18,column=4,padx=2,pady=6)

l22=tk.Label(root,text="Courses Applied For :",bg='#96f7c5',anchor=tk.W)
l22.grid(row=19,column=0,sticky="w")
cb1=tk.Radiobutton(root,text="BCA",bg='#96f7c5',anchor=tk.W)
cb1.grid(row=19,column=1,sticky=tk.W,pady=6)
cb2=tk.Radiobutton(root,text="B.Com",bg='#96f7c5',anchor=tk.E)
cb2.grid(row=19,column=1,pady=6)
cb3=tk.Radiobutton(root,text="B.Sc",bg='#96f7c5',anchor=tk.W)
cb3.grid(row=19,column=2,sticky=tk.W,pady=6)
cb4=tk.Radiobutton(root,text="B.A",bg='#96f7c5',anchor=tk.E)
cb4.grid(row=19,column=2,pady=6)
      
button=tk.Button(root,text='Submit',bg='white',command=form)
button.grid(row=20,column=2)
button=tk.Button(root,text='Reset',bg='white',command=root.destroy,anchor=tk.W)
button.grid(row=20,column=3,sticky='w')
root.mainloop()