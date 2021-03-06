# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

def merge(intervals):
    if not intervals: return 
        
    intervals = sorted(intervals)
    i = 0
    
    while i < len(intervals) - 1:
        if intervals[i][1] >= intervals[i + 1][0]:
            temp = max(intervals[i + 1][1], intervals[i][1])
            intervals[i] = [intervals[i][0], temp]
            intervals.pop(i + 1)
        else:
            i += 1
    
    return intervals

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    
    stack = []
    for i, j in intervals:
        if not stack or stack[-1][1] < i:
            stack.append([i, j])
        else:
            stack[-1][1] = max(j, stack[-1][1])
    
    return stack