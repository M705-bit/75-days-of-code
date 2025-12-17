#Odd Even Linked List
from typing import Optional, Annotated

class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        return head
        
#criando uma instância da classe Solution
head = ListNode(0)
current = head
for i in range(1,5):
    current.next = ListNode(i) 
    current = current.next

result = Solution().oddEvenList(head)
current = result
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

