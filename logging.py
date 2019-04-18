import os
import subprocess


print "1) Start mirror without options"
print "2) Show info"
print "3) Show logs"
print "4) Show errors"
print "5) Show requests"
print "6) Leave"
option = input("Choose an option? ")

while option > 6:
	print "1) Start mirror without options"
	print "2) Show info"
	print "3) Show logs"
	print "4) Show errors"
	print "5) Show requests"
	print "6) Leave"
	option = input("Choose an option? ")

if option == 1:
	print "1) Logging to file"
	print "2) No logging"
	option2 = input("Choose an option? ")
	if option2 == 1:
		os.system("npm start 2>> /home/pi/MagicMirrorLogging/err.log 1>&1 | tee -a /home/pi/MagicMirrorLogging/log.log")
	elif option2 == 2:
		os.system("npm start")
	else:
		print "select a right option"
elif option == 2:
	print "1) Logging to file"
	print "2) No logging"
	option2 = input("Choose an option? ")
	if option2 == 1:
		os.system("npm start 2>> /home/pi/MagicMirrorLogging/err.log 1>&1 | tee -a /home/pi/MagicMirrorLogging/log.log | grep -i '<info>'")
	elif option2 == 2:
		os.system("npm start 2> /dev/null | grep -i '<info>'")
	else:
		print "select a right option"
elif option == 3:
	print "1) Logging to file"
	print "2) No logging"
	option2 = input("Choose an option? ")
	if option2 == 1:
		os.system("npm start 2>> /home/pi/MagicMirrorLogging/err.log 1>&1 | tee -a /home/pi/MagicMirrorLogging/log.log | grep -i '<log>'")
	elif option2 == 2:
		os.system("npm start 2> /dev/null | grep -i '<log>'")
	else:
		print "select a right option"
elif option == 4:
	os.system("npm start 1> /dev/null")
elif option == 5:
	os.system("npm start 2> /dev/null | grep -i '\"lvl\":\"INFO\"'") 
elif option == 6:
	os.system("pkill -INT sox")

	