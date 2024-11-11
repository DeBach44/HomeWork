# DeBach
# Module_6_2"Изменять нельзя получать"

#_________________________Родительский_Класс_Vehicle__________________________________
class Vehicle:

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner # (str)владелец транспорта-(владелец может меняться)

        self.__model = __model # (str)модель (марка) транспорта-(не можем менять название модели)

        self.__engine_power = __engine_power # (int)мощность двигателя-(не можем менять мощность двигателя самостоятельно)

        self.__color = __color # (str)название цвета-(не можем менять цвет автомобиля своими руками)


#__________________________________________________________________________________________________________
    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")
#_______________________________________________________________________________________________
    def set_color(self, new_color: str):
        color_variants_lower = [] # Список, который будет пополнятся имеющимися цветами в нижнем регистре
        for i in self.__COLOR_VARIANTS: # Создания списка цветов в нижнем регистре
            color_variants_lower.append(i)
        if new_color.lower() in color_variants_lower: # Проверка на наличие  цвета в списке
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")
#_________________________Дочерние_Классы_Vehicle_____________________________________
#
#_____________________________Класс_Sedan____________________________________________
class Sedan(Vehicle):

    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
