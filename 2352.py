from collections import Counter

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        rows = [tuple(row) for row in grid]
        cols = [tuple(grid[r][c] for r in range(len(grid))) for c in range(len(grid[0]))]
        row_count = Counter(rows)
        return sum(row_count[col] for col in cols)
