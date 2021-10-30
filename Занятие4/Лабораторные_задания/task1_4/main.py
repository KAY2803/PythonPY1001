if __name__ == "__main__":

    def numbers(n, m):
        avarage = sum(range(n, m+1)) / len(range(n, m+1))
        list_ = [i for i in range(n, m+1) if i > avarage]
        return list(list_)

    print(numbers(1, 5))

    # Write your solution here
    pass
