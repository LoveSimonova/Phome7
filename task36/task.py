def print_operation_table(operation, num_rows, num_columns):
    i=1
    j=1
    matrix = [[0 for j in range(num_columns)] for i in range(num_rows)]
    for i in range(num_rows):
        for j in range (num_columns):
            matrix[i][j]=operation(i+1,j+1)
    for k in range(num_rows):
        print(matrix[k][:])

print_operation_table(lambda x, y: x * y,6,6)