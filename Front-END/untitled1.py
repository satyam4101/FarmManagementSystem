import tkinter as tk
def show_entry_fields():
    print("Name: %s\nCourse: %s\n" % (e1.get(), e2.get()))
master = tk.Tk()
master.title("Registration Form")
tk.Label(master, text="Farmers ",bg="cyan").grid(row=0,column=1) 
master.configure(background="cyan") 

tk.Label(master,text="FARMER_ID",bg="cyan").grid(row=1) 
tk.Label(master,text="FARMER_NAME",bg="cyan").grid(row=2) 
tk.Label(master,text="FARMER_SHIFT",bg="cyan").grid(row=3) 
tk.Label(master,text="FARMER_NUMBER.",bg="cyan").grid(row=4) 
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)
e7 = tk.Entry(master) 
e1.grid(row=1, column=1) 
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)

tk.Button(master,text='Submit',bg="red", command=show_entry_fields).grid(row=8,column=1,
sticky=tk.W, pady=4)
master.mainloop()