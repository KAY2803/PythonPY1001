if __name__ == "__main__":

    def money(S, a, b):
        # считает срок, на который хватит денег
        money = S + a
        expences = b
        month = 1
        while money >= expences:
            money += a
            b += b * 0.05
            expences += b
            month += 1

        return month-1

    print(money(50000, 10000, 12000))


    # Write your solution here
    pass
