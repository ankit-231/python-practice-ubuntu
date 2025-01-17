class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head: None | Node, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while start.next is not None:
                start = start.next
            start.next = p
        return head

    def display(self, head: None | Node):

        current = head
        while current:
            print(current.data, end=" ")
            current = current.next

    def removeDuplicates(self, head: None | Node):
        elements = []
        while head is not None:
            elements.append(head.data)
            head = head.next
        non_dup = []
        for i in elements:
            if i not in non_dup:
                non_dup.append(i)
        new_head = None
        for j in non_dup:
            new_head = self.insert(new_head, j)
        return new_head


mylist = Solution()
# T = int(input())
head = None

# for i in range(T):
for i in [1, 2, 2, 3, 3, 4]:
    # data = int(input())
    # head = mylist.insert(head, data)
    head = mylist.insert(head, i)
head = mylist.removeDuplicates(head)
mylist.display(head)
