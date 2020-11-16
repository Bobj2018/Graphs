from util import Stack, Queue

def earliest_ancestor(ancestors, starting_node):
    graph = {}

    #Create a graph staring from the bottom
    for item in ancestors:
        if item[1] not in graph:
            graph[item[1]] = {item[0]}
        else:
            graph[item[1]].add(item[0])

    #Travserse through the graph and save each path,
    #find the longest path, if same lenght, find smaller number
    return -1
       

if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    earliest_ancestor(test_ancestors, 6)