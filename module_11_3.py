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
    list_attributes = [method for method in dir(obj) if not callable(getattr(obj,method))]
    info['attributes'] = list_attributes
    list_methods = [method for method in dir(obj) if callable(getattr(obj,method))]
    info['methods'] = list_methods
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




































