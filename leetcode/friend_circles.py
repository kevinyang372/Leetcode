# There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

# Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

# Example 1:
# Input: 
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
# The 2nd student himself is in a friend circle. So return 2.
# Example 2:
# Input: 
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
# so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
# Note:
# N is in range [1,200].
# M[i][i] = 1 for all students.
# If M[i][j] = 1, then M[j][i] = 1.

def findCircleNum(self, M):
        
    students = set(range(len(M)))
    d = collections.defaultdict(list)
    count = 0
    
    for i in range(len(M)):
        for t in range(i + 1, len(M)):
            if M[i][t] == 1:
                d[i].append(t)
                d[t].append(i)
                
    while students:
        beginning = next(iter(students))
        visited = set([beginning])
        stack = [beginning]
        
        while stack:
            node = stack.pop()
            
            for i in d[node]:
                if i not in visited:
                    stack.append(i)
                    visited.add(i)
            
        count += 1
        students -= visited
        
    return count

# union find
class DSU:
    def __init__(self):
        self.p = [i for i in range(201)]
        
    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        self.p[self.find(x)] = self.p[y]


class Solution(object):
    def findCircleNum(self, M):
        
        dsu = DSU()
        for i in range(len(M) - 1):
            for j in range(i + 1, len(M)):
                if M[i][j] == 1 and dsu.find(i) != dsu.find(j):
                    dsu.union(i, j)
        
        visited = set()
        for i in range(len(M)):
            visited.add(dsu.find(i))
            
        return len(visited)