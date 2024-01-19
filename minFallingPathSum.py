def minFallingPathSum(m: List[List[int]]) -> int:
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
