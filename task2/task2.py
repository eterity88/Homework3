#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16]
#[2, 3, 5, 6] => [12, 15]


list = [4, 5, 7, 2, 6]
new_list = []
length = len(list)
for num in list:
    if(length > len(list)/2):
        new_list.append(num * list[length - 1])
        length -= 1
print(f"Список - {list}")
print(f"\nПроизведение пар чисел этого списка - {new_list}\n")