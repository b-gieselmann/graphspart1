from graph_interfaces import IEdge, IGraph, IVertex
from typing import Dict, List, Optional

# Implementation definitions
# You should implement the bodies of the methods required by the interface protocols.


# graph class kind of done?
class Graph(IGraph):
    def __init__(self):
        self._vertices: List[IVertex] = []

    def get_vertices(self) -> List[IVertex]:
        return self._vertices
    
    def get_edges(self) -> List[IEdge]:
        edge_list = []
        for vertex in self.get_vertices():
            for edge in vertex.get_edges():
                edge_list.append(edge)
            # [edge for edge in vertex.get_edges()]
        return edge_list
    
    def add_vertex(self, vertex: IVertex) -> None:
        # Should the method check that a vertex doesn't already exist?
        self._vertices.append(vertex)
        return
    
    def remove_vertex(self, vertex_name: str) -> None:
        for vertex in self._vertices:
            if vertex.get_name() == vertex_name:
                self._vertices.remove(vertex)
        return

    # Brooke's special add_edge that knows where to put the edge.
    def add_edge(self, source_name: str, dest_name: str, name: str, weight: float) -> None:
        # 1. Find the vertex from object reference
        # 2. Find the vertex to object reference
        source_vertex: Optional[IVertex] = None
        dest_vertex: Optional[IVertex] = None

        for vertex in self._vertices:
            if vertex.get_name() == source_name:
                source_vertex = vertex

            if vertex.get_name() == dest_name:
                dest_vertex = vertex
                
        
        if source_vertex is None or dest_vertex is None:
            raise Exception("One or more of the vertexes do not exist")

        #NOT AN ERROR
        #PYTHON SHOULD SHUT THE FUCK UP
        the_edge = Edge(name, dest_vertex, weight)
        source_vertex.add_edge(the_edge)


        
        pass

        # self._adj_list: Dict[str, List[str]] = {}

        # # Preallocated
        # self._adj_matrix_prepopulated:List[List[int]] = [[int()] * graph.VERTEX_COUNT] * graph.VERTEX_COUNT

        # # Run time allocation
        # self._adj_matrix_dynamic: List[List[int]] = [[]]

    def remove_edge(self, edge_name: str) -> None:
        # should remove edge should remove all edges with that name? 
        # Otherwise it will just remove the first instance it finds without any ability to choose which one.
        # this is not efficient. Fix later. This should ideally remove all instances with that name though.
        for vertex in self.get_vertices():
            for edge in vertex.get_edges():
                if edge.get_name() == edge_name:
                    vertex.remove_edge(edge_name)
        return

    def check_vertex_obj_in_graph(self, vertex: IVertex) -> bool:
        vertex_name = vertex.get_name()
        return self.check_vertex_name_in_graph(vertex_name)
    
    def check_vertex_name_in_graph(self, vertex_name: str) -> bool:
        for i in self.get_vertices():
            if i.get_name() == vertex_name:
                return True
        return False

# Vertex class all done
class Vertex(IVertex):
    def __init__(self, name: str) -> None:
        self._name: str = name
        self._edges: List[IEdge] = []
        self._visited = False

    def get_name(self) -> str:
        return self._name
    
    def set_name(self, name: str) -> None:
        self._name = name
        return
    
    def add_edge(self, edge: IEdge) -> None:
        self._edges.append(edge)
        return
    
    def remove_edge(self, edge_name: str) -> None:
        for edge in self._edges:
            if edge.get_name() == edge_name:
                self._edges.remove(edge)
        return
    
    def get_edges(self) -> List[IEdge]:
        return self._edges
    
    def set_visited(self, visited: bool) -> None:
        self._visited = visited
    
    def is_visited(self) -> bool:
        return self._visited
    
    def check_edge_obj_in_vertex(self, edge: IEdge):
        for i in self.get_edges():
            if i.get_name() == edge.get_name():
                if i.get_destination().get_name() == edge.get_destination().get_name():
                    return True
        return False
    
    def check_edge_name_dest_in_vertex(self, edge_name: str, dest_name: str):
        for i in self.get_edges():
            if i.get_name() == edge_name:
                if i.get_destination().get_name() == dest_name:
                    return True
        return False

    def check_edge_to_dest_in_vertex(self, dest_name: str):
        for i in self.get_edges():
            if i.get_destination().get_name() == dest_name:
                return True
        return False

# Edge class all done       
class Edge(IEdge):
    def __init__(self, name: str, destination: Vertex, weight: float = 1) -> None:
        self._name: str = name
        #self._destination: Optional[IVertex] = destination
        self._destination: IVertex = destination
        self._weight = weight
        self._is_bi_directional: bool = False

        self._weight = weight
        return
    
    def get_name(self) -> str:
        return self._name
    
    def set_name(self, name: str) -> None:
        self._name = name
        return
    
    def get_destination(self) -> IVertex:
        return self._destination
    
    def get_weight(self) -> float:
        return self._weight
    
    def set_weight(self, weight: float) -> None:
        self._weight = weight
        return