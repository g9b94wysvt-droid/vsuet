def sort_rows_ascending(matrix):
    sorted_matrix = []
    for row in matrix:
        sorted_row = sorted(row)
        sorted_matrix.append(sorted_row)
    return sorted_matrix

def transform_matrix_min_even_zero_odd_one(matrix):
    transformed_matrix = []
    for row in matrix:
        if not row:
            transformed_matrix.append([])
            continue

        min_element = min(row)
        
        new_row = []
        for element in row:
            if element == min_element:
                new_row.append(0 if element % 2 == 0 else 1)
            else:
                new_row.append(element)
        transformed_matrix.append(new_row)
    return transformed_matrix
