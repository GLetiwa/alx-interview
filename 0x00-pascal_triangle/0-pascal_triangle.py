#!/usr/bin/python3
# returns a list of lists of ints representing the Pascal’s triangle of n

if __name__ == "__main__":
    def pascal_triangle(n):
        """ Evaluates a pascal triangle """
        if n <= 0:
            return []

        triangle = [[1]]  # Initialize with the first row
        for i in range(1, n):
            row = [1]  # First element of each row is always 1
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)  # Last element of each row is always 1
            triangle.append(row)

        return triangle


# Test the function
triangle = pascal_triangle(5)
for row in triangle:
    print("[{}]".format(",".join(map(str, row))))
