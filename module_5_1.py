# DeBach
#Module_5_1"Атрибуты и методы объекта"
class House:
    pass

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for the_floor in range(1, new_floor + 1):  # Перебор этажей до нужного
            if 0 < new_floor < self.number_of_floors:  # Проверка на существование этажа
                print(the_floor)  # Вывод текущего этажа

            else:
                print("Такого этожа не существует")
                break  # Остановка программы


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
