import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None

    nodes = [(node.val, idx) for idx, node in enumerate(lists) if node]
    heapq.heapify(nodes)

    dummy = ListNode()
    current = dummy

    while nodes:
        value, idx = heapq.heappop(nodes)
        current.next = ListNode(value)
        current = current.next
        if lists[idx].next:
            lists[idx] = lists[idx].next
            heapq.heappush(nodes, (lists[idx].val, idx))

    return dummy.next
