if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]

    def numbers(lst):
        lst = [random.randint(-10, 10)]
        return len([i for i in lst if i > lst[0]])

    print(numbers(list_))
