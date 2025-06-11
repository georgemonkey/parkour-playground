from cmu_graphics import *
import random
import math


app.background = rgb(244, 244, 244)
app.running=True
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
resetreminder = Label('press "r" to reset', 160, 350, size=18, fill=rgb(18, 18, 17))
score = 1

scoreboard = Label(f'score: {score}', 250, 380, size=24, bold=True)
#ensures default increasion is 1 n not 0 
def increaseScore(points=1):
    global score
    score += points
    scoreboard.value = f'score: {score}'
def decreaseScore(points=1):
    global score
    if score<=0:
        score=0
    else:
        score -= points
        scoreboard.value = f'score: {score}'
  
#Timer
app.timer=15
app.step_count=0
app.previous_label=None
app.pre_label=0

# stars generation
star_group=Group()
def star_gen():
    star_group.clear()
    for i in range(1,2):
        x = (random.randrange(10,40))
        y = random.randrange(10,100)
        star_group.add(Star(x,y,8,5,fill=gradient(rgb(128,128,128),rgb(105,105,105),rgb(105,105,105),rgb(80,80,80),rgb(0,0,0),rgb(0,0,0),start='left')))
    for i in range(1,2):
        x = (random.randrange(50,80))
        y = random.randrange(10,100)
        star_group.add(Star(x,y,8,5,fill=gradient(rgb(128,128,128),rgb(105,105,105),rgb(105,105,105),rgb(80,80,80),rgb(0,0,0),rgb(0,0,0),start='left')))
    for i in range(1,2):
        x = (random.randrange(90,120))
        y = random.randrange(10,100)
        star_group.add(Star(x,y,8,5,fill=gradient(rgb(128,128,128),rgb(105,105,105),rgb(105,105,105),rgb(80,80,80),rgb(0,0,0),rgb(0,0,0),start='left')))
    for i in range(1,2):
        x = (random.randrange(130,160))
        y = random.randrange(10,100)
        star_group.add(Star(x,y,8,5,fill=gradient(rgb(128,128,128),rgb(105,105,105),rgb(105,105,105),rgb(80,80,80),rgb(0,0,0),rgb(0,0,0),start='left')))
    for i in range(1,2):
        x = (random.randrange(170,200))
        y = random.randrange(10,100)
        star_group.add(Star(x,y,8,5,fill=gradient(rgb(128,128,128),rgb(105,105,105),rgb(105,105,105),rgb(80,80,80),rgb(0,0,0),rgb(0,0,0),start='left')))
    for i in range(1,2):
        x = (random.randrange(210,240))
        y = random.randrange(10,100)
        star_group.add(Star(x,y,8,5,fill=gradient(rgb(128,128,128),rgb(105,105,105),rgb(105,105,105),rgb(80,80,80),rgb(0,0,0),rgb(0,0,0),start='left')))
    for i in range(1,2):
        x = (random.randrange(250,280))
        y = random.randrange(10,100)
        star_group.add(Star(x,y,8,5,fill=gradient(rgb(128,128,128),rgb(105,105,105),rgb(105,105,105),rgb(80,80,80),rgb(0,0,0),rgb(0,0,0),start='left')))
    for i in range(1,2):
        x = (random.randrange(290,320))
        y = random.randrange(10,100)
        star_group.add(Star(x,y,8,5,fill=gradient(rgb(128,128,128),rgb(105,105,105),rgb(105,105,105),rgb(80,80,80),rgb(0,0,0),rgb(0,0,0),start='left')))
    for i in range(1,2):
        x = (random.randrange(330,360))
        y = random.randrange(10,100)
        star_group.add(Star(x,y,8,5,fill=gradient(rgb(128,128,128),rgb(105,105,105),rgb(105,105,105),rgb(80,80,80),rgb(0,0,0),rgb(0,0,0),start='left')))
    for i in range(1,2):
        x = (random.randrange(370,390))
        y = random.randrange(10,100)
        star_group.add(Star(x,y,8,5,fill=gradient(rgb(128,128,128),rgb(105,105,105),rgb(105,105,105),rgb(80,80,80),rgb(0,0,0),rgb(0,0,0),start='left')))

#Tsunami
app.xt=50
tsunami_group=Group()
app.t_timer=0
def draw_tsunami(xt):
    tsunami_group.clear()
    pre_x=app.xt
    pre_y=0
    points=[]
    for y in range(0,405,5):
        x=app.xt+20*math.sin((y-50)/30)
        points.extend([x,y])
        tsunami_group.add(Line(pre_x,pre_y,x,y,lineWidth=2,fill='skyBlue'))
        pre_x=x
        pre_y=y
    points.extend([0, 400, 0, 0])
    tsunami_group.add(Polygon(*points,fill='skyBlue'))

Player = Rect(Start.centerX, Start.top - 25, 30, 50, fill=rgb(233, 78, 119), border='black')
#game objects
Background1 = Rect(0, 0, 400, 400, fill=rgb(244, 244, 244))
Start1 = Label('← → to move', 200, 120, size=18, fill=dark_gray)
Start2 = Label('space to jump', 200, 150, size=18, fill=dark_gray)
Start4 = Label('press "r" to reset', 200, 180, size=18, fill=dark_gray)
Start3 = Label('press "s" to start', 200, 210, size=18, fill=rgb(18, 18, 17))
Start5 = Label('reach the finish before the tsunami', 200, 250, size=14, fill=medium_gray)
#Game ending
Blank=Rect(0,0,400,400,fill='white',visible=False)
Again = Label('press "p" to play again', 200, 150, size=25, fill=dark_gray, visible=False)
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
    if app.running==True:
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
    ###ADD COLLSIONS HERE
        for obs in obstacles:
            checkCollision(obs)
            checkCollision(Start)
            checkCollision(Finish)
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
            app.t_timer=0
            tsunami_group.clear()
            star_gen()
            app.xt=50
            increaseScore()
            generateLevel()
        
    #Increasing timer
        app.step_count+=1
        if app.step_count==60:
            app.t_timer+=1
            if app.timer==0:
                Again.visible=True
                Label('Your score is' + str(score),200,250,size=25,fill=dark_gray,visible=False)
                Blank.visible=True
                app.running=False
            if app.previous_label:
                app.previous_label.visible=False
            if app.pre_label==1:
                app.previous_label=Label(app.timer,370,380,size = 25)
            if app.timer!=0:
                app.timer-=1
                app.step_count=0              

    #Drawing the tsunami
        if app.t_timer>=2:
            draw_tsunami(app.xt)
            app.xt+=1

    #Player losing upon hitting tsuanmi
        if tsunami_group.containsShape(Player):
            app.t_timer=0
            tsunami_group.clear()
            star_gen()
            app.xt=50
            decreaseScore()
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
        Again.visible = False
        app.t_timer=0
        tsunami_group.clear()
        decreaseScore()
        generateLevel()
        app.pre_label=1
        star_gen()
        app.running=True
        app.timer=15
        Blank.visible=False
        global score
        score=0
        
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
