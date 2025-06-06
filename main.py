from cmu_graphics import *

app.background = gradient(rgb(255,69,0),rgb(255,90,0),rgb(255,110,0),rgb(255,130,0),rgb(255,140,0),start='left')
app.stepsPerSecond = 60

gravity = 0.5
jump_velocity = -10
player_velocity_y = 0
is_jumping = False
move_left = False
move_right = False
move_speed = 4
ground_y = 300

def drawGrid(spacing=50, color='lightGray'):
    for x in range(0, app.width, spacing):
        Line(x, 0, x, app.height, fill=color)
    for y in range(0, app.height, spacing):
        Line(0, y, app.width, y, fill=color)
drawGrid()



Start = Rect(0,160,60,140,fill='gold')
Obs1=Rect(120,220,40,80,fill='yellow')
Obs2=Rect(200,200,40,100,fill='yellow')
Obs3=Rect(280,200,40,100,fill='yellow')
Obs4=Rect(280,0,40,140,fill='yellow')
Finish = Rect(360,180,40,120,fill='gold')
Rect(0,320,400,80,fill='green')
Rect(0,300,400,20,fill='saddleBrown')

Player = Rect(15,110,30,50,fill='white',border='black')

Background1 = Rect(0,0,400,400,fill=gradient('yellow','orange','darkOrange',start='top'))
Win = Label('You Win!',200,200,size=50,visible=False)
Loose = Label('You Lose',200,200,size=40,visible=False)
Again = Label('Press "p" to play again',200,250,size=25,visible=False)

Start1 = Label('Use arrow keys and spacebar to move',200,140,size=15)
Start2 = Label('Press "r" to reset',200,170,size=20)
Start3 = Label('Do the parkour and run from the tsunami',200,200,size=20)
Start4 = Label('Reach the finish line to finish the level, complete 3 levels to win',200,230,size=13)
Start5 = Label('Press "s" to start',200,260,size=20)

def onKeyPress(key):
    global player_velocity_y, is_jumping, move_left, move_right

    if key in ['s', 'r', 'p']:
        Start1.visible = False
        Start2.visible = False
        Start3.visible = False
        Start4.visible = False
        Start5.visible = False
        Background1.visible = False
        Player.centerX = 35
        Player.centerY = 305
        Win.visible = False
        Loose.visible = False
        Again.visible = False
        Background1.visible = False

    if key == 'space' and not is_jumping:
        player_velocity_y = jump_velocity
        is_jumping = True
    elif key == 'left':
        move_left = True
    elif key == 'right':
        move_right = True
    
    if Player.hitsShape(Obs1):
        if Player.centerX>105 and Player.centerX<175:
            Player.centerY=245
    

def onKeyRelease(key):
    global move_left, move_right
    if key == 'left':
        move_left = False
    elif key == 'right':
        move_right = False

def onStep():
    global player_velocity_y, is_jumping

    if move_left:
        Player.centerX -= move_speed
    if move_right:
        Player.centerX += move_speed

    player_velocity_y += gravity
    Player.centerY += player_velocity_y

    if Player.bottom >= ground_y:
        Player.bottom = ground_y
        player_velocity_y = 0
        is_jumping = False

    if Player.hitsShape(Finish):
        Win.visible = True
    
    if Player.bottom>300:
       Player.centerY=325
    if Player.top<0:
        Player.centerY=25
    if Player.right>400:
        Player.centerX=385
    if Player.left<0:
        Player.centerX=15
    
    if Player.hitsShape(Obs1):
        if Player.centerX<120:
            Player.centerX=105
        elif Player.centerX>160:
            Player.centerX=175 

    if Player.hitsShape(Obs2):
        if Player.centerX<200:
            Player.centerX=185
        elif Player.centerX>240:
            Player.centerX=255  
    
    if Player.hitsShape(Obs3):
        if Player.centerX<280:
            Player.centerX=265
        elif Player.centerX>320:
            Player.centerX=335
cmu_graphics.run()