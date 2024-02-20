Given the head of L and the head of M:

dummy = ListNode(-1)
cur = dummy

while L:
    cur.next = ListNode(L.val)
    cur = cur.next
    L = L.next

while M:
    cur.next = ListNode(L.val)
    cur = cur.next
    M = M.next

return dummy.next

####

Instead, if the original list L should be modified in place:

if not L:
    return M

if not M:
    return L

cur = L
while cur.next:
    cur = cur.next
cur.next = M

return L
    