if __name__ == "__main__":

    def palindrom(str):
        # определяет, является ли строка палиндромом
        str = str.lower()
        letters = []
        new_letters = []
        for letter in str:
            if letter != " " and letter != ",":
                letters.append(letter)
        new_letters = letters[::-1]
        if letters == new_letters:
            print('ДА')
        else:
            print('НЕТ')
        return letters
    print(palindrom('Я иду с мечем судия'))



