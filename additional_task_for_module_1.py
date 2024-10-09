grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(list(students))
a = sum(grades[0])/ len(grades[0])
grades[0] = a
b = sum(grades[1])/ len(grades[1])
grades[1] = b
c = sum(grades[2])/ len(grades[2])
grades[2] = c
d = sum(grades[3])/ len(grades[3])
grades[3] = d
e = sum(grades[4])/ len(grades[4])
grades[4] = e
average_score = dict(zip(students, grades))
print(average_score)