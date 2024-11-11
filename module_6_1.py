# DeBach
# Module_6_1"Съедобное, несъедобное"
#________________________________Класс_Animal________________________________
class Animal:#Родительский класс Mammal и Predator
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

#______________________________Класс_Plant__________________________________
class Plant:#Родительский класс для Flower и Fruit
    edible = False

    def __init__(self, name):
        self.name = name

#________________Дочерние_Классы_Animal________________________________
#Классы без собственных атрибутов ссылаются на атрибуты из родительских но после
#функции eat обьекту присвоится собственный атрибут
class Mammal(Animal):
    pass


class Predator(Animal):
    pass

#________________Дочерние_Классы_Plant________________________________
class Flower(Plant): #Атрибут edible будет браться из родительского класса
    pass


class Fruit(Plant):

    edible = True #собственный атрибут


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
