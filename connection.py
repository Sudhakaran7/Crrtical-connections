class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(edges, parent, u, idx, lowlinks, lookup, result):
            if lookup[u]:
                return  
            lookup[u] = True
            curr_idx = lowlinks[u] = idx[0]
            idx[0] += 1
            for v in edges[u]:
                if v == parent:
                    continue
                dfs(edges, u, v, idx, lowlinks, lookup, result)
                lowlinks[u] = min(lowlinks[u], lowlinks[v])
                if lowlinks[v] > curr_idx:
                    result.append([u, v])
        
        edges = [[] for _ in range(n)]
        idx, lowlinks, lookup = [0], [0]*n, [False]*n
        result = []
        for u, v in connections:
            edges[u].append(v)
            edges[v].append(u)
        dfs(edges, -1, 0, idx, lowlinks, lookup, result)
        return result

val=Solution()
n=int(input())
matrix=[]
for i in range(n):
  rows=list(map(int,input().split()))
  matrix.append(rows)
print(*val.criticalConnections(n,matrix))
