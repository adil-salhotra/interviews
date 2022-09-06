from base import ListNode, LinkedList
def remove(head, n):
    dummy = ListNode()
    dummy.next = head
    
    left = dummy
    right = head

    for _ in range(n):
        right = right.next
    
    while right:
        left = left.next
        right = right.next
    
    left.next = left.next.next
    return dummy.next