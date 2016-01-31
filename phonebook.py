#!/usr/bin/env python3.5
import os
import sys


def clear():

	if os.name == 'nt':

		os.system('cls')

	else:

		os.system('clear')

def start():

	phonebook = []

	while True:

		direction = input("""\n Do you want to [V]iew your phonebook?
						  \n Or [A]dd a person? Or [D]elete a person?
						  \n Or [S]earch a contact?
						  \n Or [Q]uit?
						  \n Type the letter in the square bracket """).lower()

		if direction == 'v':

			clear()
			view_phonebook(phonebook)

		elif direction == 'a':

			clear()
			add_person(phonebook)

		elif direction == 'd':

			clear()
			delete_person(phonebook)

		elif direction == 's':

			clear()
			search_contact(phonebook)

		elif direction == 'q':

			sys.exit()

		else:

			print("Please type one of the letters in the brackets")

def view_phonebook(phonebook):

	for contact in phonebook:

		print(contact)

def add_person(phonebook):

	first_name = input("First Name? ").capitalize()
	last_name = input("Last Name? ").capitalize()
	age = int(input("age? "))
	phone_number = input("Phonenumber ")
	new_contact = [first_name, last_name, age, phone_number]
	phonebook.append(new_contact)
	print("Your contact has been added!")

def delete_person(phonebook):

	first_name = input("What is the first name of the person? ").capitalize()
	last_name = input("What is the last name of the person? ").capitalize()

	for contact in phonebook:

		if first_name and last_name in contact:

			phonebook.remove(contact)

	print("That person has been removed!")

def search_contact(phonebook):

	last_name = input("Enter the last person's name ").capitalize()

	for contact in phonebook:

		if last_name in contact:

			print(contact)
			break

	else:

		print("I did not find that contact in your phonebook.")
		search_contact()

start()