# DeBach
# module_9_6 "Декораторы в Python"

def is_prime(func):
    def wrapper(*args):
        f = func(*args)
        prime = True
        if f <= 1:
            return (f"Сумма чисел меньше или равно 1")
        for i in range(2,f):
            if f % i == 0:
                prime = False
        if prime:
            return (f"Простое\n{f}")
        else:
            return (f"Составное\n{f}")
    return wrapper

@ is_prime
def sum_three(*args):
    sum_num = sum(args)
    return sum_num

result = sum_three(2, 3, 6)
print(result)