from SimpleGraphics import *


def handleInput ():
    print("Choose a transform type from the following:")
    print("1: Combine two whole images.")
    print("2: Verticaly combine two images.")
    print("3: Horizontaly combine two images.")

    choice = int(input("What is your choice? "))

    while choice != 1 and choice != 2 and choice != 3 :
        print("please enter either 1,2, or 3. again your choices are:")
        print("1: Combine two whole images.")
        print("2: Verticaly combine two images.")
        print("3: Horizontaly combine two images.")
        choice = int(input("What is your choice? "))

    return choice

def blendPixel (parameter_list):
    pass

def combineAll (parameter_list):
    pass

def main ():
    print("your choice is", handleInput())

main()