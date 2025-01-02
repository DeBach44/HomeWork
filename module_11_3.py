import inspect
import random
from random import choice

class Cats:

    def __init__(self):
        self.name = 'Клички нет'
        self.breed = 'Безпородный'
        self.paws = 4
        self.tail = True
        self.vaccination = False
        self.owner = False

    def info_the_cat(self):
        print(f'Кличка: {self.name}\nПорода: {self.breed}\nКоличество лап: {self.paws}')
        print(f'Хвост: {self.tail}\nПрививка: {self.vaccination}\nХозяин: {self.owner}')


cat1 = Cats()

def introspection_info(obj):
    info = dict()
    info['type'] = type(obj).__name__
    info['attributes'] = dir(obj)
    list_metods = list()
    for metod in dir(obj):
        attr = getattr(obj,metod)
        if callable(attr):
            list_metods.append(attr.__name__)
    info['methods'] = list_metods
    info['module'] = inspect.getmodule(obj)
    return info

def vivod(info):
    for key, value in info.items():
        print(key+':',value)
    print()


info = introspection_info(cat1)
vivod(info)

info = introspection_info(Cats)
vivod(info)

info = introspection_info(42)
vivod(info)

info = introspection_info(inspect)
vivod(info)

info = introspection_info('str')
vivod(info)

info = introspection_info(random.choice)
vivod(info)




































