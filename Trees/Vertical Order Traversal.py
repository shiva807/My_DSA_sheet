# Iterative solution (is slow takes 5ms)
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/ 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        q = queue.Queue()
        q.put((root, 0, 0))
        mp = {}
        while(not q.empty()):
            node, line, level = q.get()

            if line not in mp.keys():
                mp[line] = []
            mp[line].append((level, node.val))

            if(node.left):
                q.put((node.left, line-1, level+1))

            if(node.right):
                q.put((node.right, line+1, level+1))

        sorted_mp = dict(sorted(mp.items()))
        for level_val in sorted_mp.values():
            # sort by level first then values
            sorted_level_val = sorted(level_val, key=lambda x: (x[0], x[1]))
            ans.append([val for _, val in sorted_level_val])
        return ans

        


        
