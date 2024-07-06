#!/usr/bin/python3
""" pascal Triangle """


def pascal_triangle(n):
    """ pascal Triangle """

    if n <= 0:
        return []

    pascal_triangler = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            val = pascal_triangler[i - 1][j - 1] + pascal_triangler[i - 1][j]
            row.append(val)
        row.append(1)
        pascal_triangler.append(row)
    return pascal_triangler
