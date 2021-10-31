if __name__ == "__main__":
    def same_digits(n):
    # проверяет есть ли в числе одинаковые цифры
        digits = [int(d) for d in str(n)]
        for d in digits:
            if len(set(digits)) == len(str(n)):
                return "Все цифры разные"
            else:
                return "В числе есть одинаковые цифры"

    print(same_digits(12345))
    print(same_digits(2234034856))


    from collections import Counter
    def same_digits_1(n):
    # проверяет состоит ли число из одинаковых цифр
        dict_digits = Counter([d for d in str(n)])
        for counts in dict_digits.values():
            if counts > 1:
                return "В числе есть одинаковые цифры"
            else:
                return "Все цифры разные"
    print(same_digits_1(12345))
    print(same_digits_1(2234034856))