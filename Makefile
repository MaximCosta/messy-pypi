count_lignes:
	echo "---------------------------------------------"
	echo "NE PAS EXECUTER, SI ON SAIT PAS CE QUE SA FAIT"
	echo "DO NOT EXECUTE, IF YOU DONT KNOW WHAT YOU DO"
	echo "---------------------------------------------"
	sleep 4
	sudo cp $(CURDIR)/messy_pypi/main_countlignes.py /bin/main_countlignes
	sudo chmod 755 /bin/main_countlignes
	
terminal_snake:
	echo "---------------------------------------------"
	echo "NE PAS EXECUTER, SI ON SAIT PAS CE QUE SA FAIT"
	echo "DO NOT EXECUTE, IF YOU DONT KNOW WHAT YOU DO"
	echo "---------------------------------------------"
	sleep 4
	sudo cp $(CURDIR)/messy_pypi/main_terminalsnake.py /bin/main_snake
	sudo chmod 755 /bin/main_snake
