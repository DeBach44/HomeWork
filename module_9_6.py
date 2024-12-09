# DeBach
# module_9_5 "Range - это просто"

def all_variants(text):
    long = len(text)
    for i in range(1,long + 1):
        for j in range(0,long-i+1):
            yield text[j:j+i],[j,j+i]
a = all_variants("ABC")
for i in a:
    print(i)
