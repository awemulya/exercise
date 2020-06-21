import json

from graph import Graph


def get_resource_hierarchy(graph, folder_id):
    node = graph.search_node(folder_id)
    if node:
        return graph.predecessors[node.identity]
    return []


def get_resources_from_identity(graph, member_id):
    resources = []
    edges = [e for e in graph.edges if e.to_node.identity == member_id]
    for edge in edges:
        resources.append((edge.from_node.identity, edge.from_node.type_label, edge.type_label,))
    return resources


def get_identities_from_resource(graph, resource_id):
    identities = []
    edges = [e for e in graph.edges if e.from_node.identity == resource_id]
    for edge in edges:
        identities.append((edge.to_node.identity, edge.type_label,))
    return identities


def read_resource_permissions(file_path):
    data_list = []
    with open(file_path, 'r') as json_file:
        json_list = list(json_file)
    for json_str in json_list:
        data_list.append(json.loads(json_str))
    return data_list


def get_user_permissions(graph, user_email):
    if not isinstance(graph, Graph):
        raise TypeError("graph is not an instance of Graph")
    if not isinstance(user_email, str):
        raise TypeError("user_email is not an instance of str")
    pass
