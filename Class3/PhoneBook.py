phone_book = {'Frodo': {'Name' : 'Frodo', 'Number' : '919-999-1111'},
				'Samwise': {'Name' : 'Samwise', 'Number' : '818-888-2222'}
			}

print "-"*75
print "1. Look someone up"
print "2. Add new entry"
print "3. Modify entry"
print "4. Remove an entry"
print "5. View directory"
print "-"*75

choice = raw_input("What do you want to do?: ")

if (choice == "1"):
	print "You've chosen to look someone up..."
	Who = raw_input("Who do you want to look up?: ")
	print "You wanted to look up:"
	print phone_book[Who]['Name']
	print "Their number is:"
	print phone_book[Who]['Number']

if (choice == "2"):
	print "You've chosen to add an entry..."
	AddUserName = raw_input("What is the name of your new entry?: ")
	AddUserNum = raw_input("What is this person's phone number?: ")
	phone_book.update({AddUserName: {'Name' : AddUserName, 'Number' : AddUserNum}})
	print phone_book

if (choice == "3"):
	print "You've chosen to modify an entry..."
	NameMod = raw_input("Who do you want to change?: ")
	ChangeWhat = raw_input("Type 1 to change the name & 2 to change the number: ")
	
	if (ChangeWhat == "1"):
		print "You've chosen to change the name..."
		ChangeName = raw_input("What is the new name?: ")
		phone_book[NameMod]['Name'] = ChangeName
		print phone_book
	else:
		print "You've chosen to change the number..."
		ChangeNum = raw_input("What is the new number?: ")
		phone_book[NameMod]['Number'] = ChangeNum
		print phone_book

# if (choice == "4"):
# 	print "You've chosen to remove an entry..."
# 	NameToRemove = raw_input("Who do you want to remove?: ")
# 	phone_book.pop[NameToRemove]