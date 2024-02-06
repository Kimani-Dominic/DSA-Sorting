#Linked lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val):
        while head and head.val == val:
            head = head.next

        current = head
        prev = None

# Traverse the linked list and remove nodes with the given value
        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next

        return head

# Example usage:
# Create a linked list: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))

# Create an instance of the Solution class
solution_instance = Solution()

# Call the removeElements method to remove nodes with value 6
new_head = solution_instance.removeElements(head, 6)

# Print the updated linked list
while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next
