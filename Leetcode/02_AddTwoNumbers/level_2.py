class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def AddTwoNumbers(l1, l2):
    dummy_head = ListNode(0)
    carry = 0
    curr = dummy_head

    while l1 or l2 or carry:
        l1_val = 0
        if l1:
            l1_val = l1.val
            l1 = l1.next

        l2_val = 0
        if l2:
            l2_val = l2.val
            l2 = l2.next

        column_sum = l1_val + l2_val + carry
        carry, new_val = divmod(column_sum, 10)
        curr.next = ListNode(new_val)
        curr = curr.next

    return dummy_head.next


if __name__ == "__main__":
    l1_1 = ListNode(3)
    l1_2 = ListNode(4, l1_1)
    l1_3 = ListNode(2, l1_2)
    l1 = l1_3

    l2_1 = ListNode(4)
    l2_2 = ListNode(6, l2_1)
    l2_3 = ListNode(5, l2_2)
    l2 = l2_3
