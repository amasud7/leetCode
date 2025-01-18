# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # length = 0
        # curr = head
        # while curr != None:
        #     length += 1
        #     curr = curr.next
        
        # if length == 1:
        #     head = None
        #     return head

        # deleteNodeIndex = length // 2 # this is int division so it rounds down
        # curr = head
        # prev = head
        # for i in range(0, deleteNodeIndex): # plus one because range stops at the index before
        #     prev = curr
        #     curr = curr.next

        # prev.next = curr.next
        # curr.next = None

        # return head
    

        # O(n) solution (this does not pass for when there is only 1 element in the list)
        if head == None: return head

        fast = head
        prev = head
        slow = head

        while fast != None or fast.next != None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        prev.next = slow.next
        slow.next = None

        return head


# shit solution because u go through list twice
# loop through linked list to find length
# divide length by 2 
# go to that node
# and perform delete --> making sure to take care of all links


# O(n) solution where u only go through list once --> uses two pointer method

