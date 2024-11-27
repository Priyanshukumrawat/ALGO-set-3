def print_spiral(matrix):
    if not matrix:
        return

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Print the top row from left to right
        for i in range(left, right + 1):
            print(matrix[top][i], end=" ")
        top += 1

        # Print the right column from top to bottom
        for i in range(top, bottom + 1):
            print(matrix[i][right], end=" ")
        right -= 1

        if top <= bottom:
            # Print the bottom row from right to left
            for i in range(right, left - 1, -1):
                print(matrix[bottom][i], end=" ")
            bottom -= 1

        if left <= right:
            # Print the left column from bottom to top
            for i in range(bottom, top - 1, -1):
                print(matrix[i][left], end=" ")
            left += 1

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print_spiral(matrix)
