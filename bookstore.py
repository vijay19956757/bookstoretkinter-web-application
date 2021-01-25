from tkinter import *
import mysql.connector
def view_func():
    conn = mysql.connector.connect(host="localhost", user="root", password="", db="bookstore")
    cursor = conn.cursor()
    s = "SELECT * FROM booksrecord"
    cursor.execute(s)
    r=cursor.fetchall()
    #print(r[0][0])
    #print(len(r))
    for i in range(0,len(r)):
        listbox.insert(i,r[i])


def add():
    print(title1.get())
    print(author.get())
    print(year.get())
    print(isbn.get())

    conn = mysql.connector.connect(host ="localhost",user = "root",password = "",db ="bookstore")
    cursor = conn.cursor()
    s="INSERT INTO booksrecord(title,auther,year,isbn) VALUES (%s, %s ,%s,%s)"
    b1=(title1.get(),author.get(),year.get(),isbn.get())
    cursor.execute(s,b1)
    conn.commit()
    print("thank you")
def delete():
    conn = mysql.connector.connect(host="localhost", user="root", password="", db="bookstore")
    cursor = conn.cursor()
    s="delete from booksrecord"
    cursor.execute(s)
    conn.commit()
    print("record gayab")
def update():
    conn = mysql.connector.connect(host="localhost", user="root", password="", db="bookstore")
    cursor = conn.cursor()
    s=("UPDATE booksrecord SET title='test',auther='sudhanshu' where id=9")
    cursor.execute(s)
    conn.commit()
    print("aa gya naya record")

win=Tk()
win.title("Book Store System")

lable1= Label(win,text="Title")

lable2= Label(win,text="Auther")

lable3=Label(win,text="Year")

lable4=Label(win,text="ISBN")

title_text = StringVar()
title1 = Entry(win, textvariable= title_text)

author_text = StringVar()
author = Entry(win, textvariable= author_text)

year_text = StringVar()
year = Entry(win, textvariable= year_text)

isbn_text = StringVar()
isbn = Entry(win, textvariable= isbn_text)

listbox = Listbox(win, height=6, width=35)
listbox.grid(row=2, column =0, rowspan=6, columnspan=2)

sb1 =Scrollbar(win)
sb1.grid(row=2, column=2 ,rowspan = 6)

listbox.configure(yscrollcommand=sb1.set)
sb1.configure(command=listbox.yview)

b1 =Button(win, text= "View All", width=12,command=view_func)
b1.grid(row=2, column=3)

b2 =Button(win, text= "Search Book", width=12)
b2.grid(row=3, column=3)

b3 =Button(win, text= "Add Book", width=12, command=add)
b3.grid(row=4, column=3)

b4 =Button(win, text= "Update", width=12,command=update)
b4.grid(row=5, column=3)

b5 =Button(win, text= "Delete", width=12,command=delete)
b5.grid(row=6, column=3)

b6 =Button(win, text= "Close", width=12,command=win.destroy)
b6.grid(row=7, column=3)


lable1.grid(row=0,column=0)
lable2.grid(row=0,column=2)
lable3.grid(row=1,column=0)
lable4.grid(row=1,column=2)
title1.grid(row=0, column=1)
author.grid(row=0, column=3)
year.grid(row=1, column=1)
isbn.grid(row=1, column=3)



win.mainloop()