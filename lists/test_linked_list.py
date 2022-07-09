from base import LinkedList, ListNode
from reverse_linked_list import reverse
import random
import pytest

@pytest.fixture
def generated_input():
    return random.sample(range(30), 4)

def test_0(generated_input):
    list_0 = LinkedList.create_from_iter(generated_input)
    curr = list_0.head
    for value in generated_input:
        assert value == curr.val
        curr = curr.next

    

    reversed_head = reverse(list_0.head)
    list_1 = LinkedList(reversed_head)
    curr = list_1.head
    for value in generated_input[::-1]:
        assert value == curr.val
        curr = curr.next

def test_1(generated_input):
    list_0 = LinkedList.create_from_iter(generated_input)
    list_0_reversed = LinkedList.create_from_iter(generated_input[::-1])

    curr = list_0.head
    for value in generated_input:
        assert value == curr.val
        curr = curr.next
    
    curr_reversed = list_0_reversed.head
    for value in generated_input[::-1]:
        assert value == curr_reversed.val
        curr_reversed = curr_reversed.next
    

        
    
    

