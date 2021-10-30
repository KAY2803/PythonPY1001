import collections

if __name__ == "__main__":
    main_str = """
        Данное предложение будет разбиваться на отдельные слова. 
        В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
        Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """

    dict_str = {}

    def dict_count_letter(n):
        # создает словарь, содержащий буквы из фразы и их количество
        n = n.lower()
        dict_str = {}
        for letter in str(n):
            if letter.isalpha():
                if letter in dict_str:
                    dict_str[letter] += 1
                else:
                    dict_str[letter] = 1

        return dict_str

    print(dict_count_letter(main_str))

    def dict_count_symbol(n):
        # создает новый словарь с % соотношением символов к их количеству
        dict_symbol = dict_count_letter(main_str)
        total = sum(dict_symbol.values())
        new_dict_symbol = {}
        for symbol, count in dict_symbol.items():
            new_dict_symbol[symbol] = round(count / total * 100, 5)

        return new_dict_symbol

    print(dict_count_symbol(main_str))


    from collections import Counter
    main_str = main_str.lower()
    list_letter = [i for i in str(main_str) if i.isalpha()]
    print(collections.Counter(list_letter))
    