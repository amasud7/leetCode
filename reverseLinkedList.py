# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

#self.head (head) refers the the pointer pointing to the head of linked list
# use curr, prev, and head pointers
# prev should point at new head of reversed list (currently last node of of list)

        