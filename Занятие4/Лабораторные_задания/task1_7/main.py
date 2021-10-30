if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]

    def numbers(lst):
        avarage = sum(lst) / len(lst)
        new_list = [i - avarage for i in lst]
        return (new_list)

    print(numbers(list_))
