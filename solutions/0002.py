"""You are given two non-empty linked lists representing
two non-negative integers.

The digits are stored in reverse order,
and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        remainder = 0

        dummy = ListNode()
        last = dummy

        while True:

            s = l1.val + l2.val + remainder
            s, remainder = s % 10, s // 10

            new_last = ListNode(val=s)

            last.next = new_last
            last = new_last

            if l1.next is None and l2.next is None and remainder == 0:
                break

            if l1.next is not None:
                l1 = l1.next
            else:
                l1 = ListNode()

            if l2.next is not None:
                l2 = l2.next
            else:
                l2 = ListNode()

        return dummy.next


def listnode2array(l):
    result_array = []
    while True:
        result_array.append(l.val)
        if l.next is None:
            break
        else:
            l = l.next
    return result_array


if __name__ == "__main__":

    sol = Solution()

    l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3)))
    l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))
    result = listnode2array(sol.addTwoNumbers(l1, l2))
    assert result == [7, 0, 8]

    l1 = ListNode(
        val=9,
        next=ListNode(
            val=9,
            next=ListNode(
                val=9,
                next=ListNode(
                    val=9,
                    next=ListNode(val=9,
                                  next=ListNode(val=9, next=ListNode(val=9))
                                  ),
                ),
            ),
        ),
    )
    l2 = ListNode(
        val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9)))
    )
    result = listnode2array(sol.addTwoNumbers(l1, l2))
    assert result == [8, 9, 9, 9, 0, 0, 0, 1]

    l1 = ListNode(val=0)
    l2 = ListNode(val=0)
    result = listnode2array(sol.addTwoNumbers(l1, l2))
    assert result == [0]

    l1 = ListNode(val=0)
    l2 = ListNode()
    result = listnode2array(sol.addTwoNumbers(l1, l2))
    assert result == [0]
