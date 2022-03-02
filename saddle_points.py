def saddle_points(matrix):
    rotated = list(zip(*reversed(matrix)))

    saddle_points = []
    for row_number, row in enumerate(matrix):
        max_val = max(row)
        column_indicies = [i for i, v in enumerate(row) if v == max_val]

        for column in column_indicies:
            min_val = min(rotated[column])
            min_columns = [index for index, v in enumerate(
                rotated[column]) if v == min_val]
            for col in min_columns:
                if col in column_indicies and min_val == max_val:
                    saddle_points.append((row_number, column))
    return list(set(saddle_points))


print(saddle_points([[6, 7, 8], [5, 5, 5], [7, 5, 6]]))