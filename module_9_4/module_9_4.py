# DeBach
# module_9_4 "Функциональное разнообразие"
# ________________________________________________________________
# ______________________Lambda-функция____________________________
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)


# __________________________Замыкание_______________________________

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for i in data_set:
                file.write(f'{i} \n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# ____________________________Метод __call__ ______________________________________
class MysticBall:
    from random import choice

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        n = self.choice(self.words)
        return n


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
#__________________________________END______________________________________________