# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

# Calling next() will return the next smallest number in the BST.

 

# Example:



# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // return 3
# iterator.next();    // return 7
# iterator.hasNext(); // return true
# iterator.next();    // return 9
# iterator.hasNext(); // return true
# iterator.next();    // return 15
# iterator.hasNext(); // return true
# iterator.next();    // return 20
# iterator.hasNext(); // return false
 

# Note:

# next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
# You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.

class BSTIterator(object):

    def __init__(self, root):
        self.stack = []
        
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        node = self.stack.pop()
        x = node.right
        
        while x:
            self.stack.append(x)
            x = x.left
        
        return node.val
        

    def hasNext(self):
        return len(self.stack) > 0