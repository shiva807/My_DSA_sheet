# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0
        dq = deque()

        dq.append((root, 0))
        while(dq):
            size = len(dq)
            level_min = dq[0][1]

            for i in range(0, size):
                node, idx = dq.popleft()
                idx -= level_min

                if i==0:
                    first = idx
                if i==size-1:
                    last = idx

                if node.left:
                    dq.append((node.left, 2*idx+1))
                if node.right:
                    dq.append((node.right, 2*idx+2))

            ans = max(ans, last-first+1)
        
        return ans
        
