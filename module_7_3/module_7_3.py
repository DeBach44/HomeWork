#DeBach
#module_7_3"Найдёт везде"
'''
Домашнее задание по теме "Оператор "with"
'''
#_______________________________________________________________________
class WordsFinder:



    def __init__(self,*file_names):
        self.file_names = file_names

    #________________________________________________________________________
    def get_all_words(self):
        all_words = {}
        symbols = [',', '.', '=', '!', '?', ';', ':', '- ']
        for one_file in self.file_names:#one_file - один файл из file_names
            word = []
            with open(one_file, encoding= 'utf-8') as file:
                for line in file: #Перебор строк по очереди
                    line = line.lower() # line в нижний регистр
                    for i in symbols:
                        line = line.replace(i,'')
                    line = line.split()
                    word = word + line
                    all_words[one_file] = word
        return all_words

    #________________________________________________________________________

    def find(self, word):
        dict_ = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                dict_[key] = value.index(word.lower()) + 1

        return dict_

    #_________________________________________________________________________
    def count(self, word):
        counter = {}
        for key, value in self.get_all_words().items():
            word_count = value.count(word.lower())
            counter[key] = word_count

        return counter
    #_________________________________________________________________________

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
