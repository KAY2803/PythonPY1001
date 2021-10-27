def remove_whitespace(str_):
    new_list = str_.split('_')

    new_list1 = []
    for word in new_list:
        if len(word) != 0:
            new_list1.append(word)
    return " ".join(new_list1)



if __name__ == "__main__":
    str_with_space = "    123.    test   print test11    "  # исходная строка
    print(remove_whitespace(str_with_space))
