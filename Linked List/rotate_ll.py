# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        temp = head
        if not head:
            return
        
        while(temp):
            n += 1
            temp = temp.next
        
        temp = head
        while(temp.next):
            temp = temp.next
        temp.next = head

        k = k % n
        n = n-k
        temp = head
        while(n > 1):
            temp = temp.next
            n -= 1
        
        head = temp.next
        temp.next = None

        return head
