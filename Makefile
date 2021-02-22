make: secure_house.py test.sh test_debug.sh
	cp secure_house.py secure_house
	chmod +x secure_house
	chmod +x test.sh
	chmod +x test_debug.sh
clean:
	rm secure_house
	chmod -x test.sh
	chmod -x test_debug.sh
