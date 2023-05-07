class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        temp = self.head
        new_node.next = self.head
        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node

    def delete(self, val):
        current_node = self.head
        prev_node = None
        while current_node:
            if current_node.data == val and current_node == self.head:
                #case 1 - head is the only element in clist
                if current_node.next == self.head:
                    current_node = None
                    self.head = None
                    return
                #case 2 - more elements in the list
                else:
                    #traverse and update head, delete head
                    while current_node.next != self.head:
                        current_node = current_node.next
                    current_node.next = self.head.next
                    self.head = self.head.next
                    current_node = None
                    return
            elif current_node.data == val:
                prev_node.next = current_node.next
                current_node = None
                return
            else:
                if current_node.next == self.head:
                    return

            prev_node = current_node
            current_node = current_node.next

    def countnodes(self):
        current_node = self.head
        self.count = 1
        while current_node.next != self.head:
            self.count += 1
            current_node = current_node.next
        return self.count
    
    def toCircular(self, head):
        start = head
        while head.next is not None:
            head = head.next
        head.next = start
        return

    def printlist(self):
        temp = self.head
        if self.head is not None:
            while True:
                print(temp.data)
                temp = temp.next
                if temp == self.head:
                    break
        # if self.head is not None:
        #     while temp.next != self.head:
        #         print(temp.data)
        #         temp = temp.next
        #     else:
        #         print(temp.data)
            
    

clist = CircularLinkedList()
clist.push(5)
clist.push(6)
clist.push(7)
clist.printlist()
print(clist.countnodes())