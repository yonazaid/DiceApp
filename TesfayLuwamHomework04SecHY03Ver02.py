# Project:      Homework 04(TesfayLuwamhomework04SecHY03Ver02.py)
# Name:         Luwam Tesfay
# Date:         12/06/2017
# Description:  This program will let the user roll a dice 5 times and it will
#               add the numbers and tell them how luck they are. 


from graphics import *
import random

# Function that draws each dot
def Dot(center, win):

    # Displays a black circle
    Dot = Circle(center, 25)
    Dot.setFill("black")
    Dot.draw(win)

# Function that displays the dice face and calls the dot function
def Dice(win1):
    click=False
    # Create the dice face

    #Initialise
    win=win1
    paint_canvas(win)
    cnt=True
    cntDice=0
    c=0

    ##pause the program untill the user clicks
    win.getMouse()

    #The program loops 5 times when clicked
    while click==False:
        
        #The program is looping counting on 5 
        while cnt==True:
            c=c+1

         
            print("you have ",5-c,"rolls left")

            #import random numbers
            DiceRandom = random.randint(1,6)
            if DiceRandom == 1:
                paint_canvas(win)

                Dot(Point(200, 200), win)
   
                cntDice=cntDice+1
                clickX=win.getMouse()
                
            elif DiceRandom == 2:
                paint_canvas(win)


                Dot(Point(200, 200), win)
                Dot(Point(275, 125), win)
  
                cntDice=cntDice+2
                clickX=win.getMouse()
                
            elif DiceRandom == 3:
                paint_canvas(win)
       

                Dot(Point(200, 200), win)
                Dot(Point(275, 125), win)
                Dot(Point(125, 275), win)
                cntDice=cntDice+3
                clickX=win.getMouse()
            elif DiceRandom == 4:
                paint_canvas(win)


                Dot(Point(275, 125,), win)
                Dot(Point(125, 125), win)
                Dot(Point(275, 275), win)    
                Dot(Point(125, 275), win)
      
                cntDice=cntDice+4
                clickX=win.getMouse()
                
            elif DiceRandom == 5:
                paint_canvas(win)


                Dot(Point(200, 200), win)
                Dot(Point(125, 125), win)
                Dot(Point(275, 275), win)    
                Dot(Point(125, 275), win)
                Dot(Point(275, 125), win)

                #its counting the score
                cntDice=cntDice+4
                clickX=win.getMouse()

            elif DiceRandom == 6:
                paint_canvas(win)


                Dot(Point(125, 200), win)
                Dot(Point(125, 125), win)
                Dot(Point(275, 275), win)    
                Dot(Point(125, 275), win)
                Dot(Point(275, 125), win)
                Dot(Point(275, 200), win)

                #its counting the score
                cntDice=cntDice+4
                clickX=win.getMouse()
 
            #The progam will kick the user out when looped 5 times.
            if c==5:
                cnt=False
        #The outher while loop
        click=True
    #display the users score
    print("Your score is: ", cntDice)
    if  cntDice >25:
        print("you are lucky")
    elif cntDice >15 and cntDice <=25:
        print("you are good")
    elif cntDice >10 and cntDice >=15:
        print ("you have okey luck")
    else :
        print ("Sorry you are not lucky")

    


# This program will crate the dots
def paint_canvas(win):
        DiceFace = Rectangle(Point(50,50), Point(350,350))
        DiceFace.setFill("white")
        DiceFace.setOutline("white")
        DiceFace.draw(win)
    
def main():
    
    # Create window & background color
    win = GraphWin("Lab 8: Dice", 400, 400)
    win.setBackground(color_rgb(224,227,146))

    #creat the dice
    btnOutline = Rectangle(Point(300,360), Point(350,390))
    btnOutline.setFill("white")
    btnOutline.setOutline("black")
    btnOutline.draw(win)
    btnPress = Text(Point(330,375),"Exit")
    btnPress.setTextColor("black")
    btnPress.setStyle("bold")
    btnPress.draw(win)

    #crate a text to let the user know that they have 5 rools
    btnPress = Text(Point(50, 25),"Dice Total")
    btnPress.setTextColor("red")
    btnPress.setSize(18)
    btnPress.draw(win)
    btnPress = Text(Point(100, 25),"5")
    btnPress.setTextColor("red")
    btnPress.setSize(18)
    btnPress.draw(win)


    # Calls the dice function
    Dice(win)

    # Pauses program and closes
    win.getMouse()
    win.close()

main()

