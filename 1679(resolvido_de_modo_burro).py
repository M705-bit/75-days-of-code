class Node:
    def __init__(self,value):
        self.data= value
        self.prev = None
        self.next = None
class LinkedList:
    def __init__(self):
        self.list = []
        self.head = None
        self.tail = None
    def add_node(self,value):
        node = Node(value)
        if self.head == None:
            self.head = node
            return
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
            current_node.next.prev = current_node

    def delete_node(self,value):
        if self.head is None:
              return
        current_node = self.head
        while current_node is not None:
            if current_node.data == value:
                #se for o head o current_node.prev é None
                if current_node.prev is None:
                    self.head = current_node.next
                    if self.head is not None:
                        self.head.prev = None
                #se não for o head
                else:
                    if current_node.next is not None:
                        current_node.prev.next = current_node.next
                        current_node.next.prev = current_node.prev
                    else:
                        current_node.prev.next = None
                break
            
            current_node = current_node.next

    def return_list(self):
        self.list = []
        current = self.head
        while current:
            self.list.append(current.data)
            current = current.next
        return self.list
    
class Solution:
    
    def maxOperations(self, nums: list[int], k: int) -> int:
        '''
        lista_encadeada = LinkedList()
        count =0
        for i in range(0,len(nums)):
            lista_encadeada.add_node(nums[i])
        lista=lista_encadeada.return_list()
        for i in range(0, len(lista)):
            for j in range(i+1, len(lista)):
                if (lista[i]+lista[j]) == k:
                    count+=1
                    lista_encadeada.delete_node(lista[i])
                    lista_encadeada.delete_node(lista[j])
                    lista=lista_encadeada.return_list()
        print(count)
        '''
        lista_encadeada = LinkedList()
        for num in nums:
            lista_encadeada.add_node(num)

        count = 0
        current_i = lista_encadeada.head

        while current_i is not None:
            current_j = current_i.next
            while current_j is not None:
                if current_i.data + current_j.data == k:
                    count += 1
                    # Salva os próximos antes de deletar
                    next_i = current_i.next
                    next_j = current_j.next
                    lista_encadeada.delete_node(current_i.data)
                    lista_encadeada.delete_node(current_j.data)
                    current_i = lista_encadeada.head  # Reinicia a busca
                    break
                current_j = current_j.next
            else:
                current_i = current_i.next

        return count


solucao = Solution()
k = int(input("entre com um valor para k: "))
if not (1 <= k <= 10**9):
    raise ValueError("O valor de k deve estar entre 1 e 10^9")

lista = list(map(int, input("entre com uma lista: ").split(",")))
if not (1 <= len(lista) <= 10**5):
    raise ValueError("O tamanho da lista deve estar entre 1 e 10^5")

for num in lista:
    if not (1 <= num <= 10**9):
        raise ValueError("Cada número da lista deve estar entre 1 e 10^9")
    
#lista = list(map(int, input("entre com uma lista: ").split(",")))
solucao.maxOperations(lista,k)



