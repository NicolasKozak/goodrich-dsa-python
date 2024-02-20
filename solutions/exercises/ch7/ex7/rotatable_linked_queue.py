from solutions.vendor.ch07.linked_queue import LinkedQueue as Ch7LinkedQueue
from solutions.vendor.exceptions.empty import Empty

class RotatableLinkedQueue(Ch7LinkedQueue):
    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty')
        if self._size > 1:
            prev_head = self._head
            self._head = self._head._next
            self._tail._next = prev_head
            self._tail = prev_head
            self._tail._next = None
            
