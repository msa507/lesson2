#2. Задайте переменные разных типов данных:
#  - Создайте переменную immutable_var и присвойте ей кортеж
#  из нескольких элементов разных типов данных.
# - Выполните операции вывода кортежа immutable_var на экран.
#
immutable_var = 9, 52, 45.2, 'sing', int
print(immutable_var)
#
#3. Изменение значений переменных:
#  - Попытайтесь изменить элементы кортежа immutable_var. Объясните,
#  почему нельзя изменить значения элементов кортежа.
#immutable_var[0] = 99 #попытка изменить кортеж приводит к ошибке
print(immutable_var)  #кортеж - неизменяемый тип данных
print(immutable_var[0])  # возможна индексация
#
#4. Создание изменяемых структур данных:
#  - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
#  - Измените элементы списка mutable_list.
#  - Выведите на экран измененный список mutable_list.
mutable_list=[45, 'clon', 987, ['list', True]]
print(mutable_list)
print(type (mutable_list))
mutable_list [-1] = 'Ok'
print(mutable_list)