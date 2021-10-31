if __name__ == "__main__":

    def same_digits(n):
        # проверяет состоит ли число из одинаковых цифр
        digits = [int(d) for d in str(n)]

        if len(set(digits)) == 1:
            return "Все цифры числа одинаковые"
        else:
            return "Не все цифры числа одинаковые"

    print(same_digits(555555))




