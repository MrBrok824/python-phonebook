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
tk.geometry("340x330")

def main():
    
    label = Label(tk, text="Select an option:", bg='sky blue', fg='black')
    label.pack(pady=5)

    add_entry_button = Button(tk, text="Add Entry", command=lambda: addEntry(), bg="green", fg="white", width=15, height=2)
    add_entry_button.pack(pady=5)

    list_entries_button = Button(tk, text="List Entries", command=lambda: listEntries(), bg="orange", fg="white", width=15, height=2)
    list_entries_button.pack(pady=5)

    edit_entry_button = Button(tk, text="Edit Entry", command=lambda: editEntry(), bg="purple", fg="white", width=15, height=2)
    edit_entry_button.pack(pady=5)

    delete_entry_button = Button(tk, text="Delete Entry", command=lambda: deleteEntry(), bg="blue", fg="white", width=15, height=2)
    delete_entry_button.pack(pady=5)

    close_button = Button(tk, text="Quit", command=quit_app, bg="red", fg="white", width=15, height=2)
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
        print()
        for entry in allData:
            phone, name = entry
            print()
            print(f"Name: {name}")
            print(f"Phone: {phone}")
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
        label = Label(top, text=f"Current Name: {name}, Phone: {phone}", bg='sky blue', fg='black')
        label.pack()
        new_name = Entry(top)
        new_name.pack()
        b = Button(top, text="Edit Name", command=lambda: updateEntry(phone, new_name.get(), top))
        b.pack()
        b = Button(top, text="Edit Phone", command=lambda: updateNumber(name, new_name.get(), top))
        b.pack()
    else:
        print(f"No entry found with the name '{name}'.")

def updateEntry(phone, new_name, window):
    try:
        c.execute("UPDATE Phonebook SET name = ? WHERE phone = ?", (new_name, phone))
        conn.commit()
        window.destroy()
        print(f"Name updated to '{new_name}' for phone number '{phone}'.")
    except:
        print("Error occurred while updating entry.")

def updateNumber(name, new_number, window):
    c.execute('SELECT * FROM Phonebook WHERE name = ?', (name,))
    lookUp = c.fetchone()
    if lookUp:
        phone, name = lookUp
        try:
            c.execute("UPDATE Phonebook SET phone = ? WHERE name = ?", (new_number, name))
            conn.commit()
            window.destroy()
            print(f"Phone number updated to '{new_number}' for name '{name}'.")
        except:
            print("Error occurred while updating phone number.")
    else:
        print(f"No entry found with the name '{name}'.")

def deleteEntry():
    top = Toplevel(tk)
    top.title("Delete Entry")
    top.configure(bg='sky blue')

    label = Label(top, text="Enter a name to delete: ", bg='sky blue', fg='black')
    label.pack()
    name = Entry(top)
    name.pack()
    b = Button(top, text="Delete", command=lambda: deleteEntryProcess(name.get(), top))
    b.pack()

def deleteEntryProcess(name, window):
    c.execute('SELECT * FROM Phonebook WHERE name = ?', (name,))
    lookUp = c.fetchone()
    if lookUp:
        phone, name = lookUp
        try:
            c.execute("DELETE FROM Phonebook WHERE phone = ?", (phone,))
            conn.commit()
            window.destroy()
            print(f"Entry (Name: {name}, Number: {phone}) has been deleted from the phonebook.")
        except:
            print("Error occurred while deleting entry.")
    else:
        print(f"No entry found with the name '{name}'.")

if __name__ == "__main__":
    main()



