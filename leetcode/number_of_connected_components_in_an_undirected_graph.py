# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

# Example 1:

# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

#      0          3
#      |          |
#      1 --- 2    4 

# Output: 2
# Example 2:

# Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

#      0           4
#      |           |
#      1 --- 2 --- 3

# Output:  1
# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

def countComponents(self, n, edges):
        
    d = collections.defaultdict(list)
    for x, y in edges:
        d[x].append(y)
        d[y].append(x)
    
    to_visit = set(range(n))
    def dfs(node):
        to_visit.remove(node)
        for i in d[node]:
            if i in to_visit:
                dfs(i)
    
    count = 0
    while to_visit:
        node = next(iter(to_visit))
        dfs(node)
        count += 1
        
    return count + len(to_visit)