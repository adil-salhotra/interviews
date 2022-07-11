class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        return f"{self.val}"
    

class LinkedList:
    def __init__(self, head):
        if isinstance(head, ListNode):
            self.head = head
        else:
            self.head = ListNode(head)
        
    @classmethod
    def create_from_iter(cls, values=list()) -> ListNode:
        dummy = ListNode()
        curr = dummy

        for value in values:
            curr.next = ListNode(value)
            curr = curr.next

        return cls(dummy.next)
            

    def __repr__(self) -> str:
        curr = self.head
        s = ''
        while curr:
            if curr.next:
                s += f"{curr} -> "
                
            else:
                s += f"{curr}"

            curr = curr.next
            
        return s