# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = defaultdict(int)
        while head:
            visited[head] += 1
            head = head.next
            if 2 in visited.values():
                return True
        else:
            return False
