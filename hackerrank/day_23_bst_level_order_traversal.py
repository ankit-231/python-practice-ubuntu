from collections import deque


class Node:
    def __init__(self, data: int):
        self.right: Node | None = None
        self.left: Node | None = None
        self.data = data


class Solution:
    def insert(self, root: None | Node, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root: None | Node):
        """
        ChatGPT's implementation
        """
        if root is None:
            return
        queue = deque([root])

        while queue:
            current_node = queue.popleft()
            print(current_node.data, end=" ")
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)


T = int(input())
myTree = Solution()
root = None
for i in range(T):
# for i in [3, 5, 4, 7, 2, 1]:
    data = i
    root = myTree.insert(root, data)
myTree.levelOrder(root)
