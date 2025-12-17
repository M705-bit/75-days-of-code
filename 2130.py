# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self,head: Optional[ListNode]) -> int:
        current = head
        tam = 0
        array = soma = []
        while current:
            array.append(current.val)
            current = current.next
            tam+=1
        for i in range(0,tam):
            if (0 <= i <= int(tam/2)-1):
                soma.append(array[i] + array[tam-1-i])
        return max(array)
            
        
