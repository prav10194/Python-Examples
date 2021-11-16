def print_spiral(row_end, column_end, spiral):
    row_start = 0
    column_start = 0
    while (row_start < row_end and column_start < column_end):
        for i in range(column_start, column_end):
            print(spiral[row_start][i])
        row_start += 1
        
        for i in range(row_start, row_end):
            print(spiral[i][column_end-1])
        column_end -= 1

        if (row_start < row_end):
            for i in range(column_end-1, column_start-1, -1):
                print(spiral[row_end-1][i])
            row_end -= 1
        
        if (column_start < column_end):
            for i in range(row_end-1, row_start-1, -1):
                print(spiral[i][column_start])
            column_start += 1
