class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    # Helper function to reverse a portion of the list
    def reverse_list(node, k) -> tuple[ListNode, ListNode, ListNode]:
        prev, curr, tail = None, node, node
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev, node, curr

    # If there are less than k nodes, return the original list
    node_count = 0
    current_node = head
    while current_node:
        node_count += 1
        current_node = current_node.next
    if node_count < k or k == 1:
        return head

    new_head, current_tail, new_current = reverse_list(head, k)
    while node_count - k >= k:
        next_tail = new_current
        reversed_head, reversed_tail, next_current = reverse_list(
            new_current, k)
        current_tail.next = reversed_head
        current_tail = reversed_tail
        new_current = next_current
        node_count -= k

    # Connect the remaining nodes
    current_tail.next = new_current
    return new_head
