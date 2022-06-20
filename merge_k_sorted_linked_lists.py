# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        while len(lists)>1:
            #Create an empty merged list initially that stores sorted lists pairs
            merged = []
            for i in range(0, len(lists), 2):
                # Iteration is 2 because we want to merge two lists at a time, list1 and list2
                list1 = lists[i]
                list2 = lists[i+1] if (i+1)<len(lists) else None #check if there are odd number of lists
                merged.append(self.merge(list1, list2)) # add two merged lists as one in merged
            lists = merged # keep changing lists to merged and repeat the steps until one element remains in lists
        return lists[0] # return first element of lists finally
                
                
    def merge(self, list1, list2):
        # A function that merges two lists, refer leetcode 21
        sortedList = ListNode()
        tail = sortedList
        while list1 and list2:
            if list1.val<list2.val:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return sortedList.next