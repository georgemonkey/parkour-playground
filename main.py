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

Start = Rect(0,160,60,140,fill='gold')
Obs1 = Rect(120,220,40,80,fill='yellow')
Obs2 = Rect(200,200,40,100,fill='yellow')
Obs3 = Rect(280,200,40,100,fill='yellow')
Obs4 = Rect(280,0,40,140,fill='yellow')
Finish = Rect(360,180,40,120,fill='gold')
FinishLine = Rect(360,180,40,10,fill='green')
Rect(0,320,400,80,fill='green')
Rect(0,300,400,20,fill='saddleBrown')

Player = Rect(Start.centerX, Start.top - 25, 30, 50, fill='white', border='black')

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
        Player.centerX = Start.centerX
        Player.bottom = Start.top
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

def onKeyRelease(key):
    global move_left, move_right
    if key == 'left':
        move_left = False
    elif key == 'right':
        move_right = False

def checkCollision(obs):
    global player_velocity_y, is_jumping

    if Player.bottom <= obs.top + player_velocity_y and Player.right > obs.left and Player.left < obs.right:
        if Player.bottom + player_velocity_y >= obs.top:
            Player.bottom = obs.top
            player_velocity_y = 0
            is_jumping = False
    elif Player.top >= obs.bottom and Player.right > obs.left and Player.left < obs.right:
        if Player.top + player_velocity_y <= obs.bottom:
            Player.top = obs.bottom
            player_velocity_y = 0
    elif Player.right >= obs.left and Player.left < obs.left and Player.bottom > obs.top and Player.top < obs.bottom:
        Player.right = obs.left
    elif Player.left <= obs.right and Player.right > obs.right and Player.bottom > obs.top and Player.top < obs.bottom:
        Player.left = obs.right

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

    for obs in [Start, Obs1, Obs2, Obs3, Obs4,Finish]:
        checkCollision(obs)

    if Player.top < 0:
        Player.top = 0
    if Player.bottom > 320:
        Player.bottom = 320
    if Player.left < 0:
        Player.left = 0
    if Player.right > 400:
        Player.right = 400

    if Player.hitsShape(Finish):
        Win.visible = True

cmu_graphics.run()