#DeBach
#Module_3_4"Произвольное число параметров"

def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        lower_o_w = i.lower()
        if lower_o_w in root_word.lower() or root_word.lower() in lower_o_w:
            same_words.append(i)
        else:
            continue
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)