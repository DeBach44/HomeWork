#DeBach
#module_7_2"Записать и запомнить"
#_______________________________________________________________________
import io
from pprint import pprint

def custom_write(file_name, strings):#file_name - название фала
                                     #strings - список строк которые нужно вставить
    string_positions = {}
    str_num = 0
    file = open(file_name, 'w', encoding = 'utf-8')#

    for str_ in strings: #Перебор списка строк
        str_num += 1 #Номер строки
        cursor = file.tell()#Положение курсора
        file.write(f"{str_}\n")#Добавление строки в файл
        string_positions[(str_num,cursor)] = str_
    return string_positions
    file.close()

#_______________________________________________________________________
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)





