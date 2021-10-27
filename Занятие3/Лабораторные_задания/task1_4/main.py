def infinity(epsilon=0.0001):
    infinity_list = []
    n = 2

    while True:
       i = 1/n
       if i > epsilon:
           infinity_list.append(i)
           n *= 2
       else:
           break

    return sum(infinity_list)

if __name__ == "__main__":
    sum_inf = infinity()
    print(sum_inf)
