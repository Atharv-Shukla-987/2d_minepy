from ursina import *


app = Ursina()

created_chucks = []
Player = Entity(
    model="quad",
    texture='tex/up.png', 
    scale=(0.5,1),
    collider="box"
)

camera.add_script(SmoothFollow(target=Player,offset=(0,0,-20),speed=4))

def stone(x,y):
 pos = (x,y)
 Entity(
    model="quad",
    color=color.white,
    collider="box",
    position=pos,
    scale=(1/3,1/3),
    texture= 'tex/stone.jpg'
)

def chuck(x,y):
    for _x in range(6):
        __x = x + _x*(1/3)
        for _y in range(6):
            __y = y + _y*(1/3)
            stone(__x,__y)
            created_chucks.append((__x,__y))


chuck(1,1)

def input(key):
    move = 5*time.dt
    if held_keys["w"]:
        Player.y += move
        Player.texture = 'tex/up.png'
    if held_keys["s"]:
        Player.y -= move
        Player.texture = 'tex/down.png'
    if held_keys["d"]:
        Player.x += move
        Player.texture = 'tex/right.png'
    if held_keys["a"]:
        Player.x -= move
        Player.texture = 'tex/left.png'

def update():
    if Player.intersects():
        Player.x -= 0.05
        Player.y -=0.05
app.run()