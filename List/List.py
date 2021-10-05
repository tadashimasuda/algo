from typing import Any

class Node(object):

    def __init__(self,data:Any,next_node = None):
        self.data = data
        self.next = next_node


class LinkedList(object):
    def __init__(self,head=None) ->None:
        self.head = head

    def append(self,data: Any):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def insert(self,data:Any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return new_node

    def print(self)->None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self,data:Any):
        currnet_node =self.head
        if currnet_node and currnet_node.data == data:
            self.head = currnet_node.next
            currnet_node = None
            return

        prev_node = None
        while currnet_node and currnet_node.data != data:
            prev_node = currnet_node
            currnet_node = currnet_node.next

        if currnet_node is None:
            return

        prev_node.next = currnet_node.next
        currnet_node = None

if __name__ == "__main__":
    l =LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.print()
    l.remove(2)
    l.print()