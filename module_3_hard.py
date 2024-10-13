#DeBach
#Module_3_hard"Подробнее о функциях"

def summ_object_list(list_):
    '''
    Эта функция для подсчёта суммы всех чисел и длин всех строк списка
    '''
    summ = 0

    if isinstance(list_, dict): #Проверка на словарь.
        for kay, value in list_.items():
            summ += summ_object_list(kay)
            summ += summ_object_list(value)

    elif isinstance(list_,(list,tuple,set)):#Проверка на список, кортеж, множество.
        for i in list_:
            summ += summ_object_list(i)

    elif isinstance(list_,str):#Проверка на строку.
        summ += len(list_)

    elif isinstance(list_,(int,float)):#Проверка на число.
        summ += list_

    return summ
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = summ_object_list(data_structure)
print(result)
print(help(summ_object_list))
