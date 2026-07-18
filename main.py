from ursina import *
import random

app = Ursina()

created_blk = []
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
 
def adersite(x,y):
 pos = (x,y)
 Entity(
    model="quad",
    color=color.white,
    collider="box",
    position=pos,
    scale=(1/3,1/3),
    texture= 'tex/andesite.png'
)
 
def granite(x,y):
 pos = (x,y)
 Entity(
    model="quad",
    color=color.white,
    collider="box",
    position=pos,
    scale=(1/3,1/3),
    texture= 'tex/granite.jpg'
)
 
def coal(x,y):
 pos = (x,y)
 Entity(
    model="quad",
    color=color.white,
    collider="box",
    position=pos,
    scale=(1/3,1/3),
    texture= 'tex/coal_ore.png'
)
 
def copper(x,y):
 pos = (x,y)
 Entity(
    model="quad",
    color=color.white,
    collider="box",
    position=pos,
    scale=(1/3,1/3),
    texture= 'tex/copper_ore.jpg'
)
 
def emerald(x,y):
 pos = (x,y)
 Entity(
    model="quad",
    color=color.white,
    collider="box",
    position=pos,
    scale=(1/3,1/3),
    texture= 'tex\emerald_ore.jpg'
)
 
def gold(x,y):
 pos = (x,y)
 Entity(
    model="quad",
    color=color.white,
    collider="box",
    position=pos,
    scale=(1/3,1/3),
    texture= 'tex/gold_ore.jpg'
)
 
def iron(x,y):
 pos = (x,y)
 Entity(
    model="quad",
    color=color.white,
    collider="box",
    position=pos,
    scale=(1/3,1/3),
    texture= 'tex/iron_ore.png'
)
 
def redstone(x,y):
   pos = (x,y)
   Entity(
      model="quad",
      color=color.color
      ,collider="box",
      position=pos,
      scale=(1/3,1/3),
      texture='tex/redstone_ore.jpg'

   )

blks = [stone,
        adersite,
        granite,
        coal,
        copper,
        iron,
        redstone,
        gold,
        emerald]
p = [60,
     10,
     10,
     8,
     5,
     4,
     1.5,
     1,
     0.5]

def chuck(x,y):
    for _x in range(6):
        __x = x + _x*(1/3)
        for _y in range(6):
            __y = y + _y*(1/3)
            random.choices(blks,weights=p,k=1)[0](__x,__y)
            created_blk.append((__x,__y))


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