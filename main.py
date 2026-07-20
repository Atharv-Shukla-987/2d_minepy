from ursina import *
import random

app = Ursina()

blocks = {}
created_chucks = set()
removed = []
inventory = {}
blk_in_inven = []
selblk = 0
surface = -2
facing = (0,1)
velo_y = 0
g = 20
jump = 8

blk_tex = {
   'grass': {'tex' : 'tex/grass.png','slt' : 'tex/hgrass.png'},
   'stone' : {'tex': 'tex/stone.jpg', 'slt' : 'tex/hstone.png'},
   'dirt' : {'tex' : 'tex/dirt.png' , 'slt': 'tex/hdirt.png'},
   'andesite' : {'tex':'tex/andesite.png', 'slt' : 'tex/handesite.png'},
   'granite' : {'tex':'tex/granite.jpg', 'slt':'tex/hgranite.png'},
   'coal' : {'tex':'tex/coal_ore.png','slt':'tex/hcoal_ore.png'},
   'copper' : {'tex': 'tex/copper_ore.jpg','slt':'tex/hcopper_ore.png'},
   'redstone':{'tex': 'tex/redstone_ore.jpg','slt':'tex/hredstone_ore.png'},
   'iron':{'tex':'tex/iron_ore.png','slt':'tex/hiron_ore.png'},
   'gold': {'tex':'tex/gold_ore.jpg','slt':'tex/hgold_ore.png'},
   'emerald':{'tex':'tex/emerald_ore.jpg','slt':'tex/hemerald_ore.png'}
}

Player = Entity(
    model="quad",
    color=color.red, 
    scale=(1,2),
    collider="box",
    position=(0,2)
)

foot_offset= (Player.scale_y - 1)/2

sky = Sky()
sky.color = color.azure
camera.orthographic_scale = 15 
camera.add_script(SmoothFollow(target=Player,offset=(0,0,-20),speed=4))

def grass(x,y):
   pos = (x,y)
   e = Entity(
      model="quad",
      collider="box",
      position=pos,
      scale=(1,1),
      texture=blk_tex['grass']['tex']
   )
   return e

def dirt(x,y):
   pos = (x,y)
   e = Entity(
      model="quad",
      collider="box",
      position=pos,
      scale=(1,1),
      texture=blk_tex['dirt']['tex']
   )
   return e 

def stone(x,y):
 pos = (x,y)
 e = Entity(
    model="quad",
    color=color.white,
    collider="box",
    position=pos,
    scale=(1,1),
    texture= blk_tex['stone']['tex']
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
    texture= blk_tex['adersite']['tex']
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
    texture= blk_tex['granite']['tex']
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
    texture= blk_tex['coal']['tex']
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
    texture= blk_tex['copper']['tex']
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
    texture= blk_tex['emerald']['tex']
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
    texture= blk_tex['gold']['tex']
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
    texture= blk_tex['iron']['tex']
)
 return e
def redstone(x,y):
   pos = (x,y)
   e = Entity(
      model="quad"
      ,collider="box",
      position=pos,
      scale=(1,1),
      texture=blk_tex['redstone']['tex']

   )
   return e

slotbg1 = Entity(
   parent=camera.ui,
   model='quad',
   color=color.gray,
   position=(-0.225,0.45,0.1),
   scale=0.05
)
slot2bg = Entity(
    parent = camera.ui,
    model = 'quad',
    color=color.gray,
    position=(-0.175, 0.45,0.1),
    scale=0.05
)
slot3bg = Entity(
    parent = camera.ui,
    model = 'quad',
    color=color.gray,
    position=(-0.125, 0.45,0.1),
    scale=0.05
)
slot4bg = Entity(
    parent = camera.ui,
    model = 'quad',
    color=color.gray,
    position=(-0.075, 0.45,0.1),
    scale=0.05
)
slot5bg = Entity(
    parent = camera.ui,
    model = 'quad',
    color=color.gray,
    position=(-0.025, 0.45,0.1),
    scale=0.05
)
slot6bg = Entity(
    parent = camera.ui,
    model = 'quad',
    color=color.gray,
    position=(0.025, 0.45,0.1),
    scale=0.05
)
slot7bg = Entity(
    parent = camera.ui,
    model = 'quad',
    color=color.gray,
    position=(0.075, 0.45,0.1),
    scale=0.05
)
slot8bg = Entity(
    parent = camera.ui,
    model = 'quad',
    color=color.gray,
    position=(0.125, 0.45,0.1),
    scale=0.05
)
slot9bg = Entity(
    parent = camera.ui,
    model = 'quad',
    color=color.gray,
    position=(0.175, 0.45,0.1),
    scale=0.05
)
slot10bg = Entity(
    parent = camera.ui,
    model = 'quad',
    color=color.gray,
    position=(0.225, 0.45,0.1),
    scale=0.05
)

slot1 = Entity(
   parent=camera.ui,
   model='quad',
   color=color.white,
   position=(-0.225,0.45),
   scale=0.042
)
slot2 = Entity(
    parent = camera.ui,
    model = 'quad',
    color=color.white,
    position=(-0.175, 0.45),
    scale=0.042
)
slot3  = Entity(
    parent = camera.ui,
    model = 'quad',
    color=color.white,
    position=(-0.125, 0.45),
    scale=0.042
)
slot4 = Entity(
    parent = camera.ui,
    model = 'quad',
    color=color.white,
    position=(-0.075, 0.45),
    scale=0.042
)
slot5 = Entity(
    parent = camera.ui,
    model = 'quad',
    color=color.white,
    position=(-0.025, 0.45),
    scale=0.042
)
slot6 = Entity(
    parent = camera.ui,
    model = 'quad',
    color=color.white,
    position=(0.025, 0.45),
    scale=0.042
)
slot7 = Entity(
    parent = camera.ui,
    model = 'quad',
    color=color.white,
    position=(0.075, 0.45),
    scale=0.042
)
slot8 = Entity(
    parent = camera.ui,
    model = 'quad',
    color=color.white,
    position=(0.125, 0.45),
    scale=0.042
)
slot9 = Entity(
    parent = camera.ui,
    model = 'quad',
    color=color.white,
    position=(0.175, 0.45),
    scale=0.042
)
slot10 = Entity(
    parent = camera.ui,
    model = 'quad',
    color=color.white,
    position=(0.225, 0.45),
    scale=0.042
)

slots = [slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9,slot10]

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
            if __y > 0:
               continue
            
            if (__x,__y) in removed:
               continue
            
            if (__x,__y) not in blocks:
               if __y == surface+2 :
                  e = grass(__x,__y)
                  blocks[(__x,__y)] = e
               elif (__y == surface) or ( __y == surface+1):
                  e = dirt(__x,__y)
                  blocks[(__x,__y)] = e
               else:
                  e = random.choices(blks,weights=p,k=1)[0](__x,__y)
                  blocks[(__x,__y)] = e  
               e.grid_pos = (__x,__y)
                



def can_move(dir,move):
   buffer = 0.05
   half_h = Player.scale_y / 2 - 0.05
   half_w = Player.scale_x /2 - 0.05
   if dir.x != 0:
      dist = Player.scale_x / 2 + move + buffer
      offsets = [Vec3(0,-half_h,0),Vec3(0,half_h,0)]
   else:
      dist = Player.scale_y / 2 + move + buffer
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
   global g
   global velo_y
   px = int(Player.x)
   py = int(Player.y)
   pych = (py//6)*6
   pxch = (px//6)*6
   for x in range(pxch-12,pxch+18,6):
      for y in range(min(pych-12,surface-6),surface+6,6):
         chuck(x,y)
   unload()
   velo_y -= g*time.dt 
   move_y = velo_y*time.dt

   if move_y < 0 :
      if can_move(Vec3(0,-1,0),abs(move_y)):
         Player.y += move_y
      else:
         velo_y = 0
   elif move_y > 0:
      if can_move(Vec3(0,1,0),move_y):
         Player.y += move_y
      else:
         velo_y = 0
   

def input(key):
    global facing
    move = 5*time.dt
    check = move + 0.25
    if held_keys["w"]:
        
        Player.texture = 'tex/up.png'
        facing = (0,1)
    if held_keys["s"]:
        
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

    if key == "scroll up" and len(blk_in_inven):
       selblk = (selblk+1)% len(blk_in_inven)
       
    if key == "scroll down" and len(blk_in_inven):
       selblk = (selblk-1)% len(blk_in_inven)

    if key == "space":
       global velo_y
       grounded = not can_move(Vec3(0,-1,0),0.1)
       if grounded:
          velo_y = jump
    if key == "left mouse down":
       hit = mouse.hovered_entity
       if hit and hasattr(hit,"grid_pos") and hit is not Player:
          hx , hy = hit.grid_pos
          dist = ((hx-Player.x)**2 + (hy - Player.y)**2)**0.5
          
          if dist <= 1.7 and (hx,hy) in blocks:
             destroy(hit)
             del blocks[(hx,hy)]
             removed.append((hx,hy))
       

    



app.run()


