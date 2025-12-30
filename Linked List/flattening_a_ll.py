'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    
    def merge_lists(self, l1, l2):
        
        result = Node(0)
        merged = result
        
        while(l1 and l2):
            if(l1.data <= l2.data):
                result.bottom = l1
                result = result.bottom
                l1 = l1.bottom
            else:
                result.bottom = l2
                result = result.bottom
                l2 = l2.bottom
                
        if l1:
            result.bottom = l1
        else:
            result.bottom = l2

        return merged.bottom
                
    
    def flatten(self, root):
        # code here
        head = root
        if not root.next:
            return root
        
        l2 = self.flatten(root.next)
        merged = self.merge_lists(root, l2)
        
        return merged
