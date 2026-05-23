class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)

            for neigh in adj[node]:
                if neigh == prev:
                    continue
                if not dfs(neigh, node):
                    return False

            return True

        return dfs(0, -1) and n==len(visited)

        