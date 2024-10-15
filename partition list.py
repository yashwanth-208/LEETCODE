# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        node = head
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        temp1 = dummy1
        temp2 = dummy2
        while node:
            if node.val < x:
                temp1.next = ListNode(node.val)
                temp1 = temp1.next
            else:
                temp2.next = ListNode(node.val)
                temp2 = temp2.next
            node = node.next
        temp1 = dummy1
        temp2 = dummy2
        while temp1 and temp1.next:
            temp1 = temp1.next
        while temp2:
            temp1.next = temp2.next
            temp1 = temp1.next
            temp2 = temp2.next
        return dummy1.next