Given the head of the linked list:

if not head or not head.next:
    return None
cur = head
while cur.next.next:
    cur = cur.next
return cur