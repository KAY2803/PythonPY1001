if __name__ == "__main__":

    def palindrom(n):
        number_ = [int(i) for i in str(n)]
        if number_ == number_[::-1]:
            return f"Число {n} является палиндромом"
        else:
            return f"Число {n} не является палиндромом"

    print(palindrom(12343219))
    # Write your solution here
    pass
