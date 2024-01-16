# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def sum_dfs(node, sum):
            if not node:
                return False

            sum += node.val
            if not node.left and not node.right:
                if sum == targetSum:
                    return True
                return False

            return sum_dfs(node.left, sum) or sum_dfs(node.right, sum)

        return sum_dfs(root, 0)
