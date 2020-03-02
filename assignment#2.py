#Carson Banash (30085955)
#Lab B06

#imports all of the simple graphics library and the randint function
from SimpleGraphics import *
from random import randint
#sets the constants need to make the bar graph
HEIGHT_BG = 400
LENGTH_BG = 600
MARGIN_BG = 100
ORIGIN_BGX = MARGIN_BG
ORIGIN_BGY = HEIGHT_BG + MARGIN_BG
#sets the constants need for making the pie chart
DIAMATER_PC = 400
#initializes the variables total and begin
total = 0
begin = 0
#this part prints choices and asks what type of graph is wanted 
print("Graph Types")
print("1. Bar Graph")
print("2. Pie Chart")
graph_type = int(input("What kind of graph do you want?(1 or 2) "))
title = input("What do you want the title to be? ")  #asks for the name of the title

#this if statement is responsible for drawing the bar graph
if graph_type == 1:
    #sets the font and outline for the axis and draws them
    setFont("Ariel", "10") 
    setOutline("black")
    line(MARGIN_BG, MARGIN_BG, ORIGIN_BGX, ORIGIN_BGY, LENGTH_BG + MARGIN_BG, HEIGHT_BG + MARGIN_BG)
    bars_amount = int(input("How many bars do you want?(2-6) ")) #asks for the amount of bars the user wants
    #these statements are for varying the width of the bars so that it looks good if there are only 2 bars
    #in other words it changes the width of the bars to be more if there are less of them so they don't look so small
    if bars_amount >= 5:
        bar_width = 75
    elif 5 > bars_amount >= 3:
        bar_width = 100
    else:
        bar_width = 200
   
    bar_spacing = (600 - (bars_amount * bar_width)) / (bars_amount + 1)  #calculates the spacing between the bars
    #asks for the grid interval and a title for the y axis
    grid_interval = int(input("What should the grid interval be?(10-100) ")) 
    y_axisT = input("What do you want the title of the y axis to be? ")
    #sets the correct font and size and then draws the title at the top of the graph
    setFont("Ariel", "25", "bold")
    text(MARGIN_BG+(LENGTH_BG/2), MARGIN_BG/2, title)
    #sets the correct font and size and then draws the title for the y axis at the left of the graph
    setFont("Ariel", "10", "bold")
    text(MARGIN_BG/2, MARGIN_BG + HEIGHT_BG/2, y_axisT)

    #sets the correct outline and font for the next part (the grid interval lines)
    setOutline("red")
    setFont("Ariel", "8")
    #the range is from one to the quotient of the height and grid interval (giving the number of lines that can be drawn without going over) + 1
    #this loop is responsible for creating the lines to show the height of the different bars
    for k in range(1, int(HEIGHT_BG/grid_interval + 1)): 
        #draws the line at the appropriate y value which is dependent on the k value so it moves up the graph 
        line(ORIGIN_BGX, ((MARGIN_BG+HEIGHT_BG))-(grid_interval*k), LENGTH_BG + MARGIN_BG, ((MARGIN_BG+HEIGHT_BG))-(grid_interval*k))
        total = total + (grid_interval) #calculates the total amount of all of the currently drawn lines
        text(LENGTH_BG+MARGIN_BG+2, ((MARGIN_BG+HEIGHT_BG))-(grid_interval*k), total, "w" ) #displays the value of the gridline on the right side
    
    #changes the outline back to black for the creation of the bar graphs
    setOutline("black")

    #this loop is responsible for creating the bars of the bar graph
    for i in range(1, bars_amount + 1): #the range is set so that it will draw all of the uses bars
        #asks for the title and height
        bar_title = input("name bar %i: " %i)
        bar_height = int(input("how tall do you want the %s bar?(0-400) " %bar_title))
        setFill(randint(0,255), randint(0,255), randint(0,255)) #sets the fill to a random colour, using the rgb values
        #draws the bar in the correct location 
        rect(ORIGIN_BGX+(i * bar_spacing )+((i-1) * bar_width), ORIGIN_BGY - bar_height, bar_width, bar_height)
        #sets the correct front for the height value of the bar and creates it at the top of the bar
        setFont("Ariel", "10")
        text(ORIGIN_BGX+(i * bar_spacing )+((i-1) * bar_width)+bar_width/2 ,ORIGIN_BGY-bar_height+8, bar_height)
        #sets the correct font for the title of the bar and creates under the bar
        setFont("Ariel", "15", "bold")
        text(ORIGIN_BGX+(i * bar_spacing )+((i-1) * bar_width)+bar_width/2 ,ORIGIN_BGY+10, bar_title)
    
    print("Your bar graph is complete.") #prints that it's done when the graph is completely finished being drawn

if graph_type == 2: #this section of code is set to execute only if the user chooses a pie chart
    #asks for the section amount and the value of all the sections added together
    sec_amount = int(input("How many sectors do you want?(2-6) "))
    allsec_value = int(input("What is the total value of all the sectors? "))
    #sets the correct font for the title and creates it at the top of the chart
    setFont("Ariel", "25", "bold")
    text(getWidth()/2, 15, title)
    #calculates the ratio that will be multiplied to given section widths so that if the user inputs a value that is less than
    #360 for the total of all sectors, the graph still is a complete circle
    ratio = float(360/allsec_value)
    
    #this loop is responsible for creating different sections of the pie chart
    for j in range(1, sec_amount): #the range is such that it doesn't run for the last section because the width can be calculated
        sec_title = input("name section %i: " %j)
        sec_width = int(input("how wide do you want the %s section? " %sec_title))
        
        #sets the beginning of each section to the total(which is initially zero) so that it can be drawn in the right location
        begin = total
        adjusted_secWidth = sec_width * ratio #adjusts the width so that it fills the full 360 degrees of a circle 
        
        setFill(randint(0,255), randint(0,255), randint(0,255)) #sets the fill to a random colour, using the rgb values
        #creates the pie slice with the correct stating angle and the correct width
        pieSlice(getWidth()/4,getHeight()/6,DIAMATER_PC,DIAMATER_PC, begin, adjusted_secWidth)
        #sets the font size for the legend and puts the title of the section and draws a box to show the colour 
        setFont("Ariel", "8")
        text(750, 5 + (75*j), sec_title)
        rect(725, 15 + (75*j) , 50, 50)
        #adds the section width to the total degrees 
        total = total + adjusted_secWidth

    
    sec_title = input("name the last section: ") #asks for the name of the last section 
    setFill(randint(0,255), randint(0,255), randint(0,255)) #sets the fill to a random colour, using the rgb values
    #creates the last section with the appropriate start and stop degrees
    pieSlice(getWidth()/4,getHeight()/6,DIAMATER_PC,DIAMATER_PC, total, (360-total))
    #creates the last legend colour box and title
    text(750, 5 + (75*sec_amount), sec_title)
    rect(725, 15 + (75*sec_amount) , 50, 50)

    print("Your pie chart is complete.") #prints that it's done when the chart is completely finished being drawn