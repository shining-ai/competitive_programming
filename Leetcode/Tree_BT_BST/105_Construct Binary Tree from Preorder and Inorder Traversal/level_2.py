# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        def array_to_tree(left, right):
            nonlocal preorder_index
            if left > right:
                return None

            node_value = preorder[preorder_index]
            node = TreeNode(node_value)

            preorder_index += 1

            inorder_index = inorder.index(node_value)
            node.left = array_to_tree(left, inorder_index - 1)
            node.right = array_to_tree(inorder_index + 1, right)

            return node

        preorder_index = 0
        root = array_to_tree(0, len(preorder) - 1)

        return root
