# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        val = []
        self.in_order(root,val)
        return val
    
    def in_order(self,node,val):
        if node:
            self.in_order(node.left,val)
            val.append(node.val)
            self.in_order(node.right,val)


        
        