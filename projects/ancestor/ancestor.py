
def earliest_ancestor(ancestors, starting_node):

    # set up family tree
    lookup = {}
    # ancestors contains a list of tuple pairs -> (parent, child)
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        if child not in lookup:
            lookup[child] = [parent]
        else:
            lookup[child].append(parent)
        print(f"Lookup: {lookup}")

    # DFT recurse through the nodes to get to the last generation
    def recurse(graph, vertex):
        # endpoints: nowhere left to go
        print(f"Vertex: {vertex}")
        if vertex not in graph:
            return (1, vertex)
        # work: do nothing
        # recurse: get ancestors thru recursing
        ancestors = []
        for val in graph[vertex]:
            ancestors.append(recurse(graph, val))
        print(f"Ancestors: {ancestors}")

        # get oldest ancestor otherwise smallest ID, pass it on

        # only one ancestor
        if len(ancestors) == 1:
            return (ancestors[0][0] + 1, ancestors[0][1])
            
        # two ancestors, compare them
        if ancestors[0][0] > ancestors[1][0]:
            return (ancestors[0][0] + 1, ancestors[0][1])
        elif ancestors[0][0] < ancestors[1][0]:
            return (ancestors[1][0] + 1, ancestors[1][1])
        else:
            # same age, return lowest ID
            if ancestors[0][1] < ancestors[1][1]:
                return (ancestors[0][0] + 1, ancestors[0][1])
            else:
                return (ancestors[1][0] + 1, ancestors[1][1])

    # get earliest ancestor and deal with cases where
    # the one picked is the earliest ancestor
    earliest = recurse(lookup, starting_node)
    if earliest[0] == 1:
        return -1
    else:
        return earliest[1]

if __name__ == "__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    earliest_ancestor(test_ancestors, 6)