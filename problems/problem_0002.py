"""You are given two non-empty linked lists representing
two non-negative integers.

The digits are stored in reverse order,
and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.
"""


# Definition of singly-linked list.
class ListNode:
    def __init__(self, val=0, next_val=None):
        self.val = val
        self.next_val = next_val


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        remainder = 0

        dummy = ListNode()
        last = dummy

        while True:

            s = l1.val + l2.val + remainder
            s, remainder = s % 10, s // 10

            new_last = ListNode(val=s)

            last.next_val = new_last
            last = new_last

            if l1.next_val is None and l2.next_val is None and remainder == 0:
                break

            if l1.next_val is not None:
                l1 = l1.next_val
            else:
                l1 = ListNode()

            if l2.next_val is not None:
                l2 = l2.next_val
            else:
                l2 = ListNode()

        return dummy.next_val


def listnode2array(l):
    result_array = []
    while True:
        result_array.append(l.val)
        if l.next_val is None:
            break
        l = l.next_val
    return result_array
