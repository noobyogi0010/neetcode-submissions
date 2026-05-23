class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        perform bfs from each treasure chest location 
        and you can visit a visited cell again bcz it is possible that 
        the new chest is closer to the older one
        pick all the treasure chest and then run bfs from each one of them
        """
        N, M = len(grid), len(grid[0])
        
        start = []
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0:
                    start.append([i, j])

        for i, j in start:
            q = deque([[i,j,0]])
            seen = set()
            while q:
                r, c, dist = q.popleft()
                seen.add((r, c))
                grid[r][c] = min(grid[r][c], dist)

                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    if (
                        dr + r < N and 
                        dr + r >= 0 and 
                        c + dc < M and 
                        c + dc >=0 and 
                        grid[r + dr][c + dc] not in {0, -1} and
                        (r + dr, c + dc) not in seen
                    ):
                        q.append([dr + r, dc + c, dist + 1])
