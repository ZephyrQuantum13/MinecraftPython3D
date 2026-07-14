from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

width = 20
depth = 20


for x in range(width):
    for z in range(depth):
        Entity(
            model='cube',
            texture='dirt-block', 
            scale=1,
            position=(x, 0, z),
            collider='box',
            shader=lit_with_shadows_shader
        )

player = FirstPersonController()
player.position = (width/2, 2, depth/2)
player.fly = False
player.gravity = 1.5
player.speed = 6

sun = DirectionalLight()
sun.look_at(Vec3(1, -2, 0.5))
sun.shadows = True
sun.shadow_map_resolution = Vec2(1024, 1024) 

Sky() 



app.run()