class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        nodes = []
        nodes.extend(self.inorderTraversal(root.left))
        nodes.append(root.val)
        nodes.extend(self.inorderTraversal(root.right))
        return nodes
