"""
The database can store book information
Title, Year ,Author , ISBN 

User can :
Add a book,
View all books in the database
Search for a book,
Update a book info,
Delete a book,
Close 
"""


import tkinter as tk
import storage
from tkinter import * 
from tkinter import ttk 


def lookup():
    lst.delete(0,END)
    for row in storage.view_data("MyBooks.db"):
        lst.insert(END,row)

def searchup():
    lst.delete(0,END)
    for row in storage.search_data("MyBooks.db",title_input.get(), author_input.get(),year_input.get(),ISBN_input.get()):
        lst.insert(END,row)

def add_Data():
    lst.delete(0,END)
    for row in storage.insert_data(title_input.get(), author_input.get(),year_input.get(),ISBN_input.get(),"MyBooks.db"):
        lst.insert(END,row)

def choose_item(event): #retuns type of data
    global tuplee
    tuplee = lst.get(lst.curselection()[0])
    #return tuplee
    Title_bar.delete(0,END)
    Title_bar.insert(END,tuplee[1])
    
    year_bar.delete(0,END)
    year_bar.insert(END,tuplee[3])
    
    Author_bar.delete(0,END)
    Author_bar.insert(END,tuplee[2])
    
    ISBN_bar.delete(0,END)
    ISBN_bar.insert(END,tuplee[4])

def remove():
    storage.delete_data("MyBooks.db",tuplee[0])


def update_():
    storage.update_data("MyBooks.db",tuplee[0],title_input.get(), author_input.get(),year_input.get(),ISBN_input.get())

screen = tk.Tk()
screen.title("Book Database")
screen.config(bg='gray')
tk.Label(screen, text="Title").grid(row=0)
tk.Label(screen, text="Year").grid(row=1)
tk.Label(screen, text = "Author").grid(row=0,column=2)
tk.Label(screen,text = "ISBN").grid(row=1,column=2)


title_input = StringVar()
Title_bar = tk.Entry(screen,text=title_input, bg = 'orange')
Title_bar.grid(row=0, column=1)

year_input = StringVar()
year_bar = tk.Entry(screen,text=year_input , bg = 'orange')
year_bar.grid(row=1, column=1)

author_input = StringVar()
Author_bar = tk.Entry(screen,text=author_input, bg = 'orange')
Author_bar.grid(row=0, column=4)

ISBN_input= StringVar()
ISBN_bar = tk.Entry(screen,text=ISBN_input, bg = 'orange')
ISBN_bar.grid(row=1, column=4)


tk.Button(screen, text = 'Add',width = 15,command = add_Data , bg = 'yellow').grid(row = 2, column = 1,sticky='n') 
tk.Button(screen, text = 'Update',width = 15,command = update_, bg = 'yellow').grid(row = 3, column = 1,sticky='n') 
tk.Button(screen, text = 'Delete',width = 15,command = remove, bg = 'yellow').grid(row = 4,column = 1,sticky='n') 
tk.Button(screen, text = 'View',width = 15,command = lookup, bg = 'yellow').grid(row = 5, column = 1,sticky='n') 
tk.Button(screen, text = 'Search',width = 15,command  = searchup, bg = 'yellow').grid(row = 6, column = 1,sticky='n') 
tk.Button(screen, text = 'Close',width = 15,command =screen.destroy, bg = 'yellow').grid(row = 7,column = 1,sticky='n') 



lst = Listbox(screen, width = 35, height = 10, bg = 'white')
lst.grid(row = 2, column = 2, columnspan = 5,rowspan=10)

lst.bind("<<ListboxSelect>>",choose_item)
scrolll = tk.Scrollbar(screen)
scrolll.grid(row = 2, column = 7,columnspan = 1,rowspan=8)

#attach Listbox to scrollbar
lst.configure(yscrollcommand = scrolll.set)
scrolll.configure(command = lst.yview)



screen.mainloop()