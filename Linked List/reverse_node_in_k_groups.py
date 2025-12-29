# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return 
        
        count = 0 #count nodes
        temp = head
        while(temp):
            count+= 1
            temp = temp.next

        dummy = ListNode()
        dummy.next = head
        prev = dummy

        while(count >= k):
            curr = prev.next
            later = curr.next
            temp_k = k
            while(temp_k > 1):
                curr.next = later.next
                later.next = prev.next
                prev.next = later
                later = curr.next
                temp_k -= 1
            prev = curr
            count-= k

        return dummy.next
