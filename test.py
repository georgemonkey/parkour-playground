print('hi')
print('hiiiii')

from cmu_graphics import *
#App Background
app.background=gradient('blue','lightBlue','skyBlue',start='top')


#Grass and Ground
Rect(0,340,400,60,fill='green')
Line(0,335,400,335,fill='saddleBrown',lineWidth=10)


#Player
Player=Rect(20,280,30,50,fill='white',border='black')


#Finish Line
Finish=Rect(360,0,40,330,fill='white')


#Objects that obstruct or cause you to loose
Obstacle1=Rect(80,120,40,220,fill='saddleBrown')
Obstacle2=Rect(160,0,40,250,fill='saddleBrown')
Obstacle3=Rect(280,0,40,140,fill='saddleBrown')
Obstacle4=Rect(280,250,40,90,fill='saddleBrown')
Spike1=Polygon(80,120,120,120,100,100,fill='maroon')
Spike11=Line(100,100,100,120,fill='maroon')
Spike2=Polygon(160,250,200,250,180,270,fill='maroon')
Spike22=Line(180,270,180,250,fill='maroon')
Spike3=Polygon(280,140,320,140,300,160,fill='maroon')
Spike33=Line(300,160,300,140,fill='maroon')
Spike4=Polygon(280,250,320,250,300,230,fill='maroon')
Spike44=Line(300,230,300,250,fill='maroon')


#Labels that show up when you win,loose,start. And a switch in the background
Background1=Rect(0,0,400,400,fill=gradient('yellow','orange','darkOrange',start='top'))
Win=Label('You Win!',200,200,size=50,visible=False)
Loose=Label('You Lose',200,200,size=40,visible=False)
Again=Label('Press "p" to play again',200,250,size=25,visible=False)

Start1=Label('Use arrow keys to move',200,140,size=20)
Start2=Label('Press "r" to reset',200,170,size=20)
Start3=Label('Dodge the obstacles and dont hit the spikes',200,200,size=20)
Start4=Label('Reach the white box to finish and win!',200,230,size=20)
Start5=Label('Press "s" to start',200,260,size=20)

def onKeyPress(key):
#S to start
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

#On Key Press Function to move the character and restart or play again
def onKeyHold(keys):
    
    #Keys to move
    if 'left' in keys:
        Player.centerX-=5
    elif 'right' in keys:
        Player.centerX+=5
    elif 'up' in keys:
        Player.centerY-=5
    elif 'down' in keys:
        Player.centerY+=5
    
    #Stopping the player from leaving the 400x400 box
    if Player.centerY>305:
        Player.centerY=305
    if Player.centerY<25:
        Player.centerY=25
    if Player.centerX<15:
        Player.centerX=15
    if Player.centerX>380:
        Background1.visible=True
        Win.visible=True
        Again.visible=True
        
    #What to do upon hitting an obstacle
    if Player.hitsShape(Obstacle1)==True:
        if Player.centerX<80:
            Player.centerX=65
        elif Player.centerX>120:
            Player.centerX=135
    if Player.hitsShape(Obstacle2)==True:
        if Player.centerX<160:
            Player.centerX=145
        elif Player.centerX>200:
            Player.centerX=215
    if Player.hitsShape(Obstacle3)==True:
        if Player.centerX<280:
            Player.centerX=265
        elif Player.centerX>320:
            Player.centerX=335
    if Player.hitsShape(Obstacle4)==True:
        if Player.centerX<280:
            Player.centerX=265
        elif Player.centerX>320:
            Player.centerX=335
    if Player.hitsShape(Spike11)==True:
        Background1.visible=True
        Loose.visible=True
        Again.visible=True
    if Player.hitsShape(Spike22)==True:
        Background1.visible=True
        Loose.visible=True
        Again.visible=True
    if Player.hitsShape(Spike33)==True:
        Background1.visible=True
        Loose.visible=True
        Again.visible=True
    if Player.hitsShape(Spike44)==True:
        Background1.visible=True
        Loose.visible=True
        Again.visible=True

cmu_graphics.run()