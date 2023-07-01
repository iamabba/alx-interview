#!/usr/bin/python3

''' This is a function to generate Pascal's triangle
up to the specified row number.'''


def pascal_triangle(n):
    # If the input is less than or equal to 0, return an empty list
    if n <= 0:
        return []

    # Create an initial row with a single element, 1
    triangle = [[1]]

    # Continue generating rows until the desired row number is reached
    while len(triangle) < n:
        # Get the previous row
        prev_row = triangle[-1]

        # Generate a new row by summing adjacent elements from the previous row
        new_row = [1] + [
            prev_row[i] + prev_row[i + 1]
            for i in range(len(prev_row) - 1)
        ] + [1]

        # Append the new row to the triangle
        triangle.append(new_row)

    return triangle
