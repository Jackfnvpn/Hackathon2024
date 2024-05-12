class Node:
    def __init__(self, e) -> None:
        self.element = e
        self.next = None


class Pila:
    def __init__(self):
        self.testa = None
        self.size = 0

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def push(self, e):
        new_node = Node(e)
        new_node.next = self.testa
        self.testa = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Pila vuota"
        element = self.testa.element
        temp_pointer = self.testa
        self.testa = self.testa.next
        self.size -= 1
        del temp_pointer
        return element

    def top(self):
        if self.isEmpty():
            return "Pila vuota"
        element = self.testa.element
        return element
