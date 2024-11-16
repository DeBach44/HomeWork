# DeBach
# Module_7_1"Учёт товаров"
#___________________________________________________________________________
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


# _________________________________________________________________________
class Shop:
    __file_name = 'products.txt'

    def get_products(self):  #_Возврат текста фала "products.txt"
        file = open(self.__file_name, 'r')
        text = (file.read()) #_Присвоение текста считаного файла
        file.close()
        return f'{text}'

    def add(self, *products):
        file = open(self.__file_name, 'a')
        for i in products: 
            if i.name not in self.get_products():#_Проверка
                file.write(f'\n {i.name},{i.weight},{i.category}')
            else:
                print(f'{i.name},{i.weight},{i.category}: уже есть в магазине')
        file.close()
#___________________________________________________________________________________

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
