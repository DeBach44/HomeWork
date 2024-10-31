# DeBach
# Module_5_3"Перегрузка операторов"
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

    def __len__(self):  # Возврат количества этажей type int
        return self.number_of_floors

    def __str__(self):  # Возврат наименования и количества этажей type str
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    # ________________Функции_сравнения________________________________________________

    def __eq__(self, other):  # (==)
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):  # (<)
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):  # (<=)
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):  # (>)
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):  # (>=)
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):  # (!=)
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    # ________________Функции_прибавления________________________________________________

    def __add__(self, value):
        if isinstance(value, int):#Проверка на тип int
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        if isinstance(value, int):#Проверка на тип int
            self.number_of_floors += value
            return self

    def __iadd__(self, value):
        if isinstance(value, int):#Проверка на тип int
            self.number_of_floors += value
            return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
