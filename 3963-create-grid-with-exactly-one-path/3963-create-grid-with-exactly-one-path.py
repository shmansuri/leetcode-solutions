class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []

        for i in range(m):
            row =[]
            for j in range(n):
                row.append('#')
            grid.append(row)

        for i in range(m):
            for j in range(n):
                if i == 0 or j == n-1:
                    grid[i][j] = '.'
        
        return [''.join(row) for row in grid]


        