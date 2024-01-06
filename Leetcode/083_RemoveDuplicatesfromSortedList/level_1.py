class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteDuplicates(head):
    if head == None:
        return None

    node_seen = set()
    node_seen.add(head.val)
    curr = head

    while curr.next != None:
        if curr.next.val in node_seen:
            curr.next = curr.next.next
        else:
            curr = curr.next
            node_seen.add(curr.val)

    return head


if __name__ == "__main__":
    l = [1, 1, 2]

    dummy_head = ListNode(0)
    curr = dummy_head
    for i in l:
        node = ListNode(i)
        curr.next = node
        curr = node

    ans = deleteDuplicates(dummy_head.next)

    while ans != None:
        print(ans.val)
        ans = ans.next
