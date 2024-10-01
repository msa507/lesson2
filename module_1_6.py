# Работа со словарями:

my_dict = {'Сергей' : 1962, 'Lenin' : 1870, 'Ronny' : 2009}
print(my_dict)
print(my_dict ['Сергей'])    #по существ. ключу
print(my_dict.get('Lenin'))  #по существ. ключу
print(my_dict.get('Dan', 'Такого нет'))    #по не существ. ключу
#my_dict ['Robby'] = 2000
my_dict.update({'Robby': 2000,
                'Ian' : 2001})
q=my_dict.pop('Lenin')
print(q)
print(my_dict)
#
#Работа с множествами:

my_set = {58, 5, 9, 44, 58, 11, 5, (1, 2), 'Point', False, 'Point' }
print(my_set)
s = {3, True}
my_set = my_set.union (s)
print(my_set)
my_set.discard(5)
print(my_set)