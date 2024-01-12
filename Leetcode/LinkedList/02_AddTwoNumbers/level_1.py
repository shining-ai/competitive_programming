import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l1_1 = ListNode(3)
l1_2 = ListNode(4, l1_1)
l1_3 = ListNode(2, l1_2)
l1 = l1_3

l2_1 = ListNode(4)
l2_2 = ListNode(6, l2_1)
l2_3 = ListNode(5, l2_2)
l2 = l2_3

q_l1 = collections.deque()
q_l2 = collections.deque()


while l1:
    q_l1.append(l1.val)
    l1 = l1.next

while l2:
    q_l2.append(l2.val)
    l2 = l2.next


carry = 0
dummy_head = ListNode(0)
curr = dummy_head

while q_l1 or q_l2 or carry:
    if q_l1:
        l1_val = q_l1.popleft()
    else:
        l1_val = 0

    if q_l2:
        l2_val = q_l2.popleft()
    else:
        l2_val = 0

    tmp = l1_val + l2_val + carry
    carry = tmp // 10

    new_node = ListNode(tmp % 10)
    curr.next = new_node
    curr = new_node

print(vars(dummy_head.next))
