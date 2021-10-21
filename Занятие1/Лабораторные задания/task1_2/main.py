# Напишите ваше решение
TAX = 0.13
salary = float(input("Введите размер оклада (зарплаты)"))
tax = salary * TAX
income = salary - tax
print(tax, income)
