class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        nodes = []
        nodes.append(root.val)
        for child in root.children:
            nodes.extend(self.preorder(child))
        return nodes
