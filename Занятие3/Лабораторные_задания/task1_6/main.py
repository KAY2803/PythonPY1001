if __name__ == "__main__":

    def extra_money(a, b):
        # расчет недостающей суммы денег
        month = 1
        scholarship = a * 10
        expenses = [b]
        while month < 10:
            b = b + (b * 0.03)
            expenses.append(b)
            month += 1

        money = sum(expenses) - scholarship
        return money

    print(extra_money(10000, 12000))