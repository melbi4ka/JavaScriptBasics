import sys
from io import StringIO

input1 = '''S-#--
-#---
-#-#-
---#X
'''
input2 = """S----
-#--#
---#-
-#-#X
"""

input3 = """S----
-#--#
---#-
-#X#-
"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

from collections import deque

def is_inside(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols


def first_step(r, c, rows, cols, matrix):
    child_cells = [
        [r, c + 1],
        [r + 1, c]
    ]
    result = []
    for child_row, child_col in child_cells:
        if is_inside(child_row, child_col, rows, cols) and (matrix[child_row][child_col] == "-" or
                matrix[child_row][child_col] == "X"):
            result.append([child_row, child_col])
    return result


def next_step(r, c, rows, cols, matrix):
    child_cells = [
        [r, c + 1],
        [r + 1, c],
        [r - 1, c],
        [r, c - 1]
    ]
    result = []
    for child_row, child_col in child_cells:
        if is_inside(child_row, child_col, rows, cols) and (matrix[child_row][child_col] == "-" or
                matrix[child_row][child_col] == "X"):
            result.append([child_row, child_col])
    return result


matrix = []
my_row = 0
my_col = 0
rows, cols = 4, 5

for r in range(rows):
    line = list(input())
    matrix.append(line)
    for c in range(cols):
        if matrix[r][c] == "S":
            my_row = r
            my_col = c

# print(matrix)
# print(my_row)
# print(my_col)
way_out = False
no_way_out = False

while True:
    ways = deque(first_step(my_row, my_col, rows, cols , matrix))
    matrix[my_row][my_col] = "0"

    if not ways:
        no_way_out = True
        break

    while ways:
        next_row, next_col = ways.popleft()
        if matrix[next_row][next_col] == "X":
            way_out = True
            break
        matrix[next_row][next_col] = "0"
        path = deque(next_step(next_row, next_col, rows, cols, matrix))

        if path and len(path) == 1:
            r,c = path.popleft()
            next_row, next_col = r,c
            ways.append([next_row, next_col])
        elif path and len(path) > 1:
            while path:
                r,c = path.popleft()
                next_row, next_col = r,c
                ways.append([next_row, next_col])


    if way_out:
        break

if way_out:
    print("There is a way out")
if no_way_out:
    print("No way out")
for r in matrix:
    print(*r)

