import os
import subprocess
import datetime

now = datetime.datetime.now()
#day = now.strftime("%Y-%m-%d")

def menu():
	print "1) Show info"
	print "2) Show logs"
	print "3) Show errors"
	print "4) Show requests"
	print "5) to quit"
	user_input = input("Give an option: ")
	while user_input != 5:
		if user_input == 1:
			os.system("grep -i '<info>' /home/pi/MagicMirrorLogging/log.log")
		elif user_input == 2:
			module = raw_input("geef module: ")
			day = raw_input("give a day (YYYY-mm-dd): ")
			number = raw_input("number of lines: ")
			searchLog(module, day, number)
		elif user_input == 3:
			os.system("grep -i '<error>' /home/pi/MagicMirrorLogging/err.log")
		elif user_input == 4:
			os.system("grep -i '\"lvl\":\"INFO\"' /home/pi/MagicMirrorLogging/log.log")
		else:
			print('Unknown command-please try again.')
		print "1) Show info"
		print "2) Show logs"
		print "3) Show errors"
		print "4) Show requests"
		print "5) to quit"
		user_input = input("Give an option: ")

def searchLog(module, day, number):
	os.system("grep -i '<log>' /home/pi/MagicMirrorLogging/log.log | grep -i '" + module +"' | grep -i '" + day + "' | tail -" + number)
menu()