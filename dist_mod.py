#!/bin/python

def m2k(mi):
    return (mi * 1.609344)

def m2f(mi):
    return (mi * 5280.0)

def k2m(km):
    return (km / 1.609344)

def k2f(km):
    return (km * 3280.8)

def f2m(ft):
    return (ft * 0.00018939)

def f2k(ft):
    return (ft / 3280.8)

def run_dist_menu():
    weight_menu = 0
    print "-------------------------------"
    print "1. Convert from Miles to Kilometers."
    print "2. Convert from Miles to Feet."
    print "3. Convert from Kilometers to Miles."
    print "4. Convert from Kilometers to Feet."
    print "5. Convert from Feet to Miles."
    print "6. Convert from Feet to Kilometers."
    print "7. Return to main menu."
    dist_menu = input("Please choose an option from the list: ")

    if dist_menu == 1:
        print "Please enter a distance in miles to convert to kilometers."
        mi = float(raw_input())
        return m2k(mi)

    elif dist_menu == 2:
        print "Please enter a distance in miles to convert to feet."
        mi = float(raw_input())
        return m2f(mi)

    elif dist_menu == 3:
        print "Please enter a distance in kilometers to convert to miles."
        km = float(raw_input())
        return k2m(km)

    elif dist_menu == 4:
        print "Please enter a distance in kilometers to convert to feet."
        km = float(raw_input())
        return k2f(km)

    elif dist_menu == 5:
        print "Please enter a distance in feet to convert to miles."
        ft = float(raw_input())
        return f2m(ft)

    elif dist_menu == 6:
        print "Please enter a distance in feet to convert to kilometers."
        ft = float(raw_input())
        return f2k(ft)
