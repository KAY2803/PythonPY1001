def main():
    sqrt_list = []
    count = 0

    while True:
        if sum(sqrt_list) > 500:
            return len(sqrt_list[:-1])
        else:
            sqrt_list.append(count ** 2)
            print(f"Список: {sqrt_list}")
            print(f"Сумма его квадратов: {sum(sqrt_list)}")
            count +=1

if __name__ == "__main__":
    a = (main())
    print(a)






    # Write your solution here
    pass
