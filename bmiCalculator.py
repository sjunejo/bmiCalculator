#!/usr/bin/env python3
import re

###############################################
# BMI CALCULATOR v1.0
# by Sadruddin Junejo (https://github.com/sjunejo)
# TODO:
# Use Sex and Age data somehow (or remove them entirely)
# - Unit Tests
###############################################


# CONSTANTS
SEX_MALE = "m"
SEX_FEMALE = "f"
SUFFIX_POUNDS = "lb"
SUFFIX_KG = "kg"

SUFFIX_METRES = "m"

REGEX_WEIGHT = '\d+(\.\d+)?\s*(kg|lb)'
REGEX_HEIGHT = '(\d+\'\s*\d+\")|(\d+(\.\d+)?m)'

INCHES_IN_ONE_METRE = 39.3700787

def main():
    sex, age, weight, height = get_sex(), get_age(), get_weight(), get_height()
    
    bmi = calculate_bmi(height, weight)
    
    print("Your BMI is: " + str(bmi))
    
    print("Your weight class is: " + determine_weight_class(bmi))
    
    return


def get_age():
    while True:
        age = raw_input("Please enter your age (years): ")
        # Age must be an integer.
        try:
            val = int(age)
            break
        except ValueError:
            print("Please try again")
            
    return age


def get_sex():
    while True:
        sex = raw_input("Are you male or female? (Type M for male and F for female): ")
        if (sex.lower() == SEX_MALE or sex == SEX_FEMALE):
            break
        else:
            print("Incorrect input, please try again.")
            
    return sex


def get_height():
    while (True):
        height = raw_input("Please enter your height (Either in the format: x' y\" (feet,inches) or in m, e.g. 1.67m): ")
        height_regex = re.compile(REGEX_HEIGHT)
        if height_regex.match(height.lower()):
            break
        else:
            print("Incorrect input. Please try again")    
    return height


def get_weight():
    while (True):
        weight = raw_input("Please enter your weight (Suffix with 'kg' or 'lb', e.g. '100lb'): ")
        weight_regex = re.compile(REGEX_WEIGHT)
        if weight_regex.match(weight.lower()):
            break
        else:
            print("Incorrect input. Please try again")
    return weight


def calculate_bmi(height, weight):
    # BMI = Weight (kg) / Height^2
    # OR: Weight (lb) * 703 / height^2 (inches)
    # Decision to make: Should I calculate in kg or lb? Answer: Depends on user input.
    
    weight_value = float(weight[:-2])
    if (weight[-2:] == SUFFIX_KG):
        if (height[-1] != SUFFIX_METRES):
            height_value = convert_feet_and_inches_to_numeric_inches(height)
            height_value = convert_inches_to_metres(height_value)
        else:
            height_value = float(height[:-1])
            
        #
        
        bmi = weight_value/(height_value**2)
    else:
        if (height[-1] == SUFFIX_METRES):
            height_value = convert_metres_to_inches(float(height[:-1]))
        else:
            height_value = convert_feet_and_inches_to_numeric_inches(height)
            
    
        bmi = (weight_value * 703 / (height_value ** 2)) # MAGIC NUMBERS LOL
    return bmi


def determine_weight_class(bmi):
    # TODO: More sophisticated means of doing this!
    
    if (bmi < 18.5):
        weight_class = "UNDERWEIGHT"
    if (bmi >= 18.5 and bmi < 25.0):
        weight_class = "NORMAL"
    if (bmi >= 25.0 and bmi < 30):
        weight_class = "OVERWEIGHT"
    else:
        weight_class = "OBESE"
    
    return weight_class


def convert_feet_and_inches_to_numeric_inches(height):
    h_feet = height.split("'")[0]
    h_inches = height.split("'")[1].split("\"")[0]
    
    inches = int(h_feet) * 12 + int(h_inches)
    return inches

def convert_metres_to_inches(metres):
    return metres * INCHES_IN_ONE_METRE

def convert_inches_to_metres(inches):
    return inches / INCHES_IN_ONE_METRE    


# INIT
if  __name__ =='__main__':
    main()