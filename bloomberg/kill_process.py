# Given n processes, each process has a unique PID (process id) and its PPID (parent process id).

# Each process only has one parent process, but may have one or more children processes. This is just like a tree structure. Only one process has PPID that is 0, which means this process has no parent process. All the PIDs will be distinct positive integers.

# We use two list of integers to represent a list of processes, where the first list contains PID for each process and the second list contains the corresponding PPID.

# Now given the two lists, and a PID representing a process you want to kill, return a list of PIDs of processes that will be killed in the end. You should assume that when a process is killed, all its children processes will be killed. No order is required for the final answer.

# Example 1:
# Input: 
# pid =  [1, 3, 10, 5]
# ppid = [3, 0, 5, 3]
# kill = 5
# Output: [5,10]
# Explanation: 
#            3
#          /   \
#         1     5
#              /
#             10
# Kill 5 will also kill 10.
# Note:
# The given kill id is guaranteed to be one of the given PIDs.
# n >= 1.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

def killProcess(pid, ppid, kill):

    d = {}
    for x, y in zip(pid, ppid):
        if x not in d:
            d[x] = TreeNode(x)
        if y not in d:
            d[y] = TreeNode(y)
        d[y].children.append(x)

    res = []
    stack = [kill]

    while stack:
        node = stack.pop()
        res.append(node)

        stack += d[node].children

    return res

# Union Find
class DSU:
    def __init__(self):
        self.p = [i for i in range(100001)]
    
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        self.p[self.find(x)] = self.p[y]

class Solution(object):
    def killProcess(self, pid, ppid, kill):
        
        dsu = DSU()
        
        for x, y in zip(pid, ppid):
            if x == kill or y == 0:
                continue
            else:
                dsu.union(x, y)
                
        res = []
        for i in pid:
            if dsu.find(i) == kill:
                res.append(i)
        
        return res 

