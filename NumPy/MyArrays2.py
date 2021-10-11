import numpy as np

#ROWS - Each student (s0, s1, s2, s3)
#COLS - Each Test (Test0, Test1, Test2)
grades = np.array([[87,96,70], [100,87,90], [94,77,90], [100,81,82]])

student1 = grades[1]

student0_test1 = grades[0,1]

student0_1 = grades[0:2]

students1and3 = grades[[1,3]]

#only getting students 1 and 3 but only test 2
students1and3_test2 = grades[[1,3]]

all_students_test0 = grades[:,0]

all_students_test1_2 =grades[:,1:3]

all_students_test0and2 = grades[:,[0,2]]

rand_grades = np.random.randint(60,101,12).reshape(3,4)

print(rand_grades.mean())
#avg by col
print(rand_grades.mean(axis =0))
#avg by row
print(rand_grades.mean(axis =1))

#Shallow Copy
numbers = np.arange(1,6)

numbers_view = numbers.view()

numbers[1] *= 10

numbers_view[1] /= 10

numbers_slice = numbers[0:3]

numbers[1] *= 20

#Deep Copy
numbers_copy = numbers.copy()

numbers[1] *= 10

print()

