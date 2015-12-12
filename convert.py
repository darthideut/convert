#!/bin/python
from temp_mod import run_temp_menu
main_menu = 0
while main_menu != 3:
    print "----------------------------"
    print "1. Temperature Converter"
    print "2. *This is a placeholder*"
    print "3. Exit"
    main_menu = input("Welcome. Please select an option.")

    if main_menu == 1:
        print run_temp_menu()

    elif main_menu == 2:
        print "This is a placeholder."
