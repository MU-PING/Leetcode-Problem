class ListNode(object):
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
            
class Solution(object):
        def addTwoNumbers(self, l1, l2):
            """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
            """
            linklist=ListNode(0)
            ptr=linklist #linklist的指標

            quotient=0 #進位
            while  l1 or l2 or quotient:
                val1 = l1.val if l1 else 0
                val2 = l2.val if l2 else 0
                l1 = l1.next if l1 else None #l1下移
                l2 = l2.next if l2 else None #l2下移
                quotient, remainder = divmod (val1 + val2 + quotient, 10)

                ptr.next=ListNode(remainder)
                ptr=ptr.next #answer指針下移

            return linklist.next