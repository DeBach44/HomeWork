#DeBach
def get_matrix(n,m,value):
    matrix = []
    # Создание строки матрицы
    for i in range(n):
        x = []
        # Добавление столбцов матрицы в созданную строку
        for j in range(m):
            x.append(value)
        #Добавление полученной строки в matrix
        matrix.append(x)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
