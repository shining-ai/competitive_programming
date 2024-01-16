# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = collections.deque()
        queue.append((root, 0))

        while queue:
            node, level = queue.popleft()
            if not node:
                continue

            if len(ans) - 1 < level:
                ans.append([])

            ans[level].append(node.val)
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

        for i in range(len(ans)):
            if i % 2 != 0:
                ans[i].reverse()
        return ans
