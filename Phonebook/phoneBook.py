import os
from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("500x500")
window.title("PhoneBook")
def add_contact():
    entry_name = entry_co_name.get()
    phone_entry = entry_co_number.get()
    list_box.insert(END,entry_name, phone_entry)
    print("Name :"+entry_name+"\n"+"Phone_number: "+phone_entry)
    
def delete_all_context():
    list_box.delete(0,END)
    if os.path.exists("saveList.txt"):
        os.remove("saveList.txt")
        
    
def exit():
    check_exit = messagebox.askyesno("Exit","Are you sure want to quit the App") 
    if check_exit == True:
        window.quit()
        
def save_file():
    list_save = list(list_box.get(0,END))
    f = open("saveList.txt","w")
    f.write(str(list_save))
    f.close()  

def show_file():
    f = open("saveList.txt","r")
    readable = f.read()
    print(readable)
    
def delete_list_box():
    list_box.delete(0,END)
             
label_co_name = Label(window,text="Contact name")
label_co_name.place(x=0,y=0)

entry_co_name = Entry(window)
entry_co_name.place(x=90,y=0)

label_co_number = Label(window,text="Phone number")
label_co_number.place(x=0,y=20)

entry_co_number = Entry(window)
entry_co_number.place(x=90,y=20)

btn_add = Button(window,text="Add Contact",width=30,command=add_contact)
btn_add.place(x=30,y=50)

btn_save = Button(window,text="SaveList",width=30,command=save_file)
btn_save.place(x=30,y=85)

btn_copy_phone_num = Button(window,text="Delete List box",width=15,command=delete_list_box)
btn_copy_phone_num.place(x=3,y=140)

btn_open_saved_file = Button(window,text=" Open Saved file", width=12,command=show_file)
btn_open_saved_file.place(x=120,y=140)

btn_delete_context= Button(window,text=" Delete All Context", width=15,command=delete_all_context)
btn_delete_context.place(x=3,y=165)

btn_exit= Button(window,text=" Exit App", width=12,command=exit)
btn_exit.place(x=120,y=165)

list_box = Listbox(window)
scroll_bar = Scrollbar(window,orient=VERTICAL)
scroll_bar.place(x=395)
scroll_bar.config(command=list_box.yview)
list_box.config(yscrollcommand=scroll_bar.set)
list_box.place(x=270,y=0)
window.mainloop()
