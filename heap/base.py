from typing import Sized
from exceptions import IllegalStateException

class BaseHeap:
    def __init__(self, capacity: int, items: list() = []) -> None:
        self._capacity = capacity 
        self._items = items
        self._size = len(self._items)

    @property
    def size(self) -> int:
        return self._size

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def items(self) -> int:
        return self._items
        
    def increase_capacity(self, new_capacity: int):
        self._capacity = new_capacity
    
    def get_left_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 1


    def get_right_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 2
    

    def get_parent_index(self, child_index: int) -> int:
        return int((child_index - 1)/2)
    

    def has_left_child(self, parent_index: int) -> bool:
        return self.get_left_child_index(parent_index) < self.size


    def has_right_child(self, parent_index: int) -> bool:
        return self.get_right_child_index(parent_index) < self.size
    

    def has_parent(self, index: int) -> bool:
        if index == 0: return False
        return self.get_parent_index(index) >= 0
    

    def left_child(self, index: int) -> int:
        return self._items[self.get_left_child_index(index)]


    def right_child(self, index: int) -> int:
        return self._items[self.get_right_child_index(index)]


    def parent(self, index: int) -> int:
        return self._items[self.get_parent_index(index)]


    def swap(self, index_one: int, index_two: int):
        temp = self._items[index_one]
        self._items[index_one] = self._items[index_two]
        self._items[index_two] = temp
    

    def peek(self) -> int:
        if self.size <= 0: return IllegalStateException(f"Heap is empty or has undefined size.")
        return self._items[0]

class MinHeap(BaseHeap):
    def poll(self) -> int:
        if self.size <= 0: return IllegalStateException(f"Heap is empty or has undefined size.")

        item = self._items[0]  # store the top value of the heap
        self._items[0] = self._items[len(self._items) - 1]  # put the last item at the top
        self._size -= 1 # decrement the size counter
        self.heapify_down() # heapify so the heaps min-heap status is maintained

        return item # return the polled item
    

    def add(self, item: int):
        if self.size == self.capacity: return IllegalStateException(f"Cannot add to the heap as it is at maximum capacity.")

        self._items.append(item)
        self._size += 1

        self.heapify_up()


    def heapify_down(self):
        index = 0
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)

            if self.has_right_child(index) and self.right_child(index) < self.left_child(index):
                smaller_child_index = self.get_right_child_index(index)
            
            if self._items[index] < self._items[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)
            index = smaller_child_index


    def heapify_up(self):
        index = self._size - 1
        while self.has_parent(index) and self.parent(index) >= self._items[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    # This is probably a useless function. You can validate a heap by running heapify on a potentially valid heap and see if the values changed
    def is_valid_min_heap(self):
        index = self._size - 1
        while self.has_parent(index):
            if self.parent(index) > self._items[index]:
                return False
            index -= 1
        return True


class MaxHeap(BaseHeap):
    def poll(self) -> int:
        if self.size <= 0: return IllegalStateException(f"Heap is empty or has undefined size.")

        item = self._items[0]  # store the top value of the heap
        self._items[0] = self._items[len(self._items) - 1]  # put the last item at the top
        self._size -= 1 # decrement the size counter
        self.heapify_down() # heapify so the heaps min-heap status is maintained

        return item # return the polled item
    

    def add(self, item: int):
        if self.size == self.capacity: return IllegalStateException(f"Cannot add to the heap as it is at maximum capacity.")

        self._items.append(item)
        self._size += 1

        self.heapify_up()


    def heapify_down(self):
        index = 0
        while self.has_left_child(index):
            larger_child_index = self.get_left_child_index(index)

            if self.has_right_child(index) and self.right_child(index) > self.left_child(index):
                larger_child_index = self.get_right_child_index(index)
            
            if self._items[index] > self._items[larger_child_index]:
                break
            else:
                self.swap(index, larger_child_index)
            index = larger_child_index


    def heapify_up(self):
        index = self._size - 1
        while self.has_parent(index) and self.parent(index) <= self._items[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)






