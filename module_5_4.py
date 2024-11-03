# DeBach
# Module_5_4"Различие атрибутов класса и экземпляра"
class House:
    pass

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])  # Внесение в историю названия ЖК
        return super().__new__(cls)

    def __del__(self):  # Функция удаления объекта
        return print(f"{self.name} снесён, но он останется в истории.")

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

    # ________________Функции_сравнения_количества_этажей___________________________

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

    # ________________Функции_прибавления_к_количеству_этажей___________________

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
    #________________________________________________________________________________

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
