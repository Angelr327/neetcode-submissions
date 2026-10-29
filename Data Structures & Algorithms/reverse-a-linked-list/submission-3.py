# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        rev_list = []
        while curr:
            rev_list.append(curr)
            curr = curr.next

        if not rev_list:
            return None

        rev_list.reverse()

        for i in range(len(rev_list) - 1):
            rev_list[i].next = rev_list[i + 1]
        
        rev_list[-1].next = None

        return rev_list[0]

        

            
