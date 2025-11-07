def find_max_in_ordered_rows(matrix):
    max_element = None
    
    for row in matrix:
        if not row:
            continue

        is_ascending = all(row[i] <= row[i+1] for i in range(len(row) - 1))
        is_descending = all(row[i] >= row[i+1] for i in range(len(row) - 1))

        if is_ascending or is_descending:
            row_max = max(row)
            if max_element is None or row_max > max_element:
                max_element = row_max
                
    return max_element
