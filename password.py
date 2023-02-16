#Para cada elemento se define la estructura clave:valor:

#Store the names of the users and the passwords
#sotre user names and passwords and ask the user to sing in
try:
	import sys
except ImportError:
	print()
	print("ERROR: Module 'sys' wasn't found")
else: 
	pass

list1 = []

def add_element_function(listt):
	"""ask for service name, username and password
		then store it in the list

		(Remember to press "Q" to quit this windows!)
	"""

	service_name = str(input("Enter web site/app name: "))
	user_name = str(input("Enter user name: "))
	user_password = str(input("Enter user password: "))

	new_item = {
		"service": service_name, 
		"user": user_name,
		"password": user_password
		}

	listt.append(new_item)
	print("Status: Element added")
	print(f"Current elements: {len(listt)}")
	print()
	return listt 

	
def list_viewer(listt):
	"""view all elements
		in a given list

		(Remember to press "Q" to quit this windows!)
	"""
	if len(listt) == 0:
		print("There are no elements")
		print()
	else:
		i = 0
		for dictionary in listt:
			i += 1
			print(f"Account #{i} »»")
			print(
				"\tService Name: ", dictionary["service"], "\n",
				"\tUser Name: ", dictionary["user"], "\n",
				"\tPassword: ", dictionary["password"], "\n",
				)

def process_info(process):
	"""Show the information of the processes
		executed in each command

		(Remember to press "Q" to quit this windows!)
	"""
	help(process)

def remove_element(listt):
	"""Prints all the registered accounts
		Asks user which one does he/she wants to remove
		Remove the account

		(Remember to press "Q" to quit this windows!)
	"""

	for dictionary in listt:
			print(
				dictionary["service"], "\n",
				dictionary["user"], "\n",
				dictionary["password"], "\n",
				)

	user_input = int(input("Which account do you wanna delete from here? (please type the position): "))
	del listt[user_input]
	print()
	return listt

menu = {
	"1": "Add new element",
	"2": "View all current elements",
	"3": "Info",
	"4": "Remove",
	"5": "Exit"
}
while(True):
	for key, value in menu.items():
		print(key +")", value)
	try:
		user_option = input()
		if user_option not in menu:
			raise TypeError
	except TypeError:
		print(f"ERROR: '{user_option}' is not a valid command, please type a valid one (1/2/3/4/5)")
	else:
		pass
		
	if user_option == "1":
		add_element_function(listt = list1)
	elif user_option == "2":
		list_viewer(listt = list1)
	elif user_option == "3":
		while(True):
			option1 = str(input("Which process do you wanna know how it works? (1/2/3/4): "))
			if option1 == "1":
				process_info(process = add_element_function)
				break
			elif option1 == "2":
				process_info(process = list_viewer)
				break
			elif option1 == "3":
				process_info(process = process_info)
				break
			elif option1 == "4":
				process_info(process = remove_element)
				break
			else:
				print(f"'{option1}' is not a command, please type a valid command (1/2/3/4): ")
				print()
	elif user_option == "4":
		remove_element(listt = list1)
	else:
		if user_option == "5":
			print("Glad I helped you!")
			sys.exit()