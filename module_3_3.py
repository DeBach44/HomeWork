#DeBach
#Module_3_3"Распаковка позиционных параметров"

# 1) Функция с параметрами по умолчанию:

def print_params(a = 1, b = "строка", c = True):
    print(a, b , c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(a = 1.4, b = ["2", 1.6] )

#2)Распаковка параметров:

values_list = [4, "Спартак", ["a", "b"]]
values_dict = {"a":1, "b":"строка", "c":True}
print_params(*values_list)
print_params(**values_dict)

#3)Распаковка + отдельные параметры:

values_list_2 = [44.44, False]
print_params(*values_list_2, 42)