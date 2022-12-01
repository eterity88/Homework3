#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
#Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

my_list = [randint(1,100) for i in range(6)]
n = len(my_list)
print(my_list)

def OddSum(a, n):
    odd_sum = sum(a[1::2])

    print("Сумма элементов с нечетными индексами", odd_sum)
OddSum(my_list, n)


