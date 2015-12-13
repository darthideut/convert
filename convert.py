#!/bin/python
from temp_mod import run_temp_menu
from weight_mod import run_weight_menu
from dist_mod import run_dist_menu
main_menu = 0
while main_menu != 3:
    print "----------------------------"
    print "1. Temperature Converter"
    print "2. Weight Converter"
    print "3. Distance Converter"
    print "4. Exit"
    main_menu = input("Welcome. Please select an option. ")

    if main_menu == 1:
        print run_temp_menu()

    elif main_menu == 2:
        print run_weight_menu()

    elif main_menu == 3:
        print run_dist_menu()
