"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = [root]
        while q:
            next_level = []
            for i in range(len(q)):
                if i < len(q) - 1:
                    q[i].next = q[i+1]
                if q[i].left:
                    next_level.append(q[i].left)
                if q[i].right:
                    next_level.append(q[i].right)
            q = next_level
        return root
