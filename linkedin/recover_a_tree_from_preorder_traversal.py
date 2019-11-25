# We run a preorder depth first search on the root of a binary tree.

# At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  (If the depth of a node is D, the depth of its immediate child is D+1.  The depth of the root node is 0.)

# If a node has only one child, that child is guaranteed to be the left child.

# Given the output S of this traversal, recover the tree and return its root.

 

# Example 1:



# Input: "1-2--3--4-5--6--7"
# Output: [1,2,5,3,4,6,7]
# Example 2:



# Input: "1-2--3---4-5--6---7"
# Output: [1,2,5,3,null,6,null,4,null,7]
 

# Example 3:



# Input: "1-401--349---90--88"
# Output: [1,401,null,349,88,90]
 

# Note:

# The number of nodes in the original tree is between 1 and 1000.
# Each node will have a value between 1 and 10^9.

def recoverFromPreorder(self, S: str) -> TreeNode:
    
    stack = []
    level, node = 0, ''
    root = None
    
    for i in range(len(S) + 1):
        if i == len(S) or S[i] == '-':
            if node != '':
                cur = TreeNode(int(node))
                
                while stack and stack[-1][1] > level - 1:
                    stack.pop()
                    
                if stack and not stack[-1][0].left:
                    stack[-1][0].left = cur
                elif stack:
                    stack[-1][0].right = cur
                    stack.pop()
                else:
                    root = cur
                
                stack.append([cur, level])
                node = ''
                level = 0
            level += 1
        else:
            node += S[i]
    
    return root