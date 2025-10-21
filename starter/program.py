from typing import Optional
from graph_interfaces import IGraph, IVertex
from graph_impl import Graph, Vertex, Edge     

def read_graph(file_path: str) -> IGraph:  
    """Read the graph from the file and return the graph object"""
    graph_file = open(file_path, "r")
    condition = False

    map_graph = Graph()

    graph_file.readline()

    while condition == False:
        current_line = graph_file.readline()
        if current_line == "":
            condition = True
            break
        source, destination, highway, distance = current_line.rsplit(",")

        source_in_graph = map_graph.check_vertex_name_in_graph(source)
        dest_in_graph = map_graph.check_vertex_name_in_graph(destination)

        if source_in_graph == False:
            map_graph.add_vertex(Vertex(source))
        
        if dest_in_graph == False:
            map_graph.add_vertex(Vertex(destination))

        map_graph.add_edge(source, destination, highway, float(distance))
    
    return map_graph


def print_dfs(graph: IGraph, start_vertex: IVertex) -> None: 
    """Print the DFS traversal of the graph starting from the start vertex"""
    stack = []
    stack.append(start_vertex)

    print("DEPTH FIRST:")
    
    while len(stack) > 0:
        vertex = stack.pop()
        if vertex.is_visited() == False:
            print(vertex.get_name())
            vertex.set_visited(True)
            for edge in vertex.get_edges():
                stack.append(edge.get_destination())

    for vertex in graph.get_vertices():
        vertex.set_visited(False)

    return

def print_bfs(graph: IGraph, start_vertex: IVertex) -> None: 
    """Print the BFS traversal of the graph starting from the start vertex"""
    for vertex in graph.get_vertices():
        vertex.set_visited(False)
    queue = []
    queue.insert(0, start_vertex)

    print("BREADTH FIRST:")


    while len(queue) > 0:
        vertex = queue.pop()
        if vertex.is_visited() is False:
            print(vertex.get_name())
            vertex.set_visited(True)
            for edge in vertex.get_edges():
                queue.insert(0, edge.get_destination())
    
    for vertex in graph.get_vertices():
        vertex.set_visited(False)

    return


def main() -> None:
    graph: IGraph = read_graph("graph.txt")
    start_vertex_name: str  = input("Enter the start vertex name: ")

    # Find the start vertex object
    start_vertex: Optional[IVertex]= next((v for v in graph.get_vertices() if v.get_name() == start_vertex_name), None)

    if start_vertex is None:
        print("Start vertex not found")
        return
    
    print_dfs(graph, start_vertex)
    print_bfs(graph, start_vertex)


if __name__ == "__main__":
    main()