import numpy as np
# program to find the product of two_d/three_d array
# colomn needs to equal row for dot or matmul product to work


def product_of_2d(x, y):
    return np.dot(np.array(x), np.array(y))


def product_of_3d(x, y):
    return np.matmul(np.array(x), np.array(y))


# colomn of first array needs to equal row of second array for dot or matmul product to work
print(product_of_2d([[1, 2, 2], [2, 3, 2]], [[2], [2], [2]]))

print(product_of_3d([[1, 2], [2, 3]], [[1, 2], [2, 3]]))

# do a simple calculation using : sin, cos, tan, log


def simple_calc(x):
    return np.sin(x), np.cos(x), np.tan(x), np.log(x)


print(simple_calc(30))

# program to create a 3x3 identity matrix
cool_ade = np.eye(3, 3)

print(cool_ade)

# 3x3 matrix with values ranging from (2, 10)
cool_ade = np.array(np.arange(2, 11)).reshape(3, 3)

print(cool_ade)

# matmul multiplication of 5x3 matrix
column_effect = np.arange(0, 30, 2).reshape(5, 3)
print(column_effect)

row_effect = column_effect.reshape(3, 5)
print(row_effect)

# multiplication of two matrix
print(row_effect @ column_effect)


# multiplication of matrix with operand
print(np.multiply(row_effect, 3))

cool_ade = np.arange(2, 37, 2).reshape(3, 6)
print(cool_ade)

cool_ade.reshape(6, 3)
