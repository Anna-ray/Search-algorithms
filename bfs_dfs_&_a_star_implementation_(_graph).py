# -*- coding: utf-8 -*-
"""BFS DFS & A star implementation ( graph).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pnyYXoqjMrnQajNez2VccPJs5s_i3n7L
"""

#########################################################
# on commence avec la declaration de graphe ou bien ici en va decrire le graphe
graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}


######################################################
# ici on va creer une fonction pour implementer l'algo dfs
def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n, visited)
    return visited

visited = dfs(graph1,'A', [])
print(visited)

############################################################
# ici on va creer une fonction pour implementer l'algo bfs
def bfs(graph,node, visited):
#noeud visité = visited  et fils ou bien la fin de graphe = queue
    visited=[]
    queue=[]    
    visited.append(node)
    queue.append(node)
# append pour ajouter un noeud a l'ensemble, et pop pour prend le "item" specifié    
    while queue:
        s=queue.pop(0)
        
        for x in graph[s]:
            if x not in visited:
                visited.append(x)
                queue.append(x)
    return visited

visited = bfs(graph1,'A', [])
print(visited)
#########################################################################################
# ici on va creer une fonction pour implementer l'algo A* avec l'utilisation du l'heuristique 
import heapq
# cette lib pour implementer  l'algorithm de la priorité des "queues"
def astar(graph,start_node,end_node):
    # astar: F=G+H, F = f_distance, G = g_distance, 
    # H c'est l'heuristique
    f_distance={node:float('inf') for node in graph1}
    f_distance[start_node]=0
    
    g_distance={node:float('inf') for node in graph1}
    g_distance[start_node]=0
    
    came_from={node:None for node in graph1}
    came_from[start_node]=start_node
    
    queue=[(0,start_node)]

    while queue:

        current_f_distance,current_node=heapq.heappop(queue)

        if current_node == end_node:

            print('found the end_node')

            return f_distance, came_from
            
        for next_node,weights in graph1[current_node].items():
# la distance temporaire g quand en calcule a star avec les poids aussi 
            temp_g_distance=g_distance[current_node]+weights[0]
# quand en faire la comparaison pour en prend le min des distance 
            if temp_g_distance<g_distance[next_node]:

                g_distance[next_node]=temp_g_distance
# heristique h 
                heuristic=weights[1]

                f_distance[next_node]=temp_g_distance+heuristic

                came_from[next_node]=current_node
                
                heapq.heappush(queue,(f_distance[next_node],next_node))
                return f_distance, came_from

astar(graph1,'A','S')