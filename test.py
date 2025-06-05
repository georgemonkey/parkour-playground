from cmu_graphics import *


app.background = gradient(rgb(255,69,0),rgb(255,90,0),rgb(255,110,0),rgb(255,130,0),rgb(255,140,0),start='left')
app.stepsPerSecond = 60

# physics variables
gravity = 0.5
jump_velocity = -10
player_velocity_y = 0
is_jumping = False


ground_y = 300


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
    global player_velocity_y, is_jumping
    if key == 'space' and not is_jumping:
        player_velocity_y = jump_velocity
        is_jumping = True
    elif key == 'left':
        Player.centerX -= 5
    elif key == 'right':
        Player.centerX += 5

def onStep():
    global player_velocity_y, is_jumping

  
    player_velocity_y += gravity
    Player.centerY += player_velocity_y

    #landing
    if Player.bottom >= ground_y:
        Player.bottom = ground_y
        player_velocity_y = 0
        is_jumping = False

cmu_graphics.run()