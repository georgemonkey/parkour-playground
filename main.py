from cmu_graphics import *
import random
import math

# ---- app setup ----
#sets game bg
app.background = rgb(244, 244, 244)
app.running = True
#sets internal clock speed
app.stepsPerSecond = 60
#custom colours
dark_gray = rgb(60, 60, 60)
medium_gray = rgb(90, 90, 90)

# ---- tuneable settings ----
gravity = 0.5 
#
jump_velocity = -10
player_velocity_y = 0
#checks for jumping to prevent double jump
is_jumping = False
#checks for lateral movement
move_left = False
move_right = False
#sets overall player speed
move_speed = 4
#sets y lower bound location of ground
ground_y = 300

# ---- static objects and ui ----
Start = Rect(0, 160, 60, 140, fill=rgb(209, 209, 209))
Finish = Rect(360, 180, 40, 120, fill=rgb(209, 209, 209))
#the gold line that counts as finishing
FinishLine = Rect(360, 180, 40, 10, fill=rgb(255, 215, 0))
#ground 
Rect(0, 320, 400, 80, fill=rgb(209, 209, 209))
Rect(0, 300, 400, 20, fill=rgb(209, 209, 209))
resetreminder = Label('press "r" to reset', 160, 350, size=18, fill=rgb(18, 18, 17))
#sets default score
score = 0
scoreboard = Label(f'score: {score}', 250, 380, size=24, bold=True)

# ---- scoring functions ----
def increaseScore(points=1):
    global score
    score += points
    #format
    scoreboard.value = f'score: {score}'

def decreaseScore(points=1):
    global score
    if score <= 0:
        score = 0
    else:
        score -= points
        #format
        scoreboard.value = f'score: {score}'

# ---- timer ----
app.timer = 15
app.step_count = 0
#previous label given to act as a signal for code to display timer label and refresh content
app.previous_label = None
app.pre_label = 0

# ---- star generation ----
star_group = Group()
#stars are generated in 20 quadrants and one star is allowed in each quadrant, this allows for 
#more consistent star generation and the spread is more even

def star_gen():
    star_group.clear()
    for offset in range(10, 400, 40):
        x = random.randrange(offset, offset + 30)
        y = random.randrange(10, 100)
        star_group.add(Star(x, y, 8, 5, fill=gradient(
            rgb(128,128,128), rgb(105,105,105), rgb(105,105,105),
            rgb(80,80,80), rgb(0,0,0), rgb(0,0,0), start='left'
        )))

# ---- tsunami drawing ----
#horizontal movement of tsunami
app.xt = 50
#creates a group for the objects of the tsunami
tsunami_group = Group()
#sets tsunami timer
app.t_timer = 0
#function for eos
def draw_tsunami(xt):
    #essentially continously erases then redraws a new wave for each time the func. is called
    #function is called on onstep area
    tsunami_group.clear()
    pre_x = app.xt
    pre_y = 0
    points = []
    for y in range(0, 405, 5):
        x = app.xt + 20 * math.sin((y - 50) / 30)
        points.extend([x, y])
        tsunami_group.add(Line(pre_x, pre_y, x, y, lineWidth=2, fill='skyBlue'))
        pre_x = x
        pre_y = y
    points.extend([0, 400, 0, 0])
    tsunami_group.add(Polygon(*points, fill='skyBlue'))

# ---- player and start labels ----
Player = Rect(Start.centerX, Start.top - 25, 30, 50, fill=rgb(233, 78, 119), border='black')
Background1 = Rect(0, 0, 400, 400, fill=rgb(244, 244, 244))
Start1 = Label('← → to move', 200, 120, size=18, fill=dark_gray)
Start2 = Label('space to jump', 200, 150, size=18, fill=dark_gray)
Start4 = Label('press "r" to reset', 200, 180, size=18, fill=dark_gray)
Start3 = Label('press "s" to start', 200, 210, size=18, fill=rgb(18, 18, 17))
Start5 = Label('reach the finish before the tsunami', 200, 250, size=14, fill=medium_gray)

# ---- level and obstacles ----
obstacles = []

def generateLevel():
    #sets obstacles to be not visible then clears all of them
    for obs in obstacles:
        obs.visible = False
    obstacles.clear()
    #sets players start position as the start blocks x,y
    Player.centerX = Start.centerX
    Player.bottom = Start.top
    #sets left lateral limit for generating objects
    x = 100
    #when the x coord. is less than the finishing block it will generate between 3-4
    #game obstacles
    while x < 320:
        height = random.randrange(40, 100)
        y = ground_y - height
        obs = Rect(x, y, 40, height, fill=rgb(58, 58, 58))
        obstacles.append(obs)
        x += random.randrange(50, 90)
    #places the finishing block and ensures finish line and finish block r visible
    Finish.left = 360
    Finish.top = 180
    FinishLine.left = 360
    FinishLine.top = 180
    Finish.visible = True
    FinishLine.visible = True


# ---- collision detection ----
def checkCollision(obs):
    global player_velocity_y, is_jumping

    if (Player.bottom <= obs.top + player_velocity_y and Player.right > obs.left and Player.left < obs.right and Player.bottom + player_velocity_y >= obs.top):
        Player.bottom = obs.top
        player_velocity_y = 0
        is_jumping = False
    elif (Player.top >= obs.bottom and Player.right > obs.left and Player.left < obs.right and Player.top + player_velocity_y <= obs.bottom):
        Player.top = obs.bottom
        player_velocity_y = 0
    elif (Player.right >= obs.left and Player.left < obs.left and Player.bottom > obs.top and Player.top < obs.bottom):
        Player.right = obs.left
    elif (Player.left <= obs.right and Player.right > obs.right and Player.bottom > obs.top and Player.top < obs.bottom):
        Player.left = obs.right

# ---- play again screen ----
Again_Group = Group()

def Play_Again():
    Again_Group.clear()
    Again_Group.add(Rect(0, 0, 400, 400, fill='white'))
    Again_Group.add(Label('press "p" to play again', 200, 150, size=25, fill=dark_gray))
    Again_Group.add(Label('your score is: ' + str(score), 200, 250, size=25, fill=dark_gray))
    obstacles.clear()
    Player.visible=False
    Finish.visible=False
    FinishLine.visible=False
    app.running = False

# ---- game step function ----
def onStep():
    if app.running:
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
            app.t_timer = 0
            tsunami_group.clear()
            star_gen()
            app.xt = 50
            increaseScore()
            generateLevel()

        app.step_count += 1
        if app.step_count == 60:
            app.t_timer += 1
            if app.timer == 0:
                Play_Again()
            if app.previous_label:
                app.previous_label.visible = False
            if app.pre_label == 1:
                app.previous_label = Label(app.timer, 370, 380, size=25)
            if app.timer != 0:
                app.timer -= 1
                app.step_count = 0

        if app.t_timer >= 2:
            draw_tsunami(app.xt)
            app.xt += 1

        if tsunami_group.containsShape(Player):
            app.t_timer = 0
            tsunami_group.clear()
            star_gen()
            app.xt = 50
            decreaseScore()
            generateLevel()

# ---- key press controls ----
def onKeyPress(key):
    global player_velocity_y, is_jumping, move_left, move_right, score

    if key in ['s', 'p', 'r']:
        #when one of the reset keys is pressed the game is reset n regenerated
        Start1.visible = False
        Start2.visible = False
        Start3.visible = False
        Start4.visible = False
        Start5.visible = False
        Background1.visible = False
        Again_Group.clear()
        app.t_timer = 0
        tsunami_group.clear()
        decreaseScore()
        generateLevel()
        star_gen()
        app.running = True
        app.timer = 15
        score = 0
        scoreboard.value = f'score: {score}'
        app.running=True
        app.pre_label=1
        Player.visible=True
        Finish.visible=True
        FinishLine.visible=True

    if key == 'space' and not is_jumping:
        player_velocity_y = jump_velocity
        is_jumping = True
    elif key == 'left':
        move_left = True
    elif key == 'right':
        move_right = True

# ---- key release controls ----
def onKeyRelease(key):
    #sets player to stop moving when corresponding key is let go of
    global move_left, move_right
    if key == 'left':
        move_left = False
    elif key == 'right':
        move_right = False

#runs game
cmu_graphics.run()