class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.dummyhead = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if self.size == 0 or index > self.size - 1:
            return -1
        cur = self.dummyhead.next
        while index:
            cur = cur.next
            index -= 1
        self.printLinkedList()
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.dummyhead.next = ListNode(val, self.dummyhead.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
        else:
            cur = self.dummyhead.next
            while cur.next:
                cur = cur.next
            cur.next = ListNode(val)
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        else:
            cur = self.dummyhead
            while index:
                cur = cur.next
                index -= 1
            cur.next = ListNode(val, cur.next)
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index > self.size - 1:
            return
        else:
            cur = self.dummyhead
            while index:
                cur = cur.next
                index -= 1
            cur.next = cur.next.next
            self.size -= 1

    def printLinkedList(self):
        cur = self.dummyhead.next
        while cur:
            print(cur.val, end="->")
            cur = cur.next
        print("None")

if __name__ == "__main__":
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtTail(2)
    obj.addAtIndex(2,3)
    obj.printLinkedList()
    print(obj.get(3))

    obj.deleteAtIndex(2)
    obj.printLinkedList()
    print(obj.get(2))


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)