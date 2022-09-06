from base import LinkedList, ListNode
from reverse_linked_list import reverse
from remove_nth_node_from_end import remove
from reorder_list import find_middle
import random
import pytest
import os

"""
TO RUN THIS FILE USING PYTEST:
pytest -s -k linked_list
in the terminal.
"""


BORDER = os.get_terminal_size().columns * '-'
@pytest.fixture
def generated_input():
    return random.sample(range(30), 4)

def test_repr(generated_input):
    print()
    print("TEST STRING REPRESENTATION 1")
    print(BORDER)
    print(f'Original Input:  {generated_input}')
    print("List Representation:")
    print(LinkedList.create_from_iter(generated_input))
    print()

def test_repr_reversed(generated_input):
    print()
    print("TEST STRING REPRESENTATION 2")
    print(BORDER)
    print(f'Original Input:  {generated_input}')
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

def test_remove_second_from_end(generated_input):
    print()
    print("TEST REMOVE SECOND FROM LAST")
    print(BORDER)
    print(f'Original Input:  {generated_input}')
    list_0 = LinkedList.create_from_iter(generated_input)
    print()
    print(list_0)
    new_list_head = remove(list_0.head, 2)
    print()
    list_1 = LinkedList(new_list_head)
    print(list_1)

def test_remove_last(generated_input):
    print()
    print("TEST REMOVE LAST")
    print(BORDER)
    print(f'Original Input:  {generated_input}')

    list_0 = LinkedList.create_from_iter(generated_input)
    print()
    print(list_0)
    new_list_head = remove(list_0.head, 1)
    print()
    list_1 = LinkedList(new_list_head)
    print(list_1)

def test_remove_first(generated_input):
    print()
    print("TEST REMOVE FIRST")
    print(BORDER)
    print(f'Original Input:  {generated_input}')

    list_0 = LinkedList.create_from_iter(generated_input)
    print()
    print(list_0)
    new_list_head = remove(list_0.head, 4)
    print()
    list_1 = LinkedList(new_list_head)
    print(list_1)

def test_find_middle(generated_input):
    list_0 = LinkedList.create_from_iter(generated_input)
    middle = find_middle(list_0.head)
    assert middle.val == generated_input[len(generated_input) // 2]



        
    
    

