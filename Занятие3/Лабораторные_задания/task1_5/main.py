if __name__ == "__main__":

   def find_sum():
       sum_numbers = 0
       while True:
           number = int(input('Введите число: '))
           if number > 0:
               sum_numbers += number
           elif number == 0:
               break
       return sum_numbers

   print(find_sum())
