def minFallingPathSum(m) -> int:
    for row in range(1, len(m)):
        for col in range(len(m)):
            if col == 0:
                m[row][col] = m[row][col] + min(m[row - 1][col], m[row - 1][col + 1])
            elif col == len(m) - 1:
                m[row][col] = m[row][col] + min(m[row - 1][col], m[row - 1][col - 1])
            else:
                m[row][col] = m[row][col] + min(
                    m[row - 1][col], m[row - 1][col + 1], m[row - 1][col - 1]
                )
    ans = min(m[-1])
    del m
    return ans
    pass


matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
ans = minFallingPathSum(matrix)
print(ans)
