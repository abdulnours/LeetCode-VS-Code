# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Given heads of:
        # list1
        # list2   (both are sorted Linked lists)

        # Merge both into a Sorted Linked list
        # Return the head of the merged linked list

        # STRAT:
        # - compare list1[0] with list2[0]
        # - compare larger node with next node in smaller list
        # - reiterate

        result = []
        i = 0
        j = 0
        
        while i < list1.size() and j < list2.size():
            if list1[i] < list2[j]:
                result.next(list1[i])
                i += 1
            else:
                result.next(list2[j])
                j += 1

        return result
    
    def size(self):
        '''
        CONVINIENCE METHOD: no added functionality, only makes info more accessible
        Returns the number of nodes in the list 
        Takes Linear O(n) time
        '''

        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count
