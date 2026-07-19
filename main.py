from ursina import *
import random

app = Ursina()

blocks = {}
Player = Entity(
    model="quad",
    texture='tex/up.png', 
    scale=(1,2),
    collider="box",
    position=(0,0)
)

camera.orthographic_scale = 15 
camera.add_script(SmoothFollow(target=Player,offset=(0,0,-20),speed=4))

def stone(x,y):
 pos = (x,y)
 e = Entity(
    model="quad",
    color=color.white,
    collider="box",
    position=pos,
    scale=(1,1),
    texture= 'tex/stone.jpg'
)
 return e
 
def adersite(x,y):
 pos = (x,y)
 e = Entity(
    model="quad",
    color=color.white,
    collider="box",
    position=pos,
    scale=(1,1),
    texture= 'tex/andesite.png'
)
 return e
 
def granite(x,y):
 pos = (x,y)
 e = Entity(
    model="quad",
    color=color.white,
    collider="box",
    position=pos,
    scale=(1,1),
    texture= 'tex/granite.jpg'
)
 return e
 
def coal(x,y):
 pos = (x,y)
 e = Entity(
    model="quad",
    color=color.white,
    collider="box",
    position=pos,
    scale=(1,1),
    texture= 'tex/coal_ore.png'
)
 return e
 
def copper(x,y):
 pos = (x,y)
 e = Entity(
    model="quad",
    color=color.white,
    collider="box",
    position=pos,
    scale=(1,1),
    texture= 'tex/copper_ore.jpg'
)
 return e
 
def emerald(x,y):
 pos = (x,y)
 e = Entity(
    model="quad",
    color=color.white,
    collider="box",
    position=pos,
    scale=(1,1),
    texture= 'tex/emerald_ore.jpg'
)
 return e
def gold(x,y):
 pos = (x,y)
 e = Entity(
    model="quad",
    color=color.white,
    collider="box",
    position=pos,
    scale=(1,1),
    texture= 'tex/gold_ore.jpg'
)
 return e
 
def iron(x,y):
 pos = (x,y)
 e = Entity(
    model="quad",
    color=color.white,
    collider="box",
    position=pos,
    scale=(1,1),
    texture= 'tex/iron_ore.png'
)
 return e
def redstone(x,y):
   pos = (x,y)
   e = Entity(
      model="quad"
      ,collider="box",
      position=pos,
      scale=(1,1),
      texture='tex/redstone_ore.jpg'

   )
   return e

blks = [stone,
        adersite,
        granite,
        coal,
        copper,
        iron,
        redstone,
        gold,
        emerald]
p = [70,
     10,
     8.99,
     4,
     3,
     2,
     1.5,
     0.5,
     0.01]

facing = (0,1)
def snap_to_grid(v):
   return round(round(v/(1/3))*(1/3),4)

def tar_blk_pos():
   return snap_to_grid(Player.x + facing[0]*(1/3)),snap_to_grid(Player.y + facing[1]*(1/3))
def chuck(x,y):
    for _x in range(6):
        __x = round(x + _x)
        for _y in range(6):
            __y = round(y + _y)
            if (__x,__y) in spawn_point:
                continue
            if (__x,__y) not in blocks:
               blocks[(__x,__y)] = random.choices(blks,weights=p,k=1)[0](__x,__y)
                


spawn_point =[(0,0),(1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]

def can_move(dir,dis):
   hit_info = raycast(Player.world_position,dir,distance=dis,ignore=(Player,) ,debug=False)
   return not hit_info.hit

def update():
   px = int(Player.x)
   py = int(Player.y)
   for x in range(px-7,px +8):
      for y in range(py-5,py+6):
         if (x,y) not in spawn_point :
          if x%2 and y%2 :
                chuck(x,y)
   

def input(key):
    global facing
    move = 5*time.dt
    check = move + 0.25
    if held_keys["w"]:
        if can_move(Vec3(0,1,0),check):
           Player.y += move
        Player.texture = 'tex/up.png'
        facing = (0,1)
    if held_keys["s"]:
        if can_move(Vec3(0,-1,0),check):
           Player.y -= move
        Player.texture = 'tex/down.png'
        facing = (0,-1)
    if held_keys["d"]:
        if can_move(Vec3(1,0,0),check):
           Player.x += move
        Player.texture = 'tex/right.png'
        facing = (1,0)
    if held_keys["a"]:
        if can_move(Vec3(-1,0,0), check):
           Player.x -= move
        Player.texture = 'tex/left.png'
        facing = (-1,0)
    if key == "e":
       tx , ty = tar_blk_pos()
       if (tx,ty) in blocks:
          destroy(blocks[(tx,ty)])
          del blocks[(tx,ty)]
     
    if key == "f":
       tx ,ty = tar_blk_pos()
       if (tx,ty) not in blocks:
          e = stone(tx,ty)
          blocks[(tx,ty)] = e



app.run()