if __name__ == "__main__":

    def find_word(x):
        # поиск самого длинного слова в строке слов
        line = x.split()
        length = 0
        l_word = ''
        for word in line: # поиск самого длинного слова
            if len(word) > length:
                length = len(word)
                l_word = word

        list_l_word = []
        for word in line: # создание списка, если несколько слов имеют максимальную длину
            if word != l_word and len(word) == len(l_word):
                list_l_word.append(l_word)
                list_l_word.append(word)

        return list_l_word if list_l_word else l_word

    print(find_word('привет медвед как  прекрасен  этот а мирр'))


    def find_word(x):
        # поиск самого длинного слова в строке слов
        longest = max(x.split())
        return longest

    print('------')
    print(find_word('ПРИВЕТ медвед как прекрасен  этот мирр'))
