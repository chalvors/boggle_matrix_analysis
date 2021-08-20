#boggle matrix analysis main app

def find_adjacent_nodes(row_index, col_index):
    adjacent_nodes = []
    temp_num_pair = []
    count = 0

    while count < 9:
        if count == 0:
            temp_num_pair = [row_index-1, col_index-1]
        elif count == 1:
            temp_num_pair = [row_index-1, col_index]
        elif count == 2:
            temp_num_pair = [row_index-1, col_index+1]
        elif count == 3:
            temp_num_pair = [row_index, col_index+1]
        elif count == 4:
            temp_num_pair = [row_index+1, col_index+1]
        elif count == 5:
            temp_num_pair = [row_index+1, col_index]
        elif count == 6:
            temp_num_pair = [row_index+1, col_index-1]
        elif count == 1:
            temp_num_pair = [row_index, col_index-1]

        adjacent_nodes.append(temp_num_pair)
        count += 1
    
    print(adjacent_nodes)

    

def find_center_nodes():
    row_index = 0
    col_index = 0

    while row_index < 3:
        while col_index < 3:
            if row_index != 0 and row_index != 2:
                if col_index != 0 and col_index != 2:
                    print(matrix_values[row_index][col_index])
                    find_adjacent_nodes(row_index, col_index)
            col_index += 1
        row_index += 1
        col_index = 0

matrix_values = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix_values)
print('')

find_center_nodes()

