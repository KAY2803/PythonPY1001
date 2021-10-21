if __name__ == "__main__":

    A = int(input("Введите число"))
    B = int(input("Введите число"))
    C = int(input("Введите число"))

    if A < 45 and ((B and C) >= 45):
        print("true")
    elif B < 45 and ((A and C) >= 45):
        print("true")
    elif C < 45 and ((B and C) >= 45):
        print("true")
    else: print("false")
