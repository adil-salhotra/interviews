from base import LinkedList, ListNode
from reverse_linked_list import reverse
import random
import pytest
import os


BORDER = os.get_terminal_size().columns * '-'
@pytest.fixture
def generated_input():
    return random.sample(range(30), 4)

def test_repr(generated_input):
    print(f'Original Input:  {generated_input}')
    print(BORDER)
    print("List Representation:")
    print(LinkedList.create_from_iter(generated_input))
    print()

def test_repr_reversed(generated_input):
    print(f'Original Input:  {generated_input}')
    print(BORDER)
    list_repr = LinkedList.create_from_iter(generated_input[::-1])
    print("List Representation on reversed input (<list_object[::-1]>):")
    print(list_repr)
    print("Reverse the reversed input to get the original:")
    print(LinkedList(reverse(list_repr.head)))
    print()

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
    

        
    
    

