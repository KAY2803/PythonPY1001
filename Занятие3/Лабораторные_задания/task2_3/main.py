if __name__ == "__main__":

    def words_in_line():
        line = str(input('Введите строку любых слов: '))
        line = line.split()
        for i in line:
            print(i)

        return line

    print(words_in_line())

