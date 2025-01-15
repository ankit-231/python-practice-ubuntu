class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                # below gives Node(data) since root.right is None and the first if block of insert method will run
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root: None | Node):
        # External References: https://www.youtube.com/watch?v=f9QXPaLrPnE
        left_height = 0
        right_height = 0

        if root is None:
            return -1
        if root.left is not None:
            left_height = 1 + self.getHeight(root.left)

        if root.right is not None:
            right_height = 1 + self.getHeight(root.right)
        return max(left_height, right_height)


T = int(input())
# T = 7
myTree = Solution()
root = None
for i in range(T):
# for i in [3, 5, 2, 1, 4, 6, 7]:
    data = i
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)
