# -*- coding: utf-8 -*-

# graph
graph = {
    'A' : ['B', 'C', 'D'],
    'B' : ['E', 'F'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []
}

#initilaizing queue and visiting nodes arrays
visited=[]
queue=[]

#function for bfs
def bfs(visited, graph, root):
    visited.append(root)
    queue.append(root)

    #till the queue is not empty run the loop
    while queue:
      m=queue.pop(0)
      print(m, end=" ")

      #check for the neighbours and insert into arrays if not present
      for neighbour in graph[m]:
        if neighbour not in visited:
          visited.append(neighbour)
          queue.append(neighbour)

#display the traversal
print("BFS for given graph is:")
bfs(visited, graph, 'A')

