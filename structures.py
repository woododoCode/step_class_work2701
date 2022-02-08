#  a = [1, 2, 3]
#  1 in a
class Node:
    __slots__ = ('value', 'prev_node', 'next_node')

    def __init__(self, value=None):
        self.value = value
        self.prev_node = None
        self.next_node = None

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return f"{self.value}"


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next_node
        nodes.append('None')
        return ' ==> '.join(nodes)

    def add_at_start(self, value):
        if self.head is None:
            node = Node(value)
            self.head = node
        else:
            new_node = Node(value)
            self.head.prev_node = new_node
            new_node.next_node = self.head
            self.head = new_node

    def insert_in_the_end(self, value):
        new_node = Node(value)
        temp: Node = self.head
        while temp.next_node is not None:
            temp = temp.next_node
        temp.next_node = new_node
        new_node.prev_node = temp


ll = LinkedList()
for i in range(4, 0, -1):
    ll.add_at_start(i)


print(ll)
ll.insert_in_the_end(16)
ll.insert_in_the_end(1231)
ll.insert_in_the_end(124)
ll.insert_in_the_end('qggdf')
ll.insert_in_the_end(1233)
print(ll)
