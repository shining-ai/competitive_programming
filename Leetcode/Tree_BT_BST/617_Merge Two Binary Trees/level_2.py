class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve_1(root1, root2):
    def add_dfs(node_1, node_2):
        if node_1 is None:
            return node_2
        if node_2 is None:
            return node_1

        node_1.val += node_2.val
        node_1.left = add_dfs(node_1.left, node_2.left)
        node_1.right = add_dfs(node_1.right, node_2.right)

        return node_1

    return add_dfs(root1, root2)


if __name__ == "__main__":
    # list_1 = [1, 3, 2, 5]
    # list_2 = [2, 1, 3, null, 4, null, 7]
    root_1 = TreeNode(1)
    root_1.left = TreeNode(3)
    root_1.right = TreeNode(2)
    root_1.left.left = TreeNode(5)

    root_2 = TreeNode(2)
    root_2.left = TreeNode(1)
    root_2.right = TreeNode(3)
    root_2.left.right = TreeNode(4)
    root_2.right.right = TreeNode(7)

    print(solve_1(root_1, root_2))
