from ursina import *

app = Ursina() 

# здесь будет описана игровая логика
# создаем объекты модели cube, с текстурой white_cube и заданными координатами
for x in range(16): 
   for z in range(16):
       Entity(model="cube", texture="white_cube", position=Vec3(x,0,z))


app.run()
