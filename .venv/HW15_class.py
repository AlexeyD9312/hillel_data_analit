class Brick():
    lengh =0.25
    width = 0.1
    height = 0.065
    mass = 3.5
    size = lengh * width * height

    @classmethod
    def present_red_brick(cls):
        return f"Standart red brick size : lenght - {cls.lengh} m, width - {cls.width} m, height - {cls.height} m amd mass = {cls.mass} kg"

    def __init__(self,quantity:int):
        self.quantity = quantity

    def total_size_mass(self):
        total_mass = self.__class__.mass * self.quantity
        total_size = (self.__class__.lengh * self.__class__.width * self.__class__.height)*self.quantity
        return f"Total size material - {total_size} m3, and total mass - {total_mass} kg"

mat1 = Brick(1000)
print(mat1.present_red_brick())
print(mat1.total_size_mass())

Brick._mass = 3.7

def present_white_brick(cls):
    return f"Standart white brick size : lenght - {cls.lengh} m, width - {cls.width} m, height - {cls.height} m amd mass = {cls.mass} kg"

Brick.present_red_brick = classmethod(present_white_brick)

mat1 = Brick(1000)
print(mat1.present_red_brick())
print(mat1.total_size_mass())

class FoamBlock(Brick):
    lengh = 0.6
    width = 0.1
    height = 0.2
    mass = 8.3

def present_foam_block(cls):
    return f"Standart  foam block : lenght - {cls.lengh} m, width - {cls.width} m, height - {cls.height} m amd mass = {cls.mass} kg"

Brick.present_white_brick = classmethod(present_foam_block)

mat2 = FoamBlock(100)
print(mat2.present_white_brick())
print(mat2.total_size_mass())


