from node import Node


class Edge:
    def __init__(self, from_node, to_node, type_label):
        if not isinstance(from_node, Node):
            raise TypeError("from node is not an instance of Node class")
        if not isinstance(to_node, Node):
            raise TypeError("to node is not an instance of Node class")
        self.from_node = from_node
        self.to_node = to_node
        self.type_label = type_label

    def __str__(self):
        return self.type_label

    def __repr__(self):
        return u"Edge " + self.type_label + ": " + repr(self.from_node) + " -> " + repr(self.to_node)

