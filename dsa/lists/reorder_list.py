from base import ListNode, LinkedList
def find_middle(head) -> ListNode:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def reverse(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

def reorder(head):
    middle = find_middle(head)
    
    second = middle.next
    middle.next = None
    
    new_second = reverse(second)

    first = head 
    second = new_second
    
    while first and second:
        tmp1, tmp2 = first.next, second.next

        first.next = second
        second.next = tmp1
        first = tmp1 
        second = tmp2



