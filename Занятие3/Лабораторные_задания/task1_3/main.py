if __name__ == "__main__":
    # Write your solution here

    def divide(n):
        # раскладывает число на простые множители
        divider = range(2, n + 1)
        list_dividers = []

        for d in divider:
            while n % d == 0:
                    n = n / d
                    list_dividers.append(d)

        return list_dividers

    print(divide(123))



