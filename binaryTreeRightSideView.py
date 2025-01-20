# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        # edge case
        if not root:
            return []
        
        # create ans list
        ans = []

        # create q
        q = [root]

        while q:
            ans.append(q[-1].val)

            for i in range(len(q)):
                current = q.pop(0)

                if current.left:
                    q.append(current.left)
                
                if current.right:
                    q.append(current.right)
                
        return ans