#!/usr/bin/env python3

import sqlite3


conn = sqlite3.connect('phonebook.db')
c = conn.cursor()


c.execute(
	'''CREATE TABLE IF NOT EXISTS PHONEBOOK
		( PHONE INT PRIMARY KEY, \
		  NAME TEXT \
		  )''' 
		)
conn.commit() 


def printMenu():
	print (28 * "=")
	print ("==Welcome to the Phonebook==")
	print (28 * "=")
	print ("1. Look up a phone number.")
	print ("2. Add an entry.")
	print ("3. List all entries.")
	print ("4. Quit.\n")
	

def lookUpEntry():
	phone = input("Enter a phone number to look up: ")
	c.execute(' SELECT * FROM Phonebook WHERE phone = ' + phone)
	lookUp = c.fetchall()
	print ("\n",lookUp,"\n")


def addEntry():
	name = input('Enter a name: ')
	phone = input('Enter a phone number: ')
	c.execute("INSERT INTO PHONEBOOK (PHONE, NAME) VALUES(" + phone + ", '" + name + "')");
	print ("\n(%s,%s) has been added to the phonebook!\n" %(phone, name))


def listAll():
	c.execute('SELECT * FROM Phonebook')
	allData = c.fetchall()
	print("\n",allData,"\n")


def main():
	choice = ''
	while choice != '4':

		printMenu()
		choice = input("Enter you choice [1-4]: ")

		if choice == '1':
			lookUpEntry()
		elif choice == '2':
			addEntry()
		elif choice == '3':
			listAll()
		elif choice == '4':
			print("\nGoodbye!")
		else:
			print("\n!!!!! Invalid selection. Select from options [1-4] !!!!!\n")

	print ("\nExiting.")

	c.close()

if __name__ == '__main__':
	main()
