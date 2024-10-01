students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(type(students))
students_list=list(students)  #множество в список
sort_students_list=sorted(students_list) #список по алфавиту

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
num_list = len(grades)
i1 = grades[0]

av_sc = []
for i1 in grades:

      average = sum (i1) / len (i1)

      av_sc.append(average)

#print(av_sc)
dictionary = dict(zip(sort_students_list, av_sc))
print(dictionary)