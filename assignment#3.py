#Carson Banash (30085955)
#Lab B06

#imports all of the simple graphics library
from SimpleGraphics import *

#has holds all of the logic for the users choice
#there are no parameters
#there is only one return, that being the integer for the users choice
def handleInput ():

    #prints the choices for the user to choose from
    print("Choose a transform type from the following:")
    print("1: Combine two whole images.")
    print("2: Vertically combine two images.")
    print("3: Horizontally combine two images.")
    #gets the users input as an integer
    choice = int(input("What is your choice? "))

    #this loop is responsible for asking the question again if the users input(choice) isn't equal to either 1,2, or 3
    while choice != 1 and choice != 2 and choice != 3 :
        #prints the choices again 
        print("please enter either 1,2, or 3. again your choices are:")
        print("1: Combine two whole images.")
        print("2: Vertically combine two images.")
        print("3: Horizontally combine two images.")
        choice = int(input("What is your choice? ")) #gets the users input again

    #returns the users choice and ends the function.
    return choice

#this function is responsible for combining the pixels from two images into one pixel 
#the parameters are:
#image_1: this gives the function the first image in its entirety
#image_2: this gives the function the second image in its entirety
#x and y: these give the x and y location of the two pixels to be blended
#the function then returns the averaged colour values for red green and blue
def blendPixel (image_1, image_2, x, y):
    #gets the red green and blue values for each image at the given x and y coordinate
    r_img1, g_img1, b_img1 = getPixel(image_1, x, y)
    r_img2, g_img2, b_img2 = getPixel(image_2, x, y)

    #calculates the average red green and blue values for the two images with the information obtained from the images
    r_avg = r_img1 + r_img2 / 2
    g_avg = g_img1 + g_img2 / 2
    b_avg = b_img1 + b_img2 / 2
    #returns the average for the red green and blue values
    return r_avg, g_avg, b_avg

#this function is responsible for creating a new image that is the entire combination of images one and two,
#in order to do this the blend pixel function is required
#the paramaters are:
#image_1: this gives the function the entirety of the first image
#image_2: this gives the function the entirety of the second image
#the function then returns the image that is the average of both, or in other words the blended image
def combineAll (image_1, image_2):
    #creates a new image which will be filled with pixels having the values of rgb obtained from the blendPixel function
    allBlended = createImage(getWidth(image_1), getHeight(image_1))

    #these two for loops with the ranges of the height and the width of image 1 (or it could be image 2 since they are both the same size)
    #are responsible for going through the images one pixel at a time
    for y in range(getHeight(image_1)):
            for x in range(getWidth(image_1)):
                #gets the red green and blue values from the blendPixel
                r,g,b = blendPixel(image_1, image_2, x, y)
                #puts a new pixel in the new image created with the average rgb values obtained from the blendPixel function
                #and at the given x and y position
                putPixel(allBlended, x, y, r/1.5, g/1.5, b/1.5)
    #returns the image that is the combination of both of the images
    return allBlended

#this function is responsible for combining the two whole images either vertically or horizontally, which is determined by user input
#the paramaters are:
#image_1: this gives the function the entirety of the first image
#image_2: this gives the function the entirety of the second image
#choice: this is the users input, which determines whether the image will be combined vertically or horizontally
#the function returns a new image that is combined in the middle either vertically or horizontally
def combineParts(image_1, image_2, choice):
    #this if statement is to decide if the blend should be vertical or horizontal, in this case its vertical
    if choice == 2:
        #creates a new image that will be filled with the new pixels, which depend on the users choice
        partlyBlended = createImage(getWidth(image_1), getHeight(image_1))
        #these two for loops with the ranges of the height and the width of image 1 (or it could be image 2 since they are both the same size)
        #are responsible for going through the images one pixel at a time
        for y in range(getHeight(image_1)):
            for x in range(getWidth(image_1)):
                #gets the red green and blue values from each image
                r_img1, g_img1, b_img1 = getPixel(image_1, x, y)
                r_img2, g_img2, b_img2 = getPixel(image_2, x, y)

                #this if statement is for putting the first image on the left side of the blended portion
                if x <= (getWidth(image_1)/3):
                    putPixel(partlyBlended, x, y, r_img1, g_img1, b_img1)

                #this if statement is for putting the blended pixels in the middle of the new image
                elif (getWidth(image_1)/3)<x<((getWidth(image_1)/3)*2):
                    #calls the blendPixel function with the correct parameters, this is so that the middle section is blended
                    r,g,b = blendPixel(image_1, image_2, x, y)
                    #puts the blended pixels in the middle third of the image
                    putPixel(partlyBlended, x, y, r/1.5, g/1.5, b/1.5)

                #this if statement is for putting the second image on the right side of the blended portion
                elif x>((getWidth(image_1)/3)*2):
                    #puts the pixels from the second image in the right third of the image
                    putPixel(partlyBlended, x, y, r_img2, g_img2, b_img2)

    #this if statement is to decide if the blend should be vertical or horizontal, in this case its horizontal
    elif choice == 3:
        #creates a new image that will be filled with the new pixels, which depend on the users choice
        partlyBlended = createImage(getWidth(image_1), getHeight(image_1))
        #these two for loops with the ranges of the height and the width of image 1 (or it could be image 2 since they are both the same size)
        #are responsible for going through the images one pixel at a time
        for y in range(getHeight(image_1)):
            for x in range(getWidth(image_1)):
                #gets the red green and blue values from each image
                r_img1, g_img1, b_img1 = getPixel(image_1, x, y)
                r_img2, g_img2, b_img2 = getPixel(image_2, x, y)

                #this if statement is for putting the first image in the top of the blended area
                if y <= (getHeight(image_1)/3):
                    #puts the pixels from the fist image on the top third of the image
                    putPixel(partlyBlended, x, y, r_img1, g_img1, b_img1)

                #this if statement is for putting the blended pixels in the middle of the new image
                elif (getHeight(image_1)/3)<y<((getHeight(image_1)/3)*2):
                    #calls the blend pixel function with the correct parameters, this is done so that the middle section is blended
                    r,g,b = blendPixel(image_1, image_2, x, y)
                    #puts the blended pixel in the middle third of the image
                    putPixel(partlyBlended, x, y, r/1.5, g/1.5, b/1.5)

                #this if statement is for putting the second image in the bottom of the blended area
                elif y>((getHeight(image_1)/3)*2):
                    #puts the pixels from the second image on the bottom third of the image
                    putPixel(partlyBlended, x, y, r_img2, g_img2, b_img2)

    #returns the image, that being the partial blend of image one and image two
    return partlyBlended

#this function is responsible for the high-level processing, like the processing of the choice,
#all of the other functions are called here as-well,
#there are no parameters 
#there are no returns
def main ():
    #loads both of the images for use in the rest of the program
    image_1 = loadImage("/Users/carson/Desktop/DATA 211/Assignments/Mars.gif")
    image_2 = loadImage("/Users/carson/Desktop/DATA 211/Assignments/Water.gif") 
    #resizes the window to the size of both of the images (only use image_1 but could use image_2 because they are the same size)
    resize(getWidth(image_1), getHeight(image_1))

    #sets the variable choice equal to the return of the handleInput function
    choice = handleInput()

    #says that if the choice is the number one then the user has chosen to completely combine both images
    if choice == 1:
        
        #draws the image of the return of the combineAll function at the coordinate (0,0)
        drawImage(combineAll(image_1, image_2), 0, 0)
        #when the calculations are finished the program will print that the users image is complete
        print("Your image is complete.")

    #says that if the user chose option 2 then they chose to combine the images vertically
    elif choice == 2:
        #draws the image of the return of the combineParts function (which will be a vertically combined image) at the coordinate (0,0)
        drawImage(combineParts(image_1, image_2, choice), 0, 0)
        #when the calculations are finished the program will print that the users image is complete
        print("Your image is complete.")

    #says that if the user chose option 3 then they chose to combine the images horizontally
    elif choice == 3:

        #draws the image of the return of the combineParts function (which will be a horizontally combined image) at the coordinate (0,0)
        drawImage(combineParts(image_1, image_2, choice), 0, 0)
        #when the calculations are finished the program will print that the users image is complete
        print("Your image is complete.")
    
#calls the main function to start the program
main()