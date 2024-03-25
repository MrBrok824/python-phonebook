#!/usr/bin/env python3


from tkinter import *
import sqlite3

conn = sqlite3.connect('phonebook.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS PHONEBOOK
             (PHONE TEXT PRIMARY KEY, NAME TEXT)''')  
conn.commit()

tk = Tk()
tk.title("Phonebook Application")
tk.configure(bg='sky blue')
tk.geometry("334x260")

def main():
    
    label = Label(tk, text="Select an option:", bg='sky blue', fg='black')
    label.pack(pady=5)

    add_entry_button = Button(tk, text="Add Entry", command=lambda: addEntry(), bg="green", fg="white")
    add_entry_button.pack(pady=5)

    list_entries_button = Button(tk, text="List Entries", command=lambda: listEntries(), bg="orange", fg="white")
    list_entries_button.pack(pady=5)

    edit_entry_button = Button(tk, text="Edit Entry", command=lambda: editEntry(), bg="purple", fg="white")
    edit_entry_button.pack(pady=5)

    close_button = Button(tk, text="Quit", command=quit_app, bg="red", fg="white")
    close_button.pack(pady=5)

    tk.mainloop()

def quit_app():
    tk.destroy()
    conn.close()
    exit()

def addEntry():
    top = Toplevel(tk)
    top.title("Add New Entry")
    top.configure(bg='sky blue')

    label = Label(top, text="Name", bg='sky blue', fg='black')
    label.pack()
    name = Entry(top)
    name.pack()

    label2 = Label(top, text="Phone Number", bg='sky blue', fg='black')
    label2.pack()
    phone = Entry(top)
    phone.pack()

    b = Button(top, text="Add Entry", command=lambda: addEntryProcess(name.get(), phone.get()))
    b.pack()

def addEntryProcess(name, phone):
    try:
        c.execute("INSERT INTO PHONEBOOK (PHONE, NAME) VALUES(?, ?)", (phone, name))
        conn.commit()
        print(f"\n(Name: {name}, Number: {phone}) has been added to the phonebook!\n")
    except:
        print("Error occurred while adding entry.")

def listEntries():
    c.execute('SELECT * FROM Phonebook')
    allData = c.fetchall()
    if allData:
        print("All entries:")
        for entry in allData:
            phone, name = entry
            print(f"Name: {name}, Number: {phone}")
    else:
        print("Phonebook is empty.")

def editEntry():
    top = Toplevel(tk)
    top.title("Edit Entry")
    top.configure(bg='sky blue')

    label = Label(top, text="Enter a name to edit: ", bg='sky blue', fg='black')
    label.pack()
    name = Entry(top)
    name.pack()
    b = Button(top, text="Look up", command=lambda: lookupForEdit(name.get()))
    b.pack()

def lookupForEdit(name):
    c.execute('SELECT * FROM Phonebook WHERE name = ?', (name,))
    lookUp = c.fetchone()
    if lookUp:
        phone, name = lookUp
        top = Toplevel(tk)
        top.title("Edit Entry")
        top.configure(bg='sky blue')
        label = Label(top, text=f"Current Name: {name}, Number: {phone}", bg='sky blue', fg='black')
        label.pack()
        new_name = Entry(top)
        new_name.pack()
        b = Button(top, text="Update Name", command=lambda: updateEntry(phone, new_name.get(), top))
        b.pack()
        b = Button(top, text="Update Number", command=lambda: updateNumber(name, new_name.get(), top))
        b.pack()
    else:
        print(f"No entry found with the name '{name}'.")

def updateEntry(phone, new_name, window):
    c.execute("UPDATE PHONEBOOK SET NAME = ? WHERE PHONE = ?", (new_name, phone))
    conn.commit()
    window.destroy()
    print(f"Name updated to: Name: {new_name}, Number: {phone}")

def updateNumber(name, new_number, window):
    c.execute("UPDATE PHONEBOOK SET PHONE = ? WHERE NAME = ?", (new_number, name))
    conn.commit()
    window.destroy()
    print(f"Number updated to: Name: {name}, Number: {new_number}")

if __name__ == "__main__":
    main()


