from ursina import *
# импортируем объект персонажа
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina() 

# здесь будет описана игровая логика
# создаем объекты модели cube, с текстурой white_cube и заданными координатами
for x in range(16): 
   for z in range(16):
       Entity(model="cube", texture="white_cube", position=Vec3(x,0,z))
# создаем персонажа
player = FirstPersonController() 
# активируем невесомость, чтобы персонаж не упал в пустоту
player.gravity = 0.0 

# загружаем текстуру
grass_texture = load_texture('assets/grass.png')

for x_dynamic in range(16):
   for z_dynamic in range(16):
       # настраиваем объект Entity, загружаем модель block.obj
       Entity(model='assets/block', scale=0.5, texture=grass_texture, position=Vec3(x_dynamic,0,z_dynamic))

...
# загружаем текстуру руки
arm_texture = load_texture('assets/arm_texture.png')

# объявляем объект hand, привязываем к камере camera.ui, загружаем модель и размещаем ее в правом нижнем углу 
hand = Entity(parent = camera.ui, model = 'assets/arm',
             texture = arm_texture, scale = 0.2,
             rotation = Vec3(150, -10,0), position = Vec2(0.5,-0.6))
...
app.run()
