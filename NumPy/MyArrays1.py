import numpy as np
import random


# numbers 123 represent first row 456 represent 2 row with each of those elemts you have 3 columns, 3 elemts in each step, so 3 columns 2 rows

arr01 = np.array([[1, 2, 3], [4, 5, 6]])

arr02 = np.array([0.0, 0.1, 0.2, 0.3, 0.4])

for row in arr01:
    print(row)
    for col in row:
        print(col, end=' ')
    print()


for i in arr01.flat:
    print(i)

arr03 = np.zeros(5)

arr04 = np.ones((2, 4), dtype=int)

arr05 = np.full((3, 5), 13)


a = np.array([[random.randint(1, 10) for i in range(5)],
              [random.randint(1, 10) for i in range(5)]])

b = np.array(np.random.randint(1, 10, size=(2, 5)))

arr06 = np.arange(5)

arr07 = np.arange(5, 10)

arr08 = np.arange(10, 1, -2)

arr09 = np.linspace(0.0, 1.0, num=5)

arr10 = np.arange(1,21).reshape(4,5)

num01 = np.arange(1,6)

num02 = num01*2

num03 = num01**3

num01 += 10

num04 = num01 * num02

num05 = num01 > 13

num06 = num03 > num01

grades = np.array([[87,96,70], [100,87,90], [94,77,90], [100,81,82]])

print()