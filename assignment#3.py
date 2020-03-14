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

def blendPixel (image_1, image_2, x, y):
    r_img1, g_img1, b_img1 = getPixel(image_1, x, y)
    r_img2, g_img2, b_img2 = getPixel(image_2, x, y)

    r_avg = r_img1 + r_img2 / 2
    g_avg = g_img1 + g_img2 / 2
    b_avg = b_img1 + b_img2 / 2
    
    return r_avg, g_avg, b_avg

def combineAll (image_1, image_2):
    allBlended = createImage(getWidth(image_1), getHeight(image_1))
    for y in range(getHeight(image_1)):
            for x in range(getWidth(image_1)):
                r,g,b = blendPixel(image_1, image_2, x, y)
                #print(r,g,b)
                putPixel(allBlended, x, y, r/1.5, g/1.5, b/1.5)
    return(allBlended)

def combineParts(image_1, image_2, choice):
    if choice == 2:
        pass
    elif choice ==3:
        pass

def main ():
    image_1 = loadImage("/Users/carson/Desktop/DATA 211/Assignments/Mars.gif")
    image_2 = loadImage("/Users/carson/Desktop/DATA 211/Assignments/Water.gif") 
    resize(getWidth(image_1), getHeight(image_1))

    choice = handleInput()

    if choice == 1:
        
        drawImage(combineAll(image_1, image_2), 0, 0)
        print("Your image is complete.")
    else:

        combineParts(image_1, image_2, choice)
    

main()