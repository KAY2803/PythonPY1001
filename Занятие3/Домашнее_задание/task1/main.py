if __name__ == "__main__":
    # Write your solution here

    def find_numbers():
        # формирует список из вводимых значений по заданным параметрам
        numbers = []
        while True:
            number = int(input('Введите число'))
            if 3 <= number <= 13:
                numbers.append(number)
            elif number < 0:
                break
            else:
                continue
        return numbers

    print(find_numbers())


