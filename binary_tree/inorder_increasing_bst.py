# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        inorder_traversal = []
        def inorder(root):  #gets a sorted array of nodes
            if root:
                inorder(root.left)
                inorder_traversal.append(root)
                inorder(root.right)
        inorder(root)

        for i in range(len(inorder_traversal)-1):  #pointing node.right to next nodes in increasing order
            inorder_traversal[i].left = None
            inorder_traversal[i].right = inorder_traversal[i+1]
        inorder_traversal[-1].left = None  #making last node point to none, otherwise causes cycle

        return inorder_traversal[0]
