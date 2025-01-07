class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=" ")
            current = current.next

    def insert(self, head: None | Node, data: int):
        # Complete this method
        new_node = Node(data)
        last_node = self.get_tail_node(head)

        # last_node is None means LinkedList is empty, so make it the head node
        if last_node is None:
            last_node = new_node
            head = last_node
        else:
            last_node.next = new_node

        return head

    def get_tail_node(self, head: None | Node):

        # if head is None, just return it, cause it's an empty LinkedList
        # Note that you could have done head is None or head.next is None return head but the (head.next is equivalent to what we have done next so no need to check head.next right away)

        if head is None:
            return head

        # Now head is a Node (not None), so let's say current_node = head.
        # Now we start a loop which runs until current_node.next is not None. That means, if current_node does not have a next node, just stop. And we replace current_node with the next node.
        current_node = head
        while current_node.next is not None:
            current_node = current_node.next
            # if current_node.next is None here, the loop will not after this, and we get the last node of the LinkedList
        return current_node

    def get_tail_node_alternative(self, head: None | Node):
        # if head is None, just return it, cause it's an empty LinkedList
        # Note that you could have done head is None or head.next is None return head but the (head.next is equivalent to what we have done next so no need to check head.next right away)

        if head is None:
            return head

        current = head
        while True:
            next_node = current.next
            if next_node is None:
                break  # break out of the loop if next_node is not available
            current = next_node

        return current


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)

# for i in [2, 3, 4, 1]:
#     data = i
#     head = mylist.insert(head, data)

mylist.display(head)
