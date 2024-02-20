First, we go through the successors of x to find if y is among them.
In that case, we set the successor of the original predecessor of y to be x.
Likewise, we set the successor of the original predecessor of x to be y, assuming we have access to the head of L.
This algorithm will have O(n) time complexity.

In the case of a doubly linked list, it is easier since we can access the predecessor of a node directly,
and thus we don't need to iterate through the list to swap two nodes and the algorithm runs in O(1) time.

