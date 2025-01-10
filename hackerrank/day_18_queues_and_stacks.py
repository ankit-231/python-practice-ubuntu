# MY SOLUTION
class Solution:
    stack = None
    queue = None

    # Write your code here
    def pushCharacter(self, char: str):
        if self.stack is None:
            self.stack = []
        self.stack.append(char)

    def enqueueCharacter(self, char: str):
        if self.queue is None:
            self.queue = []
        self.queue.insert(0, char)

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        return self.queue.pop(0)


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
"""
pop the top character from stack
dequeue the first character from queue
compare both the characters
"""
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")

# CHATGPT's SOLUTION

# Queue is First In First Out
# Stack is Last In First Out

from collections import deque


class SolutionGPT:
    def __init__(self):
        self.stack = []
        self.queue = deque()

    def pushCharacter(self, char: str):
        self.stack.append(char)

    def enqueueCharacter(self, char: str):
        self.queue.append(char)

    def popCharacter(self):
        return self.stack.pop(0)

    def dequeueCharacter(self):
        return self.queue.popleft()
