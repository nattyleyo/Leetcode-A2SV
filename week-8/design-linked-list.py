class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        
    def get(self, index: int) -> int:
        current = self.head
        if index < 0 or current is None:
            return -1
        for _ in range(index):
            if current.next is None:
                return -1
            current = current.next            
        return current.data

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        new_node = Node(val)
        current = self.head
        for _ in range(index - 1):
            if current is None:
                return
            current = current.next
        if current is None:
            return
        new_node.next = current.next
        current.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        for _ in range(index - 1):
            if current is None:
                return
            current = current.next
        if current is None or current.next is None:
            return
        current.next = current.next.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)