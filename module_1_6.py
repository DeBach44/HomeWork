#DeBach
#Словарь
my_dict = {"Anton" : 1998, "Danil" : 1995 }
print(my_dict)
print(my_dict["Anton"])
my_dict["Sasha"] = 1993
print(my_dict["Sasha"])
my_dict.update({"Lexa" : 1991,
                "Viktor" : 1999})
a = my_dict.pop("Anton")
print(a)
print(my_dict)
#Множества
my_set = {1,1,2,2,2.5,2.5,"a","a","b","b"}
print(my_set)
my_set.update({3,"c"})
my_set.discard(2.5)
print(my_set)

