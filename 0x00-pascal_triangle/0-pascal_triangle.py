#!/usr/bin/python3
# returns a list of lists of ints representing the Pascal’s triangle of n

def pascal_triangle(n):
    """handles the pascals triangle expansion"""
    if n <= 0:
        return []
    triangle = [[1]] # first element of each row is always 1
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle

# test function
triangle = pascal_triangle(5)
for row in triangle:
    print("[{}]".format(",".join([str(x) for x in row])))
