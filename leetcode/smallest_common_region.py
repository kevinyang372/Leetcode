# You are given some lists of regions where the first region of each list includes all other regions in that list.

# Naturally, if a region X contains another region Y then X is bigger than Y.

# Given two regions region1, region2, find out the smallest region that contains both of them.

# If you are given regions r1, r2 and r3 such that r1 includes r3, it is guaranteed there is no r2 such that r2 includes r3.

# It's guaranteed the smallest region exists.

 

# Example 1:

# Input:
# regions = [["Earth","North America","South America"],
# ["North America","United States","Canada"],
# ["United States","New York","Boston"],
# ["Canada","Ontario","Quebec"],
# ["South America","Brazil"]],
# region1 = "Quebec",
# region2 = "New York"
# Output: "North America"
 

# Constraints:

# 2 <= regions.length <= 10^4
# region1 != region2
# All strings consist of English letters and spaces with at most 20 letters.

def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        
    graph = collections.defaultdict(set)
    indegree = collections.Counter()
    nodes = set()
    
    for i in regions:
        nodes.add(i[0])
        for t in range(1, len(i)):
            graph[i[0]].add(i[t])
            indegree[i[t]] += 1
            nodes.add(i[t])
            
    root = [i for i in nodes if indegree[i] == 0]
    cache = collections.defaultdict(bool)
            
    def traverse(node):
        
        r1, r2 = node == region1, node == region2
        for i in graph[node]:
            t1 = isin(i, region1)
            t2 = isin(i, region2)
            
            if t1 and t2:
                return traverse(i)
            elif t1:
                r1 = t1
            elif t2:
                r2 = t2
        
        if r1 and r2:
            return node
        
        return None
            
    def isin(node, region):
        if node == region or region in graph[node]: return True
        if (node, region) in cache: return cache[node, region]
        res = any(isin(i, region) for i in graph[node])
        cache[node, region] = res
        return res
      
    for n in root:
        t = traverse(n)
        if t: return t