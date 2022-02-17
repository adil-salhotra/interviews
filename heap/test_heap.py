import pytest
import heapq
import random

from base import MinHeap, MaxHeap
from exceptions import IllegalStateException

@pytest.fixture
def lib_heap():
    x = [random.randrange(1, 50, 1) for _ in range(10)]
    heapq.heapify(x)
    yield x

def test_heap_add_correctness():
    input_list = [random.randrange(1, 50, 1) for _ in range(10)]
    actual_heap = MinHeap(capacity=len(input_list))
    lib_heap = list()

    for item in input_list:
        actual_heap.add(item)
        heapq.heappush(lib_heap,item)
    
    assert lib_heap == actual_heap.items


def test_heap_peek(lib_heap):
    actual_heap = MinHeap(capacity=len(lib_heap), items=list(lib_heap))
    assert actual_heap.peek() == lib_heap[0]


def test_heap_poll(lib_heap):
    actual_heap = MinHeap(capacity=len(lib_heap), items=list(lib_heap))
    assert actual_heap.poll() == heapq.heappop(lib_heap)


def test_is_valid_heap(lib_heap):
    actual_heap = MinHeap(capacity=len(lib_heap), items=list(lib_heap))
    assert actual_heap.is_valid_min_heap()

def test_heap_add_when_over_capacity(lib_heap):
    actual_heap = MinHeap(capacity=len(lib_heap), items=list(lib_heap))
    try:
        actual_heap.add(3)
    except IllegalStateException:
        pass

def test_increase_capacity(lib_heap):
    actual_heap = MinHeap(capacity=len(lib_heap), items=list(lib_heap))
    actual_heap.increase_capacity(actual_heap.capacity + 1)
    assert actual_heap.capacity == len(lib_heap) + 1

# TODO: Add Max Heap Tests




    


