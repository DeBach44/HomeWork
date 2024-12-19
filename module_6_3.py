# _______________________________________________________________________
from os import remove

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self,speed):
        self._cords = [0,0,0]
        self.speed = speed

    def move(self, dx, dy, dz):
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += dz * self.speed
        if self._cords[2] <= 0:
            print("It's too deep, i can't dive :(")
            self._cords[2] = 0


    def get_cords(self):
        print(f'X: {int(self._cords[0])}, Y: {int(self._cords[1])}, Z: {int(self._cords[2])}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


# ____________________________________________________________________
class Bird(Animal):
    beak = True

    def lay_eggs(self):
        from random import randint as rdm
        random_number = rdm(1, 4)
        print(f"Here are(is) {random_number} eggs for you")


# ________________________________________________________________________
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= abs(dz) * (self.speed/2)


# _______________________________________________________________________
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

# ________________________________________________________________________
class Duckbill(Bird, PoisonousAnimal, AquaticAnimal, ):
    def __init__(self, spead):
        super().__init__(spead)

    sound = "Click-click-click"

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
