#Carson Banash (30085955)
#Lab: B06

#imports all of the SimpleGraphics library
from SimpleGraphics import *

#creates constants for the width and spacing of the bars
WIDTH_OF_BARS = 100
SPACING_OF_BARS = 25
#creates constants for the width and height of the graph
GRAPH_WIDTH = 400
GRAPH_HEIGHT = 300

    
#asks the user to input the title
title = input("What should the title be? ")

#asks the user for the values of all of the bars giving them the range 0-300
hob1 = float(input("How tall should the first bar be? (0-300) "))
hob2 = float(input("How tall should the second bar be? (0-300) "))
hob3 = float(input("How tall should the third bar be? (0-300) "))

#asks the user for the colour of each of the bars
cob1 = input("What colour should the first bar be? ")
cob2 = input("What colour should the second bar be? ")
cob3 = input("What colour should the third bar be? ")

#asks the user for the x and y coordinate of the origin
xcord = float(input("Where would you like the x coordinate of the origin of the graph? (0-800) "))
ycord = float(input("Where would you like the y coordinate of the origin of the graph? (0-600) "))

#sets the font format to Ariel with a text size of 25 and makes the text bold
setFont("Ariel", "25",  "bold")
#places the specified title at the proper x and y coordinates
text(xcord + (GRAPH_WIDTH/2), ycord - (GRAPH_HEIGHT + 25), title)

#creates the x and y axis at the specified x and y coordinate given by the user
line(xcord, ycord - GRAPH_HEIGHT, xcord, ycord, xcord + GRAPH_WIDTH, ycord)

#sets the specified colour of the first bar and places it in the correct location with 
#the appropriate dimensions and specified height
setFill(cob1)
rect(xcord+ SPACING_OF_BARS, ycord - hob1, WIDTH_OF_BARS, hob1)

#sets the specified colour of the second bar and places it in the correct location with 
#the appropriate dimensions and specified height
setFill(cob2)
rect(xcord + (2*SPACING_OF_BARS  + WIDTH_OF_BARS), ycord - hob2, WIDTH_OF_BARS, hob2)

#sets the specified colour of the third bar and places it in the correct location with 
#the appropriate dimensions and specified height
setFill(cob3)
rect(xcord + (3*SPACING_OF_BARS + 2*WIDTH_OF_BARS), ycord - hob3, WIDTH_OF_BARS, hob3)