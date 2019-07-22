# Elements of Programming Interviews in Python

## 1. Arrays

### Time Complexities
* Retrieval and update - O(1)
* Insertion (with resizing) - O(1)
* Deletion (moving all successive elements to the left) - O(N)
* Slicing - O(k) k is the slice size

### Key Functions
* `bisect.bisect`: find a position in list where an element needs to be inserted to keep the list sorted
```python
import bisect
a = [1,2,3,5]
bisect.bisect(a, 4)
# returns 3
```
* How copy works: <br>
  __shallow copy__: constructing a new collection object and then populating it with references to the child objects found in the original <br>
  __deep copy__: first constructing a new collection object and then recursively populating it with copies of the child objects found in the original
```python
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs) # shallow

xs[1][0] = 'X'
print(ys) # [[1, 2, 3], ['X', 5, 6], [7, 8, 9]]

import copy
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = copy.deepcopy(xs) # deep

print(ys) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
* List comprehension with multiple levels of looping
```python
A = [1,3,5]
B = ['A','B','C']
[(x, y) for x in A for y in B]
```
* (set) `A.issubset(B)` - check if a set is the subset of another

### Tips
* Filing an array from the front is slower than from behind (append)
* Overwritting is more time efficient than deleting

## 2. Strings

### Time Complexities
Strings are immutable
* Concatenating a single character - O(N)

### Key Functions
* `s.strip()`: remove the starting and ending empty spaces
* `s.startswith(prefix)` and `s.endswith(suffix)`
* `s.lower()`
* `s.isalnum()`: check if the string contains only alphanumeric character ('a-z/A-Z')
* `s.count(substring)`: count the number of substrings that exist in the given string

## 3. Linked Lists

### Time Complexities
* Insertion and deletion - O(1)
* Obtaining the kth element - O(N)

### Tips
* Use a _dummy head_ (with null value) to avoid having to check for empty lists
* Algorithms on linked lists usually benefit from using two iterators with one move faster than the other

## 4. Stacks And Queues

Stacks: LIFO (Last in first out)

Queues: FIFO (First in first out)

### Stack: Design A Stack That Includes A Max Operation
* Using heap / BST / Hash Table - time complexity could be reduced to O(logN) / space complexity increases to O(N)
* Using single variable to record the max is very time consuming on popping action
* Improve time complexity by caching (Every insertion records the element as well as the current max)

## 5. Binary Trees

### Traversing
* Inorder traversal (left - root - right)
* Preorder traversal (root - left - right)
* Postorder traversal (left - right - root)
* Morris inorder traversal (inorder traversal with constant space)

Morris inorder traversal
```python
def morrisInorder(root):

    res = []

    while root:
        if not root.left:
            res.append(root.val)
            root = root.right
        else:
            predecessor = find_predecessor(root.left)

            if not predecessor.right:
                predecessor.right = root # link node to remember the sequence
                root = root.left
            else:
                predecessor.right = None
                res.append(root.val)
                root = root.right

    return res

def find_predecessor(root):
    base = root.val
    while root.right and root.right.val < base:
        root = root.right

    return root
```

Iterative Inorder traversal
```python
def inorderTraversal(self, root):
    if not root: return []
    
    stack = [root]
    res = []
    visited = set()
    
    while stack:
        node = stack[-1]
        
        if node.left and node.left not in visited: #check if left child has been visited
            stack.append(node.left)
        else:
            res.append(node.val)
            stack.pop()
            visited.add(node)
            if node.right:
                stack.append(node.right)
                
    return res
```

### Time Complexities
Most tree problems could be solved with recursion, whose time complexity depends on the depth of recursion (O(h) - h is the tree height). Notice this could be translated to `O(logN)` for balanced trees and `O(N)` for skewed trees.

## 6. Heaps

_heap property_: the key at each node is at least as great as the keys stored at its children

### Time Complexities
* Insertion - O(logN)
* Lookup for max/min - O(1)
* Deletion of max/min - O(logN)
* Searching for arbitrary keys - O(N)

### Key Functions
* `heapq.heapify(L)`: transforms the element in L into a heap in-place
* `heapq.nlargest(k, L)` / `heapq.nsmallest(k, L)`: returns k largest/smallest elements in L
* `heapq.heappush(h, e)`: pushes a new element on the heap
* `heapq.heappop(h)`: pops the smallest element from the heap
* `heapq.heappushpop(h, a)`: pushes a on the heap and then pops the smallest element
* `e = h[0]`: returns the smallest element on the heap

### Tips:
* Use a heap when all you care about is the largest or smallest elements (with no need to support fast lookup / search / delete for arbitrary elements)
* A heap is a good choice when you need to compute k largest or k smallest elements

## Tricky Questions

### Finding All Prime Numbers within a Given Limit - Sieve of Eratosthenes
1. Initially, let p equal 2, the smallest prime number.
2. Enumerate the multiples of p by counting in increments of p from 2p to n, and mark them in the list.
3. Find the first number greater than p in the list that is not marked. If there was no such number, stop. Let p equal to that new number. Repeat step 2.
4. When the algorithm terminates, the numbers remaining not marked in the list are all the primes below n.

__e.g. Count the number of prime numbers less than a non-negative number, n.__
```python
def countPrimes(n):
    if n < 2: return 0

    filled = [1] * n
    filled[0] = 0
    filled[1] = 0

    for i in range(2, int(math.sqrt(n)) + 1):
        if filled[i] == 1:
            for j in range(i*i, n, i):
                filled[j] = 0

    return sum(filled)
```

### Greatest Common Divisor of Strings
Input: str1 = "ABCABC", str2 = "ABC"<br>
Output: "ABC"
1. Initially, set str1 to be the longer string and str2 to be the shorter string
2. Check if str2 is the prefix of str1
3. Recursively check for the remainder of str1 and str2

```python
def gcdOfStrings(str1, str2):

    if len(str1) == len(str2):
        return str1 if str1 == str2 else ''
    else:
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        if str1[:len(str2)] == str2:
            return gcdOfStrings(str1[len(str2):], str2)
        else:
            return ''
```