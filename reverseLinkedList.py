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
        prev = None
        curr = head

        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

#self.head (head) refers the the pointer pointing to the head of linked list
# use curr, prev, and head pointers
# prev should point at new head of reversed list (currently last node of of list)

# set prev to null
# set curr to head
# while curr != null
# set next to curr.next
# set curr.next to prev
# set prev = curr
# set curr = next

# this is the steps to reverse one link within a linked list --> repeat for the rest of the linked list
