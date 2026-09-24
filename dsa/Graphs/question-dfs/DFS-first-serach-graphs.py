# https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

dj = [[2, 3, 1], [0], [0, 4], [0], [2]]

def helper(i,adjency,visited,output):
    visited[i]= True
    output.append(i)  # Add this kid to the group list
    
    for nbr in adjency[i]:
        if not visited[nbr]:
            helper(nbr,adjency,visited,output)

def dfs(adjency):

    visited = [False] * len(adjency)

    print(visited)
    output = []
    for i in range(len(visited)):
        if visited[i] == False:
            helper(i,adjency,visited,output)
            print(output)
            # output.append()


print(dfs(dj))