class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.front = None

    def get(self, index: int) -> int:
        if not self.front:
            return -1
        if index == 0:
            return self.front.val
        tmp = self.front
        for i in range(index):
            if tmp.next:
                tmp = tmp.next
            else:
                return -1
        return tmp.val


    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.front:
            self.front = new_node
        else:
            new_node.next = self.front
            self.front = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.front:
            self.front = new_node
        else:
            tmp = self.front
            while tmp.next:
                tmp = tmp.next
            tmp.next = new_node 

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = ListNode(val)
        if not self.front:
            if index == 0:
                self.front = new_node
            elif index != 0:
                return
        elif index == 0:
            new_node.next = self.front
            self.front = new_node
        else:
            if index > self.len0x0():
                return
            if index == self.len0x0():
                self.addAtTail(val)
                return
            tmp = self.front
            prev_node = tmp
            for i in range(index):
                if tmp.next:
                    prev_node = tmp
                    tmp = tmp.next
            prev_node.next = new_node
            new_node.next = tmp

    def deleteAtIndex(self, index: int) -> None:
        if not self.front:
            return
        tmp = self.front
        if index == 0:
            if not tmp.next:
                self.front = None

            elif tmp.next:
                del_node = tmp
                tmp = tmp.next
                del_node.next = None
                del del_node
                self.front = tmp
        else:
            prev_node = tmp
            for i in range(index):
                if tmp.next:
                    prev_node = tmp
                    tmp = tmp.next
                else:
                    return
            if not tmp.next:
                prev_node.next = None
                del tmp
            elif tmp.next:
                prev_node.next = tmp.next
                tmp.next = None
                del tmp
        
    def len0x0(self):
        n = 0
        tmp = self.front
        while tmp :
            tmp = tmp.next
            n += 1
        return n



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)