# 3619. Count Islands With Total Value Divisible by K

# You are given an m x n matrix grid and a positive integer k. An island is a group of positive integers (representing land) that are 4-directionally connected (horizontally or vertically).
# The total value of an island is the sum of the values of all cells in the island.
# Return the number of islands with a total value divisible by k.

class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        DIRECTIONS = [(1,0),(0,1),(-1,0),(0,-1)]
        def in_bounds(r: int,c: int) -> bool:
            if (0 <= r < rows and 0 <= c < cols):
                return True
            return False
        def dfs(r: int, c: int) -> int:
            if not in_bounds(r,c) or grid[r][c] == 0: return 0
            value = grid[r][c]
            grid[r][c] = 0
            for dr,dc in DIRECTIONS:
                value += dfs(r + dr, c + dc)
            return value
        valid_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    island_value = dfs(r,c)
                    if island_value % k == 0:
                        valid_islands += 1
        return valid_islands

if __name__ == "__main__":
    grid: list[list[int]] = [
            [0,2,1,0,0],
            [0,5,0,0,5],
            [0,0,1,0,0],
            [0,1,4,7,0],
            [0,2,0,0,8]
            ]
    k: int = 5
    s: Solution = Solution()
    answer: int = s.countIslands(grid,k)
    print(answer)
