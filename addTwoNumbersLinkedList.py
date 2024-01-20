class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        added = val1 + val2 + carry
        ans, carry = added % 10, added // 10
        current.next = ListNode(val=ans)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        pass

    return dummy.next
    pass


# Example usage:
# Create sample linked lists
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(9)))

# Merge the lists
result = addTwoNumbers(list1, list2)

# Print the result
while result:
    print(result.val, end=" ")
    result = result.next
