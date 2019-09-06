# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

# Define a pair (u,v) which consists of one element from the first array and one element from the second array.

# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

# Example 1:

# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]] 
# Explanation: The first 3 pairs are returned from the sequence: 
#              [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# Example 2:

# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [1,1],[1,1]
# Explanation: The first 2 pairs are returned from the sequence: 
#              [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# Example 3:

# Input: nums1 = [1,2], nums2 = [3], k = 3
# Output: [1,3],[2,3]
# Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

def kSmallestPairs(self, nums1, nums2, k):
    if not nums1 or not nums2: return []
    
    i = j = 0
    l1, l2 = len(nums1), len(nums2)
    stack = [[nums1[i] + nums2[j], (i, j)]]
    seen = set([(i, j)])
    res = []
    
    while len(res) < k and stack:
        _, (n0, n1) = heapq.heappop(stack)
        res.append([nums1[n0], nums2[n1]])
        
        if n0 < l1 - 1 and (n0 + 1, n1) not in seen:
            heapq.heappush(stack, [nums1[n0 + 1] + nums2[n1], (n0 + 1, n1)])
            seen.add((n0 + 1, n1))
        if n1 < l2 - 1 and (n0, n1 + 1) not in seen:
            heapq.heappush(stack, [nums1[n0] + nums2[n1 + 1], (n0, n1 + 1)])
            seen.add((n0, n1 + 1))
            
    return res