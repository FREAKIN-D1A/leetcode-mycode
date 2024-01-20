class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        pass

def mergeTwoLists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy.next

# Example usage:
# Create sample linked lists
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

# Merge the lists
result = mergeTwoLists(list1, list2)

# Print the result
while result:
    print(result.val, end=" ")
    result = result.next
