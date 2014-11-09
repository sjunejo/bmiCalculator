#!/usr/bin/env python3
import re

###############################################
# BMI CALCULATOR v1.0
# by sjunejo.github.com
# TODO:
# - Actual Calculation
# - Unit Tests
###############################################


# CONSTANTS
GENDER_MALE = "m"
GENDER_FEMALE = "f"
SUFFIX_POUNDS = "lb"
SUFFIX_KG = "kg"

REGEX_WEIGHT = '\d+\s*(kg|lb)'
REGEX_HEIGHT = '(\d+\'\s*\d+\")|(\d+m)' 

def main():
    print(getUserInput())
    return

def getUserInput():
    return getGender(), getAge(), getWeight(), getHeight()


def getAge():
    while True:
        age = raw_input("Please enter your age (years): ")
        # Age must be an integer.
        try:
            val = int(age)
            break
        except ValueError:
            print("Please try again")
            
    return age


def getGender():
    while True:
        gender = raw_input("Are you male or female? (Type M for male and F for female): ")
        if (gender.lower() == GENDER_MALE or gender == GENDER_FEMALE):
            break
        else:
            print("Incorrect input, please try again.")
            
    return gender


def getHeight():
    while (True):
        height = raw_input("Please enter your height (Either in the format: x' y\" (feet,inches) or in m, e.g. 1.67m): ")
        heightRegex = re.compile(REGEX_HEIGHT)
        if heightRegex.match(height.lower()):
            break
        else:
            print("Incorrect input. Please try again")
    
    return height


def getWeight():
    while (True):
        weight = raw_input("Please enter your weight (Suffix with 'kg' or 'lb', e.g. '100lb'): ")
        
        weightRegex = re.compile(REGEX_WEIGHT)
        if weightRegex.match(weight.lower()):
            break
        else:
            print("Incorrect input. Please try again")
    return weight


def calculateBMI(gender, age, height, weight):
    
    return
    



# INIT
if  __name__ =='__main__':
    main()