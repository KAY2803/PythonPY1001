if __name__ == "__main__":

    s = list(range(1, 11))

    # предположим, что первый элемент в нашем списке максимальный
    max_value_index = 0
    max_value = s[max_value_index]
    A = s[0]

    for index, value in enumerate(s):
        if value >= max_value:
            max_value = value
            max_value_index = index
    s[0] = value
    s[index] = A
    print(s)



    # Write your solution here
    pass
