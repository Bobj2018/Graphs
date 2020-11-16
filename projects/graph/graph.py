"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # Initialize a queue
        q = Queue()
        # Make a set to track visted nodes
        visted = set()
        # enqueue the starting node

        q.enqueue(starting_vertex)

        while q.size() > 0:
            current_node = q.dequeue()

            if current_node not in visted:
                print(current_node)
                visted.add(current_node)
                neigbors = self.get_neighbors(current_node)

                for neigbor in neigbors:
                    q.enqueue(neigbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Initialize a stack
        s = Stack()
        # Make a set to track visted nodes
        visted = set()
        # push the starting node

        s.push(starting_vertex)

        while s.size() > 0:
            current_node = s.pop()

            if current_node not in visted:
                print(current_node)
                visted.add(current_node)
                neigbors = self.get_neighbors(current_node)

                for neigbor in neigbors:
                    s.push(neigbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
    # Initialize a queue
        q = Queue()
        q.enqueue([starting_vertex])
        # Make a set to track visted nodes
        visted = set()
        # enqueue the starting node

        while q.size() > 0:
            current_path = q.dequeue()
            current_node = current_path[len(current_path) - 1]

            if current_node not in visted:
                # CHECK IF NODE IS DESITINATION
                # IF IT IS, RETURN
                if current_node == destination_vertex:
                    return current_path
                visted.add(current_node)
                neigbors = self.get_neighbors(current_node)

                for neigbor in neigbors:
                    path = current_path.copy()
                    path.append(neigbor)
                    q.enqueue(path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        # Make a set to track visted nodes
        visted = set()
        # enqueue the starting node

        while s.size() > 0:
            current_path = s.pop()
            current_node = current_path[len(current_path) - 1]

            if current_node not in visted:
                # CHECK IF NODE IS DESITINATION
                # IF IT IS, RETURN
                if current_node == destination_vertex:
                    return current_path
                visted.add(current_node)
                neigbors = self.get_neighbors(current_node)

                for neigbor in neigbors:
                    path = current_path.copy()
                    path.append(neigbor)
                    s.push(path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
