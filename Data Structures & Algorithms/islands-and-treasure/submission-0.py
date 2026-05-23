class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECS = ((1,0), (0, 1), (-1, 0), (0, -1))

        # find all the treasure chests
        q = []
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j, 0))

        # perform bfs from starting points and keep updating the min distance
        visited = set()

        while q:
            r, c, distance = q.pop(0)
            visited.add((r, c))

            for x, y in DIRECS:
                dx, dy = r+x, c+y

                if (
                    dx in range(ROWS) and
                    dy in range(COLS) and 
                    (dx, dy) not in visited and
                    grid[dx][dy] not in (0, -1)
                ):
                    grid[dx][dy] = min(grid[dx][dy], distance+1)
                    q.append((dx, dy, distance+1))

