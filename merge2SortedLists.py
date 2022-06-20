# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        sortedList = ListNode()
        tail = sortedList
        
        while list1 and list2:
            # While list1 and list2 are NOT empty, check which number is higher and append to sortedList
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
            
        # When any ONE of the lists is NULL, the loop ends
        if list1:
            # If list2 is null, append list1 to the sortedList's tail
            tail.next = list1
        else:
            tail.next = list2
        return sortedList.next