# DeBach
# module_9_3 "Генераторные сборки"
# ____________________________________________________________________________________________________________________
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x[0]) - len(x[1]) for x in zip(first, second) if len(x[0]) != len(x[1]))

second_result = (len(first[i]) == len(second[j]) for i in range(len(first)) for j in range(len(second)) if i == j)
# ____________________________________________________________________________________________________________________
print(list(first_result))

print(list(second_result))
# _____Второй раз не выполнится_________
print(list(first_result))

print(list(second_result))
