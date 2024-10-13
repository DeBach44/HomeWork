def summ_object_list(list_):
    summ = 0
    if isinstance(list_, dict):
        for kay, value in list_.items():
            summ += summ_object_list(kay)
            summ += summ_object_list(value)
    elif isinstance(list_,(list,tuple,set)):
        for i in list_:
            summ += summ_object_list(i)
    elif isinstance(list_,str):
        summ += len(list_)
    elif isinstance(list_,(int,float)):
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
