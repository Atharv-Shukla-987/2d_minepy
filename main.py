from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

Player = Entity(
    model="quad",
    texture='tex/up.png', 
    scale=(0.5,1),
    collider="box"
)

def update():
    Player.x += (held_keys['d'] )*time.dt*5
    Player.y += (held_keys['w'] )*time.dt*5
    Player.x -= (held_keys['a'] )*time.dt*5
    Player.y -= (held_keys['s'] )*time.dt*5

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

app.run()