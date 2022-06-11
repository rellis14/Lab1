#!/usr/bin/env python3
#garbage comment for screenshot
from datetime import date

def calcAge(birthdate):
    currentdate = date.today().year
    try:
      age = int(currentdate) - int(birthdate)
      return age
    except TypeError:
      print("Please enter an int.")
    except ValueError:
      print("Please enter an int.")

def helloWorld():
	print('Hello World')

if __name__ == '__main__':
    born = input("Please enter the year you were born: ")
    print("You are " + str(calcAge(born)) + " years old.")
    helloWorld()