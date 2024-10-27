# DeBach
#Module_5_2"Специальные методы классов"
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

    def __len__(self): # Возврат количества этажей type int
        return self.number_of_floors

    def __str__(self): # Возврат наименования и количества этажей type str
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
