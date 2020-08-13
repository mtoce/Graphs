"""
Simple graph implementation
"""
from util import Stack, Queue

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            # # adding this makes the edges and nodes bidirectional in nature
            # self.vertices[v2].add(v1)
        else:
            raise IndexError("nonexistent vertex")

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
        # instantiate Queue
        q = Queue()
        # make a set to track if we've been here before
        visited = set()
        # enqueue the starting node
        q.enqueue(starting_vertex)
        # while our queue is not empty
        while q.size() > 0:
            # dequeue whatever is at the front of our line, 
            # this is our current node
            current_node = q.dequeue()
            # if we haven't visited this node yet,
            if current_node not in visited:
                # print current node
                print(current_node)
                # mark as visited
                visited.add(current_node)
                # get its neighbors
                neighbors = self.get_neighbors(current_node)
                # loop through each of the neighbors
                for neighbor in neighbors:
                    # add to queue
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        DFT is the same as BFT just using a Stack
        instead of a Queue.
        """
        # make a stack
        s = Stack()
        # make a set to track if we've been here before
        visited = set()
        # push on our starting node
        s.push(starting_vertex)
        # while our stack is not empty
        while s.size() > 0:
            # pop off whatever is on top, this is the current node
            current_node = s.pop()
            # if we haven't visited this node yet,
            if current_node not in visited:
                # print
                print(current_node)
                # mark as visited
                visited.add(current_node)
                # get its neighbors
                neighbors = self.get_neighbors(current_node)
                # for each of the neighbors
                for neighbor in neighbors:
                    # add to stack
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # if not visited
        if not visited:
            # instantiate set variable visited
            visited = set()
        # if starting_vertex not in visited
        if starting_vertex not in visited:
            # mark this vertex as visited
            visited.add(starting_vertex)
            # print starting_vertex
            print(starting_vertex)
            neighbors = self.get_neighbors(starting_vertex)
            # for each neighbor
            for neighbor in neighbors:
                # recurse on the neighbor
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # instantiate a Queue
        q = Queue()
        # make a set to track if we've been here before
        visited = set()
        # enqueue starting node
        q.enqueue([starting_vertex])
        # while our queue is not empty
        while q.size() > 0:
            path = q.dequeue()
            current_node = path[-1]
            # if we haven't visited this node yet,
            if current_node not in visited:
                # print current node
                print(current_node)
                # mark as visited
                visited.add(current_node)
                # check if the node equals the target
                if current_node == destination_vertex:
                    # if so, return the path
                    return path
                # return neighbors
                neighbors = self.get_neighbors(current_node)
                # loop through the neighbor in neighbors
                for neighbor in neighbors:
                    # new_path equal a list of path
                    new_path = list(path)
                    # append the neighbor to new_path
                    new_path.append(neighbor)
                    # enqueue new_path
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # instantiate a Stack
        s = Stack()
        # make a set to track if we've been here before
        visited = set()
        # enqueue starting node
        s.push([starting_vertex])
        # while our stack is not empty
        while s.size() > 0:
            path = s.pop()
            current_node = path[-1]
            # if we haven't visited this node yet,
            if current_node not in visited:
                # print current node
                print(current_node)
                # mark as visited
                visited.add(current_node)
                # check if the node equals the target
                if current_node == destination_vertex:
                    return path
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        # mark our node as visited
        if not visited:
            # instantiate visited set
            visited = set()
        # if no path
        if not path:
            # instantiate empty list for the path
            path = []
        # add the starting_vertex to the visited set
        visited.add(starting_vertex)
        # if the starting_vertex == destination_vertex
        if starting_vertex == destination_vertex:
            # return the path
            return path
        # if the len(path) == 0
        if len(path) == 0:
            # append the starting_vertex to path since that is the only vertex
            # in that specified path
            path.append(starting_vertex)
        # instantiate neighbors variable
        neighbors = self.get_neighbors(starting_vertex)
        # loop through the neighbor in neighbors
        for neighbor in neighbors:
            # if the neight not in visited
            if neighbor not in visited:
                # instantiate new_path
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path + [neighbor])
                # if new_path
                if new_path:
                    # return new_path
                    return new_path


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