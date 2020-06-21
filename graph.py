from edge import Edge
from node import Node


class Graph:
    def __init__(self,  edges=None, nodes=None):
        self.edges = [] if edges is None else edges
        self.nodes = [] if nodes is None else nodes
        self.predecessors = {}
        self.successors = {}

    def add_node(self, node):
        if not isinstance(node, Node):
            raise TypeError("node is not an instance of Node class")
        if self.search_node(node.identity) is None:
            self.nodes.append(node)

    def add_edge(self, edge):
        if not isinstance(edge, Edge):
            raise TypeError("edge is not an instance of Edge class")
        if self.search_edge(edge) is None:
            self.edges.append(edge)

    def search_node(self, identity):
        node = [n for n in self.nodes if n.identity == identity]
        if node:
            return node[0]
        return None

    def search_edge(self, edge):

        edges = [e for e in self.edges if (
                e.from_node == edge.from_node
                and e.to_node == edge.to_node
                and e.type_label == edge.type_label)]

        if edges:
            return edges[0]
        return None

    def update_resource(self, resource_data):
        name = resource_data['name']
        length_name = len(name.split("/"))
        ancestors = resource_data['ancestors'][1:]  # exclude self
        first_ancestor = None
        if ancestors:
            first_ancestor = ancestors[0]  # first parent
        identity = "/".join(name.split("/")[length_name - 2:])
        asset_type = resource_data['asset_type'].split("/")[-1]
        if first_ancestor:  # maintain direct successors of first parent
            node_resource_first_ancestor = Node(asset_type, first_ancestor)
            self.add_node(node_resource_first_ancestor)
            if node_resource_first_ancestor.identity not in self.successors:
                self.successors[node_resource_first_ancestor.identity] = []
            self.successors[node_resource_first_ancestor.identity].append(identity)
        node_resource = Node(asset_type, identity)
        self.add_node(node_resource)
        self.predecessors[node_resource.identity] = ancestors
        bindings_data = resource_data['iam_policy']['bindings']
        for binding_data in bindings_data:
            type_label = binding_data['role'].split("/")[-1]
            members = binding_data['members']
            for member in members:
                node_member = Node("Member", member)
                self.add_node(node_member)
                edge = Edge(node_resource, node_member, type_label)
                self.add_edge(edge)

