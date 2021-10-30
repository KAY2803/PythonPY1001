if __name__ == "__main__":

    N = 12345
    num_list = [int(i) for i in str(N)]
    print("1", num_list)
    print("2", sum(num_list))
    print("3", sum([i for i in num_list if i % 2 == 0]))
    print("4", len(num_list))
    print(f"5 min: {min(num_list)} max: {max(num_list)}")
    print(f"6 нечетные: {num_list[::2]}, четные: {num_list[1::2]}")
    print("7", str(num_list[0] - num_list[-1]))
    print(f"8 min: {min(num_list)} position: {num_list.index(min(num_list))+1}")



