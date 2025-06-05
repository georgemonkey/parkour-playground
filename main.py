from cmu_graphics import *

app.background = gradient(rgb(255,69,0),rgb(255,90,0),rgb(255,110,0),rgb(255,130,0),rgb(255,140,0),start='left')
app.stepsPerSecond = 60
#GRAVITY
gravity = 0.5
jump_velocity = -10
player_velocity_y = 0
is_jumping = False
move_left = False
move_right = False
move_speed = 4
ground_y = 300
#GRID
def drawGrid(spacing=50, color='lightGray'):
    for x in range(0, app.width, spacing):
        Line(x, 0, x, app.height, fill=color)
    for y in range(0, app.height, spacing):
        Line(0, y, app.width, y, fill=color)
drawGrid()

Rect(0,160,60,140,fill='gold')
Rect(120,220,40,80,fill='yellow')
Rect(200,200,40,100,fill='yellow')
Rect(280,200,40,100,fill='yellow')
Rect(280,0,40,140,fill='yellow')
Rect(360,180,40,120,fill='gold')
Rect(0,320,400,80,fill='green')
Rect(0,300,400,20,fill='saddleBrown')

Player = Rect(15, 110, 30, 50, fill='white', border='black')

def onKeyPress(key):
    global player_velocity_y, is_jumping, move_left, move_right
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

cmu_graphics.run()