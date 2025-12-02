from collections import Counter

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        rows = [tuple(row) for row in grid]
        cols = [tuple(grid[r][c] for r in range(len(grid))) for c in range(len(grid[0]))]
        row_count = Counter(rows)
        return sum(row_count[col] for col in cols)

if __name__ == '__main__':
    grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    print(Solution().equalPairs(grid))