if __name__ == "__main__":

    N = 9999999
    if 10 <= sum([int(i) for i in str(N)]) <= 99:
        print(f"Сумма числа {N}: {sum([int(i) for i in str(N)])} - двухзначное число")
    else:
        print(f"Сумма числа {N}: {sum([int(i) for i in str(N)])} - не является двухзначным числом")

    # Write your solution here
    pass
