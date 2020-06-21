from directory_api import get_users
from graph import Graph
from utils import read_resource_permissions, get_resource_hierarchy, get_resources_from_identity, \
    get_identities_from_resource

if __name__ == "__main__":
    resource_data_list = read_resource_permissions("./data.json")
    graph = Graph()
    for resource_data in resource_data_list:
        graph.update_resource(resource_data)

    resource_unique_id = "folders/188906894377"
    member_id = "user:ron@test.authomize.com"
    task_2 = get_resource_hierarchy(graph, resource_unique_id)
    task_3 = get_resources_from_identity(graph, member_id)
    task_4 = get_identities_from_resource(graph, resource_unique_id)
    # task_5 = get_users()  # fails due to not permitted



