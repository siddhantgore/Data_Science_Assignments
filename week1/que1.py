#Q1: Given two matrices please print the product of those two matrices
# write your python code here
# you can take the above example as sample input for your program to test
# it should work for any general input try not to hard code for only given input examples
SIZE = 10
row1 = int(input("Enter the Number of rows for matrix A:- "))
col1 = int(input("Enter number of columns for matrix A:- "))

A = []

for i in range(row1):
    temp = []
    for j in range(col1):
        temp.append(int(input()))
    A.append(temp)

row2 = int(input("Enter the Number of rows for matrix B:- "))
col2 = int(input("Enter number of columns for matrix B:- "))

B = []

for i in range(row2):
    temp = []
    for j in range(col2):
        temp.append(int(input()))
    B.append(temp)

def matrix_mul(A, B):
    if(col1 == row2):
        result = [[0 for i in range(SIZE)]
                for j in range(SIZE)]

        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]
        print("Result of AxB is:- ")
        for m in range(row1):
            for n in range(col2):
                print(result[m][n], end=" ")
            print()
    else:
        print("AxB Operaton Not Possible")


matrix_mul(A, B)
