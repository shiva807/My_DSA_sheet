"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    
    def Paths(self, root):
        ans = []

        def helper(root, path):
        
            if not root:
                return
        
            path.append(root.data)
            if not root.left and not root.right:
                ans.append(path[:])
            else:
                helper(root.left, path)
                helper(root.right, path)
            
            path.pop()
        
        
        helper(root, [])
        
        return ans
