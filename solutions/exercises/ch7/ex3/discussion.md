This solution runs in O(n) time and uses O(N) space.
An iterative solution would require instead O(1) space.
Given the head of a singly linked list L:

def count_nodes(L):
    if not L:
        return 0
    return 1 + count_nodes(L.next)
