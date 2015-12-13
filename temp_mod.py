#!/bin/python

def f2c(f_temp):
   return ((f_temp - 32.0) * (5.0/9.0))

def f2k(f_temp):
    return ((f_temp + 459.67) * (5.0/9.0))

def c2f(c_temp):
    return ((c_temp * (9.0/5.0)) + 32.0)

def c2k(c_temp):
    return (c_temp + 273.15)

def k2f(k_temp):
    return ((k_temp * (9/5)) - 459.67)

def k2c(k_temp):
    return (k_temp - 273.15)

def run_temp_menu():
    temp_menu = 0
    print "---------------------------------------"
    print "1. Convert from Fahrenheit to Celsius."
    print "2. Convert from Fahrenheit to Kelvin."
    print "3. Convert from Celsius to Fahrenheit."
    print "4. Convert from Celsius to Kelvin."
    print "5. Convert from Kelvin to Fahrenheit."
    print "6. Convert from Kelvin to Celsius."
    print "7. Return to main menu."
    temp_menu = input("Please choose an option from the list: ")

    if temp_menu == 1:
        print "Please enter a temperature in Fahrenheit to convert to Celsius."
        f_temp = float(raw_input())
        return f2c(f_temp)

    elif temp_menu == 2:
        print "Please enter a temperature in Fahrenheit to convert to Kelvin."
        f_temp = float(raw_input())
        return f2k(f_temp)

    elif temp_menu == 3:
        print "Please enter a temperature in Celsius to convert to Fahrenheit."
        c_temp = float(raw_input())
        return c2f(c_temp)

    elif temp_menu == 4:
        print "Please enter a temperature in Celsius to convert to Kelvin."
        c_temp = float(raw_input())
        return c2k(c_temp)

    elif temp_menu == 5:
        print "Please enter a temperature in Kelvin to convert to Fahrenheit."
        k_temp = float(raw_input())
        return k2f(k_temp)

    elif temp_menu == 6:
        print "Please enter a temperature in Kelvin to convert to Celsius."
        k_temp = float(raw_input())
        return k2c(k_temp)
