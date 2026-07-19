from ursina import *
import random

app = Ursina()

blocks = {}
created_chucks = set()
removed = []
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
foot_offset= (Player.scale_y - 1)/2
def tar_blk_pos():
   return round(Player.x + facing[0]),round(Player.y + facing[1])

def chuck(x,y):
    if (x,y) in created_chucks:
       return
    created_chucks.add((x,y))
    for _x in range(6):
        __x = round(x + _x)
        for _y in range(6):
            __y = round(y + _y)
            if (__x,__y) in spawn_point:
                continue
            if (__x,__y) in removed:
               continue
            
            if (__x,__y) not in blocks:
               e = random.choices(blks,weights=p,k=1)[0](__x,__y)
               e.grid_pos = (__x,__y)
               blocks[(__x,__y)] = e  
                


spawn_point =[(0,0),(1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]

def can_move(dir,move):
   buffer = 0.1
   half_h = Player.scale_y / 2 - 0.05
   half_w = Player.scale_x /2 - 0.05
   if dir.x != 0:
      dist = Player.scale_x / 2 + move + buffer
      offsets = [Vec3(0,-half_h,0),Vec3(0,half_h,0)]
   else:
      dist = Player.scale_x / 2 + move + buffer
      offsets = [Vec3(-half_w,0,0),Vec3(half_w,0,0)]
   
   for off in offsets:
      origin = Player.world_position + off
      hit_info = raycast(origin,dir,distance=dist,ignore=(Player,),debug=False)
      if hit_info.hit :
         return False
      return True
   
def unload():
   pxch = (int(Player.x)//6)*6
   pych = (int(Player.y)//6)*6
   for chpos in list(created_chucks):
      cx,cy = chpos
      dist = ((cx-pxch)**2 + (cy - pych)**2)**0.5
      if dist >  24 :
         for x_ in range(6):
            for y_ in range(6):
               key = (cx+x_,cy+y_)
               if key in blocks:
                  destroy(blocks[key])
                  del blocks[key]
         
         created_chucks.discard(chpos)
def update():
   px = int(Player.x)
   py = int(Player.y)
   pych = (py//6)*6
   pxch = (px//6)*6
   for x in range(pxch-12,pxch+18,6):
      for y in range(pych-12,pych+18,6):
         chuck(x,y)
   unload()

   

def input(key):
    global facing
    move = 5*time.dt
    check = move + 0.25
    if held_keys["w"]:
        if can_move(Vec3(0,1,0),move):
           Player.y += move
        Player.texture = 'tex/up.png'
        facing = (0,1)
    if held_keys["s"]:
        if can_move(Vec3(0,-1,0),move):
           Player.y -= move
        Player.texture = 'tex/down.png'
        facing = (0,-1)
    if held_keys["d"]:
        if can_move(Vec3(1,0,0),move):
           Player.x += move
        Player.texture = 'tex/right.png'
        facing = (1,0)
    if held_keys["a"]:
        if can_move(Vec3(-1,0,0), move):
           Player.x -= move
        Player.texture = 'tex/left.png'
        facing = (-1,0)
    if key == "left mouse down":
       hit = mouse.hovered_entity
       if hit and hasattr(hit,"grid_pos"):
          hx , hy = hit.grid_pos
          dist = ((hx-Player.x)**2 + (hy - Player.y)**2)**0.5
          if dist <= 1.5:
             destroy(hit)
             del blocks[(hx,hy)]
             removed.append((hx,hy))
   

    



app.run()