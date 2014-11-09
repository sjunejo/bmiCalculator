#!/usr/bin/env python3
import re

###############################################
# BMI CALCULATOR v1.0
# by Sadruddin Junejo (https://github.com/sjunejo)
# TODO:
# - Actual Calculation
# - Unit Tests
###############################################


# CONSTANTS
GENDER_MALE = "m"
GENDER_FEMALE = "f"
SUFFIX_POUNDS = "lb"
SUFFIX_KG = "kg"

SUFFIX_METRES = "m"

REGEX_WEIGHT = '\d+\s*(kg|lb)'
REGEX_HEIGHT = '(\d+\'\s*\d+\")|(\d+(\.\d+)?m)'


INCHES_IN_ONE_METRE = 39.3700787

def main():
    gender, age, weight, height = getGender(), getAge(), getWeight(), getHeight()
    
    bmi = calculateBMI(height, weight)
    
    print("Your BMI is: " + str(bmi))
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


def calculateBMI(height, weight):
    # BMI = Weight (kg) / Height^2
    # OR: Weight (lb) * 703 / height^2 (inches)
    # Decision to make: Should I calculate in kg or lb? Answer: Depends on user input.
    
    weightValue = float(weight[:-2])
    if (weight[-2:] == SUFFIX_KG):
        if (height[-1] != SUFFIX_METRES):
            heightValue = convertFeetAndInchesToJustInches(height)
            heightValue = convertInchesToMetres(heightValue)
        else:
            heightValue = float(height[:-1])
            
        #
        
        bmi = weightValue/(heightValue**2)
    else:
        if (height[-1] == SUFFIX_METRES):
            heightValue = convertMetresToInches(float(height[:-1]))
        else:
            heightValue = convertFeetAndInchesToJustInches(height)
            
    
        bmi = (weightValue * 703 / (heightValue ** 2)) # MAGIC NUMBERS LOL
    return bmi


def determineWeightClass(bmi):
    
    return


def convertFeetAndInchesToJustInches(height):
    h_feet = height.split("'")[0]
    h_inches = height.split("'")[1].split("\"")[0]
    
    inches = int(h_feet) * 12 + int(h_inches)
    return inches

def convertMetresToInches(metres):
    return metres * INCHES_IN_ONE_METRE

def convertInchesToMetres(inches):
    return inches / INCHES_IN_ONE_METRE    


# INIT
if  __name__ =='__main__':
    main()