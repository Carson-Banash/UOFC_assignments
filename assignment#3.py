#Carson Banash (30085955)
#Lab B06

#imports all of the simple graphics library
from SimpleGraphics import *

#has holds all of the logic for the users choice
#there are no parameters
#there is only one return, that being the integer for the users choice
def handleInput ():

    #prints the choices for the ousers choice
    print("Choose a transform type from the following:")
    print("1: Combine two whole images.")
    print("2: Vertically combine two images.")
    print("3: Horizontally combine two images.")
    #gets the users input as an integer
    choice = int(input("What is your choice? "))

    #this loop is respinsible for asking the question again if the users input(choice) isnt equal to either 1,2, or 3
    while choice != 1 and choice != 2 and choice != 3 :
        #prints the choices again 
        print("please enter either 1,2, or 3. again your choices are:")
        print("1: Combine two whole images.")
        print("2: Vertically combine two images.")
        print("3: Horizontally combine two images.")
        choice = int(input("What is your choice? ")) #gets the users imput again
        
    #returns the users choice and ends the function.
    return choice

#this function is responsible for combining the pixels from two images into one pixel 
#the parameters are:
#image_1: this gives the function the first image in its entirety
#image_2: this gives the function the second image in its entirety
#x and y: these give the x and y location of the two pixels to be blended
#the function then returns the averaged colour values for red green and blue
def blendPixel (image_1, image_2, x, y):
    r_img1, g_img1, b_img1 = getPixel(image_1, x, y)
    r_img2, g_img2, b_img2 = getPixel(image_2, x, y)

    r_avg = r_img1 + r_img2 / 2
    g_avg = g_img1 + g_img2 / 2
    b_avg = b_img1 + b_img2 / 2
    
    return r_avg, g_avg, b_avg

#this function is responsible for creating a new image that is the entire combination of images one and two,
#in order to do this the blend pixel function is required
#the paramaters are:
#image_1: this gives the function the entirety of the first image
#image_2: this gives the function the entirety of the second image
#the function then returns the image that is the average of both, or in other words the blended image
def combineAll (image_1, image_2):

    allBlended = createImage(getWidth(image_1), getHeight(image_1))

    for y in range(getHeight(image_1)):
            for x in range(getWidth(image_1)):

                r,g,b = blendPixel(image_1, image_2, x, y)
                putPixel(allBlended, x, y, r/1.5, g/1.5, b/1.5)

    return allBlended

#this function is responsible for combining the two whole images either vertically or horizontally, which is determined by user input
#the paramaters are:
#image_1: this gives the function the entirety of the first image
#image_2: this gives the function the entirety of the second image
#choice: this is the users input, which determines whether the image will be combined vertically or horizontally
#the function returns a new image that is combined in the middle either vertically or horizontally
def combineParts(image_1, image_2, choice):

    choice = choice 

    if choice == 2:
        partlyBlended = createImage(getWidth(image_1), getHeight(image_1))
        for y in range(getHeight(image_1)):
            for x in range(getWidth(image_1)):

                r_img1, g_img1, b_img1 = getPixel(image_1, x, y)
                r_img2, g_img2, b_img2 = getPixel(image_2, x, y)

                if x <= (getWidth(image_1)/3):
                    putPixel(partlyBlended, x, y, r_img1, g_img1, b_img1)

                elif (getWidth(image_1)/3)<x<((getWidth(image_1)/3)*2):
                    r,g,b = blendPixel(image_1, image_2, x, y)
                    putPixel(partlyBlended, x, y, r/1.5, g/1.5, b/1.5)

                elif x>((getWidth(image_1)/3)*2):
                    putPixel(partlyBlended, x, y, r_img2, g_img2, b_img2)

    elif choice == 3:
        partlyBlended = createImage(getWidth(image_1), getHeight(image_1))
        for y in range(getHeight(image_1)):
            for x in range(getWidth(image_1)):

                r_img1, g_img1, b_img1 = getPixel(image_1, x, y)
                r_img2, g_img2, b_img2 = getPixel(image_2, x, y)

                if y <= (getHeight(image_1)/3):
                    putPixel(partlyBlended, x, y, r_img1, g_img1, b_img1)

                elif (getHeight(image_1)/3)<y<((getHeight(image_1)/3)*2):
                    r,g,b = blendPixel(image_1, image_2, x, y)
                    putPixel(partlyBlended, x, y, r/1.5, g/1.5, b/1.5)

                elif y>((getHeight(image_1)/3)*2):
                    putPixel(partlyBlended, x, y, r_img2, g_img2, b_img2)

    return partlyBlended

#this function is responsible for the high-level processing, like the processing of the choice,
#all of the other functions are called here as-well,
#there are no parameters 
#there are no returns
def main ():
    image_1 = loadImage("/Users/carson/Desktop/DATA 211/Assignments/Mars.gif")
    image_2 = loadImage("/Users/carson/Desktop/DATA 211/Assignments/Water.gif") 
    resize(getWidth(image_1), getHeight(image_1))

    choice = handleInput()

    if choice == 1:
        
        drawImage(combineAll(image_1, image_2), 0, 0)
        print("Your image is complete.")

    elif choice == 2:

        drawImage(combineParts(image_1, image_2, choice), 0, 0)
        print("Your image is complete.")

    elif choice == 3:

        drawImage(combineParts(image_1, image_2, choice), 0, 0)
        print("Your image is complete.")
    
#calls the main function to start the program
main()