if __name__ == "__main__":

    N = 9876542
    if sum([int(i) for i in str(N)]) % 7 == 0:
        print(f"Сумма числа {N} кратна 7")
    else:
        print(f"Сумма числа {N} не кратна 7")

    # Write your solution here
    pass
