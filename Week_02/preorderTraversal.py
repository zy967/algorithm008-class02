class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        nodes = []
        nodes.append(root.val)
        nodes.extend(self.preorderTraversal(root.left))
        nodes.extend(self.preorderTraversal(root.right))
        return nodes
