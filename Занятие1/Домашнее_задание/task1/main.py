speed = float(input("Введите скорость передачи данных в б/сек"))
time = float(input("ВВедите время игры в мин"))
coast = float(input("Введите цену за 1Гбайт"))
size_ = (speed * time * 60 / (1024 ** 3))
money = (size_ - 1) * coast if size_ > 1 else 0

print(size_, money)
# Напишите ваше решение

