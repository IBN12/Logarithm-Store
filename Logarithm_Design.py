# Program: Logarithm Design
# Description: This is a mathemtical program that will will showcase
# logarithmic equations, exponential equations, and logarithmic properties.
# The program will allow the user to create logarithmic and exponential equations 
# in a looped menu system. The menu will assist the user in obtaining a value 
# from every equation and showcase their logarithmic and exponential
# properties.
#
# Properties of exponents:             Properties of Logarithms:                    Name of Property:
# b^0 = 1                              log_b(1) = 0                                 Log of 1
# b^1 = b                              log_b(b) = 1                                 Log of the base
# b^(log_b(x)) = x                     log_b(b^x) = x                               Inverse property
# (b^x)(b^y) = b^(x+y)                 log_b(xy) = log_b(x) + log_b(y)              Product property
# b^x/b^v = b^(x-y)                    log_b(x/y) = log_b(x) - log_b(y)             Quotient property
# (b^x)^n = b^nx                       log_b(x^n) = nlog_b(x)                       Power property
#
#
##########################################################################################################################################

#Libraries
import math

# Class LogProperties
class LogProperties:
    # Function Dec/Def - logarithmicEquation()
    def logarithmicEquation(self, a, b, c):
        print(f"Logaritmic Form: {c}=log_{b}({a})")
        c = math.log(a, b)
        print(f"Value: log_{b}({a}) = {c}\n")

# Variables
stopMainMenu = False # Boolean Variable that will control the main menu.
stopExpoAndLogMenu = False # Boolean variable that will control the exponential and logarithmic creation menu.
pUser = LogProperties() # Object of class type LogProperties

# while loop - Main Menu
while stopMainMenu != True:

    # while loop -The exponential and logarithmic equation creation menu:
    while stopExpoAndLogMenu != True:
        stopInvertExpoMenu = False
        print("(1) Enter numbers into a exponential equation")
        print("(2) Enter numbers into a Logarithmic equation")
        print("(3) Back to main menu")
        choice = int(input())

        if choice == 1:
            print("\nExponential form is a = b^c")
            print("c is the exponent on base b that equals a\n")

            b = int(input("Please enter any number for the base (b): "))
            c = int(input("Please enter any number for the exponent (c): "))
            print(f"You entered {b} for the base, and {c} for the exponent")
            a = pow(b, c)
            print(f"Exponential Equation Value: {b}^{c} = {a}\n")

            # while loop - Menu will allow the user to invert the exponential equation:
            while stopInvertExpoMenu != True:
                print("(1) Invert Exponential equation into a Logarithmic equation")
                print("(2) Back")
                choice = int(input())

                if choice == 1:
                    pUser.logarithmicEquation(a, b, c)
                    stopInvertExpoMenu = True
                elif choice == 2:
                    stopInvertExpoMenu = True
                else:
                    print("Invalid input. Please try again.")              
        elif choice == 2:
            print("Logarithm Equation")
        elif choice == 3:
            stopExpoAndLogMenu = True
        else:
            print("Invalid input. Please try again.")

    # Allow the user to continue the main menu or leave:
    print("\n(1) Continue in the menu")
    print("(2) Leave the menu")
    choice = int(input())
    if choice == 1:
        stopExpoAndLogMenu = False
    elif choice == 2:
        print("See Ya Later Space Cowboy")
        stopMainMenu = True






             


