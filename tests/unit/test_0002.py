from problems.problem_0002 import ListNode, Solution, listnode2array

sol = Solution()


def test_case_1():

    l1 = ListNode(val=2, next_val=ListNode(val=4, next_val=ListNode(val=3)))
    l2 = ListNode(val=5, next_val=ListNode(val=6, next_val=ListNode(val=4)))
    result = listnode2array(sol.addTwoNumbers(l1, l2))
    assert result == [7, 0, 8]


def test_case_2():
    l1 = ListNode(
        val=9,
        next_val=ListNode(
            val=9,
            next_val=ListNode(
                val=9,
                next_val=ListNode(
                    val=9,
                    next_val=ListNode(
                        val=9, next_val=ListNode(val=9, next_val=ListNode(val=9))
                    ),
                ),
            ),
        ),
    )
    l2 = ListNode(
        val=9,
        next_val=ListNode(val=9, next_val=ListNode(val=9, next_val=ListNode(val=9))),
    )
    result = listnode2array(sol.addTwoNumbers(l1, l2))
    assert result == [8, 9, 9, 9, 0, 0, 0, 1]


def test_case3():
    l1 = ListNode(val=0)
    l2 = ListNode(val=0)
    result = listnode2array(sol.addTwoNumbers(l1, l2))
    assert result == [0]


def test_case4():
    l1 = ListNode(val=0)
    l2 = ListNode()
    result = listnode2array(sol.addTwoNumbers(l1, l2))
    assert result == [0]
