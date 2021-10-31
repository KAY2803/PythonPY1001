if __name__ == "__main__":

    def happy_number(n):
        number_ = [int(i) for i in str(n)]

        if sum(number_[:3]) == sum(number_[3:]):
            return "Счастливое число"
        else:
            return "Обычное число"

    print(happy_number(123123))



