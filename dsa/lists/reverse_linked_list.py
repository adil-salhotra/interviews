from base import ListNode, LinkedList

def reverse(head):
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    return prev
