if __name__ == "__main__":

    N =407
    num_list = [int(i) for i in str(N)]
    new_list = 4 and 8 in set(num_list) or 9 in set(num_list)
    print(new_list)

    N = 407
    num_list = [int(i) for i in str(N)]
    if 4 in num_list and 8 in num_list or 9 in num_list:
        print('содержит пару цифр 4,8 и/или цифру 9')
    else:
        print('не содержит пару цифр 4,8 и цифру 9')


