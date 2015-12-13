#!/bin/python

def p2k(lbs):
    return (lbs * 0.45359237)

def p2s(lbs):
    return (lbs / 14)

def k2p(kgs):
    return (kgs / 0.45359237)

def k2s(kgs):
    return (kgs / 6.35029318)

def s2p(sts):
    return (sts * 14)

def s2k(sts):
    return (sts * 6.35029318)

def run_weight_menu():
    weight_menu = 0
    print "-------------------------------"
    print "1. Convert from Pounds to Kilograms."
    print "2. Convert from Pounds to Stones."
    print "3. Convert from Kilograms to Pounds."
    print "4. Convert from Kilograms to Stones."
    print "5. Convert from Stones to Pounds."
    print "6. Convert from Stones to Kilograms."
    print "7. Return to main menu."
    weight_menu = input("Please choose an option from the list: ")

    if weight_menu == 1:
        print "Please enter a weight in pounds to convert to kilograms."
        lbs = float(raw_input())
        return p2k(lbs)

    elif weight_menu == 2:
        print "Please enter a weight in pounds to convert to stones."
        lbs = float(raw_input())
        return p2s(lbs)

    elif weight_menu == 3:
        print "Please enter a weight in kilograms to convert to pounds."
        kgs = float(raw_input())
        return k2p(kgs)

    elif weight_menu == 4:
        print "Please enter a weight in kilograms to convert to stones."
        kgs = float(raw_input())
        return k2s(kgs)

    elif weight_menu == 5:
        print "Please enter a weight in stones to convert to pounds."
        sts = float(raw_input())
        return s2p(sts)

    elif weight_menu == 6:
        print "Please enter a weight in stones to convert to kilograms."
        sts = float(raw_input())
        return s2k(sts)
