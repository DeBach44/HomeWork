#DeBach
immutable_var = tuple(['a', 'b', 1, 2])
print(immutable_var)
print(type(immutable_var))
mutable_list = ['a', 'b', 'c', 1]
print(mutable_list)
print(type(mutable_list))
mutable_list[0] = 'x'
mutable_list.append(4)
mutable_list.extend(['e', 7, 8])
print(mutable_list)