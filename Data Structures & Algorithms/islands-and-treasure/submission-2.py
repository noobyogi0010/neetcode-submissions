class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        rather than running seoarate bfs from each treasure, lets run bfs from each of them
        at the same time. the beauty of bfs is that the first cell it'll reach from a chest
        will be the shortest distance in comparision to distances from all other chests
        """
        N, M = len(grid), len(grid[0])

        # find all the chests
        chests = deque([])
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0:
                    chests.append((i, j))

        # lets start bfs from each of the starting points at the same time
        while chests:
            i, j = chests.popleft()

            # explore all its neighbors
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (
                    i + di < N and 
                    i + di >= 0 and
                    j + dj < M and
                    j + dj >= 0 and 
                    grid[i + di][j + dj] == 2147483647
                ):
                    grid[i + di][j + dj] = grid[i][j] + 1
                    chests.append((i + di, j + dj))

        
        