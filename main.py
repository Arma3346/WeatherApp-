# Создаем два списка и связываем их с переменными
list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]

# Извлекаем из первого списка второй элемент
second_element = list1[1]

# Изменяем последний объект во втором списке и выводим его на экран
list2[-1] = "f"
print(list2)

# Соединяем оба списка в один
merged_list = list1 + list2

# Снимаем срез из соединенного списка, который содержит некоторые части обоих первоначальных списков
sliced_list = merged_list[2:7]

# Добавляем в список-срез два новых элемента
sliced_list.append(6)
sliced_list.append("g")

# Выводим список-срез с новыми элементами на экран
print(sliced_list)
