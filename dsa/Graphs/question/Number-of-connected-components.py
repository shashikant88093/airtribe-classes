# https://www.geeksforgeeks.org/problems/number-of-provinces/1



# =============================== only count the componnent =================================================


# V = 5

# edges = [[0,1],[2,1],[3,4]]


# def helper(src,graphs,vis):
#     vis[src] = True

#     for nbr in graphs[src]:
#         if not vis[nbr]:
#             helper(nbr,graphs,vis)


# def countConnected(V,edges):

#     graphs = [[] for _ in range(V)]

#     print(graphs)

#     for u,v in edges:
#         graphs[u].append(v)
#         graphs[v].append(u)


#     print(graphs)

#     vis = [False] * V
#     count = 0
#     for i in range(V):
#         if vis[i] == False:
#             count +=1
#             helper(i,graphs,vis)
#     return count


# print(countConnected(V,edges))

# ==================================== Print the created component also ==================================================

V = 5
edges = [[0, 1], [2, 1], [3, 4]]


def helper(src, graphs, vis, current_component):
    vis[src] = True
    current_component.append(src)  # Add this kid to the group list

    for nbr in graphs[src]:
        #  checking vis list False if not then break don't run helper
        if not vis[nbr]:
            helper(nbr, graphs, vis, current_component)


def countConnected(V, edges):
    graphs = [[] for _ in range(V)]

    for u, v in edges:
        graphs[u].append(v)
        graphs[v].append(u)

    vis = [False] * V
    all_components = []  # Stores all groups

    for i in range(V):
        if not vis[i]:
            current_component = []  # Start a fresh bucket for a new group
            helper(i, graphs, vis, current_component)
            all_components.append(current_component)

    # Print each component
    print(f"Total Components (Count): {len(all_components)}")
    for idx, comp in enumerate(all_components, start=1):
        print(f"Component {idx}: {comp}")

    return len(all_components)


countConnected(V, edges)