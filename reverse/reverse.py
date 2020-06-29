from stack import Stack

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def __repr__(self):
        return f'value: {self.value}'

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, s_=None):
        """
        every node can be added to a stack and then removed one by one and links set up
        """
        if self.head is None:
            return

        if self.head.next_node is None:
            return

        if s_ is None:
            s_ = Stack()
        
        current = node

        while current.next_node is not None:
            s_.push(current)
            current = current.next_node

        s_.push(current)

        self.head = s_.pop()
        node_2 = s_.pop()
        self.head.next_node = node_2

        new_current = node_2

        while s_.size > 0:
            node = s_.pop()
            new_current.next_node = node
            new_current = node

        new_current.next_node = s_.pop()

    def __repr__(self):
        ll_rep = list()
        curr = self.head

        if self.head is None:
            return '[]'

        while curr.next_node:
            ll_rep.append(curr.value)
            curr = curr.next_node

        ll_rep.append(curr.value)

        return f'{ll_rep}'
