# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def traverse(self, preorder: List[int], inorder: List[int]):

        node = TreeNode(preorder[0])

        if len(preorder) == 1:
            return node

        inorder_pos = None

        for i in range(len(inorder)):
            if inorder[i] == node.val:
                inorder_pos = i
                break
            
        if i > 0:
            node.left = self.traverse(preorder[1:i+1], inorder[:i])

        if i+1 < len(preorder):
            node.right = self.traverse(preorder[i+1:], inorder[i+1:])

        return node
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        return self.traverse(preorder, inorder)
        