def minFallingPathSum(matrix) -> int:
    rows = len(matrix)
    cols = len(matrix[0])
    minSum = min(matrix[0])
    col = matrix[0].index(minSum)
    currentRow = 1
    while currentRow < rows:
        toAdd = min(
            [
                matrix[currentRow][col],
                matrix[currentRow][col + 1 if col < cols - 1 else col],
                matrix[currentRow][col - 1 if col > 0 else col],
            ]
        )
        col = matrix[currentRow].index(toAdd)
        currentRow += 1
        minSum += toAdd
        # pass
    return minSum
    # pass


matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
ans = minFallingPathSum(matrix)
print(ans)
