a = range(123, 10000)
count_23 = 0
for i in list(a):
    if i % 23 == 0:
        count_23 += 1
print(count_23)

...  # TODO найти количество натуральных чисел кратных 23