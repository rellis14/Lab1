#!/usr/bin/env python3
from datetime import date

def calcAge(birthdate):
    currentdate = date.today().year
    return int(currentdate) - int(birthdate)

if __name__ == '__main__':
    born = input("Please enter the year you were born: ")
    print("You are " + str(calcAge(born)) + " years old.")
