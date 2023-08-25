# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: #type:ignore
        
        if list1 == None and list2 == None:
            return None

        else:
            c1 = list1
            n = 0

            while c1:
                n += 1
                c1 = c1.next
            
            c2 = list2
            m = 0

            while c2:
                m += 1
                c2 = c2.next

            dummy = ListNode() #type:ignore
            new_node = dummy

            i = 0
            j = 0
            
            #while list1 and list2:
            while i < n and j < m:
                if list1.val < list2.val:
                    new_node.next = ListNode(list1.val) #type:ignore
                    #dummy.next = new_node
                    list1 = list1.next
                    i += 1
                else:
                    new_node.next = ListNode(list2.val) #type:ignore
                    #dummy.next = new_node
                    list2 = list2.next
                    j += 1
                new_node = new_node.next

            if list1:
                new_node.next = list1
            if list2:
                new_node.next = list2

            return dummy.next
