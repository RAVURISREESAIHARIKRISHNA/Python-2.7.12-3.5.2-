import sys

birthdays = {"Alice": "Apr 1", "Bob": "Dec 12", "Carol": "Mar 4"}

while(True):
	print("Enter the name of the Candidate :\nEnter blank to exit")
	name = input()
	name = '"'+name+'"'
	if(name == ''):
		sys.exit(0)
	
	if name in birthdays :
		print("The Birthday of "+ name +" is on "+birthdays[name])
	else:
		print("candidate not found,Well!!!\nTell his Birthday I will remember")
		bday = input()
		birthday [ name ] = bday
		print("Got you!!")
