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

    def reverse_list(self, node, prev):
        # Length of 0
        if self.head is None:
            return None
        # Length of 1
        if self.head.get_next() is None:
            return
        # Length of 2+
        else:
            curr_node = node
            prev_node = prev
            next_node = node.get_next()

            while next_node.get_next() is not None:
                curr_node.set_next(prev_node)
                prev_node = curr_node
                curr_node = next_node
                next_node = curr_node.get_next()

            curr_node.set_next(prev_node)
            self.head = next_node
            self.head.set_next(curr_node)
