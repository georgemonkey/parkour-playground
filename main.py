from cmu_graphics import *
import numpy as np
import matplotlib as plt
import math
def drawGrid(spacing=50, color='lightGray'):
    for x in range(0, app.width, spacing):
        Line(x, 0, x, app.height, fill=color)
    for y in range(0, app.height, spacing):
        Line(0, y, app.width, y, fill=color)
drawGrid()
app.background=gradient(rgb(255,69,0),rgb(255,90,0),rgb(255,110,0),rgb(255,130,0),rgb(255,140,0),start='left')

Start=Rect(0,160,60,140,fill='gold')
Rect(120,220,40,80,fill='yellow')
Rect(200,200,40,100,fill='yellow')
Rect(280,200,40,100,fill='yellow')
Rect(280,0,40,140,fill='yellow')
Finish=Rect(360,180,40,120,fill='gold')
#Tsunami1=Rect(0,0,20,300,fill='darkTurquoise')
#Tsunami2=Circle(30,40,40,fill='darkTurquoise')
#Tsunami3=Circle(30,260,40,fill='darkTurquoise')
#Tsunami4=Circle(30,150,40,fill='darkTurquoise')
Rect(0,320,400,80,fill='green')
Rect(0,300,400,20,fill='saddleBrown')

Player=Rect(15,110,30,50,fill='white',border='black')

Background1=Rect(0,0,400,400,fill=gradient('yellow','orange','darkOrange',start='top'))
Win=Label('You Win!',200,200,size=50,visible=False)
Loose=Label('You Lose',200,200,size=40,visible=False)
Again=Label('Press "p" to play again',200,250,size=25,visible=False)

Start1=Label('Use arrow keys and spacebar to move',200,140,size=15)
Start2=Label('Press "r" to reset',200,170,size=20)
Start3=Label('Do the parkour and run from the tsunami',200,200,size=20)
Start4=Label('Reach the finish line to finish the level, complete 3 levels to win',200,230,size=13)
Start5=Label('Press "s" to start',200,260,size=20)

def onKeyPress(key):
    if key=='s' or key=='r' or key=='p':
        Start1.visible=False
        Start2.visible=False
        Start3.visible=False
        Start4.visible=False
        Start5.visible=False
        Background1.visible=False
        Player.centerX=35
        Player.centerY=305
        Win.visible=False
        Loose.visible=False
        Again.visible=False
        Background1.visible=False
    
    elif Player.hitsShape(Finish):
        Win.visible=True
    

    elif key=='space':
        Player.centerY-=5
        def onStep():
            app.stepsPerSecond=5
            Player.centerY+=1
    elif key=='left':
        Player.centerX-=5
    elif key=='right':
        Player.centerX+=5

cmu_graphics.run()