if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]

    def numbers(lst):
        even = [i for i in lst if i % 2 == 0]
        n_even = [i for i in lst if i % 2 != 0]

        if len(even) > len(n_even):
            return "четных больше"
        elif len(even) == len(n_even):
            return "четных и нечетных одинаково"
        return "нечетных больше"
    print(numbers(list_))


