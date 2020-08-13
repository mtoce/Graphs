from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    # instantiate Graph
    graph = Graph()
    # instantiate empty list to hold the paths
    paths = []
    # loop through the parent, child pair (tuple) in ancestors
    for parent, child in ancestors:
        # if the parent is not in the graph.vertices attribute
        if parent not in graph.vertices:
            # add_vertex parent to graph
            graph.add_vertex(parent)
        # if the child is not in the graph.vertices attribute
        if child not in graph.vertices:
            # add_vertex parent to graph
            graph.add_vertex(child)
        # add_edge connecting parent and child in the graph
        graph.add_edge(parent, child)

    # loop through the vertices in the vertices attribute
    for vertex in graph.vertices:
        # set the path equal to the DFS of the vertex and starting_node
        path = graph.dfs(vertex, starting_node)
        # if the path exists
        if path:
            # append it to the paths empty list
            paths.append(path)

    # if length of path is 1 the vertex has no ancestor in the graph
    if len(paths) == 1:
        # so return -1
        return -1
    # else (otherwise), there are ancestors
    else:
        # first_path variable as the 0 index in paths
        first_path = paths[0]
        # for a path in paths, loop through them
        for path in paths:
            # if the len of the specified path is greater than the len of the
            # first_path
            if len(path) > len(first_path):
                # replace, save over the first_path with the specified path
                first_path = path
        # return the first_path at the 0 index
        return first_path[0]


## CHECK:
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), 
                  (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 1)