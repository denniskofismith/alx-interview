#!/usr/bin/python3

def pascal_triangle(n):

    if n <= 0:
        return []

    def get_row(row_index, memo={}):
        if row_index in memo:
            return memo[row_index]

        if row_index == 1:
            memo[row_index] = [1]
        else:
            prev_row = get_row(row_index - 1, memo)
            new_row = [1]
            for i in range(1, len(prev_row)):
                new_row.append(prev_row[i - 1] + prev_row[i])
            new_row.append(1)
            memo[row_index] = new_row
        return memo[row_index]

    return [get_row(i) for i in range(1, n + 1)]
