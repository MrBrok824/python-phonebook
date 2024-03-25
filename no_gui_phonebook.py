import sqlite3

conn = sqlite3.connect('phonebook.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS PHONEBOOK
             (PHONE TEXT PRIMARY KEY, NAME TEXT)''')
conn.commit()

def printMenu():
    print("=" * 28)
    print("== Welcome to the Phonebook ==")
    print("=" * 28)
    print("\n1. Look up a phone number.")
    print("\n2. Add an entry.")
    print("\n3. List all entries.")
    print("\n4. Edit an existing entry.")
    print("\n5. Delete an existing entry.")
    print("\n6. Quit.\n")

def lookUpEntry():
    phone = input("\nEnter a phone number to look up: ")
    c.execute("SELECT * FROM PHONEBOOK WHERE PHONE = ?", (phone,))
    lookup = c.fetchone()
    if lookup:
        name = lookup[1]
        print(f"\nName: {name}")
        print(f"Phone number: {phone}\n")
    else:
        print("\nNo users with that phone number.\n")

def addEntry():
    name = input("\nEnter a name: ")
    phone = input("Enter a phone number: ")
    c.execute("INSERT INTO PHONEBOOK (PHONE, NAME) VALUES (?, ?)", (phone, name))
    conn.commit()
    print(f"\nUser ({name}, {phone}) has been added to the phonebook!\n")

def listAll():
    c.execute("SELECT * FROM PHONEBOOK")
    allData = c.fetchall()
    if allData:
        print("\nAll entries:\n")
        for entry in allData:
            phone, name = entry
            print(f"Name: {name}")
            print(f"Phone number: {phone}\n")
    else:
        print("\nPhonebook is empty.\n")

def editEntry():
    phone = input("\nEnter the phone number of the user you want to change: ")
    c.execute("SELECT * FROM PHONEBOOK WHERE PHONE = ?", (phone,))
    lookup = c.fetchone()
    if lookup:
        name = lookup[1]
        new_name = input(f"Insert new name for {name}: ")
        c.execute("UPDATE PHONEBOOK SET NAME = ? WHERE PHONE = ?", (new_name, phone))
        conn.commit()
        print(f"\nThe name for the user with phone number {phone} is changed to {new_name}\n")
    else:
        print("\nThere are no users with that phone number.\n")

def deleteEntry():
    phone = input("\nEnter the phone number of the user you want to delete: ")
    c.execute("SELECT * FROM PHONEBOOK WHERE PHONE = ?", (phone,))
    lookup = c.fetchone()
    if lookup:
        name = lookup[1]
        c.execute("DELETE FROM PHONEBOOK WHERE PHONE = ?", (phone,))
        conn.commit()
        print(f"\nUser {name} with phone number {phone} was successfully deleted from the Phonebook.\n")
    else:
        print("\nThere are no users with that phone number.\n")

def main():
    choice = ''
    while choice != '6':
        printMenu()
        choice = input("Enter your choice [1-6]: ")
        if choice == '1':
            lookUpEntry()
        elif choice == '2':
            addEntry()
        elif choice == '3':
            listAll()
        elif choice == '4':
            editEntry()
        elif choice == '5':
            deleteEntry()
        elif choice == '6':
            print("\nGoodbye!")
        else:
            print("\nInvalid selection. Select from options [1-6].\n")
            if input("Do you want to exit the program? [y/n] ").lower() == 'y':
                print("\nGoodbye!")
                break

    conn.close()

if __name__ == '__main__':
    main()

if __name__ == '__main__':
	main()
