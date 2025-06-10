from cmu_graphics import *
import random

app.background = rgb(244, 244, 244)
app.stepsPerSecond = 60
dark_gray = rgb(60, 60, 60)      
medium_gray = rgb(90, 90, 90)     
wins = 0

#tuneable settings
gravity = 0.5 
jump_velocity = -10
player_velocity_y = 0
is_jumping = False
move_left = False
move_right = False
move_speed = 4
ground_y = 300

# static objects
Start = Rect(0,160,60,140,fill=rgb(209, 209, 209))
Finish = Rect(360,180,40,120,fill=rgb(209, 209, 209))
FinishLine = Rect(360,180,40,10,fill=rgb(255, 215, 0))
Rect(0,320,400,80,fill=rgb(209, 209, 209))
Rect(0,300,400,20,fill=rgb(209, 209, 209))
resetreminder = Label('press "r" to reset', 200, 350, size=18, fill=rgb(18, 18, 17))
score = 1

scoreboard = Label(f'score: {score}', 340, 30, size=24, fill=rgb(255, 105, 180), bold=True)
#ensures default increasion is 1 n not 0 
def increaseScore(points=1):
    global score
    score += points
    scoreboard.value = f'score: {score}'
def decreaseScore(points=1):
    global score
    score -= points
    scoreboard.value = f'score: {score}'
time = 30000
timer =  Label(f'time {time}', 60, 30, size=24, fill=rgb(255, 105, 180), bold=True)

# stars generation
for i in range(10,20):
    x = (random.randrange(10,270)+15)
    y = random.randrange(10,100)
    Star(x,y,5,5)

Player = Rect(Start.centerX, Start.top - 25, 30, 50, fill=rgb(233, 78, 119), border='black')
#game objects
Background1 = Rect(0, 0, 400, 400, fill=rgb(244, 244, 244))
Start1 = Label('← → to move', 200, 120, size=18, fill=dark_gray)
Start2 = Label('space to jump', 200, 150, size=18, fill=dark_gray)
Start4 = Label('press "r" to reset', 200, 180, size=18, fill=dark_gray)
Start3 = Label('press "s" to start', 200, 210, size=18, fill=rgb(18, 18, 17))
Start5 = Label('reach the finish before the tsunami', 200, 250, size=14, fill=medium_gray)
#es
Win = Label('you win', 200, 125, size=45, fill=rgb(40, 160, 80), visible=False)
Loose = Label('you lose', 200, 125, size=45, fill=rgb(180, 50, 50), visible=False)
Again = Label('press "p" to play again', 200, 170, size=18, fill=dark_gray, visible=False)
#using 2d list from mr browns entry task!!!
obstacles = []
#level generation
def generateLevel():
    
    for obs in obstacles:
        obs.visible = False
    obstacles.clear()

    
    Player.centerX = Start.centerX
    Player.bottom = Start.top

    
    x = 100
    while x < 320:
        #random heigh gen
        height = random.randrange(40, 100)
        y = ground_y - height
        obs = Rect(x, y, 40, height, fill=rgb(58, 58, 58))
        obstacles.append(obs)
        x += random.randrange(50, 90)

    
    Finish.left = 360
    Finish.top = 180
    FinishLine.left = 360
    FinishLine.top = 180
    Finish.visible = True
    FinishLine.visible = True
#collsion check
def checkCollision(obs):
    global player_velocity_y, is_jumping

    if (Player.bottom <= obs.top + player_velocity_y and
        Player.right > obs.left and Player.left < obs.right and
        Player.bottom + player_velocity_y >= obs.top):
        
        Player.bottom = obs.top
        player_velocity_y = 0
        is_jumping = False
    elif (Player.top >= obs.bottom and Player.right > obs.left and Player.left < obs.right and
          Player.top + player_velocity_y <= obs.bottom):
        Player.top = obs.bottom
        player_velocity_y = 0
    elif (Player.right >= obs.left and Player.left < obs.left and
          Player.bottom > obs.top and Player.top < obs.bottom):
        Player.right = obs.left
    elif (Player.left <= obs.right and Player.right > obs.right and
          Player.bottom > obs.top and Player.top < obs.bottom):
        Player.left = obs.right

def onStep():
    global time
    time -=1
    timer.value = time
    global player_velocity_y, is_jumping

    player_velocity_y += gravity
    Player.centerY += player_velocity_y

    if move_left:
        Player.centerX -= move_speed
    if move_right:
        Player.centerX += move_speed

    if Player.bottom >= ground_y:
        Player.bottom = ground_y
        player_velocity_y = 0
        is_jumping = False

    for obs in obstacles:
        checkCollision(obs)

    if Player.top < 0:
        Player.top = 0
    if Player.bottom > 320:
        Player.bottom = 320
        is_jumping = False
        player_velocity_y = 0
    if Player.left < 0:
        Player.left = 0
    if Player.right > 400:
        Player.right = 400

    if Player.hitsShape(FinishLine):
        increaseScore()
        generateLevel()

def onKeyPress(key):
    global player_velocity_y, is_jumping, move_left, move_right

    if key in ['s', 'p','r']:
        Start1.visible = False
        Start2.visible = False
        Start3.visible = False
        Start4.visible = False
        Start5.visible = False
        Background1.visible = False
        Win.visible = False
        Loose.visible = False
        Again.visible = False
        decreaseScore()
        generateLevel()

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

cmu_graphics.run()