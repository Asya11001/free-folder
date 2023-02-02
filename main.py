import random
from pandas import *


def createMatrix(rowCount, columnCount, dataList):
    matrix = []
    for i in range(rowCount):
        rowList = []
        for j in range(columnCount):
            rowList.append(dataList[rowCount * i + j])
        matrix.append(rowList)

    return matrix


def displayMatrix(matrix):
    print(DataFrame(matrix))
    print("\n");


def getDeterminantRecursive(A, total=0):
    # Section 1: store indices in list for row referencing
    indices = list(range(len(A)))

    # Section 2: when at 2x2 submatrices recursive calls end
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val

    # Section 3: define submatrix for focus column and
    #      call this function
    for fc in indices:  # A) for each focus column, ...
        # find the submatrix ...
        As = A.copy()  # B) make a copy, and ...
        As = As[1:]  # ... C) remove the first row
        height = len(As)  # D)

        for i in range(height):
            # E) for each remaining row of submatrix ...
            #     remove the focus column elements
            As[i] = As[i][0:fc] + As[i][fc + 1:]

        sign = (-1) ** (fc % 2)  # F)
        # G) pass submatrix recursively
        sub_det = getDeterminantRecursive(As)
        # H) total all returns from recursion
        total += sign * A[0][fc] * sub_det

    return total


def reverseMatrix(matrix):
    return list(zip(*matrix))


def randomArray(rowCount, columnCount, rangeNumber):
    array = []
    for i in range(rowCount * columnCount):
        array.append(int(random.random() * 100 % rangeNumber + 1 - rangeNumber // 2))
    return array


def multiplyMatrix(A, B):  # Работает только с одинаковыми размерами, например 3x3 & 3x3 || 4x4 & 4x4 || 5x5 & 5x5;
    zip_b = list(zip(*B))
    return [[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in A]


def additionMatrix(A, B):
    array = []
    rowCount = len(A)
    columnCount = len(A[0])
    for i in range(rowCount):
        row = []
        for j in range(columnCount):
            row.append(A[i][j] + B[i][j])
        array.append(row)
    return array

def substractionMatrix(A, B):
    array = []
    rowCount = len(A)
    columnCount = len(A[0])
    for i in range(rowCount):
        row = []
        for j in range(columnCount):
            row.append(A[i][j] - B[i][j])
        array.append(row)
    return array


def main():
    arraySize = 3
    matrix1 = createMatrix(arraySize, arraySize, randomArray(arraySize, arraySize, rangeNumber=9))
    matrix2 = createMatrix(arraySize, arraySize, randomArray(arraySize, arraySize, rangeNumber=9))
    displayMatrix(matrix1)
    displayMatrix(matrix2)
    matrix3 = []
    matrix3 = substractionMatrix(matrix1, matrix2)

    displayMatrix(matrix3)


if __name__ == "__main__":
    main();
